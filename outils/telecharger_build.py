"""Télécharge le dernier build Hortenia terminé chez Expo (EAS).

Usage : python outils/telecharger_build.py android|ios-simulateur fichier_sortie
BUILD_ID (facultatif) force un build précis. EXPO_TOKEN est obligatoire.
BUILD_ID=gh:<run> : build du banc déposé en artefact chiffré par ce run
d'android-build.yml ou d'ios-build.yml (GITHUB_TOKEN et TESTS_JETON requis).
"""
import io, json, os, subprocess, sys, urllib.error, urllib.request, zipfile

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


def depuis_github(run, cible, sortie):
    depot = os.environ.get("GITHUB_REPOSITORY", "pierridotite/hortenia-tests-agents")
    h = {"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"], "User-Agent": AGENT,
         "Accept": "application/vnd.github+json"}
    def get(url):
        with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=600) as r:
            return r.read()
    noms = ("app-banc-android",) if cible == "android" else ("app-banc-simulateur",)
    arts = json.loads(get(f"https://api.github.com/repos/{depot}/actions/runs/{run}/artifacts"))["artifacts"]
    art = next((a for a in arts if a["name"] in noms and not a["expired"]), None)
    if not art:
        sys.exit(f"Aucun artefact {noms[0]} dans le run {run}.")
    # Le lien de l'archive redirige vers un stockage signé : le suivre sans l'en-tête Authorization
    class SansSuivre(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    try:
        urllib.request.build_opener(SansSuivre).open(urllib.request.Request(art["archive_download_url"], headers=h), timeout=60)
        sys.exit("pas de redirection pour l'archive de l'artefact")
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307, 308):
            raise
        lien = e.headers["Location"]
    with urllib.request.urlopen(urllib.request.Request(lien, headers={"User-Agent": AGENT}), timeout=900) as r:
        z = zipfile.ZipFile(io.BytesIO(r.read()))
    nom = next(n for n in z.namelist() if n.endswith(".enc"))
    open("build.enc", "wb").write(z.read(nom))
    subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", "env:TESTS_JETON",
                    "-in", "build.enc", "-out", sortie], check=True)
    os.remove("build.enc")
    ext = nom[:-4].rsplit(".", 1)[-1]
    print(f"Build du banc repris du run {run} ({nom[:-4]})")
    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"extension={ext}\nversion=run {run}\n")


def main():
    cible, sortie = sys.argv[1], sys.argv[2]
    voulu = os.environ.get("BUILD_ID", "").strip()
    if voulu.startswith("gh:"):
        return depuis_github(voulu[3:], cible, sortie)
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
