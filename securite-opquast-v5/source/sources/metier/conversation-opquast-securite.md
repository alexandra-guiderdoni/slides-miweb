# Conversation Opquast — Sécurité

> Transcription des échanges visibles entre l’utilisateur et l’assistant.
> Les messages système, instructions internes et appels d’outils ne sont pas inclus.

---

## Utilisateur

Je veux tout savoir de manière exhaustive sur la thematique securite dans opquast. Périmètre thematique securite mais aussi périmètre transversale a 360. Pour se faire tu fais une deep recherche sur le corpus opquast regle glossaire livre blog etc de maniere a ce qu’on ait une couverture complète. Une fois realise on en fera un storybord. Ameliore mon prompt avant de lancer la deep recherche et cuisine moi interroge moi puis cuisine et interroge opquast

---

## Assistant

Je vais d’abord verrouiller le cahier des charges de la recherche, sans encore lancer l’extraction. L’objectif est d’éviter une étude « sécurité = quelques règles techniques » et de couvrir aussi confiance, données, authentification, transactions, dépendances, organisation, tests et impacts utilisateur.

Oui. Avant de lancer la recherche, je veux transformer ta demande en un vrai protocole d’enquête. Le point décisif sera de ne pas confondre « rubrique Sécurité » et « vision Opquast de la sécurité ». Le livre lui-même présente la cybersécurité comme un risque transversal, relié aux utilisateurs, aux données, aux organisations, aux tests et à la qualité globale. Le glossaire montre déjà des connexions vers HTTPS, HSTS, intégrité, 2FA, données sensibles, referrers, espaces privés, ressources tierces, HTTP et d’autres notions hors de la seule rubrique Sécurité.

### Prompt de recherche amélioré

#### Deep research Opquast 360° sur la sécurité

Réalise une recherche approfondie, systématique et traçable sur la place de la SÉCURITÉ dans l’écosystème Opquast.

L’objectif n’est PAS de résumer uniquement la rubrique ou le tag « Sécurité ». Il faut reconstruire la vision Opquast de la sécurité à 360°, depuis les exigences utilisateur jusqu’aux règles techniques, aux données personnelles, aux processus métier, à la qualité logicielle, au management des risques et aux interactions avec les autres disciplines de la qualité numérique.

## 1. Corpus à interroger

Travaille prioritairement sur l’ensemble des sources Opquast accessibles :

1. Référentiel officiel Opquast Qualité numérique, version `qualite-numerique`.
2. Livre « Qualité et conformité des services numériques », 4e édition.
3. Glossaire Opquast complet et glossaire par thématique.
4. Corpus des articles, éditos et newsletters Opquast.
5. Autres ressources Opquast disponibles dans le corpus fourni.

Ne complète avec des connaissances générales ou des sources Web externes que si cela est explicitement nécessaire pour comprendre une limite ou un écart. Dans ce cas, sépare strictement :
- ce qu’affirme Opquast ;
- ce qui constitue une interprétation ;
- ce qui provient d’une source externe.

## 2. Méthode obligatoire pour les règles

Commence par interroger la checklist complète afin d’identifier les règles explicitement ou implicitement reliées à la sécurité.

Ne te limite surtout pas au mot-clé « sécurité ».

Explore notamment les notions et situations suivantes :
authentification, mot de passe, récupération de compte, changement de mot de passe, double facteur, identité, espace privé, autorisation, données sensibles, confidentialité, chiffrement, HTTPS, HTTP, certificats, HSTS, intégrité, fichiers téléchargés, types MIME, scripts, ressources tierces, CSP, referrers, cookies, formulaires sensibles, paiement, transaction, courrier électronique, fraude, phishing, domaine de messagerie, session, suppression de données, sauvegarde de données, erreurs serveur, robots.txt, disponibilité, déni de service, validation côté serveur, services tiers, dépendances, qualité logicielle, tests de sécurité et gestion des risques.

Pour chaque règle retenue comme significative, récupère ensuite sa fiche officielle avec `getRuleByNumber`, version `qualite-numerique`.

La formulation officielle et les métadonnées de l’API font référence pour la règle.

## 3. Trois niveaux de périmètre

Classe les découvertes selon trois cercles.

### Sécurité explicite : cercle A

Règles, termes, passages ou articles explicitement consacrés à la cybersécurité ou à la protection contre des attaques, interceptions, usurpations, compromissions ou altérations.

### Sécurité fonctionnelle et utilisateur : cercle B

Règles dont l’objectif premier n’est pas forcément nommé « sécurité », mais qui diminuent un risque pour l’utilisateur ou augmentent sa maîtrise :
- authentification ;
- récupération de compte ;
- maîtrise de ses données ;
- prévention des erreurs ;
- confirmation d’actions sensibles ;
- transactions ;
- téléchargement ;
- espaces privés ;
- fraude ;
- confiance ;
- identification de l’émetteur ;
- information avant une opération sensible.

### Sécurité systémique et organisationnelle : cercle C

Contenus Opquast reliant la sécurité à :
- l’assurance qualité ;
- la conformité ;
- le management des risques ;
- QSE-IP ;
- la qualité logicielle ;
- DevSecOps ;
- tests et audits ;
- dépendances à des services tiers ;
- maintenance ;
- gestion de parc ;
- dette technique ;
- IA et production de code ;
- organisation et compétences ;
- prévention plutôt que correction.

Ne qualifie pas automatiquement ces éléments de « règles de sécurité ». Explique précisément leur relation avec la sécurité.

## 4. Pour chaque règle pertinente

Documente systématiquement :

**Numéro et formulation officielle**

**Rubrique / tags / métadonnées disponibles**

**Pourquoi cette règle appartient au périmètre sécurité**
Préciser s’il s’agit d’un lien direct, indirect ou transversal.

**Situation utilisateur**
Décrire une situation concrète où le problème apparaît.

**Préjudice utilisateur**
Que peut perdre ou subir concrètement l’utilisateur ?

Exemples de catégories à examiner sans les imposer :
perte de confidentialité, usurpation d’identité, fraude, perte de données, action non désirée, blocage de compte, exposition d’informations, compromission d’un terminal, impossibilité d’accéder au service, perte de confiance.

**Ce que garantit la règle**
Rester strictement fidèle aux objectifs Opquast. Ne pas promettre une sécurité absolue.

**Mécanisme**
Expliquer simplement comment la règle réduit le risque.

**Relations avec d’autres règles**
Identifier les grappes de règles qui fonctionnent ensemble.

**Vocabulaire Opquast associé**
Relier la règle aux définitions pertinentes du glossaire.

**Passages du livre associés**
Rechercher objectifs, explications, méthode, cybersécurité, qualité logicielle, conformité, VPTCS, QSE-IP, risques, tests et assurance qualité.

**Articles et newsletters associés**
Repérer les évolutions historiques, prises de position, exemples et retours d’expérience.

## 5. Recherche transversale dans le livre

Ne limite pas la recherche au chapitre « Cybersécurité ».

Explorer notamment :
- modèle VPTCS ;
- définition de la qualité numérique ;
- risques majeurs ;
- management intégré QSE-IP ;
- conformité et assurance qualité ;
- qualité logicielle ;
- tests de sécurité ;
- DevSecOps ;
- coûts de non-qualité ;
- accessibilité et sécurité lorsqu’elles interagissent ;
- données personnelles et sécurité ;
- écoconception lorsque la sécurité évite des opérations inutiles ;
- services tiers ;
- intelligence artificielle et qualité du code ;
- pilotage et organisation.

