# Storyboard — Liens & PDF : éviter les clics aveugles et les documents fermés

## Identité

- Statut : `VALIDE_POUR_GENERATION`
- Version : `v004`
- Périmètre et édition Opquast : Référentiel Qualité Numérique V5, 2025–2030 ; rubrique Liens 136–152 ; PDF 240–241 ; règles connexes en annexes.
- Audience et objectif : professionnels du numérique ; comprendre comment la qualité des liens donne de la maîtrise **avant l'action**, puis comment la qualité des PDF prolonge cette maîtrise **après l'action**.
- Nombre de slides principales et annexes : 11 principales + 9 annexes.
- Revue : revue métier guidée par le plugin `@Assistant Opquast` en v003, puis passe finale de cohérence documentaire en v004 ; PASS. Preuves : `qa/review-assistant-opquast-v003.md` et `qa/review-coherence-v004.md`. Mode : revues exécutées dans cette conversation, non assimilées à un second auditeur humain indépendant.
- Correspondance machine : `run.json` ; une seule version active.

## Paramètres de série

- Guide commun : `docs/05-GUIDE-STYLE.md`, pack 2.0.0.
- Header exact : haut gauche `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES` ; haut droit `Opquast` puis `DES SITES MEILLEURS POUR TOUS`.
- Footer principal exact : `RÈGLES OPQUAST · LIENS & PDF`.
- Footer des annexes : `RÈGLES OPQUAST · LIENS & PDF · ANNEXE`.
- Pagination : slides principales `1/11` à `11/11` ; annexes `A1/9` à `A9/9`.
- Badges : petit cartouche de règle sous le titre, aligné à droite, seulement sur les slides de règles. Format `R. 138–141`, `R. 240`, etc. Aucun badge sur l'ouverture, les slides de synthèse et les annexes cartographiques.
- Slogan : `Avant l’action : décider. Après l’action : pouvoir agir.` Visible en slide 1 et slide 11 uniquement.
- Références visuelles réellement disponibles : guide commun de la fabrique ; pas de reprise automatique d'un ancien contenu de série.
- Exceptions au guide : aucune.
- VPTCS : non requis par le brief.
- Pattern oral obligatoire pour les slides multi-règles : traiter chaque règle séparément selon `Règle → Préjudice utilisateur → Ce que garantit la règle → Discours oral → Mémo`, puis seulement formuler la synthèse commune.

## Sources et couverture

### Source fournie

- `sources/opquast-liens-et-pdf-source-utilisateur.md` : synthèse consolidée sur liens, PDF, glossaire, doctrine et angles morts.

### Vérification officielle actuelle

- `sources/verification-opquast-v5-2026-10-04.md` : contrôle du référentiel V5 actuel.
- Point important : la source fournie signale une anomalie historique ; en V5 actuelle, **liens entrants = règle 151**, **validité des liens internes = règle 152**, et la règle 153 appartient à Navigation.
- Vérification complémentaire via `@Assistant Opquast` : le corpus du livre 4e édition (2026), passage de la règle 240, confirme la doctrine selon laquelle, en matière d’accessibilité numérique, HTML est préférable au PDF lorsque cela est possible. Cette doctrine est distinguée des règles officielles.

### Couverture des règles principales

| Règle | Version officielle | Libellé / objet utilisé | Source | Slide(s) | Principale/connexe |
|---|---|---|---|---|---|
| 136 | V5 2025–2030 | Chaque lien possède un intitulé dans le code source. | source utilisateur + vérification officielle | 3 | principale |
| 137 | V5 2025–2030 | Le libellé décrit la fonction ou la nature de la cible. | source utilisateur + vérification officielle | 3 | principale |
| 138–141 | V5 2025–2030 | Cohérence visuelle, soulignement, différenciation, liens visités. | source utilisateur + vérification officielle | 2 | principales |
| 142–143 | V5 2025–2030 | Différencier externe/interne et accès limité. | source utilisateur + vérification officielle | 3 | principales |
| 144–146 | V5 2025–2030 | Logiciel externe, téléphone activable, nouvelle fenêtre annoncée. | vérification officielle + source utilisateur | 4 | principales |
| 147–150 | V5 2025–2030 | Format, taille, langue, nom du fichier. | source utilisateur + vérification officielle | 5, 7 | principales |
| 151 | V5 2025–2030 | Liens entrants non interdits ni restreints. | vérification officielle actuelle | A2 | connexe |
| 152 | V5 2025–2030 | Tous les liens internes sont valides. | source utilisateur + vérification officielle | 6 | principale |
| 240 | V5 2025–2030 | Texte des PDF internes sélectionnable. | fiche officielle + source utilisateur | 8 | principale |
| 241 | V5 2025–2030 | PDF internes dotés d'une structure de titres. | fiche officielle + source utilisateur | 9 | principale |
| 195 | V5 2025–2030 | Styles dédiés à l'impression. | vérification officielle | A5 | connexe |
| 207 | V5 2025–2030 | Type MIME de chaque ressource indiqué par le serveur. | vérification officielle | A5 | connexe |

