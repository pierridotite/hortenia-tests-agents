"""Remplace le contenu du champ actif du simulateur iOS par un texte.
Le texte est collé (presse-papiers du simulateur puis Cmd+V) : accents et
symboles passent tels quels, sans correction automatique d'iOS.
Usage : python3 outils/ios/ecrire.py "texte à écrire" """
import os, subprocess, sys

UDID = os.environ["UDID"]


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

t = _secret(sys.argv[1])


def axe(*a):
    return subprocess.run(["axe", *a, "--udid", UDID], capture_output=True, text=True)


# Tout sélectionner (Cmd+A) puis effacer ; à défaut, 60 retours arrière
axe("key-combo", "--modifiers", "227", "--key", "4")
axe("key", "42")
axe("key-sequence", "--keycodes", ",".join(["42"] * 60), "--delay", "0.02")
colle = subprocess.run(["xcrun", "simctl", "pbcopy", UDID], input=t, text=True, capture_output=True)
r = axe("key-combo", "--modifiers", "227", "--key", "25") if colle.returncode == 0 else colle
if r.returncode:
    # Repli : frappe touche par touche (clavier US, sans accents)
    import unicodedata
    r = axe("type", unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode())
if r.returncode:
    print("échec : " + (r.stderr or r.stdout)[-300:])
else:
    print("écrit : vérifie le texte sur la prochaine capture")
