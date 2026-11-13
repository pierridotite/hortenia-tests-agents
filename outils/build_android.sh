#!/usr/bin/env bash
# Côté Linux : construit l'app Android (aab signé avec la clé gardée par
# Expo) avec « eas build --local », la dépose chez Expo (eas upload) pour les
# testeurs, et l'envoie en test interne Google Play si ENVOYER=true. Tout ce
# que sortent npm et Gradle va dans resultats/build-android.log, chiffré
# ensuite : le journal public ne montre que les étapes.
# Usage : bash outils/build_android.sh <dossier Frontend de l'app>
set -uo pipefail
APP=$1
ICI=$(pwd)
mkdir -p resultats "$RUNNER_TEMP/sortie"
LOG="$ICI/resultats/build-android.log"
echo() { builtin echo "$@"; builtin echo "== $*" >> "$LOG"; }
echec() { echo "ÉCHEC : $1 (détail dans le journal chiffré)"; builtin echo "Échec : $1" >> "$GITHUB_STEP_SUMMARY"; exit 1; }
cd "$APP" || exit 1
export EAS_NO_VCS=1 CI=1
VERSION=$(python3 -c "import json;e=json.load(open('app.json'))['expo'];print(e['version'],'(Android',str(e['android']['versionCode'])+')')")
echo "Version : $VERSION"
SORTIE="$RUNNER_TEMP/sortie/hortenia.aab"
if [ -n "${PLAY_SERVICE_ACCOUNT_JSON:-}" ]; then
  mkdir -p credentials
  printf '%s' "$PLAY_SERVICE_ACCOUNT_JSON" > credentials/play-service-account.json
fi

# Mémoire de Gradle : R8 manque de place avec les 2 Go du projet (réglage
# utilisateur, prioritaire sur gradle.properties du projet)
mkdir -p ~/.gradle
printf 'org.gradle.jvmargs=-Xmx8g -XX:MaxMetaspaceSize=1g\norg.gradle.workers.max=4\n' > ~/.gradle/gradle.properties

echo "npm ci"
npm ci --no-audit --no-fund >> "$LOG" 2>&1 || echec "npm ci"
echo "eas build --local (profil production)"
debut=$(date +%s)
eas build --local --platform android --profile production --non-interactive --output "$SORTIE" >> "$LOG" 2>&1 || echec "build Gradle"
echo "Build fait en $(( ($(date +%s) - debut) / 60 )) min ($(du -h "$SORTIE" | cut -f1))"

# Build store (ENVOYER=true, secret TikTok possible) : jamais déposé chez
# Expo, les testeurs IA ne doivent pas le reprendre
if [ "${ENVOYER:-false}" != true ]; then
  if [ -n "${TESTS_JETON:-}" ]; then
    # Quota d'envois d'Expo épuisé (offre gratuite, 13/11) : build chiffré avec
    # TESTS_JETON, en artefact du run ; les testeurs le reprennent par build_id=gh:<run>
    mkdir -p "$ICI/app-banc"
    openssl enc -aes-256-cbc -pbkdf2 -salt -pass env:TESTS_JETON -in "$SORTIE" -out "$ICI/app-banc/$(basename "$SORTIE").enc" || echec "chiffrement du build"
    ID="gh:$GITHUB_RUN_ID"
  else
    eas upload --platform android --build-path "$SORTIE" --non-interactive --json > "$RUNNER_TEMP/upload.json" 2>> "$LOG" || echec "dépôt chez Expo"
    ID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['url'].rstrip('/').split('/')[-1])" "$RUNNER_TEMP/upload.json")
  fi
  echo "Build Android déposé : $ID"
  builtin echo "Build Android $VERSION : \`$ID\` (à passer en build_id à android-claude.yml)" >> "$GITHUB_STEP_SUMMARY"
fi

if [ "${ENVOYER:-false}" = true ]; then
  [ -s credentials/play-service-account.json ] || echec "secret PLAY_SERVICE_ACCOUNT_JSON absent, envoi Google Play impossible"
  echo "Envoi Google Play (test interne)"
  # Directement par l'API Play : la file d'EAS Submit a bloqué 50 min le 12/11
  python3 -m pip install -q --break-system-packages google-auth requests >> "$LOG" 2>&1
  python3 "$ICI/outils/play_envoi.py" "$SORTIE" credentials/play-service-account.json >> "$LOG" 2>&1 || echec "envoi Google Play"
  echo "Envoyé en test interne Google Play"
  builtin echo "aab $VERSION envoyé en test interne Google Play" >> "$GITHUB_STEP_SUMMARY"
fi
rm -rf credentials