Les slides 1, 7, 10 et 11 sont des regroupements pédagogiques ou des limites de portée ; elles ne sont pas présentées comme des règles officielles autonomes.

---

## Slide 01 — Un bon lien ne demande pas un clic aveugle

**Rôle narratif** : ouverture.

**Idée principale** : la qualité d'un lien se mesure à la maîtrise qu'il laisse avant l'action ; la qualité du contenu téléchargé prolonge cette maîtrise après l'action.

**Situation** : un utilisateur rencontre des liens, boutons de téléchargement et documents sans savoir immédiatement ce qui va se passer.

**Risque utilisateur** : hésitation, clics inutiles, perte de repères, téléchargement subi, abandon.

**Principe de prévention / garantie recherchée** : rendre l'action compréhensible et prévisible avant de demander un engagement.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : synthèse pédagogique issue du corpus ; aucune règle unique à afficher.

**Exemple de mise en œuvre** : quatre questions mentales : voir, comprendre la destination, anticiper le comportement, disposer des informations pour décider.

**Scène visuelle et relations à restituer** : au centre, un lien comme point de décision ; quatre cartes autour : œil, destination, comportement, décision. Une flèche prolonge vers un PDF pour annoncer la deuxième moitié de la série.

**Textes visibles exacts** :
- Titre : `Un bon lien ne demande pas un clic aveugle`
- Cartes : `Je le vois ?` · `Je sais où il mène ?` · `Je sais ce qu’il va faire ?` · `J’ai assez d’informations pour décider ?`
- Callout : `Avant l’action : décider. Après l’action : pouvoir agir.`
- Footer : `RÈGLES OPQUAST · LIENS & PDF`
- Pagination : `1/11`

**Termes ambigus et sens exclus** : « maîtrise » = capacité à comprendre et décider, pas promesse absolue de contrôle technique.

**Éléments interdits / invariants à préserver** : pas de catalogue de numéros ; pas d'icône de curseur utilisée comme seul indicateur de lien ; pas de phrase prétendant qu'un lien « accessible » suffit à rendre le service accessible.

**Préparation orale** : préjudice = agir sans savoir ; ce que garantit la démarche = réduire la surprise et laisser l'utilisateur décider ; mémo = `Un lien doit parler avant le clic.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-01-clic-aveugle.png`.

**Critères de revue spécifiques** : comprendre en moins d'une lecture complète que la série couvre « avant » et « après » le clic.

---

## Slide 02 — Je le vois ?

**Rôle narratif** : règle / regroupement.

**Idée principale** : un lien doit être repérable comme élément interactif sans enquête au survol.

**Situation** : du texte est cliquable mais visuellement similaire au reste du contenu, ou du texte non cliquable est souligné.

**Risque utilisateur** : liens invisibles, faux signaux d'interaction, clics inutiles, perte de repères dans le parcours déjà consulté.

**Principe de prévention / garantie recherchée** : conventions visuelles stables et lisibles.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : 138, 139, 140, 141 ; référentiel officiel V5 actuel.

**Exemple de mise en œuvre** : un paragraphe où les liens sont clairement différenciés ; le même type de lien garde la même convention ; les liens visités disposent d'un état distinct.

**Scène visuelle et relations à restituer** : comparaison gauche/droite. À gauche, « deviner » avec texte uniforme et faux soulignement ; à droite, système cohérent de liens avec état visité.

**Textes visibles exacts** :
- Titre : `Je le vois ?`
- Badge : `R. 138–141`
- Colonne gauche : `À deviner` · `Texte cliquable invisible` · `Soulignement trompeur`
- Colonne droite : `À reconnaître` · `Même rôle = même convention` · `Lien identifiable sans survol` · `Visité ≠ non visité`
- Callout : `Ne pas obliger l’utilisateur à deviner ce qui est interactif.`
- Footer + pagination `2/11`.

**Termes ambigus et sens exclus** : « sans survol » n'interdit pas les effets de survol ; il interdit d'en dépendre pour découvrir le lien.

**Éléments interdits / invariants à préserver** : ne pas utiliser uniquement la couleur pour expliquer la différence ; montrer aussi forme/soulignement/label.

**Cartographie règle → préjudice → garantie** :

| Règle | Préjudice utilisateur si elle manque | Ce que garantit la règle |
|---|---|---|
| 138 | Une convention comprise sur une page change ailleurs ; l’utilisateur doit réapprendre l’interface. | Les liens de même nature conservent des couleurs, formes et comportements cohérents. |
| 139 | Du texte souligné non activable crée de faux signaux et des clics inutiles. | Le soulignement reste un signal fiable de lien. |
| 140 | L’utilisateur doit balayer ou survoler le contenu pour découvrir ce qui est activable. | Les liens sont repérables dans le contenu sans enquête préalable. |
| 141 | L’utilisateur ne sait plus ce qu’il a déjà consulté. | Le parcours déjà effectué reste perceptible grâce à un état visité distinct. |

**Préparation orale** : traiter 138, 139, 140 et 141 séparément, puis seulement relier les quatre garanties à l’idée commune de repérage. Mémo commun = `Je vois le lien avant de chercher le lien.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-02-je-le-vois.png`.

