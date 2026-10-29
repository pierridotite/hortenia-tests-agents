"""Télécharge le dernier build Hortenia terminé chez Expo (EAS).

Usage : python outils/telecharger_build.py android|ios-simulateur fichier_sortie
BUILD_ID (facultatif) force un build précis. EXPO_TOKEN est obligatoire.
"""
import json, os, sys, urllib.request

PROJET = "04c19c66-b325-42b1-b9cd-02079aea944f"
REQUETE = """query($id: String!, $plateforme: AppPlatform!) { app { byId(appId: $id) {
  builds(offset: 0, limit: 30, platform: $plateforme, status: FINISHED) {
    id appVersion appBuildVersion buildProfile isForIosSimulator createdAt artifacts { buildUrl } } } } }"""


def graphql(requete, variables):
    req = urllib.request.Request("https://api.expo.dev/graphql",
                                 data=json.dumps({"query": requete, "variables": variables}).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + os.environ["EXPO_TOKEN"]})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
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
    builds = [b for b in builds if (b.get("artifacts") or {}).get("buildUrl")]
    if not builds:
        sys.exit(f"Aucun build {cible} terminé et téléchargeable chez Expo.")
    b = builds[0]
    url = b["artifacts"]["buildUrl"]
    print(f"Build {b['appVersion']} ({b['appBuildVersion']}), profil {b['buildProfile']}, du {b['createdAt'][:16]}")
    urllib.request.urlretrieve(url, sortie)
    ext = url.split("?")[0].rsplit(".", 1)[-1]
    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"extension={ext}\nversion={b['appVersion']} ({b['appBuildVersion']})\n")


if __name__ == "__main__":
    main()
