# Correction ImageGen - slide 19

## Défaut observé

- La barre d'adresse de la fenêtre centrale contient le texte `HTTPS`, qui n'appartient pas à la liste blanche.

## Invariants à préserver

- Conserver strictement le titre, le chapitre, les trois questions, les trois panneaux, les connecteurs, le personnage, le callout, le footer et la pagination.
- Conserver la fenêtre centrale et sa barre d'adresse au même emplacement.
- Conserver le format exact 1672 x 941 pixels.

## Correction visuelle attendue

- Retirer uniquement le mot `HTTPS` et le cadenas vert de la barre d'adresse centrale.
- Laisser la barre neutre avec un petit disque gris et un trait gris abstrait, sans aucun caractère lisible.

## Interdits

- Aucun mot, protocole, URL, domaine, lettre ou chiffre dans la barre d'adresse.
- Ne pas modifier les questions, les panneaux ou tout autre élément.
- Ne pas ajouter de logo ou de texte parasite.

## Prompt complet

Cas d'usage : precise-object-edit.
Type d'actif : édition ciblée d'une slide de formation existante, paysage 16:9, exactement 1672 x 941 pixels.
Image 1 : cible d'édition. Préserver l'image entière à l'identique.
Demande principale : dans la barre d'adresse de la fenêtre centrale uniquement, supprimer le cadenas vert et le mot `HTTPS`, puis les remplacer par un petit disque gris et un trait gris abstrait. La barre doit rester neutre et ne contenir aucun caractère lisible.
Contraintes : conserver tous les autres pixels autant que possible, tous les textes autorisés, la composition, le footer `Opquast - présentation Miweb` et la pagination `19 / 30`.
À éviter : protocole, URL, domaine, lettre, chiffre, texte parasite, modification globale ou logo.
