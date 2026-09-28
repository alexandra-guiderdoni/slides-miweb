# Alternatives textuelles - Internationalisation selon Opquast V5 - V2

Notes du présentateur révisées - internationalisation-opquast-v5-v2

## Slide 1 - Internationalisation

### Alternative textuelle

Trois exigences autour d’un service multilingue : contexte, langue, continuité.

### Transcription

#### Lecture du visuel

La slide introduit la thématique Internationalisation autour de trois axes pédagogiques : **Contexte, Langue, Continuité**.

Au centre, une personne consulte un service multilingue. Trois zones structurent la lecture :

- **Contexte explicite** : le visuel montre des informations qui ne doivent pas être laissées à deviner selon le pays ou les conventions locales.
- **Langue identifiable** : l’interface permet d’identifier clairement la langue utilisée ou proposée.
- **Parcours préservé** : le changement de langue ne doit pas faire perdre le contexte de navigation.

#### Idée directrice

Internationaliser un service ne consiste pas seulement à traduire des textes. Il faut aussi rendre explicites les conventions locales, permettre aux personnes et aux outils d’identifier la langue et préserver la continuité du parcours.

#### Point de vigilance Opquast

Les exemples de **devise** ou de **formats** visibles dans le bloc « Contexte explicite » illustrent l’internationalisation au sens large. Ils ne correspondent pas, à eux seuls, à des règles de la rubrique 128 à 135.

Les axes `Contexte · Langue · Continuité` constituent un **regroupement pédagogique**, pas une classification officielle Opquast.

#### Message à retenir

**Ne rien faire deviner qui dépend du pays ou de la langue.**

### Discours oral

#### Un service international rend le contexte et la langue prévisibles

- Un numéro de téléphone ou une adresse peuvent être consultés depuis un autre pays : le contexte local ne peut donc pas rester implicite.
- La langue doit être identifiable dans le code pour les outils, mais aussi avant que l’utilisateur suive un lien.
- Lorsqu’une traduction équivalente existe, changer de langue doit conserver la page courante plutôt que recommencer le parcours depuis l’accueil.
- Quand le service propose plusieurs versions linguistiques, la préférence transmise par l’outil de consultation guide la version servie.
- Ces règles ont un point commun : réduire ce que l’utilisateur ou les outils doivent deviner et préserver la continuité du parcours.

#### Transition

Le sens de chaque exigence apparaît d’abord dans le préjudice concret qu’elle évite.

## Slide 2 - Commencer par le préjudice utilisateur

### Alternative textuelle

Quatre étapes relient la situation, le préjudice, la garantie et la règle.

### Transcription

#### Lecture du visuel

La slide présente une méthode en quatre temps :

1. **Situation**
2. **Préjudice**
3. **Garantie**
4. **Règle**

L’exemple part d’un lien en français qui mène vers une page en anglais. Le changement de langue surprend l’utilisateur. La version améliorée annonce la langue avant le clic.

#### Idée directrice

Le numéro de règle vient après la compréhension du problème utilisateur.

#### Point de vigilance Opquast

Les drapeaux éventuellement représentés dans le visuel sont seulement illustratifs. Opquast n’impose pas l’usage d’un drapeau pour signaler une langue.

#### Message à retenir

**Quel préjudice ? Que cherche à garantir la règle ?**

### Discours oral

#### Le préjudice donne le sens de l’exigence

- Passer d’une langue à une autre n’est pas un problème en soi.
- La difficulté apparaît lorsque l’utilisateur découvre ce changement seulement après avoir activé le lien.
- La règle 131 vise précisément ce risque : la langue principale de la page cible doit être identifiable lorsqu’elle diffère de celle de la page d’origine.
- L’information peut venir du libellé, du contexte du lien ou d’une icône appropriée.
- Aucune représentation unique n’est imposée : l’utilisateur doit simplement pouvoir anticiper avant d’agir.

#### Transition

Cette logique s’applique maintenant aux coordonnées dont le contexte local reste implicite.

## Slide 3 - Ne pas faire deviner le contexte local

### Alternative textuelle

