# Recette de génération - Sécurité Opquast V5 V3

## Statut

- Statut : `INTEGRE_ET_VALIDE`.
- Date : 17 octobre 2026.
- Périmètre : 30 images de slides, prompts et traçabilité de génération.
- Intégration au site : réalisée dans le jeu autonome `securite-opquast-v5-v3`.
- Build : réalisé.
- Commit, push et publication : non réalisés.

## Résultat

- 30 images présentes, de `slide-01.png` à `slide-30.png`.
- 30 images au format exact 1672 x 941 pixels.
- Aucune pagination manquante ou dupliquée.
- Un prompt principal au minimum pour chaque slide.
- Prompts de correction conservés pour les reprises ciblées.
- Quatre reçus de génération présents : étalons, lot A, lot B et lot C.
- Planche complète régénérée et inspectée en résolution originale.
- Aucun tiret cadratin ou tiret demi-cadratin dans les sources Markdown et TSV de la V3.
- `git diff --check` sans erreur.
- Contrôle des notes orales : 30 slides, 0 erreur et 0 avertissement.
- Tests du jeu : 13 tests réussis.
- Tests des scripts partagés : 12 tests réussis.
- Tests de la matrice : 27 tests réussis et 1 test ignoré.
- Validation standard du jeu : 13 tests réussis.
- Archive de téléchargement contrôlée : aucune erreur de compression.

## Relecture croisée

- Le lot A a été relu par le lot B.
- Le lot B a été relu par le lot A.
- Le lot C a été relu par le lot A.
- Les quatre étalons et la cohérence globale ont été relus par le lot C.
- Les corrections finales des slides 18, 22, 26 et 28 ont été revérifiées par un autre relecteur avec un verdict `GO`.

## Reprises effectuées après relecture

- Slide 15 : ajout de la distinction entre deux moyens au choix et deux facteurs simultanés.
- Slide 16 : suppression des quatre libellés de verdict répétés.
- Slide 17 : remplacement d'un pictogramme ambigu sur le type MIME.
- Slide 18 : restauration des formulations complètes 206 et 207, puis suppression des numéros autonomes dupliqués.
- Slide 19 : suppression de la mention `HTTPS` parasite dans la barre d'adresse.
- Slide 22 : suppression d'une occurrence autonome de `Content-Security-Policy`.
- Slide 26 : suppression de libellés d'entêtes répétés dans l'illustration.
- Slide 28 : ajout des tirets simples dans les trois formulations SPF, DKIM et DMARC.

## Écarts connus et arbitrages

- Slide 04 : le bandeau est placé plus bas que sur le masque majoritaire. L'écart est cosmétique et non bloquant.
- Slide 01 : `HTTPS` figure dans la barre d'adresse. Le prompt demandait cette preuve dans la composition, mais ne la répétait pas dans sa liste blanche.
- Slide 20 : l'image validée affiche `Content-Security-Policy active`, sans le préfixe `Exemple actuel` présent dans le storyboard.
- Slide 23 : les pictogrammes de fichiers portent `JS` et la comparaison SRI est simplifiée. Le mécanisme central reste exact et lisible.
- Slide 30 : les propriétaires sont représentés par l'équipe autour du parcours, sans attribution écrite sous chaque action.

Les slides 01, 20, 23 et 30 ont été explicitement validées comme étalons avant la génération complète. Ces écarts sont donc conservés comme arbitrages validés et ne déclenchent pas de nouvelle génération.

## Artefacts

- Images : `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/slide-01.png` à `slide-30.png`.
- Planche : `outputs/ia-slides/2026-10-17-securite-opquast-v5-v3-etalons/contact-sheet-30.png`.
- Prompts : `securite-opquast-v5-v3/source/prompts/`.
- Reçus : `imagegen-receipt.tsv`, `imagegen-receipt-a.tsv`, `imagegen-receipt-b.tsv` et `imagegen-receipt-c.tsv`.

## Limite d'outillage

Le script historique `export_imagegen_prompts.py` ne reconnaît pas les événements `Extension` identifiés par `exec-*`. La traçabilité reste assurée par les prompts sources, le manifeste des étalons, les quatre reçus, les chemins de cache et la session JSONL.
