# Conversation Opquast — Performance

> Transcription des échanges visibles consacrés à la thématique performance.
> Les messages système, instructions internes et appels d’outils ne sont pas inclus.

---

## Utilisateur

J'aimerai qu'on lance le meme prompt amélioré et la même méthodologie pour la thématique performance

---

## Assistant

Oui. Je reprends **exactement la même logique**, en réutilisant tout ce qu’on a déjà cadré : candidats Opquast aux profils variés, niveau intermédiaire, objectif compréhension + mémorisation + certification, narration par grappes de risques utilisateur, avec un second niveau organisationnel.

Je vais adapter seulement ce qui doit l’être : pour la performance, le fil conducteur devient **temps perdu, attente, surconsommation de données, instabilité et accès dégradé au service**, sans transformer Opquast en cours de Web Performance spécialisé.

Même limite que pour la sécurité : la checklist étendue complète dépasse la taille maximale de l’API. Je vais donc appliquer la même méthode robuste : **repérage dans le corpus complet, puis vérification individuelle des règles officielles via l’API**.

Premier repère : la rubrique officielle **« Serveur et performances » couvre les règles 218 à 230**. Mais, comme pour la sécurité, toute la rubrique n’est pas de la performance pure : le noyau performance semble surtout se concentrer sur compression, cache et minification. Je vais justement distinguer **rubrique**, **performance directe** et **effets transversaux**.

Un résultat structurant apparaît déjà : **« Serveur et performances » n’est pas synonyme de « performance »**. Les règles 218 à 225 parlent surtout d’accès, robots, sitemap, erreurs et continuité de navigation. Le noyau directement consacré à la performance est beaucoup plus resserré : **226 compression, 227 cache, 229 CSS minifié, 230 JavaScript minifié**, avec **119** sur les images surdimensionnées comme règle transversale très directe.

Cela va nous éviter un piège classique de certification : apprendre toute la rubrique 13 comme un bloc « performance ».

---

## Utilisateur

ok continue

---

## Assistant

La frontière devient nette : **Opquast distingue bien performance technique et maîtrise de la consommation par l’utilisateur**. La règle 119 réduit directement les octets inutiles. Les règles 147 et 148, elles, n’accélèrent pas forcément le service, mais elles permettent à l’utilisateur de décider s’il veut déclencher un téléchargement coûteux, notamment en bas débit ou en mobilité.

Je complète encore les règles périphériques médias et la doctrine générale avant de te livrer la cartographie complète.

La recherche est maintenant assez mûre pour une conclusion comparable à celle sur la sécurité. Le point central sera différent : **performance Opquast ≠ “faire un bon score Lighthouse”**. Le livre définit la performance par la taille des pages, le temps pour rendre le service utilisable et le confort des interactions, puis précise qu’une vraie démarche performance dépasse largement l’inspection des quelques règles Opquast.

# Deep research Opquast : performance à 360°

J'ai repris le même cadrage que pour la sécurité, sans te refaire les questions : **candidats à la certification Opquast, profils numériques variés, niveau intermédiaire, compréhension + mémorisation + certification, organisation par risques et situations utilisateur, utilisateur au centre et organisation au second plan**.

Même limite technique que précédemment : l'appel API de la checklist complète est trop volumineux. J'ai donc repéré les règles dans le corpus, puis vérifié individuellement les règles structurantes via l'API Opquast, version `qualite-numerique`.

## 1. La conclusion centrale

Le livre donne une définition particulièrement utile :

> La performance vise à réduire la taille globale des pages, rendre les sites et applications utilisables le plus rapidement possible et améliorer la vitesse et le confort des interactions.

Il ajoute un élément essentiel : les outils spécialisés mesurent plusieurs moments différents, comme l'arrivée des données, l'affichage, le moment où la page devient manipulable et la fin du téléchargement.

Pour notre futur storyboard, je traduirais donc la doctrine Opquast ainsi :

