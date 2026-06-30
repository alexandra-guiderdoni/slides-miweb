#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: scripts/validate_variant.sh <slug>" >&2
  exit 2
fi

slug="$1"
if [ ! -d "$slug" ]; then
  echo "Erreur : dossier absent : $slug" >&2
  exit 1
fi

html_validate_bin="node_modules/.bin/html-validate"
vnu_bin="node_modules/.bin/vnu"

python3 -m unittest discover -s "$slug/tests"

if [ ! -x "$html_validate_bin" ] || [ ! -x "$vnu_bin" ]; then
  echo "Erreur : dépendances npm absentes. Lancez npm ci depuis la racine du dépôt." >&2
  exit 1
fi

"$html_validate_bin" "$slug/index.html" "$slug/alternatives.html" "$slug/accessibilite.html" index.html
"$vnu_bin" --errors-only "$slug/index.html" "$slug/alternatives.html" "$slug/accessibilite.html" index.html
