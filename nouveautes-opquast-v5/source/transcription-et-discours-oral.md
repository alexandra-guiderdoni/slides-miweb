# Nouveautés d'Opquast V5

Ce fichier reproduit le contenu des deux accordéons de chaque slide, tel qu'il est publié
depuis `slides.json`.

## Origine des textes

Les transcriptions des slides 1 à 10 reprennent sans réécriture les accordéons rédigés
avec les visuels ; seules les balises HTML d'accordéon et les niveaux de titre ont été
transformés, et des sections « Point de vigilance » et « Message à retenir » ont été
ajoutées.

Les transcriptions des slides 11 à 17 ont été rédigées à partir des visuels : ce lot a été
livré sans storyboard ni accordéons. Elles appellent une relecture métier au même titre que
tout texte rédigé en propre.

Les discours oraux des 17 slides ont été révisés le 17 septembre 2026 pour suivre une trame
unique :

1. **Relier la règle à son impact** : quel préjudice concret l'utilisateur subit-il si la
   règle n'est pas appliquée ?
2. **Ce que garantit la règle** : quel bénéfice, quelle maîtrise ou quelle protection la
   règle apporte-t-elle, sans lui attribuer une portée qu'elle n'a pas ?

Le préjudice et la garantie sont ancrés dans les champs officiels de l'API Opquast
(objectifs, explication, vulgarisation, solution et contrôle) pour les onze règles citées
par la série. Les slides 1, 2, 11, 14, 15, 16 et 17 ne portent pas une règle : la trame y
est transposée au mouvement du référentiel, et la section de garantie y dit explicitement
ce qui n'est pas garanti ou ce qui relève d'une pratique et non d'une règle.

## Conventions

Storyboard de cadrage des slides 1 à 10 : `source/storyboard.md`.

Les empreintes SHA-256 ci-dessous sont celles des images publiées dans `assets/slides/`.

Les tirets quadratins ont été remplacés par des traits d'union dans tous les textes. Les
visuels, eux, ne sont pas retouchés et conservent leur typographie d'origine.

---

# Slide 1 - Opquast V4 → V5 : qu’est-ce qui change ?

Image publiée : `assets/slides/slide-01-bilan-v4-v5.png`  
Empreinte PNG : `5fcd2dff6b1b628a073cae303add02113e8453ad17dd75b5e66206a71e88eeeb`

## Transcription

### Lecture du visuel

La slide présente le passage d’Opquast V4 à V5. En haut figurent l’en-tête Qualité Web et la signature Opquast. Le centre montre une chaîne de cartes : V4, 240 règles, puis moins deux règles supprimées, moins une règle par fusion, plus huit nouvelles règles, et enfin V5, 245 règles. En dessous, quatre actions sont affichées : Ajouter, Retirer, Fusionner et Reformuler. Un bandeau final rappelle que le nombre change et que les exigences évoluent de plusieurs façons.

### Message à retenir

**Le nombre change. Les exigences évoluent de plusieurs façons.**

## Discours oral

Passer de 240 à 245 règles ne signifie pas avoir simplement ajouté cinq exigences. La slide montre les opérations derrière le total : deux règles sortent, deux anciennes exigences sont regroupées en une seule, et huit nouvelles règles entrent dans le référentiel.

### Le préjudice d’une lecture comptable

Personne ne subit un solde. Ce que subissent les utilisateurs, ce sont les exigences qui passent à la trappe : une grille reprise au numéro près conserve des contrôles devenus sans objet, en applique d’autres dont le sens a changé, et laisse huit situations nouvelles sans vérification.

### Ce que garantit cette lecture

Rien, à elle seule : c’est une méthode, pas une règle. Elle consiste à regarder les quatre opérations, ajouts, retraits, fusions et reformulations, avant de reporter le moindre numéro dans un outil de travail.

**Mémo oral :** Le nombre change, pas seulement le compteur.

---

# Slide 2 - Ce qui entre : 8 nouvelles règles

Image publiée : `assets/slides/slide-02-huit-nouveautes.png`  
Empreinte PNG : `0f9969636f5cf66079419f7a32ad1e7d5833fb8627d3092b8b152b5c74ef6f6c`

## Transcription

### Lecture du visuel

La slide présente la carte des huit nouvelles règles, réparties en cinq familles : contenus, données personnelles, e-commerce, formulaires et sécurité. Chaque famille contient les numéros et intitulés courts des règles concernées. Les formulaires regroupent les règles 96, 97 et 98. La sécurité regroupe les règles 216 et 217. Un bandeau de conclusion indique que ces nouveautés concernent plusieurs moments de l’expérience utilisateur.

### Message à retenir

**Huit nouveautés, plusieurs moments de l’expérience utilisateur.**

## Discours oral

Cette carte donne la vue d’ensemble des huit nouveautés. Elles ne forment pas un nouveau silo : elles touchent les contenus, les données personnelles, l’e-commerce, les formulaires et la sécurité.

### Relier les règles à leur impact

Les huit règles n’interviennent pas au même moment de l’expérience. Certaines se jouent à la lecture d’un contenu, d’autres à la création d’un compte, à l’achat, au remplissage d’un formulaire ou à la réception d’un courriel. Chercher les nouveautés dans une seule de ces zones revient à en manquer les trois quarts.

### Ce que garantit cette vue d’ensemble