> **La performance Opquast, c'est éviter de faire attendre, calculer ou télécharger inutilement l'utilisateur.**

Ce n'est pas une formulation officielle, mais elle est très fidèle au corpus.

Et surtout :

> **Une page qui semble rapide n'est pas nécessairement légère. Une page légère n'est pas nécessairement rapidement utilisable.**

Cette distinction est fondamentale.

---

# 2. Premier piège : « Serveur et performances » n'est pas « les règles de performance »

La rubrique officielle **Serveur et performances** couvre les règles **218 à 230**, soit 13 règles.

Mais toutes ne traitent pas directement de performance.

| Règle | Sujet principal |
|---|---|
| 218 | adresse avec/sans www |
| 219 | robots.txt |
| 220 | sitemap |
| 221 | redirection mobile |
| 222 | vrai code HTTP 404 |
| 223 | page 404 personnalisée |
| 224 | page 403 personnalisée |
| 225 | navigation dans les pages d'erreur |
| **226** | **compression** |
| **227** | **cache** |
| 228 | charset dans les entêtes |
| **229** | **minification CSS** |
| **230** | **minification JavaScript** |

Les formulations 218 à 230 ont été vérifiées via l'API actuelle.

Conclusion pour la certification :

> **Rubrique Serveur et performances ≠ 13 règles de performance.**

Le noyau directement performance de cette rubrique est surtout :

**226 + 227 + 229 + 230.**

Et une règle de performance extrêmement importante se trouve ailleurs :

**119**, dans Images et médias.

---

# 3. Le noyau dur : cinq règles à apprendre ensemble

## 119 : ne pas télécharger une énorme image pour en afficher une petite

> **« Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client. »**

(API Opquast, règle n° 119, version `qualite-numerique`)

Exemple :

Une image originale fait :

`5000 × 5000 px`

mais on l'affiche :

`150 × 150 px`

avec CSS ou HTML.

Visuellement, l'utilisateur voit une petite image.

Mais il peut toujours avoir téléchargé **l'énorme fichier original**.

C'est précisément ce que la règle cherche à éviter. Le livre rattache explicitement 119 à la diminution des données téléchargées, à la vitesse d'affichage et à l'impact énergétique.

### Préjudice utilisateur

Connexion lente : attente.

Forfait limité : données consommées inutilement.

Mobile ancien : traitement inutile d'une ressource disproportionnée.

### Mémo

> **119 = envoyer l'image dont j'ai réellement besoin.**

Ou, plus mémorable :

> **Petit à l'écran doit aussi pouvoir être petit à télécharger.**

---

# 4. 226 : compresser avant d'envoyer

> **« Le serveur transmet des contenus compressés aux clients qui les acceptent. »**

(API Opquast, règle n° 226, version `qualite-numerique`)

Le principe est simple.

Au lieu d'envoyer :

`HTML / CSS / JS volumineux`

le serveur compresse ces ressources et le navigateur les décompresse automatiquement.

L'API cite Gzip et Deflate. Le livre cite également Brotli dans son explication actuelle. Le bénéfice : moins de données transférées, rendu plus rapide, bande passante réduite.

Attention : on ne recompresse pas mécaniquement tout. JPEG, PNG, ZIP et autres formats déjà compressés ne gagnent pas nécessairement à être compressés à nouveau.

### Image mentale

Tu dois envoyer une grosse couverture dans une boîte.

**226 = mettre la couverture sous vide avant le transport.**

### Mémo

> **226 = moins d'octets pendant le transport.**

---

# 5. 227 : ne pas retélécharger ce que l'on possède déjà

> **« Le serveur envoie les informations permettant la mise en cache des contenus. »**

(API Opquast, règle n° 227, version `qualite-numerique`)

Le principe est différent de 226.

226 rend **un téléchargement plus léger**.

227 cherche à **éviter certains téléchargements ultérieurs**.