Fiches de contact comparées, sans puis avec indicatif international et pays.

### Transcription

#### Lecture du visuel

Deux fiches de contact sont comparées.

À gauche, le contexte reste implicite :

- `01 23 45 67 89`
- `10 rue Exemple, Paris`

À droite, les informations sont explicitées :

- `+33 1 23 45 67 89`
- `10 rue Exemple, Paris, France`

#### Règle 128

**« L'indicatif international est disponible pour tous les numéros de téléphone. »**

#### Règle 129

**« Le pays est précisé pour toutes les adresses postales. »**

#### Vérification

Pour les numéros : vérifier que l’indicatif international nécessaire est disponible. Il peut notamment être indiqué directement avec chaque numéro.

Pour les adresses : vérifier que le pays est écrit explicitement, sans demander à l’utilisateur de le déduire de la ville, du code postal ou du téléphone.

#### Point de vigilance Opquast

« Disponible » ne signifie pas nécessairement que l’indicatif doit être répété devant chaque numéro.

Cas A, indicatif directement dans le numéro :

- Téléphone : `+33 1 23 45 67 89`

C’est la solution la plus immédiate pour l’utilisateur.

Cas B, indicatif fourni globalement :

- France : indicatif international `+33`
- Téléphone : `01 23 45 67 89`
- Assistance : `01 98 76 54 32`

L’indicatif reste disponible pour les numéros concernés sans être répété devant chacun.

**À retenir** : la règle exige que l’utilisateur puisse disposer de l’indicatif international nécessaire, pas qu’une présentation unique soit utilisée.

#### Message à retenir

**Indicatif et pays : rendre explicite ce que le contexte local suppose.**

### Discours oral

#### Chaque coordonnée porte son contexte international

- Un numéro présenté seulement dans son format national suppose que l’utilisateur connaît déjà le pays.
- Pour le contrôle de la règle 128, chaque numéro est précédé de l’indicatif international et le premier zéro du numéro national est retiré.
- Pour la règle 129, le pays est écrit explicitement dans chaque adresse postale.

##### Impact du non-respect

- Une personne située à l’étranger peut ne pas savoir comment composer le numéro.
- Une ville ou un code postal ne suffisent pas toujours à identifier le pays sans ambiguïté.

##### Ce que garantissent les règles

- Le contact téléphonique peut être utilisé immédiatement, quel que soit le contexte de consultation.
- Le pays associé à l’adresse est identifiable sans recourir à d’autres indices.

#### Transition

Après le contexte géographique, une autre information doit être explicite pour les outils : la langue principale de la page.

## Slide 4 - La page doit déclarer sa langue principale

### Alternative textuelle

Une page française déclare sa langue principale dans son code source.

### Transcription

#### Lecture du visuel

Une page en français est reliée à trois usages automatisés :

- **Synthèse vocale**
- **Traduction**
- **Indexation**

Sous la page, le code affiche :

`<html lang="fr">`

#### Règle 130

**« Le code source de chaque page indique la langue principale du contenu. »**

#### Vérification

Contrôler la présence et la pertinence de l’attribut `lang` sur l’élément `html`, par exemple `<html lang="fr">`.

#### Point de vigilance Opquast

La **langue de traitement** déclarée avec `lang` ne doit pas être confondue avec la langue ou les langues du public cible.

#### Message à retenir

**La langue de traitement ne doit pas être devinée.**

### Discours oral

#### La langue déclarée permet aux outils d’interpréter la page

- La langue principale est indiquée dans le code avec un code de langue valide et pertinent.
- L’attribut `lang` de l’élément `html` donne cette information par défaut à l’ensemble du document.
- La langue déclarée décrit le contenu à traiter, pas le public auquel le service souhaite s’adresser.

##### Impact du non-respect

- Une synthèse vocale peut appliquer des règles de prononciation inadaptées.
- Les outils de traduction et d’indexation disposent de moins d’informations pour interpréter le contenu.

##### Ce que garantit la règle

- Les outils peuvent identifier la langue principale sans la déduire du texte.
- La lecture vocale, la traduction automatique et l’indexation peuvent traiter la page selon la langue déclarée.

