# Storyboard Opquast - Données personnelles

## Statut

**Version définitive, challengée avec l'Assistant Opquast et prête pour le préflight de génération.**

- Thématique principale : Données personnelles
- Périmètre principal : règles officielles 15 à 29
- Couverture principale : 15 règles sur 15
- Deck principal : 15 slides
- Annexe 1 intégrée : 4 slides « Privacy au-delà de la rubrique »
- Format : 16:9
- Usage : formation, projection, préparation certification
- Fil pédagogique : préjudice utilisateur -> garantie recherchée -> règle
- Doctrine narrative : Progressive Disclosure Slides (PDS)
- Série de référence : Opquast « Images et médias »

## Périmètre assumé

Le **deck principal** couvre les 15 règles de la rubrique Données personnelles, règles 15 à 29.

Il porte sur des exigences Opquast vérifiables en ligne et ayant une valeur ajoutée démontrable pour l'utilisateur. Il contribue à la maîtrise des risques liés à la vie privée, mais **ne constitue pas un audit exhaustif de conformité au RGPD**.

L'**Annexe 1**, intégrée au même module, ouvre sur une sélection de règles transversales liées à la vie privée dans d'autres rubriques. Cette annexe est clairement séparée du périmètre officiel 15 à 29 afin de ne pas confondre rubrique et transversalité.

## Sources de fond

- `support(1).md`
- `notebook-lm-donnees-perso(1).md`
- `VPTCS(1).md`
- `Metiers-profils-données-personnelles(1).md`
- Livre `qualite-et-conformite-des-services-numeriques-llm.md`
- API Opquast, règles 15 à 29, 30, 33, 59, 60 et 173 à 176, version `qualite-numerique`

## Sources de méthode

- skill `generer-images-slides-ia`
- skill `prompt-image`
- skill `chain-of-summaries-cos`
- `06-WORKFLOW-GENERATION.md`
- `12-STORYBOARD-TEMPLATE.md`
- `09-CHECKLIST-QA.md`
- guide de style de la série « Images et médias »

## Décisions issues du challenge Opquast

- Les axes `Savoir · Maîtriser · Protéger` restent explicitement pédagogiques.
- VPTCS respecte la chronologie officielle : V avant, P/T/C pendant, S après.
- La règle 16 est présentée comme contrôle de présence d'une procédure, sans évaluer sa qualité.
- La règle 18 reste un `processus de confirmation`, sans raccourci systématique vers `double opt-in`.
- La règle 19 parle d'un mécanisme d'authentification forte proposé, sans promesse de sécurité absolue.
- La règle 21 reste centrée sur sauvegarde et réutilisation des contenus, sans l'assimiler au droit juridique à la portabilité.
- La règle 23 montre la désactivation globale des connexions actives, conformément à la solution et au contrôle officiels.
- La règle 25 exige une politique de communication des referrers : elle n'est pas réduite à `no-referrer`.
- La règle 26 utilise un exemple de message neutre, pas une formulation officielle imposée.
- La règle 27 conserve ses deux dimensions : sécuriser l'échange et le signaler comme tel.
- La règle 28 n'assimile pas `POST` à une garantie de sécurité complète.
- La responsabilité métiers est présentée comme collective, sans faire du DPO le garant unique de la conformité.
- Le deck principal reste strictement limité aux règles 15 à 29.
- L'Annexe 1 traite séparément une sélection de règles transversales liées à la vie privée.
- La règle 33 est intégrée à l'annexe pour sa proximité pédagogique avec le consentement et le libre choix ; elle n'est pas présentée comme portant nécessairement le tag API `Privacy`.
- Les slides 03, 13 et 14 sont volontairement simplifiées pour réussir le test de compréhension en trois secondes.

---

# Colonne vertébrale PDS

La série progresse en cinq étapes.

1. **Comprendre** : poser les trois enjeux et la méthode.
2. **Maîtriser le compte** : création, confirmation, identité, sortie, sessions.
3. **Protéger les échanges** : referrers, existence d'un compte, échanges sensibles, URL.
4. **Partager la responsabilité** : VPTCS et métiers.
5. **Réviser** : cas pratiques et synthèse.

À partir de la slide 2, une barre discrète de cinq segments indique l'étape active. Aucun texte n'est nécessaire dans cette barre.

---

# Masque commun

## Format

- paysage 16:9 ;
- fond blanc dominant ;
- densité modérée ;
- une idée principale par slide ;
- scène centrale lisible en trois secondes.

## Header

En haut à gauche, texte exact :

`QUALITÉ WEB`  
`EXPÉRIENCES DURABLES`

En haut à droite, bloc typographique texte uniquement :

`Opquast`  
`DES SITES MEILLEURS POUR TOUS`

Ne pas inventer de logo, pictogramme de marque ou emblème.

## Titre

- grand titre pédagogique ;
- bleu marine profond ;
- centré, pour continuité avec la série « Images et médias » ;
- casse de phrase ;
- formulation courte.

Cette position centrée est une dérogation volontaire au réglage générique du skill afin de préserver la continuité de la série de référence.

## Typographie

- Marianne pour tout texte visible ;
- Arial seulement en fallback explicite ;
- pas de police décorative ;
- aucun paragraphe long dans les cartes.

## Palette

- bleu marine : structure, titres, information ;
- bleu clair : pédagogie et accès ;
- vert : maîtrise, solution, action possible ;
- orange : vigilance ou choix ;
- rouge : uniquement risque, blocage ou erreur ;
- violet doux : repère secondaire si nécessaire ;
- gris très clair : panneaux et séparations.

Le callout final n'est jamais rouge.

## Callout

Un callout court, centré au-dessus du footer, de largeur et position stables sur toute la série.

## Footer

### Deck principal

Texte exact :

`RÈGLES OPQUAST · DONNÉES PERSONNELLES`

Pagination exacte :

`NN / 15`

### Annexe 1

Texte exact :

`ANNEXE 1 · PRIVACY AU-DELÀ DE LA RUBRIQUE`

Pagination exacte :

`A1-NN / 04`

## Interdits communs

- pas de faux logo ;
- pas d'emblème officiel inventé ;
- pas de photo corporate ;
- pas de 3D ;
- pas de dégradé appuyé ;
- pas de blob décoratif ;
- pas de paragraphes à l'écran ;
- pas de texte inventé ;
- pas de promesse juridique absolue ;
- ne pas présenter un regroupement pédagogique comme un classement officiel Opquast.

---

# Slide 01 - Données personnelles

**Rôle narratif**

Ouverture. Installer les trois enjeux de la rubrique.

**Message clé**

Les données personnelles doivent rester compréhensibles, maîtrisables et protégées tout au long du parcours.

**Situation**

Une personne utilise un service numérique. Son profil, son compte, ses contenus et un échange sensible sont visibles autour de l'interface.

**Risque**

L'utilisateur peut ne plus savoir ce qui est fait de ses données, perdre la maîtrise de son compte ou voir des informations exposées.

**Principe**

Lire toute la rubrique avec trois verbes : savoir, maîtriser, protéger.

**Règle / repère**

Rubrique Données personnelles, règles 15 à 29.

Les trois axes `Savoir · Maîtriser · Protéger` sont un regroupement pédagogique de la présentation, pas une classification officielle Opquast.

**Scène visuelle**

Une personne devant une interface de compte. Trois zones reliées à la même interface :
- une fiche d'information « Confidentialité » ;
- des commandes de compte et d'export ;
- un échange protégé par un cadenas.

La scène doit faire comprendre qu'il s'agit d'une même expérience utilisateur, pas de trois sujets isolés.

**Personnage ou objet-système**

Utilisateur + espace personnel.

**Transformation visible**

Données dispersées et opaques -> informations lisibles, commandes disponibles, échange protégé.

**Textes visibles exacts**

Titre :
`Données personnelles`

Sous-titre :
`Savoir · Maîtriser · Protéger`

Labels :
- `Comprendre`
- `Garder la main`
- `Protéger`

Callout :
`Mes données doivent rester sous contrôle.`

**Ce que l'image seule doit faire comprendre**

Les données personnelles concernent à la fois l'information, la maîtrise du compte et la protection technique.

**Ajout / transition**

Ouvre les trois enjeux. La slide suivante explique la méthode utilisée pour lire les règles.

**Discours oral**