Chercher également les passages montrant les limites d’une checklist : ce qu’Opquast peut prévenir et ce qui exige une véritable démarche spécialisée de cybersécurité.

## 6. Glossaire

Construire une carte du vocabulaire.

Distinguer :

**Termes explicitement classés Sécurité**

puis

**Termes appartenant à d’autres catégories mais indispensables pour comprendre les enjeux de sécurité.**

Pour chaque terme :
- définition Opquast ;
- catégorie ;
- relation avec la sécurité ;
- règles associées ;
- éventuels pièges de compréhension.

## 7. Articles, éditos et newsletters

Rechercher toutes les occurrences significatives relatives à :
sécurité, cybersécurité, risques, vulnérabilités, données, hacking, DevSecOps, tests, qualité logicielle, IA, dette technique, conformité, QSE-IP, dépendances et prévention.

Ne pas simplement établir une bibliographie.

Pour chaque publication réellement utile :
- titre ;
- date ;
- auteur ;
- idée apportée ;
- articulation avec le référentiel ou le livre ;
- caractère historique ou toujours pertinent.

Identifier les évolutions de pensée d’Opquast dans le temps.

## 8. Cartographie VPTCS de la sécurité

Analyser comment la sécurité traverse :

**Visibilité**
Confiance, identité du service, liens, mails, exposition d’informations, robots, réputation.

**Perception**
Information donnée à l’utilisateur, compréhension d’une opération sensible, signaux de confiance, prévention des manipulations ou ambiguïtés.

**Technique**
HTTPS, HSTS, MIME, intégrité, headers, politiques navigateur, dépendances, serveurs, code, vulnérabilités.

**Contenus**
Informations sensibles, données personnelles, URL, documents téléchargés, messages de sécurité, mails.

**Services**
Comptes, authentification, transactions, paiements, récupération, suppression, sauvegarde, relation utilisateur après incident.

Indiquer lorsqu’une association est une interprétation analytique et non une classification officielle Opquast.

## 9. Cartographie par risques utilisateur

Regrouper les règles et contenus autour des principaux scénarios de préjudice :

- interception ;
- vol ou fuite de données ;
- usurpation ;
- compromission de compte ;
- fraude ;
- téléchargement malveillant ;
- exposition involontaire d’informations ;
- altération d’une ressource ;
- perte de données ;
- impossibilité d’accéder au service ;
- manipulation ou erreur sur une opération sensible ;
- utilisation abusive d’informations transmises à des tiers ;
- perte de contrôle par l’utilisateur.

Faire émerger les chaînes de défense constituées de plusieurs règles.

## 10. Frontières et angles morts

Cette partie est fondamentale.

Identifier explicitement :
- ce qu’Opquast couvre bien ;
- ce qu’Opquast effleure ;
- ce qu’Opquast ne prétend pas couvrir ;
- ce qui relève d’un référentiel ou d’une expertise cybersécurité spécialisée.

Ne pas transformer Opquast en référentiel de cybersécurité complet.

Chercher en particulier la frontière entre :
« prévenir certains risques élémentaires affectant l’utilisateur »
et
« sécuriser globalement un système d’information ».

## 11. Livrable final de recherche

Produire un dossier structuré comportant :

**A. Synthèse exécutive**
La vision de la sécurité selon Opquast en 10 à 15 idées fondamentales.

**B. Carte conceptuelle 360°**
Sécurité directe + dimensions transversales.

**C. Inventaire exhaustif des règles**
Avec classification direct / transversal / périphérique.

**D. Grandes familles de risques utilisateurs**

**E. Glossaire sécurité étendu**

**F. Apports du livre**

**G. Apports historiques des articles et newsletters**

**H. Articulation sécurité / données personnelles / accessibilité / qualité logicielle / conformité / UX / écoconception**

**I. Vision organisationnelle**
Prévention, compétences, tests, QA, QSE-IP, DevSecOps, management.

**J. Limites d’Opquast en matière de cybersécurité**

**K. Tensions, nuances et éventuelles évolutions du discours Opquast**

**L. Matière première pour storyboard**
Concepts forts, exemples utilisateurs, métaphores pédagogiques, règles emblématiques et regroupements narratifs possibles.

## 12. Exigence de traçabilité

Chaque affirmation importante doit être rattachée à sa source.

Utiliser lorsque possible :
(Livre, section « ... »)
(API Opquast, règle n° X, version qualite-numerique)
(Glossaire Opquast, terme « ... »)
(Article Opquast, « titre », date)

Ne jamais attribuer à Opquast une conclusion qui n’est qu’une inférence.

Les inférences utiles doivent être signalées explicitement comme telles.

## 13. Question centrale de l’enquête

Au terme de la recherche, répondre clairement à cette question :

« Quand Opquast parle de sécurité, cherche-t-il seulement à sécuriser techniquement un service numérique, ou cherche-t-il plus largement à préserver la maîtrise, les données, les actions, les intérêts et la confiance de l’utilisateur tout au long de son expérience numérique ? »

La réponse devra être démontrée par les sources et non supposée.

### Maintenant, je te cuisine

1. Qui regardera le storyboard final ?
2. Quel est ton objectif principal ?
3. Quelle place veux-tu donner à la technique ?
4. Veux-tu que je traite les règles de sécurité comme une “grappe” plutôt que règle par règle ?
5. Souhaites-tu que le centre narratif reste l’utilisateur ?
6. Doit-on intégrer le point de vue de l’organisation ?
7. Veux-tu une vraie section “Opquast n’est pas un référentiel cyber” ?
8. Jusqu’où veux-tu pousser le périmètre “transversal” ?
9. Faut-il intégrer sécurité + privacy ensemble, ou conserver une frontière très nette ?
10. Veux-tu inclure accessibilité et sécurité lorsque les exigences peuvent entrer en tension ?
11. Veux-tu que je recherche aussi les angles morts par rapport à la cybersécurité moderne ?
12. Pour les articles historiques, souhaites-tu une généalogie de la pensée Opquast ?
13. Quel format de storyboard envisages-tu ensuite ?
14. Enfin, quelle émotion intellectuelle veux-tu provoquer à la fin ?

---

## Utilisateur

Repose moi les questions une a une et j’y reponds

---

## Assistant

Commençons par la première.

**1. Qui est le public principal du futur storyboard ?**

Par exemple : candidats à la certification Opquast, certifiés, développeurs, designers UX/UI, PO/PM, chefs de projet, dirigeants, équipes cyber, ou public mixte ?

---

## Utilisateur

candidats à la certification Opquast tous dans le numérique profil divers

---

## Assistant

Parfait. Public cible retenu : **candidats à la certification Opquast, avec des profils numériques très variés**. Donc il faudra rester transversal, pédagogique et éviter de supposer un niveau technique homogène.

**2. Quel est l’objectif principal du storyboard ?**

Parmi ces directions, laquelle domine : **préparer à la certification**, **comprendre en profondeur la logique Opquast sur la sécurité**, **mémoriser les règles**, ou **les trois à la fois** ?

---

## Utilisateur

