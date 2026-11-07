# Prompt image_gen — slide 18 — tentative a002

Use case: productivity-visual.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète, exactement 1672 × 941 px, paysage. Une seule image.
Source verrouillée : storyboard-v002.md, S18, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S01, ancre de série pour en-tête et footer. Image 2 : étalon proche de la composition, grammaire visuelle seulement ; aucun de ses textes n’est à reproduire.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Une icône pour repérer le site d’un coup d’œil
Aucun sous-titre.
Badge exact, sous le titre aligné à droite : R. 104
Scène principale : à gauche, une barre d’onglets où l’un porte une icône générique grise (orange) et l’autre une petite icône de clé à molette (vert). À droite, un extrait de code dans une carte grise, avec une coche indiquant que l’élément est présent dans l’en-tête et bien formé.
Storyboard : Deux objets distincts : à gauche deux onglets sans texte, l’un avec icône générique grise et vigilance orange, l’autre clé à molette et coche verte. À droite une grande carte grise de code. Afficher le code sur trois lignes, en grande police monospace de 36 px minimum, avec retours à la ligne entre attributs si nécessaire. Afficher dans le <head> et syntaxe correcte comme deux annotations simples, pas comme code supplémentaire. Tous les guillemets des attributs sont des guillemets DROITS ASCII doubles. Aucune balise ni texte supplémentaire ; ne pas écrire des guillemets courbes dans le code. Le point de syntaxe correcte appartient à une étiquette et peut être omis selon la consigne de lot.
Texte visible exact, réparti sans ajout en blocs :
<link rel="icon" type="image/png" href="/favicon.png">
dans le <head>
syntaxe correcte
En-tête exact haut gauche :
QUALITÉ WEB
EXPÉRIENCES DURABLES
En-tête exact haut droit :
Opquast
DES SITES MEILLEURS POUR TOUS
Les secondes lignes sont en graisse normale. Espacement régulier avec UN espace normal entre chaque mot, surtout MEILLEURS POUR : cet espace doit rester égal aux autres à 2 px près. Reprendre l’en-tête corrigé de S01.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Petit point médian U+00B7, jamais une puce. Aucun slogan.
Contraintes critiques : lettre à lettre, accents, apostrophes typographiques, guillemets, ponctuation et numéros exacts. Zéro mot ajouté ni retiré. Les séparateurs de liste peuvent être remplacés par la disposition. Aucun point final isolé sur le dernier élément d’une énumération en cartes ; conserver les points des phrases complètes.
À éviter : texte parasite, pseudo-texte y compris petites barres simulant des mots, adresse, téléphone ou immatriculation lisibles, SIREN, marque réelle ajoutée, nom fictif hors fiche, logo inventé, notes orales, corrigé sur checkpoint, badge d’acte, fil d’Ariane, progression ajoutée, photo, 3D, blob, texture, ombre décorative, fond sombre, callout rouge.
Rejet si : faute, ajout, omission, inversion de sens ou de numéro, pseudo-texte, texte coupé ou illisible, mauvais badge, footer ou pagination, espace MEILLEURS POUR excessif, masque incohérent, dimensions hors tolérance de 3 px. Test des trois secondes estimé par l’assistant, aucun test humain chronométré.
Pagination exacte : 18 / 42

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Une icône pour repérer le site d’un coup d’œil
- R. 104
- <link rel="icon" type="image/png" href="/favicon.png">
- dans le <head>
- syntaxe correcte
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 18 / 42

## Reprise ciblée
Image 3 : candidate S18 a001, cible de modification.
Défaut observé : le badge R. 104 est à hauteur du titre.
Invariants : conserver tout le corps, le code caractère par caractère, les annotations, les icônes, la palette, l’en-tête, le footer et la pagination.
Correction visuelle : déplacer seulement le badge sous le titre, à droite, x=1450–1640 y=200–258. Le badge doit avoir un fond bleu très clair comme les autres règles. Recentrer le titre au besoin dans la largeur disponible, sans changer sa taille ni ses mots. Le bas du badge doit rester au-dessus du cadre de contenu.
Interdit : badge à hauteur du titre, badge vert vif, modification du code ou ajout de texte. Une seule correction de placement.

