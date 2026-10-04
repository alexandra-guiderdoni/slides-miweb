# Storyboard — Octobre, Web et accessibilité

## Identité

- Statut : `BROUILLON`
- Version : `v001`
- Série : `accessibilite-web-octobre`
- Périmètre et édition Opquast : série éditoriale Opquast/Miweb ; aucune règle Opquast officielle ciblée à ce stade.
- Audience et objectif : sensibiliser des apprenants ou équipes projet au fait que l’accessibilité n’est pas un ajout final, mais une condition constitutive d’un Web utilisable par toutes et tous.
- Nombre de slides principales et annexes : 5 slides principales ; 0 annexe prévue.
- Revue : `NOT VERIFIED` ; auto-préparation assistant, 2026-10-04 ; pas de revue externe.
- Correspondance machine : `run.json` ; storyboard actif prévu : `storyboard-v001.md`.

## Paramètres de série

- Guide commun : `docs/05-GUIDE-STYLE.md`, pack 2.0.0.
- Header exact : haut gauche `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES` ; haut droit `Opquast` puis `DES SITES MEILLEURS POUR TOUS`.
- Footer principal exact : `QUALITÉ WEB · ACCESSIBILITÉ WEB`.
- Footer des annexes : non applicable.
- Pagination, total et traitement des annexes : `1/5` à `5/5`, en bas à droite ; aucune annexe.
- Position des badges : pas de badge de règle Opquast, car aucune règle officielle n’est ciblée.
- Slogan et slides où il apparaît : `Un Web accessible n’est pas un supplément : c’est le Web qui tient sa promesse.` Slides 1 et 5.
- Références visuelles réellement disponibles : aucune image de référence spécifique chargée pour cette série ; appliquer le style commun.
- Exceptions au guide et justification : aucune.
- VPTCS : non prévu.

## Sources et couverture

| Référence | Statut | Extrait ou fait utilisé | Source | Slide(s) | Principale/connexe |
|---|---|---|---|---|---|
| S1 | W3C vérifié | En octobre 1990, Tim Berners-Lee écrit le premier client Web, navigateur et éditeur `WorldWideWeb`. | `sources/w3c-accessibilite-web.md` | 1 | Principale |
| S2 | W3C vérifié | Le W3C est fondé le 1er octobre 1994. | `sources/w3c-accessibilite-web.md` | 1 | Principale |
| S3 | W3C vérifié | Citation de Tim Berners-Lee sur universalité et accès indépendamment du handicap. | `sources/w3c-accessibilite-web.md` | 5 | Principale |
| S4 | W3C vérifié | Contexte historique de la citation dans les activités WAI. | `sources/w3c-accessibilite-web.md` | 5 | Connexe |

Les regroupements sont pédagogiques. Aucune règle Opquast officielle n’est ajoutée de mémoire.

---

## Slide 01 — Octobre, un mois qui rappelle la promesse du Web

**Rôle narratif** : ouverture.

**Idée principale** : octobre permet de relier deux jalons historiques — premier navigateur/éditeur Web et création du W3C — à la promesse d’un Web universel.

**Situation** : une équipe projet voit octobre comme un repère calendaire ; la slide transforme ce repère en rappel de conception.

**Risque utilisateur** : oublier que le Web a été conçu comme un espace d’accès et de participation, puis traiter l’accessibilité comme une contrainte externe.

**Principe de prévention / garantie recherchée** : replacer l’accessibilité dans l’histoire et la finalité du Web : accès, communication, participation.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : pas de règle Opquast officielle ; références W3C S1 et S2.

**Exemple de mise en œuvre** : utiliser une frise courte pour relier octobre 1990, 1er octobre 1994 et aujourd’hui.

**Scène visuelle et relations à restituer** : ligne horizontale sobre en trois jalons : `Octobre 1990` → `1er octobre 1994` → `Aujourd’hui`. Le troisième jalon pose la question : `Construisons-nous un Web que tout le monde peut utiliser ?`

**Textes visibles exacts** :

- Titre : `Octobre rappelle la promesse du Web`
- Jalon 1 : `Octobre 1990 · premier navigateur/éditeur Web`
- Jalon 2 : `1er octobre 1994 · naissance du W3C`
- Jalon 3 : `Aujourd’hui · tenir la promesse d’un Web utilisable par tous`
- Callout : `Un Web accessible n’est pas un supplément : c’est le Web qui tient sa promesse.`
- Footer : `QUALITÉ WEB · ACCESSIBILITÉ WEB`
- Pagination : `1/5`