**Critères de revue spécifiques** : la distinction correcte/incorrecte doit être compréhensible sans dépendre de rouge/vert seuls.

---

## Slide 03 — Je sais où il mène ?

**Rôle narratif** : règle / comparaison.

**Idée principale** : le libellé et les signes associés doivent donner assez de contexte pour comprendre la destination ou la fonction du lien.

**Situation** : une page accumule « Cliquer ici », « En savoir plus » et des liens impossibles à comprendre hors contexte.

**Risque utilisateur** : liste de liens incompréhensible dans un lecteur d'écran, hésitation, mauvaise destination, accès réservé découvert trop tard.

**Principe de prévention / garantie recherchée** : un intitulé exploitable dans le code, un libellé explicite, et des types de destinations annoncés lorsqu'ils changent le parcours.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : 136, 137, 142, 143 ; référentiel officiel V5 actuel.

**Exemple de mise en œuvre** : remplacer `En savoir plus` par `Consulter les tarifs 2026`; ajouter un signal explicite pour une cible externe ou un contenu réservé.

**Scène visuelle et relations à restituer** : trois lignes de liens « avant / après », plus deux badges de cible `Externe` et `Accès réservé`.

**Textes visibles exacts** :
- Titre : `Je sais où il mène ?`
- Badge : `R. 136–137 · 142–143`
- Exemple 1 : `En savoir plus` → `Consulter les tarifs 2026`
- Exemple 2 : `Rapport` → `Télécharger le rapport annuel`
- Labels de cible : `Externe` · `Accès réservé`
- Callout : `Un lien parle de sa destination ou de sa fonction.`
- Footer + pagination `3/11`.

**Termes ambigus et sens exclus** : ne pas affirmer que tout libellé court est mauvais ; le critère est la compréhension dans le contexte pertinent.

**Éléments interdits / invariants à préserver** : pas de marque réelle ; ne pas présenter « title » HTML comme substitut universel à un bon libellé.

**Cartographie règle → préjudice → garantie** :

| Règle | Préjudice utilisateur si elle manque | Ce que garantit la règle |
|---|---|---|
| 136 | Un lien peut devenir vide ou inexploitable dans certaines restitutions du code. | Chaque lien dispose d’un intitulé exploitable dans le code source. |
| 137 | Des libellés tels que « En savoir plus » deviennent incompréhensibles hors contexte, notamment dans une liste de liens. | Le libellé renseigne sur la fonction du lien ou la nature de sa cible. |
| 142 | L’utilisateur quitte le site sans l’avoir anticipé. | La nature interne ou externe de la destination est différenciée. |
| 143 | L’utilisateur découvre seulement après activation qu’un contenu nécessite un accès limité. | Le caractère restreint d’un contenu interne est annoncé avant l’action. |

**Préparation orale** : traiter 136, 137, 142 et 143 séparément, puis conclure sur la prédictibilité de la destination. Mémo commun = `Le lien doit dire où il emmène.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-03-ou-il-mene.png`.

**Critères de revue spécifiques** : les exemples doivent rester lisibles en projection ; pas plus de trois exemples.

---

## Slide 04 — Que va déclencher ce lien ?

**Rôle narratif** : règle / typologie.

**Idée principale** : certains liens ou contenus activables déclenchent autre chose qu’une simple navigation vers une page ; les règles 144, 145 et 146 couvrent trois garanties distinctes qu’il ne faut pas fusionner.

**Situation** : un lien ouvre une messagerie, un numéro de téléphone n’est pas directement activable sur mobile, ou un lien ouvre une nouvelle fenêtre sans avertissement.

**Risque utilisateur** : application externe ou nouvelle fenêtre déclenchée par surprise ; sur mobile, nécessité de recopier manuellement un numéro pour appeler.

**Principe de prévention / garantie recherchée** : pour la règle 144, expliciter l’ouverture d’un logiciel externe ; pour la règle 145, rendre le numéro activable via le protocole approprié ; pour la règle 146, avertir de l’ouverture d’une nouvelle fenêtre.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : 144, 145, 146 ; référentiel officiel V5 actuel.

**Exemple de mise en œuvre** : `Envoyer un e-mail`, numéro de téléphone activable, `Consulter le dossier — nouvelle fenêtre`.

**Scène visuelle et relations à restituer** : trois cartes alignées et explicitement distinctes : enveloppe = logiciel externe ; téléphone = activation directe ; fenêtre = changement de contexte annoncé. Chaque pictogramme est accompagné d’un texte.

**Textes visibles exacts** :
- Titre : `Que va déclencher ce lien ?`
- Badge : `R. 144–146`
- Carte 1 : `Envoyer un e-mail` · `libellé explicite`
- Carte 2 : `Numéro de téléphone` · `activable`
- Carte 3 : `Consulter le dossier` · `nouvelle fenêtre annoncée`
- Callout : `Trois cas, trois garanties : expliciter, activer, avertir.`
- Footer + pagination `4/11`.

