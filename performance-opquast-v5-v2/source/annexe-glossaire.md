# Annexe glossaire - Serveur et performances

## Statut et source

- Statut : `GENERE_ET_INTEGRE`.
- Format prévu : 5 slides autonomes d’annexe.
- Pagination visuelle : `ANNEXE GLOSSAIRE · N / 5`, indépendante des 35 slides du parcours principal.
- Source canonique : glossaire Opquast, catégorie « Serveur et performances », édition du 17 juin 2026.
- URL : https://training.opquast.com/digital-quality/glossaire/glossaire-serveur-et-performances/
- Fidélité : les définitions ci-dessous sont reproduites exactement. Les marqueurs Markdown de mise en gras sont les seuls ajouts.
- Génération : les quatre premières fiches ont été validées avant la génération des cinq images.

## Slide 36 - Qui échange avec le serveur ?

**Rôle** : ouverture de l’annexe et identification des acteurs, protocoles et objets échangés.

**Composition proposée** : un navigateur et un robot envoient des requêtes à un serveur. Le serveur leur retourne des ressources. Une ressource tierce arrive depuis un second domaine. Les échanges HTTP et HTTPS sont distingués sans suggérer qu’ils produisent des performances différentes.

**Liste blanche des textes visibles** :

1. Qui échange avec le serveur ?
2. Agent utilisateur
3. Client web
4. Serveur
5. HTTP
6. HTTPS
7. Ressource
8. Ressource tierce
9. QUALITÉ WEB
10. EXPÉRIENCES DURABLES
11. Opquast
12. DES SITES MEILLEURS POUR TOUS
13. RÈGLES OPQUAST · PERFORMANCE
14. ANNEXE GLOSSAIRE · 1 / 5

**Message** : le serveur répond à plusieurs types de clients et leur transmet des ressources selon le protocole utilisé.

### Notes orales - définitions exactes du glossaire

- **Agent utilisateur** : Un agent utilisateur (« user agent ») désigne, dans le domaine du web, tout **outil ou logiciel qui accède au site** et en consulte ou en exploite les pages ou les services. Les principaux agents utilisateurs sont les **navigateurs web** utilisés par les internautes, les **aides techniques d’accessibilité** ainsi que les **robots logiciels** utilisés par les moteurs de recherche. Un agent utilisateur a pour fonction d’accéder à une page web et de restituer celle-ci soit à un utilisateur, soit pour un traitement automatisé de son contenu.
- **Client web** : Un client web, ou client HTTP, est un logiciel, le plus souvent installé sur le poste de l’utilisateur, qui **envoie des demandes à un serveur web via des requêtes HTTP**, et qui exploite les résultats reçus en retour, en particulier pour les afficher. Les navigateurs web sont les clients web les plus répandus. Mais c’est aussi le cas des robots d’indexation des moteurs de recherche ou des aspirateurs de site permettant à un utilisateur de copier tout ou une partie d’un site. Des bibliothèques logicielles gérant les requêtes HTTP permettent de créer des clients web répondant à des besoins plus spécifiques.
- **Serveur** : Un serveur web est un logiciel qui **reçoit des requêtes et transmet des ressources à des clients** (navigateurs web, autre serveur, etc.). Par extension, le matériel hébergeant ces logiciels est également appelé serveur.
- **HTTP** : HTTP (« HyperText Transfer Protocol ») est un **protocole de communication** qui permet aux navigateurs (et autres clients web) et aux serveurs d’échanger des données. Il définit la manière dont les requêtes (demandes de pages, images, fichiers, etc.) et les réponses (contenu envoyé par le serveur) sont structurées et transmises. HTTP est à la base du fonctionnement du web, mais ses échanges ne sont pas chiffrés : toute personne interceptant le trafic peut potentiellement lire ou modifier les données.

  HTTPS(« HyperText Transfer Protocol Secure ») est la version sécurisée de HTTP, qui assure la **confidentialité des données échangées**, leur **intégrité** et leur **authenticité**.
