# Storyboard - Sécurité selon Opquast V5 - version 3

## Statut et périmètre

- Statut : `BROUILLON_A_VALIDER_AVANT_GENERATION`.
- Livrable actuel : storyboard source uniquement.
- Variante cible : `securite-opquast-v5-v3`.
- Durée cible : 60 minutes.
- Public : équipe numérique mixte d'une administration, avec des profils produit, éditoriaux, développement, exploitation, sécurité et support.
- Objectif principal : comprendre le risque utilisateur associé à chaque règle de la rubrique Sécurité et savoir réaliser un premier contrôle reproductible.
- Périmètre : les 21 règles de la rubrique Sécurité, numéros 197 à 217.
- Limite : ce parcours présente un socle de prévention Opquast. Il ne remplace ni une analyse de risques, ni un audit de sécurité complet, ni un test d'intrusion, ni les référentiels spécialisés de l'ANSSI ou de l'OWASP.
- Référentiel vérifié : API Opquast `qualite-numerique`, consultation du 17 octobre 2026.
- Variante publiée préservée : `securite-opquast-v5-v2` n'est pas modifiée.

## Décision pédagogique

Deux organisations ont été comparées :

- une organisation par couches techniques, plus compacte mais difficile à suivre pour un public mixte ;
- une organisation par chaîne de confiance utilisateur, qui relie chaque risque à un mécanisme, un contrôle, une limite et un propriétaire.

L'axe retenu est la chaîne de confiance utilisateur. Les couches techniques restent visibles grâce aux propriétaires et aux outils de contrôle.

La séquence suit cinq chapitres :

1. Arriver sur le bon service par un canal sûr.
2. Garder la maîtrise du compte.
3. Dire au navigateur ce qu'il peut accepter.
4. Révéler le strict nécessaire.
5. Prolonger la confiance au-delà de la page.

## Idée centrale à faire comprendre

Les règles de sécurité Opquast ne promettent pas une sécurité absolue. Elles rendent visibles et contrôlables des précautions élémentaires qui protègent l'utilisateur pendant tout son parcours : rejoindre le service, gérer son compte, charger des contenus, consulter le serveur, réaliser une transaction et recevoir un courriel.

La phrase de conclusion est :

> Protéger le parcours. Limiter l'exposition. Vérifier les preuves.

## Question d'ouverture

> Un service entièrement en HTTPS est-il nécessairement sûr pour l'utilisateur ?

Réponse attendue après la séquence : non. HTTPS protège le transport, mais ne prouve ni la légitimité complète du service, ni la sécurité du compte, ni l'innocuité des ressources chargées, ni l'authenticité des courriels.

## Retours de la passe connu-inconnu intégrés

| Trou à éviter | Réponse dans le storyboard |
|---|---|
| Confondre socle Opquast et audit cyber complet | Frontière explicite en slide 03 et rappel en slide 29 |
| Décrire des mécanismes sans partir du préjudice | Un risque utilisateur ouvre chacun des cinq chapitres |
| Présenter des règles voisines comme équivalentes | Slides de comparaison 07, 11, 18, 19, 23 et 25 |
| Ne pas savoir qui doit agir | Carte des responsabilités en slide 05 et propriétaire indiqué sur chaque contrôle |
| Confondre présence, validité et efficacité | Limite locale après chaque contrôle et synthèse en slide 29 |

## Patron commun des chapitres

Chaque chapitre applique la même progression :

1. Risque concret pour l'utilisateur.
2. Règles concernées.
3. Mécanisme attendu.
4. Contrôle réalisable.
5. Limite de ce contrôle.

Le vocabulaire de verdict reste stable :

- `Présent` : le mécanisme est observable.
- `Valide` : sa valeur ou son fonctionnement répond au contrôle Opquast.
- `Non conforme` : le mécanisme manque ou échoue.
- `Indéterminé` : la preuve disponible ne permet pas de conclure.

La seule présence d'un entête ne suffit pas toujours à prouver son efficacité.

## Grammaire visuelle Opquast à reprendre

La V3 abandonne l'identité bleu nuit de la V2 et reprend la grammaire claire de la série `navigation-opquast-v5-360`.

- Canevas : 1672 x 941 pixels, ratio 16:9.
- Fond : blanc ou blanc cassé, avec formes organiques très pâles uniquement si elles structurent la lecture.
- Titres : bleu marine, très lisibles, une seule idée par slide.
- Accents : bleu pour la question, corail pour le risque, vert pour le contrôle réussi, orange pour la limite ou le point de vigilance.
- Illustrations : scènes simples, navigateurs, formulaires, enveloppes, serveurs et flux. Aucun cadenas décoratif dominant, aucun pirate caricatural.
- Bandeau supérieur gauche : `QUALITÉ NUMÉRIQUE - OPQUAST V5`.
- Repère supérieur droit : chapitre actif ou numéro de règle dans une pastille sobre.
- Pied de page gauche : `Opquast - présentation Miweb`, en texte simple et jamais sous forme de logo.
- Pied de page droit : pagination exacte `XX / 30`.
- Cartouches récurrents : `RISQUE`, `MÉCANISME`, `CONTRÔLE`, `LIMITE`.
- Aucun faux logo Opquast, aucun texte parasite, aucune photographie et aucune décoration sans fonction informative.

