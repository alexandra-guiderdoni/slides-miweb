# OPQUAST V5 — FORMULAIRES | STORYBOARD MAÎTRE — FABRIQUE V2

**Édition de travail :** 29 octobre 2026 ; révision v007 du 6 novembre 2026 : contrat de la Fabrique appliqué, exercices couvrant les 30 règles, relecture indépendante traitée  
**Référentiel :** Opquast Qualité Numérique V5 (2025–2030), règles 69 à 98  
**Finalité :** former à reconnaître, distinguer et justifier toutes les règles de la thématique Formulaires, puis les mettre en relation avec les autres rubriques, pour se préparer à la certification.  
**Livrable :** spécification éditoriale destinée à la Fabrique V2, pas un diaporama déjà publié.  
**Durée intégrale :** environ 72 minutes (questions/échanges inclus) ; prévoir un peu de souplesse pour les réponses orales.  
**Volume :** 63 slides : un plan, 30 slides centrées chacune sur une règle, 13 termes de glossaire, 7 points de réactivation ou d’évaluation (dont 16 questions finales), une conclusion en deux temps.  

## Identité

- Statut : `VALIDE_POUR_GENERATION` ; validé par Alex le 6 novembre 2026 (« génère les slides avec Codex en suivant les règles de la fabrique »).
- Version : `v007`. Les v006, v005, v004, v003, v002 et v001 (`01-STORYBOARD-MAITRE.md`, SHA-256 `9f2fc741…1bee`) sont conservées sans modification.
- Périmètre : Opquast V5 `qualite-numerique`, rubrique Formulaires, règles 69 à 98 ; règles connexes 10, 24, 26, 103, 108, 110, 165 à 167, 172, 173 à 176, 181, 201 à 205 et 236.
- Audience : candidats à la certification Opquast, profils numériques variés.
- Nombre : 63 slides.
- Revue : `revue-mcp-storyboard-formulaires-2026-11-06.md` (auto-vérification) puis validation indépendante du 6 novembre 2026 (23 constats, tous traités en v003) ; voir « Revue avant génération ».
- Correspondance machine : `fabrique-slides/runs/formulaires-opquast-v5/run.json`.

## Paramètres de série

- Guide commun : `fabrique-slides/docs/05-GUIDE-STYLE.md`, version 2.0.0 ; seules les exceptions déclarées ci-dessous s’en écartent.
- En-tête exact : haut gauche `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES` ; haut droit `Opquast` puis `DES SITES MEILLEURS POUR TOUS`.
- Footer principal exact : `RÈGLES OPQUAST · FORMULAIRES`.
- Annexes : aucune ; pas de footer d’annexe.
- Pagination : `NN / 63`.
- Badges : petit cartouche de règle sous le titre, aligné à droite, seulement sur les 30 slides de règle et les slides de distinction, au format `R. 69` ou `R. 69 · 70 · 77 · 78`. Aucun badge sur l’ouverture, le plan, le glossaire, la méthode, les checkpoints, l’évaluation finale, le grand cas et la conclusion. Exception : S60, débrief du grand cas, affiche en texte le numéro de règle de chaque repère, sans cartouche.
- Slogan : `Un bon formulaire laisse la main à l’utilisateur.` ; visible en S01 et S62 uniquement.
- Navigation : aucun badge d’acte, barre ou pastille, conformément au guide ; le plan (S03), le sous-titre « Acte N · <libellé> » de la première slide de chaque acte (S09, S24, S31, S38, S43, S51) et les titres situent l’apprenant.
- Palette, formes et typographie : celles du guide (fond blanc dominant, bleu marine pour la structure, vert pour la solution, orange pour la vigilance, rouge réservé aux erreurs).
- Format : 16:9, 1672 × 941 px, comme la série Sécurité.
- Références visuelles réellement disponibles : le guide commun ; aucune reprise d’un contenu de série.

## Exceptions au guide et justification

Statut : `DÉCIDÉ` le 6 novembre 2026 par Alex : le contrat de la Fabrique s’applique sans exception (`AGENTS.md` §3 et §8, `prompts/PROMPT-ACCORDEONS-SLIDES-OPQUAST.md`).

- Accordéons publiés : la transcription, qui décrit le PNG final, et le discours oral, qui explique. Les champs « Garantie recherchée » et « Contrôle et pièges » de chaque slide sont la matière de l’oral et des critères de revue ; ils ne sont pas publiés tels quels.
- Discours oral : il ne récite pas les numéros de règles et n’en fait pas mémoriser ; il désigne chaque règle par son objet. Les numéros restent dans les badges `R. NN`, les textes visibles, les corrigés et les métadonnées.

## Contrat de fabrication

- **Storyboard-first :** valider ce document, puis seulement générer les illustrations, les slides HTML et la publication ; ne pas automatiser une mise en ligne sans validation.
- **Séparation :** le « Texte visible » est à projeter, le « Discours oral » reste dans les notes du présentateur ; ne pas insérer le discours dans l’image.
- **Une illustration utile par slide**, originale ou correctement autorisée, jamais une image purement décorative ; conserver une alternative textuelle pertinente.
- **Accordéons publiés :** transcription du PNG et discours oral, selon le contrat de la Fabrique (voir « Exceptions au guide et justification »). Les champs « Garantie recherchée » et « Contrôle et pièges » nourrissent l’oral et la revue. Un corrigé figure uniquement dans le champ « Corrigé (notes du présentateur, non projeté) », sauf en S60, slide de correction du grand cas, qui projette les réponses après l’exercice.
- **Règle → préjudice → garantie :** citer le numéro et l’intitulé exact dans le badge et les métadonnées quand une règle est au centre ; à l’oral, désigner la règle par son objet, puis expliquer le risque utilisateur et le bénéfice attendu.
- **Pas de fil d’Ariane dans la présentation ;** progression claire par sections, titres de slides explicites, navigation clavier et accordéons utilisables par lecteurs d’écran.
- **QCM originaux :** réponses cachées pendant la projection ; chaque corrigé figure dans les notes du présentateur de sa slide. Le storyboard se suffit à lui-même : aucun fichier de corrigé externe n’est requis.
- **Sources :** intitulés issus de la checklist V5 publique, relus le 6 novembre 2026 et contenu pédagogique reformulé à partir du livre et des sources Opquast ; ne pas reproduire intégralement le livre.
- **RGAA :** les rapprochements sont informatifs, pas une équivalence normative ni une attestation de conformité.

## Arc pédagogique

| Acte | Slides | Intention |
|---|---|---|
| 0. Entrer dans l’histoire | S01–S08 | Installer le risque, le plan, la méthode et les 13 termes |
| 1. Comprendre les champs | S09–S23 | Nom, aide, contraintes, listes, type et autocomplete |
| 2. Saisir et s’authentifier | S24–S30 | Copier-coller, mots de passe, double facteur, boutons désactivés |
| 3. Corriger sans abandonner | S31–S37 | Identifier, expliquer, conserver et traduire les erreurs |
| 4. Savoir ce qui a été envoyé | S38–S42 | Récapitulatif, navigation et confirmation, puis règles transversales |
| 5. Gérer une démarche longue | S43–S50 | Documents, étapes, retour, historique, conservation |
| 6. S’entraîner pour la certification | S51–S63 | Transversalité, méthode, évaluation, grand cas, conclusion et ressources |

## Storyboard détaillé

### S01 — Le formulaire est « envoyé ». L’utilisateur a-t-il réussi ?

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** ouverture  
- **Durée indicative :** 1:00  
- **Objectif pédagogique :** Faire ressentir qu’un formulaire est un parcours, pas une collection de champs.

**Texte visible (projection) :** Une demande urgente. Un formulaire qui semble terminé. Et pourtant : aucune certitude, aucune preuve, aucune reprise. Slogan : « Un bon formulaire laisse la main à l’utilisateur. »

**Illustration unique :** Vue unique d’un parcours de formulaire en trois états : informations manquantes, erreur inexpliquée, écran final muet.
**Alternative textuelle à fournir :** Trois états successifs d’un formulaire qui ne permet pas de savoir si une demande a abouti.

**Règle → préjudice utilisateur :** L’utilisateur doit recommencer, contacte le support ou renonce à sa démarche.

**Garantie recherchée (matière de l’oral)**

Une démarche utilisable rend les attentes, les erreurs, le résultat et les étapes compréhensibles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire raconter au public ce qui bloque : avant, pendant et après l’envoi.
- Piège certification : Ne pas tout ramener à l’accessibilité du code : Opquast couvre aussi le résultat et les risques utilisateur.

**Discours oral du présentateur (non projeté)**

Imaginez que vous deviez envoyer un dossier ce soir. Les champs semblent remplis, vous cliquez sur Envoyer, et l’écran se recharge sans explication. Est-ce terminé ? Faut-il recommencer ? Notre question centrale sera celle-ci : est-ce que l’utilisateur peut avancer, corriger et être certain du résultat ? Nous allons suivre un même parcours et rattacher chaque problème aux bonnes règles Opquast.

**Mémo oral :** Un formulaire réussi n’est pas seulement un formulaire soumis.

---

### S02 — Notre contrat de réussite : reconnaître, distinguer, décider

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** objectif  
- **Durée indicative :** 0:50  
- **Objectif pédagogique :** Définir les compétences attendues pour la certification sans promettre l’examen réel.

**Texte visible (projection) :** 30 règles Opquast V5 ; 13 termes de glossaire ; 7 points d’entraînement ; 16 questions d’évaluation finale ; un mémo de révision.

**Illustration unique :** Un seul diagramme de progression : reconnaître une règle → distinguer des règles proches → choisir un contrôle → justifier.
**Alternative textuelle à fournir :** Progression d’apprentissage en quatre capacités, de la reconnaissance à la justification.

**Règle → préjudice utilisateur :** Mémoriser les numéros sans savoir reconnaître une situation concrète mène aux confusions.

**Garantie recherchée (matière de l’oral)**

La répétition par cas et les choix argumentés renforcent la compréhension durable.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Annoncer les questions de récupération espacée et le corrigé séparé des slides.
- Piège certification : Les QCM présentés sont des exercices originaux : ils ne sont pas des questions officielles de certification.

**Discours oral du présentateur (non projeté)**

L’objectif n’est pas de réciter trente lignes. Il faut savoir identifier la bonne règle à partir d’un défaut réel, la distinguer de sa voisine et comprendre ce qu’elle protège. Nous couvrirons intégralement la rubrique Formulaires de la V5, puis les règles transversales qui peuvent concerner le même parcours. Des questions originales vérifieront la compréhension, mais personne ne peut prédire toutes les questions d’un examen futur.

**Mémo oral :** Reconnaître → distinguer → vérifier → expliquer.

---

### S03 — Le plan : six actes après l’introduction

- **Acte :** 0. Entrer dans l’histoire
- **Type :** plan
- **Durée indicative :** 0:50
- **Objectif pédagogique :** Donner une vue d’ensemble de la formation, organisée selon le parcours de l’utilisateur.

**Texte visible (projection) :** 1 Comprendre les champs · 2 Saisir et s’authentifier · 3 Corriger sans abandonner · 4 Savoir ce qui a été envoyé · 5 Gérer une démarche longue · 6 S’entraîner pour la certification.

**Illustration unique :** Une frise unique en six segments numérotés qui suit le dossier Mon Atelier, de la page vide à la confirmation.
**Alternative textuelle à fournir :** Plan de la formation en six actes, ordonnés selon les moments d’un parcours de formulaire.

**Règle → préjudice utilisateur :** Sans vue d’ensemble, l’apprenant mémorise des numéros isolés sans savoir à quel moment du parcours ils interviennent.

**Garantie recherchée (matière de l’oral)**

Le plan suit l’ordre du parcours de l’utilisateur, pas l’ordre des numéros : chaque acte regroupe les règles qui protègent un même moment.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Annoncer le fonctionnement : chaque acte s’ouvre sur une slide sous-titrée de son nom et se termine par une distinction ou un point d’entraînement.
- Piège certification : L’ordre des numéros 69 à 98 ne suit pas le parcours : 92 à 98 se travaillent avec les champs et l’authentification, pas après la démarche longue.

**Discours oral du présentateur (non projeté)**

Voici notre plan. Il ne suit pas l’ordre des numéros, mais celui d’une personne qui remplit un dossier : comprendre les champs, saisir et s’authentifier, corriger après un refus, savoir ce qui a été envoyé, puis gérer une démarche en plusieurs étapes. Le dernier acte sert à s’entraîner : règles transversales, méthode de contrôle et questions d’évaluation. Le titre de chaque slide rappellera le moment du parcours.

**Mémo oral :** Six actes, un seul parcours.

---
### S04 — Le fil rouge : un dossier « Mon Atelier » en cinq moments

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** carte  
- **Durée indicative :** 0:50  
- **Objectif pédagogique :** Installer un scénario transversal réutilisable tout au long de la formation.

**Texte visible (projection) :** 1 Préparer · 2 Comprendre les champs · 3 Saisir · 4 Corriger · 5 Valider et reprendre.

**Illustration unique :** Frise unique du parcours fictif Mon Atelier : création de compte, choix d’une date, dépôt de dossier, validation, confirmation.
**Alternative textuelle à fournir :** Cinq moments d’une démarche fictive depuis la préparation jusqu’à la confirmation.

**Règle → préjudice utilisateur :** Une bonne page isolée ne suffit pas à rendre la démarche complète utilisable.

**Garantie recherchée (matière de l’oral)**

Le découpage temporel fait apparaître les erreurs qui ne se voient qu’en parcours.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : À chaque slide, situer le défaut avant, pendant ou après la saisie.
- Piège certification : Une règle Opquast applicable dans une autre thématique peut aussi concerner le formulaire.

**Discours oral du présentateur (non projeté)**

Nous utiliserons une démarche fictive appelée Mon Atelier. On prépare un dossier, on crée éventuellement un accès, on renseigne les informations, on corrige un rejet et on vérifie l’envoi. Ce fil rouge nous évitera trente exemples sans rapport. Vous verrez aussi qu’une règle sur les formulaires peut dialoguer avec les règles de navigation, de sécurité ou de contact.

**Mémo oral :** Le parcours est notre sommaire.

---

### S05 — Glossaire 1/3 : ce qui nomme et explique un champ

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** glossaire  
- **Durée indicative :** 1:15  
- **Objectif pédagogique :** Maîtriser quatre termes susceptibles de se confondre.

**Texte visible (projection) :** Étiquette = information sur le champ. Label = élément HTML. Placeholder = exemple provisoire. Information contextuelle = aide, contrainte ou erreur.

**Illustration unique :** Un seul champ avec quatre repères numérotés : texte d’étiquette, balise label, placeholder et consigne associée.
**Alternative textuelle à fournir :** Champ de formulaire dont quatre composants terminologiques sont identifiés.

**Règle → préjudice utilisateur :** Un exemple effaçable ou une aide mal reliée peuvent être pris à tort pour une véritable étiquette.

**Garantie recherchée (matière de l’oral)**

Les quatre termes permettent d’analyser le texte visible et la sémantique HTML séparément.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire associer chaque terme à son emplacement dans un champ.
- Piège certification : Étiquette et label ne sont pas synonymes stricts : l’un est la fonction, l’autre un mécanisme HTML. La V5 ne contient pas de règle dédiée au placeholder : une proposition en ce sens figurait au point d’étape d’avril 2025, mais elle n’est pas dans les 245 règles ; un placeholder utilisé comme seule étiquette se traite avec 69.

**Discours oral du présentateur (non projeté)**

Première famille : l’étiquette dit ce qu’on attend ; label est l’une des techniques HTML pour l’associer. Placeholder affiche un indice provisoire dans le champ, mais n’est pas l’étiquette. Enfin, une information contextuelle précise un format, une limite ou une erreur. En certification, identifiez d’abord quelle information fait défaut, puis demandez-vous si le problème est visuel ou programmatique.

**Mémo oral :** Étiquette ≠ label ≠ placeholder ≠ aide.

---

### S06 — Glossaire 2/3 : aides de saisie et états de contrôle

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** glossaire  
- **Durée indicative :** 1:00  
- **Objectif pédagogique :** Distinguer suggestion, calendrier et état désactivé.

**Texte visible (projection) :** Autocomplétion : suggestions. Datepicker : calendrier de saisie. Bouton désactivé : action visible mais momentanément impossible.

**Illustration unique :** Une composition unique de trois micro-composants contextualisés dans la même interface fictive.
**Alternative textuelle à fournir :** Suggestions de champ, calendrier ouvert et bouton désactivé dans un formulaire.

**Règle → préjudice utilisateur :** Un composant pratique en apparence peut ralentir ou exclure si son état est incompréhensible.

**Garantie recherchée (matière de l’oral)**

Identifier les mécanismes permet de poser le bon contrôle d’usage.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire décrire chaque composant et son état : suggestions pendant la saisie, calendrier, bouton indisponible.
- Piège certification : Pour Opquast, un champ qui propose des suggestions, y compris un champ de recherche, doit être signalé dans le code (97).