Une image, un CSS ou un JavaScript déjà récupéré peut être conservé localement par le navigateur.

À la page suivante ou lors d'une nouvelle visite, il n'est pas forcément nécessaire de tout récupérer depuis zéro.

Le glossaire définit justement le cache navigateur comme la conservation locale d'une ressource pour éviter son nouveau téléchargement.

L'API cite notamment :

- `Cache-Control`
- `ETag`
- `Last-Modified`
- `Expires`
- réponse `304 Not Modified`

### Image mentale

226 :

> Je transporte **moins lourd**.

227 :

> Je ne transporte **pas une deuxième fois ce que tu possèdes déjà**.

### Piège certification

**Compression ≠ cache.**

C'est probablement la paire la plus importante du chapitre.

> **226 = réduire le transfert.**  
> **227 = éviter le retransfert.**

---

# 6. 229 et 230 : supprimer ce qui ne sert pas à l'exécution

### 229

> **« Les feuilles de styles internes sont minifiées. »**

(API Opquast, règle n° 229, version `qualite-numerique`)

### 230

> **« Les scripts internes sont minifiés. »**

(API Opquast, règle n° 230, version `qualite-numerique`)

La minification supprime notamment :

- espaces inutiles ;
- retours à la ligne ;
- indentations ;
- commentaires ;
- autres caractères inutiles à l'interprétation.

Le glossaire définit la minification comme une réduction des fichiers CSS et JavaScript au code strictement nécessaire au moteur, avec pour effets une moindre bande passante et de meilleures performances de téléchargement.

### Attention à la différence avec 226

Une confusion possible :

**Minifier ≠ compresser.**

Exemple conceptuel :

```text
Code lisible développeur
↓
MINIFICATION
Code plus compact
↓
COMPRESSION HTTP
Flux encore plus petit pendant le transport
```

Donc :

> **229-230 réduisent le fichier lui-même.**  
> **226 réduit le volume transmis sur le réseau.**

Les deux sont complémentaires.

### Mémo

**229 = CSS maigre**  
**230 = JS maigre**

---

# 7. La première grande grappe pédagogique

Nous avons donc une chaîne extrêmement mémorisable :

### « Ne me fais pas télécharger plus que nécessaire »

**119** : ressource image adaptée.  
**229** : CSS minifié.  
**230** : JS minifié.  
**226** : transmission compressée.  
**227** : ne pas retransmettre inutilement.

On peut même raconter le trajet dans cet ordre :

> **Je choisis la bonne ressource → je la minifie → je la compresse → je la mets en cache.**

C'est beaucoup plus puissant pédagogiquement qu'apprendre cinq règles séparément.

---

# 8. Performance perçue et poids réel ne sont pas la même chose

C'est probablement l'apport historique le plus intéressant du corpus Opquast.

Dans l'article **« Performance Web : 1 Méga, c'est beaucoup »**, publié le 15 juin 2015, Élie Sloïm souligne qu'une page de plusieurs mégaoctets peut être extrêmement bien optimisée et paraître rapide.

Mais :

> un mégaoctet reste un mégaoctet.

Pour un utilisateur dans un train, dans le métro, dans une zone mal couverte ou à l'étranger, ce volume peut devenir long, coûteux, voire impraticable.

La conclusion de l'article est particulièrement structurante :

> les sites ne doivent pas seulement être configurés pour être délivrés rapidement, ils doivent aussi être légers.

### Pour la certification

Il faut distinguer :

**vitesse apparente**  
et  
**volume réellement transféré**.

Une optimisation peut donner une sensation de rapidité sans supprimer le coût des données.

---

# 9. Deuxième distinction : téléchargement ≠ temps avant utilisation

L'article **« Pages web : tous au régime »**, du 2 avril 2013, ajoute une autre dimension.

Historiquement, le problème était surtout :

> attendre que le document soit téléchargé.

