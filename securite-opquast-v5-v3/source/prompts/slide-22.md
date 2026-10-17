# Prompt ImageGen - slide 22

## Fiche PDS

- Rôle dans la colonne vertébrale : traiter la règle 212 après le contrôle des cadres.
- Idée principale : la politique doit limiter les origines autorisées pour chaque famille de contenus.
- Scène : une page reçoit quatre familles de ressources depuis une liste d'origines autorisées et bloque les autres.
- Objet-système : navigateur central alimenté par quatre canaux contrôlés.
- Transformation visible : ressources autorisées admises, origine non autorisée arrêtée.
- Ce que l'image seule doit faire comprendre : les sources des scripts, styles, images et polices sont sélectionnées.
- Préparation de la suite : une origine autorisée ne garantit pas encore l'intégrité du fichier.
- Contraintes critiques : ne pas inventer de domaine, conserver les quatre familles et le nom complet de la politique.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Créer une slide institutionnelle française reprenant exactement le masque clair des étalons validés Sécurité Opquast V5 V3 : fond blanc dominant, petit bandeau supérieur, grand titre bleu marine aligné à gauche, badge de règle bleu clair en haut à droite, panneaux pastel très clairs, illustrations plates, traits fins, beaucoup d'espace blanc, callout bleu clair centré en bas, footer bas gauche et pagination bas droite. Typographie Marianne obligatoire, Arial seulement comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucune ombre lourde, aucun logo.

Composition : un navigateur central reçoit quatre flux autorisés, représentés par des icônes distinctes de script, style, image et police. Ces quatre flux viennent d'une zone verte ou bleue intitulée par la question sur les origines. Un cinquième flux corail venant d'une origine non autorisée est arrêté avant la page. La politique Content-Security-Policy est représentée comme une barrière de sélection, pas comme une garantie absolue. Le callout de contrôle est bleu clair. La limite apparaît dans un cartouche orange pâle distinct.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 212`
- `Restreindre l'origine des contenus`
- `Quelles origines sont autorisées ?`
- `Scripts · Styles · Images · Polices`
- `CONTRÔLE - Lire la politique Content-Security-Policy`
- `LIMITE - Une politique trop permissive peut être présente sans protéger efficacement`
- `Opquast - présentation Miweb`
- `22 / 30`

Contraintes critiques : conserver les quatre familles dans cet ordre ; ne pas ajouter de domaines, d'URL, de directives CSP ni de code ; ne pas suggérer qu'une CSP présente est nécessairement efficace ; aucun texte parasite.