- **HTTPS** : HTTPS(« HyperText Transfer Protocol Secure ») est la version sécurisée du protocole HTTP qui permet aux navigateurs (et autres clients web) et aux serveurs d’échanger des données. Elle repose sur un **chiffrement via TLS** (Transport Layer Security, successeur de SSL). Cela assure la confidentialité des données échangées, leur intégrité (elles ne peuvent pas être altérées lors du transfert sans que ce soit détecté) et leur authenticité (l’identité du site est vérifiée par un certificat numérique délivré par une autorité de certification).
- **Ressource** : Une page web affichée par un navigateur est composée à partir de différentes ressources, chacune étant **téléchargée séparément** : la source HTML de la page, un ou plusieurs fichiers CSS, un ou plusieurs fichiers JavaScript, un ou plusieurs fichiers image, etc.
- **Ressource tierce** : Ressource utilisée dans une page web (image, script, police de caractères, etc.), mais **hébergée par un tiers** et liée à la page par un appel dans le code source.

**Contraintes critiques** : ne pas représenter HTTP comme plus rapide que HTTPS ; ne pas réduire « agent utilisateur » au seul navigateur ; ne pas placer la ressource tierce dans le serveur principal.

## Slide 37 - Réduire ce qui circule

**Rôle** : slide d’éclairage sur les mécanismes qui agissent sur le fichier, le transport et les consultations suivantes.

**Composition proposée** : une ressource textuelle traverse une chaîne en trois moments. Elle est minifiée, négociée et compressée pendant le transfert, puis conservée dans le cache du navigateur. Un fichier externalisé illustre sa réutilisation entre plusieurs pages. Les en-têtes HTTP accompagnent le transfert.

**Liste blanche des textes visibles** :

1. Réduire ce qui circule
2. Minification
3. Contenu compressé
4. Négociation de contenu
5. En-tête HTTP
6. Cache navigateur
7. Externalisation
8. Fichier
9. Transport
10. Réutilisation
11. QUALITÉ WEB
12. EXPÉRIENCES DURABLES
13. Opquast
14. DES SITES MEILLEURS POUR TOUS
15. RÈGLES OPQUAST · PERFORMANCE
16. ANNEXE GLOSSAIRE · 2 / 5

**Message** : minifier, compresser, mettre en cache et externaliser répondent à des moments différents.

### Notes orales - définitions exactes du glossaire

- **Contenu compressé** : Ressources de type texte (fichiers HTML, CSS, JavaScript, XML) qui sont **compressées par le serveur avant envoi au client** afin d’accélérer le téléchargement et de réduire les coûts de bande passante. La négociation de contenus compressés s’effectue en HTTP/1.1 via les entêtes Accept-Encoding et Content-Encoding. La compression ne dispense pas de minifier les fichiers qui peuvent l’être (CSS, JavaScript) afin d’améliorer davantage les performances.
- **Négociation de contenu** : Échange d’informations, entre le client et le serveur via HTTP, qui permet de **déterminer côté serveur quel contenu répond aux contraintes exprimées par l’utilisateur** dans le paramétrage de son navigateur. Il peut s’agir par exemple de la version linguistique de la page, ou encore des types et formats de ressources supportées par le navigateur.
- **En-tête HTTP** : Un entête HTTP est une **information transmise entre un client (souvent un navigateur) et un serveur** lors d’une requête ou d’une réponse dans le cadre du protocole HTTP. Ces entêtes fournissent des métadonnées essentielles sur la ressource demandée ou envoyée, telles que son type, son statut (par exemple erreurs 404 ou 403), les cookies associés, les paramètres de cache navigateur ou encore des directives de sécurité. Ils jouent ainsi un rôle central dans le bon fonctionnement des échanges web, en influençant à la fois l’expérience utilisateur, la performance et la protection des données.
- **Minification** : Réduction de la taille des fichiers texte CSS et JavaScript, obtenue par la **suppression des commentaires, des espaces non nécessaires et la réduction a minima de la syntaxe**, ne laissant que le code strictement nécessaire au moteur de rendu du navigateur. La minification réduit l’utilisation de bande passante et améliore les performances de téléchargement.
- **Cache navigateur** : Fonctionnalité des navigateurs web leur permettant de **conserver localement l’enregistrement d’une ressource** d’une page web (image, fichier CSS, fichier JavaScript, etc.) afin de ne pas avoir à la télécharger de nouveau quand la page est visitée une seconde fois, ou que la même ressource est présente dans une autre page. La durée d’utilisation d’une ressource en cache dépend de métadonnées associées à celle-ci via des entêtes HTTP envoyés par le serveur au navigateur.
- **Externalisation** : Gestion de composants d’une page web (mise en forme CSS, JavaScript) qui **ne les inclue pas dans la source HTML** de celle-ci, mais qui les place dans des fichiers externes (feuille de style, fichier JavaScript) appelés par la page. L’externalisation d’une feuille de style CSS ou d’un fichier de script permet en particulier de ne les télécharger qu’une seule fois au cours de la visite de plusieurs pages du même site, et d’améliorer les performances de rendu grâce à leur mise en cache par le navigateur.