Les trois a la fois

---

## Assistant

Parfait. Objectif retenu : **comprendre la logique Opquast sur la sécurité, mémoriser les règles et préparer efficacement la certification**.

Cela veut dire que la recherche devra distinguer ce qu’il faut **comprendre**, ce qu’il faut **retenir**, et ce qui constitue un **piège classique de raisonnement**.

**3. Quel niveau technique veux-tu ?**

Plutôt :
- **accessible à tous**, même aux profils non techniques ;
- **intermédiaire**, avec explication simple de notions comme HTTPS, HSTS, CSP, MIME, 2FA, referrer ;
- **assez poussé**, avec mécanismes techniques détaillés quand ils aident à comprendre les règles.

Lequel ?

---

## Utilisateur

Intermédiaire

---

## Assistant

Parfait. Niveau retenu : **intermédiaire**, avec les notions techniques expliquées simplement, sans entrer dans un cours d’ingénierie sécurité.

**4. Pour le futur storyboard, préfères-tu une organisation règle par règle, ou plutôt par grandes grappes de risques et situations utilisateur ?**

Par exemple : « protéger un compte », « sécuriser une transaction », « éviter une fuite de données », puis rattacher plusieurs règles Opquast à chaque situation.

---

## Utilisateur

par grandes grappes de risques et situations utilisateur plus conforme a l’esprit opquast

---

## Assistant

Très bien. On retient donc une structure **par grappes de risques et situations utilisateur**, avec les règles Opquast rattachées ensuite. C’est plus cohérent avec une lecture par préjudices, exigences et maîtrise utilisateur.

**5. Veux-tu que le fil conducteur parte systématiquement du point de vue utilisateur ?**

Par exemple :  
« Que risque l’utilisateur ? » → « Quelle maîtrise lui manque ? » → « Quelles règles Opquast réduisent ce risque ? » → « Que faut-il retenir pour la certification ? »

Oui ou non ?

---

## Utilisateur

Oui

---

## Assistant

Parfait. Le fil conducteur sera donc **centré utilisateur** : préjudice → perte de maîtrise → règles Opquast pertinentes → bénéfice → point de mémorisation certification.

**6. Veux-tu qu’on intègre aussi le point de vue de l’organisation**, mais en second niveau seulement ?

Par exemple : intrusion, indisponibilité, coûts de non-qualité, sauvegardes, dette technique, gestion des incidents, compétences, tests, pilotage.

Ou préfères-tu rester presque exclusivement côté utilisateur ?

---

## Utilisateur

Oui

---

## Assistant

Très bien. On gardera donc **l’utilisateur au centre**, avec un second niveau consacré aux impacts organisationnels et à la prévention des risques.

**7. Veux-tu une section explicite : « Opquast n’est pas un référentiel de cybersécurité complet » ?**

Elle servirait à montrer clairement :
- ce qu’Opquast couvre ;
- ce qu’il couvre indirectement ;
- ce qui relève d’un référentiel cyber spécialisé ou d’une expertise dédiée.

Je la recommande fortement pour éviter toute confusion. Oui ou non ?

---

## Utilisateur

Oui

---

## Assistant

Parfait. On aura donc une section nette sur les **frontières du référentiel** : ce qu’Opquast couvre, ce qu’il contribue à prévenir, et ce qui exige une démarche cybersécurité spécialisée.

**8. Jusqu’où veux-tu pousser le périmètre transversal ?**

Option A : uniquement les règles avec un lien matériel évident avec la sécurité.

Option B : inclure aussi les notions de **confiance, transparence, contrôle, réversibilité, prévention des erreurs, maîtrise des actions et maîtrise des données**, dès lors qu’elles participent à la sécurité vécue par l’utilisateur.

A ou B ?

---

## Utilisateur

Je pense que a c’est mieux

---

## Assistant

Oui, je pense aussi que **A est plus solide pour la certification**. On évite de diluer la sécurité dans des notions trop larges comme la confiance ou la transparence, sauf lorsqu’un lien avec un risque de sécurité est clairement établi par les sources Opquast.

**9. Pour les données personnelles, veux-tu une frontière nette entre sécurité et privacy, ou veux-tu les traiter ensemble lorsqu’elles se recouvrent ?**

Par exemple, une fuite de données personnelles relève clairement des deux sujets, alors que le consentement aux cookies relève surtout des données personnelles.

Je te propose : **frontière nette, avec zones de recouvrement explicitement signalées**. Ça te va ?

---

## Utilisateur

En annexe parce que j’ai deja traite la privacy

---

## Assistant

Parfait. On mettra donc **privacy et données personnelles en annexe**, uniquement pour montrer les zones de recouvrement avec la sécurité, sans refaire ce que tu as déjà traité.

**10. Veux-tu intégrer les tensions entre sécurité et accessibilité**, par exemple autour des CAPTCHA, de l’authentification forte, de la récupération de compte ou de certains dispositifs de contrôle ?

Oui ou non ?

---

## Utilisateur

Oui

---

## Assistant

Très bien. On intégrera donc les **tensions sécurité / accessibilité** comme un axe transversal, mais seulement lorsqu’elles sont réellement documentées dans les sources Opquast.

**11. Veux-tu que j’identifie aussi les angles morts par rapport à la cybersécurité moderne ?**

Par exemple : gestion des secrets, vulnérabilités des dépendances, sessions, journalisation, patch management, réponse à incident, sauvegardes, passkeys, rate limiting.

L’idée ne serait pas d’ajouter des règles externes, mais de montrer clairement : **« Opquast couvre ceci, mais pas cela »**. Oui ou non ?

---

## Utilisateur

Non on reste transversal

---

## Assistant

Très bien. On reste **transversal mais centré sur Opquast**, sans comparer systématiquement avec tout le champ de la cybersécurité moderne.

**12. Veux-tu que je reconstruise l’évolution de la pensée Opquast sur la sécurité dans le temps ?**

Par exemple : règles qualité → prévention des risques → conformité → QSE-IP → qualité logicielle / DevSecOps → IA et maîtrise des productions.

Oui ou non ?

---

## Utilisateur

Oui

---

## Assistant

Très bien. On intégrera donc une **courte généalogie de la sécurité chez Opquast**, pour montrer comment le sujet s’inscrit progressivement dans une logique plus large de risques, conformité, qualité logicielle, QSE-IP et usages de l’IA, sans transformer cela en histoire générale de la cybersécurité.

**13. Quel format vises-tu pour le futur storyboard ?**

Par exemple : une présentation de **20 minutes**, **45 minutes**, **1 heure**, ou un **module de formation plus long** ?

---

## Utilisateur

1 h

---

## Assistant

Parfait. Format retenu : **1 heure**, donc assez de temps pour construire une progression pédagogique, travailler les grappes de risques, expliquer les règles emblématiques et réserver un temps de synthèse utile à la certification.

**14. À la fin de cette heure, quelle idée centrale veux-tu que le candidat garde en tête ?**

Je te propose trois formulations possibles :

A. **« La sécurité Opquast, c’est d’abord prévenir des risques concrets pour l’utilisateur. »**

B. **« La sécurité n’est pas seulement technique : elle traverse l’expérience utilisateur et plusieurs métiers du numérique. »**

C. **« Les règles Opquast forment un premier filet de prévention des risques, sans remplacer une démarche spécialisée de cybersécurité. »**