#### Transition

Cette déclaration globale doit ensuite être précisée lorsqu’un passage change de langue.

## Slide 5 - Dans une page, chaque changement de langue compte

### Alternative textuelle

Une expression anglaise dans une page française est signalée dans le code.

### Transcription

#### Lecture du visuel

Une page principalement rédigée en français contient l’expression anglaise :

`Open quality standards`

Le changement de langue est associé au repère :

`lang="en"`

Le visuel relie ce signalement à la synthèse vocale et à une prononciation correcte.

#### Règle 132

**« Chaque changement de langue est signalé. »**

#### Vérification

Repérer les contenus rédigés dans une autre langue que la langue principale et vérifier qu’un attribut `lang` approprié est présent ou hérité.

#### Nuance

La règle ne s’applique pas nécessairement aux noms propres ou à tous les mots d’origine étrangère passés dans l’usage courant. En cas de doute, la prononciation par une synthèse vocale constitue un bon critère de décision.

#### Message à retenir

**Changer de langue doit aussi être indiqué dans le code.**

### Discours oral

#### Un changement de langue se déclare là où il se produit

- La langue principale de la page reste la référence tant qu’aucun changement local n’est indiqué.
- Un passage dans une autre langue reçoit un attribut `lang` adapté sur l’élément concerné ou l’hérite d’un élément parent.
- La règle s’applique aussi aux textes placés dans les attributs HTML et restitués à l’utilisateur, par exemple l’alternative d’une image.

##### Impact du non-respect

- Une aide technique peut continuer à appliquer la prononciation de la langue principale au passage concerné.
- Un outil de traduction automatique peut interpréter moins correctement l’alternance des langues.

##### Ce que garantit la règle

- Les aides techniques peuvent interpréter chaque passage selon la langue déclarée.
- Les outils linguistiques disposent d’une information locale correspondant réellement au contenu.

#### Transition

La langue doit aussi être connue avant de suivre un lien vers une autre page.

## Slide 6 - Annoncer la langue avant le clic

### Alternative textuelle

Deux liens comparés : sans mention de langue, puis avec la langue cible.

### Transcription

#### Lecture du visuel

Deux situations sont comparées.

À gauche, un lien intitulé `Documentation` ouvre une page anglaise sans avertissement.

À droite, le lien indique :

`Documentation — English`

L’utilisateur connaît donc la langue cible avant de cliquer.

#### Règle 131

**« La langue principale de la page cible d'un lien est identifiable lorsqu'elle diffère de celle de la page d'origine. »**

#### Vérification

Repérer les liens menant vers une page dans une autre langue et vérifier que cette langue est identifiable immédiatement : dans le libellé, le contexte ou éventuellement via une icône appropriée.

#### Point de vigilance Opquast

L’attribut `hreflang` seul ne suffit pas, car il n’est pas nativement restitué à l’utilisateur par les navigateurs.

#### Message à retenir

**Pas de surprise de langue après le clic.**

### Discours oral

#### La langue cible doit être connue avant l’activation

- Le contrôle porte sur les liens dont la page cible utilise une autre langue principale que la page d’origine.
- L’information doit être disponible immédiatement, avant que l’utilisateur active le lien.
- Elle peut être portée par le libellé, par le contexte immédiat ou par une icône appropriée.

##### Impact du non-respect

- L’utilisateur peut ouvrir une page qu’il ne comprend pas.
- Cette action inutile lui fait perdre du temps et peut interrompre sa navigation.

##### Ce que garantit la règle

- L’utilisateur peut anticiper le changement de langue.
- Il décide en connaissance de cause s’il souhaite consulter la page cible.

#### Transition

Une fois la langue choisie, le service doit encore préserver la page que l’utilisateur consultait.

## Slide 7 - Changer de langue sans perdre la page courante

### Alternative textuelle

Changer de langue renvoie à l’accueil, ou mène à la même page traduite.

### Transcription

#### Lecture du visuel

Deux parcours sont comparés depuis une fiche produit en français.

**Mauvaise pratique** : le changement vers l’anglais renvoie à la page d’accueil anglaise.