Les textes visibles ci-dessous constituent une liste blanche. Aucun autre texte métier ne doit apparaître dans les images générées.

## Carte des responsabilités

Les propriétaires ci-dessous sont des rôles opérationnels proposés pour la formation. Ils ne constituent pas une classification officielle Opquast.

| Propriétaire principal | Règles principalement suivies | Contribution attendue |
|---|---|---|
| Exploitation et infrastructure | 197, 198, 199, 200, 209, 213 | Configurer le transport, les certificats et le serveur |
| Produit et fonctionnel | 201, 202, 203, 204, 215, 216 | Préserver la maîtrise du compte et les solutions de repli |
| Développement front et back | 200, 205, 206, 207, 210, 211, 212, 214 | Produire les bons entêtes, contrôler les ressources et les parcours |
| Éditorial et support | 208 | Donner une information compréhensible et retrouvable |
| Messagerie et DNS | 217 | Authentifier le domaine d'envoi et surveiller les résultats |

La responsabilité finale reste collective. Une règle peut nécessiter plusieurs métiers même si un propriétaire principal est indiqué.

## Déroulé minuté

| Partie | Slides | Durée |
|---|---:|---:|
| Ouverture, périmètre et responsabilités | 01 à 05 | 9 min |
| Chapitre A - Canal et identité du site | 06 à 09 | 9 min |
| Chapitre B - Maîtrise du compte | 10 à 16 | 13 min |
| Chapitre C - Instructions données au navigateur | 17 à 24 | 17 min |
| Chapitre D - Exposition minimale du serveur | 25 à 26 | 4 min |
| Chapitre E - Transaction et messagerie | 27 à 28 | 5 min |
| Limites et conclusion | 29 à 30 | 3 min |

## Storyboard détaillé

### Slide 01 - Un service en HTTPS est-il nécessairement sûr ?

- Rôle : question d'ouverture et prédiction avant la réponse.
- Règles : 197 à 217.
- Idée : HTTPS n'est qu'une pièce de la chaîne de confiance.
- Composition : au centre, une page avec HTTPS ; autour, quatre questions encore ouvertes sur le compte, les scripts, le serveur et le courriel.
- Textes visibles :
  - `Sécurité selon Opquast V5`
  - `Un service entièrement en HTTPS est-il nécessairement sûr ?`
  - `Votez : oui ou non`
  - `RÈGLES 197 À 217`
- Oral : recueillir une réponse rapide sans la corriger immédiatement. Annoncer que la réponse sera reconstruite par preuves successives.
- Transition : commencer par définir ce que cette séquence doit rendre possible.

### Slide 02 - Comprendre le risque, savoir contrôler

- Rôle : annoncer le contrat de la séquence.
- Règles : 197 à 217.
- Idée : chaque règle doit devenir un risque compris et un contrôle réalisable.
- Composition : une ligne en cinq étapes, de la personne au verdict.
- Textes visibles :
  - `Comprendre le risque`
  - `Identifier la règle`
  - `Voir le mécanisme`
  - `Réaliser le contrôle`
  - `Nommer la limite`
- Oral : préciser que les contrôles sont distribués entre plusieurs métiers de l'administration.
- Transition : avant de contrôler, fixer la frontière du socle.

### Slide 03 - Un socle de prévention, pas un audit cyber complet

- Rôle : borner la promesse.
- Règles : 197 à 217.
- Idée : Opquast aide à repérer des précautions fondamentales sans garantir la sécurité globale du système.
- Composition : trois anneaux emboîtés, `Socle Opquast`, `Pratiques de production`, `Expertise cyber spécialisée`.
- Textes visibles :
  - `SOCLE OPQUAST`
  - `Précautions fondamentales observables`
  - `PRATIQUES DE PRODUCTION`
  - `Organisation, supervision, tests`
  - `EXPERTISE CYBER`
  - `Analyse de risques, audit approfondi, test d'intrusion`
- Limite orale : une conformité à ces 21 règles ne vaut pas homologation de sécurité.
- Transition : le socle suit toute une chaîne de confiance.

### Slide 04 - Cinq chapitres pour suivre la chaîne de confiance

- Rôle : carte du parcours.
- Règles : 197 à 217.
- Idée : les 21 règles s'organisent selon cinq moments vécus par l'utilisateur.
- Composition : frise continue allant d'un navigateur à un courriel.
- Textes visibles :
  - `A - Rejoindre le bon service`
  - `B - Garder la maîtrise du compte`
  - `C - Contrôler ce que le navigateur accepte`
  - `D - Révéler le strict nécessaire`
  - `E - Prolonger la confiance hors de la page`
- Transition : cette chaîne n'a pas un propriétaire unique.

### Slide 05 - La sécurité est une responsabilité distribuée

