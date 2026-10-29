"""Crée le simulateur voulu (modèle et version d'iOS) et
affiche « UDID=… » et « APPAREIL=… » à ajouter à GITHUB_ENV.

Usage : python3 outils/ios/simulateur.py "<modèle>" <version iOS majeure>
Si le modèle ou la version n'existent pas sur le Mac, prend le plus proche
(même famille, puis le plus récent) et le dit.
"""
import json, subprocess, sys


def simctl(*a):
    return subprocess.run(["xcrun", "simctl", *a], capture_output=True, text=True, check=True).stdout


voulu, version = sys.argv[1], sys.argv[2]
d = json.loads(simctl("list", "-j", "devicetypes", "runtimes"))
runtimes = [r for r in d["runtimes"] if r.get("isAvailable") and r["identifier"].startswith("com.apple.CoreSimulator.SimRuntime.iOS")]
runtimes.sort(key=lambda r: [int(x) for x in r["version"].split(".")])
if not runtimes:
    sys.exit("Aucun runtime iOS sur ce Mac")
choix = [r for r in runtimes if r["version"].split(".")[0] == str(version)] or runtimes
runtime = choix[-1]
types = {t["name"]: t for t in runtime.get("supportedDeviceTypes") or d["devicetypes"]}
if voulu in types:
    modele = voulu
else:
    famille = "iPad" if voulu.startswith("iPad") else "iPhone"
    proches = [n for n in types if n.startswith(famille)]
    modele = proches[-1]
    print(f"{voulu} absent pour iOS {runtime['version']} : {modele} à la place", file=sys.stderr)
udid = simctl("create", "Testeur", types[modele]["identifier"], runtime["identifier"]).strip()

print(f"UDID={udid}")
print(f"APPAREIL={modele}, iOS {runtime['version']}")