**Bonne pratique** : le changement vers l’anglais affiche directement la traduction de la fiche produit courante.

#### Règle 133

**« Les liens d'accès aux versions traduites pointent directement vers la traduction de la page courante. »**

#### Vérification

Sur une page traduite, vérifier que le changement de langue conduit directement à la version traduite de cette même page, sans retour à la page d’accueil.

#### Message à retenir

**Changer de langue, pas recommencer sa navigation.**

### Discours oral

#### Changer de langue sans perdre le contenu courant

- Lorsqu’une page possède une version traduite, son lien de changement de langue conduit directement à cette version.
- Un retour à l’accueil de la version linguistique ne conserve pas le contexte de consultation.
- Le contrôle porte sur la correspondance entre les deux pages, pas seulement sur la présence générale de plusieurs langues dans le site.

##### Impact du non-respect

- L’utilisateur perd la page qu’il consultait.
- Il doit retrouver seul le même contenu dans une navigation qu’il connaît parfois moins bien.

##### Ce que garantit la règle

- La traduction de la page courante est accessible directement et immédiatement.
- Le changement de langue préserve la continuité du parcours.

#### Transition

Encore faut-il que le lien vers cette version soit compréhensible par la personne à laquelle il s’adresse.

## Slide 8 - Le lien vers une langue doit parler cette langue

### Alternative textuelle

Deux liens comparés : Version anglaise, puis English version.

### Transcription

#### Lecture du visuel

Deux liens vers une version anglaise sont comparés.

À gauche :

`Version anglaise`

À droite :

`English version`

Le second lien est directement rédigé dans la langue de la page cible.

#### Règle 134

**« Les liens vers les versions équivalentes des contenus sont rédigés dans leur langue cible. »**

#### Vérification

Pour chaque lien menant vers une autre version linguistique du contenu, vérifier que son libellé est rédigé dans la langue cible.

#### Message à retenir

**Le public cible doit reconnaître son propre lien.**

### Discours oral

#### Le lien parle la langue de la personne qui le cherche

- Un lien vers une version équivalente est rédigé dans la langue de cette version.
- La même exigence s’applique à l’alternative textuelle lorsque le lien est porté par une image.
- Le libellé est ainsi compréhensible sans maîtriser d’abord la langue de la page d’origine.

##### Impact du non-respect

- L’utilisateur peut ne pas reconnaître le lien qui lui est destiné.
- Une version pourtant disponible reste difficile à trouver pour son public.

##### Ce que garantit la règle

- Le lien pertinent peut être identifié immédiatement.
- Le passage vers une version linguistique équivalente reste compréhensible pour le public concerné.

#### Transition

Au-delà des liens, le serveur peut aussi tenir compte des préférences linguistiques déjà exprimées dans l’outil de consultation.

## Slide 9 - Servir d’abord la langue préférée de l’utilisateur

### Alternative textuelle

Le navigateur demande fr, es puis en ; le serveur répond en français.

### Transcription

#### Lecture du visuel

Le navigateur envoie un ordre de préférence linguistique :

`fr > es > en`

Le serveur dispose de versions :

`FR · ES · EN`

La réponse renvoyée est la version française, première langue disponible dans l’ordre de préférence.

#### Règle 135

**« Le serveur respecte l'ordre préférentiel de langues des outils de consultation. »**

#### Vérification

Modifier l’ordre des langues préférées du navigateur et vérifier que le serveur renvoie prioritairement la première version disponible correspondante.

#### Message à retenir

**Si la bonne version existe, la servir en priorité.**

### Discours oral

#### L’ordre des préférences guide la version servie

- L’outil de consultation peut transmettre au serveur une liste ordonnée de langues préférées.
- Sur un service disponible en plusieurs langues, le serveur examine cet ordre pour choisir la version à renvoyer.
- La règle porte sur les versions réellement proposées par le service, sans exiger que toutes les langues existent.

##### Impact du non-respect

- L’utilisateur peut recevoir une version moins adaptée alors qu’une version correspondant mieux à ses préférences est disponible.

##### Ce que garantit la règle