Une orientation avant d’entrer dans le détail : savoir où se situe chaque règle, et donc quelle équipe et quel moment du parcours elle concerne.

**Mémo oral :** Huit nouveautés, cinq familles.

---

# Slide 3 - Règle 14 - caractères détournés

Image publiée : `assets/slides/slide-03-regle-14-caracteres-detournes.png`  
Empreinte PNG : `6f0e054c7976d27820863b815712aef4decfd83db7eff9651171eb2c59d2bc14`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 14. Elle affiche le libellé officiel puis compare deux panneaux : à gauche, une mise en forme native du mot Bonus ; à droite, un exemple de caractères détournés, signalé par une couleur d’attention. La conclusion visible demande de préserver le texte exploitable.

### Message à retenir

**Préserver le texte exploitable.**

## Discours oral

La règle 14 part d’un écart entre l’apparence et le texte réellement exploitable. Un faux gras obtenu avec des caractères Unicode mathématiques ressemble à une mise en forme, mais il remplace les lettres par d’autres caractères.

### Relier la règle à son impact

Pour une personne équipée d’un lecteur d’écran, le mot cesse d’être un mot : la synthèse vocale énonce une suite de caractères sans signification. Le contenu échappe aussi à l’indexation par les moteurs de recherche et au traitement par les outils qui exploitent le texte.

### Ce que garantit la règle

Que le texte reste du texte. La règle n’interdit pas la mise en valeur visuelle : elle interdit de l’obtenir en substituant des caractères, quand les fonctions natives de mise en forme existent.

### Mise en œuvre

Utiliser les fonctions natives de mise en forme de l’éditeur, gras ou italique. Là où ces
fonctions n’existent pas, sur certains réseaux sociaux par exemple, renoncer à l’effet
plutôt que détourner des caractères.

Le contrôle consiste à vérifier que les contenus ne contiennent pas de caractères Unicode
détournés, non alphabétiques en particulier, qui simulent une mise en forme.

### Pour aller plus loin

Le même détournement a servi à un usage plus grave. Les caractères Unicode étant autorisés
dans les noms de domaine, il est possible de fabriquer un faux domaine visuellement
identique à un vrai et de s’en servir pour de l’hameçonnage. La règle ne traite pas ce
cas, mais il éclaire pourquoi un caractère qui ressemble à un autre n’est pas anodin.

**Mémo oral :** Préserver le texte exploitable.

---

# Slide 4 - Règle 26 - existence d’un compte

Image publiée : `assets/slides/slide-04-regle-26-existence-compte.png`  
Empreinte PNG : `04e3b7bc1ae29668c206c4aba2c448b3344ed6cf78f86082505a6b00bea1f229`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 26. Elle montre deux formulaires fictifs de récupération de compte : l’un annoté comme compte existant, l’autre comme compte inexistant. Dans les deux cas, les flèches convergent vers la même réponse publique : si un compte existe, un e-mail a été envoyé. Le bandeau final rappelle qu’il ne faut pas dévoiler l’existence du compte.

### Point de vigilance

Les annotations **Compte existant** et **Compte inexistant** sont des repères pédagogiques ajoutés pour la démonstration. Elles ne figurent pas dans l’interface vue par la personne qui utilise le service : celle-ci ne voit que la réponse commune.

Les adresses affichées sont des exemples fictifs.

### Message à retenir

**Ne pas dévoiler l’existence du compte.**

## Discours oral

La règle 26 traite une information qui ne devrait pas pouvoir être déduite depuis l’extérieur : l’existence d’un compte utilisateur.

### Relier la règle à son impact

Un message trop précis, « cette adresse est déjà utilisée » ou « mot de passe incorrect », confirme à un tiers qu’un compte existe. Cette confirmation est le premier temps d’une attaque : une fois le compte identifié, la personne mal intentionnée peut enchaîner les tentatives de mot de passe. Le préjudice ne s’arrête pas à la fuite d’une information, il ouvre la voie à l’usurpation.

### Ce que garantit la règle

Des réponses neutres et homogènes, à la création de compte, à la connexion et à la récupération de mot de passe. Elle ne rend pas le compte inviolable : elle retire à l’attaquant le moyen de savoir quels comptes existent.

### Mise en œuvre

Le sujet se joue dans la formulation des messages, à la création de compte, à la connexion
et à la récupération de mot de passe.

Messages à éviter, parce qu’ils confirment ou infirment l’existence d’un compte :

- « Cet email est déjà utilisé » ;
- « Mot de passe incorrect » ;
- « Veuillez suivre la procédure de réinitialisation envoyée par mail » ;
- « Compte verrouillé ».

Messages à privilégier, neutres et identiques dans tous les cas :

- « Si vous avez déjà un compte, utilisez la récupération de mot de passe. » ;
- « Identifiants incorrects. Veuillez vérifier votre adresse et mot de passe. » ;
- « Si un compte existe pour cette adresse, un email de réinitialisation a été envoyé. » ;
- « Impossible de se connecter. Réessayer plus tard ou utilisez la récupération de mot de
  passe. »

Un écart aussi mince qu’un message différent entre « mot de passe incorrect » et « compte
inexistant » suffit à une attaque par énumération.

**Mémo oral :** Ne pas dévoiler le compte.

---

# Slide 5 - Règle 68 - provenance des produits