Tu peux choisir A, B, C, ou me donner ta propre formulation.

---

## Utilisateur

A

---

## Assistant

C’est cadré. Idée finale retenue : **« La sécurité Opquast, c’est d’abord prévenir des risques concrets pour l’utilisateur. »** Je passe maintenant à la recherche complète : référentiel officiel, livre, glossaire, puis articles et évolution historique.

L’appel à la checklist complète dépasse la taille maximale de réponse de l’API. Je ne vais donc pas prétendre l’avoir examinée entière par ce biais : je vais repérer les règles dans le corpus, puis vérifier individuellement leur formulation officielle avec l’API.

Premier résultat solide : la rubrique **Sécurité** du livre va de la règle **197 à la règle 215**, soit 19 règles explicites. J’ai aussi déjà repéré des règles hors rubrique qui touchent matériellement la sécurité, notamment 23, 25, 26, 27 et 28. Je vérifie maintenant les formulations officielles une par une.

Les 19 règles explicites sont maintenant vérifiées officiellement. Un point important apparaît déjà : la rubrique mêle **protection technique** et **continuité d’usage**. La règle 215, par exemple, sécurise une opération tout en exigeant une solution de secours pour ne pas bloquer l’utilisateur. Je cherche maintenant les règles transversales réellement matérielles, sans élargir artificiellement le périmètre.

La recherche transversale fait ressortir quatre règles supplémentaires que je ne veux pas laisser passer : confirmation de création de compte, prévention de l’usurpation, maîtrise des données bancaires et relance du double facteur. Elles sont rangées ailleurs que dans « Sécurité », mais leurs objectifs mentionnent explicitement usurpation, fraude ou authentification.

Le périmètre commence à se stabiliser en trois niveaux : **21 règles explicitement dans la rubrique Sécurité**, un noyau de règles transversales avec effet matériel sur usurpation, fraude ou authentification, puis quelques règles « satellites » dont la sécurité n’est qu’un effet secondaire. Cette distinction sera importante pour ne pas tout appeler abusivement « règle de sécurité ».

J’ai maintenant aussi l’évolution du référentiel : la sécurité entre explicitement comme sujet essentiel avec la V2 en 2010, la confidentialité est séparée en thématique « Données personnelles » en 2020, puis la V5 de 2025 ajoute notamment les règles 26, 96, 216 et 217. Cela confirme que la lecture transversale n’est pas un ajout artificiel de notre part : elle s’est renforcée dans le référentiel lui-même.

Une nuance de version importante ressort aussi : certains tags imprimés dans le livre ne correspondent pas exactement aux métadonnées actuelles renvoyées par l’API. Pour la certification, je retiendrai donc la formulation et les métadonnées API comme référence officielle, et le livre comme référence d’explication.

# Deep research Opquast : sécurité à 360°

La recherche est suffisamment stabilisée pour servir de base au storyboard d'une heure.

J'ai croisé quatre couches : le référentiel actuel via l'API Opquast, le livre 2026, le glossaire et le corpus de 514 articles/newsletters. Une limite méthodologique doit être signalée : l'appel de la checklist complète via l'API dépasse la taille de réponse autorisée. Je n'ai donc pas prétendu l'examiner intégralement par cette voie. J'ai repéré les règles dans le corpus complet, puis vérifié individuellement les règles retenues avec `getRuleByNumber`, version `qualite-numerique`.

## 1. La conclusion principale

Ta formulation finale est remarquablement bien soutenue par le corpus :

> **« La sécurité Opquast, c'est d'abord prévenir des risques concrets pour l'utilisateur. »**

Ce n'est pas une citation officielle d'Opquast, mais **une synthèse fidèle de l'approche documentée**.

Le livre place la cybersécurité parmi les grands risques du numérique. Côté organisation, il évoque les intrusions, pertes de données, fuites, coûts de correction et conséquences d'une absence de sauvegarde. Côté utilisateur, il cite les fuites de données, virus, arnaques, usurpations d'identité et détournements de données bancaires. Surtout, il précise que le référentiel couvre **des risques basiques** de sécurité et que la sécurité informatique est d'abord une affaire de prévention des risques.

Cette dernière précision est fondamentale pour la certification : **Opquast ne prétend pas produire un référentiel complet de cybersécurité**. Il fournit un socle généraliste de risques fondamentaux, transversal aux métiers, qui ne remplace pas les experts spécialisés.

Donc la bonne représentation mentale est :

**Opquast n'apprend pas à devenir expert cyber. Opquast apprend au professionnel du numérique à ne pas ignorer des risques de sécurité élémentaires susceptibles de porter préjudice à l'utilisateur.**

## 2. Le périmètre officiel : 21 règles « Sécurité »

Le livre confirme que la rubrique Sécurité compte **21 fiches**, et la rubrique suivante commence ensuite avec Serveur et performances.

J'ai vérifié individuellement les 21 formulations avec l'API. Les formulations suivantes sont donc celles de la version actuelle `qualite-numerique`.

| Règle | Formulation officielle | Risque utilisateur dominant |
|---|---|---|
| **197** | Toutes les pages utilisent le protocole HTTPS. | Interception et vol de données |
| **198** | Les certificats de sécurité sont signés et en cours de validité. | Connexion à un service dont l'identité ou la chaîne de confiance pose problème |
| **199** | Les pages utilisant HTTPS ont un entête de transport strict. | Interception avant établissement forcé d'une connexion sécurisée |
| **200** | Les pages utilisant le protocole HTTPS ne proposent pas de ressources HTTP. | Ressources non protégées dans une page supposée sécurisée |
| **201** | Les opérations relatives aux mots de passe peuvent être effectuées intégralement en ligne. | Blocage ou récupération de compte trop fragile ou trop complexe |
| **202** | Les mots de passe peuvent être choisis ou changés par l’utilisateur. | Mauvaise maîtrise de son moyen d'authentification |
| **203** | Un dispositif sensibilise l’utilisateur sur le degré de sécurisation du mot de passe qu’il choisit. | Choix d'un mot de passe insuffisamment robuste |
| **204** | Les mots de passe peuvent être réinitialisés. | Perte durable de l'accès au compte |
| **205** | Les mots de passe ne sont pas communiqués en clair. | Divulgation d'un secret d'authentification |
| **206** | Les entêtes envoyés par le serveur désactivent la détection automatique du type MIME de chaque ressource. | Fichier dangereux interprété sous une fausse nature |
| **207** | Le serveur indique le type MIME de chaque ressource. | Contenu dangereux dissimulé sous un autre type |
| **208** | Les informations sur la sécurité des transactions sont indiquées. | Utilisateur incapable d'évaluer les conditions de transmission de données sensibles |
| **209** | Le serveur n’envoie pas la liste des fichiers des répertoires n’ayant pas de page d’index. | Exposition inutile de fichiers ou ressources |
| **210** | Le serveur envoie les informations d’activation de protection cross site scripting. | Injection et exécution de contenu malveillant |
| **211** | Le serveur envoie les informations indiquant les domaines autorisés à intégrer ses pages dans des cadres. | Utilisation trompeuse du service, notamment détournement d'interface |
| **212** | Un mécanisme de sécurité restreint l’origine des contenus. | Exécution ou affichage provenant d'une source non autorisée |
| **213** | Le serveur ne communique pas d’informations sur les logiciels et langages utilisés. | Informations facilitant la préparation d'une attaque |
| **214** | Le contrôle d’intégrité des ressources tierces est présent et valide. | Exécution d'une ressource externe modifiée ou compromise |
| **215** | Les opérations sécurisées peuvent être validées par au moins deux moyens. | Impossible de réaliser une opération légitime faute du dispositif attendu |
| **216** | L’affichage de la barre d’adresse du navigateur n’est pas bloqué. | Phishing, usurpation de domaine, vol d'identifiants |
| **217** | Le domaine de messagerie est authentifié. | Faux courriel, phishing, usurpation du domaine |

