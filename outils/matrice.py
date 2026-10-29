"""Matrice du workflow : une entrée par persona demandée, avec son téléphone
virtuel (personas.json, champ « appareil »). Sans appareil : Pixel 6, Android 14."""
import json
import os

demandees = [p.strip() for p in os.environ.get("PERSONAS", "").split(",") if p.strip()]
personas = {p["id"]: p for p in json.load(open("personas.json", encoding="utf-8"))}
lignes = []
for pid in demandees:
    a = personas.get(pid, {}).get("appareil", {})
    lignes.append({
        "persona": pid,
        "profil": a.get("profil", "pixel_6"),
        "api": a.get("android_api", 34),
        "taille_texte": str(a.get("taille_texte", 1.0)),
        "appareil": a.get("nom", "Pixel 6, Android 14"),
    })
print("personas=" + json.dumps(lignes, ensure_ascii=False))
