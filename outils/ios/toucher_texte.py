"""Attend un élément du simulateur dont le libellé contient un des textes
donnés, puis le touche en son centre. Sert aux enregistrements sans Claude
(alerte système comprise, quand AXe la voit).

Usage : python3 outils/ios/toucher_texte.py <secondes> "texte 1" ["texte 2"…]
Code de sortie 0 si touché, 1 sinon.
"""
import json, os, subprocess, sys, time

UDID = os.environ["UDID"]
delai, textes = float(sys.argv[1]), [t.lower() for t in sys.argv[2:]]


def noeuds(n):
    if isinstance(n, list):
        for x in n:
            yield from noeuds(x)
    elif isinstance(n, dict):
        yield n
        yield from noeuds(n.get("children") or [])


fin = time.time() + delai
while time.time() < fin:
    sortie = subprocess.run(["axe", "describe-ui", "--udid", UDID], capture_output=True, text=True).stdout
    try:
        arbre = json.loads(sortie)
    except json.JSONDecodeError:
        arbre = []
    for n in noeuds(arbre):
        libelle = (n.get("AXLabel") or n.get("title") or "").strip()
        f = n.get("frame") or {}
        if libelle and f and any(t in libelle.lower() for t in textes):
            x, y = f["x"] + f["width"] / 2, f["y"] + f["height"] / 2
            subprocess.run(["axe", "tap", "-x", str(round(x)), "-y", str(round(y)), "--udid", UDID])
            print(f"touché « {libelle} » en {round(x)},{round(y)}")
            sys.exit(0)
    time.sleep(1)
print("introuvable : " + " / ".join(sys.argv[2:]))
sys.exit(1)
