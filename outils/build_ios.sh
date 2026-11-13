#!/usr/bin/env bash
# Côté Mac : construit l'app iOS (cible simulateur ou store) avec
# « eas build --local ». Tout ce que sortent npm et Xcode va dans
# resultats/build-<cible>.log, chiffré ensuite : le journal public ne
# montre que les étapes.
# Usage : bash outils/build_ios.sh <dossier Frontend de l'app>
set -uo pipefail
APP=$1
ICI=$(pwd)
mkdir -p resultats "$RUNNER_TEMP/sortie"
LOG="$ICI/resultats/build-$CIBLE.log"
echo() { builtin echo "$@"; builtin echo "== $*" >> "$LOG"; }
echec() { echo "ÉCHEC : $1 (détail dans le journal chiffré)"; builtin echo "Échec : $1" >> "$GITHUB_STEP_SUMMARY"; exit 1; }
cd "$APP" || exit 1
export EAS_NO_VCS=1 CI=1
VERSION=$(python3 -c "import json;e=json.load(open('app.json'))['expo'];print(e['version'],'(iOS',e['ios']['buildNumber']+')')")
echo "Version : $VERSION, cible $CIBLE"

if [ "$CIBLE" = simulateur ]; then
  # Profil de test : comme production (mêmes variables), mais pour le simulateur
  python3 - <<'EOF'
import json
d = json.load(open("eas.json"))
d["build"]["simulateur-tests"] = {"extends": "production", "distribution": "internal",
                                  "environment": "production", "ios": {"simulator": True}}
json.dump(d, open("eas.json", "w"), indent=2)
EOF
  PROFIL=simulateur-tests; SORTIE="$RUNNER_TEMP/sortie/hortenia-simulateur.tar.gz"
  # Simulateurs des Mac du dépôt = Apple Silicon : arm64 seulement. Le
  # compilateur Swift de Xcode 26.3 plante sur la tranche x86_64 de RevenueCat
  # (9/11), et c'est deux fois moins long.
  printf 'EXCLUDED_ARCHS[sdk=iphonesimulator*] = x86_64\nONLY_ACTIVE_ARCH = YES\n' > "$RUNNER_TEMP/arm64.xcconfig"
  export XCODE_XCCONFIG_FILE="$RUNNER_TEMP/arm64.xcconfig"
else
  PROFIL=production; SORTIE="$RUNNER_TEMP/sortie/hortenia.ipa"
  # Groupe d'apps du widget : coché à la main sur developer.apple.com (l'API
  # App Store Connect ne sait pas l'attacher ; la synchro d'EAS échoue, 9/11).
  export EXPO_NO_CAPABILITY_SYNC=1
  if [ -n "${ASC_API_KEY_P8:-}" ]; then
    mkdir -p credentials
    printf '%s\n' "$ASC_API_KEY_P8" | tr -d '\r' > credentials/AuthKey_K78XTPTD68.p8
  fi
fi

echo "npm ci"
npm ci --no-audit --no-fund >> "$LOG" 2>&1 || echec "npm ci"

