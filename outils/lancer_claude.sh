#!/usr/bin/env bash
# Lancé une fois l'émulateur démarré : installe l'app et la photo de test,
# puis confie l'émulateur à Claude Code. Sa sortie va dans resultats/
# (chiffré ensuite), jamais dans le journal public.
set -uo pipefail
adb wait-for-device
adb install -r -g app.apk || adb install -r app.apk
mkdir -p photos resultats
[ -s photos/feuille-tomate-mildiou.jpg ] || curl -sSL --retry 3 -A "hortenia-tests-agents (github.com/pierridotite/hortenia-tests-agents)" \
  -o photos/feuille-tomate-mildiou.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/Tomato_late_blight.jpg?width=1200" || true
adb push photos/feuille-tomate-mildiou.jpg /sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1 \
  && adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1
adb logcat -c
claude -p "Lis CONSIGNES_CLAUDE.md et personas.json, puis fais la mission jusqu'au rapport final. PERSONAS='${PERSONAS:-}' RUN_ID='${RUN_ID}'." \
  --model "${MODELE:-claude-sonnet-5-5}" --max-turns 500 --output-format json \
  --allowedTools "Bash(adb:*),Bash(python3 outils/ecran.py:*),Bash(python3 outils/ecrire.py:*),Bash(sleep:*),Read,Write,Edit" \
  > resultats/claude-sortie.json 2> resultats/claude-erreurs.txt
echo "Claude terminé (code $?), $(ls resultats | wc -l) éléments dans resultats/"
