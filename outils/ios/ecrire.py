"""Remplace le contenu du champ actif du simulateur iOS par un texte.
Les accents sont retirés (la frappe simulée ne connaît que le clavier US).
Usage : python3 outils/ios/ecrire.py "texte à écrire" """
import os, subprocess, sys, unicodedata

UDID = os.environ["UDID"]
t = unicodedata.normalize("NFKD", sys.argv[1]).encode("ascii", "ignore").decode()
# Tout sélectionner (Cmd+A) puis effacer ; à défaut, 60 retours arrière
subprocess.run(["axe", "key-combo", "--modifiers", "227", "--key", "4", "--udid", UDID], capture_output=True)
subprocess.run(["axe", "key", "42", "--udid", UDID], capture_output=True)
subprocess.run(["axe", "key-sequence", "--keycodes", ",".join(["42"] * 60), "--delay", "0.02", "--udid", UDID], capture_output=True)
r = subprocess.run(["axe", "type", t, "--udid", UDID], capture_output=True, text=True)
if r.returncode:
    print("échec : " + (r.stderr or r.stdout)[-300:])
else:
    print("écrit : vérifie le texte sur la prochaine capture")
