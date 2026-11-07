# Prompt image_gen — slide 30 — tentative a001

Use case: productivity-visual.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète en français, exactement 1672 × 941 px. Une seule image.
Source verrouillée : storyboard-v002.md, S30, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S01 proposée VALIDEE_PRODUCTION, ancre visuelle de série. Conserver son en-tête, son échelle typographique, footer, marges et palette ; ne reprendre ni titre, ni scène, ni slogan, ni pagination.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Un e-mail « Ne pas répondre » ne doit pas être une impasse
Grand titre centré, deux lignes au maximum. Aucun sous-titre.
Badge exact sous le titre, aligné à droite : R. 111

Scène principale : un e-mail qui refuse la réponse propose une issue immédiate pour contacter le service.
Storyboard : un grand e-mail schématique en gros plan, frontal, qui occupe le centre. Il contient en haut un avertissement de ne pas répondre, placé sur un bandeau orange très pâle avec un petit signe d’attention ; en bas un grand bloc vert clair contenant les pictogrammes de formulaire et téléphone et la phrase de contact. Ces deux pictogrammes restent dans le même e-mail, jamais un renvoi hors du message. Aucune adresse, aucun numéro lisible, aucune date, aucun nom de service ou expéditeur, aucune barre de pseudo-texte. Une petite enveloppe filaire suffit à identifier le support. Ne pas représenter une interdiction de contacter l’organisation : seule la réponse directe est indisponible.
Continuité : après l’accusé de réception, chaque message laisse une possibilité de contact.

Texte visible exact dans l’e-mail, sans les séparateurs de liste :
Merci de ne pas répondre à ce message.
Une question ? Contactez-nous via notre formulaire ou par téléphone.
Ne pas ajouter de texte dans les pictogrammes. La seconde phrase peut tenir sur deux lignes bien espacées.

En-tête exact haut gauche :
QUALITÉ WEB
EXPÉRIENCES DURABLES
En-tête exact haut droit :
Opquast
DES SITES MEILLEURS POUR TOUS
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 30 / 42
Aucun slogan.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Un e-mail « Ne pas répondre » ne doit pas être une impasse
- R. 111
- Merci de ne pas répondre à ce message.
- Une question ? Contactez-nous via notre formulaire ou par téléphone.
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 30 / 42

Contraintes critiques : tous les mots exacts et dans le bon ordre ; guillemets français dans le titre ; accents sur répondre, à, être, téléphone ; trait d’union de Contactez-nous ; aucun numéro de téléphone ou adresse ; la phrase de contact et ses pictogrammes se trouvent dans le mail ; footer avec petit point médian « · » U+00B7. Les deux moyens illustrés sont un exemple, pas une exigence de deux moyens dans chaque mail.
À éviter : slogan, nom fictif ajouté, adresse e-mail ou téléphone lisible, métadonnées inventées, textes de boutons, pseudo-texte, marque réelle ajoutée, logo inventé, notes orales, badge d’acte, fil d’Ariane, barre ou pastilles de progression, photo corporate, 3D, gros dégradé, texture, ombre décorative, blob, callout rouge, fond sombre dominant.
Rejet si : texte manquant ou déformé, guillemets ou accents incorrects, message de contact extérieur au mail, no-reply présenté comme interdit, footer ou pagination incorrects, numéro lisible, texte ajouté, coupé ou illisible, dimensions hors tolérance de 3 px. Test rapide estimé ; test humain au gate.
