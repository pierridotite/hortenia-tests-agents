#!/usr/bin/env bash
# Rejoue les parcours maestro/ sur l'appareil déjà démarré (émulateur Android
# ou simulateur iOS, UDID dans l'environnement). Tout le détail (journal,
# captures, rapport JUnit) va dans resultats/, chiffré ensuite : le journal
# public ne montre que le verdict de chaque parcours.
#   PLATEFORME=android|ios  MAESTRO_FLOWS (vide = tous)
set -uo pipefail
mkdir -p resultats
MDP="Potager-$(openssl rand -hex 4)!"
echo "::add-mask::$MDP"
# Sans « : » ni « ? » (l'appli y met une espace insécable)
# Même texte sur les deux plateformes : chacune réagit au premier post du passage qu'elle trouve
TEXTE_POST="Banc Maestro ${RUN_ID:-0}, post de test pour les réactions."
if [ "$PLATEFORME" = android ]; then
  timeout 120 adb wait-for-device
  # PostHog injoignable depuis l'émulateur (même contrôle que lancer_claude.sh)
  r=$(adb shell ping -c 1 -W 2 eu.i.posthog.com 2>&1 | head -1)
  ip=$(printf '%s' "$r" | grep -oE '\(([0-9]{1,3}\.){3}[0-9]{1,3}\)' | head -1 | tr -d '()')
  case "$ip" in ""|0.0.0.0|127.*) echo "PostHog bloqué" ;; *) echo "PostHog joignable ($ip) : arrêt"; exit 1 ;; esac
  if [ "$(adb shell getprop persist.sys.locale | tr -d '\r')" != fr-FR ]; then
    # Appels bornés (18/11 : bloqué ici jusqu'à la limite du job, comme lancer_claude.sh)
    timeout 60 adb root >/dev/null 2>&1; sleep 3; timeout 120 adb wait-for-device
    timeout 30 adb shell "setprop persist.sys.locale fr-FR; setprop ctl.restart zygote"
    sleep 10; timeout 120 adb wait-for-device
    for i in $(seq 1 60); do [ "$(timeout 10 adb shell getprop sys.boot_completed | tr -d '\r')" = 1 ] && break; sleep 3; done
    if [ "$(timeout 10 adb shell getprop sys.boot_completed | tr -d '\r')" != 1 ]; then
      echo "redémarrage de zygote bloqué : redémarrage complet de l'émulateur"
      timeout 60 adb reboot; sleep 20; timeout 300 adb wait-for-device
      for i in $(seq 1 100); do [ "$(timeout 10 adb shell getprop sys.boot_completed | tr -d '\r')" = 1 ] && break; sleep 3; done
    fi
  fi
  [ -n "${POSITION:-}" ] && adb emu geo fix "${POSITION#*,}" "${POSITION%,*}" >/dev/null 2>&1
  timeout 300 adb install -r app.apk >/dev/null || { echo "installation impossible"; exit 1; }
  adb logcat -c
  APPAREIL_OPT=()
else
  ip=$(dscacheutil -q host -a name eu.i.posthog.com | awk '/ip_address/{print $2; exit}')
  if curl -s -m 8 -o /dev/null https://eu.i.posthog.com/decide/; then echo "PostHog joignable : arrêt"; exit 1; fi
  echo "PostHog bloqué"
  APPDIR=$(find app -maxdepth 3 -name "*.app" -type d | head -1)
  xcrun simctl install "$UDID" "$APPDIR" || { echo "installation impossible"; exit 1; }
  [ -n "${POSITION:-}" ] && xcrun simctl location "$UDID" set "$POSITION" 2>/dev/null
  APPAREIL_OPT=(--device "$UDID")
fi
python3 outils/maestro_post.py creer "$TEXTE_POST" || echo "post du banc non créé : le parcours des réactions échouera"
FLOWS=()
for f in ${MAESTRO_FLOWS//,/ }; do FLOWS+=("maestro/$f.yaml"); done
[ ${#FLOWS[@]} -eq 0 ] && FLOWS=(maestro/)
maestro "${APPAREIL_OPT[@]}" test "${FLOWS[@]}" \
  -e EMAIL="success+maestro-${PLATEFORME}-${RUN_ID:-0}@simulator.amazonses.com" \
  -e MOT_DE_PASSE="$MDP" -e TEXTE_POST="$TEXTE_POST" \
  --format junit --output resultats/rapport.xml --test-output-dir resultats/sortie \
  > resultats/maestro.log 2>&1
CODE=$?
python3 outils/maestro_post.py supprimer
[ "$PLATEFORME" = android ] && adb logcat -d -s ReactNativeJS AndroidRuntime > resultats/logcat.txt 2>/dev/null
python3 - <<'PY' | tee -a "${GITHUB_STEP_SUMMARY:-/dev/null}"
import xml.etree.ElementTree as ET, os
plat = os.environ.get("PLATEFORME")
try:
    cas = ET.parse("resultats/rapport.xml").getroot().iter("testcase")
except Exception:
    print(f"- {plat} : pas de rapport Maestro (voir maestro.log, chiffré)"); raise SystemExit
for c in cas:
    ko = c.find("failure") is not None or c.find("error") is not None
    print(f"- {plat} : {c.get('name')} : {'ÉCHEC' if ko else 'réussi'} ({float(c.get('time') or 0):.0f} s)")
PY
exit $CODE
