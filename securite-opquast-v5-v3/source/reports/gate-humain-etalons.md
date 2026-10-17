# Gate humain - quatre étalons Sécurité Opquast V5 V3

## Statut

- Statut : `VALIDE_PAR_LA_REFERENTE`.
- Validation explicite : 17 octobre 2026, réponse `go` après présentation des quatre étalons.
- Date de génération : 17 octobre 2026.
- Moteur : `image_gen`.
- Périmètre : slides 01, 20, 23 et 30 uniquement.
- Génération complète : terminée, intégrée et validée localement.

## Résultats

| Slide | Rôle | Inspection | Décision technique |
|---:|---|---|---|
| 01 | Ouverture | Texte exact, question lisible, quatre risques encore ouverts autour de HTTPS | Candidate acceptée |
| 20 | Éclairage | Ancien entête barré, protection actuelle visible, contrôle explicite | Candidate acceptée |
| 23 | Règle | Titre restauré après une correction ciblée, mécanisme SRI lisible et exact | Candidate remplacée puis acceptée |
| 30 | Synthèse | Trois verbes dans le bon ordre, équipe mixte, question finale actionnable | Candidate acceptée |

## Contrôles effectués

- Dimensions : 1672 x 941 pixels pour les quatre images.
- Ratio : 16:9 conforme.
- Inspection visuelle : résolution originale pour les quatre images.
- OCR : textes obligatoires retrouvés ; les symboles et pictogrammes produisent quelques caractères parasites dans la sortie OCR, sans texte parasite visible dans les images.
- Contact sheet : inspectée, cohérence globale satisfaisante.
- Masque commun : fond clair, titre bleu marine, repères supérieurs, footer bas gauche et pagination bas droite.
- Tirets : aucun tiret cadratin dans les sources éditoriales.
- Origine : chaque image finale est liée à son fichier cache et à sa copie projet dans `imagegen-receipt.tsv`.
- Prompts : fichiers complets conservés dans `source/prompts` et reliés aux appels dans `imagegen-prompts-manifest.tsv`.

## Limite d'outillage

Le script historique `export_imagegen_prompts.py` ne reconnaît que les identifiants `ig_*` et les anciens événements `image_generation_call`. La session actuelle consigne les générations sous forme d'événements `Extension` identifiés par `exec-*`. L'export automatique est donc incompatible avec ce format de journal. La traçabilité est assurée sans duplication par les prompts sources, le manifeste, le reçu, les chemins de cache et la session JSONL.

## Fichiers à examiner

- `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/slide-01.png`
- `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/slide-20.png`
- `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/slide-23.png`
- `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/slide-30.png`
- `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/contact-sheet.png`

La génération des 26 autres slides a été réalisée avec le même masque, sans modification des quatre étalons validés.
