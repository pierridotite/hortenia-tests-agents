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
# L'émulateur x86_64 (Android 14) exécute aussi le code ARM 64 bits, pas le
# 32 bits : variante arm64 d'abord, puis x86_64, puis celle par défaut.
for arch in arm64-v8a x86_64 ""; do
  opt="acknowledge_dangers=true${arch:+,arch=$arch}"
  for essai in 1 2; do
    outils-bin/apkeep -a "$paquet" -d apk-pure -o "$opt" apk/ && ls apk/* >/dev/null 2>&1 && break 2
    echo "Téléchargement ($arch) essai $essai échoué"; sleep $((essai * 10))
  done
done
ls -la apk/
ls apk/* >/dev/null 2>&1 || { echo "Aucun APK pour $paquet"; exit 1; }
