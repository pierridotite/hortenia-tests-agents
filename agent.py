"""Agents IA qui utilisent Hortenia sur un téléphone virtuel Android.

Chaque persona a un profil et un but. A chaque pas, l'agent reçoit une
capture d'écran et la liste des éléments visibles, choisit un geste
(toucher, écrire, faire défiler, retour) et note ce qui cloche. Le script
surveille en parallèle les plantages (logcat) et la sortie de l'app.

Variables d'environnement :
  GEMINI_API_KEY  clé de l'API Gemini (obligatoire)
  PERSONAS        ids séparés par des virgules (vide = tous)
  PAS_MAX         gestes maximum par persona (30 par défaut)
  RUN_ID          identifiant du lancement, sert aux adresses e-mail
  PAQUET          paquet Android (com.hortenia.app par défaut)
"""
import base64, io, json, os, re, subprocess, sys, time, unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

from openai import OpenAI, RateLimitError, APIStatusError
from PIL import Image

PAQUET = os.environ.get("PAQUET", "com.hortenia.app")
PAS_MAX = int(os.environ.get("PAS_MAX", "30"))
RUN_ID = os.environ.get("RUN_ID", str(int(time.time())))
# Chaque modèle a son propre quota gratuit : on passe au suivant dès qu'un
# modèle répond 429, et on le remet en service une minute plus tard.
MODELES = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]
ECART_APPELS = 2.0
SORTIE = Path("resultats")
RACINE = Path(__file__).parent

