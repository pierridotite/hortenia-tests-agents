#!/usr/bin/env bash
# Installe sur l'émulateur l'app téléchargée dans apk/ (.apk simple, ou
# .xapk/.apks = archive de l'APK de base et de ses morceaux).
set -uo pipefail
f=$(ls apk/* | head -1)
case "$f" in
  *.apk)
    adb install -r -g -i com.android.vending "$f" || adb install -r -g "$f" ;;
  *)
    rm -rf xapk && mkdir xapk && unzip -o -q "$f" -d xapk
    mapfile -t morceaux < <(find xapk -maxdepth 1 -name '*.apk' | sort)
    echo "Morceaux : ${morceaux[*]}"
    adb install-multiple -r -g -i com.android.vending "${morceaux[@]}" \
      || adb install-multiple -r -g "${morceaux[@]}" \
      || { mapfile -t m2 < <(printf '%s\n' "${morceaux[@]}" | grep -vE 'config\.(arm|x86|mips)' ); \
           adb install-multiple -r -g "${m2[@]}" $(printf '%s\n' "${morceaux[@]}" | grep -E 'config\.(arm64|x86_64)' | head -1); }
    # Données de jeu éventuelles (OBB)
    if [ -d xapk/Android/obb ]; then adb push xapk/Android/obb /sdcard/Android/ >/dev/null; fi ;;
esac