Les données personnelles ne sont pas seulement un sujet juridique. Pour l'utilisateur, les questions sont très concrètes : est-ce que je sais ce que vous faites de mes données ? Est-ce que je garde la maîtrise de mon compte ? Est-ce que mes informations restent protégées ?

**Impact utilisateur**

Perte de compréhension, perte de maîtrise ou exposition des informations.

**Ce que les règles visent à garantir**

Transparence, maîtrise et protection.

**Mémo oral**

`Savoir. Maîtriser. Protéger.`

**Contraintes critiques**

- les trois axes doivent être immédiatement distinguables ;
- aucune balance de justice, marteau de juge ou symbole juridique dominant ;
- ne pas réduire la thématique au RGPD ;
- ne pas suggérer que les règles 15 à 29 constituent un audit RGPD exhaustif ;
- les trois axes sont pédagogiques, pas une taxonomie officielle Opquast ;
- le mot `Protéger` ne doit pas être associé uniquement à un cadenas abstrait sans utilisateur.

**Nom de fichier**

`slide-01-donnees-personnelles-savoir-maitriser-proteger.png`

---

# Slide 02 - Commencer par le préjudice utilisateur

**Rôle narratif**

Méthode de lecture des règles.

**Message clé**

Avant de mémoriser une règle, comprendre ce que l'utilisateur risque de subir et ce que la règle cherche à préserver.

**Situation**

Un cas utilisateur simple est analysé pas à pas.

**Risque**

Apprendre des numéros ou des formulations sans comprendre pourquoi la règle existe.

**Principe**

Partir du problème concret puis remonter vers la règle.

**Règle / repère**

Méthode pédagogique de la série.

**Scène visuelle**

Progression horizontale en cinq étapes, illustrée par un même petit scénario de compte utilisateur qui se précise au fil du parcours.

**Personnage ou objet-système**

Utilisateur + fiche de compte.

**Transformation visible**

Situation concrète -> préjudice identifié -> garantie comprise -> règle retrouvée -> mise en œuvre.

**Textes visibles exacts**

Titre :
`Commencer par le préjudice utilisateur`

Étapes :
- `Situation`
- `Préjudice`
- `Garantie`
- `Règle`
- `Mise en œuvre`

Callout :
`Quel préjudice ? Que cherche à garantir la règle ?`

**Ce que l'image seule doit faire comprendre**

La règle arrive après la compréhension du problème, pas avant.

**Ajout / transition**

Transforme les trois enjeux de la slide 1 en méthode. Prépare la première famille : comprendre ce qui est fait des données.

**Discours oral**

Je vous propose de ne pas commencer par le numéro de la règle. Commençons par l'utilisateur : que lui arrive-t-il si la règle n'est pas appliquée ? Ensuite seulement, demandons-nous ce que la règle cherche à préserver.

**Impact utilisateur**

Sans cette lecture, la règle devient une consigne isolée difficile à retenir et à appliquer correctement.

**Ce que la méthode vise à garantir**

Une compréhension orientée expérience utilisateur.

**Mémo oral**

`Préjudice -> garantie -> règle.`

**Contraintes critiques**

- cinq étapes exactement ;
- `Préjudice` remplace `Risque` dans le schéma visible ;
- `Garantie` remplace `Principe` dans le schéma visible ;
- aucune règle numérotée sur cette slide ;
- ne pas transformer le schéma en frise juridique.

**Nom de fichier**

`slide-02-prejudice-garantie-regle.png`

---

# Slide 03 - L'information doit être trouvable et utile

**Rôle narratif**

Première famille de règles : transparence.

**Message clé**

Informer ne suffit pas : l'utilisateur doit pouvoir retrouver l'information, savoir où agir et comprendre les conséquences liées aux cookies.

**Situation**

Une personne consulte une seule page du service et cherche trois réponses :
- où trouver la politique de confidentialité ?
- où trouver la procédure d'accès et de rectification ?
- à quoi servent les cookies et que se passe-t-il si je les refuse ?

**Risque**

Incertitude, difficulté à agir sur ses données et conséquences des cookies mal comprises.

**Principe**

Rendre les informations essentielles trouvables dans une expérience cohérente.

**Règle / repère**

- 15 : politique de confidentialité disponible depuis toutes les pages ;
- 16 : procédure d'accès et de rectification décrite ;
- 29 : objectif des cookies et limitations de leur refus expliqués.

**Scène visuelle**

**Une seule page web**, pas trois cartes autonomes.

Trois points d'accès sont mis en évidence sur cette page :
1. un lien `Confidentialité` dans le footer ;
2. une entrée `Accès et rectification` dans la politique ou l'aide ;
3. une explication courte `Cookies : rôle et conséquences`.

Une même trajectoire visuelle relie l'utilisateur à ces trois accès.

**Personnage ou objet-système**

Utilisateur + une page web unique.

**Transformation visible**

Questions dispersées -> trois réponses trouvables dans le même service.

**Textes visibles exacts**

Titre :
`L'information doit être trouvable et utile`

Points d'accès :
- `Confidentialité`
- `Accès et rectification`
- `Cookies : rôle et conséquences`

Badges discrets :
- `15`
- `16`
- `29`

Callout :
`Trouver l'information au moment où j'en ai besoin.`

**Ce que l'image seule doit faire comprendre**

La transparence n'est pas une accumulation de textes juridiques : l'utilisateur doit pouvoir trouver les informations utiles dans son parcours.

**Ajout / transition**

Applique la méthode au premier enjeu « savoir ». La slide suivante élargit cette logique dans le temps avec VPTCS.

**Discours oral**

Une politique de confidentialité qui existe mais qu'on ne trouve pas ne remplit qu'une partie de son rôle. L'utilisateur doit aussi savoir où trouver la procédure pour agir sur ses données et comprendre à quoi servent les cookies ainsi que les conséquences de leur refus.

**Impact utilisateur**

Il peut rester dans l'incertitude, ne pas savoir comment exercer une demande ou faire un choix sans en comprendre les conséquences.

**Ce que les règles visent à garantir**

Une politique accessible, une procédure décrite et une explication compréhensible des cookies et des limitations liées à leur refus.

**Mémo oral**

`Trouver. Savoir où agir. Comprendre les conséquences.`

**Contraintes critiques**

- une seule interface principale, pas trois mini-slides ;
- ne pas écrire que la règle 16 évalue la qualité ou l'efficacité de la procédure : seule sa présence est contrôlée ;
- ne pas représenter les cookies uniquement comme une bannière de consentement ;
- ne pas ajouter ici de règle e-commerce ou newsletter ;
- trois labels visibles maximum en plus du titre et du callout ;
- les badges 15, 16 et 29 restent secondaires.

**Sources officielles**

(API Opquast, règles n° 15, 16 et 29, version qualite-numerique)

**Nom de fichier**

`slide-03-information-trouvable-et-utile.png`

---

# Slide 04 - Les données vivent avant, pendant et après la visite

**Rôle narratif**

Donner le cadre VPTCS sans transformer VPTCS en classement officiel des règles.

**Message clé**

La protection des données traverse tout le parcours utilisateur.

**Situation**

La même personne rencontre le service à trois moments : avant l'interaction, pendant l'usage et après.

**Risque**

Réduire la vie privée à un écran de consentement ou à une seule équipe.

**Principe**

Observer ce qui est visible, perçu, transmis, expliqué et rendu possible dans la durée.

**Règle / repère**

Cadre méthodologique VPTCS. Repère transversal, non classement officiel de la rubrique.

**Scène visuelle**

Une même personne traverse trois temps clairement distincts :
- avant l'interface : rencontrer et identifier le service ;
- pendant l'interface : perception, technique et contenus ;
- après l'interface : services et relation qui se prolonge.

Sous ces trois temps, cinq repères discrets : Visibilité, Perception, Technique, Contenus, Services.

**Personnage ou objet-système**

Même utilisateur sur tout le parcours.

**Transformation visible**

Vision ponctuelle -> vision complète du cycle de vie de l'expérience.

**Textes visibles exacts**

Titre :
`Les données vivent avant, pendant et après la visite`

Étapes :
- `Avant`
- `Pendant`
- `Après`

Repères :
- `Visibilité`
- `Perception`
- `Technique`
- `Contenus`
- `Services`

Callout :
`La protection traverse tout le parcours.`

**Ce que l'image seule doit faire comprendre**

Les données continuent d'exister et d'avoir des effets au-delà du formulaire où elles sont saisies.

**Ajout / transition**

Élargit la transparence à l'ensemble du parcours. La suite zoome sur la création et la maîtrise du compte.

