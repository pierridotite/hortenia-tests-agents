"""Remplace le contenu du champ actif par un texte (sans accents : adb ne
sait pas les taper). Usage : python3 outils/ecrire.py "texte à écrire" """
import os, re, subprocess, sys, unicodedata


def _secret(t):
    """@mdp-site (secret TESTS_SITE_MDP) ou @mdp-compte (compte de test de site_tests.py) : jamais affiché."""
    import json as _j
    if t == "@mdp-site":
        return os.environ.get("TESTS_SITE_MDP", "")
    if t == "@mdp-compte":
        try:
            return _j.load(open("resultats/.site_tests.json")).get("mdp_compte") or ""
        except Exception:
            return ""
    return t


t = unicodedata.normalize("NFKD", _secret(sys.argv[1])).encode("ascii", "ignore").decode()
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_MOVE_END"])
subprocess.run(["adb", "shell", "input", "keyevent", *(["67"] * 40)])
t = re.sub(r"([\\'\"`$&|;<>()*~#])", r"\\\1", t).replace(" ", "%s")
subprocess.run(["adb", "shell", "input", "text", t])
print("écrit")