Image publiée : `assets/slides/slide-05-regle-68-provenance.png`  
Empreinte PNG : `affa83201cc1f6c4c64b32732dcd3d41ffde990eff667cbe3b7f7433e3ff9387`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 68. Elle affiche le libellé officiel et une fiche produit fictive avec une tasse, un nom de produit exemple, un prix, une description et une zone Provenance indiquant Fabrication : Portugal. À droite, une illustration de colis et de localisation accompagne le message : connaître la provenance pour choisir.

### Point de vigilance

Le produit, son prix et son pays de fabrication sont des **exemples fictifs**, comme l’indique la mention portée sur le visuel. Ils illustrent l’emplacement de l’information, pas un cas réel.

### Message à retenir

**Connaître la provenance pour choisir.**

## Discours oral

La règle 68 ajoute une information dans le contexte de l’achat.

### Relier la règle à son impact

Sans elle, la personne qui achète décide sans savoir. Le motif de sa question peut être social, écologique, politique ou simplement de la curiosité : dans tous les cas, l’information lui manque au moment où elle choisit, et elle ne peut la retrouver nulle part.

### Ce que garantit la règle

La présence de l’information, et rien d’autre. Quand un produit n’a pas de provenance unique, la réponse attendue distingue le lieu de fabrication, d’assemblage et d’expédition. La règle ne porte aucun jugement sur le pays d’origine, ne vaut pas label écologique et ne promet pas une traçabilité complète.

### Mise en œuvre

Indiquer la provenance dans la fiche produit, ou ailleurs dans le service si la fiche ne
s’y prête pas.

Quand un produit n’a pas de provenance unique, ne pas en choisir une au hasard : distinguer
le lieu de fabrication des composants, le lieu d’assemblage et le lieu d’expédition. Le
message doit refléter la complexité réelle du produit plutôt que la masquer.

**Mémo oral :** Connaître pour choisir.

---

# Slide 6 - Règle 96 - relancer la double authentification

Image publiée : `assets/slides/slide-06-regle-96-relance-2fa.png`  
Empreinte PNG : `fe73bc0bd983339dd17960c3d89d9e26b760fbe40c02bdde5bb9d68dfe985a02`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 96. Elle affiche le libellé officiel et un parcours en trois étapes : demander le code, constater un code expiré ou non reçu, puis relancer. La scène centrale propose un bouton Renvoyer le code. Le bandeau final précise que l’utilisateur doit pouvoir reprendre sans contourner la sécurité.

### Message à retenir

**Pouvoir reprendre sans contourner la sécurité.**

## Discours oral

La règle 96 concerne un cas courant : un code de double authentification peut expirer, ou ne jamais arriver.

### Relier la règle à son impact

L’utilisateur se retrouve devant un formulaire qu’il ne peut plus valider, sans moyen de reprendre. Le parcours ne ralentit pas, il s’arrête : frustration, perte de confiance, et souvent abandon du service, alors que la personne était légitime et à deux doigts d’être connectée.

### Ce que garantit la règle

La possibilité de relancer la procédure. Elle ne demande pas d’affaiblir la sécurité : la relance s’accompagne normalement d’un nombre d’essais limité et de l’invalidation des codes précédents.

### Mise en œuvre

Prévoir un mécanisme de régénération et de renvoi du code, activable par un bouton ou un
lien explicite du type « Renvoyer le code », par SMS, par courriel ou via une application
d’authentification.

Concevoir cette relance avec précaution : limiter le nombre de tentatives, invalider les
codes précédents et tracer les actions, faute de quoi le mécanisme devient lui-même une
faiblesse.

Au-delà de cette règle, Opquast recommande de proposer au moins deux moyens
d’authentification différents, pour la résilience du dispositif et pour les personnes qui
ne peuvent pas utiliser le premier.

**Mémo oral :** Reprendre sans contourner.

---

# Slide 7 - Règle 97 - autocomplétion signalée dans le code

Image publiée : `assets/slides/slide-07-regle-97-autocompletion.png`  
Empreinte PNG : `862a66547037072418d14b8c5a0a75a02094f6ce78bb3310384d060a424b0b9a`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 97. Elle affiche le libellé officiel et relie un champ e-mail à un extrait de code contenant autocomplete égal email. Une flèche indique le passage du champ visible vers le signalement dans le code. Le bandeau final rappelle l’objectif : aider la saisie en donnant le bon signal au navigateur.

### Extrait de code affiché

```html
<input type="email" name="email" autocomplete="email">
```

### Message à retenir

**Aider la saisie en donnant le bon signal au navigateur.**

## Discours oral

La règle 97 ne parle pas des suggestions visibles dans un formulaire, mais de ce que le code source indique au navigateur.

### Relier la règle à son impact

Sans ce signal, le navigateur ne sait pas ce qu’on attend dans le champ et ne propose rien. La saisie devient plus longue et plus fautive pour tout le monde, et l’effort est nettement plus lourd pour les personnes qui utilisent une aide technique ou saisissent difficilement. Dans un tunnel d’achat, cette friction se paie en abandons.

### Ce que garantit la règle

Un champ dont la nature est déclarée dans le code, avec la valeur normalisée qui convient, par exemple `autocomplete="email"` pour une adresse. Elle n’impose pas l’autocomplétion partout : sur les champs sensibles, mot de passe ou code à usage unique, la désactiver reste justifié.

### Mise en œuvre

Renseigner l’attribut `autocomplete` du champ avec la valeur normalisée qui correspond à
son contenu. Les exemples donnés par la règle :