**Discours oral**

Le modèle VPTCS donne une vision structurée des exigences utilisateurs. Il se lit chronologiquement : Visibilité avant le contact avec l'interface, Perception, Technique et Contenus pendant l'interface, Services après. Ici, il sert de cadre mental pour ne pas réduire la protection des données à une seule page ou à un seul métier.

**Impact utilisateur**

Une approche trop ponctuelle laisse des angles morts dans l'expérience globale.

**Ce que le cadre apporte**

Une vision complète et structurée des exigences utilisateurs et des responsabilités du projet.

**Mémo oral**

`V avant. PTC pendant. S après.`

**Contraintes critiques**

- VPTCS est un cadre de lecture des exigences utilisateurs, pas un classement officiel des règles 15 à 29 ;
- respecter la chronologie Opquast : V avant, P/T/C pendant, S après ;
- ne pas placer mécaniquement une règle sous une seule lettre VPTCS ;
- la scène doit rester humaine et chronologique ;
- pas de matrice dense.

**Nom de fichier**

`slide-04-donnees-avant-pendant-apres-vptcs.png`

---

# Slide 05 - Le tiers peut être proposé, jamais imposé

**Rôle narratif**

Entrée dans la maîtrise du compte.

**Message clé**

L'utilisateur doit pouvoir créer son compte sans dépendre obligatoirement d'un système d'identification tiers.

**Situation**

À l'inscription, deux chemins sont proposés : un compte direct et une identification tierce.

**Risque**

L'utilisateur est exclu s'il ne souhaite pas utiliser le tiers ou si ce tiers devient indisponible.

**Principe**

Conserver une voie d'accès maîtrisée par le service.

**Règle / repère**

17. La création de compte est possible sans recours à un système d'identification tiers.

**Scène visuelle**

Deux portes vers le même service :
- porte 1 : `Créer mon compte` ;
- porte 2 : `Service tiers`.

La première reste toujours ouverte. La seconde est une option, pas un passage obligatoire.

**Personnage ou objet-système**

Utilisateur face à deux parcours d'inscription.

**Transformation visible**

Passage obligatoire par un tiers -> choix entre accès direct et accès tiers.

**Textes visibles exacts**

Titre :
`Le tiers peut être proposé, jamais imposé`

Labels :
- `Compte direct`
- `Service tiers`
- `Choix utilisateur`

Badge :
`17`

Callout :
`Toujours garder une voie d'accès indépendante.`

**Ce que l'image seule doit faire comprendre**

Le tiers est optionnel.

**Ajout / transition**

Commence la maîtrise du compte. La slide suivante vérifie que la personne qui crée et utilise ce compte est bien celle attendue.

**Discours oral**

« Connectez-vous avec un service tiers » peut être pratique. Le problème apparaît quand cela devient le seul chemin. Si l'utilisateur ne veut pas utiliser ce tiers, ou si ce tiers devient indisponible, il ne doit pas être exclu du service.

**Impact utilisateur**

Perte de liberté de choix et dépendance à un acteur extérieur.

**Ce que la règle vise à garantir**

Une solution d'accès indépendante du tiers.

**Mémo oral**

`Le tiers : option, jamais obligation.`

**Contraintes critiques**

- ne pas afficher de marques réelles de fournisseurs tiers ;
- ne pas inventer de logo Google, Facebook ou autre ;
- ne pas suggérer que l'identification tierce est interdite ;
- montrer clairement que les deux chemins arrivent au même service.

**Source officielle**

(API Opquast, règle n° 17, version qualite-numerique)

**Nom de fichier**

`slide-05-identification-tiers-optionnelle.png`

---

# Slide 06 - Créer un compte, puis vérifier qui agit

**Rôle narratif**

Sécuriser l'entrée et l'identité.

**Message clé**

La création doit être confirmée, puis le compte doit pouvoir bénéficier d'une authentification renforcée.

**Situation**

Une personne crée un compte. Un e-mail de confirmation valide la création. Lors d'une connexion sensible, un second facteur protège l'accès.

**Risque**

Création de compte à l'insu de la personne ou usurpation du compte.

**Principe**

Vérifier la création puis renforcer l'authentification.

**Règle / repère**

- 18 : processus de confirmation ;
- 19 : mécanisme de prévention des usurpations de compte ou d'identité.

**Scène visuelle**

Progression en trois temps :
1. `Demande de compte`
2. `Confirmation`
3. `Authentification renforcée`

Une même personne reste visible sur tout le flux.

**Personnage ou objet-système**

Utilisateur + e-mail de confirmation + second facteur.

**Transformation visible**

Compte demandé -> compte confirmé -> accès renforcé.

**Textes visibles exacts**

Titre :
`Créer un compte, puis vérifier qui agit`

Labels :
- `Demande`
- `Confirmation`
- `Authentification forte proposée`

Badges :
- `18`
- `19`

Callout :
`Confirmer la création, réduire le risque d'usurpation.`

**Ce que l'image seule doit faire comprendre**

Confirmation de création et prévention de l'usurpation sont deux moments différents.

**Ajout / transition**

Après la possibilité de créer le compte, cette slide sécurise son activation et son usage. La slide suivante simplifie ensuite l'accès à plusieurs services.

**Discours oral**

Quelqu'un peut saisir mon adresse électronique volontairement ou par erreur. Avant d'activer le compte, le service doit vérifier que le propriétaire de l'adresse confirme réellement la création. Ensuite, un mécanisme d'authentification forte peut limiter les risques d'usurpation.

**Impact utilisateur**

Inscription à son insu ou prise de contrôle du compte.

**Ce que les règles visent à garantir**

Une création confirmée et une protection renforcée de l'identité.

**Mémo oral**

`Confirmer la création. Renforcer l'accès.`

**Contraintes critiques**

- ne pas écrire `double opt-in` ;
- utiliser `processus de confirmation` ;
- ne pas présenter la 2FA comme protection absolue ;
- distinguer visuellement règle 18 et règle 19 ;
- trois étapes maximum.

**Sources officielles**

(API Opquast, règles n° 18 et 19, version qualite-numerique)

**Nom de fichier**

`slide-06-confirmation-et-prevention-usurpation.png`

---

# Slide 07 - Une organisation, un jeu d'identifiants

**Rôle narratif**

Réduire la charge liée à l'accès aux services.

**Message clé**

Quand une même entité propose plusieurs services privés, l'utilisateur doit pouvoir employer les mêmes identifiants.

**Situation**

Une personne accède à trois services d'une même organisation.

**Risque**

Multiplication inutile des identifiants et mots de passe.

**Principe**

Mutualiser le jeu d'identifiants et, le cas échéant, les moyens d'authentification renforcée.

**Règle / repère**

22. La connexion à tous les services proposés est possible avec les mêmes identifiants.

**Scène visuelle**

À gauche, trois services avec trois clés différentes forment un nœud confus. À droite, une seule clé utilisateur ouvre les trois services.

**Personnage ou objet-système**

Utilisateur + trois espaces privés + une clé d'identité.

**Transformation visible**

Trois identifiants -> un jeu d'identifiants commun.

**Textes visibles exacts**

Titre :
`Une organisation, un jeu d'identifiants`

Labels :
- `Service A`
- `Service B`
- `Service C`
- `Mêmes identifiants`

Badge :
`22`

Callout :
`Moins de comptes à mémoriser, accès plus simple.`

**Ce que l'image seule doit faire comprendre**

Une même identité ouvre plusieurs services de la même entité.

**Ajout / transition**

Simplifie l'accès après sa sécurisation. La slide suivante montre que cette simplicité ne doit pas créer de captivité.

**Discours oral**

Si une organisation propose plusieurs services privés, multiplier les comptes et les mots de passe impose une charge inutile. La règle vise à permettre l'usage des mêmes identifiants sur les services proposés.

**Impact utilisateur**

Charge de mémorisation et multiplication des identifiants.

**Ce que la règle vise à garantir**

Un accès plus simple et cohérent entre les services d'une même entité.

**Mémo oral**

`Une organisation, un jeu d'identifiants.`

**Contraintes critiques**

- ne pas confondre cette règle avec la règle 17 ;
- ne pas représenter un fournisseur SSO tiers comme obligatoire ;
- trois services maximum ;
- aucune marque réelle.

**Source officielle**

(API Opquast, règle n° 22, version qualite-numerique)

**Nom de fichier**

