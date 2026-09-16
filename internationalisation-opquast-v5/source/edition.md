# Édition du support « Internationalisation »

Titre public : Internationalisation selon Opquast V5

Slug de publication : `internationalisation-opquast-v5`

Base éditoriale : storyboard source conservé dans `source/storyboard.md`, version finale du 15 septembre 2026.

Le texte de `source/transcription-et-discours-oral.md` fournit le contenu des deux accordéons de chaque slide. Il reprend sans réécriture les accordéons rédigés pour la série ; seules les balises HTML d’accordéon et les niveaux de titre ont été transformés pour entrer dans le format des séries Opquast V5 déjà publiées. Le storyboard reste conservé comme trace de conception des visuels et comme source des titres, des textes visibles et des messages.

## Périmètre et numérotation

Le support réunit les 11 slides du deck principal et les 4 slides de l’Annexe 1, soit 15 visuels numérotés de 1 à 15 pour la publication web.

Les visuels d’annexe conservent la pagination imprimée sur l’image, `A1-01 / 04` à `A1-04 / 04`, ainsi que le pied de page `ANNEXE 1 · INTERNATIONALISATION TRANSVERSALE`. La numérotation web continue de 12 à 15 est donc distincte de la pagination visible, comme pour les annexes de la série Données personnelles.

## Règles couvertes

Rubrique officielle Internationalisation : règles 128 à 135, chacune traitée sur une slide du deck principal.

Règles transversales de l’Annexe 1 : 4, 82, 149, 228, 232 et 233. Elles n’appartiennent pas à la rubrique officielle et sont présentées comme des connexions directes avec les risques internationaux.

Les libellés et objectifs des 14 règles citées ont été contrôlés le 17 septembre 2026 contre l’API Opquast, version `qualite-numerique`.

Les renvois de fin de discours du type « (API Opquast, règle n°130, version qualite-numerique) » ont été retirés : ils ne sont pas destinés à être lus à l’oral. La traçabilité des règles reste portée par le champ `regles_opquast` de `slides.json` et par la présente fiche.

## Réserves de lecture

Les axes `Contexte · Langue · Continuité` de la slide 1 et le regroupement en quatre questions de la slide 11 sont des regroupements pédagogiques. Ils ne constituent pas un classement officiel Opquast, et les visuels portent cette mention.

Les drapeaux visibles sur la slide 2 sont illustratifs. Opquast n’impose pas l’usage d’un drapeau pour signaler une langue.

Les coordonnées de la slide 3, le nom affiché sur les fiches de contact et les libellés de formulaire de la slide 14 sont des exemples pédagogiques fictifs, pas des formulations officielles.

Les quatre cas de la slide 10 sont des exercices originaux de formation, jamais présentés comme des questions officielles de certification.

## Fabrication

Les 15 visuels publiés dans `assets/slides/` proviennent du lot final de la série, en 1672 × 941 pixels. Ils sont repris sans recompression ni redimensionnement.

Les fichiers générés (`index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md`, `README.md` et le ZIP) sont reconstruits depuis `slides.json` par `build.py`. Ils ne se corrigent pas à la main.