Avec les interfaces modernes, le document peut commencer à apparaître rapidement, mais l'utilisateur doit encore attendre que JavaScript, CSS et autres traitements soient exécutés avant de pouvoir réellement agir.

Donc :

```text
Téléchargement
      ↓
Affichage
      ↓
Calcul / exécution
      ↓
Interface réellement utilisable
```

La performance utilisateur ne se résume donc pas au premier affichage.

Le livre 2026 reprend cette logique en distinguant différentes mesures : arrivée des données, affichage complet, possibilité de manipuler la page, téléchargement terminé.

---

# 10. La performance est aussi un problème de contexte utilisateur

Un ordinateur récent en fibre optique peut masquer beaucoup de défauts.

Opquast insiste historiquement sur les utilisateurs :

- en mobilité ;
- en bas débit ;
- dans des zones mal couvertes ;
- sur mobile ;
- en roaming ;
- équipés de terminaux moins puissants.

Le livre explique qu'une quantité excessive de données peut directement nuire **à l'expérience et au portefeuille** de l'utilisateur.

C'est important pour notre narration.

Le préjudice utilisateur n'est pas seulement :

> « ma page met 1,2 seconde de plus ».

Il peut être :

> « je ne peux pratiquement pas utiliser le service ».

ou :

> « ce service consomme une part importante de mon forfait de données ».

---

# 11. Règles transversales : informer avant de faire consommer

Nous retrouvons ici plusieurs règles situées hors de la rubrique Serveur et performances.

## 148 : annoncer le poids d'un téléchargement

> **« La taille des fichiers internes proposés en téléchargement est indiquée. »**

(API Opquast, règle n° 148, version `qualite-numerique`)

Elle ne rend pas le fichier plus léger.

Elle donne **la maîtrise à l'utilisateur**.

Un utilisateur en connexion mobile ou bas débit peut décider :

- de télécharger maintenant ;
- d'attendre le Wi-Fi ;
- de reporter ;
- de ne pas télécharger.

L'objectif officiel mentionne explicitement l'information préventive sur la quantité de données et la possibilité de différer en bas débit ou mobile.

### Distinction clé

> **119 réduit réellement le volume.**  
> **148 informe l'utilisateur du volume avant qu'il décide.**

Les deux traitent le même risque sous deux angles différents.

---

# 12. 147 : éviter le téléchargement inutile

> **« Le format des fichiers proposés en téléchargement est indiqué. »**

(API Opquast, règle n° 147, version `qualite-numerique`)

Pourquoi est-ce connexe à la performance ?

Parce qu'un utilisateur qui télécharge un fichier qu'il ne peut pas ouvrir vient :

- de perdre son temps ;
- de consommer des données ;
- de provoquer une requête et un transfert inutiles.

L'objectif officiel mentionne explicitement :

> réduire la charge serveur en évitant les téléchargements inutiles.

### Paire pédagogique

> **147 = qu'est-ce que je vais télécharger ?**  
> **148 = combien vais-je télécharger ?**

---

# 13. 123 : combien de temps vais-je consacrer à ce média ?

> **« La durée des contenus vidéo ou audio est indiquée. »**

(API Opquast, règle n° 123, version `qualite-numerique`)

Ce n'est pas une règle de performance technique.

Mais elle appartient au même système de décision utilisateur.

Une vidéo de 2 minutes et une vidéo de 90 minutes ne demandent pas le même engagement.

L'objectif officiel est que l'utilisateur puisse décider en connaissance de cause de **consulter ou télécharger** le contenu.

Donc :

**148 = poids numérique à engager**  
**123 = temps humain à engager**

C'est une très belle connexion pédagogique.

---

# 14. 124 : ne pas faire partir une grosse consommation sans décision

> **« Les vidéos sont déclenchées par l’utilisateur. »**

(API Opquast, règle n° 124, version `qualite-numerique`)

Le cœur officiel porte surtout sur le contrôle, l'intrusion et l'accessibilité.

