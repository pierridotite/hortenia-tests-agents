#!/usr/bin/env bash
# Transforme le build Android d'Expo en APK installable sur l'émulateur.
# Un .aab (build du Play Store) passe par bundletool, signé avec une clé de
# debug : suffisant pour l'émulateur, la connexion Google ne marchera pas.
set -euo pipefail
entree="$1"; sortie="$2"; ext="${3:-aab}"
if [ "$ext" = "apk" ]; then cp "$entree" "$sortie"; exit 0; fi
curl -sSL -o bundletool.jar https://github.com/google/bundletool/releases/download/1.17.2/bundletool-all-1.17.2.jar
mkdir -p ~/.android
[ -f ~/.android/debug.keystore ] || keytool -genkeypair -keystore ~/.android/debug.keystore -storepass android -keypass android \
  -alias androiddebugkey -keyalg RSA -keysize 2048 -validity 10000 -dname "CN=Android Debug,O=Android,C=US" >/dev/null 2>&1
cp "$entree" app.aab
java -jar bundletool.jar build-apks --bundle=app.aab --output=app.apks --mode=universal \
  --ks="$HOME/.android/debug.keystore" --ks-pass=pass:android --ks-key-alias=androiddebugkey --key-pass=pass:android
unzip -o -q app.apks universal.apk
mv universal.apk "$sortie"
ls -la "$sortie"