**Discours oral du présentateur (non projeté)**

Ici, le glossaire explique trois objets qu’on rencontre tous les jours. L’autocomplétion propose des valeurs pendant la saisie ; le datepicker affiche un calendrier, mais une saisie manuelle peut rester nécessaire. Enfin, un bouton peut être visuellement désactivé. La difficulté n’est pas seulement son aspect : il faut que les personnes qui utilisent un lecteur d’écran puissent comprendre sa présence et son état.

**Mémo oral :** Suggérer, choisir, signaler l’état.

---

### S07 — Glossaire 3/3 : consentement et démarche longue

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** glossaire  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Fixer les six derniers termes du glossaire de la rubrique.

**Texte visible (projection) :** Aperçu et prévisualisation · Chemin d’étapes et processus complexe · Opt-in et opt-out : trois couples, six termes.

**Illustration unique :** Une infographie unique en trois bandes : brouillon→aperçu ; chemin d’étapes ; case décochée/cochée.
**Alternative textuelle à fournir :** Trois paires de notions : prévisualisation, progression et consentement explicite ou implicite.

**Règle → préjudice utilisateur :** Confondre les notions empêche de savoir quand l’utilisateur a réellement le contrôle.

**Garantie recherchée (matière de l’oral)**

Le vocabulaire permet d’expliquer le moment de la décision et la nature du consentement.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner une définition orale courte de chacun des six termes.
- Piège certification : Le glossaire Opquast définit l’opt-in comme un consentement explicite, « généralement requis pour le traitement de données personnelles », et l’opt-out comme un consentement implicite ; aperçu et prévisualisation sont proches.

**Discours oral du présentateur (non projeté)**

Aperçu et prévisualisation désignent l’examen du résultat avant l’envoi. Un processus complexe est une démarche en plusieurs étapes et le chemin d’étapes indique leur succession et la position courante. Enfin, opt-in signifie accepter par une action explicite ; opt-out signifie devoir agir pour s’opposer. Le glossaire Opquast précise que l’opt-in est généralement requis pour le traitement de données personnelles.

**Mémo oral :** Prévoir, se situer, choisir.

---

### S08 — Une règle se lit avec trois questions

- **Acte :** 0. Entrer dans l’histoire  
- **Type :** methode  
- **Durée indicative :** 0:45  
- **Objectif pédagogique :** Installer la méthode constante de raisonnement Opquast.

**Texte visible (projection) :** Quel préjudice ? Que garantit la règle ? Comment vérifier : observer, utiliser, inspecter le code ?

**Illustration unique :** Un triangle de méthode aux trois sommets : préjudice utilisateur, garantie recherchée, preuve de vérification.
**Alternative textuelle à fournir :** Triangle reliant le préjudice, le bénéfice utilisateur et la méthode de contrôle.

**Règle → préjudice utilisateur :** Une conclusion tirée d’un seul indice visuel ou technique peut être erronée.

**Garantie recherchée (matière de l’oral)**

La vérification combine le rendu, le parcours et le code selon la règle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Annoncer les deux accordéons de chaque slide : la description de l’image et le discours oral.
- Piège certification : Pas de verdict RGAA implicite. Le RGAA et Opquast sont distincts.

**Discours oral du présentateur (non projeté)**

Notre méthode restera constante. Premièrement : quel ennui concret subit la personne ? Deuxièmement : quelle maîtrise la règle lui rend-elle ? Troisièmement : comment le vérifier ? Parfois il suffit de voir, parfois il faut réaliser une saisie erronée, parfois inspecter le code. Chaque slide affichera peu de texte ; deux accordéons donneront la description de l’image et le discours oral.

**Mémo oral :** Préjudice → garantie → contrôle.

---

### S09 — À quoi sert ce champ ?

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 69 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 69 :** « Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/69

**Sous-titre visible :** « Acte 1 · Comprendre les champs »

**Texte visible (projection) :** Le nom accessible doit désigner le rôle du champ : <label for="courriel">Courriel</label> + id="courriel".

**Illustration unique :** Deux champs visuellement semblables, l’un sans nom et l’autre muni de son étiquette reliée par un trait sémantique.
**Alternative textuelle à fournir :** Illustration du cas de la règle 69 : Deux champs visuellement semblables, l’un sans nom et l’autre muni de son étiquette reliée par un trait sémantique.

**Règle → préjudice utilisateur :** La personne ignore ce qu’elle doit fournir ; au lecteur d’écran, le champ peut être annoncé sans rôle compréhensible.

**Garantie recherchée (matière de l’oral)**

Chaque champ possède une étiquette qui lui est propre, reliée dans le code, pour savoir quoi saisir.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Inspecter l’association for/id ou le nom accessible alternatif ; tester aussi si cliquer l’étiquette cible le champ ; lire la pertinence du texte, que le contrôle officiel réserve à un examen manuel.
- Piège certification : Un placeholder seul n’est pas une étiquette ; la présence d’un label ne garantit pas qu’il soit pertinent.

**Discours oral du présentateur (non projeté)**

Premier acte : comprendre les champs, avant même de saisir quoi que ce soit. Pour le dossier Mon Atelier, imaginons deux cases vides sans indication. L’utilisateur voit des champs mais ne connaît pas les données attendues. La règle de l’étiquette associée demande une étiquette propre à chaque champ et reliée dans le code. On inspecte for et id, ou les mécanismes ARIA adaptés, puis on lit le texte. Retenez : le problème est d’abord l’identité du champ, pas la disposition de l’étiquette sur l’écran.

**Mémo oral :** Étiquette reliée dans le code : qui suis-je ?

**Question de réactivation :** Le libellé visible existe, mais le `for` pointe vers un autre id : quelle règle ?

---

### S10 — Ce que l’étiquette ne suffit pas à dire

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 70 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 70 :** « Les informations complétant l’étiquette d’un champ sont associées à celui-ci dans le code source. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/70

**Texte visible (projection) :** « Courriel » + « une adresse professionnelle, format attendu… » : l’aide doit être liée au champ dans le code.

**Illustration unique :** Un champ avec une aide visuelle reliée par aria-describedby ; une version sans association technique à côté.
**Alternative textuelle à fournir :** Illustration du cas de la règle 70 : Un champ avec une aide visuelle reliée par aria-describedby ; une version sans association technique à côté.

**Règle → préjudice utilisateur :** L’aide est visible, mais non restituée en contexte à une personne utilisant une technologie d’assistance.

**Garantie recherchée (matière de l’oral)**

Les consignes et messages complétant l’étiquette sont associés au champ.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Chercher aria-describedby, ou un fieldset/legend pertinent quand l’information concerne un groupe ; tester la résolution des références.
- Piège certification : 70 porte sur le rattachement programmatique des informations complémentaires, pas sur leur seule proximité visuelle (78).

**Discours oral du présentateur (non projeté)**

Le champ « Courriel » a une étiquette. Pourtant, un exemple ou une consigne peuvent être nécessaires. Si cette aide n’est qu’un paragraphe à côté, sa relation peut être perdue pour le lecteur d’écran. La règle de l’aide associée demande une association dans le code, souvent avec aria-describedby ; le livre mentionne aussi fieldset et legend pour les regroupements. Plus tard, la règle de la proximité visuelle de l’aide traitera la position à l’écran. C’est volontairement un contrôle différent.

**Mémo oral :** Aide reliée dans le code : quelle aide m’accompagne ?

**Question de réactivation :** Consigne visible sous le champ, aucun lien de code : association dans le code ou proximité à l’écran ?

---

### S11 — Une étiquette peut être correcte… mais trop loin

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 77 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 77 :** « Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/77

**Texte visible (projection) :** Le texte « Téléphone » doit paraître immédiatement associé à son champ, sur ordinateur comme sur mobile.

**Illustration unique :** Comparaison dessinée d’un formulaire avec libellé éloigné et d’un formulaire où il est juste au-dessus du champ.
**Alternative textuelle à fournir :** Illustration du cas de la règle 77 : Comparaison dessinée d’un formulaire avec libellé éloigné et d’un formulaire où il est juste au-dessus du champ.

**Règle → préjudice utilisateur :** L’utilisateur associe une information au mauvais champ ou perd du temps à retrouver la relation.

**Garantie recherchée (matière de l’oral)**

Une proximité visuelle claire et une position prévisible des étiquettes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Vérifier au rendu, sur toutes les tailles d’écran, la proximité immédiate (repère de la fiche : une trentaine de pixels au plus à gauche, un interligne au-dessus, quelques pixels pour une case radio ou à cocher) et la position prévisible : au-dessus ou à gauche du champ, à droite ou à gauche pour les cases radio et à cocher.
- Piège certification : Un bon for/id satisfait 69 mais ne suffit pas pour 77 ; la règle 77 porte sur le visuel.
- Avis de l’expert (livre, 4e édition 2026) : « une étiquette plus courte que les autres est alors séparée du champ correspondant par un blanc anormalement long » (formulaires à étiquettes alignées à gauche et champs alignés à droite).

**Discours oral du présentateur (non projeté)**

Notre champ est maintenant associé dans le code, mais l’étiquette est placée loin à gauche, séparée du champ par trois colonnes. L’association dans le code est résolue, pas la proximité à l’écran. La règle de la proximité visuelle de l’étiquette exige une proximité immédiate et une position prévisible, même sur petit écran : selon la fiche, une trentaine de pixels au plus à gauche, un interligne au-dessus. Les cases à cocher et les boutons radio suivent leurs propres usages. Ne déduisez jamais le respect de cette règle de la seule présence d’un label HTML.

**Mémo oral :** Étiquette proche à l’écran : où se trouve mon étiquette ?

**Question de réactivation :** Le label est bien relié mais éloigné visuellement : quelle règle ?

---

### S12 — Une aide éloignée est une aide perdue

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 78 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 78 :** « Les informations contextuelles se rapportant à un champ de formulaire lui sont visuellement rattachées. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/78

**Texte visible (projection) :** « 10 caractères maximum » et « corrigez cette erreur » doivent être affichés près du champ concerné.

**Illustration unique :** Zoom sur un formulaire : message d’erreur loin du champ à gauche, puis message correctement contigu.
**Alternative textuelle à fournir :** Illustration du cas de la règle 78 : Zoom sur un formulaire : message d’erreur loin du champ à gauche, puis message correctement contigu.

**Règle → préjudice utilisateur :** L’utilisateur ne sait plus quelle aide ou erreur concerne quelle valeur, notamment avec le zoom.

**Garantie recherchée (matière de l’oral)**

Les consignes et messages contextuels sont visuellement rattachés au champ.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Observer l’aide et les erreurs à plusieurs tailles et zooms, sans grands espaces ni association ambiguë.
- Piège certification : 70 = code ; 78 = proximité visuelle. Ne pas confondre avec 77 qui porte sur l’étiquette elle-même.

**Discours oral du présentateur (non projeté)**

Une erreur peut être présente et techniquement associée, mais placée tout en bas d’un écran très long. Pour une personne qui agrandit, cette information est pratiquement perdue. La règle de la proximité visuelle de l’aide porte sur les aides, contraintes et messages d’erreur. Par comparaison, ses trois voisines traitent la proximité de l’étiquette à l’écran, l’association de l’aide dans le code et celle de l’étiquette dans le code. Ce quadruplet sera notre premier moyen mnémotechnique.

**Mémo oral :** Aide proche à l’écran : où est l’aide ?

**Question de réactivation :** Information d’aide liée par aria-describedby mais éloignée : règle principale ?

---

### S13 — Le carré d’or : 69 / 70 / 77 / 78

- **Acte :** 1. Comprendre les champs  
- **Type :** distinction  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Savoir identifier immédiatement les quatre contrôles voisins.

**Texte visible (projection) :** 69 étiquette dans le code · 70 aide dans le code · 77 étiquette à l’écran · 78 aide à l’écran.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Matrice deux par deux unique avec colonnes « étiquette / aide » et lignes « code / écran ».
**Alternative textuelle à fournir :** Matrice des règles 69, 70, 77 et 78 selon le type d’information et la modalité de rattachement.

**Règle → préjudice utilisateur :** En certification, remplacer « associé dans le code » par « visuellement proche » change complètement la règle.

**Garantie recherchée (matière de l’oral)**

Quatre critères orthogonaux : savoir quoi saisir et retrouver les aides, à l’écran comme dans le code.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lire quatre mini-défaillances ; demander un numéro pour chacune : label sans for, aide sans référence, label loin, aide loin.
- Piège certification : Un même champ peut violer plusieurs règles. Choisir celle que décrit précisément l’énoncé.

**Discours oral du présentateur (non projeté)**

C’est sans doute l’une des distinctions les plus rentables à mémoriser. À gauche : l’étiquette et les informations qui la complètent. En haut : le code et l’écran. Cela produit quatre cases : étiquette dans le code, aide dans le code, étiquette à l’écran, aide à l’écran. Si l’énoncé parle de relation programmatique, regardez le code. S’il parle de proximité, regardez l’écran. S’il parle d’étiquette, distinguez association et proximité de l’étiquette. S’il parle d’aide, faites de même pour l’aide.

**Mémo oral :** Code : étiquette et aide reliées. Écran : étiquette et aide proches.

**Question de réactivation :** Un `aria-describedby` correct avec un message à 5 écrans du champ : quel contrôle reste à discuter ?

---

### S14 — Obligatoire : dites-le avant de demander

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 71 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 71 :** « L’étiquette de chaque champ de formulaire indique si la saisie est obligatoire. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/71

**Texte visible (projection) :** « Nom (obligatoire) » ; si un astérisque est utilisé, expliquer sa signification avant le formulaire.

**Illustration unique :** Étiquette de champ obligatoire explicite et exemple d’astérisque avec sa légende générale.
**Alternative textuelle à fournir :** Illustration du cas de la règle 71 : Étiquette de champ obligatoire explicite et exemple d’astérisque avec sa légende générale.

**Règle → préjudice utilisateur :** La personne découvre après l’envoi qu’un champ était obligatoire.

**Garantie recherchée (matière de l’oral)**

Chaque utilisateur connaît l’obligation de saisie en amont.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Vérifier étiquettes et indications associées ; tenter la validation d’un champ non marqué obligatoire.
- Piège certification : L’attribut required seul n’est pas une indication visible suffisante ; l’absence d’indication doit correspondre à un champ réellement facultatif.

**Discours oral du présentateur (non projeté)**

Dans Mon Atelier, pourquoi apprendre que le téléphone est obligatoire seulement après le premier envoi ? La règle du caractère obligatoire signalé vise l’anticipation. L’obligation doit apparaître dans l’étiquette ou une indication associée. Si l’on utilise une étoile, il faut en expliquer le sens. Le contrôle ne se résume pas à repérer required dans le code : il faut aussi valider avec un champ non signalé obligatoire et vérifier qu’il est effectivement facultatif.

**Mémo oral :** Obligatoire signalé : dois-je répondre ?

**Question de réactivation :** Un champ `required` sans indication compréhensible : est-ce suffisant ?

---

### S15 — Format : ne transformez pas une devinette en erreur

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 72 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 72 :** « Le format de saisie des champs de formulaire qui le nécessitent est indiqué. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/72

**Texte visible (projection) :** « Date de naissance (JJ/MM/AAAA) ». Un format imposé doit être annoncé avant validation.

**Illustration unique :** Une date refusée avec un message opaque, comparée à une indication de format donnée en amont.
**Alternative textuelle à fournir :** Illustration du cas de la règle 72 : Une date refusée avec un message opaque, comparée à une indication de format donnée en amont.

**Règle → préjudice utilisateur :** L’utilisateur doit deviner la syntaxe acceptée par le système.

**Garantie recherchée (matière de l’oral)**

Le format attendu des champs qui le nécessitent est explicite.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Saisir des formats différents pour découvrir les contraintes réelles ; vérifier leur annonce dans l’étiquette ou l’aide associée.
- Piège certification : Le `type="date"` (95) ne remplace pas systématiquement l’explication de format quand celle-ci est nécessaire.

**Discours oral du présentateur (non projeté)**

Vous entrez la date avec des tirets, mais la page exige 29/10/2026. Ce n’est pas à l’utilisateur d’en deviner les séparateurs. La règle du format annoncé prévoit de donner le format pour les champs qui l’exigent, avant validation. On provoque un rejet de format, puis on cherche une indication utile associée au champ. Attention : il ne s’agit ni du caractère obligatoire, ni de la longueur maximale, ni d’un détail de type HTML.

**Mémo oral :** Format annoncé : sous quelle forme ?

**Question de réactivation :** Un formulaire refuse AAAA-MM-JJ sans indiquer JJ/MM/AAAA : quelle règle ?

---

### S16 — La casse : quand « ABC » n’est pas « abc »

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 73 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 73 :** « L’utilisateur est averti lorsqu’une saisie est sensible à la casse. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/73

**Texte visible (projection) :** « Code d’accès : respecter les majuscules et minuscules. »