Toutes : `(API Opquast, règles n° 197 à 217, version qualite-numerique)`.

Cette seule table révèle déjà quelque chose d'important : **la rubrique Sécurité n'est pas uniquement une collection de protections serveur**. Elle contient HTTPS, CSP, MIME ou SRI, mais également récupération de mot de passe, information de l'utilisateur, solution de secours pour une authentification forte, barre d'adresse et fiabilité du courrier électronique.

## 3. Les grandes grappes de risques

### Grappe 1 : « Je ne veux pas que mes échanges soient interceptés »

Règles 197, 198, 199 et 200.

**197 = HTTPS partout**  
**198 = certificat valide**  
**199 = forcer le transport sécurisé**  
**200 = aucune ressource HTTP dans la page HTTPS**

### Grappe 2 : « Je ne veux pas perdre le contrôle de mon compte »

Règles 201 à 205.

**201** : je dois pouvoir gérer mes opérations de mot de passe en ligne.

**202** : je dois pouvoir choisir ou changer mon mot de passe.

**203** : le service m'aide à percevoir son niveau de sécurisation.

**204** : si je le perds, je dois pouvoir le réinitialiser.

**205** : le service ne doit jamais me l'envoyer en clair.

## 4. La sécurité du compte dépasse la rubrique Sécurité

Plusieurs règles rangées dans d'autres rubriques ont un lien matériel direct avec la sécurité.

### Règle 18
**« La création d’un compte est soumise à un processus de confirmation. »**

### Règle 19
**« Un mécanisme de prévention des usurpations de compte ou d’identité est proposé. »**

### Règle 23
**« Il est possible de se déconnecter des espaces privés. »**

### Règle 26
**« Aucune information n’est exposée sur l’existence d’un compte utilisateur. »**

### Règle 96
**« Les procédures d’authentification à double facteur peuvent être relancées. »**

Une idée pédagogique forte en ressort :

**Une sécurité inaccessible ou impossible à utiliser peut empêcher l'utilisateur légitime d'accéder à son propre service.**

## 5. Grappe 3 : « Je ne veux pas que mon navigateur exécute n'importe quoi »

### 206 et 207 : la paire MIME

**207 = déclarer**  
**206 = ne pas deviner**

## 6. 210, 211, 212 et 214 : contrôler ce qui peut agir dans ou autour de la page

**210 : empêcher une injection malveillante**  
**211 : contrôler qui peut m'encadrer**  
**212 : contrôler d'où peuvent venir mes ressources**  
**214 : vérifier que la ressource reçue est bien celle attendue**

## 7. Grappe 4 : « Ne donne pas gratuitement des informations à l'attaquant »

### 209
Le serveur n’envoie pas la liste des fichiers des répertoires n’ayant pas de page d’index.

### 213
Le serveur ne communique pas d’informations sur les logiciels et langages utilisés.

Raisonnement commun :

> **Une information inutile pour l'utilisateur mais utile à un attaquant n'a pas besoin d'être exposée.**

## 8. Grappe 5 : « Je dois pouvoir reconnaître le vrai service »

### 216 : conserver la barre d'adresse visible

La barre d'adresse permet à l'utilisateur de voir **où il se trouve réellement**.

### 217 : authentifier le domaine de messagerie

SPF, DKIM et DMARC permettent de renforcer l'authenticité du domaine utilisé pour les courriels du service.

## 9. Grappe 6 : « Une opération sécurisée doit rester réalisable »

### 208 : informer

La règle dit : **« Les informations sur la sécurité des transactions sont indiquées. »**

### 215 : proposer une solution de secours

Un utilisateur peut parfaitement disposer d'un compte valide et être incapable de confirmer une transaction parce qu'il n'a pas son téléphone, qu'il est à l'étranger ou que le canal habituel est indisponible.

## 10. Les règles transversales : carte complète

| Niveau | Règles | Pourquoi |
|---|---|---|
| **Sécurité officielle** | **197 à 217** | Rubrique officielle Sécurité |
| **Lien de sécurité direct hors rubrique** | **18, 19, 23, 25, 26, 27, 28, 60, 96, 173** | Usurpation, authentification, fuite, fraude, données sensibles, compte |
| **Sécurité par l'utilisabilité** | **75, 76, 92** | Les choix d'interface autour des mots de passe peuvent améliorer ou dégrader la sécurité réelle |
| **Satellites avec effet sécurité documenté** | **14, 17, 22, 97, 172** | La sécurité apparaît comme effet, contexte ou recommandation secondaire |

## 11. Le glossaire : huit termes officiellement dans « Sécurité »

| Terme | Idée à retenir |
|---|---|
| **Attaque par déni de service** | Rendre un service indisponible |
| **Authentification à double facteur (2FA)** | Prouver son identité avec deux facteurs distincts |
| **Barre d'adresse du navigateur** | Permet notamment d'identifier l'URL visitée |
| **Contrôle d'intégrité** | Comparer l'empreinte reçue à l'empreinte attendue |
| **Domaine de messagerie du site** | Authentification du domaine notamment via SPF, DKIM, DMARC |
| **Entête de transport strict** | HSTS |
| **Opération sécurisée** | Action nécessitant des mesures pour protéger données, authenticité et confidentialité |
| **Type MIME** | Identification normalisée du type de ressource |

## 12. Sécurité et accessibilité : le point de rencontre

La sécurité doit empêcher l'attaquant **sans empêcher l'utilisateur légitime**.

Les meilleurs exemples sont :

**Règle 96** : le code 2FA peut être renvoyé.

**Règle 215** : une opération sécurisée dispose d'au moins deux moyens de validation.

**Règle 76** : le mot de passe peut être affiché pour limiter les erreurs de saisie.

**Règle 92** : ne pas neutraliser inutilement le copier-coller.

**Règle 17** : ne pas imposer exclusivement un système d'identification tiers.

> **La sécurité Opquast ne consiste pas seulement à fermer des portes. Elle consiste aussi à s'assurer que la bonne personne puisse encore les ouvrir.**

## 13. Privacy : à conserver en annexe comme prévu

Quatre zones de contact principales :

**25** : politique de communication des referrers.  
**27** : sécurisation des échanges de données sensibles.  
**28** : données sensibles non transmises en clair dans les URL.  
**60** : modification ou suppression des données bancaires mémorisées, notamment pour prévenir la fraude.

**Privacy pose notamment la question : quelles données et quelle maîtrise ?**  
**Sécurité pose notamment la question : comment empêcher qu'elles soient interceptées, détournées ou exploitées ?**

## 14. Une lecture VPTCS de la sécurité

