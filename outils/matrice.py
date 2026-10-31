"""Matrice des workflows : une entrée par persona demandée, avec son appareil
(personas.json, champ « appareil »). PLATEFORME=android (défaut) ou ios.
Android sans appareil : Pixel 6, Android 14.
Champ « localisation » d'une persona : refus (elle refuse la position) ou
sans_gps (le téléphone ne donne aucune position)."""
import json
import os

plateforme = os.environ.get("PLATEFORME", "android")
demandees = [p.strip() for p in os.environ.get("PERSONAS", "").split(",") if p.strip()]
personas = {p["id"]: p for p in json.load(open("personas.json", encoding="utf-8"))}
lignes = []
for pid in demandees:
    p = personas.get(pid, {})
    a = p.get("appareil", {})
    pos = p.get("position") or [45.764, 4.8357]
    ligne = {"persona": pid, "theme": a.get("theme", "clair"), "position": f"{pos[0]},{pos[1]}",
             "localisation": p.get("localisation", "")}
    if plateforme == "ios":
        ligne.update({"simulateur": a.get("simulateur", "iPhone 16"), "ios": str(a.get("ios", "18")),
                      "taille_texte": a.get("taille_texte", "large"), "appareil": a.get("nom", "iPhone 16, iOS 18"),
                      "theme": "dark" if a.get("theme") in ("dark", "sombre") else "light"})
    else:
        ligne.update({"profil": a.get("profil", "pixel_6"), "api": a.get("android_api", 34),
                      "taille_texte": str(a.get("taille_texte", 1.0)), "appareil": a.get("nom", "Pixel 6, Android 14")})
    lignes.append(ligne)
print("personas=" + json.dumps(lignes, ensure_ascii=False))