**Termes ambigus et sens exclus** : ne pas présenter la règle 145 comme une règle d’avertissement. La règle 146 n’interdit pas en soi une nouvelle fenêtre ; elle porte sur l’avertissement.

**Éléments interdits / invariants à préserver** : ne pas écrire `target=_blank interdit` ; ne pas faire du téléphone une obligation applicable à tout lien numérique.

**Cartographie règle → préjudice → garantie** :

| Règle | Préjudice utilisateur si elle manque | Ce que garantit la règle |
|---|---|---|
| 144 | Une application externe se lance sans que l’utilisateur l’ait compris avant l’activation. | Le libellé rend explicite l’ouverture d’un logiciel externe. |
| 145 | L’utilisateur, notamment sur mobile, doit recopier manuellement un numéro pour appeler. | Le numéro peut être activé directement via le protocole approprié. |
| 146 | Une nouvelle fenêtre ou un nouvel onglet rompt les repères sans avertissement préalable. | L’ouverture d’une nouvelle fenêtre est annoncée avant l’action. |

**Préparation orale** : traiter 144, 145 et 146 séparément, puis seulement formuler la synthèse commune. Mémo = `Expliciter, activer, avertir.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-04-declenchement-lien.png`.

**Critères de revue spécifiques** : les trois règles doivent rester visuellement et oralement distinctes ; ne pas leur attribuer artificiellement le même objectif.

---

## Slide 05 — Télécharger sans surprise

**Rôle narratif** : règle / exemple.

**Idée principale** : avant de lancer un téléchargement, l'utilisateur doit disposer des informations utiles pour décider.

**Situation** : un lien télécharge un fichier lourd, dans une autre langue ou au nom incompréhensible.

**Risque utilisateur** : consommation de données non anticipée, fichier inutilisable, mauvaise langue, fichier impossible à identifier après téléchargement.

**Principe de prévention / garantie recherchée** : annoncer le format, la taille des fichiers internes, la langue lorsqu'elle diffère, et utiliser un nom de fichier identifiable.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : 147, 148, 149, 150 ; référentiel officiel V5 actuel.

**Exemple de mise en œuvre** : `Rapport annuel 2026 — PDF · 2,4 Mo · EN` ; fichier `rapport-annuel-association-2026.pdf`.

**Scène visuelle et relations à restituer** : grande carte de téléchargement avec quatre métadonnées en badges et le nom de fichier affiché en dessous.

**Textes visibles exacts** :
- Titre : `Télécharger sans surprise`
- Badge : `R. 147–150`
- Lien : `Rapport annuel 2026`
- Métadonnées : `PDF` · `2,4 Mo` · `EN` · `Nom explicite`
- Fichier : `rapport-annuel-association-2026.pdf`
- Callout : `Avant de télécharger, je peux décider.`
- Footer + pagination `5/11`.

**Termes ambigus et sens exclus** : la langue est à préciser lorsqu'elle diffère de celle de la page ; la taille visée par la règle 148 concerne les fichiers internes.

**Éléments interdits / invariants à préserver** : pas d'exemple réel contenant des données personnelles ; ne pas transformer le poids en seuil de conformité inventé.

**Cartographie règle → préjudice → garantie** :

| Règle | Préjudice utilisateur si elle manque | Ce que garantit la règle |
|---|---|---|
| 147 | L’utilisateur découvre seulement après activation le type de fichier et peut ne pas disposer de l’outil adapté. | Le format est connu avant le téléchargement. |
| 148 | Un fichier interne volumineux peut consommer du temps ou des données sans que l’utilisateur l’ait anticipé. | La taille du fichier interne est connue avant le téléchargement. |
| 149 | L’utilisateur télécharge un document dans une langue inattendue. | Une différence de langue avec la page d’origine est annoncée. |
| 150 | Une fois téléchargé, le fichier devient difficile à identifier, classer ou retrouver. | Le nom du fichier interne permet d’identifier son contenu et sa provenance. |

**Préparation orale** : traiter 147, 148, 149 et 150 séparément, puis conclure sur la décision avant téléchargement. Mémo commun = `Le téléchargement commence avant le téléchargement.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-05-telecharger-sans-surprise.png`.

**Critères de revue spécifiques** : le poids, format, langue et nom doivent être visuellement associés au même fichier.

---

## Slide 06 — Le lien doit tenir sa promesse

**Rôle narratif** : règle / risque.

**Idée principale** : un lien interne cassé transforme une promesse de navigation en impasse.

**Situation** : une navigation ou un contenu pointe vers une ressource interne supprimée ou déplacée.

**Risque utilisateur** : erreur 404, rupture du parcours, perte de temps et de confiance.

**Principe de prévention / garantie recherchée** : maintenir les liens internes valides.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : règle 152, référentiel officiel V5 actuel.

**Exemple de mise en œuvre** : après déplacement d'une page, mettre à jour les liens internes ou prévoir une redirection adaptée.

**Scène visuelle et relations à restituer** : deux parcours : `Lien → contenu` fluide et `Lien → 404` interrompu ; la branche 404 est illustrée comme impasse, pas comme caricature.

