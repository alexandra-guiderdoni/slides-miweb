# Contrôle de comportement - 96ffc14 vers 896d9b6

Mode `reason`, mais tous les constats sont **mesurés** : les unités sont des fichiers statiques, comparés par diff, et la régénération du jeu a été rejouée dans une copie de travail par l'audit z01.

## Mesuré

- **Accueil racine (`/`)** : une tuile « Formulaires selon Opquast V5 » ajoutée en fin de grille ; le pied de page et le favicon basculent d'e-commerce vers formulaires. Le libellé du ZIP passe de « Télécharger les slides 1 à 66 (ZIP) » à « Télécharger les slides » (voir r1-z02-004).
- **`published-versions.json`** : une entrée ajoutée, aucune entrée existante modifiée.
- **`formulaires-opquast-v5/build.py`** : nouveau jeu ; régénération identique octet pour octet aux 6 sorties commitées ; n'écrit pas l'accueil racine.

## Raisonné

Aucun.

## Non couvert

- Comportement JavaScript des pages du jeu, confié au volet visuel.

Aucune nouvelle erreur, aucune surprise. Le jugement d'intention revient à l'humain.
