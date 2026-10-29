#!/usr/bin/env bash
# Côté Mac : attend le code de l'app chiffré pour sa clé éphémère (branche
# transfert/<run>, déposée par outils/envoyer_source.sh), le déchiffre dans
# le dossier donné. Rien du code n'est affiché.
# Usage : bash outils/recevoir_source.sh <dossier_sortie>
set -euo pipefail
SORTIE=$1
BRANCHE="transfert/$GITHUB_RUN_ID"
T="$RUNNER_TEMP/transfert"
for i in $(seq 1 120); do
  if git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; then
    git fetch -q --depth 1 origin "$BRANCHE"
    git cat-file -e "FETCH_HEAD:cle-$CIBLE.bin" 2>/dev/null && break
  fi
  [ "$i" -eq 120 ] && { echo "Code non reçu après 30 min : lancer outils/envoyer_source.sh $GITHUB_RUN_ID"; exit 1; }
  sleep 15
done
rm -rf "$T" && mkdir -p "$T" "$SORTIE"
git archive FETCH_HEAD | tar x -C "$T"
CLE=$(openssl pkeyutl -decrypt -inkey "$RUNNER_TEMP/ephemere.pem" -pkeyopt rsa_padding_mode:oaep -in "$T/cle-$CIBLE.bin")
echo "::add-mask::$CLE"
cat "$T"/source.tgz.enc.* | openssl enc -d -aes-256-cbc -pbkdf2 -pass "pass:$CLE" | tar xz -C "$SORTIE"
echo "Code reçu : $(cat "$T/source.txt")"
rm -rf "$T"