**Termes ambigus et sens exclus** : `tous` signifie diversité de situations, capacités, matériels, langues et contextes ; ne pas réduire à un public unique.

**Éléments interdits / invariants à préserver** : ne pas mentionner la provenance personnelle initiale ; ne pas ajouter de logo W3C inventé ; ne pas présenter les jalons comme une certification d’accessibilité.

**Préparation orale** : expliquer que la date sert d’entrée pédagogique, pas de commémoration décorative.

**Pré-accordéons** :

```html
<section aria-labelledby="slide-01-title">
  <h2 id="slide-01-title">Slide 1 — Octobre rappelle la promesse du Web</h2>
  <details>
    <summary>Lire la transcription de la slide 1 - Octobre rappelle la promesse du Web</summary>
    <h3>Lecture du visuel</h3>
    <p>PRETRANSCRIPTION_A_VERIFIER. La slide doit montrer une frise en trois temps : octobre 1990, 1er octobre 1994, puis aujourd’hui. Le callout rappelle que l’accessibilité n’est pas un supplément mais une condition de la promesse du Web.</p>
  </details>
  <details>
    <summary>Lire le discours oral de la slide 1 - Octobre rappelle la promesse du Web</summary>
    <p>Octobre est ici un repère pour revenir à l’intention initiale du Web : permettre l’accès et la participation.</p>
    <h3>Relier chaque règle à son impact</h3>
    <p>Il n’y a pas de règle Opquast officielle sur cette slide. Le principe éditorial est de relier un jalon historique à un impact utilisateur : si l’accès n’est pas prévu, certaines personnes ne peuvent pas lire, comprendre, agir ou participer.</p>
    <h3>Ce que garantit la règle</h3>
    <p>Le principe vise à garantir que l’accessibilité soit pensée comme une condition de fonctionnement du Web, et non comme une correction tardive.</p>
    <h3>Mémo oral</h3>
    <p>Octobre rappelle une promesse : un Web utile seulement s’il reste utilisable par toutes et tous.</p>
  </details>
</section>
```

**Fichier final prévu** : `finals/slide-01-octobre-promesse-web.png`.

**Critères de revue spécifiques** : vérifier les dates, l’absence de provenance personnelle et l’équilibre entre histoire et message d’accessibilité.

---

## Slide 02 — Deux conceptions : rustine finale ou propriété du Web

**Rôle narratif** : comparaison.

**Idée principale** : montrer l’opposition centrale : accessibilité ajoutée en fin de projet contre accessibilité intégrée dès la conception.

**Situation** : une équipe livre une interface puis demande une “passe accessibilité” juste avant publication.

**Risque utilisateur** : les obstacles deviennent structurels : navigation, compréhension, interaction, contenus et médias peuvent déjà être verrouillés par de mauvais choix.

**Principe de prévention / garantie recherchée** : intégrer l’accessibilité dans le cadrage, la conception, les contenus, le développement et les tests.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : pas de règle Opquast officielle ; principe pédagogique issu du brief et aligné avec S3.

**Exemple de mise en œuvre** : comparer deux colonnes : `Ajoutée à la fin` vs `Conçue dès le départ`.

**Scène visuelle et relations à restituer** : deux colonnes contrastées. Colonne gauche : un produit déjà fermé avec une étiquette `à corriger`. Colonne droite : un projet en construction où l’accessibilité traverse les étapes.

**Textes visibles exacts** :

- Titre : `Accessibilité : rustine finale ou propriété du Web ?`
- Colonne gauche : `Ajoutée à la fin` ; `on répare ce qui bloque déjà`
- Colonne droite : `Pensée dès le départ` ; `on évite de créer les obstacles`
- Callout : `La meilleure correction est souvent celle qu’on n’a pas à faire.`
- Footer : `QUALITÉ WEB · ACCESSIBILITÉ WEB`
- Pagination : `2/5`

**Termes ambigus et sens exclus** : `rustine` est une métaphore de correction tardive ; ne pas représenter l’accessibilité comme un audit cosmétique ou une checklist purement administrative.

**Éléments interdits / invariants à préserver** : pas de scène de handicap stéréotypée ; pas de pictogramme “handicap” unique qui réduirait le sujet.

**Préparation orale** : insister sur la prévention plutôt que sur la culpabilisation.

