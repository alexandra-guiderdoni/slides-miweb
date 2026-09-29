# Slide 16 - Connaître le temps disponible avant d'agir

## Prompt d'édition utilisé pour produire la V2

Image source : `navigation-opquast-v5-essentielle/assets/slides/slide-16.png`, copiée dans la variante avant édition.

```text
Use case: precise-object-edit.
Asset type: final French presentation slide, 1672 x 941 pixels.
Edit target: the supplied slide 16 image.

Primary request: replace only the existing visible sentence "IMPACT - Une limite inconnue peut faire perdre données et temps" with the exact sentence "IMPACT - Une limite inconnue peut faire perdre des données et du temps".

Text accuracy is mandatory. Render the replacement exactly once, with this exact spelling, capitalization, accents and simple hyphen:
"IMPACT - Une limite inconnue peut faire perdre des données et du temps"

Constraints:
- Change only that one impact sentence.
- Preserve the complete original composition, illustration, colors, typography, spacing, icons, cards, footer and pagination as closely as possible.
- Preserve every other visible string exactly as it appears in the input image.
- Keep the canvas exactly 1672 x 941 pixels.
- The replacement may remain on two lines inside the existing impact card, but must be fully visible and readable.
- Do not add, remove, repeat or rewrite any other text.
- No logo, watermark, pseudo-text or new visual element.
- Output one complete final slide only.
```

## Sortie attendue

Créer UNE SEULE image finale de slide de présentation, au format paysage 16:9, exactement 1672 x 941 pixels. Cette image est la slide finale, pas une maquette, pas une planche de variantes et pas une slide montrée dans un écran. Tout le texte doit être généré directement dans l'image par ImageGen. Aucun texte, élément graphique ou ajustement ne sera ajouté après la génération.

## Références visuelles et style

Les images fournies des séries Internationalisation Opquast et Newsletter Opquast sont uniquement des références de style. En reprendre la sobriété institutionnelle, la hiérarchie très lisible, le fond blanc lumineux, les cartes légèrement arrondies, les aplats pastel, les pictogrammes vectoriels simples et les grands espaces de respiration. Ne reprendre aucun texte, logo, emblème, nom ou contenu de ces références.

- Typographie Marianne pour tout texte visible, avec Arial comme seul fallback explicite.
- Titre aligné à gauche, bleu marine profond, très lisible.
- Bleu pour l'information préalable et la structure.
- Orange pour l'action à venir.
- Vert pour l'action engagée en connaissance de cause.
- Rouge uniquement pour le risque de perte, sans dominer la slide.
- Aucun dégradé décoratif, aucune 3D, aucune photographie, aucune ombre lourde.

## Storyboard concret

Une personne s'apprête à commencer une action dans une interface simple. Avant le bouton d'action, un grand pictogramme d'horloge analogique sans chiffres et un indicateur visuel non chiffré rendent la limite de temps perceptible. Le parcours mène ensuite vers l'action, montrant que l'information est donnée avant l'engagement et non après l'expiration. Un document préservé à la fin du parcours matérialise la protection contre la perte de données.

L'image seule doit faire comprendre que l'utilisateur connaît la contrainte temporelle avant de commencer et peut décider d'agir en conséquence.

## Composition et masque commun

- En haut à gauche : signature textuelle discrète.
- En haut à droite : repère du bloc actif.
- Sous cette ligne : grand titre aligné à gauche, puis badge de règle.
- Au centre : progression simple de gauche à droite, information temporelle, décision de la personne, action engagée, document préservé.
- Sous la scène : cartouche d'impact à gauche et cartouche de garantie à droite.
- En bas, au-dessus du pied de page : callout bleu très clair, centré et stable.
- Tout en bas : pied de page discret, signature à gauche et pagination à droite.

## Textes visibles - liste blanche exacte et exhaustive

Afficher une seule fois chacun des textes suivants, sans faute, sans reformulation et sans ajouter aucun autre mot, chiffre ou caractère textuel :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `E - GARDER LA MAIN`
- `Connaître le temps disponible avant d'agir`
- `RÈGLE 172`
- `IMPACT - Une limite inconnue peut faire perdre des données et du temps`
- `GARANTIE - La durée est annoncée avant l'action ou l'accès`
- `Le temps imposé doit être annoncé.`
- `Opquast - présentation Miweb`
- `16 / 17`

## Contraintes critiques

- Respecter exactement les accents, les apostrophes, les majuscules, la ponctuation et les numéros de la liste blanche.
- Ne montrer aucune durée, heure, minute, seconde, jauge chiffrée ou compte à rebours inventé.
- L'information temporelle doit apparaître clairement avant l'action dans le sens de lecture.
- Ne pas représenter uniquement une alerte après expiration.
- Ne produire aucun texte factice dans l'interface : seulement des formes abstraites non textuelles.
- Ne pas afficher d'autre numéro de règle ou de pagination.
- N'ajouter aucun logo, aucun filigrane et aucun emblème.
- Ne pas modifier l'image après génération : aucun overlay, aucune composition, aucun ajout de texte, aucun SVG, aucun HTML et aucun traitement par script.

Priorité absolue : exactitude des neuf textes autorisés et compréhension immédiate d'une limite de temps annoncée avant l'action.