- Rôle : carte des responsabilités.
- Règles : 197 à 217.
- Idée : les contrôles sont collectifs, même lorsqu'un métier en porte l'action principale.
- Composition : cinq colonnes reliées à un même parcours utilisateur.
- Textes visibles :
  - `Infrastructure`
  - `Produit et fonctionnel`
  - `Développement`
  - `Éditorial et support`
  - `Messagerie et DNS`
  - `Un parcours, plusieurs propriétaires`
- Limite orale : les affectations montrées sont une proposition de gouvernance, pas une taxonomie officielle Opquast.
- Transition : la première responsabilité consiste à établir un canal sûr sans masquer le lieu où l'utilisateur se trouve.

### Slide 06 - Chapitre A : rejoindre le bon service par un canal sûr

- Rôle : ouvrir le premier risque utilisateur.
- Règles : 197, 198, 199, 200 et 216.
- Risque : les échanges peuvent être interceptés ou l'utilisateur peut croire parler au mauvais service.
- Composition : une personne suit un canal jusqu'à un domaine visible ; cinq jalons distincts longent le trajet.
- Textes visibles :
  - `A - CANAL ET IDENTITÉ DU SITE`
  - `Le canal peut être protégé sans que tout le parcours soit sûr.`
  - `197 · 198 · 199 · 200 · 216`
- Propriétaires : infrastructure, développement, produit.
- Transition : cinq règles voisines répondent à cinq questions différentes.

### Slide 07 - HTTPS : cinq questions, cinq preuves

- Rôle : faire distinguer les règles voisines avant leur contrôle.
- Règles : 197, 198, 199, 200 et 216.
- Idée : ces règles se ressemblent, mais ne sont pas interchangeables.
- Composition : cinq cartes alignées, chacune avec une question et une preuve.
- Textes visibles :
  - `197 - Toutes les pages passent-elles par HTTPS ?`
  - `198 - Le certificat est-il signé et valide ?`
  - `199 - Le navigateur doit-il rester en HTTPS ?`
  - `200 - Toutes les ressources passent-elles aussi par HTTPS ?`
  - `216 - L'utilisateur voit-il toujours l'adresse ?`
- Interaction : demander quelle règle manque si la page est en HTTPS mais charge un script en HTTP.
- Transition : les quatre premières preuves se contrôlent dans le navigateur et les échanges réseau.

### Slide 08 - Contrôler le canal sans conclure trop vite

- Rôle : montrer le premier contrôle complet.
- Règles : 197, 198, 199 et 200.
- Mécanisme : HTTPS, certificat valide, entête `Strict-Transport-Security`, absence de contenu mixte.
- Composition : capture stylisée des outils réseau avec quatre repères numérotés.
- Textes visibles :
  - `CONTRÔLE`
  - `197 - Pages et ressources en HTTPS`
  - `198 - Certificat signé et valide`
  - `199 - Strict-Transport-Security avec max-age`
  - `200 - Aucune ressource chargée en HTTP`
  - `LIMITE - Une page ne représente pas tout le service`
- Démonstration : inspecter plusieurs types de pages et leurs ressources, puis le certificat et l'entête HSTS.
- Propriétaires : infrastructure et développement.
- Transition : même avec un canal conforme, l'utilisateur doit encore voir où il se trouve.

### Slide 09 - La barre d'adresse reste une preuve extérieure à la page

- Rôle : traiter la règle 216 et fermer le chapitre.
- Règle : 216.
- Risque : le graphisme d'une page peut être imité et masquer une usurpation.
- Mécanisme : la barre d'adresse reste visible dans chaque fenêtre ouverte.
- Composition : deux pages visuellement identiques, départagées par leurs domaines visibles.
- Textes visibles :
  - `RÈGLE 216`
  - `Dans la page, le graphisme peut être copié.`
  - `Dans la barre d'adresse, je vérifie où je suis.`
  - `CONTRÔLE - Ouvrir chaque fenêtre et vérifier la barre d'adresse`
  - `LIMITE - Une adresse visible n'atteste pas à elle seule la légitimité du service`
- Propriétaire : produit et fonctionnel, avec développement.
- Transition : après l'identité du service vient la maîtrise du compte.

### Slide 10 - Chapitre B : garder la maîtrise du compte

- Rôle : ouvrir le deuxième risque utilisateur.
- Règles : 201, 202, 203, 204, 205 et 215.
- Risque : l'utilisateur perd l'accès, reçoit son secret en clair ou reste bloqué par un moyen de validation indisponible.
- Composition : un parcours de compte avec six points de décision.
- Textes visibles :
  - `B - MAÎTRISE DU COMPTE`
  - `Sécuriser le compte sans enfermer son titulaire.`
  - `201 · 202 · 203 · 204 · 205 · 215`
- Propriétaires : produit, fonctionnel, développement et support.
- Transition : les cinq premières règles suivent le cycle de vie du mot de passe.

### Slide 11 - Cinq moments du mot de passe, cinq exigences