- `username` pour un identifiant de connexion ;
- `email` pour une adresse de courriel ;
- `tel` pour un numéro de téléphone ;
- `country-name` pour un nom de pays ;
- `cc-name` et `cc-number` pour le nom et le numéro d’une carte bancaire.

Réserver `autocomplete="off"` aux champs réellement sensibles, mot de passe ou code à usage
unique. L’utiliser partout prive l’utilisateur d’un confort attendu sans rien sécuriser.

**Mémo oral :** Donner le bon signal au navigateur.

---

# Slide 8 - Règle 98 - boutons désactivés et lecteurs d’écran

Image publiée : `assets/slides/slide-08-regle-98-boutons-desactives.png`  
Empreinte PNG : `2a4ea69b9c04bc5b01c8384f8af1a27caa666e8079b6b413fa1dc63bdd59a2e4`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 98. Elle affiche un formulaire avec plusieurs champs et un bouton Envoyer grisé. À côté du bouton, un état Indisponible est accompagné de l’explication Complétez les champs requis. Un pictogramme de restitution illustre que le bouton reste présent, identifiable et non activable. Le bandeau final indique qu’une action indisponible doit rester compréhensible.

### Message à retenir

**Une action indisponible doit rester compréhensible.**

## Discours oral

La règle 98 porte sur un choix d’interface très répandu : le bouton de validation grisé tant que le formulaire n’est pas complet.

### Relier la règle à son impact

L’attribut `disabled` ne fait pas que bloquer l’action : certains lecteurs d’écran ignorent purement et simplement l’élément. Une personne non voyante ne sait alors pas qu’une action existe à cet endroit. Elle ne cherche pas à comprendre pourquoi le bouton est indisponible : pour elle, il n’y a pas de bouton.

### Ce que garantit la règle

Que le bouton reste perceptible et atteignable, que son état soit annoncé et que la raison de son indisponibilité soit explicite. En pratique, cela conduit à préférer `aria-disabled="true"` à `disabled`. La règle ne rend pas le formulaire conforme pour autant : elle traite ce point précis.

### Mise en œuvre

Ne pas utiliser l’attribut HTML `disabled`, qui retire le bouton de l’arbre d’accessibilité
et peut le rendre inatteignable au clavier.

À la place :

- marquer le bouton avec `aria-disabled="true"`, pour qu’il reste perceptible, atteignable
  et annoncé comme indisponible ;
- bloquer l’action en JavaScript, au clic comme au clavier, puis la réactiver le moment
  venu ;
- expliquer l’indisponibilité avec `aria-describedby` ou `aria-label`, et la rendre visible
  au survol ou à la prise de focus.

Le contrôle porte sur les trois modes d’accès : à l’œil, au clavier et au lecteur d’écran.

**Mémo oral :** Indisponible mais compréhensible.

---

# Slide 9 - Règle 216 - barre d’adresse visible

Image publiée : `assets/slides/slide-09-regle-216-barre-adresse.png`  
Empreinte PNG : `cd771a9d83fe0978187470354a245f1f13dde0fc9eabb38f741998688afab546`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 216. Elle affiche le libellé officiel à côté d’une fenêtre de navigateur. La barre d’adresse visible contient l’adresse `https://service.example`. Le formulaire de connexion est placé sous cette barre. Une légende indique que l’utilisateur conserve un repère sur l’endroit où il se trouve. Le bandeau final demande de garder un repère vérifiable dans le navigateur.

### Point de vigilance

Le domaine `service.example` est un **exemple réservé à la documentation**. Il n’identifie aucun service réel.

### Message à retenir

**Garder un repère vérifiable dans le navigateur.**

## Discours oral

La règle 216 protège un repère simple : la barre d’adresse du navigateur.

### Relier la règle à son impact

Certains services affichent leur formulaire de connexion dans une fenêtre sans barre d’adresse. L’utilisateur saisit alors ses identifiants sans aucun moyen de vérifier où il se trouve : ni le domaine, ni le protocole, ni le certificat. C’est exactement la situation que recherche une tentative d’hameçonnage.

### Ce que garantit la règle

Que le service ne prive pas l’utilisateur de ce repère, notamment en ouvrant des fenêtres qui masquent l’URL. Elle ne prouve pas que le site est honnête : elle préserve le moyen de le vérifier.

### Mise en œuvre

Ne pas recourir aux techniques d’ouverture de fenêtre qui masquent la barre d’adresse,
c’est-à-dire `window.open()` avec des options telles que `location="no"`, `toolbar="no"`,
`fullscreen` ou `kiosk`.

Le contrôle est simple : pour chaque fenêtre ouverte par le service, vérifier que la barre
d’adresse reste visible.

**Mémo oral :** Garder la barre d’adresse visible.

---

# Slide 10 - Règle 217 - domaine de messagerie authentifié

Image publiée : `assets/slides/slide-10-regle-217-domaine-messagerie.png`  
Empreinte PNG : `6a4c06590543cfbb4eceec9ec565f09113faa425f097b8dc05ad2631ea1cdd1a`

## Transcription

### Lecture du visuel

La slide est consacrée à la règle 217. Elle montre un domaine d’envoi, service.example, qui passe par trois vérifications techniques : SPF, DKIM et DMARC, avant d’arriver dans une boîte de réception. Un encadré rappelle qu’il s’agit d’authentifier le domaine d’envoi, pas de certifier tout le message. Le bandeau final demande de vérifier le domaine sans promettre une sécurité absolue.

