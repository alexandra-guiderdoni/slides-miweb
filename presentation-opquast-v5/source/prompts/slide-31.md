ÉDITION CIBLÉE — S31 a003 — correction ShipGuard validée par Alex le 8 novembre 2026.
Source verrouillée : storyboard-v003.md, SHA-256 5b0d813679e9f6f041850c648102751cd9a61393a3ae203d020a9a041920c8c5. Écart autorisé : le texte du bandeau CSS passe de deux à trois lignes, pour ajouter les accolades externes manquantes. Ne pas modifier le storyboard.

Input images: Image 1: finals/slide-31-impression-sans-navigation.png, a002, seule image à modifier ; Image 2: finals/slide-26-texte-justifie.png, étalon de série pour le rendu du code ; Image 3: finals/slide-30-styles-impression.png, ancre A-ODETTE.
Les références 2 et 3 transmettent seulement la grammaire graphique et l’apparence d’Odette, jamais leurs textes, leur en-tête, leur footer, leur numérotation ni leur thème.
Type d’actif : image finale de slide 16:9, exactement 1672 × 941 pixels, même cadrage que l’image 1.
Titre exact : Sur papier, les menus ne servent à rien
Scène principale : conserver exactement la scène de l’image 1, Odette pointant le menu imprimé, deux feuilles dans le panneau corail, une feuille de contenu dans le panneau vert, croix, coche et flèche bleue.
Storyboard : Odette constate que les menus imprimés ne servent à rien ; la version imprimée conserve seulement le contenu. Reprise ciblée du bandeau CSS, sans recomposition de la scène.

Défaut observé : les accolades externes du bloc @media sont absentes ; le code projeté ne constitue pas un bloc CSS valide.
Correction visuelle attendue : remplacer seulement le contenu du bandeau bleu clair par exactement les trois lignes suivantes, en police à chasse fixe, avec le même style, les mêmes couleurs et le même poids qu’aujourd’hui :

```css
@media print {
  nav { display: none; }
}
```

La première ligne possède une espace entre print et l’accolade ouvrante. La deuxième commence par exactement DEUX espaces de la police à chasse fixe : le n de nav est décalé d’exactement DEUX largeurs de caractère par rapport au @, surtout pas trois. La troisième contient uniquement l’accolade fermante externe, alignée avec le @ de la première ligne. Aucun point après print.

CONTRAINTE GÉOMÉTRIQUE PRIORITAIRE : faire tenir les trois lignes dans le bandeau bleu EXISTANT (environ x=45 à 1630, y=675 à 767), sans l’agrandir vers le bas. Réduire légèrement la taille du code uniquement si nécessaire, tout en gardant sa police à chasse fixe, son poids et ses couleurs. Viser trois lignes espacées d’environ 27 pixels, avec une marge intérieure en haut et en bas. Les encadrés IMPACT et GARANTIE doivent conserver EXACTEMENT leurs dimensions et positions d’origine : x≈35 à 847 et x≈860 à 1633, y≈780 à 867, hauteur≈87 pixels. Ne déplacer leur bord supérieur ni vers le bas ni vers le haut. Ne réduire aucune icône, aucune lettre ni aucun encadré. Ne rien changer en dehors de l’intérieur du bandeau bleu. Le footer reste inchangé et dégagé.

Invariants à préserver : tout le reste de l’image 1. Odette identique : visage, cheveux blancs courts, boucles d’oreilles, cardigan beige, crayon, geste de pointage, posture et expression. Conserver les feuilles, les blocs abstraits, les panneaux, la bibliothèque, la fenêtre, la table, les livres, les feuillages, la croix, la coche et la flèche. Préserver le titre, sa taille et sa position, le badge R. 196, les deux encadrés et leurs dimensions, toutes les marges et le cadrage.

Texte visible conservé, exactement :
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Sur papier, les menus ne servent à rien
- R. 196
- IMPACT - Les menus imprimés gaspillent le papier
- GARANTIE - Seul le contenu s’imprime
- RÈGLES OPQUAST · PRÉSENTATION
- 31 / 40

Contraintes critiques : changer uniquement le bloc CSS. Les mots IMPACT et GARANTIE restent en bleu marine ; la couleur des encadrés et leur icône portent le sens. Aucune modification de personnage, de texte, de couleur ou de composition hors du bandeau. Pas de chevauchement avec les encadrés ni avec le footer. Les accolades et le point-virgule doivent être nets et lisibles ; aucune quatrième ligne.
À éviter : toute autre retouche, texte parasite, point après print, accolade omise, indentation différente de deux espaces, ligne tronquée, recomposition de la slide, modification d’Odette, réduction des encadrés, débordement sur le footer.
