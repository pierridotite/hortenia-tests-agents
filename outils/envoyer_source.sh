#!/usr/bin/env bash
# Côté session Claude (qui a le dépôt privé de l'app) : envoie le code de
# l'app aux Mac d'un run « iOS - build » en cours, chiffré pour leurs clés
# éphémères. Le code passe par la branche transfert/<run> de ce dépôt public,
# illisible sans ces clés, supprimée en fin de run.
# Usage : bash outils/envoyer_source.sh <run_id> <clone du dépôt de l'app> <ref git>
set -euo pipefail
RUN=$1; DEPOT=$2; REF=$3
ICI=$(cd "$(dirname "$0")/.." && pwd)
REPO=pierridotite/hortenia-tests-agents
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT
mkdir -p "$T/envoi"

# Clés publiques des Mac (une par cible), publiées en artefacts par le run
for i in $(seq 1 60); do
  noms=$(gh api "repos/$REPO/actions/runs/$RUN/jobs" --jq '[.jobs[]|select(.name|startswith("build"))]|length')
  cles=$(gh api "repos/$REPO/actions/runs/$RUN/artifacts" --jq '[.artifacts[]|select(.name|startswith("cle-"))|.name]|join(" ")')
  [ -n "$cles" ] && [ "$(wc -w <<<"$cles")" -ge "${noms:-1}" ] && [ "${noms:-0}" -ge 1 ] && break
  [ "$i" -eq 60 ] && { echo "Pas de clé publiée par le run $RUN"; exit 1; }
  sleep 10
done
echo "Clés reçues : $cles"

SHA=$(git -C "$DEPOT" rev-parse "$REF")
CLE=$(openssl rand -hex 32)
# Sans les fichiers sources de dessins (.eps, assets/dl), inutilisés par l'app
git -C "$DEPOT" archive --format=tar "$SHA" -- Frontend ':(exclude)Frontend/**/*.eps' ':(exclude)Frontend/assets/dl' \
  | gzip -6 | openssl enc -aes-256-cbc -pbkdf2 -salt -pass "pass:$CLE" | split -b 45m - "$T/envoi/source.tgz.enc."
for nom in $cles; do
  id=$(gh api "repos/$REPO/actions/runs/$RUN/artifacts" --jq ".artifacts[]|select(.name==\"$nom\")|.id")
  gh api "repos/$REPO/actions/artifacts/$id/zip" > "$T/$nom.zip"
  unzip -o -q "$T/$nom.zip" -d "$T"
  printf '%s' "$CLE" | openssl pkeyutl -encrypt -pubin -inkey "$T/$nom.pem" -pkeyopt rsa_padding_mode:oaep -out "$T/envoi/$nom.bin"
done
echo "$(git -C "$DEPOT" log -1 --format='%h %s' "$SHA" | cut -c1-90)" > "$T/envoi/source.txt"

cd "$T/envoi"
git init -q
git -c user.name="Claude" -c user.email="noreply@anthropic.com" add -A
git -c user.name="Claude" -c user.email="noreply@anthropic.com" commit -q -m "Transfert chiffré pour le run $RUN"
git push -q "$(git -C "$ICI" remote get-url origin)" "HEAD:refs/heads/transfert/$RUN"
echo "Code $SHA envoyé au run $RUN ($(du -sh . | cut -f1))"