### Point de vigilance

SPF, DKIM et DMARC sont les mécanismes cités sur le visuel. Le libellé officiel de la règle n’impose pas une liste technique fermée : il demande que le domaine de messagerie soit authentifié.

### Message à retenir

**Vérifier le domaine, sans promettre une sécurité absolue.**

## Discours oral

La règle 217 concerne la messagerie, pas l’apparence d’un message.

### Relier la règle à son impact

Sans authentification du domaine, n’importe qui peut envoyer des courriels qui semblent venir du service : le destinataire n’a aucun moyen de faire la différence. Le préjudice joue dans les deux sens, car les messages légitimes, confirmations de commande ou alertes, finissent eux aussi en indésirables faute de domaine reconnu.

### Ce que garantit la règle

Que le domaine d’envoi soit authentifié, ce qui passe aujourd’hui par SPF, DKIM et DMARC. Elle ne certifie pas le contenu du message et ne garantit pas qu’un courriel est digne de confiance : elle atteste que l’expéditeur est autorisé à écrire au nom du domaine.

### Mise en œuvre

Pour chaque domaine utilisé pour l’envoi de courriels :

- SPF : publier dans le DNS un enregistrement TXT listant les serveurs autorisés à envoyer
  au nom du domaine ;
- DKIM : signer les messages avec une clé privée et publier la clé publique dans le DNS ;
- DMARC : définir une politique, `none`, `quarantine` ou `reject`, et une adresse de retour
  pour recevoir les rapports.

Le contrôle se fait avec un outil de test DNS, puis en analysant les entêtes des courriels
reçus pour confirmer que les signatures s’appliquent réellement.

**Mémo oral :** Authentifier le domaine, pas tout le message.

---

# Slide 11 - Ce qui sort : deux règles

Image publiée : `assets/slides/slide-11-ce-qui-sort-deux-regles.png`  
Empreinte PNG : `f21864d08593a9ccdb8bb4740c4e775cd5c98febed9dbd1ad55737b1606b3554`

## Transcription

### Lecture du visuel

La slide présente les deux règles qui quittent le référentiel. Deux cartes affichent les
anciens libellés de la version 4 : l’une sur les liens externes ouvrant une nouvelle
fenêtre et l’information de contexte, l’autre sur la détectabilité des fils de
syndication. Deux flèches convergent vers un encadré « Hors du référentiel V5 ». Le
bandeau final rappelle qu’une règle supprimée ne devient pas pour autant une mauvaise
pratique.

### Libellés officiels

Le visuel cite les libellés complets des deux règles retirées. Contrôlés le 17 septembre
2026 contre l’API Opquast, version `assurance-qualite-web` :

- règle 25 : « Les liens externes qui ouvrent une nouvelle fenêtre ne partagent pas
  d’information de contexte. »
- règle 235 : « Les fils de syndication sont détectables par les agents utilisateurs. »

Aucune règle équivalente ne figure dans la version 5 : la recherche des termes
« syndication », « RSS », « Atom », « flux » et « agrégateur » n’y renvoie aucun résultat.

### Ce qui reste couvert

Le retrait de la règle 235 ne laisse pas l’utilisateur sans garantie. L’exigence
fondamentale d’information reste pleinement couverte par la règle 1, « Il est possible de
connaître les nouveaux contenus ou services. » Cette règle demeure techniquement neutre et
laisse le choix du canal : Opquast cite en exemple un flux RSS, une rubrique du type
« Actualités du site » ou un canal externe tel qu’un compte de réseau social, et une lettre
d’information répond à la même intention.

Ce qui disparaît avec la règle 235, c’est l’obligation de rendre un fil détectable par les
agents utilisateurs, pas le devoir d’informer sur les nouveautés.

### Message à retenir

**Supprimée ≠ mauvaise pratique.**

## Discours oral

Deux règles sortent du référentiel. C’est le mouvement le plus facile à mal interpréter.

### Relier le retrait à son impact

Une règle retirée ne devient pas une mauvaise pratique, et personne n’est pénalisé en continuant de l’appliquer. Le vrai risque est ailleurs : une grille d’audit héritée de la version 4 conserve deux contrôles qui n’ont plus d’équivalent, et le rapport qui en sort compare un service à un socle qui n’existe plus.

### Ce que garantit ce mouvement

Un référentiel qui reste un socle et non un inventaire cumulatif. Un retrait signifie que la valeur ajoutée de la règle a diminué : la pratique s’est généralisée, le contexte technique a changé, ou l’exigence est mieux portée ailleurs.

Pour les fils de syndication, l’exigence d’informer sur les nouveautés reste portée par la règle 1, qui laisse le choix du canal. C’est le contrôle qui disparaît, pas le besoin de l’utilisateur.

### Le cas de l’ancienne règle 25

L’ancienne règle 25 demandait que les liens externes ouvrant une nouvelle fenêtre ne partagent pas d’information de contexte. Elle se contrôlait lien par lien : tout `target="_blank"` devait porter `rel="noreferrer noopener"`.

Une partie de cette protection est devenue automatique. Les navigateurs modernes traitent désormais `target="_blank"` comme s’il portait `rel="noopener"`, ce que la fiche de la version 4 notait déjà. Une exigence que la plateforme applique d’office perd sa valeur ajoutée dans un socle de qualité : c’est le motif type d’un retrait.