`slide-07-memes-identifiants-plusieurs-services.png`

---

# Slide 08 - Sortir sans perdre ses contenus

**Rôle narratif**

Réversibilité.

**Message clé**

Un compte ouvert en ligne doit pouvoir être fermé en ligne, et les contenus personnels doivent pouvoir être sauvegardés.

**Situation**

Une personne décide de quitter un service.

**Risque**

Captivité du compte, perte des contenus, ressaisie future.

**Principe**

Permettre la fermeture par un processus similaire et l'export des contenus personnels dans un format exploitable.

**Règle / repère**

- 20 : fermeture par le même moyen ;
- 21 : téléchargement des contenus personnels.

**Scène visuelle**

Un espace personnel avec deux actions visibles :
- une valise ou dossier `Télécharger mes contenus` ;
- une sortie `Fermer mon compte en ligne`.

La personne quitte le service avec son dossier de contenus.

**Personnage ou objet-système**

Utilisateur + espace personnel + dossier exporté + sortie.

**Transformation visible**

Compte captif -> contenus récupérés -> compte fermé.

**Textes visibles exacts**

Titre :
`Sortir sans perdre ses contenus`

Labels :
- `Télécharger`
- `Format exploitable`
- `Fermer en ligne`

Badges :
- `20`
- `21`

Callout :
`Je peux partir sans abandonner mes contenus.`

**Ce que l'image seule doit faire comprendre**

Quitter le service et récupérer ses contenus sont deux garanties complémentaires.

**Ajout / transition**

Après l'entrée et l'accès, on traite la sortie. La slide suivante revient à la maîtrise quotidienne du compte.

**Discours oral**

Un compte créé en ligne ne devrait pas devenir un piège dont on ne peut sortir qu'en téléphonant ou en envoyant un courrier. Et si l'utilisateur a créé ou saisi des contenus, il doit pouvoir les sauvegarder et les réutiliser.

**Impact utilisateur**

Sentiment de captivité, perte de contenus ou ressaisie.

**Ce que les règles visent à garantir**

Une sortie accessible et une sauvegarde réutilisable des contenus personnels.

**Mémo oral**

`Ouvert en ligne, fermé en ligne. Mes contenus repartent avec moi.`

**Contraintes critiques**

- ne pas écrire `droit à la portabilité` ;
- montrer un format exploitable sans inventer de format obligatoire ;
- ne pas montrer la suppression du compte comme instantanée si le scénario n'est pas qualifié ;
- ne pas dire « réversibilité absolue ».

**Sources officielles**

(API Opquast, règles n° 20 et 21, version qualite-numerique)

**Nom de fichier**

`slide-08-fermeture-compte-et-export-contenus.png`

---

# Slide 09 - Garder la main sur son compte

**Rôle narratif**

Maîtrise quotidienne du compte et de l'adresse e-mail.

**Message clé**

L'utilisateur doit pouvoir fermer ses connexions actives et utiliser une adresse e-mail dédiée avec le signe +.

**Situation**

Dans les réglages de son compte, une personne vérifie ses sessions et choisit une adresse dédiée au service.

**Risque**

Session privée laissée ouverte sur un appareil ou impossibilité d'utiliser un alias permettant de tracer la diffusion de son adresse.

**Principe**

Donner des contrôles concrets sur les connexions et accepter les alias e-mail standards.

**Règle / repère**

- 23 : possibilité de se déconnecter des espaces privés ;
- 24 : alias mail contenant le signe + acceptés.

**Scène visuelle**

Écran de réglages « Mon compte » avec deux cartes :
- `Connexions actives` et action `Tout déconnecter` ;
- champ e-mail `lea+service@example.fr` marqué comme accepté.

**Personnage ou objet-système**

Utilisateur + panneau de sécurité du compte.

**Transformation visible**

Sessions dispersées et adresse refusée -> sessions maîtrisées et alias accepté.

**Textes visibles exacts**

Titre :
`Garder la main sur son compte`

Labels :
- `Connexions actives`
- `Tout déconnecter`
- `lea+service@example.fr`
- `Alias accepté`

Badges :
- `23`
- `24`

Callout :
`Fermer l'accès. Tracer son adresse.`

**Ce que l'image seule doit faire comprendre**

La maîtrise du compte passe aussi par des contrôles simples et concrets.

**Ajout / transition**

Clôt la famille « maîtrise du compte ». La slide suivante ouvre la famille « protéger les échanges ».

**Discours oral**

Une session ouverte donne accès à des informations privées. Le service doit permettre de reprendre la main sur les connexions actives. Et l'acceptation des alias avec + donne à l'utilisateur un moyen simple de dédier et de tracer une adresse e-mail.

**Impact utilisateur**

Accès non souhaité à une session ou perte d'un outil de traçabilité de l'adresse.

**Ce que les règles visent à garantir**

La possibilité de désactiver globalement les connexions actives et d'utiliser une adresse e-mail dédiée avec le signe +.

**Mémo oral**

`Couper toutes les sessions. Garder le +.`

**Contraintes critiques**

- la règle 23 doit montrer la possibilité de désactiver globalement toutes les connexions actives sur les différents appareils ;
- ne pas réduire la règle 23 à la présence d'un simple bouton de déconnexion locale ;
- l'adresse avec + doit être syntaxiquement plausible et lisible ;
- ne pas présenter l'alias comme une nouvelle boîte mail ;
- ne pas fusionner les deux règles en une seule causalité.

**Sources officielles**

(API Opquast, règles n° 23 et 24, version qualite-numerique)

**Nom de fichier**

`slide-09-deconnexion-et-alias-mail.png`

---

# Slide 10 - Changer de site ne doit pas raconter d'où je viens

**Rôle narratif**

Prévenir une fuite technique discrète.

**Message clé**

Le serveur doit maîtriser les informations de provenance communiquées lorsqu'un utilisateur suit un lien.

**Situation**

Une personne quitte une page du service pour ouvrir un site tiers.

**Risque**

L'adresse de la page d'origine peut divulguer des informations sur sa navigation.

**Principe**

Définir une politique de communication des referrers.

**Règle / repère**

25. Les entêtes envoyés par le serveur spécifient la politique de communication des referrers.

**Scène visuelle**

Flux gauche-droite :
- page d'origine ;
- filtre `Referrer-Policy` ;
- site tiers.

Le filtre applique la politique de referrer prévue avant la sortie vers le site tiers.

**Personnage ou objet-système**

Navigateur + en-tête serveur + site tiers.

**Transformation visible**

Transmission non maîtrisée de la provenance -> politique de communication explicitement définie.

**Textes visibles exacts**

Titre :
`Maîtriser ce que le site cible apprend d'où je viens`

Labels :
- `Page d'origine`
- `Referrer-Policy`
- `Site tiers`

Badge :
`25`

Callout :
`Définir ce qui peut être transmis au site cible.`

**Ce que l'image seule doit faire comprendre**

Une information invisible pour l'utilisateur peut partir vers le site cible, sauf si le serveur la maîtrise.

**Ajout / transition**

Introduit les fuites techniques. La slide suivante montre qu'une interface elle-même peut aussi révéler une information sensible.

**Discours oral**

Lorsqu'on suit un lien, le navigateur peut communiquer au site cible des informations sur la page d'origine. La règle ne demande pas forcément de supprimer tout referrer : elle demande que le serveur définisse explicitement la politique de communication afin d'éviter des fuites indésirables.

**Impact utilisateur**

Des informations de navigation peuvent être communiquées à un tiers sans qu'il en ait conscience.

**Ce que la règle vise à garantir**

Une politique explicite et maîtrisée de transmission des informations de provenance.

**Mémo oral**

`Ne pas laisser le referrer au hasard.`

**Contraintes critiques**

- écrire exactement `Referrer-Policy` ;
- ne pas afficher de valeur d'en-tête non nécessaire à la compréhension ;
- ne pas prétendre qu'aucune information n'est jamais transmise ;
- ne pas assimiler systématiquement la règle à `no-referrer` ;
- ne pas placer cette règle principalement dans « Visibilité » : la scène est technique.

**Source officielle**

(API Opquast, règle n° 25, version qualite-numerique)

**Nom de fichier**

`slide-10-referrer-policy-maitriser-provenance.png`

---

# Slide 11 - Aider sans révéler si le compte existe

**Rôle narratif**

Montrer qu'un message d'interface peut devenir une fuite.

**Message clé**

