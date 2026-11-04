"""Outil des testeurs pour la 1.7 : parle à l'onglet « Testeurs » de
hortenia.com/tests (API du serveur Hortenia). Le jeton vient du secret GitHub
TESTS_JETON et l'adresse de TESTS_API : rien de secret dans ce dépôt public.
Aucun mot de passe ni jeton n'est jamais affiché.

  python3 outils/site_tests.py preparer            impose les versions de ta persona (plan_1_7.json) à cet appareil
  python3 outils/site_tests.py versions            versions actives de cet appareil / compte
  python3 outils/site_tests.py imposer T5=B [T25=C]   change une ou plusieurs versions
  python3 outils/site_tests.py date 2027-03-01     impose une date (« aucune » pour revenir à aujourd'hui) ; relance l'app ensuite
  python3 outils/site_tests.py compte plus|email   identifiants d'un compte de test (Plus actif pour « plus »)
  python3 outils/site_tests.py evenements [20]     derniers événements de cet appareil / compte
  python3 outils/site_tests.py envoyer <notification>   « Envoyer maintenant » (comptes de test seulement)
  python3 outils/site_tests.py apercu <message> [version] [cle=valeur…]   aperçu d'un message
  python3 outils/site_tests.py simuler <action> [cle=valeur…]   situation de test (filleul, publication-proche, question, alerte, absence, semaine-factice…)
  python3 outils/site_tests.py stats               chiffres publics (/stats/publiques)
  python3 outils/site_tests.py liste               notifications, messages et actions que le serveur accepte
L'appli reprend les versions et la date à son lancement suivant : relance-la après « preparer », « imposer » ou « date »."""
import json, os, subprocess, sys, urllib.request, urllib.error

API = os.environ.get("TESTS_API", "").rstrip("/")
JETON = os.environ.get("TESTS_JETON", "")
ETAT = "resultats/.site_tests.json"
PERSONA = (os.environ.get("PERSONAS") or "").split(",")[0].strip()


def appareil():
    if os.environ.get("UDID"):
        return {"plateforme": "ios", "modele": os.environ.get("APPAREIL", ""), "udid": os.environ["UDID"]}
    m = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
    a = subprocess.run(["adb", "shell", "getprop", "ro.build.version.sdk"], capture_output=True, text=True).stdout.strip()
    return {"plateforme": "android", "modele": m, "api": a}


def etat():
    try:
        return json.load(open(ETAT))
    except Exception:
        return {}


def appel(methode, chemin, corps=None):
    if not API or not JETON:
        sys.exit("outil indisponible : TESTS_API ou TESTS_JETON manquant (à signaler dans le rapport)")
    e = etat()
    corps = dict(corps or {}, persona=PERSONA, appareil=appareil(), appareil_id=e.get("appareil_id"), compte=e.get("compte"))
    req = urllib.request.Request(API + chemin, method=methode, data=json.dumps(corps).encode(),
                                 headers={"Authorization": "Bearer " + JETON, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            rep = json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as x:
        sys.exit(f"erreur {x.code} : {x.read()[:300].decode(errors='ignore')}")
    for k in ("appareil_id", "compte"):
        if rep.get(k):
            e[k] = rep[k]
    os.makedirs("resultats", exist_ok=True)
    json.dump(e, open(ETAT, "w"))
    return rep


def kv(args):
    return dict(a.split("=", 1) for a in args if "=" in a)


def main(a):
    if not a or a[0] in ("-h", "aide"):
        print(__doc__); return
    c, r = a[0], a[1:]
    if c == "preparer":
        plan = json.load(open("plan_1_7.json", encoding="utf-8"))[PERSONA]
        rep = appel("POST", "/imposer", {"versions": plan["versions"]})
    elif c == "imposer":
        rep = appel("POST", "/imposer", {"versions": kv(r)})
    elif c == "versions":
        rep = appel("POST", "/versions")
    elif c == "date":
        rep = appel("POST", "/date", {"date": None if r[0] == "aucune" else r[0]})
    elif c == "compte":
        rep = appel("POST", "/compte-test", {"type": r[0]})
        # Le mot de passe est gardé pour ecrire.py (@mdp-compte), jamais affiché
        e = etat(); e["mdp_compte"] = rep.pop("mot_de_passe", None); json.dump(e, open(ETAT, "w"))
        rep["mot_de_passe"] = "écris-le avec : ecrire.py @mdp-compte"
    elif c == "evenements":
        rep = appel("POST", "/evenements", {"n": int(r[0]) if r else 20})
    elif c == "envoyer":
        rep = appel("POST", "/envoyer", {"notification": r[0], **kv(r[1:])})
    elif c == "apercu":
        rep = appel("POST", "/apercu", {"message": r[0], "version": r[1] if len(r) > 1 and "=" not in r[1] else None, **kv(r[1:])})
    elif c == "simuler":
        rep = appel("POST", "/simuler", {"action": r[0], **kv(r[1:])})
    elif c == "stats":
        rep = appel("POST", "/stats")
    elif c == "liste":
        rep = appel("POST", "/liste")
    else:
        sys.exit("commande inconnue : " + c)
    rep.pop("jeton", None)
    print(json.dumps(rep, ensure_ascii=False, indent=1)[:4000])


if __name__ == "__main__":
    main(sys.argv[1:])