Le volet referrer, lui, n’a pas disparu. Il est traité par une autre règle, au niveau du serveur plutôt que lien par lien, avec l’entête HTTP `Referrer-Policy`.

### Attention au numéro 25

Cette règle sur la politique de communication des referrers portait le numéro 24 en version 4. Avec le retrait de l’ancienne 25 et l’arrivée de la règle 26 sur l’existence d’un compte, la rubrique Données personnelles s’est décalée : la politique de referrers occupe désormais le numéro 25.

Le numéro 25 existe donc dans les deux versions, avec deux exigences sans rapport. C’est le même piège que celui de la slide 14 sur le numéro 235, dans une autre rubrique.

**Mémo oral :** Retirée du socle, pas devenue mauvaise.

---

# Slide 12 - Ce qui fusionne : 2 règles → 1

Image publiée : `assets/slides/slide-12-ce-qui-fusionne-2-regles-vers-1.png`  
Empreinte PNG : `d57ad36e1c018d587a4e571efedf35b2ca37e6325c513d3290dcc3266a367def`

## Transcription

### Lecture du visuel

La slide montre une fusion. Deux cartes de la version 4, l’une sur les tableaux remplacés
par des images, l’autre sur les tableaux simulés avec du texte, convergent vers une carte
unique de la version 5, la règle 245 : « Les tableaux de données ne sont pas simulés. »
Le bandeau final résume le mouvement : deux formulations regroupées, une structure à
préserver.

### Libellés officiels

Le visuel résume les deux règles fusionnées. Leurs libellés complets en version 4,
contrôlés le 17 septembre 2026 contre l’API Opquast, version `assurance-qualite-web` :

- règle 239 : « Les tableaux de données ne sont pas remplacés par des images. »
- règle 240 : « Les tableaux de données ne sont pas simulés à l’aide de texte mis en
  forme. »

La règle 245 de la version 5 couvre les deux cas sous un libellé unique.

### Message à retenir

**Deux formulations regroupées, une structure à préserver.**

## Discours oral

Deux anciennes exigences décrivaient le même problème par deux chemins. La version 4 séparait la simulation par image, ancienne règle 239, de la simulation par alignement de texte, ancienne règle 240. La version 5 les rassemble dans une règle unique et transverse.

### Ce que la règle interdit

Deux artifices, qui reviennent tous deux à remplacer la structure d’un tableau par son apparence :

- la mise sous forme d’image : capture d’écran ou scan d’un tableau bureautique collé dans la page ;
- la simulation par caractères : colonnes imitées avec des espaces insécables, des tabulations ou des caractères graphiques comme le pipe.

### Relier la règle à son impact

Pour une personne qui utilise un lecteur d’écran, une image de tableau se résume à son alternative : aucune cellule n’est reliée à son entête, et le détail des données reste hors de portée. Un tableau simulé par des espaces est lu linéairement, et les chiffres défilent détachés de ce qu’ils désignent. Opquast parle d’un contenu pratiquement dénué de sens pour la synthèse vocale.

Les données deviennent aussi inexploitables par les moteurs de recherche et les outils d’indexation, et impossibles à copier ou à réutiliser. À l’affichage, enfin, une image de tableau se pixellise sur un petit écran, et un alignement par espaces se déforme dès que la largeur ou la taille de police change.

### Ce que garantit la règle 245

Un tableau réellement balisé. Chaque cellule reste reliée à son entête de ligne ou de colonne, les données restent lisibles, copiables et indexables, et le rendu s’adapte au terminal.

Une alternative textuelle ne sauve pas une image de tableau : la rédiger reviendrait à écrire le tableau HTML, autant le publier directement. Pour un audit, la fusion fait un contrôle de moins à tenir, au même niveau d’exigence.

### Mise en œuvre

Utiliser systématiquement la structure HTML appropriée :

- `<table>` pour le tableau lui-même ;
- `<tr>` pour chaque ligne ;
- `<td>` pour les cellules de données ;
- `<th>` pour les entêtes de ligne ou de colonne ;
- `<caption>` pour le titre du tableau.

**Mémo oral :** Une seule règle, la structure reste due.

---

# Slide 13 - Ce qui se reformule : l’exemple de la 112

Image publiée : `assets/slides/slide-13-ce-qui-se-reformule-exemple-112.png`  
Empreinte PNG : `8b8632ad2d4bc04a3abb9a29ecd24c5c0322298be6e62546e631b7cfb316977e`

## Transcription

### Lecture du visuel

La slide illustre une reformulation. À gauche, le libellé de la version 4 parle du site
qui propose un moyen de contacter le responsable des réclamations. À droite, le libellé
de la version 5, la règle 112, parle d’un moyen de contacter le service après-vente ou le
support. Une flèche marquée « Reformulation » relie les deux. Le bandeau final rappelle
qu’un nouveau libellé ne fait pas une nouvelle règle.

### Contrôle des libellés

Les deux libellés affichés sont conformes aux libellés officiels, contrôlés le
17 septembre 2026 contre l’API Opquast : règle 107 en version `assurance-qualite-web`,
règle 112 en version `qualite-numerique`.

### Message à retenir

**Nouveau libellé ≠ nouvelle règle.**

## Discours oral

Ici, rien n’entre ni ne sort : c’est la même exigence, exprimée autrement.

### Relier la règle à son impact