- Rôle : montrer les ressemblances sans produire d'équivalence.
- Règles : 201 à 205.
- Idée : gérer, choisir, comprendre, réinitialiser et ne pas divulguer sont cinq capacités différentes.
- Composition : parcours linéaire en cinq étapes, sans boucle artificielle.
- Textes visibles :
  - `201 - Tout gérer en ligne`
  - `202 - Choisir ou changer`
  - `203 - Comprendre le degré de sécurisation`
  - `204 - Réinitialiser`
  - `205 - Ne jamais communiquer le mot de passe en clair`
- Transition : la disponibilité du processus et la maîtrise du secret ne doivent pas être confondues.

### Slide 12 - Gérer en ligne ne signifie pas choisir son mot de passe

- Rôle : distinguer 201 et 202.
- Règles : 201 et 202.
- Composition : deux parcours parallèles, l'un sur le canal de gestion, l'autre sur le choix du secret.
- Textes visibles :
  - `201 - Le processus complet est disponible en ligne`
  - `202 - L'utilisateur choisit ou change son mot de passe`
  - `Même compte, deux besoins distincts`
  - `CONTRÔLE - Tester création, changement et perte du mot de passe`
  - `LIMITE - Un seul profil de test ne couvre pas tous les parcours`
- Propriétaires : produit et développement.
- Transition : pouvoir choisir ne suffit pas si le risque associé au choix reste invisible.

### Slide 13 - Informer sur la robustesse sans confisquer le choix

- Rôle : traiter la règle 203.
- Règle : 203.
- Risque : l'utilisateur choisit un mot de passe faible sans en comprendre la conséquence.
- Mécanisme : retour avant la soumission définitive du formulaire.
- Composition : champ de mot de passe et indicateur progressif avec texte associé.
- Textes visibles :
  - `RÈGLE 203`
  - `Le retour intervient avant la validation.`
  - `CONTRÔLE - Saisir plusieurs mots de passe et observer le retour`
  - `LIMITE - Un indicateur visible ne prouve pas la qualité de l'algorithme`
- Propriétaires : produit et développement.
- Transition : le cas de l'oubli révèle une autre distinction essentielle.

### Slide 14 - Réinitialiser n'est pas restituer l'ancien secret

- Rôle : distinguer 204 et 205.
- Règles : 204 et 205.
- Risque : l'utilisateur reste bloqué ou reçoit un mot de passe exploitable dans un courriel.
- Composition : un lien temporaire mène à la création d'un nouveau mot de passe ; l'ancien secret n'apparaît jamais.
- Textes visibles :
  - `204 - Créer un nouveau mot de passe`
  - `205 - Ne jamais envoyer le mot de passe en clair`
  - `Réinitialiser ≠ restituer`
  - `CONTRÔLE - Suivre la procédure sans être connecté et examiner le courriel reçu`
  - `LIMITE - Ne jamais utiliser de compte réel ou de donnée personnelle dans la démonstration`
- Propriétaires : développement et support.
- Transition : la maîtrise du compte dépend aussi d'une solution de repli.

### Slide 15 - Deux moyens de validation ne signifient pas deux facteurs

- Rôle : corriger une confusion fréquente autour de la règle 215.
- Règle : 215.
- Risque : un utilisateur ne peut plus valider une opération faute du terminal ou du canal imposé.
- Mécanisme : au moins deux moyens au choix pour utiliser une authentification forte.
- Composition : une opération sécurisée se divise vers deux chemins de validation accessibles.
- Textes visibles :
  - `RÈGLE 215`
  - `Deux moyens au choix`
  - `Pas nécessairement deux facteurs simultanés`
  - `CONTRÔLE - Vérifier qu'une seconde voie est réellement proposée`
  - `LIMITE - Une voie théorique mais inutilisable ne constitue pas un secours`
- Propriétaires : produit, fonctionnel et développement.
- Transition : il faut maintenant tester le parcours comme un ensemble.

### Slide 16 - Atelier : tester un compte de bout en bout

- Rôle : récupération active et mise en pratique du chapitre.
- Règles : 201 à 205 et 215.
- Composition : checklist de parcours avec un espace de verdict.
- Textes visibles :
  - `Créer ou ouvrir un compte de test`
  - `Changer le mot de passe`
  - `Observer le retour de robustesse`
  - `Réinitialiser sans recevoir le secret`
  - `Essayer les deux moyens de validation`
  - `VERDICT - Présent, valide, non conforme ou indéterminé`
- Interaction : exercice en binôme de trois minutes sur un environnement de démonstration.
- Limite orale : le résultat porte sur les parcours testés, les rôles utilisés et l'état observé à cet instant.
- Transition : le compte peut être maîtrisé tandis que le navigateur reçoit encore de mauvaises instructions.

### Slide 17 - Chapitre C : dire au navigateur ce qu'il peut accepter

- Rôle : ouvrir le troisième risque utilisateur.
- Règles : 206, 207, 210, 211, 212 et 214.
- Risque : le navigateur interprète, charge, exécute ou encadre un contenu inattendu.
- Composition : navigateur central entouré de six consignes distinctes.
- Textes visibles :
  - `C - INSTRUCTIONS AU NAVIGATEUR`
  - `Déclarer la nature, les sources, les cadres et l'intégrité.`
  - `206 · 207 · 210 · 211 · 212 · 214`
