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

eas upload --platform android --build-path "$SORTIE" --non-interactive --json > "$RUNNER_TEMP/upload.json" 2>> "$LOG" || echec "dépôt chez Expo"
ID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['url'].rstrip('/').split('/')[-1])" "$RUNNER_TEMP/upload.json")
echo "Build Android déposé chez Expo : $ID"
builtin echo "Build Android $VERSION : \`$ID\` (à passer en build_id à android-claude.yml)" >> "$GITHUB_STEP_SUMMARY"

if [ "${ENVOYER:-false}" = true ]; then
  [ -s credentials/play-service-account.json ] || echec "secret PLAY_SERVICE_ACCOUNT_JSON absent, envoi Google Play impossible"
  echo "Envoi Google Play (test interne)"
  eas submit --platform android --profile production --path "$SORTIE" --non-interactive >> "$LOG" 2>&1 || echec "envoi Google Play"
  echo "Envoyé en test interne Google Play"
  builtin echo "aab $VERSION envoyé en test interne Google Play" >> "$GITHUB_STEP_SUMMARY"
fi
rm -rf credentials