# Identifiants d'une nouvelle cible (widget, 9/11) : EAS ne les crée pas en
# non interactif. Avec IDENTIFIANTS=true, « eas credentials:configure-build »
# tourne une fois en interactif, piloté par expect, authentifié par la clé
# App Store Connect (réutilise le certificat de distribution, crée les profils
# et le groupe d'apps). Les builds suivants repassent en non interactif.
if [ "$CIBLE" = store ] && [ "${IDENTIFIANTS:-false}" = true ]; then
  [ -s credentials/AuthKey_K78XTPTD68.p8 ] || echec "secret ASC_API_KEY_P8 absent"
  export EXPO_ASC_API_KEY_PATH="$PWD/credentials/AuthKey_K78XTPTD68.p8" EXPO_ASC_KEY_ID=K78XTPTD68 \
         EXPO_ASC_ISSUER_ID=b959d263-8901-4728-981d-4a1ae2458181 EXPO_APPLE_TEAM_TYPE=COMPANY_OR_ORGANIZATION
  pip3 install -q --break-system-packages "pyjwt[crypto]" >> "$LOG" 2>&1 || pip3 install -q "pyjwt[crypto]" >> "$LOG" 2>&1
  EXPO_APPLE_TEAM_ID=$(python3 "$ICI/outils/equipe_apple.py" "$EXPO_ASC_API_KEY_PATH" "$EXPO_ASC_KEY_ID" "$EXPO_ASC_ISSUER_ID" 2>> "$LOG") || echec "équipe Apple introuvable"
  export EXPO_APPLE_TEAM_ID
  echo "Identifiants des cibles iOS (interactif piloté)"
  unset CI
  expect -c '
    set timeout 600
    log_user 1
    spawn eas credentials:configure-build -p ios -e production
    expect {
      -re "Reuse this distribution certificate" { send "y\r"; exp_continue }
      -re "reuse the original profile"          { send "y\r"; exp_continue }
      -re "\\(Y/n\\)"                         { send "y\r"; exp_continue }
      -re "\\(y/N\\)"                         { send "n\r"; exp_continue }
      -re "Apple Team ID"                        { send "$env(EXPO_APPLE_TEAM_ID)\r"; exp_continue }
      timeout { exit 2 }
      eof
    }
    catch wait r; exit [lindex $r 3]
  ' >> "$LOG" 2>&1 || echec "identifiants des cibles iOS"
  export CI=1
  echo "Identifiants des cibles iOS : faits"
fi
echo "eas build --local (profil $PROFIL)"
debut=$(date +%s)
eas build --local --platform ios --profile "$PROFIL" --non-interactive --output "$SORTIE" >> "$LOG" 2>&1 || echec "build Xcode"
echo "Build fait en $(( ($(date +%s) - debut) / 60 )) min ($(du -h "$SORTIE" | cut -f1))"

if [ "$CIBLE" = simulateur ]; then
  if [ -n "${TESTS_JETON:-}" ]; then
    # Quota d'envois d'Expo épuisé (offre gratuite, 13/11) : build chiffré avec
    # TESTS_JETON, en artefact du run ; les testeurs le reprennent par build_id=gh:<run>
    mkdir -p "$ICI/app-banc"
    openssl enc -aes-256-cbc -pbkdf2 -salt -pass env:TESTS_JETON -in "$SORTIE" -out "$ICI/app-banc/$(basename "$SORTIE").enc" || echec "chiffrement du build"
    ID="gh:$GITHUB_RUN_ID"
  else
    eas upload --platform ios --build-path "$SORTIE" --non-interactive --json > "$RUNNER_TEMP/upload.json" 2>> "$LOG" || echec "dépôt chez Expo"
    ID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['url'].rstrip('/').split('/')[-1])" "$RUNNER_TEMP/upload.json")
  fi
  echo "Build simulateur déposé : $ID"
  builtin echo "Build simulateur $VERSION : \`$ID\` (à passer en build_id à ios-claude.yml)" >> "$GITHUB_STEP_SUMMARY"
  builtin echo "build_id=$ID" >> "$GITHUB_OUTPUT"
elif [ "${ENVOYER:-false}" = true ]; then
  [ -s credentials/AuthKey_K78XTPTD68.p8 ] || echec "secret ASC_API_KEY_P8 absent, envoi TestFlight impossible"
  echo "Envoi TestFlight"
  eas submit --platform ios --profile production --path "$SORTIE" --non-interactive >> "$LOG" 2>&1 || echec "envoi TestFlight"
  echo "Envoyé dans TestFlight"
  builtin echo "ipa $VERSION envoyée dans TestFlight" >> "$GITHUB_STEP_SUMMARY"
else
  builtin echo "ipa $VERSION construite (non envoyée)" >> "$GITHUB_STEP_SUMMARY"
fi
rm -rf credentials
