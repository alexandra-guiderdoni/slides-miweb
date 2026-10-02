# Inspection visuelle - Partie I

Date : 2026-10-02

## Périmètre

- 39 visuels publics, de `slide-01.png` à `slide-39.png`.
- 1 planche interne de continuité des personnages.
- Format vérifié : 1672 x 941 pixels pour les visuels contrôlés, ratio 16:9.
- Relecture globale sur `contact-sheet.png`, puis contrôle en pleine résolution des étalons et des reprises ciblées.

## Contrôles effectués

- Cohérence du preset local « IGPDE Accessibilité - bleu illustré ».
- Titre bleu nuit lisible, hiérarchie visuelle stable et espace libre suffisant.
- Correspondance 1 pour 1 avec les 39 entrées du storyboard.
- Continuité des six personas et de la communicante récurrente.
- Absence de représentation caricaturale ou passive du handicap.
- Respect des listes blanches de textes visibles et absence de pseudo-texte manifeste.
- Respect des usages réservés du rouge et du vert.
- QR Obligally authentique et URL visible sur la slide 26, ajoutés par surimpression déterministe.
- Logo FALC Europe authentique sur la slide 38, ajouté par surimpression déterministe.
- Symbole de QR volontairement non scannable sur les slides 03 et 34.

## Reprises réalisées

- Slide 03 : remplacement d’un motif trop proche d’un QR code par quatre carrés abstraits.
- Slide 09 : ajout du libellé exact « Percevoir + Compatible ».
- Slide 11 : alignement de Justine sur la planche personnages.
- Slide 16 : suppression des lunettes noires et de la canne blanche ; reprise d’Amir avec casque et plage braille.
- Slide 18 : suppression des marqueurs stéréotypés dans la loupe.
- Slide 23 : suppression des drapeaux et emblèmes générés.
- Slide 32 : suppression d’un faux logo FALC et remplacement par des documents génériques.

## Vérifications textuelles

- OCR Tesseract utilisé comme signal complémentaire sur les étalons ; la relecture visuelle reste la référence pour les textes intégrés aux images.
- Les transcriptions et discours oraux exacts sont conservés dans `slides.json` et contrôlés automatiquement contre `source/storyboard.md`.
- Les deux tableaux des slides 16 et 17 reçoivent des légendes propres dans le HTML.
- Les 13 thèmes de la slide 24 sont rendus sous forme de liste ordonnée sémantique dans le HTML.

## Limite connue

- Le décodeur QR natif n’a pas produit de résultat exploitable dans l’environnement. La slide 26 réutilise néanmoins sans altération éditoriale le fichier QR source authentique, avec le lien complet visible dans l’image et dans l’accordéon HTML.
