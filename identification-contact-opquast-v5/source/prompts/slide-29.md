# Prompt image_gen — slide-29-a002

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète, exactement 1672 × 941 px. Une seule image.
Source verrouillée : storyboard-v002.md, S29, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S01, ancre de série pour en-tête et footer. Image 2 : étalon de composition, style seulement, aucun texte à recopier.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Ma demande est-elle bien arrivée ?
Aucun sous-titre. Badge bleu très clair R. 110 entièrement SOUS le titre, à droite y=210–260, au-dessus du contenu. Ne pas ajouter de bouton, de délai ou de message de réussite à l’écran : l’objet de la slide est l’accusé reçu par e-mail. Conserver le point de la phrase Une trace archivable.
Scène principale : Un flux horizontal en deux temps : à gauche un formulaire envoyé, deux champs fermés vides et un pictogramme d’avion en papier, puis une grande flèche vers une boîte de réception à droite. Un e-mail y arrive, avec une enveloppe et une coche verte. L’e-mail affiche intégralement son objet : Objet : Nous avons bien reçu votre demande, sur deux lignes si besoin. Le corps de l’e-mail reste blanc sans barres ou lignes de pseudo-texte. La boîte de réception est identifiable par son plateau et l’enveloppe, sans titre ajouté. En bas un bandeau vert très pâle porte Une trace archivable. Pas d’adresse électronique, d’expéditeur ou de date.
Storyboard : Un flux horizontal en deux temps : à gauche un formulaire envoyé, deux champs fermés vides et un pictogramme d’avion en papier, puis une grande flèche vers une boîte de réception à droite. Un e-mail y arrive, avec une enveloppe et une coche verte. L’e-mail affiche intégralement son objet : Objet : Nous avons bien reçu votre demande, sur deux lignes si besoin. Le corps de l’e-mail reste blanc sans barres ou lignes de pseudo-texte. La boîte de réception est identifiable par son plateau et l’enveloppe, sans titre ajouté. En bas un bandeau vert très pâle porte Une trace archivable. Pas d’adresse électronique, d’expéditeur ou de date.
Texte visible exact :
Objet : Nous avons bien reçu votre demande
Une trace archivable.

En-tête exact haut gauche sur deux lignes : QUALITÉ WEB en gras ; EXPÉRIENCES DURABLES en graisse normale.
En-tête exact haut droit sur deux lignes : Opquast en gras ; DES SITES MEILLEURS POUR TOUS en graisse normale.
Conserver l’en-tête corrigé de S01 : UN seul espace normal entre chaque mot, notamment MEILLEURS POUR, écart maximal de 2 px avec le plus grand autre espace.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 29 / 42
Aucun slogan.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 29 / 42
- Ma demande est-elle bien arrivée ?
- Objet : Nous avons bien reçu votre demande
- Une trace archivable.
- R. 110

Contraintes critiques : tous les mots visibles exacts, sans ajout ni retrait ; accents, apostrophes typographiques, guillemets français, tirets et numéros relus lettre à lettre. Les séparateurs de liste sont remplacés par la disposition ; pas de point final isolé sur le seul dernier élément d’une énumération en cartes. Conserver les points des phrases complètes. Footer : petit point médian U+00B7, jamais une puce. Coordonnées seulement en pictogrammes et zones neutres. Ne jamais remplacer un contenu attendu par un gabarit vide.
À éviter : texte parasite, pseudo-texte y compris barres ou lignes imitant des mots, notes orales, corrigé de checkpoint, badge d’acte, marque réelle ajoutée, logo inventé, nom fictif hors fiche, adresse, téléphone ou immatriculation lisibles, SIREN, photo, 3D, texture, gros dégradé, ombre décorative, blob, progression ajoutée, callout rouge.
Rejet si : faute, ajout, omission, inversion de sens ou numéro, texte coupé ou illisible, pseudo-texte, mauvais badge, footer ou pagination, espace MEILLEURS POUR excessif, masque incohérent, dimensions hors tolérance de 3 px. Test des trois secondes estimé par l’assistant ; aucun test humain chronométré.


## Reprise ciblée PRIORITAIRE
Image 3 : candidates/slide-29-a001.png, CIBLE DE MODIFICATION. Images 1 et 2 : références de série seulement.
Défaut observé : Le badge R. 110 est à la hauteur du titre.
Invariants : Titre, objet exact du mail, phrase Une trace archivable., en-tête, footer, pagination, flux, pictogrammes, traits de mouvement et tous les éléments du corps.
Correction visuelle : Déplacer UNIQUEMENT le badge R. 110 vers le bas, x=1450–1640 et y=205–260 environ. Réduire sa hauteur à 55 px si nécessaire. Le badge est entièrement sous le bas du titre et entièrement au-dessus du panneau bleu qui commence y=277. Effacer son ancienne position en blanc ; fond du badge bleu très clair et caractères marine identiques. Aucun autre élément ne bouge.
Interdit : Ne pas dupliquer le badge ni changer son numéro. Ne pas déplacer le panneau, modifier l’objet du mail, l’avion, l’enveloppe ou les traits de mouvement.

