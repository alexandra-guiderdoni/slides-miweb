# Prompt image_gen — slide 20 — tentative a004

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Éditer UNE image, exactement 1672 × 941 px, sans recadrage ni remplissage.
Source verrouillée : storyboard-v002.md, S20, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Arbitrage d’Alex du 7 novembre 2026 : une seule tentative a004 autorisée.
Image 1 : candidates/slide-20-a003.png, CIBLE DE MODIFICATION.
Image 2 : finals/slide-01-qui-se-cache-derriere.png, ancre de série pour l’en-tête et le footer, déjà présents sur la cible.
Image 3 : finals/slide-13-trois-questions-identite.png, étalon de style seulement. Ne copier aucun de ses textes ou badges.

## Reprise ciblée
Défaut observé : les trois onglets de la rangée C sont vides alors que la situation demande des titres complets.
Invariants à préserver : rangées A et B intégralement, leurs dimensions, leurs textes, leurs guillemets et leur ponctuation ; titre, question, libellés, phrase C, en-tête, footer et pagination. Ne rien changer hors des trois onglets C et de l’extrait vide si son déplacement est nécessaire.
Correction visuelle : changer UNIQUEMENT les trois onglets de la rangée C. Les agrandir autant que nécessaire pour afficher, en entier et lisiblement, de gauche à droite : Contact – Les Ateliers du Pont ; Horaires – Les Ateliers du Pont ; Tarifs – Les Ateliers du Pont. Chaque titre commence par une petite icône générique de navigateur : un globe filaire neutre, identique sur les trois onglets. Les trois titres sont sans guillemets, sans point final, avec un tiret demi-cadratin « – ». Exploiter toute la largeur disponible de C : trois onglets larges, texte à une ligne si possible ; l’extrait <head> vide reste à droite ou se déplace dessous si nécessaire. On peut réduire raisonnablement le corps de ces seuls titres pour qu’ils restent entiers. Aucun titre ne doit être tronqué ou abrégé. Le code ne contient toujours que <head> et </head>, sans élément entre eux.
Interdit : toucher aux rangées A et B, au titre, à la question, aux libellés, à la phrase C, à l’en-tête, au footer ou à la pagination. Aucune icône de site, aucun logo, aucune clé en C ; seulement le globe générique identique. Aucun corrigé, aucun numéro de règle, aucun badge, aucune coche de réponse.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Checkpoint 2 : trois rangées d’onglets
Aucun sous-titre, aucun slogan, aucun badge.
Scène principale : trois rangées d’onglets A, B et C, sans réponse projetée.
Storyboard : A nomme le site sans distinguer les contenus ; B nomme les contenus sans le site ; C affiche des titres complets et un extrait head vide. Les trois situations restent neutres, sans diagnostic visible.

Texte visible exact :
Quelle règle n’est pas respectée ?
A. Trois onglets : puis trois onglets portant chacun « Les Ateliers du Pont »
B. Trois onglets : puis les onglets « Contact », « Horaires », « Tarifs »
C. Des titres complets, mais aucun link rel="icon" dans le code.
Contact – Les Ateliers du Pont
Horaires – Les Ateliers du Pont
Tarifs – Les Ateliers du Pont
<head>
</head>
Les énumérations A et B sont réparties en onglets, sans virgule ni point isolé sur le dernier. La phrase complète C conserve son point. Le code link rel="icon" est dans la phrase C seulement, jamais entre les balises.

En-tête exact haut gauche : QUALITÉ WEB, en gras, puis EXPÉRIENCES DURABLES, en graisse normale.
En-tête exact haut droit : Opquast, en gras, puis DES SITES MEILLEURS POUR TOUS, en graisse normale.
Un seul espace normal entre les mots ; conserver l’espacement actuel de la cible, notamment MEILLEURS POUR.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 20 / 42

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Checkpoint 2 : trois rangées d’onglets
- Quelle règle n’est pas respectée ?
- A. Trois onglets :
- « Les Ateliers du Pont » (trois fois en A)
- B. Trois onglets :
- « Contact »
- « Horaires »
- « Tarifs »
- C. Des titres complets, mais aucun link rel="icon" dans le code.
- Contact – Les Ateliers du Pont
- Horaires – Les Ateliers du Pont
- Tarifs – Les Ateliers du Pont
- <head>
- </head>
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 20 / 42

Contraintes critiques : chaque chaîne relue lettre à lettre ; accents, apostrophes typographiques, guillemets français de A et B, tiret demi-cadratin de C, guillemets droits du code et point médian exacts. Ne pas imprimer les indications de composition.
À éviter : tout autre texte, pseudo-texte, barres imitant des mots, coordonnées lisibles, marque ajoutée, logo, clé, numéro de règle, badge, corrigé, note orale, slogan, changement de masque.
Rejet si : un titre C tronqué, abrégé, manquant ou déformé ; icône de site ou clé en C ; corrigé, numéro de règle ou badge ; changement des invariants ; faute, ajout, omission, texte parasite ; espace MEILLEURS → POUR dépassant de plus de 2 px le plus grand autre espace ; dimensions hors tolérance de 3 px. Échec a004 = STOP_SERIE, aucune tentative suivante.
