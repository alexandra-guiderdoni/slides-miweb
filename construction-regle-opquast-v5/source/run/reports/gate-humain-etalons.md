# Gate humain - Quatre étalons de « Construction d'une règle »

## État du gate

- Statut : `VALIDE_PAR_UTILISATRICE`.
- Périmètre : slides 01, 06, 08 et 16 uniquement.
- Production suivante : autorisée par validation humaine explicite.
- Storyboard : [`storyboard-v001.md`](../storyboard-v001.md), SHA-256 `afad35049548c730f719ccec5da4b26a205cac5621eb53ac39e804d97dbf2069`.
- Planche comparative : [`etalons-contact-sheet.png`](etalons-contact-sheet.png), SHA-256 `78cba81ae7d565c5b2e765964c271337fc4aad98af26e9e4e48bc3c7a1cb1817`.
- Transcriptions et discours oraux : [`etalons-validation.md`](../transcripts/etalons-validation.md).

## Étalon 01 - Ouverture

- Fonction : faire constater qu'une intention utile ne suffit pas à produire une règle contrôlable.
- Visuel final : [`slide-01-idee-utile.png`](../finals/slide-01-idee-utile.png).
- Prompt final : [`slide-01-a002.md`](../prompts/slide-01-a002.md).
- Revue finale : [`slide-01-a002.json`](../qa/slide-01-a002.json).
- SHA-256 du PNG : `34547a4500921a21ffb75b88f22d30e73433b7f024b585365bf8f028928551dd`.
- Correction appliquée : permutation des deux blocs d'en-tête, sans modification du message pédagogique.

### Textes visibles

- `QUALITÉ WEB`
- `EXPÉRIENCES DURABLES`
- `Opquast`
- `DES SITES MEILLEURS POUR TOUS`
- `Une idée utile suffit-elle ?`
- `« Ce site doit être intuitif. »`
- `Intention ≠ règle contrôlable`
- `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`
- `01 / 16`

## Étalon 06 - Éclairage et regroupement

- Fonction : présenter les six exigences V5 comme six questions de même niveau.
- Visuel final : [`slide-06-six-exigences.png`](../finals/slide-06-six-exigences.png).
- Prompt final : [`slide-06-a002.md`](../prompts/slide-06-a002.md).
- Revue finale : [`slide-06-a002.json`](../qa/slide-06-a002.json).
- SHA-256 du PNG : `16132e1ed5f4fc16614af6360e46f49a3de9eacd449051e25aeaaa24c40caf76`.
- Correction appliquée : ajout d'une feuille neutre derrière la grille, sans septième carte ni texte supplémentaire.

### Textes visibles

- `QUALITÉ WEB`
- `EXPÉRIENCES DURABLES`
- `Opquast`
- `DES SITES MEILLEURS POUR TOUS`
- `Six exigences pour éprouver une proposition`
- `ATELIER V5 · SIX EXIGENCES`
- `Universelle ?`
- `Utile ?`
- `Sans seuil empirique arbitraire ?`
- `Vérifiable depuis le service ?`
- `Réaliste ?`
- `Unique ?`
- `Consensus et conseils de rédaction : étudiés à part.`
- `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`
- `06 / 16`

## Étalon 08 - Règle centrale

- Fonction : distinguer le résultat observable du processus interne à partir de la règle 152.
- Visuel final : [`slide-08-preuve-regle-152.png`](../finals/slide-08-preuve-regle-152.png).
- Prompt final : [`slide-08-a001.md`](../prompts/slide-08-a001.md).
- Revue finale : [`slide-08-a001.json`](../qa/slide-08-a001.json).
- SHA-256 du PNG : `b71e593fcfd3d9b7f5673aa31f75546df86977ee7112ff604f842ebe21497cea`.
- Correction appliquée : aucune ; la première tentative a satisfait les critères.

### Textes visibles

- `QUALITÉ WEB`
- `EXPÉRIENCES DURABLES`
- `Opquast`
- `DES SITES MEILLEURS POUR TOUS`
- `La preuve, pas la promesse`
- `A · Résultat observable`
- `B · Processus interne`
- `RÈGLE 152`
- `Tous les liens internes sont valides.`
- `Contrôle : rechercher les liens internes vers une erreur 404`
- `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`
- `08 / 16`

## Étalon 16 - Synthèse

- Fonction : relier le préjudice, la preuve et la discussion documentée sans suggérer un processus officiel.
- Visuel final : [`slide-16-preuve-partagee.png`](../finals/slide-16-preuve-partagee.png).
- Prompt final : [`slide-16-a002.md`](../prompts/slide-16-a002.md).
- Revue finale : [`slide-16-a002.json`](../qa/slide-16-a002.json).
- SHA-256 du PNG : `20bebd78a10e9c178a3ec32835520042ad9f8c218866b9def2e9edaba95afd2c`.
- Correction appliquée : retrait de trois traits assimilables à du pseudo-texte dans la fiche commune.

### Textes visibles