Les réponses de création, connexion ou récupération ne doivent pas permettre de déduire l'existence d'un compte.

**Situation**

Deux demandes de récupération sont envoyées avec deux adresses différentes. Le service fournit le même retour neutre.

**Risque**

Un tiers peut tester des adresses et identifier les comptes existants.

**Principe**

Utiliser des réponses neutres et homogènes.

**Règle / repère**

26. Aucune information n'est exposée sur l'existence d'un compte utilisateur.

**Scène visuelle**

Deux requêtes distinctes convergent vers une seule réponse identique. Une petite silhouette extérieure tente de déduire l'existence d'un compte mais ne reçoit aucun indice discriminant.

**Personnage ou objet-système**

Formulaire de récupération + deux identifiants + réponse commune.

**Transformation visible**

Réponses différentes et révélatrices -> réponse neutre commune.

**Textes visibles exacts**

Titre :
`Aider sans révéler si le compte existe`

Labels :
- `Adresse A`
- `Adresse B`
- `Même réponse`

Exemple de réponse neutre :
`Si un compte correspond à ces informations, les instructions ont été envoyées.`

Badge :
`26`

Callout :
`Informer l'utilisateur sans renseigner un attaquant.`

**Ce que l'image seule doit faire comprendre**

Deux cas différents produisent volontairement le même signal visible.

**Ajout / transition**

Après une fuite par en-tête, montre une fuite par message d'interface. La slide suivante traite les données sensibles pendant leur transmission.

**Discours oral**

Un message comme « cette adresse n'existe pas » paraît très précis et très serviable. Mais il renseigne aussi n'importe quelle personne qui teste des adresses. Le service doit rester utile sans révéler si un compte existe.

**Impact utilisateur**

Énumération de comptes et point de départ pour une tentative d'usurpation.

**Ce que la règle vise à garantir**

Des réponses qui n'exposent pas l'existence du compte.

**Mémo oral**

`Aider sans donner d'indice.`

**Contraintes critiques**

- le message affiché est un exemple pédagogique, pas une formulation officielle imposée ;
- la règle doit rester valable pour création, connexion et récupération de mot de passe ;
- ne pas utiliser « confidentialité absolue » ;
- ne pas afficher « e-mail déjà utilisé » comme bon exemple ;
- rouge uniquement sur le risque, jamais sur la réponse adaptée.

**Source officielle**

(API Opquast, règle n° 26, version qualite-numerique)

**Nom de fichier**

`slide-11-message-neutre-existence-compte.png`

---

# Slide 12 - Les données sensibles doivent circuler sans s'exposer

**Rôle narratif**

Clore la famille de protection technique.

**Message clé**

Les échanges sensibles doivent être protégés et signalés comme tels, et les données sensibles doivent rester hors des URL.

**Situation**

Une personne envoie un formulaire contenant une donnée sensible.

**Risque**

Interception sur le réseau ou conservation de la donnée dans l'URL, l'historique, les logs ou des services tiers.

**Principe**

Sécuriser l'échange, le signaler à l'utilisateur et transmettre les données hors de l'URL.

**Règle / repère**

- 27 : échanges de données sensibles sécurisés et signalés comme tels ;
- 28 : données sensibles non transmises en clair dans les URL.

**Scène visuelle**

Une interface de formulaire :
- cadenas et `HTTPS` visibles ;
- flux protégé vers le serveur ;
- barre d'adresse propre sans donnée sensible ;
- la donnée passe dans le corps de la requête, pas dans l'URL.

**Personnage ou objet-système**

Utilisateur + formulaire sensible + navigateur + serveur.

**Transformation visible**

Donnée exposée -> échange chiffré, signal visible, URL propre.

**Textes visibles exacts**

Titre :
`Les données sensibles doivent circuler sans s'exposer`

Labels :
- `HTTPS`
- `Échange protégé`
- `URL sans donnée sensible`

Badges :
- `27`
- `28`

Callout :
`Sécuriser l'échange et le faire savoir.`

**Ce que l'image seule doit faire comprendre**

La donnée est protégée pendant le transport et ne fuit pas dans l'adresse web.

**Ajout / transition**

Clôt les règles techniques de protection. La slide suivante montre que leur mise en œuvre est collective.

**Discours oral**

Cette partie contient deux idées. D'abord, les données sensibles doivent être protégées pendant leur transmission et l'utilisateur doit pouvoir savoir qu'il se trouve dans un contexte sécurisé. Ensuite, ces données ne doivent pas apparaître dans l'URL, qui circule et laisse des traces à de nombreux endroits.

**Impact utilisateur**

Interception, stockage ou diffusion involontaire de données sensibles.

**Ce que les règles visent à garantir**

Protection des échanges, confiance dans le contexte de saisie et confidentialité des données hors URL.

**Mémo oral**

`Chiffrer. Signaler. Garder l'URL propre.`

**Contraintes critiques**

- règle 27 : montrer les deux dimensions, protection et signalement ;
- règle 28 : aucune donnée sensible visible dans l'URL ;
- ne pas écrire qu'une méthode POST suffit à rendre un échange sécurisé ;
- ne pas écrire « sécurité absolue » ;
- aucun mot de passe réel ou crédible affiché.

**Sources officielles**

(API Opquast, règles n° 27 et 28, version qualite-numerique)

**Nom de fichier**

`slide-12-echanges-sensibles-securises-url-propre.png`

---

# Slide 13 - La protection des données est une responsabilité collective

**Rôle narratif**

Montrer la responsabilité collective sans transformer la slide en organigramme.

**Message clé**

Plusieurs métiers interviennent sur **la même expérience utilisateur**.

**Situation**

Un parcours de compte passe de la conception à la construction, puis à l'information et à l'accompagnement.

**Risque**

Chaque métier pense que la protection des données relève d'un autre acteur, en particulier du seul DPO.

**Principe**

Montrer des contributions complémentaires autour d'un parcours unique.

**Règle / repère**

Synthèse métiers et VPTCS issue des sources de travail. Ce n'est pas une règle Opquast unique.

**Scène visuelle**

Une **seule trajectoire utilisateur horizontale** traverse trois zones, sans cinq colonnes et sans cinq portraits.

Zone 1 :
`Concevoir`
Chips secondaires : `Design` · `Produit`

Zone 2 :
`Construire`
Chip secondaire : `Développement`

Zone 3 :
`Informer · accompagner`
Chips secondaires : `Contenus` · `DPO`

L'utilisateur et son compte restent au centre de la trajectoire. Les métiers sont des contributeurs autour du parcours, jamais des silos séparés.

**Personnage ou objet-système**

Un utilisateur + un parcours de compte + trois zones de contribution.

**Transformation visible**

Sujet renvoyé à un métier -> responsabilités complémentaires autour du même parcours.

**Textes visibles exacts**

Titre :
`La protection des données est une responsabilité collective`

Zones :
- `Concevoir`
- `Construire`
- `Informer · accompagner`

Chips secondaires :
- `Design`
- `Produit`
- `Développement`
- `Contenus`
- `DPO`

Callout :
`Une expérience, plusieurs responsabilités.`

**Ce que l'image seule doit faire comprendre**

La protection des données résulte de contributions différentes sur un parcours unique.

**Ajout / transition**

Recompose les règles en responsabilités opérationnelles. La slide suivante fait appliquer la méthode sur des situations concrètes.

**Discours oral**

La protection des données mobilise plusieurs métiers. Le développeur agit sur les flux et les comptes, le designer sur les parcours et les messages, le rédacteur sur l'information, le Product Owner sur les exigences du produit, et le DPO apporte son expertise et son accompagnement sur la protection des données. VPTCS aide à cartographier ces responsabilités sans les enfermer dans des silos.

**Impact utilisateur**

Des angles morts apparaissent lorsque chacun pense que le sujet appartient à un autre.

**Ce que l'approche vise à garantir**

Une prise en charge continue et partagée des risques liés aux données.

**Mémo oral**

`Une expérience, plusieurs responsabilités.`

**Contraintes critiques**

- trois zones visuelles seulement ;
- les cinq métiers sont des chips secondaires, pas cinq colonnes ;
- ne pas représenter le DPO comme supérieur hiérarchique ou garant unique de la conformité ;
- ne pas réduire le développeur au seul HTTPS ;
- ne pas classer rigidement chaque règle dans une lettre VPTCS ;
- pas de jargon QSE-IP visible sur cette slide.

**Source de travail**