**Illustration unique :** Deux saisies identiques sauf la casse, avec acceptation et refus explicités.
**Alternative textuelle à fournir :** Illustration du cas de la règle 73 : Deux saisies identiques sauf la casse, avec acceptation et refus explicités.

**Règle → préjudice utilisateur :** Une valeur pourtant plausible est rejetée sans explication compréhensible.

**Garantie recherchée (matière de l’oral)**

L’utilisateur est averti si le système distingue majuscules et minuscules.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Tester des variantes de casse ; si l’application rejette en raison de la casse, vérifier que l’étiquette avertit.
- Piège certification : La règle 73 ne signifie pas que tous les champs doivent être insensibles à la casse.
- Avis de l’expert (livre, 4e édition 2026) : « Cette règle joue parfois un rôle majeur, en particulier dans l’ergonomie des captchas graphiques. C’est également le cas pour la saisie des identifiants et mots de passe. »

**Discours oral du présentateur (non projeté)**

Voici un code d’invitation : AbC123. Si le système refuse abc123 parce qu’il distingue les majuscules, il faut le dire. C’est exactement l’objet de la règle de la casse. Le défaut n’est pas le format général, traité par la règle du format, ni la longueur, traitée par celle de la longueur maximale. On teste des valeurs ne différant que par les capitales puis on vérifie si cette sensibilité est annoncée auprès du champ.

**Mémo oral :** Casse annoncée : les majuscules comptent-elles ?

**Question de réactivation :** Un code saisi en minuscules échoue sans avertissement : format ou casse ?

---

### S17 — La longueur maximale : prévenir avant la troncature

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 74 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 74 :** « L’étiquette de chaque champ de formulaire qui le nécessite indique les limites de nombre de caractères. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/74

**Texte visible (projection) :** « Message (250 caractères maximum) ». Le seuil est présenté dans l’étiquette ou l’aide liée.

**Illustration unique :** Champ de message affichant « 250 caractères maximum » avant la saisie, opposé à une coupure silencieuse.
**Alternative textuelle à fournir :** Illustration du cas de la règle 74 : Champ de message affichant « 250 caractères maximum » avant la saisie, opposé à une coupure silencieuse.

**Règle → préjudice utilisateur :** Le texte peut être perdu, raccourci ou rejeté après un long effort de saisie.

**Garantie recherchée (matière de l’oral)**

Les limites en nombre de caractères des champs concernés sont annoncées.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Tester la longueur acceptée et sa cohérence avec l’indication, y compris via un message associé.
- Piège certification : Un compteur ne suffit que s’il indique le maximum et qu’il est associé au champ dans le code ; un compteur seulement visuel, ou sans maximum, ne suffit pas.

**Discours oral du présentateur (non projeté)**

Camille écrit un long commentaire et découvre qu’il ne fallait pas dépasser 250 caractères. La règle de la longueur maximale annoncée aurait évité cette surprise. On annonce la limite en amont, dans l’étiquette ou une information explicitement associée. Le contrôle est direct : on vérifie la limitation imposée et l’information donnée à la personne. Ce n’est pas la même chose que la règle du format, qui parle de la forme de la valeur.

**Mémo oral :** Longueur annoncée : combien de caractères ?

**Question de réactivation :** Un champ refuse le 251e caractère sans annoncer le maximum : quelle règle ?

---

### S18 — Quatre questions à poser avant toute saisie

- **Acte :** 1. Comprendre les champs  
- **Type :** distinction  
- **Durée indicative :** 1:00  
- **Objectif pédagogique :** Fixer les distinctions 71 à 74 sans confusion.

**Texte visible (projection) :** 71 Dois-je saisir ? · 72 Quel format ? · 73 Quelle casse ? · 74 Quelle longueur ?
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Un aide-mémoire unique en quatre cadrans autour d’un champ : obligatoire, format, majuscules, longueur.
**Alternative textuelle à fournir :** Aide-mémoire à quatre cadrans sur les contraintes de saisie.

**Règle → préjudice utilisateur :** Les restrictions découvertes après coup font multiplier les envois et les abandons.

**Garantie recherchée (matière de l’oral)**

Chaque contrainte est compréhensible au moment opportun.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Présenter les quatre défauts dans le désordre et demander le bon numéro.
- Piège certification : Une règle peut requérir à la fois un contrôle de l’application et de l’information présentée.

**Discours oral du présentateur (non projeté)**

Avant de saisir, il y a quatre questions simples : est-ce que je dois répondre ? Sous quel format ? Les majuscules comptent-elles ? Combien de caractères puis-je écrire ? Dans cet ordre, retenez obligation, format, casse, longueur. C’est un petit bloc facile à mémoriser ; ces quatre dimensions se confondent vite quand un énoncé n’en décrit qu’une.

**Mémo oral :** Obligation / Format / Casse / Longueur.

---

### S19 — Le bon type HTML aide aussi sur mobile

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 95 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 95 :** « Les champs de saisie de type e-mail, URL, téléphone, nombre, recherche, mots de passe, heure et date sont dotés du type approprié. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/95

**Texte visible (projection) :** Courriel → type=email ; téléphone → tel ; recherche → search ; date → date ; heure → time.

**Illustration unique :** Un téléphone mobile avec clavier adapté au type tel, à côté d’un champ d’adresse avec clavier e-mail.
**Alternative textuelle à fournir :** Illustration du cas de la règle 95 : Un téléphone mobile avec clavier adapté au type tel, à côté d’un champ d’adresse avec clavier e-mail.

**Règle → préjudice utilisateur :** Le clavier proposé est inadapté, la saisie plus difficile et certaines validations natives inutilisées.

**Garantie recherchée (matière de l’oral)**

Les champs concernés utilisent un type HTML correspondant aux données attendues.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Inspecter l’attribut type des input : email, url, tel, number, search, password, date, time.
- Piège certification : Le type tel ne se remplace pas par number ; type correct (95) ≠ autocomplete correct (97).

**Discours oral du présentateur (non projeté)**

Sur mobile, saisir un téléphone dans un champ number est inutilement compliqué et peut poser des problèmes. La règle des types de champs demande d’utiliser les bons types HTML : email, url, tel, number, search, password, date et time. Il s’agit du type de donnée et du clavier adapté. La règle de l’autocomplétion est autre chose : elle informe le navigateur de la finalité d’un champ et facilite le remplissage automatique.

**Mémo oral :** Type adapté : quel clavier et quel type ?

**Question de réactivation :** Adresse électronique en type=text, mais autocomplete=email : quelle règle manque ?

---

### S20 — L’autocomplétion se prépare dans le code

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 97 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 97 :** « Les champs permettant l’autocomplétion sont signalés dans le code source. »  
- **Statut V5 :** règle ajoutée en V5 (article Opquast « Publication de la version 5 », 2 octobre 2025).
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/97

**Texte visible (projection) :** autocomplete="email", "given-name", "family-name", "tel" : les jetons doivent correspondre aux données.

**Illustration unique :** Formulaire montrant des suggestions de données pertinentes et un zoom sur l’attribut autocomplete relié au champ.
**Alternative textuelle à fournir :** Illustration du cas de la règle 97 : Formulaire montrant des suggestions de données pertinentes et un zoom sur l’attribut autocomplete relié au champ.

**Règle → préjudice utilisateur :** L’utilisateur répète inutilement ses données ou reçoit des propositions inadaptées.

**Garantie recherchée (matière de l’oral)**

Les champs concernés sont explicitement identifiés pour le remplissage automatique.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Vérifier la présence et la valeur normalisée de autocomplete, puis sa pertinence pour le champ.
- Piège certification : Autocomplete HTML (97) ≠ type HTML (95). La règle 97 couvre tout champ qui propose une autocomplétion, y compris un champ de recherche : il doit être signalé dans le code.
- Avis de l’expert (livre, 4e édition 2026) : « il est important de désactiver l’autocomplétion […] uniquement pour les champs sensibles (mots de passe, codes uniques), afin de ne pas priver inutilement l’utilisateur d’un confort attendu. »

**Discours oral du présentateur (non projeté)**

Le navigateur peut remplir seul une adresse e-mail ou un prénom, à condition de connaître la finalité du champ. C’est ce que décrit la règle de l’autocomplétion, via l’attribut autocomplete et un jeton normalisé. On vérifie la valeur de cet attribut, pas seulement l’affichage de suggestions. À la certification, ne confondez pas type=email, qui concerne le type du champ, et autocomplete=email, qui concerne sa finalité de remplissage.

**Mémo oral :** Autocomplétion : quelles données puis-je préremplir ?

**Question de réactivation :** type=email et aucune valeur autocomplete : quelle exigence reste à traiter ?

---

### S21 — Une liste longue doit avoir des groupes

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 93 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 93 :** « Les éléments d’une liste déroulante qui peuvent être regroupés le sont de manière appropriée. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/93

**Texte visible (projection) :** Dans un select : <optgroup label="France">…</optgroup> pour des ensembles qui gagnent à être regroupés.

**Illustration unique :** Menu déroulant de lieux groupés par région, avec une liste désordonnée opposée en arrière-plan.
**Alternative textuelle à fournir :** Illustration du cas de la règle 93 : Menu déroulant de lieux groupés par région, avec une liste désordonnée opposée en arrière-plan.

**Règle → préjudice utilisateur :** Les options d’une liste longue deviennent difficiles à comprendre et à parcourir.

**Garantie recherchée (matière de l’oral)**

Les regroupements thématiques pertinents sont structurés et nommés.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Observer si la liste appelle des groupes, puis vérifier optgroup et son label dans le code.
- Piège certification : 93 = structurer par groupes ; 94 = définir un ordre identifiable, y compris au sein des groupes.
- Avis de l’expert (livre, 4e édition 2026) : Les fausses options vides servant de séparateurs sont un artifice purement visuel : « L’élément optgroup et son attribut label répondent en fait exactement à ce besoin, mais de manière accessible et sémantique. »

**Discours oral du présentateur (non projeté)**

Pour Mon Atelier, une liste de 60 villes peut être structurée par région. Ce n’est pas seulement une question de présentation : optgroup avec un label permet de représenter une organisation en code. La règle des groupes d’options ne force pas à regrouper toute petite liste ; elle s’applique lorsque des options pourraient utilement l’être. Ensuite il faut contrôler que chaque groupe possède un intitulé clair. Le classement des options reste un autre sujet.

**Mémo oral :** Groupes d’options : quels groupes ?

**Question de réactivation :** La liste est alphabétique mais mélange soixante-dix options de deux catégories : quel risque Opquast ?

---

### S22 — Une liste doit avoir un ordre repérable

- **Acte :** 1. Comprendre les champs  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 94 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 94 :** « Les listes d’options de formulaires sont présentées dans un ordre identifiable. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/94

**Texte visible (projection) :** Mois : janvier → décembre. Pays : ordre alphabétique. Dates : ordre chronologique.

**Illustration unique :** Menu déroulant unique : mois mélangés à gauche, mois en ordre chronologique à droite.
**Alternative textuelle à fournir :** Illustration du cas de la règle 94 : Menu déroulant unique : mois mélangés à gauche, mois en ordre chronologique à droite.

**Règle → préjudice utilisateur :** L’utilisateur passe trop de temps à chercher une option sans logique de classement.

**Garantie recherchée (matière de l’oral)**

L’ordre des options est compréhensible et identifiable.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Ouvrir chaque select, observer si l’ordre alphabétique, chronologique, numérique ou thématique est reconnaissable.
- Piège certification : 94 n’impose pas systématiquement l’alphabet : tout ordre identifiable et adapté au contenu peut convenir.

**Discours oral du présentateur (non projeté)**

Voici la liste des mois : mars, décembre, janvier, octobre. Elle fonctionne techniquement, mais la recherche est inutilement coûteuse. La règle de l’ordre des options demande un ordre identifiable. Ce peut être un ordre alphabétique, chronologique, numérique ou thématique. Ne lisez pas cette règle comme une exigence d’ordre alphabétique universel. La règle des groupes d’options porte sur les groupes, celle de l’ordre sur l’ordre des éléments ; les deux peuvent s’appliquer en même temps.

**Mémo oral :** Ordre repérable : dans quel ordre ?

**Question de réactivation :** Liste regroupée par région mais pays mélangés sans logique : groupes ou ordre ?

---

### S23 — Checkpoint 1 : listes, type, remplissage

- **Acte :** 1. Comprendre les champs  
- **Type :** quiz  
- **Durée indicative :** 1:30  
- **Objectif pédagogique :** Réactiver 93/94/95/97 en situations distinctes.

**Texte visible (projection) :** Un select non regroupé, des choix sans ordre, type=text sur téléphone, autocomplete incorrect. Quels numéros ?

**Illustration unique :** Une planche unique de quatre exemples de champs annotés A, B, C, D sans donner les réponses.
**Alternative textuelle à fournir :** Quatre contrôles de saisie à classer : groupe, ordre, type et remplissage automatique.

**Règle → préjudice utilisateur :** Une apparence correcte peut cacher plusieurs problèmes de nature différente.

**Garantie recherchée (matière de l’oral)**

La classification en quatre causes évite les réponses réflexes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Laisser chaque groupe argumenter, puis donner la correction à l’oral.
- Piège certification : Ne pas dévoiler la correction sur la slide : elle figure dans les notes du présentateur.

**Corrigé (notes du présentateur, non projeté) :** A=93 ; B=94 ; C=95 ; D=97.

**Discours oral du présentateur (non projeté)**

On consolide maintenant quatre règles qui peuvent se croiser sur un formulaire. A, la liste ne représente pas ses groupes. B, les options ne suivent aucun ordre. C, le type HTML ne correspond pas à la donnée. D, le champ ne peut pas être identifié pour le remplissage automatique. Nommez-moi les règles et surtout la différence de problème : structure, ordre, type, finalité.

**Mémo oral :** Groupes, ordre, type, autocomplétion.

**Question de réactivation :** A, B, C, D : quelle règle pour chacun, et quelle différence de problème ?

---

### S24 — Copier et coller fait partie de la saisie normale

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 92 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 92 :** « Le copier-coller est possible dans les champs de formulaire. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/92

**Sous-titre visible :** « Acte 2 · Saisir et s’authentifier »

**Texte visible (projection) :** Un mot de passe doit pouvoir être collé depuis son gestionnaire ; le collage reste possible dans les autres champs.

**Illustration unique :** Deux états d’un champ de mot de passe : paste bloqué par script, puis paste autorisé avec gestionnaire.
**Alternative textuelle à fournir :** Illustration du cas de la règle 92 : Deux états d’un champ de mot de passe : paste bloqué par script, puis paste autorisé avec gestionnaire.

**Règle → préjudice utilisateur :** Une personne doit retaper une valeur complexe ou peut être totalement bloquée.

**Garantie recherchée (matière de l’oral)**

Le copier-coller fonctionne dans les champs de formulaire, y compris les mots de passe.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Tester copier, couper et coller au clavier ou via menu contextuel ; chercher les interceptions onpaste, keydown, oncopy et oncut, citées par la fiche.
- Piège certification : L’avis de l’expert demande d’évaluer la règle selon d’éventuelles contraintes de sécurité spécifiques, mais la juge « absolument décisive » pour les champs de mot de passe ; 92 est distincte de 75 et 76.
- Avis de l’expert (livre, 4e édition 2026) : « Lorsque vous empêchez le copier-coller d’un mot de passe, vous nuisez à l’utilisation de gestionnaire de mots de passe et vous incitez à choisir des mots de passe simples et donc moins solides. »

**Discours oral du présentateur (non projeté)**

Deuxième acte : saisir et s’authentifier. Dans une newsletter de 2024, Élie Sloïm rapporte les mots d’une amie aveugle : quand le collage est interdit, elle est totalement bloquée ; l’interdiction peut aussi empêcher d’utiliser un gestionnaire de mots de passe. Ce n’est pas un confort superflu. La règle du copier-coller exige de pouvoir copier et coller dans les champs, y compris les mots de passe. On teste le comportement réel, pas seulement l’absence d’un attribut. Et on ne la confond pas avec la prévention des erreurs de création.

**Mémo oral :** Copier-coller : je peux coller.

**Question de réactivation :** Un script onpaste bloque le mot de passe : quelle règle ?

---

### S25 — Créer un mot de passe sans le créer par erreur

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 75 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 75 :** « La création d’un mot de passe par l’utilisateur fait l’objet d’un mécanisme de prévention des erreurs de saisie. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/75

**Texte visible (projection) :** À la création d’un mot de passe, proposer un mécanisme de prévention des fautes de saisie.

**Illustration unique :** Écran de création de compte avec deux champs de mot de passe comparés et un message signalant leur différence.
**Alternative textuelle à fournir :** Illustration du cas de la règle 75 : Écran de création de compte avec deux champs de mot de passe comparés et un message signalant leur différence.

**Règle → préjudice utilisateur :** La personne ne mémorise pas le mot de passe réellement enregistré et perd immédiatement l’accès.