- `QUALITÉ WEB`
- `EXPÉRIENCES DURABLES`
- `Opquast`
- `DES SITES MEILLEURS POUR TOUS`
- `Construire une règle, c'est construire une preuve partagée`
- `1 · Quel préjudice utilisateur ?`
- `2 · Quelle exigence, quelle preuve ?`
- `3 · Qui peut la discuter, la documenter et la maintenir ?`
- `Une règle utile, contrôlable, argumentée et durable.`
- `Synthèse pédagogique interne`
- `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`
- `16 / 16`

## Vérifications réalisées

- Dimensions de chaque PNG : 1672 × 941 px.
- Inspection visuelle plein écran : réalisée pour chaque tentative finale.
- En-têtes : `QUALITÉ WEB / EXPÉRIENCES DURABLES` à gauche et `Opquast / DES SITES MEILLEURS POUR TOUS` à droite.
- Footer : `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE` sur les quatre slides.
- Règle 152 : libellé contrôlé contre l'API Opquast avant génération.
- Provenance : 30 identifiants métier inventoriés, 30 affectés, aucun élément sans emplacement.
- Contrôle d'accents : passé sur les documents Markdown produits.
- Audit ShipGuard : 23 fichiers analysés, 0 finding, état provisoire `needs-human-review`.

## Limites de la validation automatique

- La conformité des chaînes a été vérifiée visuellement ; aucun OCR automatisé n'a été utilisé.
- Le contraste colorimétrique n'a pas été mesuré par un outil.
- La lisibilité en projection réelle n'a pas encore été testée en salle.
- La validation humaine des quatre étalons est démontrée par `qa/delegation-validation-2026-10-11.md`.

## PDG pass

- Déclenchement : oui, car ces sorties générées forment un gate pour une production plus large.
- Invocation du skill : `progressive-disclosure-guard` a été appliqué après lecture de son entrée complète ; une simple relecture visuelle ne suffisait pas pour contrôler les preuves, les limites et la condition d'arrêt.
- Artefacts inspectés : Goal, storyboard, matrice de couverture, prompts finaux, PNG finaux, revues QA, manifeste `run.json`, planche comparative, transcriptions et rapport de gate.
- Chevauchement : réutilisation de la fabrique existante et de son run ; aucun moteur, dossier de production ou référentiel parallèle créé.
- Auto-revue : `PDG self-check, not independent review`.
- Connu : quatre PNG finaux existent, mesurent 1672 × 941 px, possèdent un SHA lié au manifeste et ont été inspectés visuellement.
- Inconnu : rendu en projection réelle, mesure instrumentée du contraste et validation humaine.
- Risque résiduel : une vérification visuelle peut manquer une différence typographique difficile à distinguer sans OCR.
- Chemin interdit : générer les douze autres slides avant l'approbation humaine.
- Garde-fou : état du gate explicite, limites `NOT VERIFIED` et checkpoint exportable.

### Matrice de vérification fondée sur les sources

- Affirmation : les quatre étalons couvrent les rôles demandés. Source : Goal, storyboard et matrice. Verdict : confirmé. Impact : le gate peut être présenté.
- Affirmation : les règles et libellés affichés sont sourcés. Source : contrôle MCP Opquast et micro-matrice. Verdict : confirmé pour les onze règles contrôlées, dont la règle 152. Impact : aucune contradiction détectée.
- Affirmation : les PNG respectent dimensions et identité prescrites. Source : commande `file`, inspection plein écran et revues QA. Verdict : confirmé dans les cas inspectés. Impact : aucune correction technique restante identifiée.
- Affirmation : les slides sont validées par l'utilisatrice. Source : aucune décision humaine encore reçue. Verdict : inconnu. Impact : la production doit s'arrêter ici.

### Invariants à préserver

- Les quatre PNG finaux, leurs textes visibles, leurs rôles narratifs et leurs SHA doivent rester inchangés jusqu'à décision humaine.
- La suite MUST rester bloquée sans validation explicite.
- Une correction demandée MUST créer une nouvelle tentative et MUST conserver les tentatives précédentes.
- La suite MUST NOT convertir le livrable en PPTX ni élargir la mission à l'attribution ou à la licence.

## Décision obtenue

Les quatre étalons sont validés. L'utilisatrice délègue aussi la signature des gates suivants après exécution complète des contrôles prescrits.

### Carte de validation humaine

- Fichiers modifiés : run `construction-regle-opquast-v5`, ses quatre PNG finaux, ses prompts, ses revues, ses transcriptions et ce rapport.
- Chemin réel à inspecter : [`etalons-contact-sheet.png`](etalons-contact-sheet.png), puis chaque PNG final en taille réelle.
- Résultat attendu : identité cohérente, textes exacts, quatre rôles narratifs distincts et aucune dérive métier.
- Risque accepté : la lisibilité en salle et le contraste instrumenté restent non vérifiés.
- Phrase d'approbation du protocole : `Approved after human validation.`