Mais l'explication Opquast mentionne explicitement l'envoi de **grandes quantités de données sans accord explicite** lorsque les vidéos démarrent automatiquement.

Donc la performance est ici un effet transversal réel.

### Situation utilisateur

J'ouvre une page.

Je voulais lire trois lignes.

Une vidéo démarre.

Je viens de consommer des données que je n'ai jamais demandé à recevoir.

### Mémo

> **124 = ne pas consommer à ma place.**

---

# 15. Et les règles 125 et 126 ?

Il faut rester précis.

### 125, sons déclenchés par l'utilisateur

Elle relève principalement du contrôle utilisateur et de l'accessibilité.

Elle porte aussi le tag `Écoconception`, mais son objectif officiel n'est pas de faire de la performance.

### 126, animations, sons et clignotements mis en pause

Même chose : le sujet principal est le contrôle et l'accessibilité, pas la performance. `(API Opquast, règles n° 125 et 126, version qualite-numerique)`

Donc je les mettrais en **périphérie**, pas dans le noyau du module performance.

C'est exactement le type de distinction qui évite de diluer notre sujet.

---

# 16. Carte des niveaux de pertinence

Cette classification est analytique, pas officielle.

| Niveau | Règles | Raisonnement |
|---|---|---|
| **Performance directe** | **119, 226, 227, 229, 230** | Réduire directement données, transfert ou temps de chargement |
| **Maîtrise de la consommation utilisateur** | **123, 124, 147, 148** | Décider avant de consommer temps ou données |
| **Performance / sobriété indirecte** | **218, 219, 220, 222** | Éviter certains parcours ou traitements inutiles, objectifs écoconception explicites |
| **Rubrique Serveur mais pas performance** | **221, 223, 224, 225, 228** | Compatibilité, erreurs, navigation, encodage |
| **Périphérie** | **125, 126 et diverses règles d'efficacité des parcours** | Gains indirects possibles, mais performance non centrale |

---

# 17. Les « faux amis » de la rubrique Serveur et performances

Pour la certification, je ferais apprendre ceci explicitement.

### 223 n'est pas une règle de performance

> page 404 personnalisée.

Elle rassure l'utilisateur et explique que sa connexion n'est pas en cause. `(API Opquast, règle 223)`

### 224 n'est pas une règle de performance

> page 403 personnalisée.

Même logique autour d'un accès interdit.

### 225 n'est pas une règle de performance

> menu principal sur les pages d'erreur.

C'est une règle de continuité de navigation.

### 228 n'est pas une règle de performance

> charset dans les entêtes.

Elle concerne essentiellement la fiabilité de l'affichage et la compatibilité.

Donc :

> **Le nom de la rubrique décrit une famille de sujets serveur, pas une taxonomie stricte de performance.**

---

# 18. Compression, minification, cache : trois choses différentes

C'est probablement le trio technique qu'il faudra le plus travailler.

## Minification

On transforme :

```css
.card {
    margin: 10px;
    padding: 20px;
}
```

en quelque chose de plus compact :

```css
.card{margin:10px;padding:20px}
```

Le contenu fonctionnel reste le même.

**But : fichier source plus petit.**

## Compression

Ce fichier est ensuite compressé lors de son transport HTTP.

**But : moins de données circulent sur le réseau.**

## Cache

Après réception, le navigateur garde éventuellement le fichier.

Lors d'une utilisation suivante :

**But : ne pas avoir à le transférer à nouveau.**

### Mémo

> **Minifier = enlever le gras du fichier.**  
> **Compresser = serrer le fichier pendant le voyage.**  
> **Cacher = éviter de refaire le voyage.**

Pour un public de profils variés, cette métaphore fera probablement beaucoup de travail pédagogique.

---

# 19. Le glossaire montre que la performance est un système

Les termes importants ne sont pas seulement « cache » et « minification ».

Le glossaire Serveur et performances contient notamment :

**Client web** : celui qui demande et exploite les ressources.