Un litige est toujours possible. Si aucun canal n’est indiqué, l’utilisateur cherche, écrit au mauvais interlocuteur ou renonce, et le service perd la trace de sollicitations qu’il aurait pu traiter.

### Ce que garantit la règle 112

Qu’il existe au moins un moyen d’atteindre le service après-vente ou le support, mentionné dans une page où on le cherche : accueil, mentions légales, à propos, aide ou conditions générales. Le contrôle porte sur la présence de ce moyen, pas sur sa nature ni sur la qualité de la réponse.

### Pourquoi la formulation a changé

Le libellé de la version 4 parlait du « site » et du « responsable des réclamations ». Le référentiel s’applique désormais à des services qui ne sont pas tous des sites web, et l’utilisateur cherche de l’aide avant de chercher un responsable.

**Mémo oral :** Même exigence, autre formulation.

---

# Slide 14 - Attention aux numéros

Image publiée : `assets/slides/slide-14-attention-aux-numeros.png`  
Empreinte PNG : `2a5731e577037cb104edbcbc5b4831a18e1096efcc04c327b6c1b836a441d621`

## Transcription

### Lecture du visuel

La slide met en garde contre l’usage du seul numéro de règle. Elle place côte à côte deux
cartes portant le même numéro, 235, séparées par un signe « différent de » : d’un côté un
résumé sur la détection des fils de syndication, de l’autre un résumé sur le balisage des
listes dans le code. Le visuel précise lui-même qu’il compare des libellés résumés, et non
les libellés officiels complets. Le bandeau final demande de suivre l’exigence et sa
version, pas seulement le numéro.

### Libellés officiels

Le visuel compare des libellés résumés. Les libellés officiels, contrôlés le 17 septembre
2026 contre l’API Opquast, sont les suivants :

- version 4, règle 235 : « Les fils de syndication sont détectables par les agents
  utilisateurs. »
- version 5, règle 235 : « Les éléments visuellement présentés sous forme de liste sont
  balisés de façon appropriée dans le code source. »

En version 4, le balisage des listes portait le numéro 228. C’est donc bien un même
numéro qui désigne deux exigences sans rapport selon la version du référentiel.

### Message à retenir

**Suivre l’exigence et sa version, pas seulement le numéro.**

## Discours oral

C’est le piège le plus concret de la migration. Quand des règles sortent et que d’autres entrent, la numérotation se réorganise.

### Relier le numéro à son impact

Un numéro seul ne dit rien de l’exigence. Une grille, un ticket, une consigne d’équipe ou un rapport livré à un client qui cite « la 235 » sans son libellé peut faire contrôler le balisage des listes là où la version 4 parlait des fils de syndication. Personne ne voit l’erreur : le numéro est juste, le contrôle est faux.

### Ce que garantit une migration correcte

Aucune règle ne couvre ce point : c’est une pratique. Elle consiste à transporter systématiquement le libellé et la version avec le numéro, dans tout document qui cite une exigence.

**Mémo oral :** Un numéro sans version ne veut rien dire.

---

# Slide 15 - Derrière V5 : du Web au numérique

Image publiée : `assets/slides/slide-15-derriere-v5-du-web-au-numerique.png`  
Empreinte PNG : `eec034372f6a01a41690d856b36ca1a0935c2456145356a6c70f674bf81fc04c`

## Transcription

### Lecture du visuel

La slide situe le mouvement de fond de la version 5. À gauche, la qualité web est
représentée par un site web. À droite, la qualité numérique réunit quatre contextes :
intranet, application mobile, application pour ordinateur et télévision connectée. Une
flèche légendée « Élargissement progressif » traverse la slide. Le bandeau final précise
que l’applicabilité reste à examiner selon le service.

### Point de vigilance

Les quatre contextes figurés sont des exemples d’élargissement, pas une liste officielle
et fermée des périmètres couverts par le référentiel.

### Message à retenir

**L’applicabilité reste à examiner selon le service.**

## Discours oral

Cette slide situe le mouvement de fond de la version 5. Opquast l’a formulé ainsi en annonçant la nouvelle version du parcours certifiant, en octobre 2025 : « nous évoluons de la notion de web vers la notion de numérique au sens applicatif du terme ».

### Relier l’élargissement à son impact

À la création d’Opquast, le site web était l’unité de travail. Les organisations pilotent aujourd’hui un parc de services : intranets, applications mobiles, applications pour ordinateur, bornes, télévision connectée.

Tant qu’un libellé dit « le site », il ne s’applique à aucun de ces contextes, et les équipes qui les font vivre n’ont pas de socle à opposer. Le travail de réécriture est mesurable : 40 libellés de la version 4 mentionnaient « le site », contre 6 en version 5. Les règles disent désormais « le service », ou ne nomment plus de support du tout.

### Ce qui pousse ce mouvement

La démarche ne repose plus seulement sur la bonne volonté des équipes. Opquast décrit une pression réglementaire qui s’accumule : accessibilité avec l’European Accessibility Act et le RGAA, données personnelles avec le RGPD, et une vague à anticiper avec l’IA Act et le RGESN.

Un référentiel qui ne parlerait que de sites web serait hors sujet face à des obligations qui visent des services.

### Ce qui ne change pas

Le socle méthodique. Le modèle VPTCS, visibilité, perception, technique, contenus et services, formulé par Elie Sloïm et Eric Gateau en 2001, reste la grille de lecture transversale des exigences.

