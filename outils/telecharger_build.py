"""Télécharge le dernier build Hortenia terminé chez Expo (EAS).

Usage : python outils/telecharger_build.py android|ios-simulateur fichier_sortie
BUILD_ID (facultatif) force un build précis. EXPO_TOKEN est obligatoire.
"""
import json, os, sys, urllib.error, urllib.request

AGENT = "hortenia-tests-agents/1.0"
PROJET = "04c19c66-b325-42b1-b9cd-02079aea944f"
REQUETE = """query($id: String!, $plateforme: AppPlatform!) { app { byId(appId: $id) {
  builds(offset: 0, limit: 30, platform: $plateforme, status: FINISHED) {
    id appVersion appBuildVersion buildProfile isForIosSimulator createdAt artifacts { buildUrl applicationArchiveUrl } } } } }"""


def graphql(requete, variables):
    req = urllib.request.Request("https://api.expo.dev/graphql",
                                 data=json.dumps({"query": requete, "variables": variables}).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": AGENT,
                                          "Authorization": "Bearer " + os.environ["EXPO_TOKEN"]})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Expo a répondu {e.code} : {e.read()[:300].decode('utf-8', 'replace')}")
    if d.get("errors"):
        sys.exit("Erreur Expo : " + "; ".join(e.get("message", "") for e in d["errors"]))
    return d["data"]


def main():
    cible, sortie = sys.argv[1], sys.argv[2]
    plateforme = "ANDROID" if cible == "android" else "IOS"
    builds = graphql(REQUETE, {"id": PROJET, "plateforme": plateforme})["app"]["byId"]["builds"]
    if cible == "ios-simulateur":
        builds = [b for b in builds if b.get("isForIosSimulator")]
    voulu = os.environ.get("BUILD_ID", "").strip()
    if voulu:
        builds = [b for b in builds if b["id"] == voulu]
    for b in builds:  # les builds déposés par « eas upload » n'ont que l'archive
        a = b.get("artifacts") or {}
        a["buildUrl"] = a.get("buildUrl") or a.get("applicationArchiveUrl")
        b["artifacts"] = a
    builds = [b for b in builds if b["artifacts"]["buildUrl"]]
    if not builds:
        sys.exit(f"Aucun build {cible} terminé et téléchargeable chez Expo.")
    b = builds[0]
    url = b["artifacts"]["buildUrl"]
    print(f"Build {b['appVersion']} ({b['appBuildVersion']}), profil {b['buildProfile']}, du {b['createdAt'][:16]}")
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=600) as r, open(sortie, "wb") as f:
        while bloc := r.read(1 << 20):
            f.write(bloc)
    ext = url.split("?")[0].rsplit(".", 1)[-1]
    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"extension={ext}\nversion={b['appVersion']} ({b['appBuildVersion']})\n")


if __name__ == "__main__":
    main()
