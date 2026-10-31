#!/usr/bin/env bash
# Lancé une fois l'émulateur démarré : met le téléphone en français (Paris),
# installe l'app étudiée et la photo de test, puis confie l'émulateur à
# Claude Code avec CONSIGNES_CONCURRENTS.md. Sortie dans resultats/ (chiffrée
# ensuite), jamais dans le journal public.
set -uo pipefail
adb wait-for-device
# Analytics d'Hortenia coupés (la référence ne doit rien envoyer à PostHog)
for i in 1 2 3 4 5 6; do
  r=$(adb shell ping -c 1 -W 2 eu.i.posthog.com 2>&1 | head -1)
  ip=$(printf '%s' "$r" | grep -oE '\(([0-9]{1,3}\.){3}[0-9]{1,3}\)' | head -1 | tr -d '()')
  case "$ip" in
    "") [ "$i" -ge 3 ] && { echo "PostHog bloqué (nom non résolu)"; break; } ;;
    0.0.0.0|127.*) echo "PostHog bloqué ($ip)"; break ;;
    *) echo "PostHog joignable depuis l'émulateur ($ip) : arrêt"; exit 1 ;;
  esac
  sleep 5
done
adb shell ping -c 1 -W 3 google.com >/dev/null 2>&1 && echo "réseau OK" || echo "attention : pas de réseau dans l'émulateur"
echo "Langue : $(adb shell getprop persist.sys.locale) ; fuseau : $(adb shell getprop persist.sys.timezone)"
adb shell service call alarm 3 s16 Europe/Paris >/dev/null 2>&1 || true

if [ "$PAQUET" = com.hortenia.app ]; then
  adb install -r -g app.apk || adb install -r app.apk
else
  bash outils/installer_concurrent.sh
fi
adb shell pm list packages | grep -qx "package:$PAQUET" || { echo "Installation de $PAQUET échouée"; mkdir -p resultats; echo "installation échouée" > resultats/ECHEC.txt; exit 0; }
echo "Version installée : $(adb shell dumpsys package "$PAQUET" | grep -m1 versionName)"
# L'app en français même si le téléphone ne l'est pas
adb shell cmd locale set-app-locales "$PAQUET" --user 0 --locales fr-FR >/dev/null 2>&1 || true

mkdir -p photos resultats
curl -sSL --retry 3 -A "hortenia-tests-agents (github.com/pierridotite/hortenia-tests-agents)" \
  -o photos/feuille-tomate-mildiou.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/Tomato_late_blight.jpg?width=1200" || true
adb push photos/feuille-tomate-mildiou.jpg /sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1 \
  && adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1
adb emu geo fix 4.8357 45.7640 >/dev/null 2>&1   # Lyon
adb logcat -c
claude -p "Lis CONSIGNES_CONCURRENTS.md, puis fais la mission jusqu'à la fiche finale. App étudiée : ${NOM} (paquet ${PAQUET}, id ${APP}). RUN_ID='${RUN_ID}'." \
  --model "${MODELE:-claude-sonnet-5-5}" --max-turns 450 --output-format json \
  --allowedTools "Bash(adb:*),Bash(python3 outils/ecran.py:*),Bash(python3 outils/ecrire.py:*),Bash(sleep:*),Read,Write,Edit" \
  > resultats/claude-sortie.json 2> resultats/claude-erreurs.txt
echo "Claude terminé (code $?), $(find resultats -name '*.png' | wc -l) captures"
