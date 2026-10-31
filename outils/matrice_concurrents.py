"""Matrice du workflow concurrents.yml : une ligne par app de concurrents.json
(ou seulement celles de la variable APPS, ids séparés par des virgules)."""
import json, os

apps = json.load(open("concurrents.json"))["apps"]
voulues = [a.strip() for a in os.environ.get("APPS", "").split(",") if a.strip()]
if voulues:
    apps = [a for a in apps if a["id"] in voulues]
print("apps=" + json.dumps([{"app": a["id"], "nom": a["nom"], "paquet": a["paquet"]} for a in apps]))