`Metiers-profils-données-personnelles(1).md` et `VPTCS(1).md`.

**Nom de fichier**

`slide-13-responsabilite-collective-donnees-personnelles.png`

---

# Slide 14 - Cas pratiques

**Rôle narratif**

Application et préparation certification.

**Message clé**

Partir du préjudice et de la garantie permet de retrouver la règle.

**Situation**

Cinq mini-cas sont proposés comme exercices originaux de formation.

**Risque**

Chercher immédiatement un numéro de règle sans comprendre la situation.

**Principe**

Pour chaque cas : situation -> préjudice -> garantie -> règle.

**Règle / repère**

Règles mobilisées : 17, 18, 20, 26, 28.

**Scène visuelle**

Une grille très légère de cinq **vignettes iconographiques**, sans phrase explicative longue.

Organisation recommandée :
- trois vignettes sur la première ligne ;
- deux vignettes centrées sur la seconde ligne.

Chaque vignette contient seulement une lettre, une micro-interface et un libellé de deux à quatre mots.

**Personnage ou objet-système**

Cinq micro-situations d'usage.

**Transformation visible**

Cas concret -> questionnement utilisateur -> règle retrouvable à l'oral.

**Textes visibles exacts**

Titre :
`Cas pratiques`

Sous-titre :
`Quel préjudice ? Quelle garantie ?`

Vignettes :
- `A · Tiers obligatoire`
- `B · Sans confirmation`
- `C · Sortie par courrier`
- `D · Compte révélé`
- `E · Donnée dans l'URL`

Note :
`Exercices originaux de formation`

Callout :
`D'abord le préjudice, ensuite le numéro.`

**Ce que l'image seule doit faire comprendre**

Cinq situations problématiques sont à analyser, sans donner la correction à l'écran.

**Ajout / transition**

Met en pratique la méthode. La dernière slide regroupe les quinze règles autour de trois questions mémorisables.

**Discours oral**

Ne cherchez pas immédiatement le numéro. Pour chaque situation, demandez d'abord ce que l'utilisateur subit, puis ce que le service devrait préserver. Le numéro vient ensuite.

**Impact utilisateur**

Sans cette méthode, on retient des réponses mais pas la logique qui permet de les retrouver.

**Ce que l'exercice vise à garantir**

Une mémorisation par compréhension des risques.

**Mémo oral**

`D'abord le préjudice, ensuite le numéro.`

**Contraintes critiques**

- exactement cinq vignettes ;
- aucun numéro de règle visible dans les vignettes ;
- aucune correction complète visible ;
- préciser `Exercices originaux de formation` ;
- ne jamais présenter ces cas comme questions officielles d'examen ;
- priorité absolue au test des trois secondes.

**Nom de fichier**

`slide-14-cas-pratiques-donnees-personnelles.png`

---

# Slide 15 - Je comprends, je maîtrise, je protège

**Rôle narratif**

Synthèse et conclusion.

**Message clé**

Les quinze règles peuvent être mémorisées à travers trois questions utilisateur.

**Situation**

La même personne retrouve les trois axes de la slide d'ouverture, enrichis par les quinze règles.

**Risque**

Finir avec une liste de quinze numéros sans structure mémorisable.

**Principe**

Regrouper pédagogiquement les règles par enjeu utilisateur.

**Règle / repère**

Regroupement pédagogique, non classement officiel Opquast.

**Scène visuelle**

Trois grands piliers ou cartes autour de l'utilisateur :
- Comprendre ;
- Maîtriser ;
- Protéger.

Les numéros de règles sont lisibles mais secondaires.

**Personnage ou objet-système**

Utilisateur au centre + trois piliers.

**Transformation visible**

Quinze règles isolées -> trois questions mémorisables.

**Textes visibles exacts**

Titre :
`Je comprends, je maîtrise, je protège`

Carte 1 :
`Je comprends`
`15 · 16 · 29`

Carte 2 :
`Je maîtrise mon compte et mes contenus`
`17 · 18 · 19 · 20 · 21 · 22 · 23 · 24`

Carte 3 :
`Je protège mes informations`
`25 · 26 · 27 · 28`

Note :
`Regroupement pédagogique, non classement officiel Opquast`

Callout :
`Quel préjudice ? Que cherche à garantir la règle ?`

**Ce que l'image seule doit faire comprendre**

Toute la rubrique revient à trois besoins utilisateur : comprendre, garder la main, protéger les informations.

**Ajout / transition**

Referme la boucle avec la slide 1.

**Discours oral**

Si vous ne retenez qu'une structure, posez trois questions. Est-ce que je comprends ce que le service fait de mes données ? Est-ce que je garde la maîtrise de mon compte et de mes contenus ? Est-ce que mes informations restent protégées quand elles circulent ? Les numéros viennent ensuite.

**Impact utilisateur**

Sans ces règles, l'utilisateur peut ne plus savoir, ne plus maîtriser ou ne plus protéger ses données.

**Ce que les règles visent à garantir**

Une information accessible, une maîtrise effective du compte et des contenus, et une réduction des risques d'exposition des données.

**Mémo oral**

`Je comprends. Je garde la main. Je limite l'exposition.`

**Contraintes critiques**

- les quinze règles doivent apparaître exactement une fois dans les trois groupes ;
- groupe 1 : 15, 16, 29 ;
- groupe 2 : 17, 18, 19, 20, 21, 22, 23, 24 ;
- groupe 3 : 25, 26, 27, 28 ;
- la note `Regroupement pédagogique, non classement officiel Opquast` est obligatoire ;
- pas de nouvelle règle transversale sur la slide finale.

**Nom de fichier**

`slide-15-comprendre-maitriser-proteger.png`

---

# Matrice de couverture des règles

| Règle | Slide principale | Enjeu |
|---|---:|---|
| 15 | 03 | Politique de confidentialité accessible |
| 16 | 03 | Procédure d'accès et de rectification |
| 17 | 05 | Accès sans identification tierce obligatoire |
| 18 | 06 | Confirmation de création |
| 19 | 06 | Prévention de l'usurpation |
| 20 | 08 | Fermeture du compte |
| 21 | 08 | Sauvegarde des contenus personnels |
| 22 | 07 | Mêmes identifiants pour les services proposés |
| 23 | 09 | Déconnexion des espaces privés |
| 24 | 09 | Alias e-mail avec + |
| 25 | 10 | Politique de referrers |
| 26 | 11 | Non-exposition de l'existence d'un compte |
| 27 | 12 | Échanges sensibles sécurisés et signalés |
| 28 | 12 | Données sensibles hors URL |
| 29 | 03 | Objectif des cookies et conséquences du refus |

**Contrôle de couverture : 15 règles sur 15.**

---

# Annexe 1 - Privacy au-delà de la rubrique

## Statut de l'annexe

Cette annexe fait partie du **même module**, mais elle est séparée du deck principal par une rupture visuelle et une pagination propre.

Elle présente une **sélection de règles transversales liées à la vie privée** dans les rubriques E-Commerce et Newsletter :
- 30 ;
- 33 ;
- 59 ;
- 60 ;
- 173 ;
- 174 ;
- 175 ;
- 176.

Cette sélection ne doit pas être présentée comme une liste exhaustive de toutes les règles portant le tag API `Privacy`.

La règle 33 est incluse pour sa proximité pédagogique avec le libre choix et le consentement dans le parcours d'achat ; elle n'est pas présentée comme portant nécessairement le tag API `Privacy`.

---

# Annexe 1 · Slide A1-01 - La privacy dépasse la rubrique

**Rôle narratif**

Ouvrir la vision transversale après la conclusion du deck principal.

**Message clé**

Les risques liés à la vie privée réapparaissent dans d'autres moments du parcours : acheter, mémoriser un moyen de paiement, s'abonner ou se désabonner.

**Situation**

La même personne quitte la rubrique « Données personnelles » et poursuit son parcours dans deux autres univers : E-Commerce et Newsletter.

**Risque**

Croire que les enjeux de vie privée s'arrêtent aux règles 15 à 29.

**Principe**

Suivre les préjudices utilisateurs au-delà des frontières des rubriques.

**Règle / repère**

Sélection transversale :
- E-Commerce : 30, 33, 59, 60 ;
- Newsletter : 173, 174, 175, 176.

**Scène visuelle**

Au centre, un utilisateur issu du deck principal. Deux chemins s'ouvrent :
- `E-Commerce` : panier, compte, moyen de paiement ;
- `Newsletter` : inscription, message reçu, désinscription.