- Propriétaire : développement, avec infrastructure.
- Transition : le premier couple indique ce qu'est une ressource et interdit de le deviner.

### Slide 18 - Type MIME : déclarer et ne pas deviner

- Rôle : distinguer les règles 206 et 207.
- Règles : 206 et 207.
- Composition : un fichier passe par deux contrôles successifs.
- Textes visibles :
  - `207 - Le serveur déclare le bon Content-Type`
  - `206 - Le navigateur reçoit X-Content-Type-Options: nosniff`
  - `Déclarer ≠ empêcher de deviner`
  - `CONTRÔLE - Inspecter les entêtes de plusieurs types de ressources`
  - `LIMITE - La présence de Content-Type ne prouve pas que sa valeur est correcte`
- Propriétaire : développement.
- Transition : trois règles suivantes peuvent mobiliser CSP, mais elles ne poursuivent pas le même but.

### Slide 19 - Une même famille d'entêtes, trois questions différentes

- Rôle : empêcher l'équivalence entre 210, 211 et 212.
- Règles : 210, 211 et 212.
- Composition : trois portes autour d'une page, chacune répondant à une question différente.
- Textes visibles :
  - `210 - Comment limiter l'exécution de scripts injectés ?`
  - `211 - Qui peut intégrer ma page dans un cadre ?`
  - `212 - D'où les contenus peuvent-ils être chargés ?`
  - `Une même politique peut porter plusieurs protections.`
- Interaction : faire associer `XSS`, `iframe` et `origine des contenus` aux trois numéros.
- Transition : la première protection doit reposer sur un mécanisme encore maintenu.

### Slide 20 - La règle 210 ne demande plus X-XSS-Protection

- Rôle : éclairage sur l'évolution de la règle.
- Règle : 210.
- Risque : un script injecté s'exécute dans le contexte de la page.
- Mécanisme : protection explicite et actuelle, par exemple une politique CSP active et applicable.
- Composition : une ancienne voie barrée et une politique actuelle inspectée dans les entêtes.
- Textes visibles :
  - `RÈGLE 210`
  - `Protection explicite contre les attaques XSS`
  - `X-XSS-Protection - obsolète ou déprécié`
  - `Exemple actuel - Content-Security-Policy active`
  - `CONTRÔLE - Vérifier un mécanisme transmis et applicable`
