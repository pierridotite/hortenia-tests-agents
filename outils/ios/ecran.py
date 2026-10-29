"""Capture l'écran du simulateur iOS et liste les éléments visibles.

Usage : python3 outils/ios/ecran.py <dossier> <numero>
Écrit <dossier>/<numero>.png à la taille de l'écran en POINTS : une position
lue sur l'image se passe telle quelle à `bash outils/ios/geste.sh toucher X Y`.
Affiche les éléments (texte, bouton, champ) avec le centre en points, et
signale un plantage de l'app (processus absent, rapport de plantage récent).
"""
import json, os, subprocess, sys, time
from pathlib import Path
from PIL import Image

UDID = os.environ["UDID"]
APP = "com.hortenia.app"


def run(*a, timeout=60):
    return subprocess.run(list(a), capture_output=True, text=True, timeout=timeout).stdout


def elements(noeud, sortie):
    if isinstance(noeud, list):
        for n in noeud:
            elements(n, sortie)
        return
    if not isinstance(noeud, dict):
        return
    f = noeud.get("frame") or {}
    texte = (noeud.get("AXLabel") or noeud.get("title") or "").strip()
    valeur = str(noeud.get("AXValue") or "").strip()
    genre = (noeud.get("type") or noeud.get("role_description") or "").strip()
    if f and (texte or valeur or "Field" in genre or genre in ("Button", "TextArea")):
        sortie.append((genre, texte, valeur, f))
    elements(noeud.get("children") or [], sortie)


dossier, numero = Path(sys.argv[1]), sys.argv[2]
dossier.mkdir(parents=True, exist_ok=True)
brut = dossier / f"{numero}-brut.png"
run("xcrun", "simctl", "io", UDID, "screenshot", "--type=png", str(brut))
try:
    arbre = json.loads(run("axe", "describe-ui", "--udid", UDID))
except json.JSONDecodeError:
    arbre = []
liste = []
elements(arbre, liste)
img = Image.open(brut).convert("RGB")
largeur_pts = 0
for g, t, v, f in liste:
    largeur_pts = max(largeur_pts, int(f.get("x", 0) + f.get("width", 0)))
if not largeur_pts:
    largeur_pts = img.size[0] // 3
echelle = img.size[0] / largeur_pts
chemin = dossier / f"{numero}.png"
img.resize((round(img.size[0] / echelle), round(img.size[1] / echelle))).save(chemin)
brut.unlink()
print(f"capture : {chemin} ({img.size[0] // round(echelle)}x{round(img.size[1] / echelle)} points ; une position lue sur l'image = une position à toucher)")

for genre, texte, valeur, f in liste:
    if genre in ("Application", "Window") or f.get("width", 0) <= 0:
        continue
    cx, cy = round(f["x"] + f["width"] / 2), round(f["y"] + f["height"] / 2)
    nom = "champ" if "Field" in genre or genre == "TextArea" else ("bouton" if genre in ("Button", "Link", "Switch", "Cell", "Tab") else "texte")
    v = f" valeur « {valeur[:40]} »" if valeur and valeur != texte else ""
    print(f"- {nom} « {texte[:70]} »{v} centre=({cx},{cy})")

if APP not in run("xcrun", "simctl", "spawn", UDID, "launchctl", "list"):
    print("ATTENTION : l'app Hortenia ne tourne plus (plantage ou fermeture).")
rapports = Path.home() / "Library/Logs/DiagnosticReports"
recents = [p for p in rapports.glob("*.ips") if "ortenia" in p.name and time.time() - p.stat().st_mtime < 120] if rapports.exists() else []
for p in recents:
    print(f"PLANTAGE : rapport {p.name} il y a moins de 2 min")