**Contraintes critiques** : ne pas confondre minification et compression ; ne pas présenter le cache comme une suppression systématique de tout échange ; relier les en-têtes HTTP au transport sans les représenter comme le contenu lui-même.

## Slide 38 - De la configuration aux pages servies

**Rôle** : slide d’architecture reliant le logiciel serveur, sa configuration et les modèles de publication.

**Composition proposée** : un serveur Apache et son fichier .htaccess occupent la zone de configuration. La racine du site conduit vers deux branches : site statique, directement servi depuis des fichiers, et site dynamique ou application web, relié à un CMS et une base de données.

**Liste blanche des textes visibles** :

1. De la configuration aux pages servies
2. Apache
3. .htaccess
4. Racine du site
5. Application web
6. CMS
7. Base de données
8. Site dynamique
9. Site statique
10. Configuration
11. Publication
12. QUALITÉ WEB
13. EXPÉRIENCES DURABLES
14. Opquast
15. DES SITES MEILLEURS POUR TOUS
16. RÈGLES OPQUAST · PERFORMANCE
17. ANNEXE GLOSSAIRE · 3 / 5

**Message** : la manière de configurer et de produire les pages détermine les ressources mobilisées côté serveur.

### Notes orales - définitions exactes du glossaire

- **Apache** : Logiciel libre et open source de **serveur web**, développé par la fondation Apache Software Foundation. Il permet d’héberger et de diffuser des sites ou des applications web sur Internet en répondant aux requêtes des navigateurs via le protocole HTTP ou HTTPS.
- **Htaccess** : Fichier de **configuration d’un serveur web Apache**, toujours nommé « .htaccess ». Il permet en particulier de définir les droits d’accès, les pages d’erreurs personnalisées et les redirections.
- **Racine du site** : Répertoire physique sur le serveur directement accessible à partir de l’URL du domaine. On y trouve notamment le fichier **robots.txt** et souvent le fichier **sitemap.xml**, tous deux essentiels pour l’indexation de contenus par les moteurs de recherche externes.
- **Application web** : Logiciel en ligne utilisable dans un **agent utilisateur** (navigateur), sans nécessiter d’installation sur le périphérique client (ordinateur, smartphone, etc). Les applications web couvrent un large champ d’activités, comportant notamment la bureautique (traitement de texte, tableur), la gestion de contenus, les applications de cartographie, les outils de partage et de réseau social, les webmails, les agendas, les outils de gestion et de retouche d’images, etc.
- **CMS** : Un CMS (« Système de gestion de contenu ») est une application permettant la **conception, la production et la mise à jour d’un site web ou d’un service en ligne**. Un CMS permet le travail collaboratif sur un document, la gestion de sa chaîne de publication (workflow) depuis sa création jusqu’à sa mise en ligne finale, ainsi que la gestion de différents statuts, rôles et permissions pour les éditeurs de contenu.
- **Base de données** : Une base de données est une **collection structurée d’informations**, organisées afin d’être traitées par des moyens informatiques. Le système de gestion de base de données est une suite de programmes qui gère la collecte, le stockage, le retraitement et l’utilisation de données qui y sont stockées.

  Un site web dynamique s’appuie généralement sur une base de données pour stocker et afficher ses contenus. Les CMS (WordPress, Drupal, Prestashop, etc.) utilisent presque toujours une base pour gérer textes, utilisateurs et médias. À l’inverse, un site statique (HTML CSS JavaScript sans base, utilisant par exemple des générateurs comme Jekyll, Hugo ou Eleventy) affiche son contenu directement depuis les fichiers hébergés sur le serveur.
