#!/usr/bin/env bash
# Lancé une fois l'émulateur démarré : installe l'app et la photo de test,
# puis confie l'émulateur à Claude Code. Sa sortie va dans resultats/
# (chiffré ensuite), jamais dans le journal public.
set -uo pipefail
adb wait-for-device
# PostHog doit être injoignable depuis l'émulateur, sinon on n'y va pas.
# Bloqué = le nom ne se résout pas, ou se résout en 0.0.0.0 (que
# l'émulateur rend parfois en 127.0.0.1). Une vraie
# adresse IP arrête tout.
for i in 1 2 3 4 5 6; do
  r=$(adb shell ping -c 1 -W 2 eu.i.posthog.com 2>&1 | head -1)
  ip=$(printf '%s' "$r" | grep -oE '\(([0-9]{1,3}\.){3}[0-9]{1,3}\)' | head -1 | tr -d '()')
  echo "Vérification PostHog $i : ${r:-sans réponse}"
  case "$ip" in
    "") [ "$i" -ge 3 ] && { echo "PostHog bloqué (nom non résolu)"; break; } ;;
    0.0.0.0|127.*) echo "PostHog bloqué ($ip)"; break ;;
    *) echo "PostHog joignable depuis l'émulateur ($ip) : test annulé"; exit 1 ;;
  esac
  sleep 5
done
adb shell ping -c 1 -W 3 api.expo.dev >/dev/null 2>&1 && echo "réseau OK" || echo "attention : pas de réseau dans l'émulateur"
adb install -r -g app.apk || adb install -r app.apk
mkdir -p photos resultats
[ -s photos/feuille-tomate-mildiou.jpg ] || curl -sSL --retry 3 -A "hortenia-tests-agents (github.com/pierridotite/hortenia-tests-agents)" \
  -o photos/feuille-tomate-mildiou.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/Tomato_late_blight.jpg?width=1200" || true
adb push photos/feuille-tomate-mildiou.jpg /sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1 \
  && adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1
# Taille du texte du téléphone (réglage Accessibilité), pour les profils seniors
[ -n "${TAILLE_TEXTE:-}" ] && adb shell settings put system font_scale "$TAILLE_TEXTE"
[ "${THEME:-clair}" = sombre ] && adb shell cmd uimode night yes
# Position du jardin de la persona (latitude,longitude)
[ -n "${POSITION:-}" ] && adb emu geo fix "${POSITION#*,}" "${POSITION%,*}" >/dev/null 2>&1
# Localisation de la persona (personas.json) : refus = autorisation de position
# retirée (install -g l'accorde) pour que l'app la demande ; sans_gps = position
# coupée sur le téléphone
CONSIGNE_POSITION=""
case "${LOCALISATION:-}" in
  refus)
    adb shell pm revoke com.hortenia.app android.permission.ACCESS_FINE_LOCATION 2>/dev/null || true
    adb shell pm revoke com.hortenia.app android.permission.ACCESS_COARSE_LOCATION 2>/dev/null || true
    CONSIGNE_POSITION=" Localisation de ce test : ta persona refuse de partager sa position. À chaque demande d'autorisation de position, réponds « Ne pas autoriser » (ou « Refuser »), puis termine l'onboarding sans position (ville tapée à la main). Note si l'app explique pourquoi elle demande, si un bouton tourne sans fin, si « Placer mon jardin ici » reste en chargement ou si l'app redemande avec insistance, et vérifie ensuite que la météo et le planning marchent avec la ville choisie." ;;
  sans_gps)
    adb shell pm revoke com.hortenia.app android.permission.ACCESS_FINE_LOCATION 2>/dev/null || true
    adb shell pm revoke com.hortenia.app android.permission.ACCESS_COARSE_LOCATION 2>/dev/null || true
    adb shell cmd location set-location-enabled false 2>/dev/null || adb shell settings put secure location_mode 0
    CONSIGNE_POSITION=" Localisation de ce test : ce téléphone ne donne aucune position (pas de signal GPS). À l'étape « Où est votre jardin ? », accepte la demande d'autorisation, touche « Position approximative » puis « Position précise », capture toutes les 5 s et note combien de secondes passent avant un message ou un retour à la normale (plus de 20 s = bug). Vérifie que « Placer mon jardin ici » ne reste pas en chargement, puis tape une ville pendant qu'une recherche de position tourne encore, et termine l'onboarding avec cette ville. Sur Android, si l'app propose d'activer la localisation du téléphone, refuse : le GPS reste coupé." ;;
esac
[ -n "${LOCALISATION:-}" ] && echo "Localisation : $LOCALISATION"
echo "Téléphone : ${APPAREIL:-Pixel 6, Android 14} (texte x${TAILLE_TEXTE:-1.0}, thème ${THEME:-clair})"
adb logcat -c
claude -p "Lis ${CONSIGNES:-CONSIGNES_CLAUDE.md} et personas.json, puis fais la mission jusqu'au rapport final. PERSONAS='${PERSONAS:-}' RUN_ID='${RUN_ID}'. Téléphone de ce test : ${APPAREIL:-Pixel 6, Android 14}, taille du texte x${TAILLE_TEXTE:-1.0}, thème ${THEME:-clair} ; signale ce qui tient à l'écran (texte coupé, bouton hors écran, mise en page cassée).${CONSIGNE_POSITION}" \
  --model "${MODELE:-claude-sonnet-5-5}" --max-turns 500 --output-format json \
  --allowedTools "Bash(adb:*),Bash(python3 outils/ecran.py:*),Bash(python3 outils/ecrire.py:*),Bash(sleep:*),Read,Write,Edit" \
  > resultats/claude-sortie.json 2> resultats/claude-erreurs.txt
echo "Claude terminé (code $?), $(ls resultats | wc -l) éléments dans resultats/"