### Visibilité
216 et 217 participent à la capacité de l'utilisateur à reconnaître l'origine du service ou de ses communications.

### Perception
203 et 208 apportent de l'information perceptible.

### Technique
197 à 200, 206, 207, 209 à 214.

### Contenus
208 est un contenu d'information sécurité.

### Services
201 à 205, 215 et 96 sont très fortement liés au service rendu.

## 15. Opquast n'est pas un référentiel de cybersécurité complet

Une personne certifiée Opquast doit pouvoir dire :

> « Je sais que ce risque existe, je connais un socle de prévention et je sais qu'il faut parfois mobiliser une expertise spécialisée. »

Elle ne doit pas en déduire :

> « Je connais les règles Opquast, donc je sais sécuriser intégralement un système d'information. »

## 16. Du référentiel à la qualité logicielle

Le livre traite explicitement les **tests de sécurité** et inscrit la sécurité dans les pratiques de production, notamment via **DevSecOps**.

## 17. Du projet au management : QSE-IP

Opquast décrit cinq familles que les organisations doivent piloter ensemble :

**Qualité, Sécurité, Environnement, Inclusion, Privacy.**

## 18. L'évolution historique d'Opquast sur la sécurité

| Période | Évolution |
|---|---|
| **2009-2010** | La sécurité devient explicitement l'un des grands sujets à intégrer au référentiel global. |
| **2020** | Séparation nette entre « Données personnelles » et « Sécurité ». |
| **2023** | QSE-IP : la sécurité passe d'un sujet seulement opérationnel à un sujet de management intégré. |
| **2024** | Le discours insiste fortement sur la transversalité. |
| **2025** | V5 ajoute notamment les règles 26, 96, 216 et 217. |
| **2026** | Le livre articule sécurité, gestion des risques, tests logiciels, DevSecOps, normes, management et IA. |

## 19. L'IA ajoute une nouvelle raison de connaître les fondamentaux

Le livre 2026 identifie plusieurs risques spécifiques : du code généré ou modifié par IA peut introduire des vulnérabilités, l'IA peut contribuer aux attaques informatiques et elle peut renforcer l'ingénierie sociale via faux documents, deepfakes, imitations de voix ou d'identités.

## 20. Attention aux métadonnées : livre et API ne sont pas toujours identiques

Pour la préparation à la certification :

**formulation officielle + métadonnées actuelles = API Opquast, version `qualite-numerique`**

**explication, contexte, exemples, avis de l'expert = livre 2026**

## 21. Les principaux pièges à connaître pour la certification

1. **HTTPS n'est pas une seule règle** : 197, 198, 199 et 200 répondent à quatre problèmes différents.
2. **206 et 207 forment une paire** : ne pas laisser le navigateur deviner le MIME, et lui donner le bon MIME.
3. **201 à 205 forment le cycle du mot de passe** : gérer, choisir, évaluer, réinitialiser, ne jamais communiquer en clair.
4. **210, 211, 212 et 214 ne sont pas interchangeables** : XSS, encadrement, origine des contenus, intégrité d'une ressource tierce.
5. **208 informe** sur la sécurité des transactions, elle ne constitue pas à elle seule le mécanisme de sécurisation.
6. **215 ne renforce pas mécaniquement l'authentification** : elle évite qu'un dispositif fort bloque l'utilisateur légitime.
7. **216 redonne un indice à l'humain** : voir le vrai domaine aide à détecter le phishing.
8. **217 concerne le courrier électronique** : authentifier le domaine réduit notamment usurpation et phishing.
9. **Sécurité et Privacy sont distinctes**, même lorsqu'une même fuite relève des deux.
10. **Opquast ne garantit jamais une sécurité absolue** : c'est un socle de prévention de risques fondamentaux.

## 22. Ce que le storyboard devra raconter

Le storyboard d'une heure devrait partir de cinq situations utilisateur :

**Quelqu'un écoute mes échanges.**  
Puis 197 à 200.

**Quelqu'un prend mon compte, ou je n'arrive plus moi-même à y accéder.**  
Puis 18, 19, 23, 96, 201 à 205, 215 et les règles d'utilisabilité du mot de passe.

**Mon navigateur reçoit ou exécute quelque chose qu'il ne devrait pas.**  
Puis 206, 207, 210, 211, 212, 214.

**Le service révèle trop d'informations utiles à une attaque.**  
Puis 209, 213 et les satellites pertinents.

**Je crois être au bon endroit ou lire le bon message, mais ce n'est pas vrai.**  
Puis 216, 217 et l'ingénierie sociale.

## 23. La phrase de synthèse que je garderais

> **La sécurité Opquast ne cherche pas à faire de vous des experts cyber. Elle vous apprend à repérer et prévenir des risques de sécurité fondamentaux qui peuvent faire du tort à l'utilisateur.**

Puis la phrase-mémoire :

> **Sécurité Opquast = prévenir un préjudice utilisateur.**

---

## Utilisateur

- **HTTPS n'est pas une seule règle** : 197, 198, 199 et 200 répondent à quatre problèmes différents.

lesquels ?

- **206 et 207 forment une paire** : ne pas laisser le navigateur deviner le MIME, et lui donner le bon MIME.

précise.

- **201 à 205 forment le cycle du mot de passe** : gérer, choisir, évaluer, réinitialiser, ne jamais communiquer en clair. développe
- **210, 211, 212 et 214 ne sont pas interchangeables** : XSS, encadrement, origine des contenus, intégrité d'une ressource tierce. précise aussi
- **208 informe** sur la sécurité des transactions, elle ne constitue pas à elle seule le mécanisme de sécurisation. précise
- **215 ne renforce pas mécaniquement l'authentification** : elle évite qu'un dispositif fort bloque l'utilisateur légitime. précise
- **216 redonne un indice à l'humain** : voir le vrai domaine aide à détecter le phishing. c'est à dire**217 concerne le courrier électronique** : authentifier le domaine réduit notamment usurpation et phishing.

1.

---

## Assistant

Oui. Je vais reprendre chaque groupe comme un mini-mécanisme : **problème concret → ce que fait la règle → ce qu’elle ne fait pas → mémo certification**. Cela évitera d’apprendre seulement des acronymes.

## 1. 197, 198, 199, 200 : quatre problèmes différents autour de HTTPS

Ces quatre règles peuvent sembler dire « mettez HTTPS », mais chacune ferme une porte différente.

| Règle | La question à se poser | Le problème traité |
|---|---|---|
| **197** | Est-ce que tout passe en HTTPS ? | Interception des échanges |
| **198** | Le certificat est-il valide et signé ? | Validité de la relation sécurisée et alertes navigateur |
| **199** | Le navigateur est-il obligé de rester en HTTPS ? | Retour ou passage initial par HTTP |
| **200** | Une page HTTPS charge-t-elle encore quelque chose en HTTP ? | Contenu mixte, partie de page non sécurisée |

### 197 : « Toutes les pages utilisent le protocole HTTPS »

C'est la **base** : les échanges entre le navigateur et le serveur sont chiffrés. Le préjudice visé est l'interception ou le vol de données pendant leur transport.

**Image mentale :** je mets mes échanges dans un tunnel protégé.

**Mémo :** `197 = chiffrer le transport`.

### 198 : « Les certificats de sécurité sont signés et en cours de validité »