- La version correspondant à la langue préférée disponible est envoyée prioritairement.
- Le choix déjà exprimé dans l’outil de consultation est pris en compte par le service.

#### Transition

Ces exigences peuvent maintenant être reconnues dans quatre situations concrètes.

## Slide 10 - Cas pratiques

### Alternative textuelle

Quatre cas d’exercice sur le contexte local, la langue et le parcours.

### Transcription

#### Lecture du visuel

Quatre situations sont proposées comme exercices originaux de formation :

- **A · Numéro local** : un numéro est affiché sans indicatif international.
- **B · Langue surprise** : un lien en français ouvre une page anglaise.
- **C · Retour à l’accueil** : changer de langue renvoie vers la page d’accueil.
- **D · Changement non signalé** : une expression anglaise apparaît dans une page française.

#### Question de relecture

Pour chaque cas :

1. Quel préjudice l’utilisateur peut-il subir ?
2. Que devrait garantir le service ?
3. Quelle règle permet de retrouver cette exigence ?

#### Point de vigilance Opquast

Le cas D est visuellement résumé par une expression anglaise « sans explication ». **La règle 132 ne demande pas une explication visible** : elle demande que le changement de langue soit signalé dans le code, notamment avec l’attribut `lang`.

#### Message à retenir

**D’abord le préjudice, ensuite le numéro.**

### Discours oral

#### Quatre ruptures, quatre protections

- Un numéro seulement national n’est pas immédiatement utilisable depuis l’étranger : la règle 128 rend l’indicatif international disponible avec le numéro.
- Un lien qui masque la langue cible crée une surprise après l’activation : la règle 131 permet de l’anticiper.
- Un changement de langue qui renvoie à l’accueil fait perdre le contenu courant : la règle 133 préserve la page consultée.
- Un passage étranger non déclaré peut être mal interprété par les aides techniques : la règle 132 signale localement sa langue.
- Dans chaque cas, la protection intervient avant l’action ou au moment exact où le parcours risque de se rompre.

#### Transition

Ces quatre situations rejoignent une même exigence : rendre la langue et le parcours prévisibles.

## Slide 11 - Une langue identifiable, un parcours prévisible

### Alternative textuelle

Les huit règles regroupées en quatre questions utilisateur.

### Transcription

#### Lecture du visuel

Les huit règles de la rubrique sont regroupées pédagogiquement en quatre questions.

#### Expliciter le contexte

- **128** : L'indicatif international est disponible pour tous les numéros de téléphone.
- **129** : Le pays est précisé pour toutes les adresses postales.

#### Identifier la langue

- **130** : Le code source de chaque page indique la langue principale du contenu.
- **131** : La langue principale de la page cible d'un lien est identifiable lorsqu'elle diffère de celle de la page d'origine.
- **132** : Chaque changement de langue est signalé.
- **134** : Les liens vers les versions équivalentes des contenus sont rédigés dans leur langue cible.

#### Préserver le parcours

- **133** : Les liens d'accès aux versions traduites pointent directement vers la traduction de la page courante.

#### Respecter les préférences

- **135** : Le serveur respecte l'ordre préférentiel de langues des outils de consultation.

#### Note de cadrage

Ce regroupement est pédagogique et ne constitue pas un classement officiel Opquast.

#### Message à retenir

**Pas de langue à deviner, pas de parcours à recommencer.**

### Discours oral

#### Prévoir la langue sans perdre le fil

- Les coordonnées deviennent utilisables lorsque le contexte géographique n’est plus laissé à deviner.
- La langue doit être comprise par les outils dans le code et identifiable par l’utilisateur dans l’interface.
- Changer de version linguistique doit conserver le contenu actuellement consulté.
- Lorsque plusieurs versions sont disponibles, leur sélection tient compte de l’ordre de préférence transmis par l’outil de consultation.
- Ces exigences se complètent : comprendre le contexte, anticiper la langue, rester sur la bonne page et recevoir la version la plus adaptée.

#### Transition

Cette prévisibilité dépend aussi de règles classées hors de la rubrique Internationalisation.

## Slide 12 - L’internationalisation dépasse la rubrique