Les besoins de l’utilisateur non plus ne changent pas : trouver l’information, avancer sans blocage, utiliser un service fiable. Ce sont les supports qui se multiplient, pas les attentes.

### Ce que cet élargissement ne garantit pas

Que toutes les règles s’appliquent partout. L’applicabilité s’examine service par service, et une règle non applicable reste non applicable : c’est un constat d’audit, pas un échec.

### Ce que cela change pour la certification

Le parcours certifiant porte désormais le nom « Mobiliser un référentiel qualité numérique ». Il n’évalue plus l’usage d’une checklist de règles, mais la capacité à mobiliser l’ensemble du référentiel, modèle, règles, contextes utilisateurs, fiches et glossaire, en conditions professionnelles.

**Mémo oral :** Le périmètre s’élargit, l’applicabilité s’examine.

---

# Slide 16 - Tags et applicabilité

Image publiée : `assets/slides/slide-16-tags-et-applicabilite.png`  
Empreinte PNG : `d218e4a92b865814bb5922422ec0db4eced555c182190d7404d2d36ce6e258ec`

## Transcription

### Lecture du visuel

La slide réunit deux compléments annoncés pour 2026. À gauche, l’évolution des tags : les
étiquettes Conception, Développement et Éditorial laissent place à Fonctionnel, Technique
et Contenus. À droite, l’applicabilité, présentée selon le type de service, avec quatre
exemples : site web, application mobile, service e-commerce et service métier. Le visuel
mentionne une annonce du 14 avril 2026. Le bandeau final indique que les usages du
référentiel sont en cours d’évolution.

### Source

La date du 14 avril 2026 est celle de la publication, par Opquast, de l’article
[Au programme : livre, tags et numérique](https://www.opquast.com/au-programme-livre-tags-et-numerique/),
consulté le 17 septembre 2026. Cet article annonce les deux évolutions présentées ici : le
remplacement des tags Conception, Développement et Éditorial par Fonctionnel, Technique et
Contenus, et un travail d’applicabilité des règles par type de service. Ces évolutions
portent sur les usages du référentiel et ne modifient pas les 245 règles présentées dans
cette série.

### Point de vigilance

Les quatre exemples illustrés ne reprennent pas les catégories publiées par Opquast.
L’article recense notamment les sites web et portails publics, les intranets et extranets,
les applications mobiles, les applications pour ordinateur, les bornes interactives, la
télévision connectée, les médias sociaux, le courriel et les jeux vidéo. Les mentions
« Service e-commerce » et « Service métier » portées par le visuel sont des exemples
d’illustration, pas des catégories du tableau d’applicabilité.

Opquast présente par ailleurs ce travail comme ouvert et appelle les retours : les
catégories et leurs volumes de règles applicables peuvent évoluer.

### Message à retenir

**Des usages du référentiel en cours d’évolution.**

## Discours oral

Cette slide ne parle plus du contenu des règles, mais de la façon de s’en servir.

### Relier les tags à leur impact

Classer par Conception, Développement et Éditorial, c’est ranger les règles par métier, donc par organisation. Dès que l’organisation diffère, le classement ne tombe plus juste et chaque équipe doit refaire le tri. Classer par Fonctionnel, Technique et Contenus, c’est ranger par nature de l’exigence, ce qui reste valable quelle que soit la répartition des rôles.

### Ce que ce complément apporte

L’applicabilité par type de service répond à la question laissée ouverte par la slide précédente : cette information a vocation à être portée par le référentiel lui-même plutôt que reconstruite par chaque équipe. Opquast présente ce travail comme ouvert et appelle les retours.

**Mémo oral :** Classer par nature d’exigence, pas par métier.

---

# Slide 17 - Conclusion : comment évolue un référentiel ?

Image publiée : `assets/slides/slide-17-conclusion-evolution-referentiel.png`  
Empreinte PNG : `d348038d5849bf74c1ad5e9369098c81429168517eaade2af88fec339e8348b9`

## Transcription

### Lecture du visuel

La slide de conclusion reprend les quatre opérations d’évolution du référentiel, chacune
avec son critère : ajouter quand une exigence utile doit entrer dans le socle, retirer
quand la valeur ajoutée d’une règle diminue, fusionner quand des exigences proches peuvent
être regroupées, reformuler quand l’expression doit être clarifiée et adaptée. Les quatre
cartes convergent vers l’encadré « 240 → 245 », qui ferme la boucle ouverte par la
première slide. Le bandeau final demande de revoir les exigences et les contrôles, pas
seulement les numéros.

### Message à retenir

**Revoir les exigences et les contrôles, pas seulement les numéros.**

## Discours oral

Nous revenons au point de départ. L’écart entre 240 et 245 tient en quatre opérations, et chacune répond à un critère différent.

### Relier les opérations à leur impact

Une mise à jour qui se contente de changer le total affiché laisse en place des contrôles périmés et n’ajoute pas ceux qui manquent. Ce sont les utilisateurs du service audité qui en portent les conséquences, sans que le rapport ne le montre jamais.

### Ce que garantit cette méthode

Une reprise exigence par exigence plutôt qu’un report de numéros : repérer les huit règles qui entrent, les deux qui sortent, la fusion et les reformulations, puis mettre à jour les contrôles correspondants en transportant chaque libellé avec sa version.

**Mémo oral :** Revoir les exigences, pas le compteur.

---