**Garantie recherchée (matière de l’oral)**

La création du mot de passe inclut une prévention des erreurs.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Créer un compte et vérifier la présence de deux champs successifs comparés à la soumission, comme le prévoit le contrôle officiel ; noter l’affichage en clair ou un lien de connexion unique comme des solutions alternatives citées par la fiche.
- Piège certification : La mise en œuvre cite des pistes non limitatives (double saisie, affichage en clair, lien ou code de connexion unique), mais le contrôle officiel vérifie la présence systématique d’une double saisie : en audit, c’est ce contrôle qui fait foi. Ne pas désactiver le collage dans la confirmation (92).

**Discours oral du présentateur (non projeté)**

On vient de créer un compte. Le mot de passe est masqué, on se trompe d’un caractère et personne ne le remarque. La règle de la prévention des erreurs de création demande un mécanisme pour prévenir cette erreur au moment de la création. La fiche cite plusieurs pistes, dont l’affichage en clair, mais son contrôle vérifie une double saisie comparée : en audit, c’est ce contrôle qui fait foi. La question porte sur la prévention de la création erronée, pas encore sur la possibilité générale d’afficher les caractères en clair.

**Mémo oral :** Création du mot de passe : prévenir l’erreur.

**Question de réactivation :** La création de compte ne propose qu’un seul champ de mot de passe, sans confirmation : quelle règle le contrôle officiel invalide-t-il ?

---

### S26 — Je choisis de voir mon mot de passe

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 76 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 76 :** « Les caractères saisis dans un champ de mot de passe peuvent être affichés en clair. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/76

**Texte visible (projection) :** Un contrôle « Afficher le mot de passe » permet de vérifier les caractères saisis.

**Illustration unique :** Champ de mot de passe avec bouton afficher/masquer, un seul état illustré en zoom.
**Alternative textuelle à fournir :** Illustration du cas de la règle 76 : Champ de mot de passe avec bouton afficher/masquer, un seul état illustré en zoom.

**Règle → préjudice utilisateur :** L’utilisateur ignore ce qu’il a tapé, notamment sur clavier virtuel ou avec une technologie d’assistance.

**Garantie recherchée (matière de l’oral)**

Les caractères peuvent être révélés à la demande de l’utilisateur.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Actionner l’affichage en clair puis le masquage ; vérifier que la valeur est préservée.
- Piège certification : 76 = révélation ; 75 = prévention à la création ; 92 = copier-coller.
- Avis de l’expert (livre, 4e édition 2026) : « L’applicabilité de cette règle est à estimer selon les contextes où des impératifs spécifiques de sécurité s’imposent. »

**Discours oral du présentateur (non projeté)**

Sur un clavier mobile, les erreurs de frappe sont fréquentes. Avec la règle de l’affichage du mot de passe, la personne peut décider d’afficher ce qu’elle a saisi. Le contrôle peut basculer le type HTML entre password et text. Nous vérifions réellement que cela marche et que le mot de passe ne change pas pendant la bascule. Ce contrôle aide aussi à la prévention, mais cette règle est spécifiquement celle de la visibilité des caractères.

**Mémo oral :** Affichage en clair : je peux voir les caractères.

**Question de réactivation :** Deux champs de confirmation sans bouton Afficher : règle de la prévention satisfaite ? règle de l’affichage satisfaite ?

---

### S27 — Code expiré : pouvoir recommencer la double authentification

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 96 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 96 :** « Les procédures d’authentification à double facteur peuvent être relancées. »  
- **Statut V5 :** règle ajoutée en V5 (article Opquast « Publication de la version 5 », 2 octobre 2025).
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/96

**Texte visible (projection) :** Si un code à usage unique arrive trop tard, un moyen « Renvoyer le code » doit être disponible.

**Illustration unique :** Flux d’authentification à deux facteurs avec code expiré, puis lien de relance accessible.
**Alternative textuelle à fournir :** Illustration du cas de la règle 96 : Flux d’authentification à deux facteurs avec code expiré, puis lien de relance accessible.

**Règle → préjudice utilisateur :** L’utilisateur perd la possibilité d’entrer sur son compte après un échec de réception du code.

**Garantie recherchée (matière de l’oral)**

La procédure de double authentification peut être relancée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lancer une procédure de test autorisée et vérifier qu’il existe un moyen fonctionnel d’obtenir un nouveau code.
- Piège certification : Une autre méthode d’authentification est une recommandation complémentaire ; la règle 96 vise la relance.

**Discours oral du présentateur (non projeté)**

Mon Atelier envoie un code de connexion. Le réseau est mauvais et le code expire. S’il n’existe aucun moyen de le renvoyer, la démarche est bloquée. C’est la règle du renvoi du code. Elle n’a rien à voir avec l’affichage du mot de passe : elle vise une procédure à double facteur. Au-delà de la règle, Opquast suggère plusieurs canaux possibles, mais le contrôle central est simple : la procédure peut-elle être relancée ?

**Mémo oral :** Renvoi du code : nouveau code, nouvelle chance.

**Question de réactivation :** Le code de validation n’arrive pas ; pas de bouton de relance : quelle règle ?

---

### S28 — Un bouton désactivé doit rester compréhensible

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 98 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 98 :** « Les boutons désactivés ne sont pas masqués aux lecteurs d’écran. »  
- **Statut V5 :** règle ajoutée en V5 (article Opquast « Publication de la version 5 », 2 octobre 2025).
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/98

**Texte visible (projection) :** « Continuer » indisponible : sa présence, son état et la raison du blocage doivent être compréhensibles.

**Illustration unique :** Bouton Continuer désactivé mais explicite, associé à un message expliquant l’étape manquante.
**Alternative textuelle à fournir :** Illustration du cas de la règle 98 : Bouton Continuer désactivé mais explicite, associé à un message expliquant l’étape manquante.

**Règle → préjudice utilisateur :** Une personne utilisant un lecteur d’écran ne sait pas qu’une action existe ni pourquoi elle ne fonctionne pas.

**Garantie recherchée (matière de l’oral)**

Les boutons momentanément désactivés restent perceptibles et leur état intelligible.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Inspecter le code (pas d’attribut disabled ; aria-disabled est la solution proposée), puis tester au clavier et au lecteur d’écran que le bouton reste atteignable, annoncé comme indisponible, et que la raison est restituée.
- Piège certification : Pour Opquast, l’attribut HTML disabled fait échouer la règle : le contrôle officiel vérifie que les boutons désactivés en cours de saisie ne l’utilisent pas. Solution attendue : aria-disabled="true", action bloquée par script, raison exposée par aria-describedby ou aria-label.
- Avis de l’expert (livre, 4e édition 2026) : « certains lecteurs d’écran ignorent totalement les éléments marqués ainsi et ne les annoncent pas à l’utilisateur. Résultat : une personne non-voyante ne saura même pas qu’une action est prévue à cet endroit de l’interface. »

**Discours oral du présentateur (non projeté)**

Le bouton Continuer est gris et ne peut pas être activé. Si le lecteur d’écran l’ignore, l’utilisateur ne comprend pas le chemin vers la suite. La règle des boutons désactivés demande de rendre perceptibles l’existence et l’état du bouton. La solution Opquast propose de conserver un bouton atteignable avec aria-disabled et de bloquer réellement son action par script. Retenez la conséquence pour l’examen : un bouton doté de l’attribut disabled échoue au contrôle de cette règle, car il sort du parcours au clavier.

**Mémo oral :** Bouton désactivé : une action indisponible reste identifiable.

**Question de réactivation :** Un bouton grisé disparaît du parcours lecteur d’écran : quelle règle ?

---

### S29 — Le piège des mots de passe : cinq règles, cinq intentions

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** distinction  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Ne pas confondre prévenir, révéler, coller, relancer et expliquer l’indisponibilité.

**Texte visible (projection) :** 75 prévenir l’erreur · 76 afficher · 92 copier/coller · 96 relancer un code · 98 expliquer un bouton désactivé.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Cinq vignettes réunies dans un seul parcours de connexion, avec cinq points de friction numérotés.
**Alternative textuelle à fournir :** Parcours de connexion découpé en cinq difficultés et cinq réponses Opquast.

**Règle → préjudice utilisateur :** Une solution utile ne remplace pas automatiquement un autre dispositif attendu.

**Garantie recherchée (matière de l’oral)**

Chaque règle protège une capacité différente, à un moment du parcours.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Proposer cinq mini-cas en ordre aléatoire ; faire citer les numéros et les moments.
- Piège certification : Les règles 201 à 205, situées en Sécurité, sont des compléments, pas des doublons de cette série.

**Discours oral du présentateur (non projeté)**

L’un des grands pièges de cette rubrique est de tout mélanger sous « mot de passe accessible ». Pourtant, créer un mot de passe sans faute relève de la prévention ; afficher les caractères, de l’affichage en clair ; coller depuis un gestionnaire, du copier-coller ; demander un nouveau code, du renvoi ; comprendre pourquoi Continuer est inactif, du bouton désactivé. En certification, partez de l’action qui manque réellement à la personne.

**Mémo oral :** Prévenir / voir / coller / relancer / comprendre.

---

### S30 — Checkpoint 2 : choisissez la bonne règle

- **Acte :** 2. Saisir et s’authentifier  
- **Type :** quiz  
- **Durée indicative :** 2:00  
- **Objectif pédagogique :** Renforcer la récupération active des règles de l’acte 2.

**Texte visible (projection) :** A. Collage bloqué dans le champ mot de passe. B. Impossible d’afficher le mot de passe saisi. C. « Continuer » désactivé par l’attribut disabled, introuvable au clavier. D. Création de compte : un seul champ de mot de passe.

**Illustration unique :** Planche unique de quatre situations A–D : collage refusé, champ masqué sans bouton d’affichage, bouton Continuer grisé hors du parcours au clavier, création de compte à champ unique.
**Alternative textuelle à fournir :** Quatre situations d’authentification proposées au public sans afficher la correction.

**Règle → préjudice utilisateur :** Le choix automatique de la « règle la plus familière » cache les distinctions.

**Garantie recherchée (matière de l’oral)**

Les apprenants justifient chaque réponse par les mots précis de l’énoncé.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire voter, puis dévoiler la correction à l’oral après discussion.
- Piège certification : Ne pas tout ramener à « mot de passe sécurisé » : ces quatre situations relèvent de quatre règles distinctes.

**Corrigé (notes du présentateur, non projeté) :** A=92 ; B=76 ; C=98 (le contrôle officiel vérifie l’absence de l’attribut disabled) ; D=75 (le contrôle officiel vérifie la double saisie).

**Discours oral du présentateur (non projeté)**

Quatre scènes de notre parcours de connexion. Premièrement, impossible de coller son mot de passe depuis un gestionnaire. Deuxièmement, aucun moyen d’afficher les caractères saisis. Troisièmement, le bouton Continuer est désactivé par l’attribut disabled et disparaît quand on navigue au clavier. Enfin, la création de compte ne propose qu’un seul champ de mot de passe. Pour chaque scène, cherchez le geste qui manque à la personne : coller, voir, comprendre l’état du bouton, éviter l’erreur de création.

**Mémo oral :** Partir du geste qui manque à la personne.

**Question de réactivation :** Pour chaque situation, quelle règle, et quel mot de l’énoncé la désigne ?

---

### S31 — Le vrai test commence quand la saisie est refusée

- **Acte :** 3. Corriger sans abandonner  
- **Type :** transition  
- **Durée indicative :** 0:50  
- **Objectif pédagogique :** Basculer du formulaire idéal au comportement réel en erreur.

**Sous-titre visible :** « Acte 3 · Corriger sans abandonner »

**Texte visible (projection) :** Camille clique sur Envoyer. Trois informations sont rejetées. Peut-elle comprendre, corriger et garder son travail ?

**Illustration unique :** Page de formulaire après validation : trois zones entourées sans texte de solution.
**Alternative textuelle à fournir :** Formulaire dont plusieurs saisies sont rejetées après envoi.

**Règle → préjudice utilisateur :** Les erreurs provoquent une impasse si elles ne sont pas localisables et réparables.

**Garantie recherchée (matière de l’oral)**

Un retour d’erreur aide à se remettre en mouvement sans recommencer.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire observer l’écran : « Où ? Pourquoi ? Puis-je modifier ? Dans quelle langue ? »
- Piège certification : Une seule bannière « Erreur » ne satisfait pas à elle seule 79, 80 et 81.

**Discours oral du présentateur (non projeté)**

Troisième acte : corriger sans abandonner. Nous venons de remplir plusieurs champs. Maintenant, trois saisies sont rejetées. C’est là que commence le vrai travail de qualité. L’utilisateur doit savoir quels champs sont concernés, pour quelle raison, et retrouver ses réponses encore modifiables. Le message doit aussi être dans la langue du formulaire. Les quatre règles qui suivent se retiennent comme quatre questions très simples.

**Mémo oral :** Où ? Pourquoi ? Encore modifiable ? Compréhensible ?

---

### S32 — Une erreur doit désigner les champs concernés

- **Acte :** 3. Corriger sans abandonner  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 79 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 79 :** « En cas de rejet des données saisies dans un formulaire, les champs contenant les données rejetées sont indiqués à l’utilisateur. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/79

**Texte visible (projection) :** Titre de page : « Erreur : 3 champs à corriger » ; chaque étiquette de champ erroné signale le rejet.

**Illustration unique :** Page de formulaire en erreur avec résumé et trois étiquettes de champs marquées comme incorrectes.
**Alternative textuelle à fournir :** Illustration du cas de la règle 79 : Page de formulaire en erreur avec résumé et trois étiquettes de champs marquées comme incorrectes.

**Règle → préjudice utilisateur :** L’utilisateur ne sait pas où agir, même s’il sait que l’envoi a échoué.

**Garantie recherchée (matière de l’oral)**

La présence d’erreurs et les champs à corriger sont explicitement identifiés.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Provoquer un refus, puis vérifier que la présence d’erreurs est annoncée au moins dans l’élément title de la page et que chaque champ en erreur est signalé dans son étiquette, comme l’exige le contrôle officiel.
- Piège certification : 79 dit où est le problème ; ce n’est pas la même chose que 80, qui explique pourquoi.
- Avis de l’expert (livre, 4e édition 2026) : « Pour aller plus loin dans l’accessibilité des signalements d’erreurs, il est également recommandé de recourir à l’attribut aria-invalid. »

**Discours oral du présentateur (non projeté)**

Trois champs ont été refusés, mais seule une petite alerte apparaît en haut. Où doit aller Camille ? La règle des champs en erreur demande d’identifier les champs concernés. Le contrôle officiel va plus loin : la présence d’erreurs doit être annoncée au moins dans le titre de la page, et chaque champ erroné signalé dans son étiquette. Ce n’est pas encore l’explication de la raison : celle-ci appartient à la règle de l’explication de l’erreur. Pensez « Où ? ».

**Mémo oral :** Champs en erreur : où corriger ?

**Question de réactivation :** Une bannière dit « erreur », sans citer les champs, et aucune étiquette ne signale l’erreur : quelle règle ?

---

### S33 — Dire pourquoi, pas seulement « erreur »

- **Acte :** 3. Corriger sans abandonner  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 80 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 80 :** « En cas de rejet des données saisies dans un formulaire, les raisons du rejet sont indiquées à l’utilisateur. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/80

**Texte visible (projection) :** « Date invalide. Saisissez-la au format JJ/MM/AAAA. »

**Illustration unique :** Deux messages d’erreur sur un champ de date : « invalide » et « format JJ/MM/AAAA attendu ».
**Alternative textuelle à fournir :** Illustration du cas de la règle 80 : Deux messages d’erreur sur un champ de date : « invalide » et « format JJ/MM/AAAA attendu ».

**Règle → préjudice utilisateur :** L’utilisateur sait qu’il s’est trompé mais ne sait pas comment revenir dans le parcours.

**Garantie recherchée (matière de l’oral)**

Les raisons du rejet et une aide à la correction sont explicites.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Tester différentes erreurs de formats, champs vides et contraintes ; lire la précision des raisons fournies.
- Piège certification : « Champ incorrect » localise peut-être, mais n’explique pas suffisamment la cause pour 80.

**Discours oral du présentateur (non projeté)**

La date de Camille est refusée. Dire seulement « Erreur » ou « Date incorrecte » ne l’aide guère. La règle de l’explication de l’erreur exige d’expliquer la nature du rejet et de donner de quoi corriger. On teste plusieurs types d’échec pour voir si la réponse est réellement utile. La règle des champs en erreur indiquait quels champs reprendre ; ici, c’est le contenu du message et sa capacité à guider la correction qui comptent.

**Mémo oral :** Raison de l’erreur : pourquoi ce rejet ?

**Question de réactivation :** Message « Valeur incorrecte » sans raison ni conseil : quelle règle ?

---

### S34 — Ne faites pas payer deux fois la même saisie

- **Acte :** 3. Corriger sans abandonner  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 81 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 81 :** « En cas de rejet des données saisies dans un formulaire, toutes les données saisies peuvent être modifiées par l’utilisateur. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/81

