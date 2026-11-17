"""App Store Connect : préparer puis soumettre une version iOS, par l'API
(clé du secret ASC_API_KEY_P8). Usage :
  python3 outils/asc_soumission.py etat|preparer|soumettre|retirer VERSION BUILD [fichier nouveautés] [produits séparés par des virgules]
- etat      : lit la version, le build, les produits ; ne change rien.
- retirer   : retire de l'examen la version VERSION (soumission en attente ou
              en cours d'examen) ; elle redevient modifiable.
- preparer  : renomme la version modifiable s'il y en a une (ex. 1.7.2 retirée
              de l'examen devient 1.8.0), sinon crée la version si elle manque, attache le build (attend qu'il soit
              traité), écrit les nouveautés fr-FR.
- soumettre : ajoute les produits (abonnements) non encore approuvés et la
              version à une soumission, puis l'envoie en revue.
"""
import json, os, sys, time, urllib.error, urllib.request
import jwt

APP = "6737479478"
KID, ISS = "K78XTPTD68", "b959d263-8901-4728-981d-4a1ae2458181"
CLE = os.environ["ASC_CLE"]
action, version, build = sys.argv[1:4]
notes = open(sys.argv[4]).read().strip() if len(sys.argv) > 4 and sys.argv[4] else ""
produits = [p for p in (sys.argv[5].split(",") if len(sys.argv) > 5 else []) if p]
resume = []


def jeton():
    t = int(time.time())
    return jwt.encode({"iss": ISS, "iat": t, "exp": t + 900, "aud": "appstoreconnect-v1"}, CLE,
                      algorithm="ES256", headers={"kid": KID, "typ": "JWT"})