**Textes visibles exacts** :
- Titre : `Le lien doit tenir sa promesse`
- Badge : `R. 152`
- Parcours correct : `Lien interne` → `Contenu disponible`
- Parcours cassé : `Lien interne` → `404`
- Callout : `Un lien interne cassé est une impasse évitable.`
- Footer + pagination `6/11`.

**Termes ambigus et sens exclus** : ne pas étendre la règle 152 aux liens externes ; leur destination dépend d'un tiers.

**Éléments interdits / invariants à préserver** : pas de promesse « zéro 404 sur Internet » ; bien limiter au périmètre interne.

**Préparation orale** : impact = impasse dans un parcours que l'organisation maîtrise ; garantie = continuité des destinations internes ; mémo = `Interne : je maîtrise largement la destination.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-06-lien-promesse.png`.

**Critères de revue spécifiques** : le périmètre « interne » doit être visible.

---

## Slide 07 — Le clic n’est que la moitié du parcours

**Rôle narratif** : transition / synthèse pédagogique.

**Idée principale** : les règles de lien préparent la décision ; les règles PDF déterminent ensuite si le contenu obtenu est réellement exploitable.

**Situation** : un téléchargement peut être parfaitement annoncé et pourtant mener à un document inutilisable.

**Risque utilisateur** : croire l'expérience réussie au moment du clic alors que le contenu reste fermé aux usages nécessaires.

**Principe de prévention / garantie recherchée** : contrôler les deux couches de l'expérience.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : regroupement pédagogique ; 147–150 en amont, 240–241 en aval.

**Exemple de mise en œuvre** : un lien PDF correctement décrit mène à un PDF dont le texte est sélectionnable et la structure navigable.

**Scène visuelle et relations à restituer** : deux moitiés reliées par une flèche : `Avant le clic — qualité du lien` puis `Après le clic — qualité du document`.

**Textes visibles exacts** :
- Titre : `Le clic n’est que la moitié du parcours`
- Colonne gauche : `Avant le clic` · `Identifier` · `Comprendre` · `Décider`
- Colonne droite : `Après le clic` · `Lire` · `Parcourir` · `Manipuler`
- Callout : `Un téléchargement bien annoncé peut encore mener à un document inutilisable.`
- Footer + pagination `7/11`.

**Termes ambigus et sens exclus** : « inutilisable » = inutilisable pour certains usages ou utilisateurs, pas nécessairement impossible à afficher.

**Éléments interdits / invariants à préserver** : aucune nouvelle règle inventée ; marquer clairement la slide comme synthèse.

**Préparation orale** : impact = fausse impression de qualité si on s'arrête au lien ; garantie = penser l'expérience de bout en bout ; mémo = `Le lien ouvre la porte, le document doit rester praticable.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-07-deux-couches.png`.

**Critères de revue spécifiques** : distinction avant/après immédiatement perceptible.

---

## Slide 08 — Un PDF visible peut rester inexploitable

**Rôle narratif** : règle / comparaison.

**Idée principale** : un PDF peut afficher du texte qui n'existe en réalité que sous forme d'image.

**Situation** : document scanné ou exporté comme image, visuellement lisible mais sans vrai texte exploitable.

**Risque utilisateur** : impossibilité ou forte difficulté à sélectionner, copier, rechercher, traduire, indexer et exploiter le texte avec des aides techniques.

**Principe de prévention / garantie recherchée** : fournir du texte réel sélectionnable dans les PDF internes.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : règle 240 ; fiche officielle V5 et source utilisateur.

**Exemple de mise en œuvre** : comparer un scan-image et un document dont le texte peut être sélectionné.

**Scène visuelle et relations à restituer** : comparaison deux colonnes de PDF visuellement proches. À gauche, sélection impossible ; à droite, une phrase est surlignée comme sélection réelle.

**Textes visibles exacts** :
- Titre : `Un PDF visible peut rester inexploitable`
- Badge : `R. 240`
- Colonne gauche : `PDF image` · `Le texte ressemble à du texte`
- Colonne droite : `PDF avec texte réel` · `Le texte est sélectionnable`
- Tests : `Sélectionner` · `Copier` · `Rechercher` · `Traduire`
- Callout : `Voir le texte ne prouve pas qu’il existe comme texte.`
- Footer + pagination `8/11`.

**Termes ambigus et sens exclus** : texte sélectionnable ≠ PDF pleinement accessible.

**Éléments interdits / invariants à préserver** : ne pas affirmer qu'OCR seul garantit la qualité complète ; ne pas représenter une conformité globale.

