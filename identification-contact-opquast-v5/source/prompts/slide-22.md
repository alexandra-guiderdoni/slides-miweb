# Prompt image_gen — slide-22-a002

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète, exactement 1672 × 941 px. Une seule image.
Source verrouillée : storyboard-v002.md, S22, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S01, ancre de série pour en-tête et footer. Image 2 : étalon de composition, style seulement, aucun texte à recopier.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Deux moyens de contact, pas un seul
Aucun sous-titre. Badge R. 107 sous le titre, aligné à droite.
Scène principale : Un pictogramme d’utilisateur à gauche se sépare en deux chemins bien visibles. Chemin supérieur : formulaire rectangulaire avec champs vides et signe d’erreur orange. Chemin inférieur : téléphone avec coche verte. Le premier chemin est bloqué, le second reste utilisable. La phrase Formulaire en panne ? → Téléphone. peut être au-dessus du diagramme ; la phrase Au moins deux moyens, qui fonctionnent. dans un bandeau vert très pâle en bas. Aucun mot dans les pictogrammes, aucun trait simulant du texte dans le formulaire.
Storyboard : Un pictogramme d’utilisateur à gauche se sépare en deux chemins bien visibles. Chemin supérieur : formulaire rectangulaire avec champs vides et signe d’erreur orange. Chemin inférieur : téléphone avec coche verte. Le premier chemin est bloqué, le second reste utilisable. La phrase Formulaire en panne ? → Téléphone. peut être au-dessus du diagramme ; la phrase Au moins deux moyens, qui fonctionnent. dans un bandeau vert très pâle en bas. Aucun mot dans les pictogrammes, aucun trait simulant du texte dans le formulaire.
Texte visible exact :
Formulaire en panne ? → Téléphone.
Au moins deux moyens, qui fonctionnent.

En-tête exact haut gauche sur deux lignes : QUALITÉ WEB en gras ; EXPÉRIENCES DURABLES en graisse normale.
En-tête exact haut droit sur deux lignes : Opquast en gras ; DES SITES MEILLEURS POUR TOUS en graisse normale.
Conserver l’en-tête corrigé de S01 : UN seul espace normal entre chaque mot, notamment MEILLEURS POUR, écart maximal de 2 px avec le plus grand autre espace.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 22 / 42
Aucun slogan.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 22 / 42
- Deux moyens de contact, pas un seul
- Formulaire en panne ?
- →
- Téléphone.
- Au moins deux moyens, qui fonctionnent.
- R. 107

Contraintes critiques : tous les mots visibles exacts, sans ajout ni retrait ; accents, apostrophes typographiques, guillemets français, tirets et numéros relus lettre à lettre. Les séparateurs de liste sont remplacés par la disposition ; pas de point final isolé sur le seul dernier élément d’une énumération en cartes. Conserver les points des phrases complètes. Footer : petit point médian U+00B7, jamais une puce. Coordonnées seulement en pictogrammes et zones neutres. Ne jamais remplacer un contenu attendu par un gabarit vide.
À éviter : texte parasite, pseudo-texte y compris barres ou lignes imitant des mots, notes orales, corrigé de checkpoint, badge d’acte, marque réelle ajoutée, logo inventé, nom fictif hors fiche, adresse, téléphone ou immatriculation lisibles, SIREN, photo, 3D, texture, gros dégradé, ombre décorative, blob, progression ajoutée, callout rouge.
Rejet si : faute, ajout, omission, inversion de sens ou numéro, texte coupé ou illisible, pseudo-texte, mauvais badge, footer ou pagination, espace MEILLEURS POUR excessif, masque incohérent, dimensions hors tolérance de 3 px. Test des trois secondes estimé par l’assistant ; aucun test humain chronométré.


## Reprise ciblée PRIORITAIRE
Image 3 : candidates/slide-22-a001.png, CIBLE DE MODIFICATION. Images 1 et 2 : références de série seulement.
Défaut observé : Le badge R. 107 est à la même hauteur que le titre.
Invariants : Tous les textes exacts, titre, scène, objets, traits, couleurs, en-tête, footer et pagination. Rien d’autre ne bouge.
Correction visuelle : Déplacer uniquement le badge R. 107 vers le bas dans la bande BLANCHE sous le titre et au-dessus du panneau de contenu : badge x=1450–1640, y=179–229 environ. Réduire sa hauteur à 50 px et son texte à 32 px si nécessaire, sans toucher aux caractères R. 107. Effacer son ancienne position en blanc. Son sommet est sous le bas du titre, son bas reste au-dessus du panneau bleu qui commence vers y=235. Aucun chevauchement.
Interdit : Changer le titre, déplacer le panneau, toucher aux autres objets ou textes, dupliquer le badge, lui faire toucher le titre ou le panneau.