**Serveur** : celui qui répond et transmet les ressources.

**Ressource** : HTML, CSS, JavaScript, image, etc., téléchargés séparément.

**Ressource tierce** : ressource venant d'un autre serveur, comme un script, une police ou une régie.

**Contenu compressé** : ressource texte compressée avant transmission.

**Cache navigateur** : conservation locale d'une ressource.

**Minification** : suppression de ce qui n'est pas nécessaire à l'exécution.

**Site statique / dynamique** : deux modes de production ayant des profils de ressources serveur différents.

Le livre ajoute encore :

- lazy loading ;
- CDN ;
- caches serveur ;
- sites statiques ;
- optimisation de l'hébergement.

Mais ces notions ne deviennent pas automatiquement des règles Opquast.

---

# 20. Pourquoi Opquast ne contient-il pas « un bon LCP doit être inférieur à X » ?

C'est une question passionnante pour comprendre le référentiel.

Opquast écarte volontairement les règles reposant sur :

- des seuils numériques arbitraires ;
- des technologies susceptibles d'évoluer ;
- des critères trop contextuels ;
- des exigences difficiles à rendre universelles.

Le livre explique explicitement que les règles Opquast ne doivent normalement pas contenir de valeur numérique arbitraire et doivent rester universelles et durables.

Cela explique pourquoi le référentiel contient :

> « transmettre des contenus compressés »

mais pas nécessairement :

> « votre page doit obtenir 96/100 à tel outil ».

### C'est capital

**Opquast fixe des fondamentaux.**

**La performance spécialisée mesure, compare et optimise.**

---

# 21. Opquast n'est pas un référentiel complet de Web Performance

Comme pour la cybersécurité, cette limite doit apparaître dans la présentation.

Le livre est explicite :

> l'essentiel des bénéfices d'une vraie démarche d'amélioration des performances ne vient pas simplement du déploiement des règles Opquast en inspection, mais d'une véritable démarche de mesure et d'optimisation portant sur les contenus, l'hébergement et les pratiques de développement.

Et plus généralement, Opquast explique que performance, sécurité, accessibilité ou SEO peuvent être approfondis quasiment sans limite par des approches spécialisées. Le référentiel constitue un **socle transversal**, pas un remplacement des experts.

Donc :

> **Connaître Opquast ne fait pas de vous un spécialiste WebPerf.**

Mais cela évite à un professionnel généraliste de passer à côté de fondamentaux comme :

- images disproportionnées ;
- absence de compression ;
- absence de cache ;
- CSS et JS inutilement volumineux ;
- téléchargements imposés ou imprévisibles.

---

# 22. Performance et écoconception : très liées, mais pas synonymes

C'est une distinction qu'il faudra maintenir.

Le livre présente la performance comme une composante essentielle de l'écoconception.

Et les règles :

- 119 ;
- 226 ;
- 227 ;
- 229 ;
- 230

sont toutes reliées à l'écoconception dans les sources consultées.

Mais :

> **améliorer la performance n'équivaut pas automatiquement à écoconcevoir l'ensemble du service.**

Le livre présente l'écoconception comme beaucoup plus large : visibilité, perception, technique, contenus, services et cycle de vie du service numérique.

Pour notre module performance :

**écoconception = bénéfice transversal majeur**, mais pas sujet principal.

---

# 23. Performance et accessibilité

Le recouvrement est surtout contextuel.

Un service très lourd peut pénaliser :

- une personne utilisant un appareil ancien ;
- quelqu'un en connexion instable ;
- un utilisateur en mobilité ;
- un utilisateur disposant de ressources matérielles limitées.

Opquast insiste historiquement sur ces contextes d'usage et sur les publics souvent oubliés, notamment les utilisateurs en bas débit.

Les règles 123, 147 et 148 portent d'ailleurs également le tag accessibilité.

Le message pédagogique n'est donc pas :

> « performance = accessibilité ».