Ici, la question n'est plus « est-ce chiffré ? », mais **le certificat utilisé pour établir cette connexion est-il valide ?**

Un certificat invalide ou expiré déclenche typiquement une alerte du navigateur et peut conduire l'utilisateur à abandonner sa navigation.

Nuance importante : le certificat n'est pas présenté comme une preuve absolue de l'identité du propriétaire. Opquast parle de contribution à la sécurisation et de validité, pas de garantie absolue.

**Image mentale :** le tunnel existe, mais je vérifie aussi que son laissez-passer est valable.

**Mémo :** `198 = certificat valide`.

### 199 : « Les pages utilisant HTTPS ont un entête de transport strict »

C'est **HSTS**.

197 dit : « mon site fonctionne en HTTPS ».

199 ajoute : **« navigateur, pour ce site, n'essaie même pas de repasser par HTTP »**.

Le navigateur transforme directement les tentatives HTTP en HTTPS, ce qui évite qu'une première requête HTTP puisse servir à une attaque de type homme du milieu ou à une redirection malveillante.

**Image mentale :** le tunnel sécurisé n'est plus seulement disponible, il devient le chemin imposé.

**Mémo :** `199 = HTTPS obligatoire`.

### 200 : « Les pages utilisant le protocole HTTPS ne proposent pas de ressources HTTP »

Une page peut elle-même être en HTTPS tout en chargeant une image, un script, une feuille CSS ou une autre ressource en HTTP.

C'est le **mixed content**, le contenu mixte.

Le problème : on a une enveloppe sécurisée contenant encore des éléments qui ne le sont pas. Le navigateur peut déclencher une alerte et la ressource HTTP constitue une faiblesse potentielle.

**Image mentale :** la maison est verrouillée, mais une fenêtre est restée ouverte.

**Mémo global :**

> **197 : HTTPS**  
> **198 : certificat valide**  
> **199 : HTTPS imposé**  
> **200 : HTTPS partout jusque dans les ressources**

# 2. 206 et 207 : « déclarer » puis « interdire de deviner »

Le **type MIME** sert à indiquer au navigateur la nature d'une ressource : image, PDF, JavaScript, CSS, etc.

### 207 : le serveur indique le type MIME

Le serveur doit dire explicitement :

> « Cette ressource est de tel type. »

Il fournit donc le `Content-Type` correspondant à la ressource.

Le problème visé est notamment un contenu dangereux dissimulé sous une autre nature. Opquast veut que le navigateur sache précisément ce qu'il reçoit.

**Mémo :** `207 = le serveur DÉCLARE`.

### 206 : désactiver la détection automatique

Mais même si le serveur annonce un type, certains navigateurs peuvent essayer de **deviner eux-mêmes** la nature du contenu.

C'est le MIME sniffing.

La règle 206 demande donc notamment :

`X-Content-Type-Options: nosniff`

Autrement dit :

> « Navigateur, ne joue pas aux devinettes. Respecte le type annoncé. »

### La paire

> **207 : je te dis ce que c'est.**  
> **206 : tu ne cherches pas à deviner autre chose.**

C'est probablement le meilleur moyen de les mémoriser.

# 3. 201 à 205 : le cycle de vie du mot de passe

Il ne faut surtout pas apprendre ces cinq règles comme cinq variantes de « sécuriser le mot de passe ».

Elles décrivent **cinq moments ou besoins différents**.

### 201 : pouvoir tout gérer en ligne

> « Les opérations relatives aux mots de passe peuvent être effectuées intégralement en ligne. »

Je veux changer ou récupérer mon accès : je ne dois pas être obligé d'attendre un courrier postal ou de basculer dans une procédure hors ligne pénalisante.

Le préjudice principal est ici **le blocage ou le délai subi par l'utilisateur**.

**201 = disponibilité du processus.**

### 202 : pouvoir choisir ou changer

> « Les mots de passe peuvent être choisis ou changés par l’utilisateur. »

L'utilisateur doit conserver une maîtrise de son propre moyen d'authentification.

S'il reçoit un mot de passe généré automatiquement, il doit pouvoir le modifier ensuite.

**202 = maîtrise du mot de passe.**

### 203 : être informé de sa robustesse

> « Un dispositif sensibilise l’utilisateur sur le degré de sécurisation du mot de passe qu’il choisit. »

C'est la jauge ou le retour du type :

« faible / moyen / fort ».

Point subtil : cette règle **ne vise pas nécessairement à interdire** le choix tant qu'un niveau donné n'est pas atteint. Elle vise d'abord à informer l'utilisateur sur le risque associé à son choix.

**203 = comprendre la robustesse de son choix.**

### 204 : pouvoir repartir avec un nouveau mot de passe

> « Les mots de passe peuvent être réinitialisés. »

Mot de passe oublié : on ne doit pas récupérer nécessairement l'ancien. On crée **un nouveau mot de passe** via une procédure de réinitialisation.

La règle protège donc simultanément :

- la continuité d'accès au compte ;
- la sécurité, puisqu'il n'est pas nécessaire de stocker le mot de passe sous une forme permettant de le restituer à l'utilisateur.

**204 = j'ai oublié, je RÉINITIALISE.**

### 205 : ne jamais me renvoyer mon secret en clair

> « Les mots de passe ne sont pas communiqués en clair. »

Et particulièrement par courrier électronique.

Pour Opquast, la bonne logique en cas de perte est par exemple :

**courriel avec lien temporaire → procédure en ligne → création d'un nouveau mot de passe**

et non :

**« Bonjour, votre mot de passe est Toto1234 »**.

Le préjudice est l'interception du mot de passe lui-même.

### Le cycle complet

> **201 : je peux gérer en ligne**  
> **202 : je peux choisir/changer**  
> **203 : je connais la robustesse**  
> **204 : je peux réinitialiser**  
> **205 : mon secret n'est pas renvoyé en clair**

Et surtout :

**204 ≠ 205**

204 explique **comment reprendre la main**.  
205 explique **ce qu'il ne faut pas divulguer pendant cette reprise en main**.

# 4. 210, 211, 212, 214 : quatre contrôles très différents

Le piège vient du fait que CSP intervient dans plusieurs règles.

Il faut raisonner par **menace**.

### 210 : empêcher l'exécution d'un contenu injecté

> « Le serveur envoie les informations d’activation de protection cross site scripting. »

Le **XSS** consiste à injecter puis exécuter un contenu malveillant dans une page.

La règle demande qu'un mécanisme explicite de protection soit transmis au navigateur, par exemple une politique CSP adaptée.

**210 = quelqu'un tente d'INJECTER et d'exécuter du contenu.**

### 211 : empêcher un site malveillant d'encadrer ma page

> « Le serveur envoie les informations indiquant les domaines autorisés à intégrer ses pages dans des cadres. »

Ici, le problème n'est pas principalement ce que **ma page charge**.

C'est **qui a le droit d'afficher ma page dans son propre `frame` ou `iframe`**.

Sinon un site malveillant peut intégrer ma véritable interface et tromper l'utilisateur sur ce qu'il est en train de cliquer.

C'est notamment le risque de **clickjacking**.

Les mécanismes cités sont notamment `X-Frame-Options` ou la directive CSP `frame-ancestors`.

**211 = qui peut M'ENCADRER ?**