**Pré-accordéons** :

```html
<section aria-labelledby="slide-02-title">
  <h2 id="slide-02-title">Slide 2 — Accessibilité : rustine finale ou propriété du Web ?</h2>
  <details>
    <summary>Lire la transcription de la slide 2 - Accessibilité : rustine finale ou propriété du Web ?</summary>
    <h3>Lecture du visuel</h3>
    <p>PRETRANSCRIPTION_A_VERIFIER. La slide doit comparer deux approches : à gauche, l’accessibilité ajoutée à la fin ; à droite, l’accessibilité pensée dès le départ. Le callout indique que la meilleure correction est souvent celle qu’on n’a pas à faire.</p>
  </details>
  <details>
    <summary>Lire le discours oral de la slide 2 - Accessibilité : rustine finale ou propriété du Web ?</summary>
    <p>Le cœur de la série est cette opposition : corriger tard, ou concevoir pour éviter les obstacles.</p>
    <h3>Relier chaque règle à son impact</h3>
    <p>Le principe de prévention a un impact direct : il évite que des choix d’interface, de contenu ou de code excluent des utilisateurs avant même les tests.</p>
    <h3>Ce que garantit la règle</h3>
    <p>Il vise à garantir que l’accessibilité soit présente dans les décisions de projet, pas seulement dans une vérification finale.</p>
    <h3>Mémo oral</h3>
    <p>Ne pas ajouter l’accessibilité à la fin : construire avec elle.</p>
  </details>
</section>
```

**Fichier final prévu** : `finals/slide-02-rustine-ou-propriete.png`.

**Critères de revue spécifiques** : vérifier que la comparaison est immédiatement lisible et ne surpromet pas une absence totale de correction.

---

## Slide 03 — Ce qui se joue : accéder, comprendre, agir, participer

**Rôle narratif** : impact utilisateur.

**Idée principale** : traduire l’accessibilité en capacités concrètes pour les utilisateurs.

**Situation** : une personne doit obtenir une information, remplir une démarche, consulter un média ou interagir avec un service.

**Risque utilisateur** : si le site exclut certains modes d’accès, l’utilisateur perd du temps, abandonne ou se retrouve privé d’un service.

**Principe de prévention / garantie recherchée** : concevoir pour plusieurs façons de percevoir, naviguer, comprendre et interagir.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : pas de règle Opquast officielle ; aligné avec S3 sur l’inclusion et la levée des barrières.

**Exemple de mise en œuvre** : quatre verbes d’usage : `Accéder`, `Comprendre`, `Agir`, `Participer`.

**Scène visuelle et relations à restituer** : quatre verbes disposés comme une chaîne ou un carré stable. Chaque verbe a une micro-situation : lire l’information, comprendre le choix, valider une action, contribuer ou communiquer.

**Textes visibles exacts** :

- Titre : `L’accessibilité se mesure dans l’usage`
- Verbe 1 : `Accéder` ; `atteindre l’information`
- Verbe 2 : `Comprendre` ; `saisir le sens`
- Verbe 3 : `Agir` ; `réaliser la tâche`
- Verbe 4 : `Participer` ; `prendre part au Web`
- Callout : `L’obstacle technique devient vite un obstacle social.`
- Footer : `QUALITÉ WEB · ACCESSIBILITÉ WEB`
- Pagination : `3/5`

**Termes ambigus et sens exclus** : `mesure` désigne une lecture qualitative de l’usage dans cette slide, pas une métrique chiffrée.

**Éléments interdits / invariants à préserver** : ne pas associer chaque verbe à un handicap unique ; ne pas utiliser de données personnelles réelles.

**Préparation orale** : ramener le sujet au préjudice concret : ne pas accéder à un service, ne pas terminer une action, ne pas participer.

**Pré-accordéons** :

