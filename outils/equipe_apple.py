"""Affiche l'identifiant d'équipe Apple (OU du certificat de distribution),
lu par l'API App Store Connect avec la clé du secret ASC_API_KEY_P8.
Usage : python3 outils/equipe_apple.py <chemin .p8> <key id> <issuer id>"""
import base64, json, subprocess, sys, time, urllib.error, urllib.request
import jwt  # pyjwt[crypto]

cle, kid, iss = sys.argv[1:4]
jeton = jwt.encode({"iss": iss, "iat": int(time.time()), "exp": int(time.time()) + 600, "aud": "appstoreconnect-v1"},
                   open(cle).read(), algorithm="ES256", headers={"kid": kid, "typ": "JWT"})
def lire(chemin):
    req = urllib.request.Request("https://api.appstoreconnect.apple.com" + chemin, headers={"Authorization": f"Bearer {jeton}"})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        print(chemin, e.code, e.read().decode()[:400], file=sys.stderr)
        return None

# droits de la clé, pour le journal
for ch in ("/v1/bundleIds?limit=1", "/v1/profiles?limit=1", "/v1/apps?limit=1"):
    print(ch, "ok" if lire(ch) is not None else "refusé", file=sys.stderr)
# identifiant du widget : créé s'il manque (pour y cocher le groupe d'apps)
WIDGET = "com.hortenia.app.widget"
b = lire(f"/v1/bundleIds?filter[identifier]={WIDGET}")
if b is not None and not [x for x in b["data"] if x["attributes"]["identifier"] == WIDGET]:
    req = urllib.request.Request("https://api.appstoreconnect.apple.com/v1/bundleIds", method="POST",
        data=json.dumps({"data": {"type": "bundleIds", "attributes": {"identifier": WIDGET, "name": "Hortenia Widget", "platform": "IOS"}}}).encode(),
        headers={"Authorization": f"Bearer {jeton}", "Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req); print("identifiant", WIDGET, "créé", file=sys.stderr)
    except urllib.error.HTTPError as e:
        print("création", WIDGET, e.code, e.read().decode()[:300], file=sys.stderr)
elif b is not None:
    print("identifiant", WIDGET, "déjà là", file=sys.stderr)
certs = lire("/v1/certificates?limit=20") or {"data": []}
for c in certs["data"]:
    if "DISTRIBUTION" not in c["attributes"]["certificateType"]:
        continue
    der = base64.b64decode(c["attributes"]["certificateContent"])
    sujet = subprocess.run(["openssl", "x509", "-inform", "DER", "-noout", "-subject", "-nameopt", "sep_multiline"],
                           input=der, capture_output=True).stdout.decode()
    for ligne in sujet.splitlines():
        if ligne.strip().startswith("OU="):
            print(ligne.strip()[3:]); sys.exit(0)
sys.exit("aucun certificat de distribution trouvé")