### 212 : contrôler d'où viennent les contenus que ma page charge

> « Un mécanisme de sécurité restreint l’origine des contenus. »

Ici on retourne à l'intérieur de ma page.

Ma page peut avoir besoin de charger :

- scripts ;
- CSS ;
- images ;
- polices ;
- etc.

La CSP peut dire :

> « Les scripts ne peuvent venir que de telles origines, les images de telles autres, etc. »

**212 = D'OÙ ai-je le droit de charger ?**

### 214 : vérifier que le fichier tiers n'a pas été modifié

> « Le contrôle d’intégrité des ressources tierces est présent et valide. »

Imagine maintenant qu'une ressource soit autorisée par la règle 212.

Il reste un autre problème :

> **est-ce toujours exactement le fichier que j'attendais ?**

Le mécanisme SRI associe une **empreinte cryptographique** au fichier.

Si le fichier tiers est modifié ou corrompu et ne correspond plus à l'empreinte attendue, le navigateur peut refuser de l'exécuter ou de l'appliquer.

**214 = est-ce bien LE BON FICHIER, inchangé ?**

### Le mémo

> **210 : ce qui est injecté**  
> **211 : qui peut m'encadrer**  
> **212 : d'où je peux charger**  
> **214 : est-ce toujours le fichier attendu**

Et la distinction cruciale :

> **212 vérifie l'origine autorisée. 214 vérifie l'intégrité du fichier provenant de cette origine.**

# 5. 208 : sécuriser et informer sont deux exigences différentes

> « Les informations sur la sécurité des transactions sont indiquées. »

C'est une règle facile à surinterpréter.

Elle ne dit pas :

> « les transactions sont sécurisées ».

Elle dit :

> **l'utilisateur est informé de leur sécurisation.**

L'objectif de **cette règle précise** est :

> « Contribuer à l’information des utilisateurs sur la sécurisation des échanges de données sensibles. »

Il peut notamment s'agir d'indiquer le mode et le niveau de chiffrement ou d'expliquer comment l'utilisateur peut retrouver cette information dans son navigateur.

Donc :

**mécanisme technique de sécurité ≠ information sur le mécanisme de sécurité.**

### Exemple mental

Une banque pourrait avoir une infrastructure techniquement sécurisée mais ne donner **aucune information compréhensible** à son client sur la sécurisation de la transaction.

Pour 208, il reste un défaut.

**Mémo :** `208 = informer sur la sécurité de la transaction`.

# 6. 215 : le deuxième moyen est une solution de secours

> « Les opérations sécurisées peuvent être validées par au moins deux moyens. »

Celle-ci est souvent mal comprise.

Elle ne dit pas :

> « il faut deux facteurs pour rendre toute opération encore plus forte ».

Elle dit :

> **si une opération exige un mécanisme fort, l'utilisateur doit disposer d'au moins deux moyens possibles de la valider.**

Exemple :

- SMS ;
- terminal de validation.

Ou :

- clé de sécurité ;
- code de secours ;
- confirmation sur un autre appareil.

Pourquoi ?

Parce qu'un utilisateur peut perdre son téléphone, ne pas l'avoir avec lui, être à l'étranger ou ne pas disposer du dispositif prévu.

Le risque est alors paradoxal :

**le mécanisme de sécurité fonctionne tellement bien qu'il bloque également la personne légitime.**

Les objectifs officiels sont bien de prévenir l'échec de l'opération et d'éviter l'exclusion pour des raisons techniques ou matérielles.

### À ne pas confondre

**2FA : deux preuves pour authentifier une personne.**

**Règle 215 : au moins deux chemins possibles pour accomplir l'opération sécurisée.**

Ce n'est pas la même notion.

**Mémo :** `215 = une porte sécurisée + une solution de secours sécurisée`.

# 7. 216 : « voir le vrai domaine », concrètement, ça veut dire quoi ?

> « L’affichage de la barre d’adresse du navigateur n’est pas bloqué. »

Imagine une fenêtre de connexion qui ressemble parfaitement à celle de ta banque :

Logo correct.  
Couleurs correctes.  
Formulaire identifiant / mot de passe correct.

Mais **aucune barre d'adresse n'est visible**.

Tu ne peux plus facilement constater que tu es en réalité sur :

`ma-banque-securisee-pirate.example`

et non sur le domaine réel attendu.

La barre d'adresse constitue donc un **repère extérieur au contenu de la page**.

C'est important : un attaquant peut reproduire le graphisme d'un service. Il ne peut pas simplement transformer son propre nom de domaine en celui qu'il imite.

La barre permet notamment de contrôler :

- le protocole utilisé ;
- le certificat ;
- le nom de domaine.

La masquer réduit la capacité de l'utilisateur à reconnaître une tentative de phishing ou un site frauduleux.

### La logique utilisateur

> « Ce que je vois DANS la page peut être copié.  
> La barre d'adresse m'aide à vérifier OÙ je suis. »

**Mémo :** `216 = toujours savoir où je suis`.

# 8. 217 : la même logique, mais dans le courrier électronique

> « Le domaine de messagerie est authentifié. »

Cette fois, le problème n'est plus :

**« suis-je vraiment sur le bon site ? »**

mais :

**« ce courriel vient-il réellement du domaine qu'il prétend représenter ? »**

Opquast cite trois mécanismes :

**SPF** : indique quels serveurs sont autorisés à envoyer des courriels pour le domaine.

**DKIM** : ajoute une signature cryptographique permettant de vérifier le message par rapport à une clé publique publiée dans le DNS.

**DMARC** : définit notamment la politique à appliquer lorsque les contrôles ne correspondent pas aux attentes, et fournit des mécanismes de rapport.

### Préjudice utilisateur

Sans authentification correcte, l'utilisateur peut recevoir un faux courriel ressemblant à celui du véritable service :

> « Votre compte est bloqué, cliquez ici et reconnectez-vous. »

Il croit au message, suit le lien et remet ses identifiants à un fraudeur.

Opquast rattache explicitement 217 aux courriels frauduleux, au phishing et à l'usurpation d'identité.

### 216 + 217 forment donc une paire pédagogique intéressante

> **216 : est-ce vraiment le site auquel je crois parler ?**  
> **217 : est-ce vraiment le service qui m'envoie ce mail ?**

Dans les deux cas, on lutte notamment contre **l'usurpation et l'ingénierie sociale**, pas seulement contre une attaque purement technique.

## La carte mentale finale

Je résumerais tout ce bloc comme ceci :

**197-200 : protéger le canal de communication**  
**201-205 : protéger sans faire perdre la maîtrise du compte**  
**206-207 : ne jamais laisser d'ambiguïté sur la nature des fichiers**  
**208 : expliquer la sécurisation à l'utilisateur**  
**210-212-214 : contrôler ce qui peut s'exécuter, s'intégrer et être chargé**  
**215 : ne pas enfermer l'utilisateur légitime dehors**  
**216-217 : permettre de reconnaître le vrai service**

Et là on retrouve exactement notre idée centrale :

> **Chez Opquast, la sécurité ne se réduit pas à durcir un serveur. Elle cherche à empêcher qu'un risque technique devienne un préjudice concret pour l'utilisateur.**

---

## Utilisateur

je peux avoir un md de l'ensemble de cette conversation