- **Site dynamique** : Par opposition aux sites statiques, les pages des sites dynamiques sont en tout ou partie **générées à la volée à partir des contenus stockés dans une base de données** et peuvent être adaptées en fonction des caractéristiques de la demande (heure, adresse IP de l’ordinateur du demandeur, formulaire rempli par le demandeur, etc.) qui ne sont connues qu’au moment de sa consultation.
- **Site statique** : Site dont les pages sont générées manuellement ou à l’aide d’un générateur de sites statiques pour produire des **pages complètes affichées telles qu’elle par le serveur à l’agent utilisateur**. Les sites ou pages statiques demandent moins de ressources serveur et sont plus légers que ceux ayant recours à un système de gestion de contenu avec base de données. Ils sont de plus en plus utilisés pour les blogs, les portfolios, les sites vitrine, etc. Les pages peuvent être composées à partir de simples fichiers HTML, Markdown, etc., et utilisent également plusieurs langages de templating complétés par CSS et JavaScript si besoin.

**Contraintes critiques** : ne pas présenter Apache comme le seul serveur possible ; associer .htaccess uniquement à Apache ; ne pas affirmer qu’un site dynamique utilise toujours une base de données ; ne pas représenter un site statique comme dépourvu de CSS ou de JavaScript.

## Slide 39 - Répondre sans créer d’impasse

**Rôle** : slide de distinction entre statuts d’erreur, pages personnalisées et mécanismes de redirection.

**Composition proposée** : une requête se divise en trois réponses. Une ressource absente produit 404, une ressource interdite produit 403 et une ressource déplacée produit une redirection serveur. Une page d’erreur personnalisée permet de poursuivre la navigation. Une redirection côté client est isolée comme mécanisme différent et potentiellement perturbant.

**Liste blanche des textes visibles** :

1. Répondre sans créer d’impasse
2. Erreur 403
3. Accès refusé
4. Erreur 404
5. Ressource absente
6. Page d’erreur personnalisée
7. Redirection serveur
8. Redirection côté client
9. Reprendre la navigation
10. QUALITÉ WEB
11. EXPÉRIENCES DURABLES
12. Opquast
13. DES SITES MEILLEURS POUR TOUS
14. RÈGLES OPQUAST · PERFORMANCE
15. ANNEXE GLOSSAIRE · 4 / 5

**Message** : un statut, une page d’erreur et une redirection répondent à des situations différentes.

### Notes orales - définitions exactes du glossaire

- **Erreur 403** : Code d’erreur envoyé par un serveur, via un entête HTTP. Une erreur 403 « Accès non autorisé » signifie que le serveur a bien reçu et compris la requête, mais qu’il **refuse d’y répondre**. Elle survient généralement lorsqu’un utilisateur tente d’accéder à une ressource (page, image, etc.) sans disposer des droits nécessaires, par exemple sans être connecté à son compte.

  Chaque logiciel serveur gérant les contenus (logiciel serveur du type Apache ou CMS) dispose d’une page 403 par défaut. Celle-ci nécessite le plus souvent d’être adaptée pour éviter le risque de confronter l’utilisateur à un message d’erreur peu compréhensible ou à une page en impasse. L’erreur 403 diffère d’une erreur 404, où la ressource n’existe pas.
- **Erreur 404** : Code d’erreur envoyé par un serveur, via un entête HTTP. Une erreur 404 indique que la **ressource demandée (page, image, fichier de style ou de script, etc.) n’existe pas ou n’est plus disponible**. Elle résulte souvent d’un lien brisé ou d’une URL incorrecte. Contrairement à l’erreur 403, le problème ne vient pas des autorisations, mais de l’absence de la ressource sur le serveur.

  Chaque logiciel serveur gérant les contenus (logiciel serveur du type Apache ou CMS) dispose d’une page 404 par défaut. Celle-ci nécessite le plus souvent d’être adaptée pour éviter le risque de confronter l’utilisateur à un message d’erreur peu compréhensible ou à une page en impasse. L’erreur 404 diffère d’une erreur 403, où la ressource existe, mais où son accès n’est pas autorisé.