Mais :

> **une mauvaise performance peut créer ou aggraver des situations d'exclusion.**

---

# 24. Performance, SEO et business

Le livre rappelle que le temps d'affichage influence le taux de conversion et que la performance est également prise en compte par les moteurs de recherche.

Mais pour notre présentation, je conserverais ces effets **en second niveau**.

Le centre doit rester :

> **l'expérience et le préjudice utilisateur.**

Sinon on retombe vite dans :

> « faites de la performance pour Google ».

Ce n'est pas la logique Opquast que nous cherchons à transmettre.

---

# 25. Une lecture VPTCS de la performance

Ceci est une **cartographie pédagogique**, pas un classement officiel.

### Visibilité

La performance peut influencer la visibilité via le référencement et le fonctionnement des moteurs.

Les règles 219 et 220 réduisent également certains parcours inutiles des robots.

### Perception

Un service lent paraît moins fluide et moins maîtrisé.

Une interface qui apparaît mais reste longtemps inutilisable dégrade fortement la qualité perçue.

### Technique

C'est le noyau :

**119, 226, 227, 229, 230**

plus les techniques spécialisées de chargement, CDN, architecture, etc.

### Contenus

Le poids et la nature des contenus déterminent une grande partie du volume :

- images ;
- vidéo ;
- audio ;
- documents ;
- scripts ou widgets éditoriaux tiers.

### Services

Un parcours inutilement long ou composé de trop d'allers-retours peut coûter du temps, du réseau et des traitements.

Le livre distingue d'ailleurs les règles à impact performance direct de celles qui produisent indirectement **des expériences rapides et efficaces avec peu d'allers-retours**.

---

# 26. L'histoire Opquast de la performance

Il y a une vraie continuité.

### 2010 : la performance devient un sujet essentiel du référentiel

Lors de la V2, Opquast explique avoir ajouté ou renforcé des sujets essentiels, dont **sécurité et performance**.

### 2013 : le problème n'est déjà plus seulement le téléchargement

Dans **« Pages web : tous au régime »**, Opquast insiste sur :

- poids HTML ;
- CSS ;
- JavaScript ;
- temps de traitement ;
- délai avant que la page devienne réellement manipulable ;
- machines et connexions réelles des utilisateurs.

### 2015 : « 1 Méga, c'est beaucoup »

Le discours ajoute une distinction fondamentale entre :

**optimisation du temps d'affichage**

et

**quantité réelle de données transférées**.

### 2020 : la performance devient explicitement transversale

Les contenus sur les tags Opquast présentent performance, accessibilité, sécurité ou mobile comme des axes transversaux que l'on peut croiser avec les règles et les phases projet.

### 2026 : performance dans la qualité numérique globale

Le livre replace la performance dans :

- UX ;
- écoconception ;
- SEO ;
- qualité logicielle ;
- assurance qualité ;
- optimisation spécialisée.

Et surtout il fixe clairement la frontière entre **socle Opquast** et **démarche WebPerf experte**.

---

# 27. Les principales confusions à préparer pour la certification

1. **Rubrique Serveur et performances ≠ uniquement performance.**
2. **119 est une règle majeure de performance mais se trouve dans Images et médias.**
3. **226 compression ≠ 227 cache.**
4. **229/230 minification ≠ 226 compression.**
5. **119 réduit réellement le poids, 148 informe seulement sur le poids avant téléchargement.**
6. **147 évite notamment des téléchargements inutiles en informant sur le format.**
7. **123 informe sur la durée, pas sur le poids du média.**
8. **124 donne le contrôle du déclenchement de la vidéo, avec un bénéfice transversal sur les données consommées.**
9. **Une page rapide peut malgré tout transférer énormément de données.**
10. **Une page rapidement affichée peut rester longtemps inutilisable.**
11. **Performance ≠ écoconception**, même si les deux se recouvrent fortement.
12. **Opquast ≠ audit WebPerf spécialisé.**

