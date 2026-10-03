# Inspection de la série bureautique

## Sources conservées

- `storyboard.md` relie les 27 vues web aux diapositives 54 à 80 du support IGPDE.
- `prompts/` conserve les prompts soumis et les reprises des slides 04 et 20.
- `contact-sheet.png` présente les 27 images dans l'ordre, de gauche à droite puis de haut en bas.
- `imagegen-delivery-receipt.tsv` associe chaque image à son prompt, à l'empreinte du fichier généré et à celle du fichier publié, sans chemin local de génération.
- `source-images/` conserve les deux PNG originaux du quiz A/B. Leur insertion dans la slide 03 est décrite dans `composition-slide-03.md`.

## Contrôles réalisés

- Les 27 fichiers `slide-01.png` à `slide-27.png` sont présents et mesurent 1672 × 941 pixels.
- Les quatre étalons acceptés, 01, 03, 11 et 24, gardent les mêmes pixels que les fichiers retenus lors de leur validation.
- Les deux PNG sources du quiz sont conservés à l'octet près ; leur empreinte SHA-256 est indiquée dans `composition-slide-03.md`.
- Les slides 04 et 20 ont été reprises après inspection pour rendre visibles les différences de structure et la distinction entre source accentuée et affichage en majuscules.
- Les 27 alternatives courtes de `slides.json` ont été relues dans le contexte des images ; chacune tient en 80 caractères au plus. Les transcriptions et les notes du formateur restent dans deux champs distincts.
- Les 27 PNG publiés ont été recompressés sans changement des pixels décodés. Leur poids total est passé de 30 905 954 à 28 725 590 octets, soit 7,1 % de moins. Le script habituel du dépôt ne pouvait pas s'exécuter car `oxipng` et Pillow étaient absents ; la recompression a été effectuée avec FFmpeg et une comparaison SHA-256 des pixels décodés avant et après chaque fichier.

## Limites visibles

Les slides 05, 06, 21, 22 et 23 comportent des pictogrammes W ou PDF ajoutés par ImageGen. Ils identifient les formats bureautiques mais s'écartent de la consigne générique du prompt qui limitait les logos et les textes supplémentaires.

L'inspection visuelle et la validation technique du site ne constituent pas un audit de conformité RGAA.