Les numéros de règles sont secondaires.

**Personnage ou objet-système**

Même utilisateur + parcours d'achat + parcours newsletter.

**Transformation visible**

Rubrique isolée -> vision transversale de la privacy.

**Textes visibles exacts**

Titre :
`La privacy dépasse la rubrique`

Branches :
- `E-Commerce`
- `Newsletter`

Repères :
- `30 · 33 · 59 · 60`
- `173 · 174 · 175 · 176`

Callout :
`Suivre le préjudice, pas seulement la rubrique.`

**Ce que l'image seule doit faire comprendre**

La protection de la vie privée continue dans les parcours d'achat et d'abonnement.

**Discours oral**

La rubrique Données personnelles s'arrête à la règle 29, mais les risques pour l'utilisateur ne s'arrêtent pas là. Dans l'achat et les newsletters, on retrouve les mêmes questions : est-ce que je choisis vraiment ? Est-ce que mes données sont mémorisées avec mon accord ? Est-ce que je peux sortir facilement ?

**Impact utilisateur**

Perte de choix, mémorisation non souhaitée ou difficulté à se désengager.

**Ce que cette annexe vise à montrer**

La continuité des exigences utilisateur entre plusieurs rubriques du référentiel.

**Mémo oral**

`La privacy traverse les parcours.`

**Contraintes critiques**

- annoncer explicitement qu'il s'agit d'une annexe transversale ;
- ne pas fusionner ces règles avec la rubrique officielle 15 à 29 ;
- ne pas présenter la sélection comme exhaustive ;
- deux branches seulement : E-Commerce et Newsletter.

**Nom de fichier**

`annexe-1-slide-01-privacy-au-dela-rubrique.png`

---

# Annexe 1 · Slide A1-02 - Acheter sans compte, choisir les services ajoutés

**Rôle narratif**

Montrer la maîtrise de l'utilisateur au moment de l'achat.

**Message clé**

L'achat doit pouvoir se faire sans compte et les services annexes ne doivent pas être activés par défaut.

**Situation**

Une personne arrive au paiement. Deux choix sont visibles :
- `Acheter sans compte` ;
- `Créer un compte`.

Une option annexe facultative est présente mais non cochée.

**Risque**

Création de compte imposée ou service annexe ajouté sans véritable choix.

**Principe**

Lever la barrière du compte et laisser l'utilisateur activer lui-même les services annexes.

**Règle / repère**

- 30 : achat possible sans création de compte ;
- 33 : inscription à des services annexes non activée par défaut.

**Scène visuelle**

Un checkout simple :
- deux chemins équivalents vers la commande ;
- une case facultative vide `Ajouter le service`.

La scène doit montrer le choix, pas un formulaire complet.

**Personnage ou objet-système**

Acheteur + étape de commande.

**Transformation visible**

Compte obligatoire et option préactivée -> achat direct et option réellement choisie.

**Textes visibles exacts**

Titre :
`Acheter sans compte, choisir les services ajoutés`

Actions :
- `Acheter sans compte`
- `Créer un compte`

Option :
`Ajouter le service`

Badges :
- `30`
- `33`

Callout :
`Je peux acheter sans compte. Rien n'est ajouté sans moi.`

**Ce que l'image seule doit faire comprendre**

Le compte et le service annexe sont des choix, pas des obligations cachées.

**Discours oral**

Deux barrières peuvent retirer du contrôle à l'acheteur : l'obligation de créer un compte avant de commander et l'ajout par défaut d'un service annexe. Les règles 30 et 33 redonnent l'initiative à l'utilisateur.

**Impact utilisateur**

Abandon de commande, collecte de données supplémentaire ou engagement involontaire.

**Ce que les règles visent à garantir**

Un achat direct possible et un vrai choix pour les services annexes.

**Mémo oral**

`Acheter sans compte. Rien ajouter sans moi.`

**Contraintes critiques**

- la case du service annexe est vide ;
- ne pas écrire que tout achat doit être anonyme ;
- ne pas supprimer la possibilité de créer un compte : elle reste une option ;
- la règle 33 est présentée comme règle E-Commerce liée au libre choix, sans lui attribuer abusivement un tag API.

**Sources officielles**

(API Opquast, règles n° 30 et 33, version qualite-numerique)

**Nom de fichier**

`annexe-1-slide-02-achat-sans-compte-opt-in.png`

---

# Annexe 1 · Slide A1-03 - Ma carte n'est mémorisée que si je le choisis

**Rôle narratif**

Prolonger la maîtrise sur les données bancaires.

**Message clé**

La mémorisation d'un moyen de paiement demande un consentement explicite et l'utilisateur doit pouvoir ensuite modifier ou supprimer les données mémorisées.

**Situation**

Une personne paie. Une option non cochée propose la mémorisation du moyen de paiement. Plus tard, dans son compte, elle peut modifier ou supprimer ce moyen mémorisé.

**Risque**

Mémorisation non souhaitée ou impossibilité de revenir sur son choix.

**Principe**

Consentement explicite à l'entrée, maîtrise dans la durée.

**Règle / repère**

- 59 : données bancaires mémorisées seulement après consentement explicite ;
- 60 : données bancaires mémorisées modifiables ou supprimables.

**Scène visuelle**

Un flux en deux temps :
1. paiement avec case vide `Mémoriser ce moyen de paiement` ;
2. espace compte avec actions `Modifier` et `Supprimer`.

Aucun numéro de carte complet.

**Personnage ou objet-système**

Acheteur + moyen de paiement + espace compte.

**Transformation visible**

Mémorisation implicite -> choix explicite -> possibilité de changer d'avis.

**Textes visibles exacts**

Titre :
`Ma carte n'est mémorisée que si je le choisis`

Option :
`Mémoriser ce moyen de paiement`

Actions :
- `Modifier`
- `Supprimer`

Badges :
- `59`
- `60`

Callout :
`Je choisis de mémoriser. Je peux changer d'avis.`

**Ce que l'image seule doit faire comprendre**

Le consentement ne suffit pas au moment initial : la maîtrise doit continuer après la mémorisation.

**Discours oral**

Mémoriser un moyen de paiement peut être pratique, mais ce choix doit venir de l'utilisateur. Et ce choix ne doit pas être irréversible : les données mémorisées doivent pouvoir être modifiées ou supprimées.

**Impact utilisateur**

Mémorisation bancaire non souhaitée, risque accru en cas de données obsolètes ou impossibilité de retirer ces informations.

**Ce que les règles visent à garantir**

Consentement explicite et maîtrise durable des données bancaires mémorisées.

**Mémo oral**

`Je choisis. Je peux changer d'avis.`

**Contraintes critiques**

- case de mémorisation non cochée par défaut ;
- aucune donnée bancaire complète ou réaliste à l'écran ;
- ne pas suggérer qu'un simple consentement rend la mémorisation sans risque ;
- montrer la modification et la suppression, pas seulement la consultation.

**Sources officielles**

(API Opquast, règles n° 59 et 60, version qualite-numerique)

**Nom de fichier**

`annexe-1-slide-03-memorisation-donnees-bancaires.png`

---

# Annexe 1 · Slide A1-04 - Newsletter : confirmer pour entrer, sortir simplement

**Rôle narratif**

Clore l'annexe par le cycle complet d'abonnement et de désabonnement.

**Message clé**

L'entrée dans une newsletter demande une confirmation ; la sortie doit rester accessible depuis chaque newsletter et depuis le site, sans imposer un nouvel e-mail de confirmation.

**Situation**

Une personne s'inscrit à une newsletter, confirme son adresse, reçoit un message puis décide plus tard de se désinscrire.

**Risque**

Inscription par un tiers, erreur d'adresse, absence de voie de sortie ou désinscription inutilement compliquée.

**Principe**

Confirmer l'entrée et simplifier la sortie.

**Règle / repère**

- 173 : inscription soumise à un processus de confirmation ;
- 174 : lien de désinscription dans chaque newsletter ;
- 175 : désinscription depuis une newsletter sans demande de confirmation par courriel ;
- 176 : désinscription possible depuis le site.

**Scène visuelle**

Un seul cycle horizontal :

`Inscription`
-> `Confirmation`
-> `Newsletter`
-> deux sorties :
  - `Lien de désinscription`
  - `Depuis le site`

Sous la sortie depuis la newsletter, petit repère :
`Pas d'e-mail de confirmation supplémentaire`

