"""Remplace le contenu du champ actif par un texte (sans accents : adb ne
sait pas les taper). Usage : python3 outils/ecrire.py "texte à écrire" """
import re, subprocess, sys, unicodedata

t = unicodedata.normalize("NFKD", sys.argv[1]).encode("ascii", "ignore").decode()
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_MOVE_END"])
subprocess.run(["adb", "shell", "input", "keyevent", *(["67"] * 40)])
t = re.sub(r"([\\'\"`$&|;<>()*~#])", r"\\\1", t).replace(" ", "%s")
subprocess.run(["adb", "shell", "input", "text", t])
print("écrit")