**Texte visible (projection) :** Après un rejet, toutes les données saisies restent disponibles et modifiables.

**Illustration unique :** Un formulaire avant/après erreur montrant les mêmes valeurs conservées, avec possibilité de les modifier.
**Alternative textuelle à fournir :** Illustration du cas de la règle 81 : Un formulaire avant/après erreur montrant les mêmes valeurs conservées, avec possibilité de les modifier.

**Règle → préjudice utilisateur :** L’utilisateur doit ressaisir son dossier, abandonne ou introduit de nouvelles erreurs.

**Garantie recherchée (matière de l’oral)**

Les réponses déjà fournies peuvent encore être revues et modifiées après rejet.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Remplir plusieurs champs, provoquer une erreur, inspecter tous les champs puis essayer d’en modifier plusieurs.
- Piège certification : Conserver seulement les valeurs valides ne couvre pas « toutes les données saisies peuvent être modifiées ». Le contrôle officiel vérifie que le formulaire est réaffiché tel qu’il a été rempli.

**Discours oral du présentateur (non projeté)**

Camille a passé dix minutes à renseigner son dossier. Un code postal incorrect efface toutes les réponses. Même si le message d’erreur est précis, le préjudice reste énorme. La règle de la conservation des saisies après erreur demande que les informations puissent être retrouvées et modifiées après le rejet. Pour le tester, on remplit plusieurs champs, on provoque une erreur, puis on revient sur des réponses sans rapport avec l’erreur. C’est ce pouvoir de correction globale qu’il faut retenir.

**Mémo oral :** Saisies conservées : je ne recommence pas.

**Question de réactivation :** Les champs valides sont effacés après un refus : quelle règle ?

---

### S35 — Le message d’erreur parle la langue du formulaire

- **Acte :** 3. Corriger sans abandonner  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 82 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 82 :** « Les messages d’erreur personnalisés sont exprimés dans la langue du formulaire. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/82

**Texte visible (projection) :** Formulaire en français → messages d’erreur personnalisés en français.

**Illustration unique :** Champ de formulaire français avec un message « Invalid input » puis son équivalent français.
**Alternative textuelle à fournir :** Illustration du cas de la règle 82 : Champ de formulaire français avec un message « Invalid input » puis son équivalent français.

**Règle → préjudice utilisateur :** L’utilisateur reçoit une consigne incompréhensible ou linguistiquement incohérente.

**Garantie recherchée (matière de l’oral)**

Les messages personnalisés sont compréhensibles dans la langue du formulaire.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Déclencher plusieurs erreurs et vérifier la langue des messages produits par le site.
- Piège certification : La règle 82 porte sur la langue, pas sur la précision de la cause (80). Le comportement des messages natifs dépend aussi du navigateur.
- Avis de l’expert (livre, 4e édition 2026) : « la mise en place et le paramétrage effectifs de la traduction ne sont pas automatiques. L’implémentation de cette règle impose de procéder à de nombreux tests, notamment en changeant l’ordre préférentiel des langues de consultation dans les navigateurs web. »

**Discours oral du présentateur (non projeté)**

Le formulaire est entièrement en français, mais l’application affiche « Invalid input » lorsqu’on se trompe. La règle de la langue des messages d’erreur demande que les messages personnalisés suivent la langue du formulaire. On ne vérifie pas seulement la présence d’une traduction générique : on déclenche les différents cas d’erreur. Même si le message dit clairement la raison dans une autre langue, il peut rester contraire à cette règle. Gardez distinctes langue et explication.

**Mémo oral :** Langue du message : quelle langue ?

**Question de réactivation :** Un message très précis s’affiche en anglais dans un formulaire français : quelle règle ?

---

### S36 — Quatre erreurs, quatre réponses : 79–82

- **Acte :** 3. Corriger sans abandonner  
- **Type :** distinction  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Fixer une séquence logique de résolution des erreurs.

**Texte visible (projection) :** 79 Où ? · 80 Pourquoi ? · 81 Puis-je modifier ? · 82 Dans quelle langue ?
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Cycle unique en quatre étapes autour d’un formulaire rejeté.
**Alternative textuelle à fournir :** Cycle de réparation d’un formulaire allant de la localisation de l’erreur à la langue du message.

**Règle → préjudice utilisateur :** Confondre information, assistance et conservation peut faire croire qu’une erreur est correctement traitée.

**Garantie recherchée (matière de l’oral)**

L’utilisateur peut comprendre l’échec, identifier les champs et corriger sans perdre ses données.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner à chaque équipe une défaillance à classer dans le bon numéro.
- Piège certification : Un message peut être visible et précis, tout en restant insuffisant si les champs sont effacés.

**Discours oral du présentateur (non projeté)**

Voici le quartet le plus utile après un échec de soumission. Les champs en erreur répondent « où » ; l’explication, « pourquoi » ; la conservation, « puis-je encore modifier sans tout recommencer » ; la langue, « dans quelle langue ». Sur le même formulaire, les quatre risques peuvent coexister. Les formulations des QCM pourront être très proches : ne cherchez pas un mot-clé unique, cherchez le préjudice précis décrit.

**Mémo oral :** Où / Pourquoi / Modifier / Langue.

---

### S37 — Checkpoint 3 : trois messages, trois diagnostics

- **Acte :** 3. Corriger sans abandonner  
- **Type :** quiz  
- **Durée indicative :** 1:30  
- **Objectif pédagogique :** Appliquer les règles de rejet sans intuition approximative.

**Texte visible (projection) :** A. Champs invalides non identifiés. B. Champs désignés, mais sans raison. C. Formulaire remis à zéro après erreur.

**Illustration unique :** Une seule planche A/B/C de trois captures fictives de rejet.
**Alternative textuelle à fournir :** Trois formes de refus d’un formulaire à associer à trois règles.

**Règle → préjudice utilisateur :** Une correction partielle ne garantit pas la poursuite du parcours.

**Garantie recherchée (matière de l’oral)**

Diagnostiquer la couche réellement en défaut.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire répondre A, B et C, puis poser le cas D : un message en anglais sur un formulaire français.
- Piège certification : Les réponses ne figurent que dans les notes du présentateur, jamais sur la slide.

**Corrigé (notes du présentateur, non projeté) :** A=79 ; B=80 ; C=81 ; D=82.

**Discours oral du présentateur (non projeté)**

Nous allons maintenant choisir sans hésiter. Cas A : le système rejette l’envoi mais ne désigne pas les champs. Cas B : les champs sont pointés, mais les raisons ne sont pas indiquées. Cas C : toutes les réponses ont disparu. Si j’ajoute un quatrième cas avec un message en anglais sur un formulaire français, quelle règle intervenait ? Répondez d’abord avec les questions : où, pourquoi, modifier, langue.

**Mémo oral :** Le rejet se diagnostique en quatre dimensions.

**Question de réactivation :** Quatre cas, quatre dimensions : où, pourquoi, modifier, langue ?

---

### S38 — Avant de confirmer, voir l’ensemble du dossier

- **Acte :** 4. Savoir ce qui a été envoyé  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 83 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 83 :** « Lors de la saisie d’un formulaire réparti sur plusieurs pages, un récapitulatif global est affiché avant l’envoi définitif. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/83

**Sous-titre visible :** « Acte 4 · Savoir ce qui a été envoyé »

**Texte visible (projection) :** Formulaire réparti sur plusieurs pages → récapitulatif global avant envoi définitif.

**Illustration unique :** Étape finale de Mon Atelier avec une synthèse de toutes les sections précédentes avant un bouton Confirmer.
**Alternative textuelle à fournir :** Illustration du cas de la règle 83 : Étape finale de Mon Atelier avec une synthèse de toutes les sections précédentes avant un bouton Confirmer.

**Règle → préjudice utilisateur :** L’utilisateur confirme sans vision globale des informations fournies au fil des étapes.

**Garantie recherchée (matière de l’oral)**

Les données d’un formulaire multipage peuvent être vérifiées dans leur ensemble avant l’envoi final.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Exécuter le parcours multipage et contrôler l’existence du récapitulatif global avant la validation définitive.
- Piège certification : 83 porte spécifiquement sur le formulaire réparti sur plusieurs pages ; ne pas la confondre avec la prévisualisation de contenu public (10).

**Discours oral du présentateur (non projeté)**

Quatrième acte : savoir ce qui a été envoyé. Mon Atelier a demandé l’identité, l’adresse et les pièces justificatives sur trois pages. Juste avant l’envoi final, Camille doit pouvoir retrouver l’ensemble de ses réponses. C’est la règle du récapitulatif avant envoi. Le point décisif est le moment : avant la validation définitive. L’écran de confirmation après l’envoi ne peut pas tenir lieu de récapitulatif préalable. C’est une confusion classique avec les règles de la navigation après envoi et du résultat annoncé.

**Mémo oral :** Récapitulatif : tout relire avant.

**Question de réactivation :** Une confirmation après l’envoi remplace-t-elle le récapitulatif avant ?

---

### S39 — Après l’envoi, ne pas créer une impasse

- **Acte :** 4. Savoir ce qui a été envoyé  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 84 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 84 :** « La page affichée après l’envoi d’un formulaire permet de reprendre directement la navigation. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/84

**Texte visible (projection) :** La page après soumission garde les moyens de navigation : menu, accueil, poursuite.

**Illustration unique :** Écran « demande envoyée » avec navigation accessible, opposé à un cul-de-sac sans lien.
**Alternative textuelle à fournir :** Illustration du cas de la règle 84 : Écran « demande envoyée » avec navigation accessible, opposé à un cul-de-sac sans lien.

**Règle → préjudice utilisateur :** La personne se retrouve bloquée ou retourne en arrière avec risque de nouvel envoi.

**Garantie recherchée (matière de l’oral)**

L’utilisateur peut poursuivre directement sa navigation après l’envoi.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Soumettre le formulaire et contrôler les liens/menu de reprise sur la page affichée.
- Piège certification : 84 ne demande pas le message de réussite lui-même : c’est l’objet de 85.
- Avis de l’expert (livre, 4e édition 2026) : « Elle nécessite une attention particulière en cas d’intégration de services externes. »

**Discours oral du présentateur (non projeté)**

Après avoir envoyé son dossier, Camille arrive sur une page sans menu, sans lien de retour et sans issue claire. C’est la règle de la navigation après envoi qui pose problème. La page affichée après la soumission doit permettre de reprendre directement la navigation. Cela évite notamment le recours au bouton Retour, qui peut entraîner un second envoi. La présence d’un message de succès ne suffit donc pas à satisfaire cette règle.

**Mémo oral :** Après l’envoi : je peux continuer.

**Question de réactivation :** Une page dit « succès » mais ne contient aucun accès pour poursuivre : quelle règle ?

---

### S40 — Un formulaire doit répondre clairement « oui » ou « non »

- **Acte :** 4. Savoir ce qui a été envoyé  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 85 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 85 :** « La soumission d’un formulaire est suivie d’un message indiquant la réussite ou non de l’action souhaitée. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/85

**Texte visible (projection) :** Après soumission : « Votre demande a été reçue » ou « Votre demande n’a pas pu être enregistrée ».

**Illustration unique :** Deux cartes de confirmation explicites de succès et d’échec, au sein d’une seule page de parcours.
**Alternative textuelle à fournir :** Illustration du cas de la règle 85 : Deux cartes de confirmation explicites de succès et d’échec, au sein d’une seule page de parcours.

**Règle → préjudice utilisateur :** L’utilisateur ne sait pas si l’action souhaitée s’est réellement produite.

**Garantie recherchée (matière de l’oral)**

Un message immédiat et explicite confirme la réussite ou l’échec de l’opération.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Envoyer le formulaire et vérifier une confirmation explicite du résultat dans le contenu et, selon l’avis de l’expert, dans le titre de page, pas seulement une transition de page.
- Piège certification : 85 = message de résultat sur le service ; 110 = accusé de réception par courriel pour une demande d’information.

**Discours oral du présentateur (non projeté)**

L’écran suivant s’affiche, mais le dossier est-il enregistré ? S’il n’y a pas de message clair de réussite ou d’échec, on manque la règle du résultat annoncé. Ce retour doit correspondre à la réalité de l’opération. Attention au trio : le récapitulatif est avant l’envoi, la navigation concerne la possibilité de continuer après, le résultat concerne ce qui est annoncé après. Et ce message sur la page n’est pas la même chose qu’un accusé de réception envoyé par courriel.

**Mémo oral :** Résultat annoncé : suis-je arrivé au bout ?

**Question de réactivation :** Une page de navigation est présente, mais aucun résultat n’est annoncé : quelle règle ?

---

### S41 — 83 / 84 / 85 : avant, après, résultat

- **Acte :** 4. Savoir ce qui a été envoyé  
- **Type :** distinction  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Distinguer trois moments voisins du parcours.

**Texte visible (projection) :** 83 Avant : récapitulatif · 84 Après : navigation possible · 85 Après : succès ou échec explicite.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Frise unique « avant l’envoi / soumettre / après l’envoi » avec trois repères numérotés.
**Alternative textuelle à fournir :** Frise montrant récapitulatif avant envoi, reprise de navigation et confirmation du résultat après.

**Règle → préjudice utilisateur :** Une bonne page finale peut manquer de récapitulatif ; une confirmation peut manquer de navigation.

**Garantie recherchée (matière de l’oral)**

Trois garanties indépendantes : vérifier, poursuivre, connaître le résultat.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Trois contre-exemples oraux : récap après, succès sans menu, menu sans résultat.
- Piège certification : N’inversez jamais la temporalité « avant la validation définitive » et « après l’envoi ».

**Discours oral du présentateur (non projeté)**

Le mot qui vous aide à gagner ce point en certification, c’est le temps. Avant de valider un formulaire en plusieurs pages : le récapitulatif, une vue globale. Après soumission : la navigation, la page permet de continuer. Après soumission encore : le résultat, annoncé sans ambiguïté. Si un QCM propose un message de réussite comme réponse à un problème de récapitulatif préalable, c’est un piège temporel.

**Mémo oral :** Avant : récapitulatif ; après : navigation + résultat.

---

### S42 — Un succès sur la page n’est pas un accusé de réception

- **Acte :** 4. Savoir ce qui a été envoyé  
- **Type :** transversal  
- **Durée indicative :** 1:10  
- **Objectif pédagogique :** Relier la rubrique Formulaires à Identification/contact et à Contenus.

**Texte visible (projection) :** 85 = résultat affiché · 110 = accusé de réception archivable · 108 = délai de réponse · 10 = vérifier avant publication publique.

**Illustration unique :** Une seule ligne de temps avec prévisualisation, résultat à l’écran, courriel reçu et délai annoncé.
**Alternative textuelle à fournir :** Quatre informations distinctes situées avant et après un formulaire de demande.

**Règle → préjudice utilisateur :** L’utilisateur peut savoir que l’envoi a réussi sans posséder une preuve conservable ni savoir quand attendre une réponse.

**Garantie recherchée (matière de l’oral)**

La qualité du suivi dépend de plusieurs règles distinctes appartenant à d’autres rubriques.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Proposer un formulaire de contact envoyé : demander quel contenu reste à fournir après la confirmation.
- Piège certification : Ne pas confondre Opquast 110 et RGAA 11.10 : même numérotation apparente, référentiels distincts.

**Discours oral du présentateur (non projeté)**

Un message « votre demande a été prise en compte » répond à la règle du résultat annoncé. Mais si Camille contacte un service, elle peut aussi avoir besoin d’un accusé de réception archivable, objet d’une règle dédiée, et de connaître le délai de réponse prévu, objet d’une autre. Si elle publie un avis ou une image, la règle sur la prévisualisation peut intervenir avant l’envoi. Un formulaire traverse plusieurs rubriques Opquast : c’est une vraie logique de certification.

**Mémo oral :** Résultat ≠ reçu ≠ délai ≠ aperçu.

---

### S43 — Préparer les pièces avant le début du parcours

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 86 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 86 :** « L’utilisateur est averti au début d’un processus complexe de la nature des données et documents exigés. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/86

**Sous-titre visible :** « Acte 5 · Gérer une démarche longue »

**Texte visible (projection) :** « Avant de commencer : pièce d’identité, justificatif de domicile. »

**Illustration unique :** Page d’introduction de démarche avec liste de pièces nécessaires avant la première étape.
**Alternative textuelle à fournir :** Illustration du cas de la règle 86 : Page d’introduction de démarche avec liste de pièces nécessaires avant la première étape.

**Règle → préjudice utilisateur :** L’utilisateur s’interrompt à mi-parcours parce qu’un document nécessaire n’avait pas été annoncé.

**Garantie recherchée (matière de l’oral)**

La personne peut anticiper et réunir les données ou pièces nécessaires.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Vérifier sur la page d’entrée du processus la liste des informations et documents exigés avant la première étape.
- Piège certification : 86 = préparer les documents ; 87 = connaître toutes les étapes ; 172 = connaître une limite de temps.