---

# 28. Les grappes de risques que je recommande pour le storyboard

Je vois déjà une structure beaucoup plus forte que « règles 218 à 230 ».

## Grappe « A » : je télécharge trop

Préjudice :

- attente ;
- forfait consommé ;
- page impraticable en connexion faible.

Règles :

**119, 226, 229, 230**

Question mentale :

> **Est-ce que tout ce que je reçois est réellement nécessaire ?**

## Grappe « B » : je retélécharge inutilement

Règle centrale :

**227**

Question :

> **Pourquoi me renvoyer ce que mon navigateur possède déjà ?**

## Grappe « C » : le site décide de consommer à ma place

Règles :

**123, 124, 147, 148**

Logique :

- dis-moi combien de temps ;
- dis-moi quel fichier ;
- dis-moi combien il pèse ;
- laisse-moi décider quand déclencher une vidéo.

Question :

> **Puis-je décider avant de payer le coût en temps ou en données ?**

## Grappe « D » : ça s'affiche, mais ce n'est toujours pas utilisable

Ici, on sort partiellement des règles individuelles pour expliquer le concept de performance numérique.

Le problème peut venir :

- du réseau ;
- du nombre de ressources ;
- du JavaScript ;
- du calcul ;
- de l'appareil ;
- des services tiers.

## Grappe « E » : ma fibre masque les problèmes de mes utilisateurs

C'est la grappe contexte.

Situations :

- train ;
- métro ;
- roaming ;
- réseau faible ;
- appareil ancien ;
- données mobiles limitées.

Le message :

> **Ne testez pas la qualité uniquement dans les conditions confortables de l'équipe qui produit le service.**

---

# 29. La phrase centrale que je proposerais

Pour la sécurité, nous avions :

> **Sécurité Opquast = prévenir un préjudice utilisateur.**

Pour la performance, je proposerais :

> **Performance Opquast = ne pas faire attendre, télécharger ou calculer inutilement l'utilisateur.**

Et une deuxième phrase très mémorisable :

> **Rapide n'est pas forcément léger, affiché n'est pas forcément utilisable.**

Cette deuxième phrase permet d'expliquer presque toute la philosophie du chapitre.

---

# 30. La carte mentale de révision

```text
PERFORMANCE OPQUAST

        Ce que je télécharge
               │
       ┌───────┴───────┐
       │               │
     poids           transferts
       │               │
   119 images       226 compression
   229 CSS          227 cache
   230 JS
       │
       ▼
moins de données
       │
       ▼
moins d'attente
moins de coût réseau
meilleure expérience

+ maîtrise utilisateur

123 durée média
124 vidéo volontaire
147 format fichier
148 taille fichier
```

Et autour :

```text
Performance
   ↕
UX
   ↕
Accessibilité contextuelle
   ↕
Écoconception
   ↕
SEO
   ↕
Coûts d'infrastructure
```

Mais **sans confondre ces disciplines**.

---

## Conclusion de la recherche

La sécurité nous avait conduit à :

> **prévenir des risques de sécurité qui deviennent des préjudices utilisateur.**

La performance conduit à un raisonnement parallèle :

> **prévenir les coûts inutiles imposés à l'utilisateur : temps d'attente, quantité de données, traitements et perte de fluidité.**

Et le corpus Opquast ajoute deux nuances essentielles :

> **Une bonne performance ne consiste pas seulement à afficher vite.**

> **Les quelques règles Opquast constituent un socle. L'optimisation WebPerf réelle nécessite ensuite mesure, expertise et amélioration continue.**

Pour le storyboard d'une heure, je partirais donc non pas de « Serveur et performances », mais de **l'utilisateur qui paie la performance avec trois monnaies : son temps, ses données et les ressources de son terminal**. C'est, à mon sens, notre meilleur fil narratif.

---

## Utilisateur

je peux avoir un md à télécharger de toute notre conversation sur la performance
