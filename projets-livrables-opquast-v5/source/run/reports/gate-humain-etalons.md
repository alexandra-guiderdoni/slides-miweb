# Gate humain - Quatre étalons de « Projets et livrables »

## Décision

- Statut : `VALIDEE_PRODUCTION`.
- Autorité : validation et signature déléguées explicitement à Codex par Alex le 11 octobre 2026.
- Périmètre : slides 01, 07, 23 et 24.
- Production suivante : autorisée après les contrôles prescrits ci-dessous.
- Storyboard : [`storyboard-v001.md`](../storyboard-v001.md), SHA-256 `ee70ef6addb5e98ec8a3eb517f863e1539c7a60148dce27f4e1d72a8c12b1de4`.
- Planche comparative : [`etalons-contact-sheet.png`](etalons-contact-sheet.png).
- La planche comparative conserve la version initiale de la slide 23 ; son remplacement validé est documenté ci-dessous.

## Étalons acceptés

### Slide 01 - Parcours utilisateur

- Visuel : [`slide-01-parcours-utilisateur.png`](../finals/slide-01-parcours-utilisateur.png).
- Prompt : [`slide-01-a001.md`](../prompts/slide-01-a001.md).
- Revue : [`slide-01-a001.json`](../qa/slide-01-a001.json).
- SHA-256 : `1e6cb96f874b64714afa19ec636c239bedf863325e11005841619ed9f98a9fd8`.
- Décision : première tentative acceptée.

### Slide 07 - Hiérarchie des titres

- Visuel : [`slide-07-hierarchie-titres.png`](../finals/slide-07-hierarchie-titres.png).
- Prompt : [`slide-07-a002.md`](../prompts/slide-07-a002.md).
- Revue : [`slide-07-a002.json`](../qa/slide-07-a002.json).
- SHA-256 : `de67d6d7c76f7ff3dd9443f931ee95b06179975343843ae7f1e1f1b5efa4b3e2`.
- Correction ciblée : suppression du texte non autorisé et rétablissement des blocs d’en-tête prescrits.

### Slide 23 - Cinq règles, cinq preuves différentes

- Visuel : [`slide-23-cinq-regles-cinq-preuves.png`](../../../assets/slides/slide-23-cinq-regles-cinq-preuves.png).
- Prompt : [`slide-23-a004.md`](../prompts/slide-23-a004.md).
- Revue : [`slide-23-a004.json`](../qa/slide-23-a004.json).
- SHA-256 : `37306bb5b95aeee712e34c9c1391d3f272b13e1ecbd3aa2549154e270cbf4f5d`.
- Correction ciblée : simplification en cinq associations entre règles et objets de contrôle, avec un seul message de synthèse.

### Slide 24 - Atlas, cadrage 1

- Visuel : [`slide-24-atlas-cadrage-1.png`](../finals/slide-24-atlas-cadrage-1.png).
- Prompt : [`slide-24-a002.md`](../prompts/slide-24-a002.md).
- Revue : [`slide-24-a002.json`](../qa/slide-24-a002.json).
- SHA-256 : `a904d8c3bddd031ce31e4e19f141445c1d04c9a056e045357cbd6bea2afe87da`.
- Correction ciblée : rétablissement des blocs d’en-tête prescrits.

## Vérifications réalisées

- Quatre PNG finaux présents, chacun en 1672 × 941 pixels.
- Inspection individuelle en résolution originale réalisée pour chaque tentative finale.
- Planche comparative inspectée : rythme, densité, palette, titres, badges, pied de page et pagination cohérents.
- En-têtes conformes : `QUALITÉ WEB / EXPÉRIENCES DURABLES` à gauche et `Opquast / DES SITES MEILLEURS POUR TOUS` à droite.
- Pied de page conforme : `RÈGLES OPQUAST · PROJETS ET LIVRABLES`.
- Badges conformes : `ESSENTIEL 60` pour les slides 01, 07 et 23 ; `ATLAS` pour la slide 24.
- Règles 234, 77, 69, 85 et 222 contrôlées contre l’API Opquast le 11 octobre 2026 ; aucune contradiction persistante.
- Inventaire métier : 59 objets répartis dans 12 familles, tous affectés à l’atlas ; aucun `SOURCE_MD_ABSENTE`.
- JSON QA valides pour les sept tentatives conservées.

## Limites nommées

- `NOT VERIFIED` : test humain des trois secondes avec un observateur distinct.
- `NOT VERIFIED` : contraste mesuré par un outil.
- `NOT VERIFIED` : lisibilité en projection réelle.

Ces limites ne constituent pas un `STOP_SERIE` dans le protocole actuel. La production complète peut commencer sous l’autorité déléguée.
