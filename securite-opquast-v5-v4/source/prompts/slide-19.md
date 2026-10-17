# Prompt ImageGen - slide 19 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-30.png`, étalon V4 le plus proche pour trois protections de même poids

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : empêcher l'équivalence entre les règles 210, 211 et 212.
- Scène : une page centrale est protégée par trois portes répondant à trois questions différentes.
- Transformation : une même famille d'entêtes devient trois protections distinctes.
- Contrainte critique : XSS avec 210, cadre avec 211, origine avec 212.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française, paysage 16:9, exactement 1672 x 941 pixels.

Reprendre fidèlement le masque V4 : fond ivoire, micro-entête avec trait vert, repère de chapitre, grand titre bleu marine, trois panneaux pastel égaux, callout bleu très clair centré en bas, footer et pagination stables. Illustration plate, bleu institutionnel, corail uniquement pour un script injecté refusé, vert pour les protections actives. Typographie proche de Marianne. Aucun dégradé, photographie, 3D, ombre lourde ou faux logo.

Composition : une page centrale entourée de trois portes séparées. Porte 210 : bloque l'exécution d'un script injecté. Porte 211 : contrôle l'intégration dans un cadre. Porte 212 : filtre l'origine des contenus. Les trois cartes ont la même importance et convergent sans fusion. En bas, un seul callout rappelle qu'une même politique peut porter plusieurs protections.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `Une même famille d'entêtes, trois questions différentes`
- `210 - Comment limiter l'exécution de scripts injectés ?`
- `211 - Qui peut intégrer ma page dans un cadre ?`
- `212 - D'où les contenus peuvent-ils être chargés ?`
- `Une même politique peut porter plusieurs protections.`
- `Opquast - présentation Miweb`
- `19 / 30`

Critères de rejet : association erronée des règles ; porte absente ou ajoutée ; équivalence suggérée ; code, URL, logo ou texte parasite ; mauvaise pagination.