- **Page d'erreur personnalisée** : Page affichée à la suite, en particulier, d’une erreur serveur 403 ou 404, avec un contenu et une présentation adaptés pour **parer les risques que l’utilisateur soit dérouté ou bloqué dans sa navigation** sur le site. La page d’erreur personnalisée remplace la page par défaut minimale, qui est automatiquement envoyée au navigateur par le serveur web.
- **Redirection serveur** : À la suite, par exemple, d’un déplacement de page ou de ressource dans l’architecture des contenus, le serveur adresse la nouvelle page ou la nouvelle ressource directement à l’utilisateur, de manière totalement transparente pour lui, même s’il a saisi l’ancienne URL. Les redirections côté serveur **évitent le risque de dérouter l’utilisateur**, contrairement aux redirections côté client. Leur bonne gestion est également nécessaire pour parer des risques en matière de référencement.

  Un code d’entête HTTP spécifique est prévu à cet effet (301 pour une redirection permanente, 302 pour une redirection temporaire). Il est exploité notamment par les robots d’indexation.
- **Rafraîchissement et redirection automatiques côté client** : Un rafraîchissement automatique côté client est un procédé qui **force le rechargement de la totalité de la page web à intervalle régulier**. Par exemple, pour actualiser des contenus publicitaires ou une zone d’actualités. Une redirection automatique côté client est un procédé qui, après chargement d’une page, force le chargement d’une autre page à la place de celle-ci, immédiatement ou après un délai permettant de consulter (en théorie) un message d’explication.

  Ces deux procédés ont le défaut majeur d’**interrompre de manière imprévue ou trop rapide la consultation de la page en cours par l’utilisateur**, particulièrement pour les utilisateurs de lecteurs d’écran, ou encore pour les utilisateurs en mobilité dont la connexion peut être instable.

**Contraintes critiques** : distinguer le statut HTTP de la page visible ; ne pas confondre 403 et 404 ; ne pas présenter une redirection côté client comme équivalente à une redirection serveur.

## Slide 40 - Relier les termes sans les confondre

**Rôle** : synthèse de l’annexe.

**Composition proposée** : quatre zones reliées dans l’ordre de consultation : acteurs et échanges, fichiers et transfert, configuration et publication, réponses et continuité. Un utilisateur reste au centre de la chaîne. Aucun terme nouveau n’est ajouté.

**Liste blanche des textes visibles** :

1. Relier les termes sans les confondre
2. Acteurs et échanges
3. Fichiers et transfert
4. Configuration et publication
5. Réponses et continuité
6. Comprendre le rôle de chaque terme
7. QUALITÉ WEB
8. EXPÉRIENCES DURABLES
9. Opquast
10. DES SITES MEILLEURS POUR TOUS
11. RÈGLES OPQUAST · PERFORMANCE
12. ANNEXE GLOSSAIRE · 5 / 5

**Message** : les termes décrivent des acteurs, des mécanismes et des réponses complémentaires, pas des synonymes.

### Notes orales

- Les **acteurs et échanges** distinguent l’agent utilisateur, le client web, le serveur, les protocoles et les ressources.
- Les **fichiers et transferts** distinguent la minification, la compression, la négociation de contenu, les en-têtes HTTP, le cache navigateur et l’externalisation.
- La **configuration et la publication** relient Apache, .htaccess, la racine du site, les applications web, les CMS, les bases de données et les sites statiques ou dynamiques.
- Les **réponses et la continuité** distinguent les erreurs 403 et 404, les pages d’erreur personnalisées et les redirections côté serveur ou côté client.
- Le glossaire fournit un vocabulaire commun ; il ne transforme pas tous ces termes en critères de performance ni en règles appartenant au même objectif.
- **À retenir** : nommer précisément le mécanisme évite d’attribuer au serveur, au navigateur ou au protocole une garantie qu’il ne fournit pas.

**Contraintes critiques** : ne pas présenter les quatre familles comme une classification officielle du glossaire ; ne pas ajouter de terme absent des quatre slides précédentes ; préserver la distinction entre rubrique Opquast et choix pédagogique.
