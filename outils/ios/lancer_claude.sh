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
# Localisation de la persona (personas.json) : sans_gps = aucune position simulée
if [ "${LOCALISATION:-}" = sans_gps ]; then
  xcrun simctl location "$UDID" clear 2>/dev/null || true
else
  xcrun simctl location "$UDID" set "${POSITION:-45.7640,4.8357}" 2>/dev/null || true
fi
case "${LOCALISATION:-}" in
  refus) CONSIGNE_POSITION=" Localisation de ce test : ta persona refuse de partager sa position. À chaque demande d'autorisation de position, réponds « Ne pas autoriser » (ou « Refuser »), puis termine l'onboarding sans position (ville tapée à la main). Note si l'app explique pourquoi elle demande, si un bouton tourne sans fin, si « Placer mon jardin ici » reste en chargement ou si l'app redemande avec insistance, et vérifie ensuite que la météo et le planning marchent avec la ville choisie." ;;
  sans_gps) CONSIGNE_POSITION=" Localisation de ce test : ce téléphone ne donne aucune position (pas de signal GPS). À l'étape « Où est votre jardin ? », accepte la demande d'autorisation, touche « Position approximative » puis « Position précise », capture toutes les 5 s et note combien de secondes passent avant un message ou un retour à la normale (plus de 20 s = bug). Vérifie que « Placer mon jardin ici » ne reste pas en chargement, puis tape une ville pendant qu'une recherche de position tourne encore, et termine l'onboarding avec cette ville." ;;
  *) CONSIGNE_POSITION="" ;;
esac
[ -n "${LOCALISATION:-}" ] && echo "Localisation : $LOCALISATION"
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
  CONSIGNE="Lis CONSIGNES_CLAUDE_IOS.md et personas.json, puis fais la mission jusqu'au rapport final. PERSONAS='${PERSONAS:-}' RUN_ID='${RUN_ID}'. Appareil de ce test : ${APPAREIL}, taille du texte ${TAILLE_TEXTE:-large}, thème ${THEME:-light} ; signale ce qui tient à l'écran (texte coupé, bouton hors écran, sous l'encoche ou la barre d'accueil, mise en page cassée).${CONSIGNE_POSITION}"
fi
sleep 8
# Première capture : mémorise la taille de l'écran en points pour les outils
python3 outils/ios/ecran.py "$RUNNER_TEMP/amorce" 00 > /dev/null 2>&1 || true
CONSIGNE="$CONSIGNE Le simulateur est déjà démarré et les outils le trouvent seuls (variable UDID déjà définie) : utilise directement les commandes des consignes, sans chercher le simulateur ni lire l'environnement."
claude -p "$CONSIGNE" \
  --model "${MODELE:-claude-sonnet-5-5}" --max-turns 500 --output-format json \
  --allowedTools "Bash(bash outils/ios/geste.sh:*),Bash(python3 outils/ios/ecran.py:*),Bash(python3 outils/ios/ecrire.py:*),Bash(sleep:*),Read,Write,Edit" \
  > resultats/claude-sortie.json 2> resultats/claude-erreurs.txt
echo "Claude terminé (code $?), $(ls resultats | wc -l) éléments dans resultats/"
