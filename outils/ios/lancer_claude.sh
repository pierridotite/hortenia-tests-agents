#!/usr/bin/env bash
# Côté Mac, simulateur démarré : installe l'app et la photo de test, règle
# l'apparence et la taille du texte, vérifie que PostHog est coupé, puis
# confie le simulateur à Claude Code. Sortie dans resultats/ (chiffré
# ensuite), jamais dans le journal public.
# ESSAI=1 : pas d'app, Claude vérifie seulement les outils sur Réglages.
set -uo pipefail
: "${UDID:?}"
# PostHog injoignable depuis le Mac (le simulateur passe par lui), sinon on n'y va pas
ip=$(dscacheutil -q host -a name eu.i.posthog.com | awk '/ip_address/{print $2; exit}')
echo "PostHog résolu en : ${ip:-rien}"
if curl -s -m 8 -o /dev/null https://eu.i.posthog.com/decide/; then
  echo "PostHog joignable depuis le Mac : test annulé"; exit 1
fi
echo "PostHog bloqué"
curl -s -m 8 -o /dev/null https://api.expo.dev && echo "réseau OK" || echo "attention : pas de réseau"

xcrun simctl ui "$UDID" appearance "${THEME:-light}"
[ -n "${TAILLE_TEXTE:-}" ] && xcrun simctl ui "$UDID" content_size "$TAILLE_TEXTE"
xcrun simctl location "$UDID" set "${POSITION:-45.7640,4.8357}" 2>/dev/null || true
mkdir -p photos resultats
[ -s photos/feuille-tomate-mildiou.jpg ] || curl -sSL --retry 3 -A "hortenia-tests-agents (github.com/pierridotite/hortenia-tests-agents)" \
  -o photos/feuille-tomate-mildiou.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/Tomato_late_blight.jpg?width=1200" || true
xcrun simctl addmedia "$UDID" photos/feuille-tomate-mildiou.jpg || true
echo "Appareil : ${APPAREIL:-?} (texte ${TAILLE_TEXTE:-large}, thème ${THEME:-light})"

if [ "${ESSAI:-0}" = 1 ]; then
  xcrun simctl launch "$UDID" com.apple.Preferences
  CONSIGNE="Lis outils/ios/ESSAI.md et fais l'essai jusqu'au bout."
else
  APPDIR=$(find app -maxdepth 3 -name "*.app" -type d | head -1)
  xcrun simctl install "$UDID" "$APPDIR" || { echo "installation impossible"; exit 1; }
  xcrun simctl launch "$UDID" com.hortenia.app
  CONSIGNE="Lis CONSIGNES_CLAUDE_IOS.md et personas.json, puis fais la mission jusqu'au rapport final. PERSONAS='${PERSONAS:-}' RUN_ID='${RUN_ID}'. Appareil de ce test : ${APPAREIL}, taille du texte ${TAILLE_TEXTE:-large}, thème ${THEME:-light} ; signale ce qui tient à l'écran (texte coupé, bouton hors écran, sous l'encoche ou la barre d'accueil, mise en page cassée)."
fi
sleep 8
# Première capture : mémorise la taille de l'écran en points pour les outils
python3 outils/ios/ecran.py "$RUNNER_TEMP/amorce" 00 > /dev/null 2>&1 || true
claude -p "$CONSIGNE" \
  --model "${MODELE:-claude-sonnet-5-5}" --max-turns 500 --output-format json \
  --allowedTools "Bash(bash outils/ios/geste.sh:*),Bash(python3 outils/ios/ecran.py:*),Bash(python3 outils/ios/ecrire.py:*),Bash(sleep:*),Read,Write,Edit" \
  > resultats/claude-sortie.json 2> resultats/claude-erreurs.txt
echo "Claude terminé (code $?), $(ls resultats | wc -l) éléments dans resultats/"
