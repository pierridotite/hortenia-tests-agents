"""Fait juger un lot de vidéos montées par les jardiniers du panel, un Claude par personne.

Usage : python mirofish/juger_videos.py <dossier du lot> <dossier de sortie>

Le dossier contient panel.md (une personne par ligne numérotée) et, pour chaque
vidéo Vxx, Vxx-images.jpg (une image par seconde) et Vxx-voix.txt (la voix off,
aussi affichée en sous-titres). Chaque personne voit les vidéos comme dans son
fil Facebook, puis les classe. Les réponses vont dans le dossier de sortie,
chiffré ensuite ; le journal public ne montre que des compteurs.
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import subprocess
import sys

lot, sortie = sys.argv[1:3]
MODELE = os.environ.get("MODELE", "claude-sonnet-5-5")
os.makedirs(sortie, exist_ok=True)
videos = sorted(os.path.basename(p)[:-11] for p in glob.glob(os.path.join(lot, "*-images.jpg")))
panel = [l.strip() for l in open(os.path.join(lot, "panel.md"), encoding="utf-8") if re.match(r"\d+\. ", l)]

def consigne(personne):
    liste = "\n".join(
        f"- {v} : images seconde par seconde dans {os.path.abspath(os.path.join(lot, v + '-images.jpg'))} ; "
        f"voix off (aussi en sous-titres) : « {open(os.path.join(lot, v + '-voix.txt'), encoding='utf-8').read().strip()} »"
        for v in videos)
    return f"""Tu joues cette personne, réelle et cohérente : {personne}

Nous sommes fin octobre. En faisant défiler ton fil Facebook sur ton téléphone, tu tombes sur {len(videos)} vidéos courtes verticales sponsorisées par Hortenia, une application de potager. Pour chacune, ouvre l'image indiquée avec l'outil Read : c'est la vidéo image par image (une image par seconde, le numéro en haut à gauche).
{liste}

Réagis comme tu le ferais vraiment, en français et avec ta propre voix. Pour chaque vidéo : est-ce que les 2 premières secondes t'arrêtent, regarderais-tu jusqu'au bout, qu'est-ce qui te plaît, qu'est-ce qui sonne faux ou « pub », et cliquerais-tu sur le lien pour installer l'app gratuite. Juge aussi l'image : photos, lisibilité des textes, rythme, finition (est-ce que ça fait amateur ou « fait par une IA » ?).

Puis classe les vidéos de la meilleure à la moins bonne pour te donner envie d'installer Hortenia.
Termine par une ligne exacte au format :
CLASSEMENT: Vxx > Vxx > Vxx | ARRET: Vxx,Vxx (celles qui t'arrêtent) | CLIC: Vxx (ou aucune) | NOTES: Vxx=n/10, Vxx=n/10, Vxx=n/10"""

def juger(i_personne):
    i, personne = i_personne
    cmd = ["claude", "-p", "--model", MODELE, "--output-format", "json", "--tools", "Read",
           "--allowedTools", "Read", "--max-turns", "8", "--no-session-persistence",
           "--strict-mcp-config", "--disable-slash-commands"]
    for _ in range(3):
        try:
            r = subprocess.run(cmd, input=consigne(personne), capture_output=True, text=True, timeout=900)
            d = json.loads(r.stdout)
            if not d.get("is_error") and d.get("result"):
                return i, personne, d["result"]
        except (subprocess.TimeoutExpired, json.JSONDecodeError):
            pass
    return i, personne, None

resultats = []
with cf.ThreadPoolExecutor(int(os.environ.get("PARALLELE", "10"))) as ex:
    for i, personne, texte in ex.map(juger, enumerate(panel)):
        resultats.append({"personne": personne, "reponse": texte})
        print(f"{i + 1}/{len(panel)} {'ok' if texte else 'échec'}", flush=True)
json.dump(resultats, open(os.path.join(sortie, "jugements.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{sum(1 for r in resultats if r['reponse'])} jugements sur {len(panel)}")