**Personnage ou objet-système**

Abonné + boîte mail + site.

**Transformation visible**

Entrée non vérifiée et sortie difficile -> entrée confirmée et deux voies de désinscription simples.

**Textes visibles exacts**

Titre :
`Newsletter : confirmer pour entrer, sortir simplement`

Étapes :
- `Inscription`
- `Confirmation`
- `Newsletter`

Sorties :
- `Se désinscrire`
- `Depuis le site`

Repère :
`Pas d'e-mail de confirmation supplémentaire`

Badges discrets :
- `173`
- `174`
- `175`
- `176`

Callout :
`Confirmer l'entrée. Faciliter la sortie.`

**Ce que l'image seule doit faire comprendre**

L'inscription est vérifiée, mais la désinscription ne doit pas devenir un parcours d'obstacles.

**Discours oral**

À l'entrée, la confirmation évite qu'un tiers inscrive une adresse à l'insu de son propriétaire ou qu'une erreur de saisie passe inaperçue. À la sortie, le lien doit être présent dans chaque newsletter, la désinscription doit aussi être possible depuis le site et, depuis le lien reçu, on ne doit pas imposer un nouvel e-mail de confirmation. Une confirmation en ligne peut toutefois être utilisée pour éviter une désinscription involontaire.

**Impact utilisateur**

Spam subi, inscription erronée ou difficulté à arrêter les envois.

**Ce que les règles visent à garantir**

Une inscription confirmée et une sortie accessible, effective et sans étape e-mail inutile.

**Mémo oral**

`Confirmer pour entrer. Pouvoir sortir simplement.`

**Contraintes critiques**

- ne pas écrire `double opt-in` comme libellé de la règle 173 ;
- la règle 175 interdit la demande de confirmation **par courriel**, pas nécessairement une confirmation en ligne ;
- le lien de désinscription doit apparaître dans la newsletter ;
- montrer aussi une voie de désinscription depuis le site ;
- ne pas présenter la désinscription comme forcément automatique au premier clic.

**Sources officielles**

(API Opquast, règles n° 173 à 176, version qualite-numerique)

**Nom de fichier**

`annexe-1-slide-04-newsletter-confirmation-desinscription.png`

---

# Matrice de couverture - Annexe 1

| Règle | Slide annexe | Thématique | Enjeu |
|---|---:|---|---|
| 30 | A1-02 | E-Commerce | Acheter sans création de compte |
| 33 | A1-02 | E-Commerce | Services annexes non activés par défaut |
| 59 | A1-03 | E-Commerce | Consentement explicite pour mémoriser les données bancaires |
| 60 | A1-03 | E-Commerce | Modifier ou supprimer les données bancaires mémorisées |
| 173 | A1-04 | Newsletter | Confirmation de l'inscription |
| 174 | A1-04 | Newsletter | Lien de désinscription dans chaque newsletter |
| 175 | A1-04 | Newsletter | Pas de confirmation par courriel pour se désinscrire depuis la newsletter |
| 176 | A1-04 | Newsletter | Désinscription possible depuis le site |

**Contrôle de couverture de l'annexe : 8 règles sur 8 de la sélection définie.**

---

# Processus de génération à appliquer

## 1. Préflight

Avant toute image :

- relire ce storyboard ;
- charger le guide de style de la série « Images et médias » ;
- conserver le masque commun défini ici ;
- vérifier les textes critiques ;
- créer le dossier projet de sortie.

## 2. Génération imagegen-first

- générer **une seule slide à la fois** avec `image_gen` ;
- commencer uniquement par la slide 01 ;
- inspecter la slide 01 avant de générer la suite ;
- produire et valider les 15 slides principales avant de lancer l'Annexe 1 ;
- générer ensuite les 4 slides de l'Annexe 1 avec le même masque, mais leur footer et leur pagination propres ;
- une slide = un appel ;
- ne jamais produire une planche composite comme source finale.

## 3. Test des trois secondes

Pour chaque candidate, une personne extérieure doit pouvoir identifier rapidement :

- qui agit ;
- quel objet matérialise le problème ;
- ce qui change ;
- pourquoi c'est utile.

Si ce test échoue, la slide est à reprendre avant la suite.

## 4. Inspection de chaque slide

Vérifier :

- titre exact ;
- règle correcte ;
- préjudice correct ;
- garantie correcte ;
- texte exact ;
- pagination ;
- hiérarchie ;
- lisibilité ;
- absence de texte parasite ;
- couleurs sémantiques ;
- stabilité du masque ;
- absence de faux logo.

## 5. Reprise ciblée avec `prompt-image`

Utiliser `prompt-image` uniquement lorsqu'une candidate est presque correcte mais présente un défaut.

La reprise doit toujours contenir :

1. défaut observé ;
2. invariants à préserver ;
3. correction visuelle attendue ;
4. interdits.

Ne pas régénérer les slides déjà validées.

## 6. Usage de `chain-of-summaries-cos`

Ne pas industrialiser COS.

L'utiliser uniquement si une slide devient trop dense ou ambiguë, en priorité :

- slide 13, responsabilité collective ;
- slide 14, cas pratiques ;
- éventuellement slide 03 si les trois règles deviennent trop textuelles.

Le résumé doit rester fondé sur les sources et ne pas ajouter de règle ou de garantie non documentée.

## 7. Contact sheet

Après validation des quinze PNG principaux :

- créer une première contact sheet du deck principal ;
- vérifier le rythme global ;
- contrôler la variation des compositions ;
- réinspecter au moins une slide pleine résolution par famille de layout.

Après validation de l'Annexe 1 :

- créer une seconde contact sheet spécifique aux 4 slides annexes ;
- vérifier que la rupture `ANNEXE 1` est immédiatement perceptible sans casser la cohérence de série.

## 8. Packaging

Seulement après validation des PNG :

- exporter les prompts ;
- tenir le reçu `imagegen-receipt.tsv` ;
- créer le PPTX 16:9 avec une image pleine page par slide si demandé ;
- vérifier **15 slides principales + 4 slides d'Annexe 1 = 19 slides** si l'annexe est incluse dans l'export ;
- produire le rapport QA.

## 9. ShipGuard

ShipGuard peut auditer :

- storyboard ;
- Markdown ;
- manifestes ;
- structure du projet.

Il ne valide pas à lui seul la qualité graphique des PNG.

---

# Familles de layout recommandées

Pour éviter une série monotone tout en conservant le masque :

- Slides 01 et 15 : synthèse en trois axes.
- Slides 02, 06, 10 et 12 : progression horizontale.
- Slides 03, 09 et 13 : cartes structurées autour d'une scène centrale.
- Slides 05, 07 et 08 : transformation avant / action / après.
- Slide 04 : parcours chronologique en trois moments.
- Slide 11 : convergence de deux cas vers une réponse neutre.
- Slide 14 : grille de cinq cas pratiques.
- A1-01 : bifurcation simple vers E-Commerce et Newsletter.
- A1-02 : choix au checkout.
- A1-03 : flux en deux temps consentement -> gestion.
- A1-04 : cycle horizontal inscription -> confirmation -> sortie.

---

# Checklist QA pré-génération

- [x] Périmètre officiel 15 à 29 identifié.
- [x] 15 règles couvertes.
- [x] Regroupements pédagogiques explicitement qualifiés.
- [x] Préjudice utilisateur présent pour chaque slide de règle.
- [x] Garantie recherchée présente pour chaque slide de règle.
- [x] Formulations sensibles 16, 18, 21, 23, 27 et 28 revérifiées.
- [x] VPTCS conservé comme cadre transversal, pas comme taxonomie officielle.
- [x] Métiers intégrés comme responsabilité collective.
- [x] Règles transversales exclues du deck principal et intégrées séparément en Annexe 1.
- [x] Annexe 1 : 8 règles transversales sélectionnées, contrôlées via l'API.
- [x] Colonne vertébrale PDS en cinq étapes.
- [x] Masque commun défini.
- [x] Textes visibles exacts définis.
- [x] Contraintes critiques définies.
- [x] Noms de fichiers définis.
- [ ] Slide 01 générée et inspectée.
- [ ] Slides 02 à 15 générées et inspectées.
- [ ] Annexe 1, slides A1-01 à A1-04, générées et inspectées.
- [ ] Prompts exportés et audités.
- [ ] Contact sheet créée et inspectée.
- [ ] PPTX vérifié si demandé.
