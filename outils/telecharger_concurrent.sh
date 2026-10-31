#!/usr/bin/env bash
# Télécharge l'APK public d'une app concurrente (miroir APKPure, sans compte
# Google) avec apkeep (EFF). Résultat : dossier apk/ avec un .apk ou un .xapk.
# Usage : bash outils/telecharger_concurrent.sh <paquet>
set -euo pipefail
paquet="$1"
mkdir -p apk outils-bin
if [ ! -x outils-bin/apkeep ]; then
  curl -sSL --retry 3 -o outils-bin/apkeep \
    https://github.com/EFForg/apkeep/releases/latest/download/apkeep-x86_64-unknown-linux-gnu
  chmod +x outils-bin/apkeep
fi
for essai in 1 2 3; do
  outils-bin/apkeep -a "$paquet" -d apk-pure apk/ && ls apk/* >/dev/null 2>&1 && break
  echo "Téléchargement $essai échoué, nouvel essai"; sleep $((essai * 10))
done
ls -la apk/
ls apk/* >/dev/null 2>&1 || { echo "Aucun APK pour $paquet"; exit 1; }
