# Prompt ImageGen - slide 08

## Fiche PDS

- Rôle dans la colonne vertébrale : montrer le premier contrôle complet.
- Idée principale : quatre preuves techniques distinctes doivent être inspectées sans conclure pour tout le service.
- Scène : une développeuse inspecte une fenêtre réseau stylisée avec quatre repères numérotés.
- Personnage ou objet-système : outils réseau du navigateur et certificat.
- Transformation visible : quatre observations produisent un contrôle borné par une limite explicite.
- Ce que l'image seule doit faire comprendre : HTTPS ne se contrôle pas par un cadenas unique.
- Contraintes critiques : quatre preuves exactes, HSTS avec max-age, aucune ressource HTTP, limite lisible.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, exactement 1672 x 941 pixels.

Reprendre le masque clair des quatre étalons : fond blanc, titre bleu marine, badge ou repère bleu clair, panneaux gris froid, vert pour les contrôles positifs, orange pour la limite, corail uniquement si une ressource HTTP est explicitement refusée, illustration plate, typographie Marianne avec Arial comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : sous le bandeau commun, placer une développeuse devant un grand panneau d'outils réseau stylisé. Quatre repères numérotés et lisibles pointent vers une page et ses ressources en HTTPS, un certificat signé et valide, l'entête Strict-Transport-Security avec max-age, puis l'absence de ressource chargée en HTTP. En bas, un large callout orange pâle nomme la limite. La scène doit être un contrôle concret, pas une interface réaliste surchargée.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `CONTRÔLE`
- `197 - Pages et ressources en HTTPS`
- `198 - Certificat signé et valide`
- `199 - Strict-Transport-Security avec max-age`
- `200 - Aucune ressource chargée en HTTP`
- `LIMITE - Une page ne représente pas tout le service`
- `Opquast - présentation Miweb`
- `08 / 30`

Masque commun : repère supérieur, scène centrale, callout de limite centré en bas, footer bas gauche, pagination bas droite. Aucun logo.

Contraintes critiques : conserver le tiret simple entre chaque numéro et son libellé ; conserver `Strict-Transport-Security` et `max-age` exactement dans le seul libellé autorisé `199 - Strict-Transport-Security avec max-age` ; ne pas écrire de valeur numérique de max-age ; ne pas écrire `HTTP`, `HTTPS`, `CSS`, un nom d'entête ou tout autre mot à l'intérieur de la fausse interface, des icônes ou des ressources ; y utiliser uniquement des traits abstraits sans caractères lisibles ; ne pas confondre HTTPS et HTTP ; ne pas ajouter de résultat global, d'adresse, de code long, de marque, de logo ou de texte parasite.
