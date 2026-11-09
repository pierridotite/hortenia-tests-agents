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
