"""Capture l'écran de l'émulateur et liste les éléments visibles.

Usage : python3 outils/ecran.py <dossier> <numero>
Écrit <dossier>/<numero>.png (moitié de la taille réelle, pour la lecture)
et affiche les éléments (texte, description, champ de saisie) avec la
position de leur centre en pixels RÉELS de l'écran, à passer à
`adb shell input tap X Y`. Signale aussi les plantages récents (logcat).
"""
import io, re, subprocess, sys
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image


def adb(*a, binaire=False):
    r = subprocess.run(["adb", *a], capture_output=True, timeout=60)
    return r.stdout if binaire else r.stdout.decode("utf-8", "replace")


dossier, numero = Path(sys.argv[1]), sys.argv[2]
dossier.mkdir(parents=True, exist_ok=True)
brut = adb("exec-out", "screencap", "-p", binaire=True)
# Écrans multiples (pliable) : screencap écrit un avertissement avant le PNG
brut = brut[brut.find(b"\x89PNG"):] if b"\x89PNG" in brut else brut
img = Image.open(io.BytesIO(brut)).convert("RGB")
l, h = img.size
chemin = dossier / f"{numero}.png"
img.resize((l // 2, h // 2)).save(chemin)
print(f"capture : {chemin} (écran réel {l}x{h}, image à la moitié : multiplier par 2 une position lue sur l'image)")

adb("shell", "uiautomator", "dump", "/sdcard/ui.xml")
xml = adb("exec-out", "cat", "/sdcard/ui.xml")
try:
    noeuds = ET.fromstring(xml[xml.find("<"):]).iter("node")
except ET.ParseError:
    noeuds = []
for n in noeuds:
    texte, desc = (n.get("text") or "").strip(), (n.get("content-desc") or "").strip()
    saisie = n.get("class", "").endswith("EditText")
    if not (texte or desc or saisie):
        continue
    m = re.findall(r"\d+", n.get("bounds", ""))
    if len(m) != 4:
        continue
    x1, y1, x2, y2 = map(int, m)
    genre = "champ" if saisie else ("bouton" if n.get("clickable") == "true" else "texte")
    print(f"- {genre} « {(texte or desc)[:70]} » centre=({(x1 + x2) // 2},{(y1 + y2) // 2})")

app = adb("shell", "dumpsys", "activity", "activities")
m = re.search(r"(mResumedActivity|topResumedActivity)[^\n]*", app)
print("premier plan :", m.group(0).split()[-2] if m else "?")
crash = adb("logcat", "-d", "-b", "crash") + adb("logcat", "-d", "AndroidRuntime:E", "ReactNativeJS:E", "*:S")
adb("logcat", "-c")
lignes = [x for x in crash.splitlines() if x.strip() and not x.startswith("-----")]
if lignes:
    print("ERREURS LOGCAT depuis la dernière capture :")
    print("\n".join(lignes[-15:]))
