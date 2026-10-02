# Inspection de la série

## Périmètre

- 14 visuels correspondant aux slides PPTX 1 à 14.
- La slide PPTX 15 est exclue.
- Format contrôlé : 1672 x 941 pixels pour les 14 images.
- Visuels 01 à 08 : style IGPDE bleu illustré.
- Visuels 09 à 14 : fac-similés recto-verso des cartes Ideance originales.

## Contrôles visuels et éditoriaux

- Les quatre étalons 01, 04, 07 et 09 ont été validés avant la production complète.
- Les textes des slides 01 à 08 ont été relus en résolution originale et contrôlés par OCR.
- Les photographies des intervenants, l'affiche, les QR codes et les cartes restent authentiques.
- Les adresses électroniques ne figurent pas dans les images et restent présentes dans les transcriptions.
- La revue indépendante consolidée a conclu `VALIDÉ SOUS RÉSERVE`, avec 0 P0.
- Les réserves documentaires ont été corrigées avant la création de `slides.json` : état d'avancement, textes des QR codes, libellés PPTX, hiérarchie Recto-Verso, marque Ideance et textes visibles de la slide 03.

## Contrôles des QR codes

- Slide 02 : QR décodé vers `https://www.info.gouv.fr/accessibilite`.
- Slides 09 à 14 : QR décodés vers les six ancres de l'article Ideance consacré aux idées reçues.

## Audit des alternatives courtes

| Slides | Rôle du visuel | Décision |
| --- | --- | --- |
| 01 à 08 | Informer et structurer une progression pédagogique | Alternative courte centrée sur l'information utile, complétée par une description longue. |
| 09 à 14 | Confronter une idée reçue à son décryptage | Alternative courte centrée sur la correction de l'idée reçue, complétée par la transcription exacte du recto, du verso et du PPTX. |

- Les 14 alternatives comptent moins de 80 caractères.
- Aucune ne commence par « image de », « photo de », « illustration de » ou « logo ».
- Les descriptions longues portent la structure et les informations qui ne tiennent pas dans l'alternative courte.
- Les textes visibles restent disponibles séparément dans `slides.json`.

## Accordéons

- `Transcription` reprend le contenu exact et hiérarchisé des slides.
- `Lire le discours oral` reprend intégralement les notes des sources PPTX.
- Les deux contenus restent distincts dans la présentation et dans les exports d'alternatives.
