# Prompt ImageGen - slide 19

## Fiche PDS

- Rôle : empêcher l’équivalence entre les règles 210, 211 et 212.
- Scène : une page centrale est protégée par trois portes répondant à trois questions différentes.
- Transformation : une même famille d’entêtes devient trois protections distinctes.
- Continuité : prépare l’éclairage détaillé de la règle 210.
- Contrainte critique : associer XSS à 210, cadre à 211 et origine des contenus à 212.

## Prompt complet

Cas d’usage : infographic-diagram.
Type d’actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Reprendre exactement le masque clair des étalons : fond blanc, en-tête et chapitre en haut, grand titre bleu marine, trois panneaux pastel égaux autour d’une page centrale, callout bleu clair centré en bas, footer bas gauche, pagination bas droite. Bleu institutionnel pour la structure, corail uniquement pour un script injecté refusé, vert pour les protections actives. Marianne obligatoire, Arial en fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : page web centrale entourée de trois portes clairement séparées. Porte 210 : bloque l’exécution d’un script injecté. Porte 211 : contrôle l’intégration de la page dans un cadre. Porte 212 : filtre l’origine des contenus chargés. Les trois cartes ont la même importance et convergent vers la page sans fusion. En bas, un seul callout rappelle qu’une même politique peut porter plusieurs protections.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `Une même famille d'entêtes, trois questions différentes`
- `210 - Comment limiter l'exécution de scripts injectés ?`
- `211 - Qui peut intégrer ma page dans un cadre ?`
- `212 - D'où les contenus peuvent-ils être chargés ?`
- `Une même politique peut porter plusieurs protections.`
- `Opquast - présentation Miweb`
- `19 / 30`

Contraintes critiques : trois portes seulement ; associer correctement 210, 211 et 212 ; ne pas écrire qu’elles sont équivalentes ; aucun code supplémentaire, URL, logo ou texte parasite.