**Discours oral du présentateur (non projeté)**

Cinquième acte : gérer une démarche longue, en plusieurs étapes. Nous voici au début d’un parcours complexe. La règle des pièces à préparer demande d’annoncer les données et documents qui seront nécessaires avant la première étape. Si l’on réclame un justificatif au quatrième écran sans avertissement, le processus s’interrompt. L’enjeu est de rendre la démarche préparatoire et réaliste. Attention : afficher les étapes ne suffit pas à signaler les pièces, et donner les pièces ne suffit pas à expliquer la durée d’une session.

**Mémo oral :** Pièces annoncées : quoi préparer ?

**Question de réactivation :** Documents demandés seulement à l’étape 4 : quelle règle ?

---

### S44 — Un processus complexe montre toutes ses étapes

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 87 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 87 :** « Les processus complexes sont accompagnés de la liste de leurs étapes. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/87

**Texte visible (projection) :** Identité → Coordonnées → Documents → Vérification → Confirmation.

**Illustration unique :** Chemin d’étapes complet et stable en haut de chaque page du parcours.
**Alternative textuelle à fournir :** Illustration du cas de la règle 87 : Chemin d’étapes complet et stable en haut de chaque page du parcours.

**Règle → préjudice utilisateur :** L’utilisateur ne sait pas ce qui lui reste à faire ni s’il a choisi une démarche trop longue.

**Garantie recherchée (matière de l’oral)**

La liste des étapes du processus est disponible à chaque étape.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Parcourir chaque page et vérifier la présence de la liste intégrale des étapes.
- Piège certification : 87 = liste complète ; 88 = identification de celle en cours. Un simple « Étape 2/5 » ne montre pas nécessairement la liste.

**Discours oral du présentateur (non projeté)**

Au début du dossier, Camille voit seulement « Continuer ». Combien de pages ? Quelles actions viendront ensuite ? La règle de la liste des étapes exige que les processus complexes s’accompagnent de la liste de leurs étapes, à chaque étape. Un chemin d’étapes complet évite le sentiment d’être piégé. Mais ne confondez pas cette liste avec le repérage de l’étape actuelle, qui relève de la règle voisine.

**Mémo oral :** Liste des étapes : quels sont les prochains écrans ?

**Question de réactivation :** Un formulaire indique seulement « 2 sur 5 » sans liste des étapes : liste des étapes ou étape en cours ?

---

### S45 — Savoir précisément où l’on est

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 88 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 88 :** « L’étape en cours d’un processus complexe est indiquée. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/88

**Texte visible (projection) :** « Étape 3 sur 5 : Documents », mise en évidence dans le parcours et le contenu.

**Illustration unique :** Chemin d’étapes où « Documents » est mis en évidence et reproduit dans le titre de page.
**Alternative textuelle à fournir :** Illustration du cas de la règle 88 : Chemin d’étapes où « Documents » est mis en évidence et reproduit dans le titre de page.

**Règle → préjudice utilisateur :** La personne voit la liste mais ne sait pas à quelle étape elle se trouve.

**Garantie recherchée (matière de l’oral)**

L’étape courante du parcours est clairement indiquée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Examiner chaque page et l’indication d’étape active ; vérifier le titre et le chemin d’étapes.
- Piège certification : 88 = étape actuelle ; 87 = liste globale. Les deux peuvent échouer indépendamment.
- Avis de l’expert (livre, 4e édition 2026) : « L’indication de l’étape en cours relève également du titre de la page (élément title). Par ailleurs, dans le chemin d’étapes, cette indication doit être perceptible indépendamment du support des styles CSS ou de la perception de la couleur. »

**Discours oral du présentateur (non projeté)**

Camille connaît les cinq étapes, mais aucune n’est signalée comme active. Le chemin est présent ; le repérage ne l’est pas. C’est la règle de l’étape en cours. L’étape en cours doit être identifiable, notamment dans le contenu et le titre de la page. Un intitulé précis comme « Étape 3 : Documents » aide aussi les technologies d’assistance à comprendre la progression. La nuance entre liste des étapes et étape en cours est fondamentale.

**Mémo oral :** Étape en cours : où suis-je ?

**Question de réactivation :** Toutes les étapes sont visibles mais aucune n’est active : liste des étapes ou étape en cours ?

---

### S46 — Revenir à l’étape précédente sans bricolage

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 89 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 89 :** « Chaque étape d’un processus complexe permet de revenir à l’étape précédente. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/89

**Texte visible (projection) :** Chaque étape propose un retour explicite vers l’étape précédente.

**Illustration unique :** Boutons « Précédent » et « Suivant » dans un parcours de cinq étapes.
**Alternative textuelle à fournir :** Illustration du cas de la règle 89 : Boutons « Précédent » et « Suivant » dans un parcours de cinq étapes.

**Règle → préjudice utilisateur :** La personne ne peut corriger un choix antérieur sans recommencer ou risquer un retour navigateur.

**Garantie recherchée (matière de l’oral)**

Un mécanisme propre au parcours permet de remonter étape par étape.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Sur chaque étape après la première, activer « Précédent » et vérifier qu’elle est atteignable.
- Piège certification : 89 = possibilité de retour via le parcours ; 90 = avertissement sur l’historique navigateur ; 91 = conservation des données.

**Discours oral du présentateur (non projeté)**

On est à l’étape Documents, mais on veut corriger l’adresse de l’étape Coordonnées. La règle du retour à l’étape précédente demande un moyen de revenir à l’étape précédente. C’est une capacité de navigation interne au processus. Le bouton Retour du navigateur n’est pas automatiquement un substitut suffisant. Et attention : cette règle ne dit pas, à elle seule, si les données seront conservées. Cette exigence est distincte.

**Mémo oral :** Étape précédente : revenir.

**Question de réactivation :** Pas de bouton Précédent dans un formulaire multipage : quelle règle ?

---

### S47 — Le bouton Retour du navigateur peut coûter cher

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 90 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 90 :** « L’utilisateur est averti de la perte d’information en cas d’utilisation de l’historique de son navigateur dans un processus complexe. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/90

**Texte visible (projection) :** Si « Retour » du navigateur risque d’effacer les données, avertir avant la perte.

**Illustration unique :** Navigation arrière du navigateur avec alerte de perte potentielle de saisie.
**Alternative textuelle à fournir :** Illustration du cas de la règle 90 : Navigation arrière du navigateur avec alerte de perte potentielle de saisie.

**Règle → préjudice utilisateur :** L’utilisateur perd des réponses sans savoir que cette opération allait les effacer.

**Garantie recherchée (matière de l’oral)**

Le risque de perte par historique navigateur est signalé.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Amorcer la saisie après la première étape du processus, utiliser l’historique arrière et observer si des données sont perdues sans avertissement.
- Piège certification : La règle 90 est conditionnelle au risque de perte lié à l’historique. Ne pas confondre avec le mécanisme Précédent (89).
- Avis de l’expert (livre, 4e édition 2026) : « Cette règle s’applique tout particulièrement en l’absence de mécanisme explicite permettant à l’utilisateur de revenir à une étape précédente de la série de formulaires. »

**Discours oral du présentateur (non projeté)**

Nous allons volontairement utiliser le bouton Retour du navigateur, et non le bouton Précédent de la démarche. Si ce retour entraîne la perte d’informations, l’utilisateur doit en être averti. C’est la règle de l’avertissement lié à l’historique. Le livre illustre un avertissement JavaScript. Retenez surtout la condition et le comportement testé : on part d’une saisie commencée, on utilise l’historique et on vérifie ce qui arrive aux données et à l’avertissement.

**Mémo oral :** Avertissement : attention à l’historique.

**Question de réactivation :** Le navigateur revient en arrière et efface sans avertissement : quelle règle ?

---

### S48 — Revenir ne doit pas effacer les réponses précédentes

- **Acte :** 5. Gérer une démarche longue  
- **Type :** regle  
- **Durée indicative :** 0:42  
- **Objectif pédagogique :** Identifier sans hésitation la règle 91 à partir d’une situation et savoir la vérifier.
- **Règle officielle Opquast V5 n° 91 :** « La navigation dans un processus complexe ne provoque pas la perte des données précédemment soumises. »  
- **Source normative Opquast :** https://checklists.opquast.com/fr/qualite-numerique/91

**Texte visible (projection) :** Retour par les étapes du processus : les valeurs déjà soumises réapparaissent.

**Illustration unique :** Même étape d’adresse avant et après un aller-retour, avec données conservées.
**Alternative textuelle à fournir :** Illustration du cas de la règle 91 : Même étape d’adresse avant et après un aller-retour, avec données conservées.

**Règle → préjudice utilisateur :** Une navigation normale dans la démarche fait perdre les réponses déjà fournies.

**Garantie recherchée (matière de l’oral)**

Les données des étapes précédemment soumises sont conservées et réaffichées.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Utiliser « Précédent » puis « Suivant » dans la démarche et comparer les réponses conservées.
- Piège certification : 91 traite de la conservation effective dans le parcours, pas seulement d’un avertissement sur le Retour navigateur.

**Discours oral du présentateur (non projeté)**

Camille revient de Documents à Coordonnées en utilisant le bouton prévu. Toutes ses réponses doivent être là. La règle de la conservation entre étapes porte précisément sur ce point. Avec la règle du retour, on sait revenir ; avec celle de la conservation, on ne perd pas son travail. Avec celle de l’avertissement, un autre scénario est testé : l’historique du navigateur et son éventuel avertissement. Garder ces trois scénarios séparés permet de répondre sans hésitation.

**Mémo oral :** Retour sans perte : conserver le travail.

**Question de réactivation :** Précédent existe mais les valeurs réapparaissent vides : retour possible ou données conservées ?

---

### S49 — Les cinq leviers d’une démarche longue : 87–91

- **Acte :** 5. Gérer une démarche longue  
- **Type :** distinction  
- **Durée indicative :** 1:30  
- **Objectif pédagogique :** Mémoriser la suite 87-91 comme cinq capacités indépendantes.

**Texte visible (projection) :** 87 liste des étapes · 88 étape courante · 89 retour interne · 90 perte via historique avertie · 91 données conservées.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Chemin de progression unique avec cinq indicateurs : liste, position, retour, avertissement, conservation.
**Alternative textuelle à fournir :** Cinq capacités d’un parcours multipage, numérotées de 87 à 91.

**Règle → préjudice utilisateur :** Une navigation possible ne suffit pas lorsque la position est obscure ou les données sont perdues.

**Garantie recherchée (matière de l’oral)**

Voir le parcours, se situer, reculer, être averti, conserver les réponses.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner les cinq intentions dans le désordre ; faire redonner le bon numéro.
- Piège certification : 89, 90 et 91 paraissent proches mais impliquent trois manipulations de test différentes.

**Discours oral du présentateur (non projeté)**

Pour les cinq règles de la démarche longue, mémorisez une petite histoire. Je vois la liste des étapes. Je sais où je suis. Je peux revenir. Si l’historique du navigateur peut faire perdre des données, j’en suis averti. Si je navigue normalement dans les étapes, les données restent présentes. Chaque phrase désigne une règle et correspond à un contrôle concret différent.

**Mémo oral :** Liste → position → retour → avertissement → conservation.

---

### S50 — Cas intégrateur : quatre écrans, sept risques

- **Acte :** 5. Gérer une démarche longue  
- **Type :** etude-de-cas  
- **Durée indicative :** 2:00  
- **Objectif pédagogique :** Appliquer 83 et 86–91 à un parcours entier.

**Texte visible (projection) :** Au départ, pièces inconnues ; ni liste des étapes ni étape active ; aucun retour possible depuis l’étape 3 ; à l’étape 4, le bouton « Précédent » ramène des champs vides ; « Retour » du navigateur sans avertissement ; aucun récapitulatif final.

**Illustration unique :** Une illustration unique de quatre étapes d’un dossier avec sept zones numérotées à diagnostiquer.
**Alternative textuelle à fournir :** Parcours de quatre écrans présentant des lacunes de préparation, progression, retour et récapitulatif.

**Règle → préjudice utilisateur :** Une démarche peut rester inutilisable alors que chacun de ses champs paraît correct.

**Garantie recherchée (matière de l’oral)**

La qualité se vérifie dans la succession des étapes et dans la conservation des données.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : En groupe, associer chaque difficulté à une règle et à un geste de test.
- Piège certification : Un défaut de retour navigateur n’établit pas automatiquement une violation de 91 : distinguer les scénarios.

**Corrigé (notes du présentateur, non projeté) :** pièces annoncées trop tard=86 ; liste des étapes absente=87 ; étape active absente=88 ; aucun retour possible depuis l’étape 3=89 ; champs vides en revenant par « Précédent »=91 ; « Retour » du navigateur sans avertissement=90, à tester avant de conclure ; récapitulatif absent=83.

**Discours oral du présentateur (non projeté)**

À vous de mener l’analyse. Nous voyons une démarche de quatre écrans. Les documents nécessaires ne sont révélés qu’en cours de route ; ni la liste des étapes ni l’étape active ne sont affichées ; à l’étape 3, aucun bouton ne permet de revenir ; à l’étape 4, le bouton Précédent ramène des champs vides ; le Retour du navigateur efface sans prévenir. Enfin, il n’y a aucun récapitulatif avant confirmation. En groupe, associez chaque problème à la règle précise. Je vous demanderai aussi ce que vous testeriez réellement avant de conclure, notamment pour l’historique du navigateur.

**Mémo oral :** Le parcours révèle des défauts invisibles au scan d’une page.

**Question de réactivation :** Associer chaque difficulté à sa règle et proposer un test.

---

### S51 — Un formulaire mobilise d’autres rubriques Opquast

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** transversal  
- **Durée indicative :** 1:45  
- **Objectif pédagogique :** Éviter de limiter l’analyse d’un formulaire à 69–98.

**Sous-titre visible :** « Acte 6 · S’entraîner pour la certification »

**Texte visible (projection) :** Données personnelles 24/26 · Navigation 165–167/172 · Contact 103/108/110 · Newsletter 173–176 · Sécurité 201–205 · Structure 236 · Présentation 181 · Contenus 10.

**Illustration unique :** Carte radiale unique « formulaire » reliée à huit autres thématiques Opquast.
**Alternative textuelle à fournir :** Carte des règles transversales autour d’un formulaire.

**Règle → préjudice utilisateur :** La focalisation sur la rubrique peut faire oublier le titre de page, le clavier, les données ou la sécurité.

**Garantie recherchée (matière de l’oral)**

Le référentiel se lit de manière transversale selon le risque rencontré.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner le défaut « erreur signalée uniquement en rouge » et demander la règle, hors rubrique ; ajouter les cas de la publication publique et de l’accusé de réception.
- Piège certification : Les questions sur formulaires peuvent relever d’une autre rubrique Opquast ; ne pas fabriquer de correspondance automatique.

**Corrigé (notes du présentateur, non projeté) :** 181 pour l’erreur signalée par la seule couleur ; 10 pour la vérification avant publication ; 110 pour l’accusé de réception.

**Discours oral du présentateur (non projeté)**

Vous connaissez maintenant les trente règles de la rubrique : place à l’entraînement, pour le dernier acte. Mais un formulaire reste une page du service numérique. Les alias e-mail ont leur propre règle, la divulgation de l’existence d’un compte aussi, tout comme le titre de page ; la navigation au clavier en mobilise plusieurs ; l’annonce des limites de temps en a une ; les inscriptions aux newsletters, un groupe entier. Nous avons aussi la sécurité des mots de passe et les identifiants HTML uniques. En examen, pensez transversal.

**Mémo oral :** Un formulaire n’est pas qu’une rubrique.

---

### S52 — Opquast ≠ RGAA : deux angles complémentaires

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** methode  
- **Durée indicative :** 1:00  
- **Objectif pédagogique :** Éviter les fausses équivalences entre référentiels.

**Texte visible (projection) :** Opquast : qualité et risques utilisateur. RGAA : critères et tests d’accessibilité. Même composant, questions distinctes.

**Illustration unique :** Deux lentilles distinctes examinant un même champ de formulaire : qualité de l’usage et conformité au référentiel d’accessibilité.
**Alternative textuelle à fournir :** Deux angles d’analyse, Opquast et RGAA, appliqués au même champ.

**Règle → préjudice utilisateur :** Déclarer « conforme RGAA » à partir d’une règle Opquast est méthodologiquement incorrect.

**Garantie recherchée (matière de l’oral)**

Les preuves et décisions restent rattachées au référentiel réellement contrôlé.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner 69 et 11.1 comme sujets proches, puis montrer qu’ils n’ont pas des tests identiques.
- Piège certification : Une conformité Opquast ne prouve pas la conformité RGAA, et inversement.

**Discours oral du présentateur (non projeté)**