```html
<section aria-labelledby="slide-03-title">
  <h2 id="slide-03-title">Slide 3 — L’accessibilité se mesure dans l’usage</h2>
  <details>
    <summary>Lire la transcription de la slide 3 - L’accessibilité se mesure dans l’usage</summary>
    <h3>Lecture du visuel</h3>
    <p>PRETRANSCRIPTION_A_VERIFIER. La slide doit présenter quatre verbes : accéder, comprendre, agir, participer. Chaque verbe est relié à une conséquence d’usage concrète.</p>
  </details>
  <details>
    <summary>Lire le discours oral de la slide 3 - L’accessibilité se mesure dans l’usage</summary>
    <p>L’accessibilité n’est pas abstraite : elle se voit dans ce que les personnes peuvent réellement faire.</p>
    <h3>Relier chaque règle à son impact</h3>
    <p>Le principe d’accessibilité relie chaque choix de conception à un impact : atteindre une information, comprendre un message, valider une action ou participer à un échange.</p>
    <h3>Ce que garantit la règle</h3>
    <p>Il vise à garantir que les choix techniques et éditoriaux ne ferment pas inutilement l’accès à ces usages essentiels.</p>
    <h3>Mémo oral</h3>
    <p>Ce qui bloque l’interface bloque aussi la participation.</p>
  </details>
</section>
```

**Fichier final prévu** : `finals/slide-03-acceder-comprendre-agir-participer.png`.

**Critères de revue spécifiques** : vérifier que les quatre verbes restent équilibrés et que la slide ne transforme pas l’accessibilité en slogan vague.

---

## Slide 04 — Intégrer l’accessibilité dans les décisions de projet

**Rôle narratif** : mise en œuvre.

**Idée principale** : convertir le principe en décisions concrètes dans une chaîne de production.

**Situation** : une équipe veut éviter que l’accessibilité soit traitée comme une tâche isolée à la fin.

**Risque utilisateur** : si chaque métier attend le suivant, les obstacles s’accumulent et deviennent coûteux ou difficiles à corriger.

**Principe de prévention / garantie recherchée** : partager la responsabilité : cadrage, design, contenu, développement, test.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : pas de règle Opquast officielle ; principe pédagogique de gestion de projet.

**Exemple de mise en œuvre** : cinq étapes en flux, chacune avec une question courte.

**Scène visuelle et relations à restituer** : flux gauche-droite en cinq étapes : `Cadrer`, `Concevoir`, `Rédiger`, `Développer`, `Tester`. Chaque étape contient une question d’accessibilité.

**Textes visibles exacts** :

- Titre : `L’accessibilité se décide tout au long du projet`
- Étape 1 : `Cadrer` ; `qui doit pouvoir utiliser ?`
- Étape 2 : `Concevoir` ; `quels parcours éviteront les blocages ?`
- Étape 3 : `Rédiger` ; `le message est-il compréhensible ?`
- Étape 4 : `Développer` ; `l’interface reste-t-elle utilisable autrement ?`
- Étape 5 : `Tester` ; `quels obstacles restent visibles ?`
- Callout : `Chaque étape peut prévenir un obstacle.`
- Footer : `QUALITÉ WEB · ACCESSIBILITÉ WEB`
- Pagination : `4/5`

**Termes ambigus et sens exclus** : `utilisable autrement` signifie clavier, lecteur d’écran, zoom, préférences utilisateur, contextes variés ; ne pas le limiter à un seul outil.

**Éléments interdits / invariants à préserver** : ne pas représenter les étapes comme une conformité garantie ; ne pas inventer une obligation juridique.

**Préparation orale** : faire comprendre que l’accessibilité est une responsabilité distribuée, pas une tâche du seul développeur ou du seul auditeur.

**Pré-accordéons** :

```html
<section aria-labelledby="slide-04-title">
  <h2 id="slide-04-title">Slide 4 — L’accessibilité se décide tout au long du projet</h2>
  <details>
    <summary>Lire la transcription de la slide 4 - L’accessibilité se décide tout au long du projet</summary>
    <h3>Lecture du visuel</h3>
    <p>PRETRANSCRIPTION_A_VERIFIER. La slide doit montrer cinq étapes : cadrer, concevoir, rédiger, développer, tester. Chaque étape est associée à une question d’accessibilité.</p>
  </details>
  <details>
    <summary>Lire le discours oral de la slide 4 - L’accessibilité se décide tout au long du projet</summary>
    <p>Cette slide transforme le principe en organisation de projet.</p>
    <h3>Relier chaque règle à son impact</h3>
    <p>Chaque étape a un impact utilisateur : un mauvais cadrage ignore des besoins, un mauvais design bloque des parcours, un contenu flou empêche de comprendre, un code fragile limite les modes d’accès, un test trop tardif laisse passer des obstacles.</p>
    <h3>Ce que garantit la règle</h3>
    <p>Le principe vise à garantir que les obstacles soient cherchés et prévenus au moment où les décisions se prennent.</p>
    <h3>Mémo oral</h3>
    <p>L’accessibilité n’est pas une étape de plus : elle traverse les étapes existantes.</p>
  </details>
</section>
```