def api(methode, chemin, corps=None, ok404=False):
    # GET et PATCH sont rejoués (5 essais, 30 s d'écart) sur une erreur 5xx ou un délai dépassé :
    # App Store Connect a des pannes qui vont et viennent. POST n'est jamais rejoué (doublon possible).
    essais = 5 if methode in ("GET", "PATCH") else 1
    for n in range(1, essais + 1):
        req = urllib.request.Request("https://api.appstoreconnect.apple.com" + chemin, method=methode,
                                     data=json.dumps(corps).encode() if corps is not None else None,
                                     headers={"Authorization": f"Bearer {jeton()}", "Content-Type": "application/json"})
        try:
            r = urllib.request.urlopen(req, timeout=60).read()
            return json.loads(r) if r else {}
        except urllib.error.HTTPError as e:
            texte = e.read().decode()[:1500]
            if ok404 and e.code == 404:
                return None
            if e.code >= 500 and n < essais:
                print(f"{methode} {chemin} : HTTP {e.code}, nouvel essai dans 30 s ({n}/{essais})")
                time.sleep(30)
                continue
            sys.exit(f"{methode} {chemin} : HTTP {e.code}\n{texte}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if n < essais:
                print(f"{methode} {chemin} : {e}, nouvel essai dans 30 s ({n}/{essais})")
                time.sleep(30)
                continue
            sys.exit(f"{methode} {chemin} : {e}")


def dire(m):
    print(m); resume.append(m)


def version_ios():
    d = api("GET", f"/v1/apps/{APP}/appStoreVersions?filter[platform]=IOS&limit=10")["data"]
    return next((v for v in d if v["attributes"]["versionString"] == version), None), d


def le_build():
    d = api("GET", f"/v1/builds?filter[app]={APP}&filter[version]={build}&filter[preReleaseVersion.version]={version}&limit=5")["data"]
    return d[0] if d else None


def abonnements():
    trouves = {}
    for g in api("GET", f"/v1/apps/{APP}/subscriptionGroups?limit=50")["data"]:
        for s in api("GET", f"/v1/subscriptionGroups/{g['id']}/subscriptions?limit=50")["data"]:
            trouves[s["attributes"]["productId"]] = s
    return trouves


v, toutes = version_ios()
dire("versions iOS : " + ", ".join(f"{x['attributes']['versionString']} ({x['attributes']['appStoreState']})" for x in toutes))
b = le_build()
dire(f"build {version} ({build}) : " + (b["attributes"]["processingState"] if b else "absent"))
abos = abonnements()
for p in produits:
    s = abos.get(p)
    dire(f"produit {p} : " + (s["attributes"]["state"] if s else "introuvable"))

if action == "etat" and v:
    # Nouveautés en ligne, langue par langue ; comparées au JSON fourni s'il y en a un.
    attendu = json.loads(notes) if notes.lstrip().startswith("{") else {}
    for l in api("GET", f"/v1/appStoreVersions/{v['id']}/appStoreVersionLocalizations?limit=50")["data"]:
        loc, wn = l["attributes"]["locale"], (l["attributes"].get("whatsNew") or "").strip()
        verdict = "" if not attendu else (" : identique au texte fourni" if wn == (attendu.get(loc) or "").strip() else " : DIFFÉRENT du texte fourni")
        dire(f"nouveautés {loc} ({len(wn)} car.) « {wn[:60]}… »{verdict}")

MODIFIABLES = ("PREPARE_FOR_SUBMISSION", "DEVELOPER_REJECTED", "REJECTED", "METADATA_REJECTED")

if action == "retirer":
    if not v:
        sys.exit(f"version {version} introuvable")
    subs = api("GET", f"/v1/reviewSubmissions?filter[app]={APP}&filter[platform]=IOS"
                      "&filter[state]=WAITING_FOR_REVIEW,IN_REVIEW,UNRESOLVED_ISSUES&include=items&limit=10")
    retiree = False
    for sub in subs.get("data", []):
        items = api("GET", f"/v1/reviewSubmissions/{sub['id']}/items?include=appStoreVersion&limit=20")["data"]
        if any((i["relationships"].get("appStoreVersion", {}).get("data") or {}).get("id") == v["id"] for i in items):
            api("PATCH", f"/v1/reviewSubmissions/{sub['id']}", {"data": {"type": "reviewSubmissions", "id": sub["id"], "attributes": {"canceled": True}}})
            dire(f"version {version} retirée de l'examen (soumission {sub['id']}, état {sub['attributes']['state']})")
            retiree = True
    if not retiree:
        sys.exit(f"aucune soumission en cours pour la version {version}")
    for _ in range(20):
        time.sleep(15)
        etat = api("GET", f"/v1/appStoreVersions/{v['id']}")["data"]["attributes"]["appStoreState"]
        if etat in MODIFIABLES:
            break
    dire(f"état de la version {version} : {etat}")

if action == "preparer":
    if not v:
        m = next((x for x in toutes if x["attributes"]["appStoreState"] in MODIFIABLES), None)
        if m:
            ancienne = m["attributes"]["versionString"]
            v = api("PATCH", f"/v1/appStoreVersions/{m['id']}", {"data": {"type": "appStoreVersions", "id": m["id"],
                  "attributes": {"versionString": version}}})["data"]
            dire(f"version {ancienne} renommée en {version}")
    if not v:
        v = api("POST", "/v1/appStoreVersions", {"data": {"type": "appStoreVersions",
              "attributes": {"platform": "IOS", "versionString": version, "releaseType": "AFTER_APPROVAL"},
              "relationships": {"app": {"data": {"type": "apps", "id": APP}}}}})["data"]
        dire(f"version {version} créée")
    for _ in range(60):
        b = le_build()
        if b and b["attributes"]["processingState"] == "VALID":
            break
        time.sleep(60)
    else:
        sys.exit("build pas encore traité par Apple après 60 min")
    api("PATCH", f"/v1/appStoreVersions/{v['id']}/relationships/build", {"data": {"type": "builds", "id": b["id"]}})
    dire(f"build {build} attaché à la version {version}")
    if notes:
        # Nouveautés : texte (fr-FR) ou JSON {"fr-FR": "...", "en-GB": "...", ...}
        try:
            parlangue = json.loads(notes) if notes.lstrip().startswith("{") else {"fr-FR": notes}
        except ValueError:
            sys.exit("nouveautés : JSON illisible")
        locs = api("GET", f"/v1/appStoreVersions/{v['id']}/appStoreVersionLocalizations?limit=50")["data"]
        for l in locs:
            loc = l["attributes"]["locale"]
            texte = parlangue.get(loc) or parlangue.get(loc.split("-")[0])
            if texte:
                api("PATCH", f"/v1/appStoreVersionLocalizations/{l['id']}", {"data": {"type": "appStoreVersionLocalizations", "id": l["id"], "attributes": {"whatsNew": texte[:4000]}}})
                dire(f"nouveautés {loc} écrites")
            else:
                dire(f"nouveautés {loc} : aucun texte fourni, inchangées")

if action == "soumettre":
    if not v:
        sys.exit("version absente : lancer preparer d'abord")
    sub = api("POST", "/v1/reviewSubmissions", {"data": {"type": "reviewSubmissions", "attributes": {"platform": "IOS"},
              "relationships": {"app": {"data": {"type": "apps", "id": APP}}}}})["data"]
    for p in produits:
        s = abos.get(p)
        if s and s["attributes"]["state"] in ("READY_TO_SUBMIT", "DEVELOPER_ACTION_NEEDED", "REJECTED"):
            api("POST", "/v1/subscriptionSubmissions", {"data": {"type": "subscriptionSubmissions",
                "relationships": {"subscription": {"data": {"type": "subscriptions", "id": s["id"]}}}}})
            dire(f"produit {p} joint à la prochaine version")
    api("POST", "/v1/reviewSubmissionItems", {"data": {"type": "reviewSubmissionItems",
        "relationships": {"reviewSubmission": {"data": {"type": "reviewSubmissions", "id": sub["id"]}},
                          "appStoreVersion": {"data": {"type": "appStoreVersions", "id": v["id"]}}}}})
    api("PATCH", f"/v1/reviewSubmissions/{sub['id']}", {"data": {"type": "reviewSubmissions", "id": sub["id"], "attributes": {"submitted": True}}})
    dire(f"version {version} envoyée en revue")

with open(os.environ.get("GITHUB_STEP_SUMMARY", "/dev/null"), "a") as f:
    f.write("\n".join(resume) + "\n")