**Préparation orale** : impact = document visuellement ouvert mais fonctionnellement fermé ; garantie = contenu textuel réellement manipulable ; mémo = `Le premier test : puis-je sélectionner le texte ?`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-08-pdf-texte-reel.png`.

**Critères de revue spécifiques** : la différence doit porter sur l'exploitabilité, pas sur l'esthétique du PDF.

---

## Slide 09 — Un PDF doit aussi se parcourir

**Rôle narratif** : règle / mécanisme de production.

**Idée principale** : du texte réel ne suffit pas ; une structure de titres permet d'entrer dans l'organisation du document.

**Situation** : long PDF composé de paragraphes visuellement titrés mais sans structure de titres exploitable.

**Risque utilisateur** : lecture linéaire imposée, difficulté à comprendre l'organisation et à atteindre une section.

**Principe de prévention / garantie recherchée** : utiliser une hiérarchie de titres dans la source et préserver cette structure dans le PDF.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : règle 241 ; fiche officielle V5.

**Exemple de mise en œuvre** : `Titre 1 → Titre 2 → Titre 3` dans la source, puis `Exporter en PDF balisé/tagué`, puis navigation par sections/signets.

**Scène visuelle et relations à restituer** : flux de gauche à droite : document source avec styles de titres → export balisé → PDF avec panneau de structure.

**Textes visibles exacts** :
- Titre : `Un PDF doit aussi se parcourir`
- Badge : `R. 241`
- Étape 1 : `Source structurée` · `Titre 1 · Titre 2 · Titre 3`
- Étape 2 : `Export balisé / tagué`
- Étape 3 : `PDF structuré` · `Accéder aux sections`
- Callout : `La structure se prépare dans le document source.`
- Footer + pagination `9/11`.

**Termes ambigus et sens exclus** : ne pas dire qu'un sommaire visuel équivaut nécessairement à une structure de titres technique.

**Éléments interdits / invariants à préserver** : pas de logo Word/Adobe réel ; pictogrammes neutres.

**Préparation orale** : impact = document long difficile à parcourir ; garantie = accès plus direct aux sections et meilleure exploitation par aides techniques et outils ; mémo = `Un PDF structuré commence avant l'export.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-09-pdf-structure.png`.

**Critères de revue spécifiques** : la relation source → export → résultat doit être explicite.

---

## Slide 10 — Deux règles ne font pas un PDF pleinement accessible

**Rôle narratif** : limite de portée / vigilance.

**Idée principale** : les règles 240 et 241 sont utiles mais ne couvrent pas à elles seules toutes les dimensions d'accessibilité d'un PDF.

**Situation** : une équipe coche « texte sélectionnable » et « titres » puis conclut à une accessibilité complète.

**Risque utilisateur** : faux sentiment de conformité ; ordre de lecture, images, tableaux ou contrastes peuvent encore créer des obstacles.

**Principe de prévention / garantie recherchée** : présenter précisément ce que les règles couvrent et ce qu'elles ne permettent pas de conclure.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : limites déduites du corpus fourni ; 240 et 241 restent les règles officielles concernées. Les éléments additionnels sont des compléments d'analyse, pas de nouvelles exigences Opquast ajoutées au référentiel.

**Exemple de mise en œuvre** : deux zones : `Opquast vérifie ici` vs `D’autres contrôles peuvent rester nécessaires`.

**Scène visuelle et relations à restituer** : grand cercle central `240 + 241` entouré d'un périmètre plus large en pointillés.

**Textes visibles exacts** :
- Titre : `Deux règles ne font pas un PDF pleinement accessible`
- Zone centrale : `Règles PDF spécifiques 240–241` · `Texte sélectionnable` · `Structure de titres`
- Zone élargie : `D’autres contrôles peuvent rester nécessaires` · `Ordre de lecture` · `Alternatives d’images` · `Tableaux` · `Contrastes`
- Label : `Complément d’analyse — pas une règle Opquast supplémentaire`
- Callout : `Respecter 240 et 241 ne permet pas, à lui seul, de conclure à une accessibilité PDF complète.`
- Footer + pagination `10/11`.

**Termes ambigus et sens exclus** : ne pas citer PDF/UA ou RGAA comme si Opquast les certifiait ; ne pas fixer de critères techniques non sourcés dans cette slide.

**Éléments interdits / invariants à préserver** : aucune mention « conforme RGAA » ou « conforme PDF/UA » ; aucune surpromesse.

**Préparation orale** : impact = éviter de transformer un contrôle partiel en conclusion globale ; garantie = limiter correctement la portée des règles ; mémo = `Deux contrôles utiles, pas un certificat global.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-10-limite-pdf.png`.

**Critères de revue spécifiques** : la distinction officiel/complément doit être visible, pas seulement expliquée à l'oral.

---

## Slide 11 — Une même promesse : garder la maîtrise

**Rôle narratif** : synthèse.

**Idée principale** : liens et PDF racontent le même principe qualité : donner les informations et les moyens nécessaires pour que l'utilisateur maîtrise son parcours.

**Situation** : succession d'actions numériques où la perte de maîtrise peut se produire avant ou après le clic.

**Risque utilisateur** : surprise, impasse, document fermé, abandon.

**Principe de prévention / garantie recherchée** : avant l'action, permettre de décider ; après l'action, fournir un contenu exploitable.

**Règle(s), libellé(s) exact(s), limites utiles et source(s)** : synthèse du corpus, sans nouvelle règle.

**Exemple de mise en œuvre** : deux colonnes reliées : `Avant` et `Après`.