**Fichier final prévu** : `finals/slide-04-decisions-projet.png`.

**Critères de revue spécifiques** : vérifier que les questions restent courtes, lisibles et non normatives.

---

## Slide 05 — Universalité : la promesse à garder visible

**Rôle narratif** : synthèse.

**Idée principale** : conclure par la citation de Tim Berners-Lee et relier universalité, accessibilité et responsabilité de conception.

**Situation** : une équipe doit retenir une formule simple après la séquence.

**Risque utilisateur** : réduire l’accessibilité à une obligation séparée ou à une correction de surface.

**Principe de prévention / garantie recherchée** : garder la citation comme boussole : le Web est puissant parce qu’il est universel ; l’accès indépendamment du handicap en est un aspect essentiel.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : pas de règle Opquast officielle ; citation S3, contexte S4.

**Exemple de mise en œuvre** : citation centrale, puis trois mots-repères : `Accès`, `Universalité`, `Participation`.

**Scène visuelle et relations à restituer** : grande citation au centre, attribution à Tim Berners-Lee, puis trois repères bas de slide. Style sobre, pas de portrait inventé.

**Textes visibles exacts** :

- Titre : `La puissance du Web réside dans son universalité`
- Citation : `« La puissance du Web réside dans son universalité. Son accès par toutes et tous, indépendamment du handicap, en est un aspect essentiel. »`
- Attribution : `Tim Berners-Lee · W3C`
- Repères : `Accès` · `Universalité` · `Participation`
- Callout : `Construire accessible, c’est construire le Web lui-même.`
- Footer : `QUALITÉ WEB · ACCESSIBILITÉ WEB`
- Pagination : `5/5`

**Termes ambigus et sens exclus** : `universalité` ne signifie pas uniformité ; l’objectif est de permettre plusieurs modes d’accès.

**Éléments interdits / invariants à préserver** : ne pas inventer un portrait de Tim Berners-Lee ; ne pas attribuer la citation à une autre personne ; ne pas supprimer la référence W3C.

**Préparation orale** : fermer la série sur une idée mémorisable : l’accessibilité n’est pas un supplément, elle est une condition de l’universalité du Web.

**Pré-accordéons** :

```html
<section aria-labelledby="slide-05-title">
  <h2 id="slide-05-title">Slide 5 — La puissance du Web réside dans son universalité</h2>
  <details>
    <summary>Lire la transcription de la slide 5 - La puissance du Web réside dans son universalité</summary>
    <h3>Lecture du visuel</h3>
    <p>PRETRANSCRIPTION_A_VERIFIER. La slide doit afficher la citation de Tim Berners-Lee, son attribution au W3C, les repères accès, universalité et participation, puis le callout final.</p>
  </details>
  <details>
    <summary>Lire le discours oral de la slide 5 - La puissance du Web réside dans son universalité</summary>
    <p>La citation permet de refermer la série sur la finalité du Web.</p>
    <h3>Relier chaque règle à son impact</h3>
    <p>Le principe relie l’universalité à un impact direct : permettre l’accès à l’information et à l’action, indépendamment des situations de handicap et des contextes d’usage.</p>
    <h3>Ce que garantit la règle</h3>
    <p>Il vise à garantir que l’accessibilité reste une exigence de conception du Web, pas une option ajoutée après coup.</p>
    <h3>Mémo oral</h3>
    <p>Construire accessible, c’est construire le Web lui-même.</p>
  </details>
</section>
```

**Fichier final prévu** : `finals/slide-05-universalite.png`.

**Critères de revue spécifiques** : vérifier l’exactitude de la citation traduite, l’attribution à Tim Berners-Lee et la présence de la référence W3C.

---

## Revue avant génération

- Statut actuel : `BROUILLON`.
- Revue métier : `NOT VERIFIED`.
- Contrôle assistant réalisé : cohérence interne, absence de provenance personnelle, absence de règle Opquast inventée, présence des sources W3C.
- Contrôles non réalisés : API Opquast, revue externe, génération ImageGen, inspection PNG, accordéons finaux, ShipGuard.
- Prochaine action documentée : relire/valider le storyboard ou demander modifications ; ne pas générer tant que le storyboard actif n’est pas `VALIDE_POUR_GENERATION`.
