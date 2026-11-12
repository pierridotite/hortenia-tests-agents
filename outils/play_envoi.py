"""Envoie un aab en test interne Google Play directement par l'API (sans
passer par la file d'EAS Submit). Usage : play_envoi.py <aab> <clé json>"""
import json, sys, requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

aab, cle = sys.argv[1], sys.argv[2]
cred = service_account.Credentials.from_service_account_file(cle, scopes=["https://www.googleapis.com/auth/androidpublisher"])
cred.refresh(Request())
h = {"Authorization": f"Bearer {cred.token}"}
app = "applications/com.hortenia.app"
base = f"https://androidpublisher.googleapis.com/androidpublisher/v3/{app}"
edit = requests.post(f"{base}/edits", headers=h, timeout=60).json()["id"]
with open(aab, "rb") as f:
    r = requests.post(f"https://androidpublisher.googleapis.com/upload/androidpublisher/v3/{app}/edits/{edit}/bundles?uploadType=media",
                      headers={**h, "Content-Type": "application/octet-stream"}, data=f, timeout=1800)
if not r.ok:
    sys.exit(f"envoi du bundle refusé : HTTP {r.status_code} {r.text[:300]}")
vc = r.json()["versionCode"]
t = requests.put(f"{base}/edits/{edit}/tracks/internal", headers=h, timeout=60,
                 json={"track": "internal", "releases": [{"versionCodes": [str(vc)], "status": "completed"}]})
if not t.ok:
    sys.exit(f"piste interne refusée : HTTP {t.status_code} {t.text[:300]}")
c = requests.post(f"{base}/edits/{edit}:commit?changesInReviewBehavior=ERROR_IF_IN_REVIEW", headers=h, timeout=120)
if not c.ok:
    sys.exit(f"validation refusée : HTTP {c.status_code} {c.text[:300]}")
print(f"versionCode {vc} en test interne")
