#!/usr/bin/env bash
# Chiffre le dossier resultats avec la clé publique du dépôt : le dépôt est
# public, seul le détenteur de la clé privée peut lire captures et rapport.
set -euo pipefail
mkdir -p resultats resultats.chiffres
tar czf resultats.tgz resultats
CLE=$(openssl rand -hex 32)
echo "::add-mask::$CLE"
openssl enc -aes-256-cbc -pbkdf2 -salt -in resultats.tgz -out resultats.chiffres/resultats.tgz.enc -pass "pass:$CLE"
printf '%s' "$CLE" | openssl pkeyutl -encrypt -pubin -inkey cle_publique.pem \
  -pkeyopt rsa_padding_mode:oaep -out resultats.chiffres/cle.bin
rm -f resultats.tgz
ls -la resultats.chiffres