Nous allons être précis sur les autorités. Opquast aborde la qualité transversale d’un service ; le RGAA est un référentiel français d’accessibilité avec ses propres critères et tests. Les règles se recoupent parfois, mais il n’existe pas de traduction un pour un. Par exemple, le sujet des étiquettes est présent dans les deux. En certification Opquast, on répond depuis la formulation Opquast ; dans un audit RGAA, depuis les tests RGAA.

**Mémo oral :** Même champ, référentiels distincts.

---

### S53 — La bonne méthode de contrôle : regarder, essayer, inspecter

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** methode  
- **Durée indicative :** 1:15  
- **Objectif pédagogique :** Savoir choisir une preuve adaptée à chaque règle.

**Texte visible (projection) :** Observer : 77/78/87/88. Jouer le parcours : 79–85/89–92/96. Inspecter le code : 69/70/93/95/97/236.

**Illustration unique :** Triptyque unique présentant observation d’écran, scénario de test, code source.
**Alternative textuelle à fournir :** Trois modalités d’évaluation complémentaires : observer, interagir et inspecter.

**Règle → préjudice utilisateur :** Une vérification seulement visuelle manque des associations techniques et des comportements après envoi.

**Garantie recherchée (matière de l’oral)**

Chaque règle est contrôlée par une observation adaptée à son mécanisme.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Demander comment prouver trois règles : l’étiquette associée au champ, le signalement des champs rejetés, la conservation des données en revenant.
- Piège certification : Une seule méthode ne permet pas d’évaluer toutes les règles de la rubrique ; rester prudent sur les tests par AT.

**Corrigé (notes du présentateur, non projeté) :** 69 : inspecter le code ; 79 : provoquer un rejet ; 91 : revenir dans le parcours et comparer les valeurs.

**Discours oral du présentateur (non projeté)**

On termine la méthode de vérification avec trois verbes. Observer : pour le placement des labels et le chemin d’étapes. Utiliser réellement : pour les erreurs, la soumission et le retour. Inspecter le code : pour les labels, les descriptions, les types et l’autocomplétion. Certaines règles nécessitent plusieurs gestes. Un passage automatique sans scénario ne peut pas démontrer la conservation des données après une erreur.

**Mémo oral :** Voir / Tester / Inspecter.

---

### S54 — Les dix confusions qui coûtent des points

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** synthese  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Réviser les oppositions avant l’évaluation finale.

**Texte visible (projection) :** 69/77 · 70/78 · 71/72/73/74 · 75/76/92 · 79/80/81/82 · 83/84/85 · 87/88 · 89/90/91 · 93/94 · 95/97.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Fiche unique de dix couples ou familles avec pictogrammes distincts.
**Alternative textuelle à fournir :** Liste graphique de dix regroupements de règles proches à distinguer.

**Règle → préjudice utilisateur :** Une connaissance vague de chaque règle ne suffit pas lorsque plusieurs réponses semblent plausibles.

**Garantie recherchée (matière de l’oral)**

Les associations mnémotechniques réduisent les confusions.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire expliquer en une phrase la différence de chaque couple, sans consulter les notes.
- Piège certification : Éviter les fausses règles « toujours » et « jamais » lorsque le libellé officiel comporte une condition.

**Discours oral du présentateur (non projeté)**

Nous avons fait le tour de la rubrique, mais le plus utile pour la certification se trouve dans les frontières entre règles proches. Le code contre le visuel ; l’obligation contre le format ; la prévention contre l’affichage du mot de passe ; le champ en erreur contre sa raison ; la fin du parcours contre son récapitulatif ; la position contre la liste des étapes ; l’avertissement contre la conservation. Nous allons maintenant jouer avec ces ambiguïtés.

**Mémo oral :** Les frontières sont plus importantes que les numéros seuls.

---

### S55 — Évaluation finale 1/4 : questions 1 à 4

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** quiz  
- **Durée indicative :** 2:30  
- **Objectif pédagogique :** Évaluer la connaissance des distinctions en condition de reconnaissance rapide.

**Texte visible (projection) :** 1. Libellé relié dans le code, mais affiché loin du champ. 2. Consigne juste sous le champ, sans lien dans le code. 3. Champ obligatoire : rien ne l’annonce. 4. Refus selon la casse, sans avertissement.

**Illustration unique :** Une seule mise en situation stylisée pour quatre questions ; quatre repères 1 à 4 et aucun corrigé visible.
**Alternative textuelle à fournir :** Quatre situations de test présentées sans réponses pour une évaluation formative.

**Règle → préjudice utilisateur :** La bonne réponse peut sembler proche d’une autre règle : lire le défaut exact.

**Garantie recherchée (matière de l’oral)**

Une restitution sans support révèle les règles encore fragiles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lire chaque question, faire répondre par une seule règle, désignée par son objet, et une justification d’une phrase.
- Piège certification : Ne pas afficher les réponses simultanément. Questions originales, jamais qualifiées d’officielles.

**Corrigé (notes du présentateur, non projeté) :** 1=77 (69 est respectée : l’association existe) ; 2=70 (78 est respectée : la consigne est proche) ; 3=71 ; 4=73 (sensibilité à la casse non annoncée, pas 72).

**Discours oral du présentateur (non projeté)**

Nous passons à une évaluation rapide. Pour chaque situation, choisissez une seule règle, puis justifiez le choix en une phrase. Si plusieurs défauts sont imaginables, cherchez celui qui est précisément décrit. Après chaque groupe, je reviendrai sur une seule opposition clé. Les réponses ne sont pas projetées : elles sont réservées aux notes du présentateur.

**Mémo oral :** Justifier l’énoncé précis plutôt que deviner.

**Question de réactivation :** Reprendre à l’oral la question qui a le plus divisé le groupe, et faire justifier la réponse par le critère qui la distingue.

---

### S56 — Évaluation finale 2/4 : questions 5 à 8

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** quiz  
- **Durée indicative :** 2:30  
- **Objectif pédagogique :** Évaluer la connaissance des distinctions en condition de reconnaissance rapide.

**Texte visible (projection) :** 5. Commentaire tronqué à 250 caractères, limite jamais annoncée. 6. Téléphone en type=number. 7. Champ e-mail sans attribut autocomplete. 8. Date refusée avec « format JJ/MM/AAAA attendu », jamais indiqué avant.

**Illustration unique :** Une seule mise en situation stylisée pour quatre questions ; quatre repères 5 à 8 et aucun corrigé visible.
**Alternative textuelle à fournir :** Quatre situations de test présentées sans réponses pour une évaluation formative.

**Règle → préjudice utilisateur :** La bonne réponse peut sembler proche d’une autre règle : lire le défaut exact.

**Garantie recherchée (matière de l’oral)**

Une restitution sans support révèle les règles encore fragiles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lire chaque question, faire répondre par une seule règle, désignée par son objet, et une justification d’une phrase.
- Piège certification : Ne pas afficher les réponses simultanément. Questions originales, jamais qualifiées d’officielles.

**Corrigé (notes du présentateur, non projeté) :** 5=74 ; 6=95 (tel est le type approprié, number ne l’est pas) ; 7=97 ; 8=72 (80 est respectée : le message donne la raison du rejet).

**Discours oral du présentateur (non projeté)**

Nous passons à une évaluation rapide. Pour chaque situation, choisissez une seule règle, puis justifiez le choix en une phrase. Si plusieurs défauts sont imaginables, cherchez celui qui est précisément décrit. Après chaque groupe, je reviendrai sur une seule opposition clé. Les réponses ne sont pas projetées : elles sont réservées aux notes du présentateur.

**Mémo oral :** Justifier l’énoncé précis plutôt que deviner.

**Question de réactivation :** Reprendre à l’oral la question qui a le plus divisé le groupe, et faire justifier la réponse par le critère qui la distingue.

---

### S57 — Évaluation finale 3/4 : questions 9 à 12

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** quiz  
- **Durée indicative :** 2:30  
- **Objectif pédagogique :** Évaluer la connaissance des distinctions en condition de reconnaissance rapide.

**Texte visible (projection) :** 9. Champs à corriger listés, sans aucune raison. 10. Après une erreur, les réponses valides sont figées. 11. Demande en plusieurs pages envoyée sans vue d’ensemble. 12. « Demande reçue », mais ni menu ni lien pour continuer.

**Illustration unique :** Une seule mise en situation stylisée pour quatre questions ; quatre repères 9 à 12 et aucun corrigé visible.
**Alternative textuelle à fournir :** Quatre situations de test présentées sans réponses pour une évaluation formative.

**Règle → préjudice utilisateur :** La bonne réponse peut sembler proche d’une autre règle : lire le défaut exact.

**Garantie recherchée (matière de l’oral)**

Une restitution sans support révèle les règles encore fragiles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lire chaque question, faire répondre par une seule règle, désignée par son objet, et une justification d’une phrase.
- Piège certification : Ne pas afficher les réponses simultanément. Questions originales, jamais qualifiées d’officielles.

**Corrigé (notes du présentateur, non projeté) :** 9=80 ; 10=81 ; 11=83 ; 12=84 (85 est respectée : le résultat est annoncé).

**Discours oral du présentateur (non projeté)**

Nous passons à une évaluation rapide. Pour chaque situation, choisissez une seule règle, puis justifiez le choix en une phrase. Si plusieurs défauts sont imaginables, cherchez celui qui est précisément décrit. Après chaque groupe, je reviendrai sur une seule opposition clé. Les réponses ne sont pas projetées : elles sont réservées aux notes du présentateur.

**Mémo oral :** Justifier l’énoncé précis plutôt que deviner.

**Question de réactivation :** Reprendre à l’oral la question qui a le plus divisé le groupe, et faire justifier la réponse par le critère qui la distingue.

---

### S58 — Évaluation finale 4/4 : questions 13 à 16

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** quiz  
- **Durée indicative :** 2:30  
- **Objectif pédagogique :** Évaluer la connaissance des distinctions en condition de reconnaissance rapide.

**Texte visible (projection) :** 13. Étapes visibles, aucune signalée comme active. 14. « Précédent » efface l’étape antérieure. 15. Retour du navigateur : saisie effacée sans avertissement. 16. Régions groupées, mais dans un ordre incohérent.

**Illustration unique :** Une seule mise en situation stylisée pour quatre questions ; quatre repères 13 à 16 et aucun corrigé visible.
**Alternative textuelle à fournir :** Quatre situations de test présentées sans réponses pour une évaluation formative.

**Règle → préjudice utilisateur :** La bonne réponse peut sembler proche d’une autre règle : lire le défaut exact.

**Garantie recherchée (matière de l’oral)**

Une restitution sans support révèle les règles encore fragiles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Lire chaque question, faire répondre par une seule règle, désignée par son objet, et une justification d’une phrase.
- Piège certification : Ne pas afficher les réponses simultanément. Questions originales, jamais qualifiées d’officielles.

**Corrigé (notes du présentateur, non projeté) :** 13=88 ; 14=91 (89 est respectée : le bouton existe) ; 15=90 ; 16=94 (93 est respectée : les groupes existent).

**Discours oral du présentateur (non projeté)**

Nous passons à une évaluation rapide. Pour chaque situation, choisissez une seule règle, puis justifiez le choix en une phrase. Si plusieurs défauts sont imaginables, cherchez celui qui est précisément décrit. Après chaque groupe, je reviendrai sur une seule opposition clé. Les réponses ne sont pas projetées : elles sont réservées aux notes du présentateur.

**Mémo oral :** Justifier l’énoncé précis plutôt que deviner.

**Question de réactivation :** Reprendre à l’oral la question qui a le plus divisé le groupe, et faire justifier la réponse par le critère qui la distingue.

---

### S59 — Grand cas final : un formulaire à auditer en cinq minutes

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** atelier  
- **Durée indicative :** 5:00  
- **Objectif pédagogique :** Mobiliser les 30 règles et les transversales dans un cas de synthèse.

**Texte visible (projection) :** Dossier Mon Atelier, quatre écrans : étiquette absente, consignes détachées, code impossible à renvoyer, erreurs vagues, retour destructeur, résultat absent… et six autres défauts à trouver.

**Anomalies à représenter (verrouillées, une par repère, sans numéro de règle sur l’image) :**

- Écran 1 « Créer mon accès » : repère 1, champ « Courriel » avec un placeholder pour seule indication, et un zoom de code sans label ni aria-label ; repère 2, un seul champ de mot de passe, sans confirmation ; repère 3, écran du code de double authentification sans lien « Renvoyer le code ».
- Écran 2 « Coordonnées » : repère 4, consigne de format du téléphone reliée au champ dans le code, mais affichée en bas de page, loin du champ ; repère 5, champ téléphone qui ouvre un clavier numérique de calcul ; repère 6, liste des pays sans ordre identifiable ; repère 7, aucun focus visible sur le champ atteint au clavier.
- Écran 3 « Documents » : repère 8, justificatif demandé ici alors qu’il n’était pas annoncé au départ ; repère 9, bannière « Erreur » après envoi, sans champ signalé dans le titre ni dans les étiquettes ; repère 10, message « Valeur incorrecte » sans raison ni aide.
- Écran 4 « Vérification » : repère 11, retour par le bouton « Précédent » du formulaire vers l’écran Coordonnées, dont les champs sont vides ; repère 12, page finale avec menu, mais sans message de réussite ni d’échec.

**Illustration unique :** Une seule grande illustration fictive de parcours en quatre écrans, avec les douze anomalies listées ci-dessus, indiquées par des repères numérotés de 1 à 12 sans corrigé.
**Alternative textuelle à fournir :** Parcours fictif de formulaire comportant douze défauts repérés à diagnostiquer.

**Règle → préjudice utilisateur :** Un même dossier peut échouer sur des aspects de nature très différente.

**Garantie recherchée (matière de l’oral)**

L’utilisateur doit pouvoir comprendre, saisir, corriger, revenir et obtenir un résultat certain.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Demander en 5 minutes : identifier au moins dix défauts, leur règle, le geste de contrôle et le préjudice.
- Piège certification : Le cas comporte délibérément une règle transversale pour vérifier que le public ne limite pas sa recherche à 69–98.

**Discours oral du présentateur (non projeté)**

Dernier exercice. Vous avez devant vous le dossier fictif Mon Atelier. Le parcours comporte plusieurs anomalies : certaines se voient, d’autres nécessiteraient d’ouvrir le code ou d’interagir. Par équipes, retenez dix anomalies au minimum. Pour chacune, donnez la règle, l’impact humain et le test qui permettrait de le vérifier. L’objectif n’est pas de deviner une note, mais de décrire une investigation défendable.

**Mémo oral :** Un défaut → un risque → une règle → un contrôle.

---

### S60 — Débrief du grand cas : réparer le parcours, pas la façade

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** correction  
- **Durée indicative :** 2:10  
- **Objectif pédagogique :** Montrer comment justifier sans surinterpréter.

**Texte visible (projection) :** Écran 1 : règles 69, 75, 96. Écran 2 : règles 78, 95, 94, 165. Écran 3 : règles 86, 79, 80. Écran 4 : règles 91, 85.

**Illustration unique :** Même illustration que S59 ; chaque repère numéroté est accompagné, en texte, du numéro de sa règle. Le geste de contrôle reste dans le corrigé et l’oral.
**Alternative textuelle à fournir :** Parcours du grand cas avec correspondances entre anomalies, règles et mécanismes de test.

**Règle → préjudice utilisateur :** Une réparation de surface peut laisser subsister les erreurs fonctionnelles.

**Garantie recherchée (matière de l’oral)**

Un contrôle argumenté sépare les défauts observés des hypothèses à tester.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Détailler au moins dix défauts avec leur règle, leur préjudice et leur geste de contrôle ; vérifier qu’une règle transversale a été repérée.
- Piège certification : Un dessin ne prouve pas un défaut programmatique : le visuel suscite une vérification, non un verdict de code.

**Corrigé (notes du présentateur, non projeté) :** 1=69, inspecter le code : ni label ni aria-label ; 2=75, créer un compte ; 3=96, déclencher la procédure de test et chercher la relance ; 4=78, observer à plusieurs tailles d’écran (la consigne est reliée au champ dans le code : 70 et 72 sont respectées) ; 5=95, inspecter l’attribut type (tel attendu) ; 6=94, ouvrir la liste ; 7=165, règle transversale de la rubrique Navigation, parcourir à la tabulation ; 8=86, relire la page d’entrée du processus ; 9=79, provoquer un rejet et lire le titre de page et les étiquettes ; 10=80, provoquer plusieurs erreurs ; 11=91, faire un aller-retour avec le bouton « Précédent » du formulaire ; 12=85, soumettre et lire le résultat.

**Discours oral du présentateur (non projeté)**

Reprenons écran par écran. À la création d’accès : le courriel n’a qu’un placeholder, et l’inspection du code confirme l’absence de label et d’aria-label ; le mot de passe n’a pas de confirmation, et le code ne peut pas être renvoyé. Aux coordonnées : la consigne est loin du champ, le téléphone n’a pas le bon type, les pays n’ont pas d’ordre, et le focus clavier a disparu, ce qui relève de la navigation. Aux documents : les pièces n’étaient pas annoncées au départ, et le rejet ne dit ni où ni pourquoi. À la vérification : revenir efface les réponses, et la fin n’annonce aucun résultat. Notons à chaque fois ce que l’image ne permet pas, seule, de démontrer.

