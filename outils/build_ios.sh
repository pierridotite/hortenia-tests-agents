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
else
  PROFIL=production; SORTIE="$RUNNER_TEMP/sortie/hortenia.ipa"
  if [ -n "${ASC_API_KEY_P8:-}" ]; then
    mkdir -p credentials
    printf '%s\n' "$ASC_API_KEY_P8" | tr -d '\r' > credentials/AuthKey_K78XTPTD68.p8
  fi
fi

echo "npm ci"
npm ci --no-audit --no-fund >> "$LOG" 2>&1 || echec "npm ci"
echo "eas build --local (profil $PROFIL)"
debut=$(date +%s)
eas build --local --platform ios --profile "$PROFIL" --non-interactive --output "$SORTIE" >> "$LOG" 2>&1 || echec "build Xcode"
echo "Build fait en $(( ($(date +%s) - debut) / 60 )) min ($(du -h "$SORTIE" | cut -f1))"

if [ "$CIBLE" = simulateur ]; then
  eas upload --platform ios --build-path "$SORTIE" --non-interactive --json > "$RUNNER_TEMP/upload.json" 2>> "$LOG" || echec "dépôt chez Expo"
  ID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['url'].rstrip('/').split('/')[-1])" "$RUNNER_TEMP/upload.json")
  echo "Build simulateur déposé chez Expo : $ID"
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