**Scène visuelle et relations à restituer** : balance ou continuité horizontale, sans personnage : lien → décision → document → exploitation.

**Textes visibles exacts** :
- Titre : `Une même promesse : garder la maîtrise`
- Colonne gauche : `Avant l’action` · `Voir` · `Comprendre` · `Anticiper` · `Choisir`
- Colonne droite : `Après l’action` · `Lire` · `Naviguer` · `Manipuler` · `Retrouver`
- Callout principal : `Avant l’action : décider. Après l’action : pouvoir agir.`
- Conclusion courte : `Éviter les clics aveugles et les documents fermés.`
- Footer + pagination `11/11`.

**Termes ambigus et sens exclus** : « pouvoir agir » ne signifie pas que toutes les actions sont possibles ; il s'agit de préserver les usages couverts par les règles et le contexte.

**Éléments interdits / invariants à préserver** : ne pas transformer la synthèse en certification globale du service.

**Préparation orale** : impact = perte de maîtrise à deux moments différents ; garantie = continuité d'usage ; mémo = `Le lien prépare l'action. Le document doit permettre de la poursuivre.`

**Pré-transcription** : `PRETRANSCRIPTION_A_VERIFIER`.

**Fichier final prévu** : `finals/slide-11-maitrise.png`.

**Critères de revue spécifiques** : conclusion mémorisable et symétrie avant/après nette.

---

# Annexes

Les annexes sont volontairement réparties sur **9 écrans**. Aucune annexe ne doit devenir une planche catalogue illisible en projection. Chaque écran limite le nombre de concepts et conserve un message de lecture unique.

## Annexe A1 — Liens : identifier et qualifier la destination

**Rôle narratif** : référence, première moitié de la rubrique Liens.

**Contenu visible prévu** : deux groupes seulement :
- `Identifier et présenter` : règles 136 à 141
- `Qualifier la destination` : règles 142 à 143

Chaque règle apparaît sous forme `numéro + libellé court`, sans objectif développé.

**Message de lecture** : `Avant d’activer un lien, je dois pouvoir l’identifier et comprendre sa destination.`

**Footer** : `RÈGLES OPQUAST · LIENS & PDF · ANNEXE` · `A1/9`.

**Fichier final prévu** : `finals/annexe-a1-liens-136-143.png`.

---

## Annexe A2 — Liens : de l’action à la fiabilité

**Rôle narratif** : référence, seconde moitié de la rubrique Liens.

**Contenu visible prévu** : trois groupes courts :
- `Déclencher ou changer de contexte` : 144 à 146
- `Informer avant téléchargement` : 147 à 150
- `Écosystème et validité` : 151 à 152

**Point documentaire obligatoire** : `151 = liens entrants` ; `152 = liens internes valides`.

**Message de lecture** : `Le lien doit rester prévisible jusqu’à l’action et fiable dans la durée.`

**Footer** : `... · ANNEXE` · `A2/9`.

**Fichier final prévu** : `finals/annexe-a2-liens-144-152.png`.

---

## Annexe A3 — Liens transversaux : données, confiance et images

**Rôle narratif** : référence transversale.

**Contenu visible prévu** : quatre règles seulement :
- `25` : politique de communication des referrers
- `28` : données personnelles sensibles absentes des URL
- `64` : lien vers la source d’un label, ordre ou récompense
- `117` : alternative appropriée d’une image-lien

**Limite** : ces règles ne sont pas présentées comme appartenant à la rubrique Liens.

**Footer** : `... · ANNEXE` · `A3/9`.

**Fichier final prévu** : `finals/annexe-a3-liens-transversaux-donnees-images.png`.

---

## Annexe A4 — Liens transversaux : internationalisation

**Rôle narratif** : référence transversale focalisée.

**Contenu visible prévu** :
- `131` : langue cible identifiable lorsqu’elle diffère
- `133` : lien vers la traduction équivalente de la page courante
- `134` : libellé de version rédigé dans la langue cible

**Message de lecture** : `Changer de langue ne doit pas faire perdre la destination ni le contexte.`

**Footer** : `... · ANNEXE` · `A4/9`.

**Fichier final prévu** : `finals/annexe-a4-internationalisation.png`.

---

## Annexe A5 — Liens transversaux : navigation, newsletter et serveur

**Rôle narratif** : référence transversale complémentaire.

**Contenu visible prévu** : six entrées regroupées en trois paires :
- Navigation : `155` retour à l’accueil ; `164` liens d’accès rapide
- Newsletter : `174` lien de désinscription ; `176` désinscription depuis le site
- Diffusion : `195` styles d’impression ; `207` type MIME de chaque ressource

**Limite** : montrer la transversalité, pas prétendre que tous ces sujets ont le lien comme objet principal.

**Footer** : `... · ANNEXE` · `A5/9`.

**Fichier final prévu** : `finals/annexe-a5-navigation-newsletter-serveur.png`.

---

## Annexe A6 — Glossaire : parler précisément des liens

**Rôle narratif** : vocabulaire d’audit.

**Contenu visible prévu** : six cartes maximum :
- `Libellé de lien`
- `Image-lien`
- `Liens de même nature`
- `Liens consécutifs`
- `Lien d’accès rapide`
- `Lien interne / externe / entrant`

Chaque carte tient en une définition d’une ligne issue du glossaire réellement consulté.

**Footer** : `... · ANNEXE` · `A6/9`.

**Fichier final prévu** : `finals/annexe-a6-glossaire-liens.png`.

---

## Annexe A7 — Glossaire : URL et PDF

**Rôle narratif** : vocabulaire technique complémentaire.

**Contenu visible prévu** : quatre cartes :
- `Lien absolu / relatif`
- `PDF`
- `PDF image`
- `PDF interne`

**Message de lecture** : `Deux fichiers qui se ressemblent visuellement peuvent être très différents pour les outils et les utilisateurs.`

**Footer** : `... · ANNEXE` · `A7/9`.

**Fichier final prévu** : `finals/annexe-a7-glossaire-url-pdf.png`.

---

## Annexe A8 — PDF : limites d’un contrôle partiel

**Rôle narratif** : vigilance, première moitié.

**Contenu visible prévu** : trois blocs seulement :
- `Accessibilité au-delà de 240–241` : ordre de lecture, alternatives d’images, tableaux, contrastes
- `Chaîne de production` : la qualité du PDF dépend aussi du document source et de l’export
- `PDF externes` : maîtrise éditoriale plus faible, préjudice utilisateur toujours possible

**Label obligatoire** : `Analyse complémentaire issue du corpus fourni — pas une liste de règles Opquast.`

**Footer** : `... · ANNEXE` · `A8/9`.

**Fichier final prévu** : `finals/annexe-a8-limites-pdf.png`.

---

## Annexe A9 — PDF : choisir le format avant de publier

**Rôle narratif** : vigilance, seconde moitié et clôture des annexes.

**Bandeau doctrinal** : `En matière d’accessibilité numérique, HTML est préférable au PDF lorsque cela est possible.` Source : livre, passage associé à la règle 240. Cette phrase est présentée comme doctrine du livre, jamais comme règle autonome.

**Contenu visible prévu** : quatre cartes :
- `Mobile` : mise en page fixe, zoom et déplacements possibles
- `Volume` : téléchargement potentiellement coûteux pour un besoin court
- `Formulaires PDF` : compatibilité et restitution variables selon lecteurs et conception
- `Métadonnées & versions` : titre interne, noms, obsolescence et archivage

**Question finale** : `Avons-nous réellement besoin d’un PDF ?`

**Footer** : `... · ANNEXE` · `A9/9`.

**Fichier final prévu** : `finals/annexe-a9-choisir-format.png`.

---

## Revue avant génération

### Contrôles effectués

- `bootstrap` : `READY_LOCAL`, aucun dossier créé, travaux existants préservés.
- `doctor` : PASS, pack 2.0.0, 84 fichiers vérifiés, dépendances optionnelles disponibles.
- `resume` du run actif `liens-et-pdf` : `RESUMABLE`, storyboard validé, 20 slides attendues, 0 candidate générée, 0 problème enregistré.
- Source utilisateur présente dans le run et utilisée comme base éditoriale.
- Vérification actuelle du référentiel Opquast V5 conservée pour la numérotation et les règles clés.
- COS appliqué à la source dense pour séparer cœur narratif, annexes et limites.
- Revue métier `@Assistant Opquast` documentée en v003 ; la présente v004 ne change pas le fond métier, elle corrige uniquement la cohérence interne et la traçabilité du storyboard.
- Aucune génération d’image n’est déclarée pour ce run.

### Écarts / décisions

1. **Volume** : la série complète compte 20 slides, mais le parcours à présenter reste de 11 slides principales ; les 9 annexes constituent un bloc de référence optionnel.
2. **Correction de numérotation** : la règle des liens entrants est 151 dans la V5 actuelle ; la validité des liens internes est 152.
3. **Table de couverture** : 151 est rattachée à A2 ; 195 et 207 à A5, conformément au contenu réel des annexes.
4. **Angles morts PDF** : conservés comme analyse complémentaire, jamais comme exigences Opquast supplémentaires.
5. **Règles 240–241** : leur portée est explicitement limitée ; aucune conclusion de conformité PDF globale.
6. **Règle 145** : séparée conceptuellement de l’avertissement de changement de contexte ; son bénéfice propre est l’activation directe du numéro de téléphone.
7. **Doctrine HTML/PDF** : source primaire retrouvée dans le corpus du livre via `@Assistant Opquast` ; point verrouillé comme doctrine, pas comme règle autonome.
8. **Dédensification** : la couverture exhaustive reste répartie sur neuf annexes focalisées afin de préserver la lisibilité ; aucune annexe n’est obligatoire dans le fil oral principal.

### Statut de sortie

Storyboard `VALIDE_POUR_GENERATION`. La v004 est une révision de cohérence de la v003 : aucune règle, aucun message pédagogique central et aucun nombre de slides n’ont été ajoutés ou supprimés. La génération reste séquentielle : une candidate, inspection, décision, puis slide suivante.