**Mémo oral :** Corriger une preuve, pas une impression.

---

### S61 — Le mémo des dix distinctions

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** synthese  
- **Durée indicative :** 1:15  
- **Objectif pédagogique :** Fixer une trame de révision orale rapide.

**Texte visible (projection) :** Nom/aide : code ou écran. Avant : obligation/format/casse/longueur. Après erreur : où/pourquoi/modifier/langue. Processus : liste/position/retour/perte.
**Mention visible :** « Regroupement pédagogique, non officiel. »

**Illustration unique :** Une seule carte mentale compacte organisée autour des cinq moments du parcours fictif.
**Alternative textuelle à fournir :** Carte mentale des notions à distinguer pour les formulaires Opquast.

**Règle → préjudice utilisateur :** Sous pression, l’oubli des distinctions produit des réponses approximatives.

**Garantie recherchée (matière de l’oral)**

Une organisation par intention aide à retrouver rapidement le numéro.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Faire redire les séries 69/70/77/78, 71–74, 79–82, 83–85, 87–91.
- Piège certification : Ce mémo aide la restitution, mais ne remplace pas l’étude des contenus officiels.

**Discours oral du présentateur (non projeté)**

Pour réviser, ne récitez pas une liste sèche. Reconstruisez notre histoire. Avant : quelle contrainte dois-je connaître ? Pendant : comment saisir, coller et comprendre ? En erreur : où, pourquoi, puis-je modifier, quelle langue ? Après l’envoi : récapitulatif, navigation, résultat. Dans un processus long : liste, étape courante, retour, historique, conservation. Vous retrouverez ainsi chaque règle à partir du besoin de l’utilisateur.

**Mémo oral :** Une histoire vaut mieux que trente cartes isolées.

---

### S62 — Dernière question : l’utilisateur garde-t-il la maîtrise ?

- **Acte :** 6. S’entraîner pour la certification  
- **Type :** conclusion  
- **Durée indicative :** 1:20  
- **Objectif pédagogique :** Terminer sur le principe central de l’assurance qualité numérique.

**Texte visible (projection) :** Trois réflexes : partir du préjudice décrit · distinguer les règles voisines par un seul critère · chercher aussi hors de la rubrique. Slogan : « Un bon formulaire laisse la main à l’utilisateur. »

**Illustration unique :** Frise unique du dossier Mon Atelier désormais complet, avec six étapes réussies.
**Alternative textuelle à fournir :** Parcours complet qui mène sans perte de données à une confirmation explicite.

**Règle → préjudice utilisateur :** Quand une étape échoue, le service peut exclure la personne malgré une interface esthétique.

**Garantie recherchée (matière de l’oral)**

Des pratiques vérifiables réduisent les risques à chaque moment d’un parcours.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Donner un dernier cas non étudié et demander quelle question la personne poserait d’abord.
- Piège certification : La réussite de la certification suppose l’apprentissage et l’entraînement personnels, pas une promesse de résultat.

**Discours oral du présentateur (non projeté)**

Notre fil rouge se termine : on a pu se préparer, comprendre chaque champ, saisir sans blocage, corriger sans perdre son travail, vérifier avant d’envoyer et obtenir une réponse claire. Voilà ce que ces trente règles construisent ensemble. Gardez trois réflexes. Partir du préjudice décrit par l’énoncé, pas d’un mot-clé. Distinguer les règles voisines par un seul critère : le code ou l’écran, avant ou après l’envoi, la liste ou la position. Et chercher aussi hors de la rubrique : couleur, clavier, contact ou sécurité. Pour réussir la certification, retenez moins des phrases par cœur que les problèmes humains qu’elles évitent et le contrôle qui prouverait qu’on a agi correctement.

**Mémo oral :** Préjudice, critère, transversalité : un bon formulaire laisse la main à l’utilisateur.

---

### S63 — Pour aller plus loin

- **Acte :** 6. S’entraîner pour la certification
- **Type :** ressources
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Donner les sources officielles pour réviser après la formation, puis ouvrir les questions.

**Texte visible (projection) :** Checklist Opquast V5 · Glossaire Formulaires · Livre « Qualité et conformité des services numériques » · Vos questions.

**Illustration unique :** Quatre cartes de ressources sobres, sans logo reproduit, autour du dossier Mon Atelier refermé.
**Alternative textuelle à fournir :** Quatre ressources pour réviser les règles Formulaires d’Opquast, suivies d’un temps de questions.

**Règle → préjudice utilisateur :** Sans source de référence, la révision repose sur des souvenirs approximatifs des intitulés.

**Garantie recherchée (matière de l’oral)**

Les intitulés officiels, le glossaire et le livre restent les références ; les exercices de cette formation sont des créations pédagogiques.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : Checklist : https://checklists.opquast.com/fr/qualite-numerique/ ; glossaire : https://training.opquast.com/digital-quality/glossaire/glossaire-formulaires/ ; livre (4e édition, 2026), rubrique Formulaires.
- Piège certification : Vérifier les modalités de certification sur le site Opquast au moment de l’inscription : un support de formation daté ne les garantit pas.

**Discours oral du présentateur (non projeté)**

Pour réviser, revenez toujours aux sources. La checklist donne les intitulés exacts et les fiches de chaque règle, avec leur mise en œuvre et leur contrôle. Le glossaire fixe le vocabulaire des formulaires. Le livre développe chaque rubrique. Nos exercices vous entraînent, mais ce ne sont pas des questions officielles. Place maintenant à vos questions.

**Mémo oral :** Réviser depuis les sources, pas depuis le support.

---
## Contrôle final de couverture

**30/30 règles 69–98 présentes chacune dans une slide de règle dédiée.** Les slides de synthèse et de QCM ne remplacent pas ces présentations.

| Règle | Slide dédiée | Lien officiel |
|---|---|---|
| 69 | S09 — À quoi sert ce champ ? | https://checklists.opquast.com/fr/qualite-numerique/69 |
| 70 | S10 — Ce que l’étiquette ne suffit pas à dire | https://checklists.opquast.com/fr/qualite-numerique/70 |
| 71 | S14 — Obligatoire : dites-le avant de demander | https://checklists.opquast.com/fr/qualite-numerique/71 |
| 72 | S15 — Format : ne transformez pas une devinette en erreur | https://checklists.opquast.com/fr/qualite-numerique/72 |
| 73 | S16 — La casse : quand « ABC » n’est pas « abc » | https://checklists.opquast.com/fr/qualite-numerique/73 |
| 74 | S17 — La longueur maximale : prévenir avant la troncature | https://checklists.opquast.com/fr/qualite-numerique/74 |
| 75 | S25 — Créer un mot de passe sans le créer par erreur | https://checklists.opquast.com/fr/qualite-numerique/75 |
| 76 | S26 — Je choisis de voir mon mot de passe | https://checklists.opquast.com/fr/qualite-numerique/76 |
| 77 | S11 — Une étiquette peut être correcte… mais trop loin | https://checklists.opquast.com/fr/qualite-numerique/77 |
| 78 | S12 — Une aide éloignée est une aide perdue | https://checklists.opquast.com/fr/qualite-numerique/78 |
| 79 | S32 — Une erreur doit désigner les champs concernés | https://checklists.opquast.com/fr/qualite-numerique/79 |
| 80 | S33 — Dire pourquoi, pas seulement « erreur » | https://checklists.opquast.com/fr/qualite-numerique/80 |
| 81 | S34 — Ne faites pas payer deux fois la même saisie | https://checklists.opquast.com/fr/qualite-numerique/81 |
| 82 | S35 — Le message d’erreur parle la langue du formulaire | https://checklists.opquast.com/fr/qualite-numerique/82 |
| 83 | S38 — Avant de confirmer, voir l’ensemble du dossier | https://checklists.opquast.com/fr/qualite-numerique/83 |
| 84 | S39 — Après l’envoi, ne pas créer une impasse | https://checklists.opquast.com/fr/qualite-numerique/84 |
| 85 | S40 — Un formulaire doit répondre clairement « oui » ou « non » | https://checklists.opquast.com/fr/qualite-numerique/85 |
| 86 | S43 — Préparer les pièces avant le début du parcours | https://checklists.opquast.com/fr/qualite-numerique/86 |
| 87 | S44 — Un processus complexe montre toutes ses étapes | https://checklists.opquast.com/fr/qualite-numerique/87 |
| 88 | S45 — Savoir précisément où l’on est | https://checklists.opquast.com/fr/qualite-numerique/88 |
| 89 | S46 — Revenir à l’étape précédente sans bricolage | https://checklists.opquast.com/fr/qualite-numerique/89 |
| 90 | S47 — Le bouton Retour du navigateur peut coûter cher | https://checklists.opquast.com/fr/qualite-numerique/90 |
| 91 | S48 — Revenir ne doit pas effacer les réponses précédentes | https://checklists.opquast.com/fr/qualite-numerique/91 |
| 92 | S24 — Copier et coller fait partie de la saisie normale | https://checklists.opquast.com/fr/qualite-numerique/92 |
| 93 | S21 — Une liste longue doit avoir des groupes | https://checklists.opquast.com/fr/qualite-numerique/93 |
| 94 | S22 — Une liste doit avoir un ordre repérable | https://checklists.opquast.com/fr/qualite-numerique/94 |
| 95 | S19 — Le bon type HTML aide aussi sur mobile | https://checklists.opquast.com/fr/qualite-numerique/95 |
| 96 | S27 — Code expiré : pouvoir recommencer la double authentification | https://checklists.opquast.com/fr/qualite-numerique/96 |
| 97 | S20 — L’autocomplétion se prépare dans le code | https://checklists.opquast.com/fr/qualite-numerique/97 |
| 98 | S28 — Un bouton désactivé doit rester compréhensible | https://checklists.opquast.com/fr/qualite-numerique/98 |

**Règles connexes citées** (rubrique ; slides) — intitulés et rubriques relus via le MCP (instantané du 3 septembre 2026) :

- 10 (Contenus) : S38, S42, S51
- 24 (Données personnelles) : S51
- 26 (Données personnelles, nouvelle en V5) : S51
- 103 (Identification et contact) : S51
- 108 (Identification et contact) : S42, S51
- 110 (Identification et contact) : S40, S42, S51
- 165 (Navigation) : S51, S60
- 166 (Navigation) : S51
- 167 (Navigation) : S51
- 172 (Navigation) : S43, S51
- 173 à 176 (Newsletter) : S51
- 181 (Présentation) : S51
- 201 à 205 (Sécurité) : S29, S51
- 236 (Structure et code) : S51, S53

**13/13 termes du glossaire :** présentés dans S05, S06 et S07 ; le glossaire officiel en classe 11 en Formulaires, plus Opt-in et Opt-out, rangés aussi en Données personnelles.  
**Structure :** introduction S01–S08, dont le plan en S03 ; développement en cinq actes S09–S50 ; entraînement S51–S60 ; conclusion S61–S63.  
**Vérification pédagogique :** 3 points de réactivation (S23, S30, S37), 16 questions d’évaluation finale (S55 à S58), cas intégrateur S50, grand cas S59–S60 ; chaque corrigé figure dans les notes du présentateur de sa slide.  
**Limite :** ce storyboard ne reproduit pas les questions officielles de l’examen et ne peut garantir son résultat.

## Revue avant génération

- 29 octobre 2026 : v001, édition de travail.
- 6 novembre 2026 : revue MCP (auto-vérification), 4 corrections bloquantes et 7 recommandées, appliquées en v002 avec plan et conclusion.
- 6 novembre 2026 : validation indépendante (sous-agent, MCP Opquast, skill opquast-skill, fiches publiques, livre), 4 constats bloquants, 9 importants et 10 mineurs ; vérification complémentaire dans NotebookLM (livre et corpus d’articles), qui confirme les attributions au livre et rétablit la nouveauté V5 de 96, 97 et 98.
- 6 novembre 2026 : v003, tous les constats traités, sauf la décision sur les exceptions au guide, réservée à Alex.
- 6 novembre 2026 : décision d’Alex, contrat de la Fabrique appliqué ; v004, discours oraux et mémos réécrits sans numéros de règles, sous-titres d’acte.
- 6 novembre 2026 : v005, chaque règle 69 à 98 est la bonne réponse d’au moins un exercice corrigé ; textes visibles des exercices allégés.
- 6 novembre 2026 : relecture indépendante de la v005 (oraux comparés à la v003, exercices confrontés aux fiches) : 1 constat bloquant, 7 importants, 9 mineurs ; tous traités en v006. Fin des boucles de raffinement : troisième passe.
- 6 novembre 2026 : v007, avis de l’expert du livre ajoutés sur douze règles (passages retrouvés via NotebookLM, vérifiés mot pour mot dans le fichier du livre) ; deux oraux raccourcis ; instantané MCP comparé aux fiches publiques du 6 novembre 2026 : contenu identique pour les 30 règles.
- Résultat : `VALIDE_POUR_GENERATION`, décision d’Alex du 6 novembre 2026 ; empreinte SHA-256 enregistrée dans `run.json`. Gate humain sur les quatre étalons (S01, S13, S30, S60) avant la suite de la série.

## Sources principales

- **Référentiel officiel Opquast V5 (245 règles)** : https://checklists.opquast.com/fr/qualite-numerique/ ; Intitulés et numéros des règles ; source primaire.
- **Glossaire Opquast, rubrique Formulaires** : https://training.opquast.com/digital-quality/glossaire/glossaire-formulaires/ ; 13 notions principales de vocabulaire.
- **Publication du référentiel V5 (2 octobre 2025)** : https://www.opquast.com/publication-de-la-version-5-du-referentiel-opquast/ ; huit règles ajoutées, dont 26, 96, 97 et 98 ; conditions de réutilisation. Passage vérifié dans le corpus du MCP et dans NotebookLM le 6 novembre 2026.
- **Point d’étape V5 (29 avril 2025)** : https://www.opquast.com/check-list-opquast-version-5-point-detape-29-avril-2025/ ; propositions de nouvelles règles, dont le renvoi du code à double facteur (96) et les boutons désactivés non masqués aux lecteurs d’écran (98) ; la proposition sur le placeholder n’est pas dans les 245 règles.
- **Avis de l’expert** : livre, 4e édition 2026, rubrique 4 « Formulaires », cité sur douze slides ; passages vérifiés dans `Livre-Qualite-Conformite-Numerique/qualite-et-conformite-des-services-numeriques-llm.md`.
- **Fiches détaillées des règles 69 à 98** : mise en œuvre et contrôle lus via le MCP Opquast (instantané local du 3 septembre 2026), recoupés avec les fiches publiques et le livre le 6 novembre 2026. Les intitulés suivent la checklist publique du 6 novembre 2026 ; l’instantané local diffère pour 92 (« copier coller ») et 95 (« type mail »).
- **Placeholder, l’attribut maudit (article 2017)** : https://www.opquast.com/20170131placeholder-attribut-maudit/ ; Information permanente vs exemple provisoire.
- **Accessibilité de nos formations et examens en ligne (article 2019)** : https://www.opquast.com/accessibilite-de-nos-formations-et-examens-en-ligne/ ; Retour d’expérience sur parcours au lecteur d’écran.
- **Ces règles qui ne sont rien (newsletter 113, 2024)** : https://www.opquast.com/edito-newsletter-n113-ces-regles-qui-ne-sont-rien/ ; Impact de l’interdiction du collage.
- **Juste un petit formulaire (newsletter 36, 2017)** : https://www.opquast.com/20170331edito-juste-un-petit-formulaire/ ; Coût et transversalité de la conception.
- **226 mini-user stories (article 2016)** : https://www.opquast.com/20161012226-mini-user-stories/ ; Préjudices et bénéfices formulés côté utilisateur.
- **Opquast et l’accessibilité (article 2017)** : https://www.opquast.com/opquast-et-laccessibilite/ ; Complémentarité qualité / accessibilité.
- **Naviguons au clavier, vite (newsletter 98, 2023)** : https://www.opquast.com/edito-newsletter-n98-naviguons-au-clavier-vite/ ; Priorité aux tests de navigation clavier.
- **Livre :** Élie Sloïm et Laurent Denis, *Qualité et conformité des services numériques*, 4e édition (2026), partie 3 « Référentiel Opquast », rubrique 4 « Formulaires » ; partie 2, chapitre 3 « Déploiement en projet numérique » et chapitre 7 « Aspects économiques et coûts qualité ». Source disponible dans le corpus de connaissances de l’Assistant Opquast.
- **Attribution et licence :** règles et objectifs officiels du référentiel sous licence Creative Commons BY-SA selon Opquast. Les scripts oraux, synthèses et exercices ici sont des créations pédagogiques nouvelles ; ne pas réutiliser aveuglément les images et textes éditoriaux originaux.