### Alternative textuelle

Internationalisation reliée aux conventions, à l’interface et à l’encodage.

### Transcription

#### Lecture du visuel

La rubrique Internationalisation est placée au centre et reliée à trois familles de risques transversaux :

- **Conventions locales** : règles 4 et 149.
- **Langue de l’interface** : règle 82.
- **Caractères et encodage** : règles 228, 232 et 233.

#### Règles transversales représentées

- **4** : Les dates sont présentées dans des formats explicites.
- **82** : Les messages d'erreur personnalisés sont exprimés dans la langue du formulaire.
- **149** : La langue des fichiers en téléchargement est précisée lorsqu'elle diffère de celle de la page d'origine.
- **228** : Les entêtes envoyés par le serveur contiennent les informations relatives au jeu de caractères employé.
- **232** : Le code source de chaque page contient une métadonnée qui définit le jeu de caractères.
- **233** : Le codage de caractères utilisé est UTF-8.

#### Périmètre

Ces règles ne font pas partie de la rubrique officielle 128 à 135. Elles sont présentées ici parce qu’elles répondent directement à des risques liés au contexte international.

#### Autres rapprochements transversaux

Certaines règles des images et médias peuvent également contribuer à l’internationalisation :

- **Règle 121** : « Chaque contenu audio et vidéo est accompagné de sa transcription textuelle. » La transcription permet notamment l’exploitation du contenu par des outils linguistiques et sa traduction.
- **Règles 117 et 118** : les alternatives textuelles des images-liens et des images porteuses d’information rendent également ces informations textuelles exploitables, notamment par des outils de traduction automatique.

Ces règles ne font pas partie de la rubrique Internationalisation. Elles illustrent la transversalité du sujet.

#### Message à retenir

**Les rubriques classent les règles. Les risques, eux, se croisent.**

### Discours oral

#### L’internationalisation traverse plusieurs rubriques

- Une date doit rester explicite malgré les différences de conventions de lecture.
- La langue d’un fichier doit être connue avant son téléchargement lorsqu’elle diffère de celle de la page.
- Un message d’erreur personnalisé doit rester dans la langue du formulaire.
- L’encodage doit être déclaré et réellement appliqué pour préserver les caractères.
- Les alternatives textuelles des images et les transcriptions des médias rendent également leur information exploitable sous forme de texte.
- Ces rapprochements décrivent des risques internationaux communs, sans modifier le classement officiel des règles.

#### Transition

Le premier point commun concerne l’anticipation : comprendre une date et connaître la langue d’un fichier avant d’agir.

## Slide 13 - Ce qui varie selon le pays doit être explicité

### Alternative textuelle

Date et fichier comparés, d’abord ambigus, puis explicités.

### Transcription

#### Lecture du visuel

Deux comparaisons sont présentées.

Pour la date :

- ambigu : `12/11/10`
- explicite : `12 novembre 2010`

Pour le téléchargement :

- ambigu : `Rapport PDF`
- explicite : `Report PDF — English`

#### Règle 4

**« Les dates sont présentées dans des formats explicites. »**

#### Règle 149

**« La langue des fichiers en téléchargement est précisée lorsqu'elle diffère de celle de la page d'origine. »**

#### Vérification

Pour la règle 4 : le mois est écrit en lettres et l’année sur quatre chiffres.

Pour la règle 149 : lorsque la langue du fichier diffère de celle de la page, l’utilisateur peut connaître cette langue avant de télécharger.

#### Message à retenir

**Avant d’interpréter ou de télécharger : expliciter.**

### Discours oral

#### Les conventions doivent être explicites avant l’action

- Pour une date affichée, le mois est écrit en lettres et l’année comporte quatre chiffres.
- Les dates saisies par l’utilisateur ne sont pas concernées lorsqu’un sélecteur de date ou une indication du format attendu lève l’ambiguïté.
- Pour un fichier rédigé dans une autre langue que la page, cette langue est annoncée dans le lien ou dans son contexte.

##### Impact du non-respect