- Limite : la présence de CSP ne prouve pas que sa politique est suffisamment restrictive.
- Source précise : la solution détaillée de la [règle 210](https://checklists.opquast.com/fr/qualite-numerique/210) demande de ne pas reposer sur l'entête `X-XSS-Protection`, qualifié d'obsolète ou déprécié.
- Transition : une autre directive protège contre l'encadrement trompeur.

### Slide 21 - Qui peut intégrer la page dans un cadre ?

- Rôle : traiter la règle 211.
- Règle : 211.
- Risque : une page légitime est intégrée dans une interface trompeuse pour détourner les clics.
- Mécanisme : `X-Frame-Options` ou directive CSP `frame-ancestors`.
- Composition : une page centrale accepte un cadre autorisé et refuse deux cadres tiers.
- Textes visibles :
  - `RÈGLE 211`
  - `Autoriser explicitement ou interdire l'intégration`
  - `X-Frame-Options`
  - `CSP frame-ancestors`
  - `CONTRÔLE - Vérifier que la politique limite réellement les domaines`
- Limite : la présence d'un entête sans valeur adaptée ne suffit pas.
- Transition : contrôler les cadres ne contrôle pas toutes les ressources chargées.

### Slide 22 - Restreindre l'origine des contenus

- Rôle : traiter la règle 212.
- Règle : 212.
- Risque : la page charge ou exécute un contenu depuis une origine non autorisée.
- Mécanisme : directives CSP comme `script-src`, `style-src`, `img-src` et `font-src`.
- Composition : une liste d'origines autorisées alimente la page ; les autres sont refusées.
- Textes visibles :
  - `RÈGLE 212`
  - `Quelles origines sont autorisées ?`
  - `Scripts · Styles · Images · Polices`
  - `CONTRÔLE - Lire la politique Content-Security-Policy`
  - `LIMITE - Une politique trop permissive peut être présente sans protéger efficacement`
- Propriétaire : développement.
- Transition : une origine autorisée peut encore servir un fichier qui a changé.

### Slide 23 - Vérifier le fichier exact, pas seulement son origine

- Rôle : expliquer la règle 214 sans supposer que le public connaît SRI.
- Règle : 214.
- Risque : un script ou une feuille de style tiers est modifié après son intégration.
- Mécanisme : le navigateur calcule l'empreinte cryptographique du fichier reçu et la compare à l'empreinte attendue dans l'attribut `integrity`.
- Composition : deux fichiers venant du même domaine ; un seul possède exactement l'empreinte attendue.
- Textes visibles :
  - `RÈGLE 214`
  - `Une origine autorisée ne garantit pas un fichier inchangé.`
  - `Empreinte reçue = empreinte attendue`
  - `integrity="sha384-..."`
  - `SRI - Subresource Integrity`
- Explication orale : `sha384` désigne une fonction de hachage. Il ne s'agit ni d'un chiffrement ni d'un secret. Le navigateur bloque la ressource si l'empreinte ne correspond pas.
- Contrôle : examiner chaque élément `script` et `link` qui appelle une ressource tierce, puis vérifier la présence et la validité de `integrity`.
- Limite : le contrôle doit porter sur la ressource effectivement chargée ; une ressource dynamique peut nécessiter une autre stratégie de maîtrise.
- Propriétaire : développement.
- Transition : il reste à réunir ces contrôles sans confondre présence et efficacité.

### Slide 24 - Atelier : lire les entêtes et le code source

- Rôle : mise en pratique du chapitre C.
- Règles : 206, 207, 210, 211, 212 et 214.
- Composition : écran partagé entre l'onglet Réseau et le code HTML.
- Textes visibles :
  - `ENTÊTES`
  - `Content-Type`
  - `X-Content-Type-Options: nosniff`
  - `Content-Security-Policy`
  - `X-Frame-Options ou frame-ancestors`
  - `CODE SOURCE`
  - `integrity="sha384-..."`
  - `VERDICT - Présent, valide ou indéterminé ?`
- Interaction : faire trouver une preuve, puis demander ce qu'elle ne permet pas encore d'affirmer.
- Limites : une seule page ne couvre pas le service ; un entête présent peut être trop permissif ; une empreinte ne protège que la ressource associée.
- Transition : le serveur peut aussi révéler des informations inutiles sans rien exécuter dans la page.

### Slide 25 - Chapitre D : ne pas exposer l'inutile

- Rôle : rapprocher 209 et 213 sans les confondre.
- Règles : 209 et 213.
- Risque : une information inutile à l'utilisateur facilite la préparation d'une attaque.
- Composition : deux fuites distinctes, arborescence de fichiers et entêtes techniques.
- Textes visibles :
  - `D - EXPOSITION MINIMALE`
  - `209 - Ne pas lister les fichiers d'un répertoire`
  - `213 - Ne pas révéler les logiciels et langages du serveur`
  - `Même principe, deux surfaces différentes`
- Propriétaire : infrastructure, avec développement.
- Transition : ces deux surfaces se contrôlent par deux observations différentes.

### Slide 26 - Contrôler ce que le serveur révèle

- Rôle : contrôle pratique et limites du chapitre D.
- Règles : 209 et 213.
- Composition : une URL de répertoire à gauche, une réponse HTTP à droite.
- Textes visibles :
  - `209 - Appeler un répertoire sans page d'index`
  - `Attendu - erreur ou redirection, jamais la liste des fichiers`
  - `213 - Inspecter Server, X-Powered-By et X-AspNet-Version`
  - `Attendu - aucune information sur les logiciels et langages`
  - `LIMITE - Un répertoire et une réponse ne prouvent pas la configuration globale`
- Démonstration : utiliser un environnement de test connu. Ne pas transformer l'anecdote des fiches Covid en fait établi faute de source vérifiée.
- Transition : la confiance se prolonge enfin dans l'information transactionnelle et le courriel.

### Slide 27 - Chapitre E : informer sur la sécurité d'une transaction

- Rôle : traiter la règle 208 et ouvrir le dernier chapitre.
- Règle : 208.
- Risque : l'utilisateur transmet des données sensibles sans pouvoir retrouver l'information sur leur sécurisation.
- Mécanisme : information accessible dans l'aide ou la FAQ sur le mode et le niveau de chiffrement, ou sur la façon de les vérifier dans le navigateur.
- Composition : page de transaction reliée à une aide claire.
- Textes visibles :
  - `E - CONFIANCE AU-DELÀ DE LA PAGE`
  - `RÈGLE 208`
  - `Informer sur la sécurisation de la transaction`
  - `INFORMATION ≠ MÉCANISME DE SÉCURITÉ`
  - `CONTRÔLE - Retrouver une information compréhensible et à jour`
- Limite : le texte informe, mais ne prouve pas à lui seul que le mécanisme annoncé fonctionne.
- Propriétaire : éditorial et support, avec validation technique.
- Transition : lorsque le service envoie un courriel, la preuve quitte la page et passe par le domaine de messagerie.

### Slide 28 - Authentifier le domaine qui envoie les courriels

- Rôle : traiter la règle 217 et faire réaliser le contrôle complet.
- Règle : 217.
- Risque : un courriel frauduleux semble provenir du service administratif.
- Mécanisme : SPF autorise des serveurs, DKIM signe les messages, DMARC définit une politique et vérifie l'alignement.
- Composition : trois preuves convergent vers un courriel reçu.
- Textes visibles :
  - `RÈGLE 217`
  - `SPF - Qui peut envoyer ?`
  - `DKIM - Le message est-il signé ?`
  - `DMARC - Que faire si l'alignement échoue ?`
  - `CONTRÔLE - DNS + entêtes d'un courriel réellement reçu`
  - `LIMITE - Le DNS seul ne prouve pas l'application sur un message`
- Démonstration : utiliser une capture datée et anonymisée d'un domaine de l'administration. Ne jamais afficher d'adresse personnelle ni d'entêtes contenant des données identifiantes.
- Propriétaire : messagerie et DNS.
- Transition : les cinq chapitres ont produit des preuves, mais chacune conserve une portée limitée.

### Slide 29 - Un contrôle ne prouve que ce qu'il observe

- Rôle : synthèse des limites des contrôles.
- Règles : 197 à 217.
- Idée : un résultat valable doit nommer son échantillon, son instant et ce qui reste indéterminé.
- Composition : cinq cartes `preuve` et `limite`.
- Textes visibles :
  - `Une page ≠ tout le service`
  - `Un entête présent ≠ une politique efficace`
  - `Une procédure visible ≠ un parcours utilisable jusqu'au bout`
  - `Un enregistrement DNS ≠ un courriel authentifié`
  - `Une conformité Opquast ≠ un audit cyber complet`
- Oral : dater les captures, conserver la commande ou le chemin de contrôle, indiquer les profils et pages testés, conclure `indéterminé` quand la preuve manque.
- Transition : il reste à transformer le contrôle en responsabilité partagée.

### Slide 30 - Protéger, limiter, vérifier

- Rôle : conclusion et mise en action.
- Règles : 197 à 217.
- Composition : le parcours complet revient, avec un propriétaire sous chaque action.
- Textes visibles :
  - `Protéger le parcours`
  - `Limiter l'exposition`
  - `Vérifier les preuves`
  - `Quelle règle allez-vous contrôler demain à 9 h ?`
- Conclusion orale : la sécurité Opquast devient utile lorsque chaque règle est reliée à un risque utilisateur, à une preuve contrôlable, à une limite explicite et à un propriétaire capable d'agir.

## Distinctions à préserver dans les notes orales

- 197, 198, 199, 200 et 216 participent à la confiance dans l'accès, mais portent respectivement sur la couverture HTTPS, le certificat, l'obligation de rester en HTTPS, les ressources de la page et la visibilité de l'adresse.
- 201 et 202 portent sur deux maîtrises différentes : disponibilité du processus en ligne et choix du mot de passe.
- 204 permet de créer un nouveau mot de passe ; 205 interdit de communiquer un mot de passe en clair.
- 215 exige au moins deux moyens de validation au choix pour une opération sécurisée ; la règle ne définit pas une authentification à deux facteurs.
- 207 déclare la nature de la ressource ; 206 empêche le navigateur de chercher à en deviner une autre.
- 210 traite la protection contre les attaques XSS ; 212 restreint l'origine des contenus. Une politique CSP peut contribuer aux deux sans rendre les règles équivalentes.
- 211 contrôle qui peut encadrer la page ; la directive CSP `frame-ancestors` peut porter ce contrôle.
- 212 autorise ou refuse des origines ; 214 vérifie le contenu exact d'une ressource tierce par son empreinte.
- 209 empêche l'énumération de fichiers ; 213 évite la divulgation d'informations techniques dans les entêtes.
- 208 informe l'utilisateur ; 217 authentifie techniquement le domaine de messagerie.

## Matrice des 21 règles, contrôles, limites et propriétaires

| Règle | Chapitre | Contrôle principal | Limite à annoncer | Propriétaire principal proposé |
|---:|---|---|---|---|
| [197](https://checklists.opquast.com/fr/qualite-numerique/197) | A | Vérifier que chaque page et chaque ressource utilisent HTTPS | Un échantillon de pages ne couvre pas automatiquement tout le service | Infrastructure |
| [198](https://checklists.opquast.com/fr/qualite-numerique/198) | A | Examiner la signature et la période de validité du certificat | Un certificat valide ne prouve pas à lui seul l'identité complète du service | Infrastructure |
| [199](https://checklists.opquast.com/fr/qualite-numerique/199) | A | Inspecter `Strict-Transport-Security` et `max-age` | La présence doit être contrôlée sur les pages concernées | Infrastructure |
| [200](https://checklists.opquast.com/fr/qualite-numerique/200) | A | Rechercher les ressources HTTP dans les pages HTTPS | Une page sans contenu mixte ne suffit pas pour tout le site | Développement |
| [201](https://checklists.opquast.com/fr/qualite-numerique/201) | B | Effectuer intégralement en ligne les opérations liées au mot de passe | Tester tous les parcours utiles et pas seulement le changement nominal | Produit et fonctionnel |
| [202](https://checklists.opquast.com/fr/qualite-numerique/202) | B | Choisir ou modifier le mot de passe | Un mot de passe généré reste acceptable seulement s'il peut être modifié | Produit et fonctionnel |
| [203](https://checklists.opquast.com/fr/qualite-numerique/203) | B | Observer avant soumission un retour sur le degré de sécurisation | L'indicateur visible ne valide pas son algorithme | Produit et développement |
| [204](https://checklists.opquast.com/fr/qualite-numerique/204) | B | Réinitialiser sans être connecté et créer un nouveau mot de passe | Vérifier qu'il ne s'agit pas d'un simple renvoi de l'ancien mot de passe | Produit et développement |
| [205](https://checklists.opquast.com/fr/qualite-numerique/205) | B | Vérifier qu'aucun mot de passe n'est envoyé par courriel | Examiner création, rappel et réinitialisation | Développement |
| [206](https://checklists.opquast.com/fr/qualite-numerique/206) | C | Vérifier `X-Content-Type-Options: nosniff` | L'entête n'assure pas que le type déclaré est correct | Développement |
| [207](https://checklists.opquast.com/fr/qualite-numerique/207) | C | Vérifier un `Content-Type` adapté à chaque type de ressource | La présence seule ne valide pas la valeur | Développement |
| [208](https://checklists.opquast.com/fr/qualite-numerique/208) | E | Retrouver l'information depuis l'aide ou la FAQ | Une information ne prouve pas le fonctionnement du chiffrement | Éditorial et support |
| [209](https://checklists.opquast.com/fr/qualite-numerique/209) | D | Appeler des répertoires sans page d'index | Quelques répertoires testés ne couvrent pas toute l'arborescence | Infrastructure |
| [210](https://checklists.opquast.com/fr/qualite-numerique/210) | C | Vérifier une protection XSS explicite, actuelle et applicable | Une CSP présente peut rester trop permissive | Développement |
| [211](https://checklists.opquast.com/fr/qualite-numerique/211) | C | Vérifier `X-Frame-Options` ou CSP `frame-ancestors` | Il faut examiner la valeur et pas seulement le nom de l'entête | Développement |
| [212](https://checklists.opquast.com/fr/qualite-numerique/212) | C | Lire les directives de `Content-Security-Policy` | La présence de CSP ne valide pas la pertinence de toutes ses sources | Développement |
| [213](https://checklists.opquast.com/fr/qualite-numerique/213) | D | Contrôler l'absence d'informations techniques dans les entêtes | Un proxy ou une autre route peut produire une réponse différente | Infrastructure |
| [214](https://checklists.opquast.com/fr/qualite-numerique/214) | C | Vérifier `integrity` sur chaque `script` et `link` tiers | L'empreinte protège uniquement la ressource à laquelle elle est associée | Développement |
| [215](https://checklists.opquast.com/fr/qualite-numerique/215) | B | Réaliser l'opération avec au moins deux moyens au choix | Une solution de secours doit être réellement utilisable | Produit et fonctionnel |
| [216](https://checklists.opquast.com/fr/qualite-numerique/216) | A | Vérifier la barre d'adresse dans chaque fenêtre ouverte | Une adresse visible ne garantit pas la légitimité globale du service | Produit et fonctionnel |
| [217](https://checklists.opquast.com/fr/qualite-numerique/217) | E | Vérifier SPF, DKIM, DMARC puis les entêtes d'un message reçu | Le DNS seul ne prouve ni la signature ni l'alignement du message réel | Messagerie et DNS |

## Preuves de démonstration à préparer

- Chapitre A : capture datée du certificat, des requêtes HTTPS, de HSTS et de l'absence de contenu mixte sur plusieurs pages représentatives.
- Chapitre B : compte de démonstration sans donnée personnelle, parcours de changement et de réinitialisation, deux moyens de validation disponibles.
- Chapitre C : capture datée des entêtes HTTP et d'un extrait HTML contenant un attribut `integrity` valide.
- Chapitre D : environnement de test montrant une redirection ou une erreur pour un répertoire sans index, puis des entêtes sans divulgation technique.
- Chapitre E : page d'aide transactionnelle et courriel reçu anonymisé montrant les résultats SPF, DKIM et DMARC.

Les exemples DNS et les entêtes de messagerie doivent être figés et datés. La présentation ne doit pas dépendre d'un contrôle en direct sur un service public.

## Quatre slides étalons à valider avant génération

- Ouverture : slide 01.
- Règle : slide 23 sur l'empreinte d'intégrité des ressources tierces.
- Éclairage : slide 20 sur la règle 210 et l'abandon de `X-XSS-Protection`.
- Synthèse : slide 30.

Aucune génération massive, rédaction complète des notes orales ou délégation parallèle ne commence avant validation explicite de ces quatre étalons.

## Auto-évaluation du storyboard

| Dimension | Note sur 10 | Justification |
|---|---:|---|
| Couverture | 10 | Les 21 règles figurent dans le parcours et dans la matrice finale |
| Clarté | 9 | Cinq chapitres, un patron stable et des distinctions explicites |
| Conviction | 9 | Chaque règle part d'un risque utilisateur et aboutit à une preuve |
| Engagement | 9 | Question d'ouverture, associations, atelier compte et atelier entêtes |
| Actionnabilité | 10 | Contrôle, limite et propriétaire sont indiqués pour chaque règle |

## Sources d'autorité

- Référentiel Opquast V5, fiches officielles des règles 197 à 217, API `qualite-numerique`, consultée le 17 octobre 2026.
- Grammaire visuelle de référence : `navigation-opquast-v5-360/source/storyboard.md` et ses 17 premières slides.
- Contrat éditorial interne : `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`.
- Passe de couverture connu-inconnu réalisée avant la présente réécriture.
