#!/usr/bin/env bash
# Lancé par l'émulateur une fois démarré : installe l'app, dépose une photo
# de feuille de tomate malade dans la galerie, puis lance les agents.
set -uo pipefail
adb wait-for-device
adb install -r -g app.apk || adb install -r app.apk
mkdir -p photos
[ -s photos/feuille-tomate-mildiou.jpg ] || curl -sSL --retry 3 -A "hortenia-tests-agents (github.com/pierridotite/hortenia-tests-agents)" \
  -o photos/feuille-tomate-mildiou.jpg "https://commons.wikimedia.org/wiki/Special:FilePath/Tomato_late_blight.jpg?width=1200" || true
adb push photos/feuille-tomate-mildiou.jpg /sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1 \
  && adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/feuille-tomate.jpg >/dev/null 2>&1
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
python agent.py
