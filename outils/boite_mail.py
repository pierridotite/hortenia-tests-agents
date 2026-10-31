"""Boîte mail temporaire gratuite (mail.tm) pour les apps concurrentes qui
exigent un compte. Rien au nom de Pierre (accord du 31/10/2026) ; la boîte
est jetable.

Usage : python3 outils/boite_mail.py creer <id>   -> adresse et mot de passe à utiliser dans l'app
        python3 outils/boite_mail.py lire <id>    -> derniers e-mails reçus (texte, liens, codes)
"""
import json, os, random, re, string, sys, time, urllib.request
from pathlib import Path

API = "https://api.mail.tm"


def appel(methode, chemin, corps=None, jeton=None):
    entetes = {"Content-Type": "application/json", "Accept": "application/json"}
    if jeton:
        entetes["Authorization"] = "Bearer " + jeton
    req = urllib.request.Request(API + chemin, method=methode, headers=entetes,
                                 data=json.dumps(corps).encode() if corps is not None else None)
    with urllib.request.urlopen(req, timeout=30) as r:
        t = r.read()
        return json.loads(t) if t else {}


def liste(rep):
    return rep.get("hydra:member", []) if isinstance(rep, dict) else rep


action, ident = sys.argv[1], sys.argv[2]
fichier = Path("boites") / f"{ident}.json"
fichier.parent.mkdir(exist_ok=True)
if action == "creer":
    if fichier.exists():
        b = json.loads(fichier.read_text())
    else:
        dom = liste(appel("GET", "/domains"))[0]["domain"]
        suffixe = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
        b = {"adresse": f"camille.potager.{suffixe}@{dom}",
             "mot_de_passe": "Potager-" + os.environ.get("RUN_ID", "000000")[-6:] + "!"}
        appel("POST", "/accounts", {"address": b["adresse"], "password": b["mot_de_passe"]})
        fichier.write_text(json.dumps(b))
    print(f"adresse : {b['adresse']}\nmot de passe : {b['mot_de_passe']}")
elif action == "lire":
    b = json.loads(fichier.read_text())
    jeton = appel("POST", "/token", {"address": b["adresse"], "password": b["mot_de_passe"]})["token"]
    msgs = []
    for _ in range(6):
        msgs = liste(appel("GET", "/messages", jeton=jeton))
        if msgs:
            break
        time.sleep(10)
    if not msgs:
        print("aucun e-mail reçu (attends un peu et relance)")
    for m in msgs[:3]:
        d = appel("GET", f"/messages/{m['id']}", jeton=jeton)
        html = " ".join(d.get("html") or [])
        texte = d.get("text") or re.sub(r"<[^>]+>", " ", html)
        print(f"--- {d.get('from', {}).get('address')} : {d.get('subject')}")
        print(re.sub(r"\s+", " ", texte)[:1500])
        liens = list(dict.fromkeys(re.findall(r"https?://[^\s\"'<>)]+", texte + " " + html)))
        if liens:
            print("liens :\n" + "\n".join(liens[:10]))
