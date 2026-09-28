#!/usr/bin/env bash
# Optimisation sans perte des images d'un jeu de slides. Voir PRD-009.
#
# Recompresse assets/slides/*.png avec oxipng, et prouve que l'operation est
# sans perte en comparant l'empreinte SHA-256 des pixels decodes avant et apres.
# Le redimensionnement n'a lieu que s'il est demande explicitement : il fait
# grossir le PNG, la recompression qui suit le rattrape.
set -euo pipefail

usage() {
  cat >&2 <<'AIDE'
Usage: scripts/optimiser-images.sh <dossier-jeu> [--dimensions LxH]

  <dossier-jeu>       dossier du jeu, par exemple navigation-opquast-v5
  --dimensions LxH    reechantillonne d'abord toutes les images, par exemple
                      1600x900 ; a n'utiliser que si les dimensions du lot sont
                      heterogenes de facon visible

Sans --dimensions, les dimensions d'origine sont conservees.
AIDE
  exit 2
}

[ "$#" -ge 1 ] || usage
slug="$1"
shift
dimensions=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --dimensions)
      [ "$#" -ge 2 ] || usage
      dimensions="$2"
      shift 2
      ;;
    *) usage ;;
  esac
done

slides="$slug/assets/slides"
if [ ! -d "$slides" ]; then
  echo "Erreur : dossier absent : $slides" >&2
  exit 1
fi
if ! ls "$slides"/slide-*.png >/dev/null 2>&1; then
  echo "Erreur : aucune image slide-*.png dans $slides" >&2
  exit 1
fi

if ! command -v oxipng >/dev/null 2>&1; then
  echo "Erreur : oxipng est absent du PATH." >&2
  echo "Installation : brew install oxipng" >&2
  exit 1
fi

if ! python3 -c "import PIL" >/dev/null 2>&1; then
  echo "Erreur : Pillow est absent." >&2
  echo "Installation : python3 -m pip install Pillow" >&2
  exit 1
fi

poids() { du -sk "$1" | cut -f1; }
empreinte() {
  python3 - "$1" <<'PY'
import hashlib, pathlib, sys
from PIL import Image
h = hashlib.sha256()
for chemin in sorted(pathlib.Path(sys.argv[1]).glob("slide-*.png")):
    with Image.open(chemin) as image:
        h.update(image.convert("RGB").tobytes())
print(h.hexdigest())
PY
}

nombre=$(ls "$slides"/slide-*.png | wc -l | tr -d ' ')
poids_initial=$(poids "$slides")
echo "Jeu          : $slug"
echo "Images       : $nombre"
printf 'Poids initial: %s Mo\n' "$((poids_initial / 1024))"

if [ -n "$dimensions" ]; then
  echo
  echo "Reechantillonnage en $dimensions ..."
  python3 - "$slides" "$dimensions" <<'PY'
import pathlib, sys
from PIL import Image
dossier = pathlib.Path(sys.argv[1])
largeur, hauteur = (int(v) for v in sys.argv[2].lower().split("x"))
change = 0
for chemin in sorted(dossier.glob("slide-*.png")):
    with Image.open(chemin) as image:
        image = image.convert("RGB")
        if image.size == (largeur, hauteur):
            continue
        image.resize((largeur, hauteur), Image.Resampling.LANCZOS).save(
            chemin, format="PNG", optimize=True
        )
        change += 1
print(f"  images reechantillonnees : {change}")
PY
  poids_redimensionne=$(poids "$slides")
  printf '  poids apres redimensionnement : %s Mo\n' "$((poids_redimensionne / 1024))"
fi

avant=$(empreinte "$slides")
poids_avant=$(poids "$slides")

echo
echo "Recompression sans perte ..."
oxipng -o max --strip safe "$slides"/slide-*.png 2>&1 | tail -3

apres=$(empreinte "$slides")
poids_apres=$(poids "$slides")

echo
if [ "$avant" != "$apres" ]; then
  echo "ECHEC : la recompression a modifie les pixels." >&2
  echo "  empreinte avant : $avant" >&2
  echo "  empreinte apres : $apres" >&2
  exit 1
fi
echo "Sans perte confirme : empreinte des pixels identique"
echo "  ${avant:0:32}"

echo
# Les poids sont en kilo-octets : un gain inferieur au pour cent reste lisible.
python3 - "$poids_initial" "$poids_avant" "$poids_apres" <<'PY'
import sys
initial, avant, apres = (int(v) for v in sys.argv[1:4])
gain = 100 * (avant - apres) / avant if avant else 0.0
print(f"Poids final  : {apres / 1024:.1f} Mo (gain de {gain:.2f} % sur la recompression)")
if initial != apres:
    total = 100 * (initial - apres) / initial if initial else 0.0
    print(f"Bilan        : {initial / 1024:.1f} Mo -> {apres / 1024:.1f} Mo ({total:+.2f} %)")
PY

echo
echo "Les images ont change : relancer python3 $slug/build.py pour reconstruire le ZIP."
