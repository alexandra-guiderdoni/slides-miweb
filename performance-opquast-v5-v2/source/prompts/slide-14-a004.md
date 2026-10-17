# Prompt image_gen - slide 14, tentative a004

## Défaut observé

La candidate a003 respecte la composition, le masque, la hiérarchie et la liste blanche, mais les deux pictogrammes de fichiers de la colonne `AVANT L’ENVOI` contiennent les textes parasites `CSS` et `JS`. Ces six lettres ne font pas partie de la liste blanche à cet emplacement et répètent inutilement le libellé placé sous les pictogrammes.

## Invariants à préserver

- Conserver strictement l’intégralité de la candidate a003 : dimensions, cadrage, fond, marges, palette, typographie, panneaux, espacements, icônes, marque, footer et pagination.
- Conserver exactement tous les textes autorisés, sans modification de caractère, de ponctuation, d’accent, de casse, de taille ou de position.
- Conserver les trois colonnes, leurs couleurs et leurs relations visuelles.
- Conserver les deux pictogrammes de fichiers et leurs glyphes graphiques bleus `{ }` et `</>`.
- Conserver la résolution 1672 × 941 pixels et le ratio 16:9.

## Correction visuelle attendue

- Effacer uniquement les lettres `CSS` dans le pictogramme de fichier de gauche.
- Effacer uniquement les lettres `JS` dans le pictogramme de fichier de droite.
- Recentrer verticalement le glyphe bleu `{ }` dans le premier fichier.
- Recentrer verticalement le glyphe bleu `</>` dans le second fichier.
- Les deux fichiers doivent rester immédiatement identifiables comme des fichiers de code compacts grâce à leurs glyphes, sans aucun mot à l’intérieur.

## Interdits

- Ne modifier aucun autre élément de la slide.
- N’ajouter aucune lettre, aucun mot, aucun chiffre, aucun pseudo-texte et aucun symbole supplémentaire.
- Ne supprimer, reformuler, déplacer ou tronquer aucun texte autorisé.
- Ne changer ni les numéros 119, 226, 227, 229 et 230, ni la pagination `14 / 32`.
- Ne déformer aucune marque, icône, bordure ou relation visuelle.
- Ne pas réintroduire `CSS`, `JS` ou toute autre abréviation à l’intérieur des pictogrammes.