client = OpenAI(api_key=os.environ["GEMINI_API_KEY"], timeout=60, max_retries=0,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
dernier_appel = [0.0]
repos_jusqua = {m: 0.0 for m in MODELES}


# ---------- adb ----------

def adb(*args, binaire=False, timeout=60):
    r = subprocess.run(["adb", *args], capture_output=True, timeout=timeout)
    return r.stdout if binaire else r.stdout.decode("utf-8", "replace")


def capture():
    png = adb("exec-out", "screencap", "-p", binaire=True)
    return Image.open(io.BytesIO(png)).convert("RGB")


def elements_ecran():
    """Éléments visibles (texte, description, cliquable) avec leur centre."""
    adb("shell", "uiautomator", "dump", "/sdcard/ui.xml", timeout=30)
    xml = adb("exec-out", "cat", "/sdcard/ui.xml")
    try:
        racine = ET.fromstring(xml[xml.find("<"):])
    except ET.ParseError:
        return []
    liste = []
    for n in racine.iter("node"):
        texte = (n.get("text") or "").strip()
        desc = (n.get("content-desc") or "").strip()
        cliquable = n.get("clickable") == "true"
        saisie = n.get("class", "").endswith("EditText")
        if not (texte or desc or cliquable or saisie):
            continue
        m = re.findall(r"\d+", n.get("bounds", ""))
        if len(m) != 4:
            continue
        x1, y1, x2, y2 = map(int, m)
        if x2 - x1 < 8 or y2 - y1 < 8:
            continue
        liste.append({
            "id": len(liste), "texte": texte[:80], "description": desc[:80],
            "cliquable": cliquable, "champ_saisie": saisie,
            "x": (x1 + x2) // 2, "y": (y1 + y2) // 2,
        })
    return liste[:70]


def app_au_premier_plan():
    sortie = adb("shell", "dumpsys", "activity", "activities")
    m = re.search(r"(mResumedActivity|topResumedActivity)[^\n]*", sortie)
    return (m.group(0) if m else ""), (PAQUET in (m.group(0) if m else ""))


def lancer_app(effacer=True):
    if effacer:
        adb("shell", "pm", "clear", PAQUET)
        for p in ("POST_NOTIFICATIONS", "ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION", "CAMERA"):
            adb("shell", "pm", "revoke", PAQUET, f"android.permission.{p}")
    adb("shell", "monkey", "-p", PAQUET, "-c", "android.intent.category.LAUNCHER", "1")
    time.sleep(8)


def sans_accents(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()


def vider_champ():
    adb("shell", "input", "keyevent", "KEYCODE_MOVE_END")
    adb("shell", "input", "keyevent", *(["67"] * 40))


def ecrire(texte):
    t = sans_accents(texte)
    # input text ne gère ni les espaces ni certains caractères spéciaux
    t = re.sub(r"([\\'\"`$&|;<>()*~#])", r"\\\1", t).replace(" ", "%s")
    adb("shell", "input", "text", t)


def glisser(direction, l, h):
    cx, cy = l // 2, h // 2
    d = {"haut": (cx, int(h * .75), cx, int(h * .3)), "bas": (cx, int(h * .3), cx, int(h * .75)),
         "gauche": (int(l * .85), cy, int(l * .15), cy), "droite": (int(l * .15), cy, int(l * .85), cy)}
    x1, y1, x2, y2 = d.get(direction, d["haut"])
    adb("shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), "350")


def erreurs_logcat():
    """Nouvelles erreurs depuis le dernier appel (plantages natifs et JS)."""
    txt = adb("logcat", "-d", "-v", "brief", "AndroidRuntime:E", "ReactNativeJS:E", "ReactNative:E", "*:S")
    txt += adb("logcat", "-d", "-b", "crash")
    adb("logcat", "-c")
    lignes = [l for l in txt.splitlines() if l.strip() and not l.startswith("---------")]
    return lignes[-40:]


# ---------- modèle ----------

def appeler(messages, json_attendu=True):
    for essai in range(16):
        dispo = [m for m in MODELES if repos_jusqua[m] <= time.time()]
        if not dispo:
            time.sleep(max(1.0, min(repos_jusqua.values()) - time.time()))
            continue
        modele = dispo[0]
        attente = dernier_appel[0] + ECART_APPELS - time.time()
        if attente > 0:
            time.sleep(attente)
        dernier_appel[0] = time.time()
        try:
            r = client.chat.completions.create(
                model=modele, messages=messages, temperature=0.4,
                **({"response_format": {"type": "json_object"}} if json_attendu else {}))
            txt = r.choices[0].message.content or ""
            return json.loads(txt) if json_attendu else txt
        except RateLimitError:
            repos_jusqua[modele] = time.time() + 60
        except APIStatusError as e:
            if getattr(e, "status_code", 0) not in (500, 503):
                raise
            repos_jusqua[modele] = time.time() + 30
        except Exception:  # délai dépassé, réponse coupée, JSON invalide
            repos_jusqua[modele] = time.time() + 20
    raise RuntimeError("modèle indisponible")


CONSIGNES = """Tu joues un vrai utilisateur de l'application mobile Hortenia (potager), sur un téléphone Android.
Profil : {profil}
Ton but : {but}

Règles :
- Agis comme cette personne : sa patience, son aisance avec le numérique, ses attentes. Si quelque chose l'agacerait ou la perdrait, dis-le.
- Ne paie jamais rien, n'accepte aucun achat ni abonnement, ne saisis aucune carte bancaire. Tu peux ouvrir l'écran d'abonnement pour le regarder, puis le fermer.
- Ne publie rien dans la communauté, ne commente pas, ne signale personne, n'envoie aucun avis ni message au support : ce sont de vrais utilisateurs.
- Au plus une question à l'assistant HortenIA et un seul diagnostic photo.
- Pour un compte par e-mail : adresse {email}, mot de passe {mdp}. N'utilise pas Google ni Apple.
- Si une autorisation est demandée (notifications, position), réagis comme la persona le ferait.
- Écrire dans un champ remplace son contenu. Le clavier peut cacher des boutons : l'action "retour" le ferme.
- Si tu refais la même chose sans que l'écran change, signale un "blocage" et essaie autre chose.

A chaque pas tu reçois la capture d'écran et la liste des éléments visibles (id, texte, position).
Réponds uniquement en JSON :
{{"vu": "ce que tu vois, en une phrase",
  "pensee": "ce que la persona pense ou ressent, en une phrase",
  "action": "toucher" | "ecrire" | "defiler" | "retour" | "attendre" | "terminer",
  "element": id de l'élément à toucher ou du champ où écrire (sinon null),
  "x": abscisse en pixels de l'écran si aucun élément ne convient (sinon null), "y": ordonnée (sinon null),
  "texte": texte à écrire (action ecrire),
  "direction": "haut" | "bas" | "gauche" | "droite" (action defiler, haut = voir la suite),
  "probleme": null ou {{"type": "bug" | "blocage" | "confusion" | "lenteur" | "texte" | "design", "gravite": 1 a 3, "description": "précis : écran, ce qui se passe, ce qui était attendu"}},
  "but_atteint": true | false}}
Choisis "terminer" quand le but est atteint ou si la persona abandonnerait, en expliquant pourquoi dans "pensee"."""


def jouer(persona):
    pid = persona["id"]
    dossier = SORTIE / pid
    dossier.mkdir(parents=True, exist_ok=True)
    email = f"success+agent-{pid}-{RUN_ID}@simulator.amazonses.com"
    mdp = f"Potager-{RUN_ID[-6:]}-{pid[:3]}!"
    systeme = CONSIGNES.format(profil=persona["profil"], but=persona["but"], email=email, mdp=mdp)
    journal, historique = [], []
    adb("logcat", "-c")
    lancer_app(effacer=True)
    debut = time.time()
    fin_raison = "pas maximum atteint"
    for pas in range(1, PAS_MAX + 1):
        img = capture()
        l, h = img.size
        img.save(dossier / f"{pas:02d}.png")
        petite = img.resize((l // 3, h // 3))
        tampon = io.BytesIO(); petite.save(tampon, "JPEG", quality=70)
        elements = elements_ecran()
        resume_hist = "\n".join(historique[-8:]) or "(début)"
        messages = [
            {"role": "system", "content": systeme},
            {"role": "user", "content": [
                {"type": "text", "text": f"Pas {pas}/{PAS_MAX}. Écran {l}x{h} px (image réduite au tiers, les positions des éléments et x, y sont en pixels réels).\n"
                                         f"Derniers gestes :\n{resume_hist}\n\nÉléments visibles :\n{json.dumps(elements, ensure_ascii=False)}"},
                {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + base64.b64encode(tampon.getvalue()).decode()}},
            ]},
        ]
        t0 = time.time()
        try:
            d = appeler(messages)
        except RuntimeError:
            fin_raison = "modèle indisponible"
            break
        action = d.get("action")
        el = next((e for e in elements if e["id"] == d.get("element")), None) if d.get("element") is not None else None
        x, y = (el["x"], el["y"]) if el else (d.get("x"), d.get("y"))
        if action == "toucher" and x is not None and y is not None:
            adb("shell", "input", "tap", str(int(x)), str(int(y)))
        elif action == "ecrire":
            if el or (x is not None and y is not None):
                adb("shell", "input", "tap", str(int(x)), str(int(y))); time.sleep(0.6)
            vider_champ()
            ecrire(d.get("texte") or "")
        elif action == "defiler":
            glisser(d.get("direction") or "haut", l, h)
        elif action == "retour":
            adb("shell", "input", "keyevent", "4")
        elif action == "attendre":
            time.sleep(4)
        time.sleep(2.5)
        erreurs = erreurs_logcat()
        activite, dans_app = app_au_premier_plan()
        entree = {"pas": pas, "capture": f"{pas:02d}.png", "secondes_modele": round(time.time() - t0, 1),
                  **{k: d.get(k) for k in ("vu", "pensee", "action", "texte", "direction", "probleme", "but_atteint")},
                  "element": el, "erreurs_logcat": erreurs, "premier_plan": activite}
        if d.get("texte") and mdp in str(d.get("texte")):
            entree["texte"] = "(mot de passe)"
        journal.append(entree)
        historique.append(f"{pas}. {action} {(el['texte'] or el['description']) if el else ''} {entree['texte'] or ''} -> {d.get('pensee', '')}".strip())
        print(f"[{pid}] pas {pas} : {action}", flush=True)
        if any("FATAL EXCEPTION" in e or "beginning of crash" in e for e in erreurs):
            journal[-1]["plantage"] = True
        if not dans_app and "permissioncontroller" not in activite and "packageinstaller" not in activite:
            journal[-1]["hors_app"] = True
            if any(j.get("hors_app") for j in journal[-3:-1]):
                lancer_app(effacer=False)
        (dossier / "journal.json").write_text(json.dumps({"persona": persona, "fin": "en cours", "pas": len(journal), "journal": journal}, ensure_ascii=False, indent=1))
        if action == "terminer":
            fin_raison = "terminé par l'agent" + (" (but atteint)" if d.get("but_atteint") else " (but non atteint)")
            break
    img = capture(); img.save(dossier / "fin.png")
    bilan = {"persona": persona, "fin": fin_raison, "duree_s": round(time.time() - debut), "pas": len(journal), "journal": journal}
    (dossier / "journal.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1))
    return bilan


def synthese(bilans):
    extrait = []
    for b in bilans:
        extrait.append({"persona": b["persona"]["nom"], "but": b["persona"]["but"], "fin": b["fin"],
                        "parcours": [{k: j.get(k) for k in ("pas", "vu", "pensee", "action", "probleme", "plantage", "hors_app")}
                                     | ({"erreurs": j["erreurs_logcat"][:6]} if j.get("erreurs_logcat") else {}) for j in b["journal"]]})
    consigne = ("Tu es testeur QA senior. Voici le parcours d'agents qui ont utilisé l'app Android Hortenia. "
                "Écris en français un rapport Markdown : 1) résumé en 5 lignes ; 2) bugs et plantages, du plus grave au moins grave, "
                "chacun avec persona, numéro de pas (capture), ce qui se passe, ce qui était attendu ; 3) blocages et confusions d'usage ; "
                "4) ce qui a bien marché ; 5) 5 corrections prioritaires. Ne cite que ce qui est dans les journaux, n'invente rien.")
    return appeler([{"role": "system", "content": consigne},
                    {"role": "user", "content": json.dumps(extrait, ensure_ascii=False)}], json_attendu=False)


def main():
    personas = json.loads((RACINE / "personas.json").read_text())
    choix = [p.strip() for p in os.environ.get("PERSONAS", "").split(",") if p.strip()]
    if choix:
        personas = [p for p in personas if p["id"] in choix]
    SORTIE.mkdir(exist_ok=True)
    adb("shell", "settings", "put", "global", "window_animation_scale", "0")
    bilans = []
    for p in personas:
        try:
            bilans.append(jouer(p))
        except Exception as e:  # une persona qui échoue ne doit pas arrêter les autres
            print(f"[{p['id']}] erreur : {type(e).__name__}", flush=True)
            bilans.append({"persona": p, "fin": f"erreur du script : {e}", "pas": 0, "journal": []})
    try:
        (SORTIE / "rapport.md").write_text(synthese(bilans))
    except Exception as e:
        (SORTIE / "rapport.md").write_text(f"Synthèse impossible : {e}")
    (SORTIE / "bilans.json").write_text(json.dumps([{k: b[k] for k in ("fin", "pas")} | {"id": b["persona"]["id"]} for b in bilans], ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