- Une date numérique peut être interprétée différemment selon les conventions nationales.
- L’utilisateur peut télécharger un fichier avant de découvrir qu’il ne comprend pas sa langue.

##### Ce que garantissent les règles

- La date peut être comprise et réutilisée sans méprise sur son sens.
- La langue du fichier est connue avant le téléchargement, ce qui évite une action inutile.

#### Transition

La cohérence linguistique doit aussi résister au moment où le formulaire signale une erreur.

## Slide 14 - Même formulaire, même langue

### Alternative textuelle

Message d’erreur en anglais, puis dans la langue du formulaire.

### Transcription

#### Lecture du visuel

Deux formulaires français sont comparés.

À gauche, le message d’erreur apparaît en anglais :

`This field is required`

À droite, le message est exprimé dans la langue du formulaire :

`Ce champ est obligatoire`

#### Règle 82

**« Les messages d'erreur personnalisés sont exprimés dans la langue du formulaire. »**

#### Vérification

Déclencher les erreurs du formulaire et vérifier que les messages personnalisés sont exprimés dans la même langue que les libellés et étiquettes du formulaire.

#### Message à retenir

**L’aide doit rester dans la langue de l’interaction.**

### Discours oral

#### L’erreur reste dans la langue du formulaire

- La règle porte sur les messages d’erreur personnalisés affichés pendant la saisie.
- Leur langue correspond à celle des autres libellés du formulaire, notamment les étiquettes des champs.
- Les outils de gestion des erreurs doivent donc fournir les traductions réellement utilisées par chaque version du formulaire.

##### Impact du non-respect

- L’utilisateur peut ne pas comprendre ce qu’il doit corriger au moment où il a besoin d’aide.
- La rupture de langue augmente la difficulté de saisie.

##### Ce que garantit la règle

- Les erreurs personnalisées restent compréhensibles dans le contexte du formulaire.
- L’utilisateur peut identifier plus facilement la correction attendue.

#### Transition

La langue peut enfin être correcte sur le fond tout en devenant illisible si les caractères sont mal encodés.

## Slide 15 - Serveur, page et contenu doivent parler le même encodage

### Alternative textuelle

Serveur, document et contenu déclarent le même encodage UTF-8.

### Transcription

#### Lecture du visuel

La slide représente trois niveaux techniques autour d’une page affichant plusieurs écritures :

1. **HTTP header** : `charset=utf-8`
2. **meta charset** : `<meta charset="utf-8">`
3. **UTF-8** : codage réel du contenu

#### Règle 228

**« Les entêtes envoyés par le serveur contiennent les informations relatives au jeu de caractères employé. »**

#### Règle 232

**« Le code source de chaque page contient une métadonnée qui définit le jeu de caractères. »**

#### Règle 233

**« Le codage de caractères utilisé est UTF-8. »**

#### Vérification

- 228 : le `charset` est présent dans l’en-tête HTTP `Content-Type` et correspond au document.
- 232 : le code source contient une métadonnée de charset pertinente.
- 233 : le contenu est effectivement encodé en UTF-8, sans caractères inattendus ou erronés.

#### Message à retenir

**Déclarer le charset. Utiliser réellement UTF-8.**

### Discours oral

#### Trois niveaux doivent décrire le même encodage

- L’en-tête HTTP indique au navigateur le jeu de caractères employé et doit correspondre au document servi.
- La métadonnée du code source fournit aussi cette information, notamment pour permettre un affichage hors ligne correct.
- Le contenu est réellement encodé en UTF-8 : une déclaration correcte ne compense pas des caractères enregistrés dans un autre encodage.

##### Impact du non-respect

- Des accents ou d’autres caractères peuvent être remplacés par des signes inattendus.
- Le navigateur et les outils d’indexation peuvent interpréter le document avec un mauvais jeu de caractères.

##### Ce que garantissent les règles

- Le navigateur dispose d’informations cohérentes pour afficher les caractères.
- UTF-8 fournit un codage international qui prévient de nombreux défauts d’affichage et facilite la manipulation des contenus.

#### Conclusion

Un service international reste exploitable lorsque le contexte, la langue, le parcours et les caractères sont tous rendus explicites.
