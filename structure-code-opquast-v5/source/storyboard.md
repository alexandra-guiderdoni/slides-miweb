# OPQUAST V5 — STRUCTURE ET CODE | STORYBOARD MAÎTRE — FABRIQUE V2

<!-- PDG-LARGE-FILE-JUSTIFICATION: storyboard maître unique explicitement demandé ; les 38 fiches autonomes répètent les masques complets pour éviter toute interprétation à la fabrication. -->

**Édition de travail :** 8 novembre 2026, révision v003, deux relectures indépendantes traitées.
**Référentiel :** Opquast Qualité Numérique V5, rubrique Structure et code, règles 231 à 245.
**Finalité :** reconnaître, distinguer, vérifier et justifier les quinze règles, en partant des usages des personnes.
**Livrable :** storyboard éditorial et visuel ; aucune image, aucun prompt ImageGen définitif, aucune publication, aucun commit.
**Durée intégrale :** environ 40 minutes ; 40 min 05 s de durées indicatives cumulées, réflexion et correction des exercices comprises.
**Volume :** 38 slides : ouverture et méthode (6), quinze règles dédiées, cinq distinctions, quatre checkpoints, une transversalité, huit questions finales sur deux slides, grand cas et correction, mémo, conclusion, ressources.

## Identité

- Statut : `VALIDE_POUR_GENERATION` ; validation bornée au storyboard, voir « Validation ».
- Version : `v003`, dérivée de v002 ; v001 et v002 conservées sans modification.
- Périmètre : règles 231 à 245 ; règles connexes 69 et 185 seulement, liées par des passages du livre.
- Audience : candidats à la certification Opquast, profils numériques variés, pas seulement développeurs.
- Nombre : 38 slides, aucune annexe.
- Revue : deux relectures indépendantes du 8 novembre 2026, de v001 (9 importants, 14 mineurs), puis de v002 (3 importants, 11 mineurs) ; corrections consignées aux Journaux v002 et v003. Aucune troisième relecture indépendante revendiquée.
- Correspondance machine : `run.json` pointe uniquement vers v003, statut `VALIDE_POUR_GENERATION`, avec SHA-256 du fichier final et référence de la seconde relecture.
- Pourquoi : le brief fait foi. Même qualité de scènes incarnées que Présentation ; les situations techniques doivent devenir des usages concrets. Aucun paquet pourquoi spécifique à cette série trouvé par recherche ciblée. La fiche `wiki/raw/why/inbox/2026-06-28-slides-ia-qa-reprise-ciblee.md`, lue historiquement en v001 comme contexte non promu, documente le risque de mélange conceptuel et de texte parasite ; elle ne remplace pas le brief.

## Changements depuis v001

Historique v002, conservé pour traçabilité ; le Journal v003 et la section Validation font foi pour la révision active. Les 23 constats de la première relecture sont traités ; aucun n’est écarté. La v001 reste intacte. Le Journal v002 donne les décisions et les emplacements. Les huit questions finales sont nouvelles ; le grand cas conserve sept défauts indépendants, sans relevé qui désigne une réponse. S19 et S20 sont permutées. Les trois ajouts autorisés aux blocs de Théo, Inès et Odette sont les seuls écarts aux blocs de Présentation.

## Paramètres de série

- Guide commun : `docs/05-GUIDE-STYLE.md`, version 2.0.0, avec les exceptions ci-dessous.
- En-tête exact : haut gauche `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES` ; haut droit `Opquast` puis `DES SITES MEILLEURS POUR TOUS`.
- Footer exact : `RÈGLES OPQUAST · STRUCTURE ET CODE`, point médian U+00B7 ; aucune annexe.
- Pagination : `NN / 38`, bas droit, résolue à la fabrication (par exemple `07 / 38`).
- Badges : seulement les quinze slides de règle et les cinq distinctions, sous le titre, alignés à droite, formats `R. 231` ou `R. 240 · 241` ; aucun badge sur les exercices, la transversalité ou la correction.
- Slogan original de cette série : `Le contenu se lit, se parcourt, se réutilise`, seulement S01 et S37.
- Navigation : ni pastilles de progression, ni fil d’Ariane, ni barre segmentée ; le plan, les sous-titres d’acte et les titres suffisent.
- Tirets : tiret simple dans les textes visibles et oraux ; guillemets français et apostrophes typographiques hors code ; guillemets droits dans le code.
- Format : 16:9, exactement 1672 × 941 px.
- Densité : au plus 160 caractères pour la somme des chaînes de Texte visible, titre compris ; seuls en-tête, footer, badge et pagination sont exclus. Encadrés : au plus 70 caractères, exactement un encadré pour chaque ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE.
- Encadrés : les mots `IMPACT`, `GARANTIE`, `CONTRÔLE`, `LIMITE` restent en bleu marine, comme le reste du texte. Les couleurs sémantiques portent sur les fonds et icônes.
- Test des trois secondes : cible de compréhension, appréciation `reasoned` du rédacteur ; aucun test humain chronométré effectué.
- Alternatives : propositions de storyboard, pas transcriptions finales de PNG. Tout futur accordéon descriptif reste `PRETRANSCRIPTION_A_VERIFIER` tant que les images finales ne sont pas inspectées.

### Références de composition et ancres

Images de Présentation examinées lors de la rédaction v001, d’après la trace conservée ; les neuf comparateurs Pnn ont aussi été réexaminés en v003, dans `/Users/alex/Claude/projets-heberges/slides-miweb/presentation-opquast-v5/assets/slides/` :

- `P01` = `slide-01.png` : ouverture, personnage en situation, grand titre et slogan.
- `P06` = `slide-06.png` : Samuel au bureau, objets concrets et gestes de vérification.
- `P13` = `slide-13.png` : Malik et Nora, contexte de vie, deux encadrés, titre à gauche.
- `P18` = `slide-18.png` : checkpoint, question en bandeau, cartes, personnage qui réfléchit.
- `P19` = `slide-19.png` : action physique de Nora, effet agrandi sur l’interface.
- `P26` = `slide-26.png` : règle avec code, scène d’Inès, comparaison lisible.
- `P30` = `slide-30.png` : Odette agit sur un document, deux objets comparés.
- `P37` = `slide-37.png` : grand cas sans personnage, colonne d’annotations dégagée.
- `P39` = `slide-39.png` : conclusion, même contenu utilisé par plusieurs personnes.

Ancres de personnages déjà validées, préservées depuis Présentation. Base absolue : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/fabrique-slides/runs/presentation-opquast-v5/finals/` :

- `A-NORA` (Nora) = `runs/presentation-opquast-v5/finals/slide-01-ouverture.png`.
- `A-SAMUEL` (Samuel) = `runs/presentation-opquast-v5/finals/slide-06-methode.png`.
- `A-MALIK` (Malik) = `runs/presentation-opquast-v5/finals/slide-13-forme-position.png`.
- `A-THEO` (Théo) = `runs/presentation-opquast-v5/finals/slide-08-couleur-seule.png`.
- `A-INES` (Inès) = `runs/presentation-opquast-v5/finals/slide-26-texte-justifie.png`.
- `A-ODETTE` (Odette) = `runs/presentation-opquast-v5/finals/slide-30-styles-impression.png`.

Les alias A-THEO et A-INES ne créent pas de nouvelles images : ils nomment les apparitions validées indiquées dans la mission. A-ODETTE conserve son nom fourni. Chaque fiche nomme l’ancre de chaque personne effectivement illustrée ; seuls les trois ajouts déclarés ci-dessous modifient les blocs de personnages.

Références de composition autorisées, issues du contrat Présentation ; inspection historique v001 conservée :

- `N01`, `N03`, `N10`, `N17` = `/Users/alex/Claude/projets-heberges/slides-miweb/navigation-opquast-v5-360/assets/slides/slide-NN.png`, avec NN respectivement 01, 03, 10, 17.
- `S20` = `/Users/alex/Claude/projets-heberges/slides-miweb/securite-opquast-v5-v4/source/etalons/slide-20.png`.
- N01 : écran central ; N03 : deux panneaux ; N10 : personne et interface agrandie ; N17 : cartes alignées ; S20 : deux fenêtres détaillées. Ces images transmettent la composition et le style ; aucun personnage étranger à la fiche ne doit être reproduit. Les Pnn restent des comparateurs de qualité, pas des compositions envoyées par défaut. P37 fixe la richesse attendue du grand cas.

### Bloc style (à répéter mot pour mot dans chaque prompt)

> Slide de formation institutionnelle française, format paysage 16:9, exactement 1672 × 941 pixels. Fond ivoire presque blanc, structure et titres bleu marine, panneaux pastel arrondis aux aplats doux. Couleurs à sens fixe : corail pour l’impact sur l’utilisateur, vert pour la garantie, bleu clair pour le contrôle, orange pour la limite ; chaque encadré porte aussi son mot et son icône, la couleur n’est jamais le seul repère. Illustration vectorielle plate aux traits fins, avec personnage, dans l’esprit des références fournies. Feuillages vectoriels discrets, très pâles, seulement en bordure de la slide, jamais sous un texte. Typographie sans sérif proche de Marianne, casse de phrase pour le titre. Aucun dégradé, aucune photographie, aucune 3D, aucune ombre lourde, aucun faux logo, aucun texte en dehors de la liste fournie : toute zone d’interface sans texte prévu est composée de lignes et de blocs abstraits, sans lettres ni chiffres. Chaque texte de la liste apparaît une seule fois. Ne reprendre ni l’en-tête, ni le footer, ni la numérotation des images de référence.

### Les quatre masques (chacun à répéter mot pour mot dans les prompts des fiches qui le citent)

Reprise mot pour mot de Présentation, seuls le footer et le total changent. La partie commune est incluse dans chaque masque ; aucune zone vide ne doit être ajoutée par habitude.

- `MASQUE RÈGLE` : S07-S09, S12-S14, S17-S18, S20, S22-S23, S25-S28.
- `MASQUE COMPARAISON` : S10, S15, S19, S24, S29.
- `MASQUE EXERCICE` : S11, S16, S21, S30, S32-S35.
- `MASQUE LIBRE` : S01-S06, S31, S36-S38.

- `MASQUE RÈGLE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

- `MASQUE COMPARAISON` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

- `MASQUE EXERCICE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

- `MASQUE LIBRE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

### Bloc personnage (à répéter mot pour mot dans chaque prompt où Nora apparaît)

> Nora, femme d’une trentaine d’années, cheveux bleu nuit très foncé, mi-longs, s’arrêtant aux épaules, raie sur le côté, peau claire, pull à col rond bleu vif uni, pantalon bleu marine, baskets blanches, sans lunettes. Expression attentive et calme, léger sourire quand la situation se résout. Même style de dessin et même apparence que le personnage féminin des références `N10` et `S20`, en illustration vectorielle plate aux traits fins, sans contour noir épais. Si l’ancre `A-NORA` est fournie, Nora reproduit exactement le personnage de cette image. Nora garde la même apparence d’une slide à l’autre.

### Personnages ponctuels (à répéter mot pour mot dans les prompts concernés)

Écart autorisé en v002 (I7) : seule la phrase de reproduction exacte est ajoutée aux blocs de Théo, Inès et Odette, avant leur phrase finale. Les blocs de Nora, Samuel et Malik restent mot pour mot ceux de Présentation. « Leurs personnages » désigne les autres références de composition ; l’image d’ancre fournie fait foi pour l’apparence. Chaque bloc se termine par la même phrase : « Reprendre le style de dessin des références, pas l’apparence de leurs personnages. »

- **Samuel**, intégrateur de la Maison des Lisières : homme d’une quarantaine d’années, cheveux courts poivre et sel, barbe courte, chemise bleu ciel aux manches retroussées, pantalon gris anthracite. Si l’ancre `A-SAMUEL` est fournie, il la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Malik**, utilisateur de lecteur d’écran : homme d’une cinquantaine d’années, crâne rasé, peau brune, casque audio gris clair, pull vert sauge, assis droit devant un ordinateur portable, mains sur le clavier, expression concentrée et sereine ; aucun attribut caricatural (ni lunettes noires, ni canne au premier plan, ni geste de tâtonnement). Si l’ancre `A-MALIK` est fournie, il la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Théo**, participant qui distingue mal le rouge du vert : jeune homme d’une vingtaine d’années, cheveux châtains en bataille, sweat gris clair, tablette en main ; rien dans son apparence ne signale le daltonisme. Si son image de référence est fournie, il la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Inès**, lectrice dyslexique : adolescente d’environ quinze ans, longs cheveux noirs attachés en queue-de-cheval, gilet lavande, à l’aise et concentrée ; rien dans son apparence ne signale la dyslexie. Si son image de référence est fournie, elle la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Odette**, voisine de Nora, qui aime annoter le programme sur papier : femme d’environ soixante-quinze ans, cheveux blancs courts, cardigan beige, un crayon à la main, assise bien droite, alerte. Si son image de référence est fournie, elle la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.

### Critères de rejet communs (à reprendre dans chaque prompt)

- Texte manquant, ajouté, déformé ou répété ; faute d’apostrophe, de guillemet, d’accent ou de tiret.
- Cadre, carte, bandeau ou encadré vide, ou portant un texte hors liste.
- En-tête, footer, pagination ou badge inexacts ; reprise de l’en-tête, du footer ou de la numérotation d’une référence.
- Faux logo, URL, adresse ou numéro lisibles hors liste.
- Personnage différent de son bloc ou de son ancre ; représentation caricaturale d’une personne en situation de handicap ou âgée.
- Pour les slides à code : toute différence, caractère par caractère, avec la ligne de code de la liste.

## Exceptions au guide et justification

- **Feuillages en bordure** : reprise demandée de l’exception Présentation, vectoriels très pâles, sans passer sous le texte.
- **Fond ivoire presque blanc** : continuité de teinte avec la référence validée.
- **Titre à gauche hors MASQUE LIBRE** : stabilité des trois masques de contenu ; titre centré conservé en LIBRE.
- **Corail pour l’impact** : rouge adouci, toujours réservé au préjudice ; les mots des encadrés restent bleu marine.
- **Code visible** : S07 (time sur trois lignes), S08 (meta), S13 (liste sur deux lignes), S26 (caption), S34 et S35 (mêmes fragments p et meta refresh, propriétés id en vue source). Chaque extrait est syntaxiquement valide dans le contexte nommé ; il peut illustrer un défaut sémantique, jamais une syntaxe tronquée. Aucun autre code visible. Les mentions h1 puis h3, id dupliqué ou caption absent sont des constats en langage courant, pas des extraits.
- **Grand cas sans personnage, S34 et S35** : seule exception à la scène incarnée, pour garder lisibles la page, son PDF, sept observations et leurs repères.
- **Grand cas, observations brutes** : deux extraits HTML valides, propriétés id de deux éléments de la même page, plan h1 puis h3, ancien contenu collé, texte tabulaire dans pre et balises P du PDF. Chaque défaut repose sur un état présent. Aucune légende de diagnostic avant correction, aucun panneau vide, aucune vignette avant/après.
- **Propriétés répétées nécessaires** : les deux propriétés de source `id=a` et `id="a"` décrivent la même valeur sur deux éléments distincts ; ce sont des relevés d’attributs dans leur contexte, pas deux fragments HTML autonomes. La balise PDF `P` ne paraît qu’une fois, sur une branche regroupant tous les paragraphes, titres visuels compris. Les étiquettes de S35 relient le mot et le numéro par une espace, sans flèche typographique, pour tenir 160 caractères. Aucune exception de densité.

## Contrat de fabrication

- **Storyboard-first :** v003 verrouillée après traitement des deux relectures indépendantes et validation sur mandat d’autonomie ; les futurs prompts et images restent une étape distincte. Cette mission s’arrête au storyboard, au manifeste, aux contrôles et à leur copie vérifiée.
- **Séparation :** Texte visible constitue une liste blanche ; Discours oral, contrôles, corrigés cachés et métadonnées ne sont pas projetés. Exception unique : S35 porte la correction du grand cas.
- **Une scène par slide :** un personnage agit avec un objet dans un lieu ; pas de schéma de code autonome, ni de gabarit vide. Seules S34 et S35 sont sans personnage. Une comparaison peut montrer deux états d’un même usage ; les exercices emploient les cartes du masque avec un personnage qui travaille.
- **Données fictives :** Maison des Lisières, situations et relevés originaux ; aucune personne, marque, adresse, téléphone ou URL réels dans les scènes. Les ressources réelles restent nommées dans le document.
- **Règle → préjudice → garantie :** les numéros restent au badge, aux métadonnées et aux corrigés ; aucun numéro de règle à prononcer dans le discours oral.
- **Exercices originaux :** quatre checkpoints, huit questions finales et un grand cas. Questions ouvertes : aucune paire de règles ni choix binaire annoncé avant réponse. Les distracteurs restent dans les corrigés cachés. Chaque item donne le fait qui permet de conclure ; les précisions de contexte n’ajoutent pas après coup le défaut manquant. Pour les tableaux, S30 demande le contrôle spécifique du défaut constaté : relations (242), présence du titre (243), ordre (244), simulation (245). Cette priorité pédagogique est déclarée et ne nie pas les recoupements du contrôle général de 245. L’évaluation emploie des faits nouveaux (format erroné, appel du menu au clavier sur un article, portée inversée, titre non pertinent, ordre de fiches, PDF à corps scanné mais titres structurés, valeur vide, entête contraire à un contenu UTF-8), sans reprendre les constats des checkpoints.
- **Sources :** livre, quatrième édition 2026, partie 3, rubrique 14, pour le contenu ; libellés 231-245 de l’instantané fourni ; MCP pour les deux libellés connexes ; glossaire local fourni. Ne pas substituer une intuition technique au livre. Les cas et regroupements sont pédagogiques, pas officiels.
- **Portée :** ni obligation légale nationale, ni verdict global d’accessibilité, ni promesse de classement ou de réussite à l’examen.
- **Futurs prompts :** reprise mot pour mot du Bloc style, du masque, des blocs de personnages présents, de la fiche PDS, de la liste blanche et des critères de rejet. Aucun prompt définitif n’est produit ici.
- **Liste blanche fournie lors de la future génération :** en-tête complet, badge résolu s’il existe, chaînes de Texte visible, footer exact, pagination résolue ; la mesure de densité n’inclut que Texte visible. Chaque chaîne une seule fois ; un mot contenu dans une ligne de code ne doit pas être dupliqué ailleurs par improvisation.
- **Références fournies à chaque génération :** au plus cinq images distinctes : étalon du masque, composition principale, ancres de tous les personnages présents, puis N10, N17, N03 et N01 dans les places restantes. Avant validation, S20 occupe la place d’étalon. La composition principale de chaque fiche est choisie parmi N01, N03, N10, N17 ou S20 ; aucune Pnn de personnage n’est utilisée à ce titre. Le PNG E35 est l’image à éditer pour S34, pas une composition supplémentaire. Dédupliquer les chemins résolus, puis les pixels décodés (dimensions et pixels), car des fichiers différents peuvent contenir la même image ; une image identique compte une seule fois, même si elle remplit plusieurs rôles. Compléter seulement avec une référence encore absente. Rejeter tout jeu dépassant cinq images ou perdant une ancre ; ne jamais reprendre un personnage de composition ni de l’étalon à la place de celui décrit. S37 : E01 + N01 + les trois ancres, cinq places au plus ; aucun complément Nnn. Inspection des références effectivement envoyées à renouveler à la production.
- **Après validation :** E01 pour LIBRE, E17 pour les règles sans code et les distinctions, E08 pour les règles avec code, E16 pour checkpoints et évaluations, E35 pour le grand cas. E01 devient l’ancre de série ; elle ne remplace pas A-NORA, ancre du personnage reprise de Présentation. Exception S34 : édition du PNG E35.
- **Oral :** titres de contenu, puces prononçables, impact et garantie sur les règles, transition de sens ; aucune gestion de groupe ni commentaire de fabrication dans le discours. Les consignes d’animation restent dans Contrôle et pièges.

## Fabrication du grand cas (S34 et S35)

- **Correction d’abord :** S35 est le cinquième étalon et la première image à générer lors de la future production. Elle annote les défauts sans réparer la page. P37 reste le comparateur de richesse et de lisibilité.
- **Scène commune :** une seule consultation sans personnage : site 52 %, colonne de correction 21 %, PDF 27 %. Les sept états présents sont le plan h1 puis h3, le paragraphe à puces, l’ancien motif collé à la place du texte sélectionné, les deux mêmes id dans la page, la meta refresh, les horaires textuels alignés par pipes dans pre et le regroupement des titres visuels PDF sous P. Aucun avant/après, aucune horloge, aucun volet vide. L’Illustration de S34 contient la scène commune à recopier, mesurée séparément des instructions propres aux repères.
- **Assemblage sans contradiction :** pour S35, reprendre seulement la scène commune, puis ses ajouts S35. Pour S34, reprendre la scène commune, puis l’interdiction des repères. Ne jamais injecter simultanément les consignes de retrait et d’ajout.
- **S34 dérivée par édition :** retirer les sept pastilles, sept traits et sept étiquettes du PNG S35 validé ; remplacer Correction par Grand cas : trouvez sept défauts et 35 / 38 par 34 / 38. Conserver tous les objets, propriétés, sélections, motifs et textes de la scène commune.
- **Indépendance :** sept objets de contrôle, sept règles : 234, 235, 237, 236, 239, 245 et 241. L’identifiant concerne deux blocs éditoriaux, jamais un champ de formulaire. Le menu, désormais en S32 Q2, n’est pas testé ici. Le collage reprend un ancien dessin et non une chaîne de texte déformée : aucun diagnostic d’encodage. Le PDF comporte de vrais mots sélectionnables, exclusivement regroupés sous des balises de paragraphe ; aucun scan. La grille est du texte HTML sélectionnable, pas une image : le défaut de Présentation sur l’image de texte ne s’applique pas. Réparer un objet ne répare pas les autres.
- **Acceptation :** chaque défaut doit avoir son signe positif lisible : saut de niveaux, p avec puces, grand motif collé distinct, même valeur id sur deux éléments, meta, pipes et pre, P rattaché aux titres PDF. Refuser toute preuve fondée seulement sur une absence. Comparer les deux PNG côte à côte en pleine résolution ; même scène, mêmes positions, mêmes chaînes. Aucun diagnostic résiduel en S34. Deux extraits HTML exacts ; les propriétés id sont des relevés de la vue source, pre et P des noms de nœuds d’inspection. Avant acceptation de l’étalon, faire chercher les sept défauts sur la scène nue à une personne ignorant le corrigé ; sinon rejet. Ce test humain n’a pas été exécuté pendant la rédaction.
- **Repli :** si l’édition n’est pas disponible ou si deux éditions ne conservent pas la scène, régénérer S34 avec E35 comme référence en rejetant les repères résiduels. Après trois échecs du résultat, arrêter et soumettre une bifurcation. Repli inverse possible : scène nue validée, puis correction. Aucun assemblage ni ajout de texte par script.
- **Limites :** scénario fictif, aucun audit réel. Dates, déclarations et codage effectif, menu contextuel, associations et titre d’un vrai tableau, ordre d’un tableau de mise en page et accessibilité globale ne sont pas établis. Les défauts de 242 et 243 ne s’ajoutent pas à une simulation sans cellules HTML.

## Arc pédagogique

- Acte 0, S01-S06 : situation, contrat, plan, fil rouge, glossaire, méthode.
- Acte 1, S07-S11 : caractères et dates (231-233), déclaration et codage effectif, checkpoint 1.
- Acte 2, S12-S16 : structure du contenu (234-236), titres et listes, checkpoint 2.
- Acte 3, S17-S21 : garder la main (237-239), copie et menu, checkpoint 3.
- Acte 4, S22-S24 : PDF (240-241), texte manipulable et titres balisés.
- Acte 5, S25-S30 : tableaux (242-245), cellules/entêtes et titre, mise en page et simulation, checkpoint 4.
- Acte 6, S31-S38 : liens avec deux rubriques, évaluation, grand cas et correction, mémo, conclusion, ressources.

Ce découpage en actes est un **regroupement pédagogique original construit à partir du livre**, pas une organisation officielle de la checklist.

## Sources et couverture

Tableau au format de Présentation, expressément demandé pour cette mission. Libellés exacts conservés depuis le fichier fourni, apostrophes comprises.

| Règle | Libellé exact (checklist V5, instantané MCP fourni) | Slide dédiée | Exercice corrigé |
|---|---|---|---|
| 231 | La date de publication ou de mise à jour des contenus est mise à disposition sous forme programmatique. | S07 | S11 A, S32 Q1 |
| 232 | Le code source de chaque page contient une métadonnée qui définit le jeu de caractères. | S08 | S11 B, S33 Q7 |
| 233 | Le codage de caractères utilisé est UTF-8. | S09 | S11 C, S33 Q8 |
| 234 | Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. | S12 | S16 A, S35 repère 1 |
| 235 | Les éléments visuellement présentés sous forme de liste sont balisés de façon appropriée dans le code source. | S13 | S16 B, S35 repère 2 |
| 236 | Chaque identifiant HTML n'est utilisé qu'une seule fois par page. | S14 | S16 C, S35 repère 4 |
| 237 | La copie du contenu n'est pas bloquée. | S17 | S21 A, S35 repère 3 |
| 238 | L'accès au menu contextuel n'est pas bloqué. | S18 | S21 B, S32 Q2 |
| 239 | Aucune redirection ou rafraîchissement automatique côté client n'est imposée. | S20 | S21 C, S35 repère 5 |
| 240 | Le texte des documents PDF internes est sélectionnable. | S22 | S33 Q6 |
| 241 | Les documents PDF internes sont dotés d'une structure de titres. | S23 | S35 repère 7 |
| 242 | Les cellules des tableaux de données sont reliées à leurs entêtes. | S25 | S30 A, S32 Q3 |
| 243 | Les titres des tableaux de données sont renseignés. | S26 | S30 B, S32 Q4 |
| 244 | La linéarisation des tableaux utilisés pour la mise en page ne nuit pas à la compréhension des contenus. | S27 | S30 C, S33 Q5 |
| 245 | Les tableaux de données ne sont pas simulés. | S28 | S30 D, S35 repère 6 |

Règles connexes, libellés exacts obtenus avec `opquast_get_rule`, `version=qualite-numerique`, le 8 novembre 2026 : `isError=false`, `source=local`, instantané `2026-09-03`, repli HTTP 403, clé API absente. Aucun accès à l’API actuelle n’est revendiqué.

| Règle | Libellé exact | Lien établi par le livre | Slide |
|---|---|---|---|
| 69 | Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. | 236, avis de l’expert : les identifiants servent à associer chaque champ à son étiquette. | S14, S31 |
| 185 | Un contenu qui doit être restitué dans un lecteur d'écran ne lui est pas dissimulé. | 243, contrôle : un caption masqué doit rester accessible aux lecteurs d’écran. | S26, S31 |

Ces liens sont des rapprochements pédagogiques bornés par les passages cités ; ils ne créent pas une double non-conformité automatique. Les recoupements des tableaux sont explicités par la question de contrôle spécifique de S30, sans choix binaire annoncé.

### Inventaire de sources et périmètre de preuve

- **Livre, fait foi :** `sources/opquast/livre-rubrique-14-structure-code.md`, lu en entier, objectifs, solutions, contrôles et avis des quinze règles.
- **Libellés :** `sources/opquast/libelles-231-245-2026-11-08.md`, lu ; provenance locale décrite dans ce fichier, pas une récupération MCP refaite pour les quinze règles.
- **Glossaire :** `sources/opquast/glossaire-structure-code-2026-11-08.md`, lu, copie datée du corpus de juin 2026. Six notions utilisées en S05 ; source statique/générée et tableaux précisent aussi les contrôles.
- **Contrats et modèle :** brief, AGENTS de la Fabrique et du projet Opquast, guide, workflow, prompt accordéons, storyboard Présentation v003 et ses deux relectures lus. Les extraits techniques du contrat des notes orales ont été lus ; pas de révision de slides.json.
- **Images :** neuf Pnn demandées réexaminées en v003 avec l’outil de lecture ; P08 pour Théo, N01, N03, N10, N17 et S20 inspectées historiquement en v001. Aucune nouvelle génération en v003. Les copies d’ancre sont comparées par pixels ; leur inspection n’est pas une nouvelle validation de série.
- **Complément technique :** spécification HTML WHATWG pour les fragments affichés, dont meta refresh et attributs non cités ; syntaxe seulement, sans changer la portée du livre.
- **Hors périmètre :** production des PNG, prompts définitifs, transcriptions finales, générateur web, contrôle réel d’un site, accessibilité des PDF produits, publication et commit.

## Storyboard détaillé

### S01 — Structure et code selon Opquast V5

- **Acte :** 0. Entrer dans l’histoire
- **Type :** ouverture
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Faire ressentir que le même programme peut être visible sans être utilisable par les outils de la personne.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Ouvrir sur un usage empêché.
- Idée principale : Une page doit livrer du contenu exploitable, au-delà de son apparence.
- Scène : qui, Nora ; où, à la table de la bibliothèque de la Maison des Lisières ; objet, le programme PDF sur son portable et un carnet de citations ; tension, elle veut reprendre une phrase mais ne peut sélectionner que la page entière ; action, elle fait glisser la souris sur une ligne ; résultat, un rectangle entoure toute la page-image, pas les mots.
- Transformation visible : Le geste de sélection attrape une image entière au lieu des mots.
- Test des trois secondes : « Elle voit le programme, mais ne peut en reprendre une phrase. »
- Ajout par rapport à la slide précédente : Première scène ; la conclusion reprendra ce geste en situation de réussite.

**Référence de composition principale :** `N01`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Structure et code selon Opquast V5`
- `Le contenu se lit, se parcourt, se réutilise`
- `15 règles · 231 à 245`

**Illustration :** Nora est assise à gauche, une main sur la souris, son carnet ouvert à droite du portable. Une grande vue du PDF occupe la droite : lignes abstraites prises dans un unique rectangle de sélection à poignées, sans surlignage de mots. Une ligne pointillée s’interrompt entre l’écran et le carnet. Façade culturelle suggérée derrière une fenêtre, sans enseigne. Slogan sous le titre, compteur dans un cartouche bas. Aucun code.

**Alternative textuelle à fournir :** Nora essaie de sélectionner une phrase du programme PDF ; une seule image est sélectionnée, et son carnet reste sans citation.

**Règle → préjudice utilisateur :** Situation illustrative de la règle 240 : voir une page scannée ne donne pas accès à un texte manipulable.

**Garantie recherchée (matière de l’oral)**

Un contenu utilisable par les outils de consultation et de réutilisation ; ce seul geste ne prouve pas toute son accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Ne pas dessiner de mots surlignés : ce serait l’inverse du défaut annoncé.
- Le titre PDF n’est pas un diagnostic sur sa structure ; celle-ci sera vérifiée séparément.

**Discours oral du présentateur (non projeté)**

#### Voir ne suffit pas

- Le programme est bien à l’écran, mais Nora veut en citer une phrase.
- Dans un PDF composé d’images, les mots ne sont pas du texte manipulable pour les outils de consultation.
- Le livre relie cette difficulté à la copie, à l’indexation et à la lecture par les aides techniques.
- La structure du contenu compte autant que sa présence à l’écran.

#### Transition

- Un défaut se comprend par l’usage qu’il empêche.

**Mémo oral :** Voir un contenu ne suffit pas à pouvoir l’utiliser.

**Fichier final prévu :** `finals/slide-01-ouverture.png`

---

### S02 — Reconnaître, distinguer, vérifier

- **Acte :** 0. Entrer dans l’histoire
- **Type :** objectif
- **Durée indicative :** 0:40
- **Objectif pédagogique :** Fixer les trois compétences visées sans promettre une réussite à l’examen.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Poser le contrat d’apprentissage.
- Idée principale : Partir d’un usage, nommer son mécanisme, apporter une preuve.
- Scène : qui, Nora ; où, à la même table ; objet, le programme, deux fiches de diagnostic et une feuille de contrôle ; tension, deux causes peuvent donner une même gêne ; action, elle observe le document, compare les fiches puis note le geste qui tranchera ; résultat, trois moments reliés, sans réponse d’exercice.
- Transformation visible : De l’observation à une vérification choisie.
- Test des trois secondes : « Observer, comparer, puis vérifier. »
- Ajout par rapport à la slide précédente : Le geste empêché devient une démarche de diagnostic.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Reconnaître, distinguer, vérifier`
- `15 règles · 4 checkpoints · 8 questions · 1 grand cas`

**Illustration :** Trois mini-scènes de Nora à une table continue : elle essaie une sélection dans le PDF ; elle rapproche deux fiches abstraites ; elle écrit un résultat dans son carnet. Les objets restent concrets, pas une rangée de pictogrammes. Compteur dans un bandeau sous la table.

**Alternative textuelle à fournir :** Nora observe un document, compare deux diagnostics et consigne une vérification : trois compétences pour quinze règles.

**Règle → préjudice utilisateur :** Confondre des règles proches peut laisser le problème utilisateur entier.

**Garantie recherchée (matière de l’oral)**

Des choix fondés sur le mécanisme effectivement constaté.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Exercices originaux, sans lien avec des questions officielles d’examen.
- Les distracteurs attendus seront consignés dans les corrigés, selon le format Présentation ; il s’agit de questions ouvertes argumentées, pas de QCM officiels.

**Discours oral du présentateur (non projeté)**

#### Une gêne, plusieurs causes possibles

- Une copie empêchée dans une page et un PDF sans texte ne se corrigent pas de la même façon.
- Un menu contextuel inaccessible ne prouve pas que la commande Copier est bloquée ailleurs.
- Reconnaître la situation puis distinguer les mécanismes permet de choisir un contrôle utile.
- La preuve porte sur ce qui a été effectivement observé.

#### Transition

- Les usages donnent un ordre à ces vérifications.

**Mémo oral :** Un usage, un mécanisme, une preuve.

**Fichier final prévu :** `finals/slide-02-contrat.png`

---

### S03 — Cinq usages, puis l’entraînement

- **Acte :** 0. Entrer dans l’histoire
- **Type :** plan
- **Durée indicative :** 0:40
- **Objectif pédagogique :** Rendre lisibles les regroupements pédagogiques originaux.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Donner la carte du parcours.
- Idée principale : Cinq domaines de situations, puis leur combinaison.
- Scène : qui, Nora ; où, dans un atelier de la Maison des Lisières ; objet, six postes de travail et un carnet de révision ; tension, le vocabulaire technique paraît disparate ; action, Nora déplace son programme d’un poste au suivant ; résultat, un parcours continu de lecture et de réutilisation.
- Transformation visible : Le même programme passe entre six postes.
- Test des trois secondes : « Des caractères aux tableaux, puis aux cas. »
- Ajout par rapport à la slide précédente : Le contrat devient une carte ordonnée.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Cinq usages, puis l’entraînement`
- `1. Caractères et dates`
- `2. Structure du contenu`
- `3. Garder la main`
- `4. Documents PDF`
- `5. Tableaux`
- `6. S’entraîner`

**Illustration :** Une table d’atelier en perspective forme un parcours, Nora y transporte le programme. Six panneaux titrés surplombent six postes : feuille portant une date en barres abstraites ; document à sections ; souris et page ; PDF ouvert ; grille de données ; carnet où Nora écrit. Chaque poste représente un objet utilisé, pas un symbole de code isolé. Pas de barre de progression ajoutée.

**Alternative textuelle à fournir :** Parcours : caractères et dates, structure du contenu, garder la main, documents PDF, tableaux, puis entraînement.

**Règle → préjudice utilisateur :** Une liste de règles sans logique rend les distinctions difficiles à mémoriser.

**Garantie recherchée (matière de l’oral)**

Retrouver chaque règle par le besoin auquel elle répond.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Regroupement pédagogique original construit à partir du livre ; aucune de ces catégories d’acte n’est une catégorie officielle Opquast.

**Discours oral du présentateur (non projeté)**

#### Des outils au service de cinq usages

- Les caractères et la date doivent être interprétables par les outils.
- Les titres, les listes et les identifiants organisent le contenu et ses relations.
- Copier, ouvrir un menu et lire à son rythme supposent de garder la main.
- Les PDF et les tableaux doivent transmettre leur texte et leur organisation.
- Ces usages se combinent dans une même consultation.

#### Transition

- Un lieu et son site permettent de suivre ces usages ensemble.

**Mémo oral :** Lire, se repérer, agir, réutiliser.

**Fichier final prévu :** `finals/slide-03-plan.png`

---

### S04 — La Maison des Lisières continue

- **Acte :** 0. Entrer dans l’histoire
- **Type :** fil rouge
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Réinstaller les personnages et le lieu sans changer leur identité.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Ancrer les nouvelles situations dans le fil rouge validé.
- Idée principale : Le programme du lieu culturel circule entre des personnes et des outils différents.
- Scène : qui, Nora et Samuel ; où, à l’accueil de la Maison des Lisières ; objet, la page Programme et son PDF ; tension, publier ne suffit pas à tous les usages ; action, Nora montre le document à Samuel qui ouvre la page source ; résultat, deux supports d’un même contenu posés sur le comptoir.
- Transformation visible : Du programme publié à ses usages et à son code.
- Test des trois secondes : « Le même programme, sur le site et en PDF. »
- Ajout par rapport à la slide précédente : Le parcours acquiert son terrain commun.

**Référence de composition principale :** `N01`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora), `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `La Maison des Lisières continue`
- `Un lieu culturel fictif et son site`
- `Programme`
- `PDF interne`
- `Horaires`

**Illustration :** Nora debout à gauche montre son portable à Samuel derrière le comptoir. À droite, une vue de page titrée Programme, un document détaché titré PDF interne et une grille titrée Horaires. Trois objets au plus, lignes abstraites, sans autre texte ni coordonnées.

**Alternative textuelle à fournir :** Nora et Samuel examinent le programme du site, son PDF interne et ses horaires, dans le lieu culturel fictif de la Maison des Lisières.

**Règle → préjudice utilisateur :** Un même contenu peut devenir inexploitable selon son format ou son organisation.

**Garantie recherchée (matière de l’oral)**

Suivre les besoins de lecture et de réutilisation au-delà d’un seul support.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Nora et Samuel gardent leurs blocs exacts. Les quatre autres personnages seront repris avec leurs ancres, sans nouveau personnage.
- PDF interne : document publié par le service dans le périmètre des deux règles du livre ; pas de nouvelle définition juridique.

**Discours oral du présentateur (non projeté)**

#### Un programme qui circule

- Nora consulte le programme et en reprend des extraits ; Samuel maintient le site.
- Malik parcourt les titres et les tableaux avec son lecteur d’écran.
- Théo appelle les actions d’un lien sur sa tablette ; Inès lit une notice ; Odette annote le programme.
- Leur apparence ne sert pas à expliquer leurs difficultés : ce sont les gestes et les outils qui les rendent visibles.
- La Maison des Lisières et toutes les situations sont fictives.

#### Transition

- Quelques mots permettent de décrire précisément ce que ces outils exploitent.

**Mémo oral :** Un lieu, plusieurs usages du même contenu.

**Fichier final prévu :** `finals/slide-04-fil-rouge.png`

---

### S05 — Six mots pour regarder sous la page

- **Acte :** 0. Entrer dans l’histoire
- **Type :** glossaire
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Définir six notions utiles depuis le glossaire lu.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Partager le vocabulaire.
- Idée principale : Le code décrit des objets et des relations que les outils peuvent utiliser.
- Scène : qui, Samuel ; où, à son bureau de la Maison des Lisières ; objet, le programme et six fiches de vocabulaire ; tension, les mots techniques restent abstraits ; action, il place chaque fiche près de l’objet correspondant sur une grande page d’essai ; résultat, six notions rattachées au même document.
- Transformation visible : Des mots isolés deviennent des repères sur une page.
- Test des trois secondes : « Six mots décrivent ce que les outils lisent. »
- Ajout par rapport à la slide précédente : Les usages reçoivent un vocabulaire commun.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Six mots pour regarder sous la page`
- `Élément HTML`
- `Attribut`
- `Métadonnée`
- `Unicode`
- `Identifiant HTML`
- `Structure de titres`

**Illustration :** Samuel debout devant son écran agrandi fixe six petites fiches pastel en deux rangées. Il tient la dernière, Structure de titres, près d’un plan extrait en retraits. Les cinq autres sont rattachées à des zones de document par des traits fins ; aucun faux code. La scène de bureau reste dominante, les fiches ne remplacent pas l’action.

**Alternative textuelle à fournir :** Samuel associe six termes à une page : élément HTML, attribut, métadonnée, Unicode, identifiant HTML et structure de titres.

**Règle → préjudice utilisateur :** Un mot mal compris conduit à rechercher la mauvaise preuve.

**Garantie recherchée (matière de l’oral)**

Un vocabulaire suffisant pour choisir les contrôles, sans exiger de savoir programmer.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Source : glossaire local, entrées Balise et élément HTML, Attribut, Métadonnée, Unicode, Identifiant HTML, Structure de titres.
- Ne pas recopier l’exemple ambigu content="description" du glossaire ; aucune syntaxe de métadonnée description n’est enseignée ici.

**Discours oral du présentateur (non projeté)**

#### Les objets et leurs relations

- Un élément HTML réunit ses balises et son contenu, ou une balise unique pour certains éléments.
- Un attribut apporte une information à un élément.
- Une métadonnée décrit la page ; celle qui indique le codage se place dans l’élément head.
- Unicode attribue des numéros aux caractères ; UTF-8 en est une forme de codage courante sur le web.
- Un identifiant HTML désigne un élément de façon unique dans la page.
- Une structure de titres reflète l’organisation des sections et sous-sections, avec les titres HTML ou leurs équivalents ARIA.

#### Transition

- Ces notions servent à lire des preuves, au-delà du rendu à l’écran.

**Mémo oral :** Le code nomme et relie les objets.

**Fichier final prévu :** `finals/slide-05-glossaire.png`

---

### S06 — Observer, inspecter, essayer

- **Acte :** 0. Entrer dans l’histoire
- **Type :** méthode
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Choisir le geste de contrôle indiqué par le livre selon l’objet.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Installer la méthode de preuve.
- Idée principale : L’apparence ne suffit pas à vérifier une structure ou un comportement.
- Scène : qui, Samuel ; où, à son bureau ; objet, la page Programme sur un écran et ses informations d’inspection sur l’autre ; tension, une page paraît correcte ; action, il extrait le plan puis essaie la sélection dans le PDF ; résultat, il consigne deux résultats distincts, sans verdict global.
- Transformation visible : Une page apparemment correcte révèle ses propriétés à l’inspection et à l’usage.
- Test des trois secondes : « Regarder ne remplace pas essayer. »
- Ajout par rapport à la slide précédente : Le glossaire débouche sur des gestes du livre.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Observer, inspecter, essayer`
- `Lire le code et les entêtes HTTP`
- `Extraire les titres`
- `Copier et ouvrir le menu`
- `Sélectionner le texte PDF`
- `Linéariser les tableaux`

**Illustration :** Samuel utilise souris et clavier devant deux écrans, le second présentant un plan abstrait à retraits. Un PDF ouvert est posé en vignette à côté de l’écran principal. Les cinq gestes sont portés par cinq fiches sur le bord du bureau. Pas de coche globale, aucun résultat d’exercice.

**Alternative textuelle à fournir :** Samuel inspecte la structure et essaie les fonctions ; cinq gestes associent code, titres, copie, PDF et linéarisation.

**Règle → préjudice utilisateur :** Un contrôle limité au rendu laisse passer un code mal structuré ou une fonction bloquée.

**Garantie recherchée (matière de l’oral)**

Des observations ciblées : le résultat d’un contrôle ne vaut que pour la propriété examinée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôles issus du livre 231 à 245 : inspection, entêtes HTTP, validation, gestes du navigateur, PDF et linéarisation.
- Source statique et code généré ne se confondent pas : tenir compte des titres générés et des tableaux dans le DOM, comme le demande le livre.

**Discours oral du présentateur (non projeté)**

#### Le bon geste pour la bonne propriété

- Le code et les entêtes HTTP renseignent la date et le codage des caractères.
- Un plan extrait révèle les titres, y compris ceux que des scripts génèrent ou que les styles masquent.
- Copier et ouvrir le menu contextuel sont deux essais distincts.
- Dans un PDF, sélectionner le texte et examiner les titres répondent aussi à deux questions différentes.
- Linéariser révèle l’ordre réel des contenus d’un tableau de mise en page.

#### Transition

- La première information à rendre exploitable est parfois une simple date.

**Mémo oral :** Une propriété, son contrôle.

**Fichier final prévu :** `finals/slide-06-methode.png`

---

### S07 — Une date pour les outils

- **Acte :** 1. Caractères et dates
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Associer la date affichée à un balisage time et datetime au bon format.
- **Badge :** `R. 231`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ouvrir l’acte Caractères et dates par une information utile aux outils.
- Idée principale : Une date affichée peut aussi être interprétable dans le code.
- Scène : qui, Nora ; où, à la bibliothèque ; objet, deux notices de publication dans son outil de veille ; tension, elle cherche la notice la plus récente ; action, elle demande un tri par date ; résultat, la notice du 8 novembre remonte et sa date est reliée à une vue de son balisage.
- Transformation visible : La notice datée est retrouvée après le tri ; la date réellement affichée et sa valeur standard apparaissent ensemble.
- Test des trois secondes : « Elle retrouve la notice récente grâce à sa date exploitable. »
- Ajout par rapport à la slide précédente : Premier contrôle appliqué : la date de publication, distincte de la date d’un événement.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E08`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Acte 1 · Caractères et dates`
- `Une date pour les outils`
- `Publié le 8 novembre`
- `<time datetime="2026-11-08">`
- `8 novembre`
- `</time>`
- `GARANTIE - Date exploitable par les outils`

**Illustration :** Nora devant son portable, carnet de veille ouvert. Une flèche de tri remonte une notice dans une pile de deux notices ; la première porte Publié le 8 novembre, la seconde reste abstraite. Un médaillon d’inspection relie la date aux trois lignes exactes de l’élément time. Publié le 8 novembre est la chaîne de la page ; 8 novembre est le contenu de l’extrait, chaîne distincte explicitement autorisée. La situation montre un usage illustratif de classement, sans promettre le comportement d’un moteur de recherche. Un seul encadré GARANTIE.

**Alternative textuelle à fournir :** Nora retrouve une notice par son tri de veille ; sa date de publication affichée est reliée au balisage time et à sa valeur standard.

**Règle → préjudice utilisateur :** Le livre vise la date de publication ou de mise à jour difficile à exploiter pour l’indexation, sans promettre de meilleur classement.

**Garantie recherchée (matière de l’oral)**

Fournir une date exploitable par les moteurs et outils d’indexation, selon le contrôle du livre.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 231 : contrôler chaque date de publication ou de mise à jour affichée, time et datetime au format requis.
- L’avis de l’expert admet aussi schema.org ; le contrôle décrit time. Cette fiche choisit time sans présenter les autres voies comme interdites.
- Code : fragment complet time, date réelle ISO AAAA-MM-JJ ; ne pas ajouter une heure ou un fuseau inutile. Ne pas confondre publication et rendez-vous.

**Discours oral du présentateur (non projeté)**

#### Une date pour les humains et leurs outils

- La notice affiche une date de publication ; son balisage permet aux outils d’indexation de l’exploiter.
- Le livre propose l’élément time et son attribut datetime, au format standard.
- Pour une date, une forme année, mois, jour suffit le plus souvent.
- L’avis de l’expert évoque aussi schema.org ; le format reste indispensable.

##### Impact du non-respect

- Les outils disposent moins facilement d’une date pour classer les contenus.

##### Ce que garantit la règle

- Une date de publication ou de mise à jour disponible sous forme programmatique ; aucune position dans les résultats n’est promise.

#### Transition

- Les mots eux-mêmes ont besoin d’une indication de codage.

**Mémo oral :** Une date affichée, une date exploitable.

**Fichier final prévu :** `finals/slide-07-date-programmatique.png`

---

### S08 — Déclarer le jeu de caractères

- **Acte :** 1. Caractères et dates
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Identifier la métadonnée de codage et son utilité hors ligne.
- **Badge :** `R. 232`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Rendre le rôle de la déclaration tangible.
- Idée principale : Le navigateur doit retrouver dans la page une indication cohérente de son codage.
- Scène : qui, Odette ; où, à la bibliothèque ; objet, la page sauvegardée du programme ; tension, son titre se brouille hors ligne ; action, elle compare la version enregistrée sans indication de codage à la version comportant une meta adaptée ; résultat, le titre devient lisible dans la seconde vue.
- Transformation visible : Deux états de la même lecture hors ligne : titre brouillé à gauche, lisible à droite, meta visible dans la seconde vue.
- Test des trois secondes : « Hors ligne, un titre brouillé peut redevenir lisible. »
- Ajout par rapport à la slide précédente : De la date à la lecture correcte des caractères.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E08`. Ancres de chaque personnage présent : `A-ODETTE` (Odette).

**Texte visible (projection)**

- `Déclarer le jeu de caractères`
- `?t?`
- `Été`
- `<meta charset="utf-8">`
- `IMPACT - Hors ligne, les caractères peuvent se brouiller`
- `CONTRÔLE - Une meta adaptée au codage réel`

**Illustration :** Odette pose son crayon et compare sur le portable deux états de la page enregistrée, avec une petite icône de connexion coupée commune. À gauche, ?t?, chaque point d’interrogation ordinaire entouré d’un petit carré dessiné ; à droite, Été, accompagné de l’extrait meta exact. Sa main pointe le titre redevenu lisible. Les deux mots sont distincts, chacun écrit une fois. Illustration du risque décrit par le livre, pas diagnostic de sa cause : seule l’inspection établit ici l’absence ou la présence de meta. Deux encadrés en bas ; aucun autre personnage ajouté.

**Alternative textuelle à fournir :** Odette compare deux lectures hors ligne du programme : titre brouillé sans indication locale dans le scénario, puis titre Été lisible avec une meta adaptée.

**Règle → préjudice utilisateur :** Sans indication dans la page, le livre décrit un risque d’erreurs de caractères hors ligne ou quand l’entête HTTP manque.

**Garantie recherchée (matière de l’oral)**

Indiquer dans le HTML le jeu de caractères effectif, en cohérence avec l’information du serveur.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 232 : rechercher meta charset ou la forme http-equiv Content-Type et vérifier la pertinence de la valeur.
- L’entête HTTP Content-Type est prioritaire selon le livre ; une métadonnée ne corrige pas à elle seule un entête contradictoire.
- Code corrigé des guillemets corrompus du livre : balise meta complète, sans balise fermante. Les caractères cassés ne prouvent pas seuls l’absence de meta. La dégradation est illustrative ; aucune promesse de correction systématique par une meta seule.

**Discours oral du présentateur (non projeté)**

#### La page garde son indication de codage

- Le serveur transmet normalement le codage par un entête HTTP.
- La métadonnée du HTML rappelle cette information et joue un rôle clé hors ligne ou si l’entête manque.
- Elle doit correspondre au codage effectif du document.
- Le contrôle cherche sa présence et la pertinence de sa valeur, pas seulement le mot UTF-8.

##### Impact du non-respect

- Le navigateur peut mal interpréter les caractères lorsqu’il manque une information fiable.

##### Ce que garantit la règle

- Une indication dans chaque page, utile notamment à sa consultation hors ligne.

#### Transition

- Déclarer un codage et réellement utiliser UTF-8 restent deux questions.

**Mémo oral :** Déclarer ce que la page utilise.

**Fichier final prévu :** `finals/slide-08-metadonnee-caracteres.png`

---

### S09 — UTF-8 tout au long du trajet

- **Acte :** 1. Caractères et dates
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Distinguer un encodage réel cohérent d’une simple étiquette UTF-8.
- **Badge :** `R. 233`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Montrer l’intérêt d’UTF-8 dans la circulation du contenu.
- Idée principale : Le codage effectif et ses déclarations doivent être cohérents.
- Scène : qui, Nora ; où, au bureau éditorial ; objet, l’export du programme reçu dans un tableur ; tension, le nom Café s’y dégrade ; action, elle rapproche l’export de la publication corrigée après contrôle de la chaîne UTF-8 ; résultat, le mot transmis redevient lisible.
- Transformation visible : Le mot Caf? dans l’export reçu devient Café dans la publication après correction de la chaîne.
- Test des trois secondes : « L’export a abîmé le mot ; le trajet corrigé le préserve. »
- Ajout par rapport à la slide précédente : La métadonnée ne suffit plus : on vérifie la cohérence du trajet et le contenu effectif.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `UTF-8 tout au long du trajet`
- `Caf?`
- `Café`
- `UTF-8`
- `IMPACT - Un import peut abîmer les caractères`
- `CONTRÔLE - Entête HTTP, HTML, contenu réel`

**Illustration :** Nora reçoit un export dans un tableur au bureau : une cellule agrandie contient Caf?, et sa main s’arrête sur le mot. Un second état de la notice publiée porte Café, net, après reprise de la chaîne ; un seul bandeau UTF-8 relie les deux supports. Le reste des cellules et du programme est abstrait. Le préjudice visible illustre le livre ; il ne permet pas à lui seul d’identifier un encodage. Pas de base cylindrique ni de chaîne d’objets abstraits comme scène principale.

**Alternative textuelle à fournir :** Nora reçoit un export dont Café est dégradé en Caf? ; une publication après contrôle UTF-8 préserve le mot.

**Règle → préjudice utilisateur :** Des encodages incohérents fragilisent l’affichage et la manipulation lors des imports, exports ou migrations.

**Garantie recherchée (matière de l’oral)**

Utiliser un codage international et prévenir les défauts de caractères ; l’encodage n’est pas établi par l’apparence seule.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 233 : trois temps, entête HTTP Content-Type, cohérence de la métadonnée éventuelle, encodage effectif ; outil Internationalization Checker du W3C cité par le livre.
- Configurer serveur et bases, choisir des outils compatibles UTF-8. Ne pas déduire l’encodage réel du seul libellé meta ni du mot corrompu ; le préjudice est illustratif, la preuve vient des trois temps du contrôle.

**Discours oral du présentateur (non projeté)**

#### Prévenir les erreurs de circulation

- Le livre recommande UTF-8 pour sa capacité à représenter de très nombreux caractères.
- Il demande de configurer le serveur et les bases, et de choisir des outils compatibles.
- La vérification rapproche l’entête HTTP, le HTML et le contenu effectivement encodé.
- Le livre cite le validateur HTML et l’outil d’internationalisation du W3C.

##### Impact du non-respect

- Les défauts de caractères compliquent la lecture et la manipulation des contenus.

##### Ce que garantit la règle

- Le recours à UTF-8 dans une chaîne cohérente contribue à prévenir ces défauts et à faciliter les migrations.

#### Transition

- Une déclaration présente n’est donc pas la preuve d’un encodage réel correct.

**Mémo oral :** UTF-8 se vérifie dans le contenu aussi.

**Fichier final prévu :** `finals/slide-09-encodage-utf8.png`

---

### S10 — Déclaré et utilisé : deux preuves

- **Acte :** 1. Caractères et dates
- **Type :** distinction
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Séparer la présence d’une métadonnée du choix effectif d’UTF-8.
- **Badge :** `R. 232 · 233`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Distinguer deux règles voisines.
- Idée principale : L’une demande une déclaration dans la page, l’autre le codage UTF-8.
- Scène : qui, Samuel ; où, au bureau éditorial ; objet, la page enregistrée et le fichier importé qui ont gêné Odette et Nora ; tension, lire UTF-8 sur une étiquette peut masquer un contenu réellement différent ; action, il ouvre le head dans le panneau gauche, puis confronte entête HTTP et contenu dans le panneau droit ; résultat, une fiche de présence et trois pièces de contrôle sont physiquement séparées.
- Transformation visible : Samuel sépare la recherche d’une déclaration dans head et le rapprochement de trois preuves de codage.
- Test des trois secondes : « La présence d’une déclaration et son encodage ne se confondent pas. »
- Ajout par rapport à la slide précédente : La distinction explicite entre les deux fiches précédentes.

**Référence de composition principale :** `N03`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Déclaré et utilisé : deux preuves`
- `Métadonnée dans la page`
- `UTF-8 réellement utilisé`
- `Une déclaration ne prouve pas l’encodage`

**Illustration :** Samuel debout entre deux panneaux titrés. À gauche, il ouvre l’élément head d’une page sauvegardée : loupe et emplacement de métadonnée en lignes abstraites. À droite, il rapproche sur le bureau le relevé HTTP, le fichier reçu dans le tableur et le résultat de contrôle du contenu. Sur le fichier, deux groupes de glyphes abstraits désaccordés indiquent la gêne à résoudre, sans créer de diagnostic. Les deux panneaux répondent aux deux incidents vécus précédemment ; pas de bureau décoratif ni de coche de conformité. Bandeau final de distinction.

**Alternative textuelle à fournir :** Deux preuves : une métadonnée dans le HTML et une cohérence UTF-8 entre serveur, déclaration et contenu réel.

**Règle → préjudice utilisateur :** Cocher UTF-8 en lisant seulement une métadonnée laisse passer un contenu encodé autrement.

**Garantie recherchée (matière de l’oral)**

Choisir un contrôle adapté à chaque règle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Un fichier encodé et servi en UTF-8 peut manquer de meta : défaut de 232, sans défaut de 233 établi.
- Ne pas fabriquer un exemple visible avec un encodage obsolète présenté comme du HTML actuel valide.

**Discours oral du présentateur (non projeté)**

#### Deux questions indépendantes

- La métadonnée doit se trouver dans chaque page et désigner le codage pertinent.
- UTF-8 doit être réellement utilisé, avec des indications cohérentes.
- Une page peut être effectivement en UTF-8 tout en manquant de métadonnée.
- Inversement, lire une déclaration ne dispense pas de contrôler le contenu et l’entête.

#### Transition

- C’est le constat précis qui désigne la règle à retenir.

**Mémo oral :** Déclarer et encoder : deux preuves.

**Fichier final prévu :** `finals/slide-10-distinction-declaration-encodage.png`

---

### S11 — Checkpoint 1 : caractères et dates

- **Acte :** 1. Caractères et dates
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** Rattacher trois constats à leur règle sans déduire plus que leur preuve.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Réactiver les trois règles de l’acte.
- Idée principale : Chaque constat vise une propriété distincte.
- Scène : qui, Samuel ; où, à son bureau ; objet, trois fiches de constat ; tension, les deux dernières parlent du même codage ; action, il note une réponse par fiche ; résultat, aucune correction visible.
- Transformation visible : Les trois contrôles deviennent trois diagnostics à produire.
- Test des trois secondes : « Trois constats, trois objets de contrôle. »
- Ajout par rapport à la slide précédente : Application après la distinction.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Checkpoint 1 : caractères et dates`
- `Quelle règle est prouvée enfreinte ?`
- `A. Date sans forme programmatique`
- `B. UTF-8 réel, aucune meta`
- `C. Codage réel : pas UTF-8`

**Illustration :** Question en bandeau, trois cartes A à C titrées de leur ligne. Samuel écrit sur un carnet à gauche. Les cartes contiennent respectivement une notice datée et son relevé d’inspection, une page enregistrée, un fichier importé ; vues abstraites. Aucune coche, croix, couleur de correction ou réponse chiffrée.

**Alternative textuelle à fournir :** Trois constats à rattacher à une règle : une date sans représentation programmatique, une page UTF-8 sans meta, un contenu qui n’utilise pas UTF-8.

**Règle → préjudice utilisateur :** Confondre déclaration et contenu conduit à corriger la mauvaise chose.

**Garantie recherchée (matière de l’oral)**

Un rattachement appuyé sur la propriété effectivement contrôlée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 40 secondes de réflexion puis 40 secondes de correction, comprises dans la durée.
- A signifie : date de publication affichée, sans time ni autre représentation programmatique ; cette absence figure dans le constat projeté ; aucune exception n’est cachée à l’oral. B suppose un contrôle préalable du contenu et de l’entête.
- Les distracteurs restent dans les notes, comme dans Présentation.

**Discours oral du présentateur (non projeté)**

#### Trois informations à distinguer

- La date affichée, l’indication de codage et le codage effectif sont trois objets de contrôle.
- Une preuve portant sur un objet ne tranche pas les deux autres.
- Un affichage lisible ne remplace ni le balisage de la date ni l’examen du codage.

#### Transition

- Une fois les caractères interprétables, il reste à organiser le contenu.

**Corrigé (notes du présentateur, non projeté) :** A → 231 : aucune forme programmatique pour la date publiée, ni time ni autre solution (distracteur : 232, qui vise une autre métadonnée). B → 232 : la métadonnée manque malgré un codage UTF-8 établi (distracteur : 233, aucun défaut de codage n’est donné). C → 233 : le codage effectif n’est pas UTF-8 (distracteur : 232, le constat ne dit pas que la déclaration manque).

**Mémo oral :** Nommer la propriété réellement contrôlée.

**Fichier final prévu :** `finals/slide-11-checkpoint-1.png`

---

### S12 — Atteindre la bonne section

- **Acte :** 2. Structure du contenu
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Comprendre le plan de titres HTML et les contrôles de hiérarchie.
- **Badge :** `R. 234`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ouvrir l’acte Structure du contenu.
- Idée principale : Un vrai plan permet de rejoindre directement une section.
- Scène : qui, Malik ; où, à la bibliothèque ; objet, la longue page Programme ; tension, de gros textes sans balisage de titre ne fournissent pas de plan ; action, il appelle la liste des titres au clavier ; résultat, une vue corrigée lui permet de rejoindre la rubrique des ateliers.
- Transformation visible : Un plan extrait donne accès aux sections, au lieu d’une lecture continue imposée.
- Test des trois secondes : « Malik rejoint une section depuis le plan. »
- Ajout par rapport à la slide précédente : Du codage des caractères à l’organisation de la page.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `Acte 2 · Structure du contenu`
- `Atteindre la bonne section`
- `Ateliers`
- `IMPACT - Sans titres, je parcours tout`
- `GARANTIE - Les sections ont une hiérarchie exploitable`

**Illustration :** Malik au clavier à gauche. Une grande page avec trois sections en blocs abstraits est reliée à un plan à retraits bleu clair ; une entrée du plan porte Ateliers. Un trait rejoint cette entrée à la section visée. Aucun h1 dessiné comme un mot de la page, aucun titre fictif ajouté. Deux encadrés bas ; la scène montre la solution, pas deux plans trop petits.

**Alternative textuelle à fournir :** Malik appelle le plan de titres de la page et rejoint directement Ateliers au lieu de tout parcourir.

**Règle → préjudice utilisateur :** Sans titres balisés et hiérarchisés, l’accès direct aux sections et l’extraction du plan sont compromis.

**Garantie recherchée (matière de l’oral)**

Fournir une structure que les utilisateurs et les outils d’indexation peuvent exploiter.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 234 : au moins un h1 pour la section principale, h2 à h6 selon les sous-sections, pas de trou dans la descente de niveaux. Un retour vers un niveau supérieur n’est pas un trou.
- Tenir compte des titres masqués et générés par JavaScript. L’expert précise que plusieurs h1 sont possibles ; ne jamais imposer un h1 unique.
- La taille ou la graisse d’un texte ne prouve pas son niveau. L’entrée Ateliers figure une seule fois dans le plan.

**Discours oral du présentateur (non projeté)**

#### Un plan que les outils peuvent extraire

- Des titres balisés permettent d’atteindre directement la section recherchée.
- Le livre demande au moins un titre de premier niveau, puis des sous-titres adaptés au contenu.
- Il vérifie l’absence de niveau sauté en descendant la hiérarchie.
- Le plan doit prendre en compte les titres masqués et ceux qui sont générés par des scripts.
- Plusieurs titres de premier niveau peuvent être justifiés par l’organisation du contenu.

##### Impact du non-respect

- Malik perd les points d’entrée que son lecteur d’écran peut exploiter.

##### Ce que garantit la règle

- Une organisation en sections et sous-sections exploitable au-delà de l’affichage graphique.

#### Transition

- À l’intérieur d’une section, une liste a elle aussi une structure.

**Mémo oral :** Un titre est une relation dans un plan.

**Fichier final prévu :** `finals/slide-12-titres-hierarchises.png`

---

### S13 — Des puces, une vraie liste

- **Acte :** 2. Structure du contenu
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Identifier le balisage attendu des listes visuelles et ses limites.
- **Badge :** `R. 235`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Passer du plan aux items regroupés.
- Idée principale : Les marqueurs visibles doivent correspondre à une sémantique de liste.
- Scène : qui, Malik ; où, à la table de préparation ; objet, le matériel de l’atelier sur le portable ; tension, des puces tapées ne sont pas identifiées comme liste ; action, il parcourt au clavier la version balisée ; résultat, une restitution annonce la liste et ses deux éléments.
- Transformation visible : Le balisage relie les deux items à une annonce de liste dans l’usage de Malik.
- Test des trois secondes : « Malik entend que le matériel forme une liste de deux éléments. »
- Ajout par rapport à la slide précédente : Des sections de page à leur contenu détaillé.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E08`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `Des puces, une vraie liste`
- `<ul><li>Fil</li>`
- `<li>Papier</li></ul>`
- `« Liste, 2 éléments »`
- `IMPACT - Puces tapées : aucune liste annoncée`
- `GARANTIE - Items annoncés`

**Illustration :** Malik au clavier, casque gris clair, devant le matériel de l’atelier. Deux lignes exactes forment la liste complète dans un ruban d’inspection. Une bulle « Liste, 2 éléments » rejoint son casque ; Fil et Papier ne sont écrits que dans le code, les objets restent une bobine et une pile de papier sans étiquette. Le scénario illustre une restitution possible, pas une phrase universelle de lecteur d’écran. Aucun autre personnage.

**Alternative textuelle à fournir :** Malik parcourt le matériel balisé comme liste ; une annonce illustrative lui signale deux éléments, Fil et Papier.

**Règle → préjudice utilisateur :** Des retours à la ligne et des signes tapés ne permettent pas aux outils d’identifier et de restituer la liste comme telle.

**Garantie recherchée (matière de l’oral)**

Une liste identifiable, compréhensible et réutilisable par les navigateurs et aides techniques.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 235 : ul/li, ol/li, dl/dt/dd selon le type ; à défaut, rôles list/listitem pour les listes ordonnées ou non ordonnées, pas d’équivalent de liste de définitions par rôle.
- Contrôle des listes explicitement présentées avec marqueurs et retours à la ligne ; ne pas exiger une liste pour toute énumération horizontale. dl associe entrée et description, pas un formulaire ou menu déroulant.
- Code : deux lignes concaténées forment un fragment ul complet et valide. Le ddn du contrôle imprimé est une coquille ; retenir dd, présent dans les solutions. L’annonce et son absence dans le cas de puces tapées sont illustratives ; elles n’ont pas été testées sur un logiciel réel.

**Discours oral du présentateur (non projeté)**

#### Une liste ne se réduit pas à sa puce

- Les éléments HTML permettent aux outils de reconnaître une liste et ses items.
- Le type dépend du contenu : non ordonné, ordonné, ou termes associés à des descriptions.
- Le livre admet à défaut les rôles ARIA de liste et d’item, sans équivalent pour les listes de définitions.
- Le contrôle vise d’abord les listes explicitement affichées avec marqueurs et retours à la ligne.

##### Impact du non-respect

- La liste paraît structurée mais les outils ne peuvent pas en exploiter correctement l’organisation.

##### Ce que garantit la règle

- Une sémantique adaptée au type de liste, au-delà de son dessin.

#### Transition

- Pour relier un élément précis à une information, il faut aussi pouvoir le désigner sans ambiguïté.

**Mémo oral :** La puce se voit, la liste se balise.

**Fichier final prévu :** `finals/slide-13-listes-balisees.png`

---

### S14 — Un identifiant, un seul élément

- **Acte :** 2. Structure du contenu
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Comprendre la portée par page de l’unicité des id.
- **Badge :** `R. 236`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Montrer le risque d’une cible ambiguë.
- Idée principale : Un identifiant dupliqué fragilise les associations et les scripts.
- Scène : qui, Samuel ; où, devant le formulaire de réservation au bureau ; objet, deux composants copiés depuis le même modèle ; tension, ils partagent un identifiant ; action, il lance le contrôle des identifiants et corrige le second composant ; résultat, chaque étiquette retrouve une cible distincte.
- Transformation visible : Deux traits croisés deviennent deux associations séparées.
- Test des trois secondes : « Deux champs doivent avoir deux cibles distinctes. »
- Ajout par rapport à la slide précédente : Des regroupements de contenu aux relations entre éléments.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Un identifiant, un seul élément`
- `id dupliqué`
- `IMPACT - Les associations deviennent ambiguës`
- `CONTRÔLE - Chaque id est unique dans la page`

**Illustration :** Samuel à gauche relit le résultat d’un contrôle. Un médaillon montre deux champs et leurs étiquettes abstraites reliés par deux traits corail croisés ; le cartouche id dupliqué désigne le résultat. À droite, les mêmes paires portent deux formes de cible distinctes, les traits ne se croisent plus. Aucun extrait HTML invalide affiché, aucune conséquence identique promise sur tous les navigateurs.

**Alternative textuelle à fournir :** Samuel détecte un identifiant HTML dupliqué dans deux composants puis rétablit deux associations distinctes.

**Règle → préjudice utilisateur :** Selon le livre, des id dupliqués peuvent perturber les relations champ-étiquette, les scripts et la restitution, avec des effets variables.

**Garantie recherchée (matière de l’oral)**

Réduire les ambiguïtés d’interprétation du DOM : une valeur id par page, un seul élément.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 236 : validateur HTML ou autre outil, chaque valeur id unique. Ne pas remplacer cette règle par une exigence de validité complète du HTML.
- Périmètre : même page, pas tout le site ; les classes peuvent être répétées. Exemple illustratif, aucun comportement précis du lecteur d’écran n’est affirmé.
- Lien explicite du livre vers les champs et étiquettes : règle connexe 69, libellé exact dans Sources et couverture et S31.

**Discours oral du présentateur (non projeté)**

#### Une référence doit retrouver une seule cible

- Copier un composant peut dupliquer son identifiant dans la même page.
- Le livre décrit un risque pour les scripts et pour l’association d’un champ à son étiquette.
- Le comportement varie selon les outils ; un affichage apparemment normal ne prouve donc rien.
- Un validateur peut repérer cette erreur précise sans faire de toute erreur HTML un défaut de cette règle.

##### Impact du non-respect

- Une interaction ou une restitution peut devenir erronée ou bloquante.

##### Ce que garantit la règle

- Des identifiants uniques dans la page limitent l’interprétation hasardeuse de ces relations.

#### Transition

- Un repère unique, un titre et une liste répondent à des besoins différents.

**Mémo oral :** Unique dans la page, pas dans tout le site.

**Fichier final prévu :** `finals/slide-14-identifiants-uniques.png`

---

### S15 — Plan de sections ou liste d’items

- **Acte :** 2. Structure du contenu
- **Type :** distinction
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Séparer le balisage des titres et celui des listes visuelles.
- **Badge :** `R. 234 · 235`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Distinguer deux organisations du contenu.
- Idée principale : La hiérarchie de sections n’est pas l’énumération de ses items.
- Scène : qui, Inès ; où, devant la notice d’un atelier à la bibliothèque ; objet, son sommaire et le matériel nécessaire ; tension, les deux présentent plusieurs lignes ; action, elle rejoint une section puis parcourt les items ; résultat, deux gestes et deux organisations.
- Transformation visible : Des lignes semblables visuellement deviennent deux usages distincts.
- Test des trois secondes : « Choisir une section ou parcourir une liste. »
- Ajout par rapport à la slide précédente : La structure se distingue par sa fonction, pas sa forme.

**Référence de composition principale :** `N03`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-INES` (Inès).

**Texte visible (projection)**

- `Plan de sections ou liste d’items`
- `Titres : rejoindre une section`
- `Liste : regrouper des items`
- `Des lignes empilées ne prouvent ni l’un ni l’autre`

**Illustration :** Inès à sa table, une main sur la tablette, l’autre sur une fiche de matériel. Deux panneaux : à gauche, son geste vise une entrée d’un plan à retraits reliée à une section ; à droite, elle rapproche deux objets d’une liste à puces abstraite. Tous les textes sont les titres des panneaux et le bandeau. Aucun diagnostic sur la dyslexie.

**Alternative textuelle à fournir :** Inès utilise un plan pour rejoindre une section et une liste pour parcourir les items de matériel.

**Règle → préjudice utilisateur :** Corriger une liste avec des titres ou des titres avec des puces ne répare pas le besoin de navigation correspondant.

**Garantie recherchée (matière de l’oral)**

Identifier la relation recherchée avant de choisir le balisage.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Ne pas présenter tout élément en gros caractères comme un titre, ni toute succession de lignes comme une liste.
- Une liste de sommaire peut contenir des liens vers des titres ; cela ne confond pas les deux structures.

**Discours oral du présentateur (non projeté)**

#### Deux relations différentes

- Les titres organisent le document en sections et sous-sections.
- Une liste regroupe des items d’un type adapté à leur relation.
- Un sommaire peut être une liste de liens vers des titres : les deux structures coexistent.
- La mise en forme seule ne permet pas de les vérifier ; il faut examiner leur balisage.

#### Transition

- Le contrôle doit nommer la relation qui manque.

**Mémo oral :** Les titres organisent, les listes regroupent.

**Fichier final prévu :** `finals/slide-15-distinction-titres-listes.png`

---

### S16 — Checkpoint 2 : structurer

- **Acte :** 2. Structure du contenu
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** Distinguer titres, listes et identifiants avec trois constats explicites.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Réactiver les trois règles de structure.
- Idée principale : Chaque défaut porte sur une relation identifiée au code.
- Scène : qui, Inès ; où, à la table de lecture ; objet, trois constats préparés par Samuel ; tension, les écrans seuls pourraient se ressembler ; action, elle rapproche les constats de ses notes ; résultat, ses réponses restent cachées.
- Transformation visible : L’apparence laisse place à trois constats précis.
- Test des trois secondes : « Un exercice sur ce que dit le code. »
- Ajout par rapport à la slide précédente : Application de la distinction précédente et de l’unicité.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-INES` (Inès).

**Texte visible (projection)**

- `Checkpoint 2 : structurer`
- `Quelle règle est prouvée enfreinte ?`
- `A. Plan : h1 puis h3`
- `B. Puces tapées, simples paragraphes`
- `C. Même id sur deux champs`

**Illustration :** Trois cartes A à C à droite, une ligne chacune ; Inès à gauche écrit une réponse dans son carnet. Vignettes : un plan à étage sauté, une liste visible à puces avec un relevé source abstrait, deux champs reliés à une même cible. Aucune coche, croix ou réponse visible. h1 puis h3 est un constat en langage courant, pas une ligne de code.

**Alternative textuelle à fournir :** Trois constats : un niveau de titre sauté, des puces sans balisage de liste, un identifiant partagé par deux champs.

**Règle → préjudice utilisateur :** Une mauvaise association entre constat et règle laisse la structure défaillante.

**Garantie recherchée (matière de l’oral)**

Diagnostiquer la relation absente ou ambiguë.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 40 secondes de réflexion, 40 secondes de correction.
- A : la succession descendante est donnée après extraction de tous les titres, masqués et générés compris. B : aucun rôle ARIA de liste ni d’item. Ces deux précisions lèvent les exceptions sans changer la réponse.

**Discours oral du présentateur (non projeté)**

#### Trois relations à préserver

- Le plan organise les sections selon leurs niveaux.
- La liste permet de reconnaître ses items.
- L’identifiant retrouve un élément précis.
- Le constat d’inspection indique laquelle de ces relations fait défaut.

#### Transition

- Même structurée, la page peut retirer à la personne les commandes de son navigateur.

**Corrigé (notes du présentateur, non projeté) :** A → 234 : trou dans la succession descendante h1 puis h3 après extraction complète (distracteur : 235, aucun item de liste n’est en cause). B → 235 : liste visuelle sans éléments appropriés ni rôles ARIA (distracteur : 234, les lignes sont des items, pas des sections). C → 236 : même identifiant attribué deux fois dans la page (distracteur : 69, qui vise l’association champ-étiquette ; seule l’unicité est ici constatée).

**Mémo oral :** Repérer la relation qui manque.

**Fichier final prévu :** `finals/slide-16-checkpoint-2.png`

---

### S17 — Reprendre une phrase

- **Acte :** 3. Garder la main
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Reconnaître le blocage de la copie dans une page web et tester la commande habituelle.
- **Badge :** `R. 237`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ouvrir l’acte Garder la main.
- Idée principale : La personne doit pouvoir utiliser la commande Copier du navigateur.
- Scène : qui, Nora ; où, à une table de café de la Maison des Lisières ; objet, la notice HTML d’un atelier et un carnet numérique ; tension, elle veut citer une phrase mais la commande de copie est bloquée ; action, elle lance Copier depuis le menu principal ; résultat, le collage ne reprend pas le passage.
- Transformation visible : Un passage sélectionné n’arrive pas dans la note de citation.
- Test des trois secondes : « Elle veut citer ; la commande Copier échoue. »
- Ajout par rapport à la slide précédente : Après les relations de contenu, les commandes de la personne.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Acte 3 · Garder la main`
- `Reprendre une phrase`
- `Copie bloquée`
- `IMPACT - Je ne peux pas reprendre ce passage`
- `GARANTIE - Les fonctions de copie restent disponibles`

**Illustration :** Nora utilise un portable et sélectionne des lignes abstraites dans une page web, distincte d’un PDF. Une petite commande du menu principal en haut de l’écran est activée ; le résultat Copie bloquée apparaît dans une notification de démonstration. La flèche vers sa note est interrompue par un petit signe d’arrêt. La note contient des lignes abstraites antérieures, pas un cadre vide. Aucun menu contextuel représenté.

**Alternative textuelle à fournir :** Nora tente de copier un passage d’une page HTML pour le citer ; la commande est bloquée et le passage n’arrive pas dans sa note.

**Règle → préjudice utilisateur :** Blocage de la copie : gêne pour citer, traduire, référencer ou réutiliser le contenu, usages cités par le livre.

**Garantie recherchée (matière de l’oral)**

Laisser les fonctions courantes de copie du navigateur disponibles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 237 : ne bloquer la copie ni par JavaScript ni par CSS ni par une autre technique ; vérifier la fonction courante pour chaque page.
- Ne pas affirmer qu’un menu contextuel bloqué prouve une copie bloquée ; cette scène utilise le menu principal.
- L’absence de nouveau texte dans une note n’est pas une preuve réelle : la notification rend explicite le résultat fictif du geste. Aucun essai sur le site réel n’est revendiqué.

**Discours oral du présentateur (non projeté)**

#### Réutiliser fait partie de la consultation

- Une personne peut vouloir traduire un passage, le citer ou garder une référence.
- Bloquer la commande de copie gêne ces usages ordinaires.
- Le livre demande de laisser fonctionner la copie, quelle que soit la technique de blocage envisagée.
- Il rappelle qu’on ne peut pas empêcher complètement la copie d’un contenu disponible en ligne.

##### Impact du non-respect

- Nora ne peut pas reprendre son passage par la fonction courante du navigateur.

##### Ce que garantit la règle

- La disponibilité de cette fonction pour la manipulation et la réutilisation du contenu.

#### Transition

- Le menu contextuel rassemble d’autres commandes qu’il faut vérifier à part.

**Mémo oral :** La consultation comprend la réutilisation.

**Fichier final prévu :** `finals/slide-17-copie-contenu.png`

---

### S18 — Le menu reste à moi

- **Acte :** 3. Garder la main
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Distinguer l’accès au menu contextuel des commandes de copie.
- **Badge :** `R. 238`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Montrer une autre commande retirée.
- Idée principale : Ouvrir le menu contextuel permet d’accéder aux actions du navigateur.
- Scène : qui, Théo ; où, dans le hall ; objet, un lien du programme sur sa tablette tenue en main ; tension, il veut accéder aux actions sur ce lien ; action, il maintient le doigt sur le lien pour appeler les actions contextuelles ; résultat, le menu habituel reste disponible dans la situation corrigée.
- Transformation visible : Le geste ouvre un menu au lieu d’être neutralisé.
- Test des trois secondes : « Le navigateur laisse choisir les actions du lien. »
- Ajout par rapport à la slide précédente : De Copier à un menu qui contient aussi d’autres actions.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-THEO` (Théo).

**Texte visible (projection)**

- `Le menu reste à moi`
- `Ouvrir dans un nouvel onglet`
- `IMPACT - Mes actions habituelles disparaissent`
- `LIMITE - Un menu applicatif spécifique peut se justifier`

**Illustration :** Théo tient sa tablette d’une main et maintient un doigt de l’autre sur un lien. Dans l’agrandissement, les actions contextuelles s’ouvrent ; une seule ligne est lisible, Ouvrir dans un nouvel onglet. Les autres sont des barres abstraites. Pas de clavier ajouté ni de mot Copier. Geste tactile équivalent choisi pour cette scène, sans imitation exacte ni promesse sur tous les navigateurs.

**Alternative textuelle à fournir :** Théo appelle le menu contextuel d’un lien et peut choisir de l’ouvrir dans un nouvel onglet.

**Règle → préjudice utilisateur :** Bloquer le menu contextuel retire l’accès habituel aux fonctions de consultation et de navigation.

**Garantie recherchée (matière de l’oral)**

Laisser à l’utilisateur le contrôle de ses menus et actions, avec la nuance applicative citée par l’expert.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 238 : vérifier l’ouverture du menu contextuel sur l’ensemble des contenus affichés ; le geste peut être un clic droit ou un raccourci adapté au système. L’appui long est l’adaptation illustrative au tactile, à contrôler sur le navigateur cible en production.
- Exception de l’expert : application graphique ou cartographique dotée d’un menu spécifique pour le contenu manipulé ; pas une permission générale de neutraliser le menu.
- Le contenu exact varie selon le navigateur et le contexte ; aucune promesse d’une même liste de commandes partout.

**Discours oral du présentateur (non projeté)**

#### Un menu appartient aux usages du navigateur

- Le clic droit ou certains raccourcis ouvrent des actions liées au contenu visé.
- Leur liste dépend du navigateur et du contexte.
- Les neutraliser gêne des fonctions utiles sans protéger réellement le contenu contre la copie.
- L’expert admet le cas d’une application qui fournit un menu spécifique pour des actions graphiques ou cartographiques.

##### Impact du non-respect

- Théo perd son accès habituel aux actions sur le lien.

##### Ce que garantit la règle

- L’accès aux fonctions contextuelles de l’outil de consultation, dans le périmètre prévu par le livre.

#### Transition

- Copier et appeler le menu restent deux gestes indépendants, même sur un même contenu.

**Mémo oral :** Le menu reste un outil de la personne.

**Fichier final prévu :** `finals/slide-18-menu-contextuel.png`

---

### S19 — Copier ou ouvrir le menu

- **Acte :** 3. Garder la main
- **Type :** distinction
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Rendre les deux essais indépendants.
- **Badge :** `R. 237 · 238`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Distinguer deux blocages souvent confondus.
- Idée principale : La copie peut rester possible quand le menu contextuel est bloqué, et inversement.
- Scène : qui, Nora ; où, devant son portable au café ; objet, la même page dans deux essais successifs ; tension, un blocage peut masquer l’autre ; action, elle copie via le menu principal puis appelle le menu contextuel ; résultat, les deux observations sont inscrites séparément.
- Transformation visible : Un jugement global devient deux résultats indépendants.
- Test des trois secondes : « Deux gestes, deux réponses à recueillir. »
- Ajout par rapport à la slide précédente : Les deux premières règles de l’acte sont comparées explicitement.

**Référence de composition principale :** `N03`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Copier ou ouvrir le menu`
- `Copier par la commande habituelle`
- `Ouvrir le menu contextuel`
- `Un geste réussi ne prouve pas l’autre`

**Illustration :** Nora entre deux panneaux titrés. Gauche : elle sélectionne un passage et le retrouve dans sa note, sans texte lisible. Droite : elle appelle un menu contextuel ; le contour de menu est interrompu par un signe d’arrêt. Le contraste entre les gestes est la seule idée. Bandeau bas sur les preuves indépendantes.

**Alternative textuelle à fournir :** Nora réussit une copie par le menu principal mais ne peut ouvrir le menu contextuel : deux contrôles distincts.

**Règle → préjudice utilisateur :** Déduire les deux résultats d’un seul geste fait passer un blocage inaperçu.

**Garantie recherchée (matière de l’oral)**

Vérifier séparément la fonction Copier et l’ouverture du menu contextuel.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Le cas illustratif donne une copie réussie et un menu bloqué. Il ne prétend pas que ce comportement vaut pour tous les navigateurs.
- La commande utilisée pour copier n’est pas le menu contextuel testé dans l’autre panneau.

**Discours oral du présentateur (non projeté)**

#### Deux résultats à recueillir

- Copier un passage peut se faire par une commande qui reste accessible sans le menu contextuel.
- Le menu contextuel donne accès à d’autres fonctions que Copier.
- Son blocage ne prouve donc pas un blocage de la copie.
- Il faut essayer les deux fonctionnalités pour conclure sur chacune.

#### Transition

- La même précision s’applique à un changement automatique de page.

**Mémo oral :** Copier et ouvrir le menu : deux essais.

**Fichier final prévu :** `finals/slide-19-distinction-copie-menu.png`

---

### S20 — Ne pas recommencer sa lecture

- **Acte :** 3. Garder la main
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Reconnaître un rafraîchissement ou une redirection côté client imposé et la désactivation préalable attendue.
- **Badge :** `R. 239`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Protéger le temps de lecture.
- Idée principale : Un changement automatique imposé peut couper une consultation en cours.
- Scène : qui, Inès ; où, sur un banc du hall ; objet, une longue notice d’atelier sur sa tablette ; tension, la page se recharge sans commande de sa part ni arrêt proposé ; action, elle lisait un passage à mi-page ; résultat, elle se retrouve au début et cherche sa place.
- Transformation visible : Le repère de lecture à mi-page est perdu après rechargement.
- Test des trois secondes : « La page a changé avant qu’elle ait fini. »
- Ajout par rapport à la slide précédente : Des commandes bloquées à une action déclenchée sans choix.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-INES` (Inès).

**Texte visible (projection)**

- `Ne pas recommencer sa lecture`
- `Recharge imposée`
- `IMPACT - Je perds le passage que je lisais`
- `CONTRÔLE - Pas de meta refresh, le reste désactivable avant`

**Illustration :** Inès assise avec sa tablette, un doigt repère une ligne. Deux vues successives du même écran sont reliées par une flèche circulaire : à gauche une barre de défilement à mi-course, à droite en haut. Une petite marque de lecture reste en pointillé à l’ancien endroit. Le résultat Recharge imposée est une observation fictive du scénario, pas un bouton. Pas de compte à rebours qui ajouterait un texte hors liste.

**Alternative textuelle à fournir :** Une recharge non demandée ramène Inès au début de la notice ; elle cherche le passage qu’elle lisait.

**Règle → préjudice utilisateur :** Le livre décrit interruptions, pertes de repères, répétition du défilement et données mobiles non désirées.

**Garantie recherchée (matière de l’oral)**

Laisser le contrôle du changement à l’utilisateur ; les mécanismes éventuels doivent être désactivables auparavant via le site.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 239 : absence de meta http-equiv refresh ; pour les autres mécanismes cités, vérifier une désactivation préalable dans l’interface du site, pas seulement une option du navigateur.
- Ne pas assimiler toute mise à jour partielle AJAX à un rechargement imposé, ni une redirection HTTP 3xx à une redirection côté client. La distinction AJAX est une précision pédagogique hors livre ; le livre inclut l’entête HTTP refresh parmi les mécanismes à contrôler.
- La non-désactivabilité est une donnée explicite du scénario ; un simple dessin de flèche circulaire ne la prouverait pas. Le contrôle réel exige observation et inspection.

**Discours oral du présentateur (non projeté)**

#### Le temps de lire ne se décide pas à l’avance

- Un rechargement peut ramener au début du contenu ; une redirection peut laisser trop peu de temps pour lire un avertissement.
- Le livre souligne les difficultés au lecteur d’écran et lors d’une consultation mobile.
- Il demande de ne pas utiliser la métadonnée de rafraîchissement automatique.
- Les autres mécanismes éventuels doivent pouvoir être désactivés avant leur déclenchement, depuis le site.

##### Impact du non-respect

- La lecture est interrompue et le passage doit être retrouvé ; des données mobiles peuvent être consommées sans souhait de l’utilisateur.

##### Ce que garantit la règle

- La maîtrise de la consultation face aux redirections et rechargements côté client.

#### Transition

- Les commandes bloquées et le changement automatique se distinguent par le geste qui a échoué.

**Mémo oral :** Le temps de lecture appartient à la personne.

**Fichier final prévu :** `finals/slide-20-rafraichissement-impose.png`

---

### S21 — Checkpoint 3 : garder la main

- **Acte :** 3. Garder la main
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** Identifier les trois défauts de maîtrise de l’interface.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Réactiver les règles sur les commandes et le temps.
- Idée principale : Le geste empêché ou imposé désigne la règle.
- Scène : qui, Nora ; où, à la table de café ; objet, trois relevés de gestes ; tension, deux parlent du navigateur, le troisième du rythme ; action, elle écrit trois diagnostics ; résultat, réponses masquées.
- Transformation visible : Trois gestes deviennent trois rattachements.
- Test des trois secondes : « Quel contrôle a réellement échoué ? »
- Ajout par rapport à la slide précédente : Application après la recharge imposée et la distinction copie/menu.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Checkpoint 3 : garder la main`
- `Quelle règle est prouvée enfreinte ?`
- `A. Copier bloqué, menu ouvert`
- `B. Menu bloqué, copie possible`
- `C. Recharge auto non désactivable`

**Illustration :** Question en bandeau, trois cartes titrées A à C. Nora écrit sur son carnet. Les mini-scènes montrent une sélection vers une note, une main au-dessus d’un menu, une page revenue en haut. Aucun symbole de réussite ou d’erreur ajouté : les constats textuels suffisent et les réponses restent dans les notes.

**Alternative textuelle à fournir :** Trois résultats à diagnostiquer : copie bloquée seule, menu contextuel bloqué seul, recharge automatique sans désactivation préalable possible.

**Règle → préjudice utilisateur :** Confondre le menu et la copie laisse l’un des blocages sans solution.

**Garantie recherchée (matière de l’oral)**

Rattacher le défaut au résultat constaté, sans présumer celui des autres gestes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 40 secondes de réflexion puis 40 de correction.
- B : page éditoriale ordinaire, pas un menu spécifique d’application ; C : pas de désactivation possible avant le rechargement. Aucun navigateur particulier n’est supposé.

**Discours oral du présentateur (non projeté)**

#### Ce qui est bloqué et ce qui est imposé

- La fonction de copie et le menu contextuel sont contrôlés séparément.
- Le rechargement imposé retire un autre choix : celui de poursuivre la lecture.
- La disponibilité d’une fonction ne compense pas le blocage d’une autre.

#### Transition

- Un document téléchargé doit lui aussi laisser du texte et des repères exploitables.

**Corrigé (notes du présentateur, non projeté) :** A → 237 : la fonction Copier échoue alors que le menu s’ouvre (distracteur : 238, explicitement écartée). B → 238 : menu contextuel bloqué dans une page ordinaire, copie possible (distracteur : 237, explicitement écartée). C → 239 : recharge côté client sans désactivation préalable dans le site (distracteur : 238, aucune ouverture de menu n’est en cause).

**Mémo oral :** Garder ses commandes et son rythme.

**Fichier final prévu :** `finals/slide-21-checkpoint-3.png`

---

### S22 — Du vrai texte dans le PDF

- **Acte :** 4. Documents PDF
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Comprendre la sélection de texte comme contrôle d’un PDF interne, avec une garantie limitée.
- **Badge :** `R. 240`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ouvrir l’acte Documents PDF en reprenant le geste de l’ouverture.
- Idée principale : Un PDF d’images ne fournit pas un texte manipulable.
- Scène : qui, Odette ; où, à son bureau de préparation ; objet, le programme PDF qu’elle veut annoter et dont elle garde un extrait ; tension, la première version est un scan ; action, elle sélectionne une ligne dans la version avec texte ; résultat, seuls les mots sont surlignés et peuvent être repris.
- Transformation visible : D’une sélection de l’image entière à une sélection de mots.
- Test des trois secondes : « Cette fois, les mots sont sélectionnables. »
- Ajout par rapport à la slide précédente : Du contrôle du navigateur à la matière textuelle d’un PDF interne.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-ODETTE` (Odette).

**Texte visible (projection)**

- `Acte 4 · Documents PDF`
- `Du vrai texte dans le PDF`
- `IMPACT - Une image ne fournit pas de texte manipulable`
- `LIMITE - Sélectionnable ne veut pas dire tout accessible`

**Illustration :** Odette, crayon posé près de sa main, utilise la souris. Deux vues de PDF : à gauche, un rectangle de sélection à poignées entoure toute une page-image ; à droite, un surlignage bleu épouse les lignes d’un texte abstrait. Même document de programme, pas de titres inspectés ni de signets ajoutés. Deux encadrés bas.

**Alternative textuelle à fournir :** Odette compare un programme scanné, sélectionné comme image entière, et sa version avec texte dont elle peut sélectionner une ligne.

**Règle → préjudice utilisateur :** Un PDF purement scanné ne donne pas de texte aux outils pour copier, traduire, indexer ou restituer son contenu.

**Garantie recherchée (matière de l’oral)**

Une manipulation et un accès textuel au moins minimaux, sans équivalence avec l’accessibilité complète du document.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 240 : ouvrir chaque PDF interne, vérifier le texte immédiatement sélectionnable ou consultable par un lecteur d’écran.
- Solution : conversion depuis une source numérique, OCR le cas échéant ; ne pas dire que tout scan est irrémédiablement inutilisable.
- L’expert préfère le HTML lorsque possible et limite la sélection à un indice d’accès minimal. L’OCR et la structure de titres sont deux questions distinctes.

**Discours oral du présentateur (non projeté)**

#### Une image de page n’est pas son texte

- Un scan pur rassemble des images de pages ; les outils ne trouvent pas de texte manipulable.
- Le livre propose une conversion depuis la source numérique, ou une reconnaissance de caractères si nécessaire.
- La vérification consiste à sélectionner le texte immédiatement ou à le consulter au lecteur d’écran.
- Quand c’est possible, le livre préfère le format HTML au PDF pour l’accessibilité.

##### Impact du non-respect

- Copier, traduire, indexer ou faire restituer le texte devient impossible dans un document composé seulement d’images.

##### Ce que garantit la règle

- Un accès textuel minimal ; la structure et les autres propriétés du PDF restent à contrôler.

#### Transition

- Pouvoir sélectionner le texte ne donne pas encore le plan du document.

**Mémo oral :** Du texte sélectionnable, un accès minimal.

**Fichier final prévu :** `finals/slide-22-pdf-texte-selectionnable.png`

---

### S23 — Dans le PDF, rejoindre une section

- **Acte :** 4. Documents PDF
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Distinguer la structure de titres d’un PDF de son apparence et de sa seule sélection.
- **Badge :** `R. 241`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ajouter la navigation au texte manipulable.
- Idée principale : Les titres structurés permettent d’accéder aux sections du PDF.
- Scène : qui, Malik ; où, à une table de la bibliothèque ; objet, le long programme PDF ; tension, le document a du texte mais il faut atteindre une section éloignée ; action, Malik appelle la navigation par titres au clavier ; résultat, son lecteur d’écran rejoint les informations d’inscription.
- Transformation visible : Le texte parcouru en continu devient un document à points d’entrée.
- Test des trois secondes : « Malik peut sauter à la section utile. »
- Ajout par rapport à la slide précédente : Après sélectionner, naviguer dans le document.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `Dans le PDF, rejoindre une section`
- `Inscription`
- `IMPACT - Sans plan, je parcours le document`
- `CONTRÔLE - Vérifier les éléments de structure de titre`

**Illustration :** Malik utilise son clavier à gauche. Le PDF en grand à droite présente un volet de signets issu des titres, organisé avec retraits ; son entrée Inscription rejoint la section correspondante. Le contenu reste en lignes abstraites. Le volet est un moyen de contrôle accepté par le livre, au même titre que l’inspection et la consultation au lecteur d’écran. Un seul mot lisible dans le plan.

**Alternative textuelle à fournir :** Malik utilise la structure de titres du programme PDF pour atteindre directement la section Inscription.

**Règle → préjudice utilisateur :** Sans structure de titres, l’accès direct aux sections du PDF et leur compréhension par les aides techniques sont compromis.

**Garantie recherchée (matière de l’oral)**

Un document structuré qui permet de trouver et de parcourir ses sections.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 241 : styles Titre 1, Titre 2, Titre 3 dans la source bureautique, option PDF balisé ou tagué à l’export ; contrôle des éléments de titres par inspection, lecteur de signets ou lecteur d’écran.
- Trois moyens valables du livre : outil d’inspection du code, lecteur PDF affichant les signets, ou consultation au lecteur d’écran. La scène choisit les signets issus des titres ; aucun de ces moyens n’est déclassé.
- Pas de promesse d’accessibilité globale après un export balisé.

**Discours oral du présentateur (non projeté)**

#### Un document à points d’entrée

- Une structure de titres facilite l’accès direct aux différentes sections du PDF.
- Dans une source bureautique, les styles de titres préparent cette structure.
- L’export doit conserver un PDF balisé ou tagué.
- Le livre propose plusieurs moyens de contrôler les éléments de titres, l’inspection du code, un lecteur PDF affichant les signets, ou la consultation au lecteur d’écran.

##### Impact du non-respect

- Malik perd les accès directs aux sections et doit parcourir davantage de contenu.

##### Ce que garantit la règle

- La présence de titres structurés pour organiser et parcourir le PDF, sans certifier ses autres propriétés.

#### Transition

- Le texte et le plan se vérifient séparément, même dans un seul PDF.

**Mémo oral :** Des titres dans la source, conservés dans le PDF.

**Fichier final prévu :** `finals/slide-23-pdf-structure-titres.png`

---

### S24 — Texte PDF et titres PDF

- **Acte :** 4. Documents PDF
- **Type :** distinction
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Empêcher l’assimilation entre sélection du texte et structure de titres.
- **Badge :** `R. 240 · 241`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Distinguer les deux règles PDF.
- Idée principale : Avoir du texte et offrir un plan sont deux propriétés.
- Scène : qui, Nora ; où, à la table d’accueil ; objet, le même programme PDF ; tension, sélectionner fonctionne, mais aucun titre structuré n’est trouvé ; action, elle essaie la sélection puis consulte le résultat d’inspection ; résultat, un succès ne masque plus le second défaut.
- Transformation visible : Un document textuel révèle une absence de plan à un autre contrôle.
- Test des trois secondes : « Copier fonctionne ; le plan manque encore. »
- Ajout par rapport à la slide précédente : Les deux propriétés du PDF sont mises en regard.

**Référence de composition principale :** `N03`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Texte PDF et titres PDF`
- `Sélection : reprendre les mots`
- `Titres : rejoindre les sections`
- `Du texte ne prouve pas une structure de titres`

**Illustration :** Nora au centre, main sur la souris. Panneau gauche : dans le PDF, des lignes sont surlignées individuellement et rejoignent sa note. Panneau droit : une fiche d’inspection montre une recherche de titres sans résultat, matérialisée par un petit signe d’absence, pas un cadre de liste vide. Le bandeau porte la limite. Aucun mot de diagnostic supplémentaire.

**Alternative textuelle à fournir :** Dans le même PDF, Nora peut sélectionner les mots mais l’inspection ne trouve pas de titres structurés.

**Règle → préjudice utilisateur :** Valider les titres après une simple sélection laisse la navigation au sein du PDF sans preuve.

**Garantie recherchée (matière de l’oral)**

Deux contrôles, deux résultats, aucune conclusion globale sur l’accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Le livre propose au choix inspection, lecteur PDF affichant les signets, ou lecteur d’écran pour vérifier les éléments de titres. Le panneau droit choisit ici l’inspection ; les deux autres voies sont tout aussi valables.
- La sélection ne prouve pas non plus l’exactitude d’une reconnaissance de caractères ; cette qualité n’est pas évaluée ici.

**Discours oral du présentateur (non projeté)**

#### Deux qualités qui se complètent

- Le texte sélectionnable permet une manipulation minimale du contenu.
- La structure de titres donne des points d’entrée dans le document.
- Un PDF peut offrir la première sans la seconde.
- Il faut examiner chacune ; ni un beau titre visuel ni une sélection réussie ne remplace le contrôle de la structure, par inspection, signets ou lecteur d’écran.

#### Transition

- Dans un tableau, le texte a aussi besoin de relations pour devenir compréhensible.

**Mémo oral :** Sélectionner ne prouve pas structurer.

**Fichier final prévu :** `finals/slide-24-distinction-pdf-texte-titres.png`

---

### S25 — Relier la cellule à ses entêtes

- **Acte :** 5. Tableaux
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Expliquer les associations entre cellules et entêtes dans les tableaux de données.
- **Badge :** `R. 242`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Ouvrir l’acte Tableaux par la compréhension d’une cellule.
- Idée principale : Une valeur isolée perd le contexte fourni par ses entêtes.
- Scène : qui, Malik ; où, dans la bibliothèque ; objet, les horaires d’ateliers sous forme de tableau ; tension, il faut comprendre à quoi correspond la cellule entendue ; action, il navigue de cellule en cellule ; résultat, l’entête et la valeur sont restituées ensemble dans la situation corrigée.
- Transformation visible : Une cellule est reliée à l’entête qui lui donne son sens.
- Test des trois secondes : « Le nombre est accompagné de son contexte. »
- Ajout par rapport à la slide précédente : Du plan d’un document aux relations internes d’une grille.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `Acte 5 · Tableaux`
- `Relier la cellule à ses entêtes`
- `« Samedi, 10 h »`
- `IMPACT - Une valeur seule perd son contexte`
- `GARANTIE - Les entêtes accompagnent la cellule`

**Illustration :** Malik à gauche, mains sur le clavier. Un grand tableau de deux colonnes et deux lignes de données est affiché à droite, en blocs abstraits. Une cellule est entourée d’un trait bleu marine ; un trait rejoint son entête, distinguée par une forme et une teinte. Une bulle de restitution porte « Samedi, 10 h ». Elle représente une relation illustrative, pas une annonce universelle de logiciel. Aucun autre nombre dans la grille.

**Alternative textuelle à fournir :** Malik navigue dans les horaires ; une cellule est reliée à son entête et la restitution associe samedi à dix heures.

**Règle → préjudice utilisateur :** Une valeur vocalisée sans ses entêtes peut rendre un tableau clair à l’écran incompréhensible.

**Garantie recherchée (matière de l’oral)**

Permettre aux aides techniques de restituer les relations logiques entre valeurs et entêtes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 242 : th pour les entêtes, scope="col" ou scope="row" pour une colonne ou ligne entière ; id/headers appropriés pour des entêtes ne portant que sur une partie.
- Les derniers tirets du contrôle répètent id/headers sans rappeler la condition ; lire avec les solutions et l’expert, qui autorisent scope sur tableaux simples. Écart de rédaction signalé en vigilance.
- Préférer des tableaux simples, voire morceler un complexe, selon l’expert. L’annonce exacte varie et n’a pas été testée ; seule l’association est illustrée.

**Discours oral du présentateur (non projeté)**

#### Une valeur a besoin de son contexte

- Dans un tableau, les entêtes indiquent ce que signifie chaque donnée.
- Le livre demande de baliser ces entêtes et leur portée.
- Pour un tableau simple, scope relie une entête à toute sa ligne ou sa colonne.
- Les associations plus complexes peuvent demander des identifiants et des références explicites ; l’expert préfère simplifier les tableaux quand c’est possible.

##### Impact du non-respect

- Une succession de valeurs peut devenir incompréhensible au lecteur d’écran.

##### Ce que garantit la règle

- Des relations explicites que les aides techniques peuvent exploiter, sans promettre une annonce identique partout.

#### Transition

- Comprendre une cellule ne dit pas encore quel tableau on vient de rencontrer.

**Mémo oral :** Une cellule se comprend avec ses entêtes.

**Fichier final prévu :** `finals/slide-25-cellules-entetes.png`

---

### S26 — Nommer le tableau entier

- **Acte :** 5. Tableaux
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Comprendre le rôle propre de caption et le contrôle manuel de sa pertinence.
- **Badge :** `R. 243`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Distinguer le nom de l’ensemble de celui des colonnes.
- Idée principale : Le titre permet d’identifier la nature des informations du tableau.
- Scène : qui, Malik ; où, devant les horaires au même bureau ; objet, une page présentant plusieurs tableaux ; tension, il doit choisir le bon ensemble ; action, il parcourt leur liste par son outil ; résultat, un titre pertinent distingue le tableau utile.
- Transformation visible : Un tableau devient identifiable avant de parcourir ses cellules.
- Test des trois secondes : « Il sait quel tableau choisir. »
- Ajout par rapport à la slide précédente : Après le sens d’une cellule, la nature de l’ensemble.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E08`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `Nommer le tableau entier`
- `<caption>Horaires</caption>`
- `IMPACT - Quel tableau contient ce que je cherche ?`
- `CONTRÔLE - Un titre présent, pertinent et restitué`

**Illustration :** Malik sélectionne au clavier un tableau parmi deux vignettes de grille sur son écran. Le tableau visé est relié à la ligne de code caption dans un petit ruban d’inspection, pas à une bulle répétant le mot. Le code montre le titre associé au tableau ; les cellules restent abstraites. Le point d’interrogation de l’encadré reste dans cet encadré, sans bandeau supplémentaire.

**Alternative textuelle à fournir :** Malik identifie le tableau des horaires grâce à un titre caption renseigné ; le code est montré comme extrait de son tableau.

**Règle → préjudice utilisateur :** Sans titre pertinent, identifier la nature des informations d’un tableau devient difficile, notamment dans une liste de tableaux.

**Garantie recherchée (matière de l’oral)**

Nommer chaque tableau de données par un caption pertinent et accessible au lecteur d’écran, visible ou non.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 243 : présence de caption, pertinence et maintien de son accessibilité s’il est masqué par CSS. Présence partiellement automatisable ; pertinence à examiner manuellement.
- Code : extrait caption complet, valide dans son contexte table ; il n’est pas présenté comme un tableau HTML complet.
- Le titre n’est pas une entête de colonne et n’est pas remplacé, dans la solution retenue par le livre, par un simple texte placé au-dessus. Connexe 185 sourcée par le contrôle du caption masqué.

**Discours oral du présentateur (non projeté)**

#### Identifier avant de parcourir

- Un lecteur d’écran peut proposer la liste des tableaux d’une page.
- Leur titre permet de choisir le bon ensemble sans commencer par ses valeurs.
- Le livre utilise caption, éventuellement masqué à l’affichage s’il reste accessible aux lecteurs d’écran.
- Un outil peut détecter sa présence ; sa pertinence exige un examen humain.

##### Impact du non-respect

- La nature du tableau reste difficile à identifier avant sa lecture.

##### Ce que garantit la règle

- Un titre qui décrit les informations du tableau et reste restituable.

#### Transition

- Avant de contrôler une grille, il faut aussi savoir si elle contient des données ou sert à placer des blocs.

**Mémo oral :** Le caption nomme l’ensemble.

**Fichier final prévu :** `finals/slide-26-titre-tableau.png`

---

### S27 — L’ordre doit tenir sans les colonnes

- **Acte :** 5. Tableaux
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Identifier un tableau de mise en page et vérifier sa linéarisation.
- **Badge :** `R. 244`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Faire entendre la lecture d’une ancienne mise en page.
- Idée principale : Des blocs placés en colonnes doivent conserver leur sens dans l’ordre du code.
- Scène : qui, Malik ; où, à la bibliothèque ; objet, une page archivée présentant Reliure et Photo en deux colonnes par un tableau de mise en page ; tension, l’ordre linéaire sépare les noms de leurs descriptions ; action, Malik écoute l’ordre des blocs au clavier ; résultat, les deux noms se suivent avant les deux descriptions, les paires sont perdues.
- Transformation visible : Deux couples verticaux deviennent une suite dans un ordre incohérent.
- Test des trois secondes : « Ce qui allait ensemble est séparé dans l’ordre de lecture. »
- Ajout par rapport à la slide précédente : Du tableau de données au tableau utilisé pour disposer la page.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-MALIK` (Malik).

**Texte visible (projection)**

- `L’ordre doit tenir sans les colonnes`
- `Reliure`
- `Photo`
- `IMPACT - Les descriptions perdent leur atelier`
- `CONTRÔLE - Linéariser et relire le sens`

**Illustration :** Malik au clavier, casque gris clair. À gauche, la page archivée montre deux colonnes : Reliure au-dessus de sa description, Photo au-dessus de la sienne. Chaque nom porte une pastille distinctive, ronde à hachures obliques pour Reliure, carrée à points pour Photo ; la description associée porte le même motif. À droite, une suite liée au casque se lit verticalement : pastille ronde seule, pastille carrée seule, bloc descriptif hachuré, bloc descriptif pointillé. Les mots Reliure et Photo ne sont écrits que dans la page initiale ; la suite emploie seulement les formes et motifs correspondants. Ainsi les associations initiales et leur séparation restent visibles sans répétition de texte ni couleur seule. L’outil de linéarisation est expliqué à l’oral, pas manipulé par un autre personnage hors image.

**Alternative textuelle à fournir :** Malik écoute une page mise en colonnes : les noms Reliure et Photo sont suivis seulement ensuite de leurs descriptions. Formes et motifs montrent les deux associations séparées par cet ordre.

**Règle → préjudice utilisateur :** L’ordre du code peut rendre incompréhensible une disposition pourtant claire à l’écran.

**Garantie recherchée (matière de l’oral)**

Conserver un contenu compréhensible quand la mise en forme par tableau n’est pas restituée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 244 : tableau de mise en forme sans données liées à des entêtes ; linéariser et vérifier l’absence d’incohérence ou de perte.
- Solution du livre : regrouper dans une même cellule les informations verticalement associées. Ne pas condamner tout tableau de mise en page par ce seul libellé.
- L’expert situe surtout le cas dans des pages anciennes ; ce n’est pas une recommandation de bâtir les nouvelles pages avec des tableaux. Les titres et descriptions de la scène sont des contenus, pas des entêtes de données.

**Discours oral du présentateur (non projeté)**

#### Lire dans l’ordre du code

- Une ancienne page peut utiliser des cellules pour placer deux contenus côte à côte.
- L’aide technique peut les restituer linéairement dans l’ordre du code.
- Si les noms arrivent tous avant leurs descriptions, leurs associations deviennent difficiles à suivre.
- Le livre propose de regrouper dans une même cellule ce qui doit rester verticalement associé.

##### Impact du non-respect

- L’ordre linéaire casse le sens des contenus.

##### Ce que garantit la règle

- Une lecture compréhensible même sans la disposition initiale du tableau de mise en page.

#### Transition

- Pour de véritables données, le risque inverse existe : une grille dessinée sans tableau.

**Mémo oral :** L’ordre du code doit garder le sens.

**Fichier final prévu :** `finals/slide-27-linearisation-mise-en-page.png`

---

### S28 — Une grille dessinée ne suffit pas

- **Acte :** 5. Tableaux
- **Type :** règle
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Reconnaître un tableau de données simulé et connaître le balisage attendu.
- **Badge :** `R. 245`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : Revenir aux données et à leur structure réelle.
- Idée principale : Des colonnes de texte alignées par des pipes ne fournissent pas un tableau exploitable.
- Scène : qui, Samuel ; où, au bureau éditorial ; objet, des horaires saisis en texte avec des pipes dans un document ; tension, il pourrait les publier tels quels ; action, il publie à la place les données dans un vrai tableau ; résultat, la page fournit des cellules et leurs relations aux outils.
- Transformation visible : Des lignes de texte sélectionnables sont remplacées par de vraies cellules HTML.
- Test des trois secondes : « Il publie des cellules, pas des colonnes de texte. »
- Ajout par rapport à la slide précédente : Le tableau de mise en page était réel ; ici le tableau de données manque.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Une grille dessinée ne suffit pas`
- `Texte aligné`
- `Tableau HTML`
- `IMPACT - La grille n’est pas exploitable comme tableau`
- `GARANTIE - Les données ont de vraies cellules`

**Illustration :** Samuel à gauche reprend les horaires d’un document textuel. Dans le panneau Texte aligné, des lignes de blocs abstraits sont disposées en colonnes séparées par des barres verticales dessinées ; une sélection bleue épouse une partie de ligne et un caret dessiné marque une position dans le texte. Dans le panneau Tableau HTML, une seule cellule est sélectionnée et reliée à son entête. Aucun contour d’image, aucune pixellisation, aucune poignée d’angle : les deux supports contiennent du texte. Pas de catalogue de balises en scène principale.

**Alternative textuelle à fournir :** Samuel remplace des horaires en texte aligné par pipes par un tableau HTML aux cellules et entêtes exploitables.

**Règle → préjudice utilisateur :** Une image ou des espaces alignés n’exposent pas les relations d’un tableau aux aides techniques et à l’indexation.

**Garantie recherchée (matière de l’oral)**

Publier les tableaux de données avec table et les éléments associés demandés par le livre.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Livre 245 : pas de tableau de données en image ; vérifier table, tr, td, th et caption pour les contenus reliant données et entêtes.
- Les colonnes simulées par espaces insécables ou pipes sont visées. Une simple liste alignée n’est pas automatiquement un tableau de données.
- Les deux panneaux sont textuels : aucun défaut de texte remplacé par une image ne peut être retenu. Le livre vise aussi les captures, sans que cette scène les emploie. Une alternative à une capture ne dispense pas du vrai tableau ; l’expert conseille de le publier directement. Les liens avec 242 et 243 sont internes à la rubrique, sans prétendre rendre leurs contrôles interchangeables.

**Discours oral du présentateur (non projeté)**

#### Publier les relations, pas seulement la forme

- Des horaires saisis en colonnes avec des séparateurs restent du texte, sans cellules de tableau HTML.
- Les alignements par espaces ou caractères graphiques posent le même problème de structure.
- Le livre demande de baliser les tableaux de données avec les éléments adaptés.
- Il conseille de publier directement le tableau plutôt que de fabriquer l’alternative d’une image de tableau.

##### Impact du non-respect

- Les outils ne disposent pas d’un tableau de données exploitable et compréhensible.

##### Ce que garantit la règle

- La présence d’un vrai tableau de données ; ses titres et ses relations restent à contrôler précisément.

#### Transition

- Un tableau de mise en page et un tableau simulé demandent donc deux diagnostics différents.

**Mémo oral :** Des données tabulaires, un vrai tableau.

**Fichier final prévu :** `finals/slide-28-tableaux-non-simules.png`

---

### S29 — Mise en page ou données simulées

- **Acte :** 5. Tableaux
- **Type :** distinction
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Distinguer la fonction d’un tableau existant de l’absence de tableau pour des données.
- **Badge :** `R. 244 · 245`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Distinguer les deux dernières règles de la rubrique.
- Idée principale : Dans un cas le tableau existe pour placer des blocs ; dans l’autre il manque pour représenter des données.
- Scène : qui, Samuel ; où, devant deux pages du site au bureau ; objet, une page archivée en colonnes et des horaires textuels alignés par pipes ; tension, les deux ressemblent à des grilles ; action, il linéarise la première et inspecte la seconde ; résultat, deux contrôles différents.
- Transformation visible : Deux grilles apparemment proches révèlent deux objets.
- Test des trois secondes : « Tableau pour disposer, ou texte aligné à la place d’un tableau. »
- Ajout par rapport à la slide précédente : La forme de grille ne décide pas de la règle.

**Référence de composition principale :** `N03`. Étalon du masque après validation : `E17`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Mise en page ou données simulées`
- `Tableau pour placer des blocs`
- `Texte aligné sans cellules`
- `Linéariser la mise en page, baliser les données`

**Illustration :** Samuel entre deux panneaux. Gauche : une ancienne page en deux colonnes de blocs d’atelier se déroule en une bande linéaire ; une main accompagne ce déroulé. Droite : il sélectionne une partie de ligne dans les horaires textuels, avec caret et séparateurs dessinés. Chaque panneau est titré, aucun code, aucun autre texte. Bandeau bas sur les deux gestes.

**Alternative textuelle à fournir :** Samuel linéarise un tableau qui place des contenus et repère du texte aligné qui simule un tableau de données.

**Règle → préjudice utilisateur :** Confondre ces objets conduit à exiger des entêtes de données pour une mise en page, ou à ignorer une simulation.

**Garantie recherchée (matière de l’oral)**

Identifier la fonction du contenu avant de choisir le contrôle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Données : valeurs liées à des entêtes ; mise en page : blocs disposés sans cette relation, selon le livre.
- 242 et 243 restent distinguées dans S25 et S26 : entêtes pour les cellules, caption pour la nature de l’ensemble. Cette comparaison ne les remplace pas.

**Discours oral du présentateur (non projeté)**

#### La fonction décide du contrôle

- Le tableau de mise en page sert à disposer des blocs ; il faut vérifier leur sens après linéarisation.
- Les horaires textuels alignés remplacent un tableau de données ; il faut publier les relations dans un vrai tableau.
- Une grille visible ne suffit à identifier ni la technique ni la fonction.
- L’examen du contenu et du code permet de les départager.

#### Transition

- Les tableaux de données demandent encore de distinguer le titre de l’ensemble et les entêtes des cellules.

**Mémo oral :** D’abord la fonction, ensuite le contrôle.

**Fichier final prévu :** `finals/slide-29-distinction-mise-en-page-simulation.png`

---

### S30 — Checkpoint 4 : tableaux

- **Acte :** 5. Tableaux
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** Rattacher les quatre règles de tableaux à des constats ciblés.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Réactiver les quatre règles de tableaux.
- Idée principale : Objet, relation, nom et ordre ne se corrigent pas par le même geste.
- Scène : qui, Samuel ; où, à la table de préparation ; objet, quatre constats ; tension, tous concernent des grilles ; action, il les associe à quatre fiches de contrôle ; résultat, aucune réponse visible.
- Transformation visible : Quatre grilles deviennent quatre diagnostics.
- Test des trois secondes : « Quatre constats, quatre règles à distinguer. »
- Ajout par rapport à la slide précédente : Les quatre règles sont rapprochées dans un exercice unique.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Checkpoint 4 : tableaux`
- `Quel contrôle précis échoue ?`
- `A. Entêtes non reliées`
- `B. Vrai tableau, aucun caption`
- `C. Mise en page : ordre perdu`
- `D. Données en texte à pipes`

**Illustration :** Quatre cartes A à D au-dessus de la table, chacune titrée. Samuel feuillette son carnet. Les objets sont respectivement une cellule et sa colonne, une grille sans nom propre, une page en colonnes déroulée, du texte sélectionné entre des séparateurs verticaux dessinés. Aucun code extrait, coche, croix ou réponse visible.

**Alternative textuelle à fournir :** Quatre constats : relations aux entêtes absentes, caption absent, ordre perdu après linéarisation d’une mise en page, données en texte aligné par pipes.

**Règle → préjudice utilisateur :** Confondre les contrôles peut laisser des cellules sans sens ou des données inexploitées.

**Garantie recherchée (matière de l’oral)**

Nommer le défaut ciblé et choisir son contrôle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 40 secondes de réflexion, 40 secondes de correction.
- Question ouverte sur le contrôle spécifique, sans paire de réponses. A et B concernent de vrais tableaux HTML ; C un tableau de mise en page ; D des horaires textuels alignés par pipes, avec sélection de mots et caret ; aucun contenu n’est une image. Les constats projetés sont les défauts à rattacher, les notes n’en ajoutent aucun.
- Convention pédagogique annoncée avec la question : répondre par le contrôle qui traite précisément la relation, le titre, l’ordre ou la simulation observés. Le contrôle général de 245 recoupe th et caption ; une réponse argumentée à ce niveau général doit être affinée vers le contrôle spécifique, pas rejetée comme factuellement fausse. Aucune exclusivité normative inventée.

**Discours oral du présentateur (non projeté)**

#### Quatre questions sur les grilles

- Les entêtes donnent leur contexte aux cellules.
- Le titre permet d’identifier la nature du tableau.
- L’ordre linéaire doit conserver le sens d’une mise en page.
- Les données doivent être publiées comme un tableau, avec de vraies cellules.

#### Transition

- Ces relations prolongent des exigences déjà rencontrées dans les formulaires et les contenus masqués.

**Corrigé (notes du présentateur, non projeté) :** A → 242 : contrôle spécifique des relations cellule-entêtes (distracteur 243 : titre du tableau, autre objet). B → 243 : contrôle spécifique de présence de caption dans un vrai tableau (distracteur 244 : aucun ordre de mise en page n’est examiné). C → 244 : perte de sens à la linéarisation d’un tableau de mise en page (distracteur 245 : ce n’est pas une simulation de données). D → 245 : tableau de données simulé par du texte et des pipes (distracteur 244 : aucune mise en page linéarisée). Les contrôles de 242 et 243 précisent ceux que 245 récapitule ; la question porte sur cette précision, sans prétendre rendre leurs champs disjoints.

**Mémo oral :** Cellule, ensemble, ordre, structure.

**Fichier final prévu :** `finals/slide-30-checkpoint-4.png`

---

### S31 — Des relations au-delà de la rubrique

- **Acte :** 6. S’entraîner
- **Type :** transversalité
- **Durée indicative :** 1:00
- **Objectif pédagogique :** Relier seulement deux règles connexes explicitement appuyées par le livre.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Relier les usages sans ajouter de nouveaux apprentissages non sourcés.
- Idée principale : Les associations et la restitution ne s’arrêtent pas aux frontières des rubriques.
- Scène : qui, Samuel ; où, au bureau ; objet, une étiquette de formulaire et un titre de tableau masqué ; tension, les deux relations doivent rester exploitables ; action, il vérifie la cible du champ et la restitution du titre ; résultat, deux contrôles complémentaires sur la même page.
- Transformation visible : Les propriétés de la rubrique sont reliées à deux exigences voisines.
- Test des trois secondes : « Relier un champ, rendre son information disponible. »
- Ajout par rapport à la slide précédente : Les tableaux et les identifiants rejoignent Formulaires et Présentation.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-SAMUEL` (Samuel).

**Texte visible (projection)**

- `Des relations au-delà de la rubrique`
- `236 → 69 · Champ et étiquette`
- `243 → 185 · Titre masqué, restitué`

**Illustration :** Samuel assis montre deux zones sur la même page agrandie : en haut un champ et son étiquette reliés par une ligne unique ; plus bas un tableau et son titre représenté en cartouche pointillé hors de l’affichage, relié à une restitution audio abstraite. Les deux lignes de relation sont placées sous chaque zone, sans créer de badge. Aucun diagnostic automatique pour les deux règles à partir d’un seul constat.

**Alternative textuelle à fournir :** Samuel vérifie une association champ-étiquette puis un titre de tableau masqué qui doit rester restituable au lecteur d’écran.

**Règle → préjudice utilisateur :** Une association ambiguë ou un titre masqué pour tous peut priver l’utilisateur d’une information nécessaire.

**Garantie recherchée (matière de l’oral)**

Conserver les associations et l’accès aux informations utiles ; chaque règle garde son contrôle propre.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Lien 236 → 69 : avis de l’expert sur les id et l’association des champs à leurs étiquettes. Lien 243 → 185 : contrôle du caption masqué qui doit rester accessible aux lecteurs d’écran.
- Libellés exacts récupérés par MCP le 8 novembre 2026, source local, instantané 2026-09-03 ; voir Sources et couverture.
- Aucune autre règle connexe n’est introduite sur simple intuition. Le livre peut évoquer l’indexation sans autoriser un nouveau lien numéroté non sourcé.

**Discours oral du présentateur (non projeté)**

#### Deux liens concrets entre rubriques

- L’avis sur les identifiants rappelle que les lecteurs d’écran en dépendent pour relier les champs à leurs étiquettes.
- Cela rejoint la règle des formulaires qui demande à chaque champ une étiquette propre dans le code.
- Le contrôle du titre de tableau demande de vérifier sa restitution quand il est masqué à l’affichage.
- Cela rejoint la règle de présentation qui protège les contenus destinés au lecteur d’écran.
- Ces rapprochements n’assimilent pas les contrôles : un même constat ne prouve pas automatiquement deux défauts.

#### Transition

- La précision du constat reste la meilleure protection contre les confusions.

**Mémo oral :** Relier les règles, conserver leurs preuves.

**Fichier final prévu :** `finals/slide-31-transversalite.png`

---

### S32 — Évaluation 1/2

- **Acte :** 6. S’entraîner
- **Type :** évaluation
- **Durée indicative :** 1:45
- **Objectif pédagogique :** Appliquer les contrôles de date, de menu contextuel, de portée des entêtes et de pertinence du titre à quatre situations nouvelles.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Première moitié des huit questions finales.
- Idée principale : Quatre questions ouvertes, sans liste de choix ; chaque fait projeté apporte sa preuve.
- Scène : qui, Odette ; où, à la table de bibliothèque ; objet, quatre nouvelles fiches d’inspection ; tension, une information présente peut être erronée et une commande au clavier peut être interceptée ; action, elle note la règle et le fait probant ; résultat, réponses gardées dans le carnet.
- Transformation visible : Des règles rencontrées deviennent des décisions personnelles.
- Test des trois secondes : « Quatre nouveaux constats à justifier. »
- Ajout par rapport à la slide précédente : Début de l’évaluation après les liens transversaux.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-ODETTE` (Odette).

**Texte visible (projection)**

- `Évaluation 1/2`
- `Quelle règle est prouvée enfreinte ?`
- `1. datetime publié 8/11/26`
- `2. Article, menu contextuel bloqué`
- `3. Colonne, scope row`
- `4. Budget, caption Horaires`

**Illustration :** Quatre cartes numérotées, deux rangées. Odette écrit au crayon devant le portable. Vignettes : notice datée et calendrier ; clavier devant un article et geste d’appel des actions contextuelles ; tableau dont les colonnes sont repérées par une portée horizontale ; budget à valeurs monétaires et titre d’horaires. Seules les chaînes de la liste sont lisibles. Les expressions datetime et scope sont des constats de valeur en langage courant, pas du code HTML tronqué. Aucune coche, croix, réponse ni numéro de règle.

**Alternative textuelle à fournir :** Quatre nouveaux constats : date de publication au format non standard, menu contextuel bloqué au clavier sur un article, portée row sur des entêtes de colonnes, titre Horaires sur un budget.

**Règle → préjudice utilisateur :** Une valeur renseignée peut rester inexploitable ; le clavier doit aussi donner accès aux actions contextuelles.

**Garantie recherchée (matière de l’oral)**

Fonder chaque réponse sur le résultat du contrôle désigné.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : une réponse écrite et un fait probant par item ; aucune paire ni choix annoncé. 55 secondes de réflexion et 50 de correction, celle-ci peut suivre S33 dans les durées cumulées.
- Q1 : seule date de publication fournie sous forme programmatique ; la valeur 8/11/26 est le constat, aucun schema.org correct ne la supplée. Q2 : l’appel clavier du menu contextuel est intercepté dans un article éditorial ordinaire, pas une application à menu spécifique ; le texte projeté donne le blocage. Ce mode d’appel diffère du geste de pointeur des checkpoints. L’unicité est déplacée vers le repère 4 du grand cas, dans une seule page.
- Q3 : tableau simple réel, entêtes de colonnes entières ; row est la valeur scope observée, pas une absence de tableau. Q4 : vrai tableau de budget avec caption existant, accessible, mais non pertinent. Pour Q3 et Q4, la réponse spécifique du livre porte sur les associations et sur la pertinence ; une simulation n’est pas constatée.
- L’absence de structure PDF n’est plus un item de S32 ; les trois moyens de contrôle de 241 sont développés en S23-S24 et utilisés dans le grand cas.

**Discours oral du présentateur (non projeté)**

#### Présent ne veut pas dire pertinent

- Une date fournie dans le code doit respecter un format exploitable.
- Le menu contextuel doit rester accessible aussi lorsqu’il est appelé au clavier.
- La portée d’une entête doit correspondre à la relation réelle avec les cellules.
- Le titre d’un tableau doit décrire la nature de ses informations.

#### Transition

- La précision des valeurs compte autant que l’existence des éléments.

**Corrigé (notes du présentateur, non projeté) :** Q1 → 231 : datetime 8/11/26 ne respecte pas le format standard de date, aucune autre forme appropriée dans ce cas (distracteur 232 : rien sur le codage). Q2 → 238 : accès au menu contextuel bloqué par interception de son appel clavier sur un article ordinaire (distracteur 237 : aucune commande Copier éprouvée). Q3 → 242 : scope row ne décrit pas les entêtes de colonnes entières du tableau simple (distracteur 243 : aucun défaut de titre établi). Q4 → 243 : le caption Horaires ne décrit pas les informations budgétaires (distracteur 242 : les associations sont un autre contrôle). Pas de simulation prouvée ; pas de choix à lire avant réponse.

**Mémo oral :** Vérifier la valeur, pas seulement la présence.

**Fichier final prévu :** `finals/slide-32-evaluation-1.png`

---

### S33 — Évaluation 2/2

- **Acte :** 6. S’entraîner
- **Type :** évaluation
- **Durée indicative :** 1:45
- **Objectif pédagogique :** Examiner quatre situations nouvelles de mise en page, texte PDF, valeur de métadonnée et cohérence de transmission.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Seconde moitié des huit questions finales.
- Idée principale : Chaque cas donne un autre échec de contrôle, sans reproduire un item de checkpoint.
- Scène : qui, Nora ; où, à la table de bibliothèque ; objet, quatre dossiers nouveaux, fiches de prestations et tarifs, PDF reçu, métadonnée et transmission ; tension, le rendu peut masquer la perte des relations ou du texte ; action, elle justifie quatre rattachements ; résultat, ses réponses restent hors projection.
- Transformation visible : Quatre inspections nouvelles fournissent quatre faits précis à rattacher.
- Test des trois secondes : « Quatre autres questions, sans réponse visible. »
- Ajout par rapport à la slide précédente : Complément de l’évaluation avant le cas intégrateur.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E16`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Évaluation 2/2`
- `Quelle règle est prouvée enfreinte ?`
- `5. Tableau de mise en page, prix à part`
- `6. PDF : titres balisés, scan`
- `7. Meta charset vide`
- `8. UTF-8, HTTP Latin-1`

**Illustration :** Quatre cartes 5 à 8, même composition que S32. Nora écrit. Carte 5 : deux fiches de prestations associées chacune à leur prix dans la page initiale, puis ordre linéaire regroupant les deux prestations avant les prix ; motifs appariés sans texte ajouté. Carte 6 : PDF interne à titres structurés et sélectionnables ; son texte de corps est scanné, sélectionné comme image. Aucun tableau ni liste dans ce corps. Carte 7 : loupe sur une zone de valeur meta effectivement laissée vide, sans suggérer une carte de gabarit. Carte 8 : fichier et entête de transmission rapprochés. Aucun autre texte, coche, croix ou réponse.

**Alternative textuelle à fournir :** Constats nouveaux : un tableau de mise en page sépare prestations et prix après linéarisation, un PDF à titres structurés mais au corps scanné, une meta charset vide et un contenu UTF-8 servi sous déclaration HTTP Latin-1.

**Règle → préjudice utilisateur :** Une ressemblance de symptôme ne permet pas de conclure sur le mécanisme.

**Garantie recherchée (matière de l’oral)**

Retenir la fonction ou la structure directement éprouvée par le constat.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : répondre sans choix annoncé ; 55 secondes de réflexion et 50 de correction. Les réponses aux huit questions peuvent être corrigées ensemble après S33.
- Q5 : le constat projeté nomme explicitement un tableau de mise en page, sans entêtes de données ; le résultat de linéarisation dessiné dissocie chaque prestation de son prix. Q6 : PDF interne avec structure de titres correcte et texte de titres sélectionnable, mais paragraphes du corps seulement en images, sans couche de texte ni restitution textuelle. « titres balisés » désigne explicitement une structure correcte, représentée dans la vignette ; ce n’est pas un PDF entièrement scanné. Le défaut porte seulement sur le texte du corps. Aucun constat de défaut de titres ne peut en être déduit.
- Q7 : meta de déclaration du jeu de caractères présente mais valeur vide ; le codage réel n’est pas fourni, donc ne pas conclure sur UTF-8 effectif. Q8 : contenu réellement UTF-8 mais entête HTTP annonçant Latin-1, établis par inspection ; la meta n’est pas observée. Les deux items ne refont ni une meta absente ni le contenu réellement non UTF-8 du checkpoint : ici le contenu est bien UTF-8, c’est l’entête qui le contredit.
- Nouvelles mises à l’épreuve : sens perdu dans l’ordre de fiches, corps scanné malgré des titres structurés, pertinence de la valeur et contradiction de transmission. Aucun couple de règles proposé avant réponse.

**Discours oral du présentateur (non projeté)**

#### Les objets gardent chacun leur contrôle

- L’ordre linéaire doit conserver les associations utiles d’une mise en page.
- Le PDF a déjà ses titres structurés ; ses paragraphes scannés ne fournissent pourtant pas de texte manipulable. Cette image du corps ne prouve aucun défaut de titres, qui sont contrôlés séparément.
- Une métadonnée vide ne définit aucun jeu de caractères.
- Le codage annoncé et le contenu transmis doivent rester cohérents avec l’usage réel d’UTF-8.

#### Transition

- Plusieurs de ces difficultés peuvent se rencontrer dans une seule consultation.

**Corrigé (notes du présentateur, non projeté) :** Q5 → 244 : la linéarisation du tableau de mise en page sépare les prestations de leurs prix (distracteur 245 : un tableau de mise en page existe, ce n’est pas une grille simulée). Q6 → 240 : le corps du PDF interne reste une image sans texte, malgré des titres correctement structurés (distracteur 241 : structure de titres explicitement correcte ; aucune seconde réponse). Q7 → 232 : la valeur vide de la meta ne définit aucun jeu de caractères (distracteur 233 : l’encodage réel est inconnu). Q8 → 233 : contenu UTF-8 servi sous entête HTTP Latin-1, incohérence établie par le premier et le troisième temps du contrôle du livre (distracteur 232 : présence et valeur de meta non examinées). Aucun choix à annoncer avant réponse.

**Mémo oral :** Une inspection précise borne la conclusion.

**Fichier final prévu :** `finals/slide-33-evaluation-2.png`

---

### S34 — Grand cas : trouvez sept défauts

- **Acte :** 6. S’entraîner
- **Type :** grand cas
- **Durée indicative :** 3:00
- **Objectif pédagogique :** Combiner sept observations sur une page et son PDF, sans extrapoler.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Cas intégrateur sans personnage, exception déclarée.
- Idée principale : Sept défauts indépendants se découvrent dans les objets, les extraits et les gestes, sans notification qui les nomme.
- Scène : qui, aucun personnage ; où, consultation du programme ; objet, site éditorial, note de citation et PDF textuel ; tension, sept relations ou fonctions sont défaillantes ; action, plan, source, copie, attributs et balises sont montrés ; résultat, sept observations brutes restent sans leurs réponses.
- Transformation visible : Même scène que la correction, sans ses sept repères.
- Test des trois secondes : « Une vraie page et son PDF à examiner, pas une liste de réponses. »
- Ajout par rapport à la slide précédente : Des constats séparés à une consultation unique.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E35`. Aucun personnage, aucune ancre de personnage.

**Fabrication :** édition du PNG validé de S35, retrait des seuls repères, titre et pagination remplacés ; voir Fabrication du grand cas.

**Texte visible (projection)**

- `Grand cas : trouvez sept défauts`
- `h1`
- `h3`
- `<p>• A<br>• B</p>`
- `Ctrl`
- `C`
- `V`
- `id=a`
- `id="a"`
- `<meta http-equiv=refresh content=5>`
- `Jour|h`
- `Sam|9`
- `pre`
- `P`

**Illustration :** Aucun personnage. Une seule consultation : site à gauche (52 %), colonne libre au centre (21 %), PDF interne à droite (27 %). La page comporte navigation en barres, vignette d’atelier et sections en blocs abstraits. Sept états s’y observent. (1) Le plan complet extrait présente h1 puis h3 en retrait. (2) Les puces de matériel sont reliées à `<p>• A<br>• B</p>`, fragment complet sans rôles ARIA. (3) Deux lignes HTML sélectionnées sont bleues ; le raccourci de copie puis de collage utilise les trois touches Ctrl, C et V, la première commune et maintenue. La note contient un grand motif orange à losanges, identique au dessin antérieur du presse-papiers, nettement différent des lignes sélectionnées. (4) Dans la même vue source, deux blocs éditoriaux distincts portent les propriétés id=a et id="a", alignées côte à côte ; aucun champ de formulaire. (5) Le ruban head contient `<meta http-equiv=refresh content=5>`. (6) Les horaires Jour|h puis Sam|9 forment deux lignes de texte avec un caret dessiné ; un surlignage épouse quelques caractères. L’inspecteur les rattache au nœud pre, contenant seulement ce texte. (7) Le PDF possède un titre et des intertitres visuels, quelques mots surlignés et une arborescence complète de balises ; une branche P remplie regroupe tous les paragraphes, y compris ces titres visuels, reliés par des traits fins. Autres contenus abstraits. Les chiffres entre parenthèses décrivent l’ordre de conception et ne sont pas projetés.

**Consigne propre à S34 :** aucune pastille, aucun trait de correction, aucune étiquette de réponse. Les traits d’inspection internes à la scène restent.

**Alternative textuelle à fournir :** Page Programme et PDF textuel : plan h1 puis h3, puces dans p, collage de l’ancien dessin du presse-papiers, même valeur id sur deux éléments de la même page, meta refresh, horaires textuels à pipes dans pre, titres visuels du PDF rattachés aux paragraphes P. Rattachements cachés.

**Règle → préjudice utilisateur :** Accumuler ces défauts retire des moyens de se repérer, de lire à son rythme et de réutiliser le programme.

**Garantie recherchée (matière de l’oral)**

Rattacher seulement les sept constats aux usages et contrôles qui les étayent.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : trois minutes pour relever sept défauts et proposer un contrôle ou remède ; correction en S35, 1:45.
- Scénario fictif, pas audit réel. Sept signes positifs : niveaux sautés, balisage p, motif collé distinct, même valeur id sur deux éléments de la page, meta refresh, texte dans pre, titres visuels rattachés à P. Aucune réponse ne repose sur une note inchangée, un menu absent ou un volet vide.
- Le plan contient tous les titres masqués et générés. Le fragment p contient toute la liste, sans rôles ARIA. Les deux relevés id sont des attributs de deux blocs différents, pas deux références vers une même cible, pas deux pages et pas des relations champ-étiquette. Leur valeur est a dans les deux écritures ; les guillemets ne la changent pas. Les deux propriétés forment une seule rangée de la vue source, sans balises HTML tronquées.
- Le collage insère l’ancien dessin du presse-papiers après le geste Ctrl avec C puis V ; la commande courante n’a pas repris le texte sélectionné. Le dessin collé est présent et grand ; pas de déduction depuis une absence ou une différence minuscule. Les losanges et la forme distinguent les objets, pas seulement la couleur. L’appel du menu n’est pas représenté ; il est évalué en S32 Q2.
- La meta refresh est un mécanisme que le livre demande de ne pas utiliser. Le nœud pre ne contient que les caractères des horaires : sélection textuelle et caret prouvent ici une représentation textuelle, pas une image. Les pipes sont des caractères ASCII ordinaires ; les jours et heures sont bien des données liées à des entêtes. Ni rôle de tableau, ni balisage table dans ce contenu inspecté complet. Ne pas ajouter des défauts de caption ou d’associations à ce seul défaut de simulation.
- Le PDF contient du vrai texte sélectionnable. Son arborescence complète est remplie de paragraphes sous P ; des traits rattachent positivement ses titres visuels à ce type de balise. Le défaut n’est pas déduit d’un panneau vide. Inspection choisie parmi les trois moyens valables du livre ; signets et lecteur d’écran restent admis. Aucun défaut de texte sélectionnable n’est montré.
- Hors preuve : date, métadonnée de caractères, UTF-8 réel, menu, associations et titre d’un vrai tableau, ordre d’un tableau de mise en page, accessibilité globale. Sept remèdes indépendants ; l’identifiant des blocs ne sert à aucune autre relation de l’exercice.
- Acceptation future : inspection côte à côte, puis recherche des sept défauts sur la scène nue par une personne ignorant le corrigé. Non réalisé ici. Rejeter tout état illisible ; ne pas le sauver par une notification qui nomme la réponse.

**Discours oral du présentateur (non projeté)**

#### Une page et son document

- Le programme se consulte dans le site et dans un PDF textuel.
- Le plan, la liste et les extraits montrent des propriétés distinctes.
- Le collage montre un ancien dessin au lieu du passage sélectionné ; deux blocs portent le même identifiant.
- Les horaires restent du texte aligné ; les titres visuels du PDF sont rattachés à des paragraphes.
- Le code et les balises PDF fournissent d’autres observations ; ils ne se déduisent pas de la beauté du document.

#### Transition

- Chaque observation doit maintenant être reliée à son défaut précis.

**Corrigé (notes du présentateur, non projeté) :** Sept réponses en S35 ; aucune réponse projetée ici.

**Mémo oral :** Observer, rattacher, ne pas extrapoler.

**Fichier final prévu :** `finals/slide-34-grand-cas.png`

---

### S35 — Correction

- **Acte :** 6. S’entraîner
- **Type :** correction projetée
- **Durée indicative :** 1:45
- **Objectif pédagogique :** Nommer et rattacher les sept constats sans modifier la scène.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : Correction projetée et premier étalon à fabriquer.
- Idée principale : Sept observations correspondent à sept défauts distincts dans le périmètre retenu.
- Scène : qui, aucun personnage ; où, même consultation qu’en S34 ; objet, même page et même PDF ; tension, chaque observation doit être rattachée ; action, sept pastilles et traits sont ajoutés vers les étiquettes ; résultat, les sept réponses sont projetées sans déplacer les objets.
- Transformation visible : La consultation inchangée reçoit sept repères.
- Test des trois secondes : « Sept constats, sept rattachements. »
- Ajout par rapport à la slide précédente : Les réponses du grand cas, et uniquement elles.

**Référence de composition principale :** `S20`. Étalon du masque après validation : `E35`. Aucun personnage, aucune ancre de personnage.

**Fabrication :** cinquième étalon, première image à fabriquer après verrouillage ; son PNG validé sert à produire S34.

**Texte visible (projection)**

- `Correction`
- `h1`
- `h3`
- `<p>• A<br>• B</p>`
- `Ctrl`
- `C`
- `V`
- `id=a`
- `id="a"`
- `<meta http-equiv=refresh content=5>`
- `Jour|h`
- `Sam|9`
- `pre`
- `P`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `Plan 234`
- `Liste 235`
- `Copie 237`
- `Id 236`
- `Meta 239`
- `Texte 245`
- `PDF 241`

**Illustration :** Aucun personnage. Une seule consultation : site à gauche (52 %), colonne libre au centre (21 %), PDF interne à droite (27 %). La page comporte navigation en barres, vignette d’atelier et sections en blocs abstraits. Sept états s’y observent. (1) Le plan complet extrait présente h1 puis h3 en retrait. (2) Les puces de matériel sont reliées à `<p>• A<br>• B</p>`, fragment complet sans rôles ARIA. (3) Deux lignes HTML sélectionnées sont bleues ; le raccourci de copie puis de collage utilise les trois touches Ctrl, C et V, la première commune et maintenue. La note contient un grand motif orange à losanges, identique au dessin antérieur du presse-papiers, nettement différent des lignes sélectionnées. (4) Dans la même vue source, deux blocs éditoriaux distincts portent les propriétés id=a et id="a", alignées côte à côte ; aucun champ de formulaire. (5) Le ruban head contient `<meta http-equiv=refresh content=5>`. (6) Les horaires Jour|h puis Sam|9 forment deux lignes de texte avec un caret dessiné ; un surlignage épouse quelques caractères. L’inspecteur les rattache au nœud pre, contenant seulement ce texte. (7) Le PDF possède un titre et des intertitres visuels, quelques mots surlignés et une arborescence complète de balises ; une branche P remplie regroupe tous les paragraphes, y compris ces titres visuels, reliés par des traits fins. Autres contenus abstraits. Les chiffres entre parenthèses décrivent l’ordre de conception et ne sont pas projetés.

**Ajouts propres à S35 :** sur la scène commune ci-dessus, ajouter sept pastilles bleu marine numérotées 1 à 7, sept traits et sept étiquettes vertes dans la colonne centrale, dans l’ordre : Plan 234, Liste 235, Copie 237, Id 236, Meta 239, Texte 245, PDF 241. Aucun chiffre répété devant les étiquettes ; mots et numéros espacés. Aucun trait ne masque une preuve. Ne pas inclure la consigne de retrait propre à S34 dans le prompt de S35.

**Alternative textuelle à fournir :** Page Programme et PDF textuel : plan h1 puis h3, puces dans p, collage de l’ancien dessin du presse-papiers, même valeur id sur deux éléments de la même page, meta refresh, horaires textuels à pipes dans pre, titres visuels du PDF rattachés aux paragraphes P. Sept repères rattachent ces constats respectivement aux règles 234, 235, 237, 236, 239, 245 et 241.

**Règle → préjudice utilisateur :** Sans rattachement précis, une correction peut traiter un symptôme en laissant le mécanisme en place.

**Garantie recherchée (matière de l’oral)**

Choisir pour chaque défaut le remède de portée adaptée, sans conclure sur les propriétés non contrôlées.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Scénario fictif, pas audit réel. Sept signes positifs : niveaux sautés, balisage p, motif collé distinct, même valeur id sur deux éléments de la page, meta refresh, texte dans pre, titres visuels rattachés à P. Aucune réponse ne repose sur une note inchangée, un menu absent ou un volet vide.
- Le plan contient tous les titres masqués et générés. Le fragment p contient toute la liste, sans rôles ARIA. Les deux relevés id sont des attributs de deux blocs différents, pas deux références vers une même cible, pas deux pages et pas des relations champ-étiquette. Leur valeur est a dans les deux écritures ; les guillemets ne la changent pas. Les deux propriétés forment une seule rangée de la vue source, sans balises HTML tronquées.
- Le collage insère l’ancien dessin du presse-papiers après le geste Ctrl avec C puis V ; la commande courante n’a pas repris le texte sélectionné. Le dessin collé est présent et grand ; pas de déduction depuis une absence ou une différence minuscule. Les losanges et la forme distinguent les objets, pas seulement la couleur. L’appel du menu n’est pas représenté ; il est évalué en S32 Q2.
- La meta refresh est un mécanisme que le livre demande de ne pas utiliser. Le nœud pre ne contient que les caractères des horaires : sélection textuelle et caret prouvent ici une représentation textuelle, pas une image. Les pipes sont des caractères ASCII ordinaires ; les jours et heures sont bien des données liées à des entêtes. Ni rôle de tableau, ni balisage table dans ce contenu inspecté complet. Ne pas ajouter des défauts de caption ou d’associations à ce seul défaut de simulation.
- Le PDF contient du vrai texte sélectionnable. Son arborescence complète est remplie de paragraphes sous P ; des traits rattachent positivement ses titres visuels à ce type de balise. Le défaut n’est pas déduit d’un panneau vide. Inspection choisie parmi les trois moyens valables du livre ; signets et lecteur d’écran restent admis. Aucun défaut de texte sélectionnable n’est montré.
- Hors preuve : date, métadonnée de caractères, UTF-8 réel, menu, associations et titre d’un vrai tableau, ordre d’un tableau de mise en page, accessibilité globale. Sept remèdes indépendants ; l’identifiant des blocs ne sert à aucune autre relation de l’exercice.
- Acceptation future : inspection côte à côte, puis recherche des sept défauts sur la scène nue par une personne ignorant le corrigé. Non réalisé ici. Rejeter tout état illisible ; ne pas le sauver par une notification qui nomme la réponse.

**Discours oral du présentateur (non projeté)**

#### Sept défauts et leurs remèdes

- Le plan complet saute un niveau descendant : rétablir la hiérarchie des sections.
- Les puces sont dans un paragraphe : donner aux items une sémantique de liste.
- La copie reprend un ancien dessin au lieu du passage sélectionné : laisser fonctionner la commande courante.
- Deux blocs de la même page portent le même identifiant : attribuer à chacun sa valeur unique.
- La métadonnée déclenche une recharge : le livre demande de ne pas utiliser ce mécanisme.
- Les horaires sont des lignes de texte à séparateurs : les publier comme un vrai tableau.
- Les titres visuels du PDF sont balisés en paragraphes : leur donner une structure de titres conservée à l’export.

#### Limites de l’observation

- Rien ne prouve les dates, le codage effectif, l’accès au menu ou les propriétés d’un véritable tableau absent de cette scène.

#### Transition

- Ces diagnostics reposent sur les distinctions rencontrées dans toute la rubrique.

**Corrigé (notes du présentateur, non projeté) :** Repère 1 → 234 : saut h1 puis h3 dans le plan complet. Repère 2 → 235 : puces dans p et br, fragment complet sans rôles ARIA. Repère 3 → 237 : la commande courante reprend l’ancien dessin au lieu du texte sélectionné, échec de copie rendu par un collage présent. Repère 4 → 236 : même valeur a sur deux éléments de la même page, même avec deux écritures de guillemets ; aucun champ de formulaire ni autre relation inspectée. Repère 5 → 239 : meta refresh dans head. Repère 6 → 245 : données textuelles dans pre avec pipes, sans structure de tableau ; aucune image de texte, donc pas de réponse 187. Repère 7 → 241 : inspection complète montrant les titres visuels du PDF balisés P, comme de simples paragraphes. Le PDF contient du vrai texte, aucun défaut 240. Le menu n’est pas testé. Sept remèdes indépendants, aucun huitième défaut à inventer.

**Mémo oral :** Une correction utile reste dans sa preuve.

**Fichier final prévu :** `finals/slide-35-correction-grand-cas.png`

---

### S36 — Cinq distinctions à garder

- **Acte :** 6. S’entraîner
- **Type :** mémo
- **Durée indicative :** 0:45
- **Objectif pédagogique :** Offrir une synthèse de révision centrée sur les confusions travaillées.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Rassembler les cinq distinctions.
- Idée principale : Une propriété ne prouve pas sa voisine.
- Scène : qui, Nora ; où, devant son carnet à la bibliothèque ; objet, cinq fiches de révision ; tension, ne pas confondre les gestes ; action, elle classe les fiches dans le carnet et en garde une ouverte ; résultat, cinq paires servent de rappel.
- Transformation visible : Les situations deviennent des repères de révision.
- Test des trois secondes : « Cinq distinctions évitent des raccourcis. »
- Ajout par rapport à la slide précédente : Du cas complexe à une synthèse transportable.

**Référence de composition principale :** `N17`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Cinq distinctions à garder`
- `Déclaration / UTF-8 réel`
- `Titres / listes`
- `Copie / menu`
- `Texte PDF / titres PDF`
- `Mise en page / données simulées`

**Illustration :** Nora range cinq fiches dans un carnet ouvert sur une table. Chaque onglet porte une distinction et dépasse du carnet ; sa main pointe la fiche Texte PDF / titres PDF. Le portable à côté montre le programme abstrait, pour garder un objet vécu. Aucun catalogue d’icônes autonomes.

**Alternative textuelle à fournir :** Nora classe cinq distinctions : déclaration et UTF-8, titres et listes, copie et menu, texte et titres PDF, mise en page et simulation de données.

**Règle → préjudice utilisateur :** Les raccourcis de preuve conduisent à des diagnostics erronés.

**Garantie recherchée (matière de l’oral)**

Revenir au contrôle propre à l’objet avant de conclure.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Les entêtes de cellules et le titre du tableau forment une distinction supplémentaire travaillée en S25, S26 et S30, rappelée à l’oral ; pas de sixième carte qui surchargerait la synthèse.

**Discours oral du présentateur (non projeté)**

#### Chaque propriété garde sa preuve

- La déclaration du codage ne prouve pas son usage effectif.
- Une liste d’items n’est pas un plan de sections.
- La copie et l’ouverture du menu contextuel sont deux fonctions.
- Le texte du PDF et ses titres demandent deux examens.
- Un tableau de mise en page se linéarise ; une simulation de données se remplace par une vraie structure.
- Dans cette structure, les entêtes donnent le contexte des cellules et le titre nomme l’ensemble.

#### Transition

- Le bénéfice de ces distinctions est très concret : retrouver la maîtrise du programme.

**Mémo oral :** Ne pas donner à une preuve plus de portée qu’elle n’en a.

**Fichier final prévu :** `finals/slide-36-memo.png`

---

### S37 — Le contenu reste entre leurs mains

- **Acte :** 6. S’entraîner
- **Type :** conclusion
- **Durée indicative :** 0:40
- **Objectif pédagogique :** Refermer la scène initiale sur des usages rendus possibles, sans promesse globale.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Conclure en écho à l’ouverture.
- Idée principale : Structurer le contenu sert les personnes qui le lisent, le parcourent et le réutilisent.
- Scène : qui, Nora, Malik et Odette ; où, autour de la table de bibliothèque de l’ouverture ; objet, le programme sur trois supports ; tension, résolue pour les gestes montrés ; action, Nora sélectionne une phrase, Malik rejoint une section, Odette annote une version imprimée ; résultat, le même programme sert trois usages.
- Transformation visible : Le geste empêché de l’ouverture aboutit à une citation sélectionnable.
- Test des trois secondes : « Chacun utilise le programme à sa manière. »
- Ajout par rapport à la slide précédente : Du mémo à sa raison d’être humaine.

**Référence de composition principale :** `N01`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora), `A-MALIK` (Malik), `A-ODETTE` (Odette).

**Texte visible (projection)**

- `Le contenu reste entre leurs mains`
- `Le contenu se lit, se parcourt, se réutilise`

**Illustration :** Table de la bibliothèque, Nora au centre utilise la souris et voit des mots abstraits surlignés dans le PDF, à la différence du rectangle-image de S01. Malik à gauche navigue au clavier dans un plan, casque gris clair ; Odette à droite annote une feuille au crayon. Les trois blocs et ancres restent exacts. Aucun pictogramme de certification ni coche de conformité globale. Slogan en bandeau vert pâle.

**Alternative textuelle à fournir :** Nora sélectionne une phrase du programme, Malik rejoint une section par ses titres, Odette annote une feuille : trois usages du même contenu.

**Règle → préjudice utilisateur :** Un contenu conçu pour une seule façon de le voir retire des moyens de le parcourir ou de le réutiliser.

**Garantie recherchée (matière de l’oral)**

Des usages possibles dans les situations contrôlées, sans conclure à une conformité globale du service.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Écho de composition S01 ; ne pas reproduire le rectangle de sélection de l’image initiale.
- Théo, Inès et Samuel sont présents dans le reste de la série ; aucune contrainte d’afficher six personnes dans cette scène.

**Discours oral du présentateur (non projeté)**

#### Garder les usages possibles

- Nora peut reprendre une phrase ; Malik peut rejoindre une section ; Odette peut travailler sur son programme.
- Les caractères, les titres, les commandes et les relations de données servent ces usages.
- Chacun se vérifie par un contrôle adapté, sans qu’un succès dispense des autres.
- La structure du code devient ainsi une aide concrète à la consultation.

#### Conclusion

- Le contenu se lit, se parcourt, se réutilise.

**Mémo oral :** Le code sert les usages des personnes.

**Fichier final prévu :** `finals/slide-37-conclusion.png`

---

### S38 — Revenir aux sources

- **Acte :** 6. S’entraîner
- **Type :** ressources
- **Durée indicative :** 0:30
- **Objectif pédagogique :** Donner les trois sources et leurs limites d’accès sans créer une transcription finale.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · STRUCTURE ET CODE` ; tout en bas à droite : la pagination `NN / 38`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : Ouvrir la suite de la révision.
- Idée principale : Les fiches officielles et le livre permettent de vérifier le détail.
- Scène : qui, Nora ; où, à la table de bibliothèque ; objet, un livre, le glossaire et la checklist ; tension, un résumé ne contient pas tous les contrôles ; action, elle ouvre le livre à côté de sa note de révision ; résultat, la révision retourne aux sources.
- Transformation visible : Du résumé à ses documents de référence.
- Test des trois secondes : « Trois sources pour contrôler un détail. »
- Ajout par rapport à la slide précédente : Après la conclusion, les moyens de poursuivre.

**Référence de composition principale :** `N10`. Étalon du masque après validation : `E01`. Ancres de chaque personnage présent : `A-NORA` (Nora).

**Texte visible (projection)**

- `Revenir aux sources`
- `Checklist Opquast V5`
- `Glossaire Structure et code`
- `Qualité et conformité des services numériques`

**Illustration :** Nora ouvre un livre à côté de son portable et annote son carnet. Les trois noms de ressources figurent sur des onglets attachés au livre, à un dictionnaire et à la checklist ouverte, pas sur une couverture inventée. Aucun logo, URL ou nom d’auteur lisible ajouté dans la scène.

**Alternative textuelle à fournir :** Nora révise avec la checklist Opquast V5, le glossaire Structure et code et le livre Qualité et conformité des services numériques.

**Règle → préjudice utilisateur :** Un résumé sans retour aux sources peut faire perdre les conditions des contrôles.

**Garantie recherchée (matière de l’oral)**

Retrouver libellés, objectifs, solutions, contrôles et avis de l’expert dans les sources indiquées.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Les liens et provenances figurent dans Sources principales. Glossaire : extrait local du 17 juin 2026, copié le 8 novembre ; accès en ligne non public, non revérifié ici.
- Aucune nouvelle affirmation de licence ou de droits sur le livre ; aucune publication de son corpus.

**Discours oral du présentateur (non projeté)**

#### Les sources gardent le détail

- La checklist donne les libellés des règles et leurs fiches.
- Le glossaire précise le vocabulaire de la rubrique.
- Le livre développe les objectifs, les solutions, les contrôles et les nuances de l’expert.
- Un cas concret se vérifie contre ces détails avant de conclure.

#### Conclusion

- Revenir aux sources garde les nuances utiles.

**Mémo oral :** Un doute précis appelle une source précise.

**Fichier final prévu :** `finals/slide-38-ressources.png`

---

## Contrôle final de couverture

- **Couverture :** 15/15 fiches dédiées, 15/15 règles bonnes réponses d’exercices corrigés, 15/15 couvertes par S32-S33 et S35 ensemble. Huit questions ouvertes ; sept défauts indépendants. Les renvois de Sources et couverture sont résolus vers les corrigés du fichier.
- **Mesures par script :** maximum visible 160 caractères (S30, S33 et S35), S33 Q5 inclus ; encadré maximal 59 caractères (S20). Somme de toutes les chaînes de Texte visible, titre compris, hors en-tête, footer, badge et pagination. Exactement 29 encadrés : 14 IMPACT, 6 GARANTIE, 7 CONTRÔLE, 2 LIMITE ; un par ligne, un en S07, deux dans chacune des quatorze autres slides de règle, aucun ailleurs. Scène nue commune : 1 467 caractères, hors consignes de repères. Mesures dans `/tmp/structure-storyboard-v003-session/verification.json`, script `verify.py` exécuté avec `python3 -I`.
- **Gabarit préservé :** 38 fiches et masques ; comparaisons au modèle Présentation avec les seules substitutions footer et pagination. Blocs de style et de personnages, critères de rejet conservés, trois ajouts I7 historiques isolés.
- **Oral :** zéro numéro de règle dans les discours et mémos, corrigés exclus ; zéro tiret long dans les textes visibles et oraux, recherches par script. Durées : 2 405 secondes, 40 min 05 s.
- **Preuve locale :** script, rapport JSON et diff v002/v003 dans `/tmp/structure-storyboard-v003-session/`. Contrôle d’accents, conservation de v001/v002 et de state/current.json, SHA-256 du storyboard final dans run.json ; copie ciblée sur le Mac Studio, empreintes comparées des deux côtés.

Ces contrôles portent sur le texte. Le rendu, les gestes réels, les annonces d’aide technique, la recherche des sept défauts par un observateur humain et l’édition restent non vérifiés. La validation autorise une future génération, sans l’exécuter pendant cette mission.

## Cinq slides étalons proposées

À fabriquer après validation du storyboard et à comparer à Présentation avant toute série ; aucun PNG produit pendant cette mission :

- **E35, S35 Correction** : générée en premier ; sept défauts indépendants, site et PDF textuel, sept états positifs, deux extraits courts et propriétés DOM, sept repères ; scène commune séparée des ajouts ; son PNG validé permet l’édition S34.
- **E01, S01 Ouverture** : MASQUE LIBRE, Nora en action, slogan et cadre de vie ; devient l’ancre de série tout en conservant A-NORA comme ancre d’apparence.
- **E17, S17 Copie du contenu** : MASQUE RÈGLE sans code, geste et préjudice lisibles, deux encadrés.
- **E08, S08 Métadonnée de caractères** : MASQUE RÈGLE avec un extrait complet et exact, Odette active, faible charge de texte.
- **E16, S16 Checkpoint 2** : MASQUE EXERCICE, question et trois cas, Inès en action, pas de correction visible.

## Revue avant génération

- Historique v001, 8 novembre 2026 : lecture du brief, des contrats, du modèle et de ses deux relectures, inspection des PNG et lecture des trois sources de la série.
- Historique v001, 8 novembre 2026 : consultation MCP des deux règles connexes ; provenance locale enregistrée. Aucun accès API actuel revendiqué.
- 8 novembre 2026 : v001 par Codex, statut BROUILLON ; aucune nouvelle image ou publication.
- 8 novembre 2026 : v002 par Codex, 23 constats traités, trois ajouts I7 déclarés ; contrôles du fichier écrit et copie ciblée sur le Mac Studio, statut BROUILLON maintenu. Aucune nouvelle consultation MCP ; provenance de v001 conservée.
- 8 novembre 2026 : v003 par Codex ; deux relectures Structure et code et sources relues, neuf PNG Pnn réexaminés ; 14 constats traités, validation sur mandat de l’orchestrateur, manifeste verrouillé.
- **Auto-vérification PDG, pas une revue indépendante.** Couverture : quinze libellés, quinze fiches dédiées et des bonnes réponses dans les exercices. Ancrage : chaque règle relue contre le livre ; exemples originaux séparés des prescriptions. Régression documentaire : masques et personnages comparés au modèle, ajouts I7 isolés, textes comptés, ancres et chemins locaux contrôlés. Le rendu, les gestes réels et le test humain des trois secondes ne sont pas exécutés.

### PDG pass

- Déclencheur : spécification durable de fabrication ; skill `/Users/alex/Claude/.claude/skills/progressive-disclosure-guard/SKILL.md` lu. Une faute se propagerait aux images ; contrôle borné du storyboard et du manifeste nécessaire.
- Artéfacts : brief, missions v001-v003, livre rubrique 14, libellés, glossaire, deux relectures Structure et code, v002 et modèle Présentation v003 ; contrats de fabrication. Réutiliser les blocs et masques ; remplacer seulement la version active du run. Aucun moteur ni règle de harnais ajouté.
- Affirmation / source / verdict / impact : « masques identiques » / modèle et comparaison de 38 fiches / mesuré par script / préserver la fabrication ; « couverture 15/15 » / badges, corrigés et renvois / mesuré / aucun oubli ; « sept états positifs » / livre et scène commune / reasoned / qualité de l’étalon à vérifier ; « version active exacte » / run.json, SHA-256 et `resume` / mesuré après verrouillage / reprise fiable.
- Connu : contraintes, sources et périmètre. Inconnu : futur rendu et fidélité de l’édition. Hypothèses explicitées : toutes les opérations dessinées sont des scénarios, pas des essais réellement exécutés. Risque peu visible : un simple mot P ou pre ne suffit pas sans son rattachement explicite et son inspection complète, à contrôler sur E35.
- Préserver : originaux v001/v002, masques, personnages, références, durées, état partagé et travaux étrangers. Interdits : génération, prompt définitif, publication, commit, diagnostic de conformité globale. Mauvaise voie : compter une absence comme preuve ou sauver une scène incompréhensible par l’oral.
- Couverture : chacun des 14 constats possède une décision au Journal v003. Ancrage : corrections relues contre le livre ; recoupements 187/245 éliminés des objets d’exercice. Régression : comparaisons des blocs, listes blanches, corrigés, mesures et véritable commande `resume` ; parité des deux fichiers sur les deux Mac.
- Auto-vérification PDG, pas une revue indépendante. Les relectures indépendantes sont les deux fichiers déjà livrés ; aucune troisième relecture revendiquée. Les validations humaines de rendu et le test de la scène nue sont reportés à l’acceptation de l’étalon.

## Décisions reprises du brief

- Même Maison des Lisières et mêmes six personnages, sans nouveau personnage ponctuel.
- Même Bloc style, quatre masques et critères de rejet ; changement limité au footer et au total pour les masques.
- Bleu marine pour les quatre mots des encadrés ; titre à gauche hors masque libre ; une scène incarnée par slide hors grand cas.
- Correction du grand cas générée en premier ; cinq étalons et limite de cinq références selon l’ordre du brief.
- L’autorisation de cette mission s’arrête au storyboard v003, à run.json, à `resume` et à leur copie vérifiée sur le Mac Studio. Les étapes de production décrites dans le brief ne sont pas engagées.

## Sources principales

- **Brief :** `brief.md` de ce run, décisions et méthode, lu le 8 novembre 2026.
- **Livre :** *Qualité et conformité des services numériques*, quatrième édition 2026, partie 3, rubrique 14 ; copie `sources/opquast/livre-rubrique-14-structure-code.md`, lue intégralement.
- **Checklist officielle :** https://checklists.opquast.com/fr/qualite-numerique/ ; libellés 231-245 du fichier local fourni. Les pages web des quinze règles n’ont pas été rouvertes : la provenance du fichier est conservée honnêtement. Connexes : MCP local 69 et 185, provenance de v001 ; aucune nouvelle interrogation dans cette révision.
- **Glossaire :** https://training.opquast.com/digital-quality/glossaire/glossaire-structure-et-code/ ; lecture par l’extrait local fourni, pas par une session authentifiée. La date d’extraction d’origine est le 17 juin 2026, copie du 8 novembre.
- **Modèle :** `runs/presentation-opquast-v5/storyboard-v003.md` et ses deux relectures indépendantes v001 et v002 dans `sources/revues/`, lus en entier ; neuf PNG publiés inspectés.
- **Notes :** `/Users/alex/Claude/projets-heberges/slides-miweb/docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`, contrat éditorial consulté ; la mission actuelle garde le livre comme autorité de fond.
- **Syntaxe uniquement :** [élément time, HTML WHATWG](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element), [déclaration du codage](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-charset), [listes ul et li](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element), [caption et tableaux](https://html.spec.whatwg.org/multipage/tables.html#the-caption-element), consultés à la rédaction v001 le 8 novembre 2026. Pour la v002 : [pragma refresh](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv-refresh) et [syntaxe des attributs](https://html.spec.whatwg.org/multipage/syntax.html#attributes-2), consultés le 8 novembre 2026 ; le parseur de session contrôle les fragments. Ces vérifications ne modifient pas les prescriptions du livre.
- **Droits :** les scènes, synthèses et exercices sont des créations pédagogiques ; aucun droit nouveau sur le livre n’est affirmé et aucun extrait du corpus n’est publié par cette mission.

## Journal v001 (historique, décisions remplacées par v002)

- Gabarit remplacé par 38 fiches complètes ; ouverture sur un geste PDF empêché, conclusion en écho sur ce même geste devenu possible.
- Cinq regroupements thématiques originaux ; les tableaux sont distingués par fonction, relations de cellules, titre et ordre.
- Blocs de personnages repris sans réécriture ; A-THEO et A-INES sont des alias explicites des ancres fournies. E01 sera une ancre de série distincte de l’ancre d’apparence A-NORA.
- Densité bornée ; pas de faux texte nécessaire pour comprendre une scène. Les chaînes utiles aux transformations, résultats et codes sont dans les listes blanches.
- Relectures de Présentation prises en compte : masques complets, aucune carte imposée sans contenu, syntaxe complète, aucun défaut invisible affirmé à l’œil, pas de coche cachant une ambiguïté d’exercice, correction du grand cas préparée en premier.
- Les exercices reprennent le format d’appariement sans légende projetée. Les choix des paires sont donnés dans les notes ; pour les tableaux, cette borne empêche de nier les recoupements du contrôle de 245.
- Grand cas : page et PDF, sept résultats d’actions ou inspections déjà fournis, pas sept propriétés de code prétendument visibles. Aucun diagnostic de tableau dans cette scène.
- Aucune image, aucun prompt définitif, aucun accordéon final, aucune publication ni commit. Le statut reste BROUILLON. La synchronisation ciblée hors Git ne constitue pas une publication.

## Points de vigilance pour la relecture

- **Dates et caractères :** time/datetime et schema.org selon le livre ; code réel et déclarations distincts. Les caractères brouillés de S08-S09 deviennent des points d’interrogation ordinaires et des carrés dessinés ; illustration de risque, aucun diagnostic depuis le seul symptôme. Les questions finales testent une meta vide et un contenu UTF-8 servi sous entête contradictoire.
- **Titres et listes :** plan complet, titres masqués et générés compris ; plusieurs h1 admis. Rôles ARIA de liste admis ; ddn corrigé en dd d’après les solutions. L’annonce de liste est illustrative, non testée sur un logiciel réel.
- **Identifiants :** même page, deux éléments éditoriaux au repère 4 ; aucune association de formulaire observée. Les deux formes d’attribut de la vue source désignent la même valeur, sans affirmer un effet universel sur les navigateurs.
- **Maîtrise :** copie par raccourci et ancien dessin collé, pas note vide ; menu évalué sur un article au clavier, pas par un écran sans menu. Appui long de S18 : adaptation tactile à tester. Meta refresh écartée par le livre ; autres mécanismes désactivables avant. HTTP 3xx distinct de HTTP refresh ; AJAX est une précision hors livre.
- **PDF :** en Q6, titres structurés corrects et corps scanné sans texte : seul ce dernier défaut est évalué. Dans le grand cas, mots sélectionnables et titres visuels positivement rattachés à P dans l’inspection complète. Signets, inspection et lecteur d’écran restent trois moyens acceptés du livre ; aucun panneau vide.
- **Tableaux :** scope pour tableaux simples, id/headers selon la portée partielle. S30 demande le contrôle spécifique, les recoupements du contrôle général de 245 sont déclarés. Q5 nomme le tableau de mise en page. Les scènes de simulation utilisent du texte à pipes sélectionnable ; aucune image d’horaires, aucune réponse 187 concurrente.
- **Grand cas :** une seule scène commune ; instructions propres aux repères séparées. Chaque état doit rester présent et lisible après édition. Pas de code/texte supplémentaire, panneau vide, diagnostic ou huitième défaut. Test humain sur scène nue obligatoire avant acceptation de E35 ; non exécuté ici.
- **Références :** composition et étalon ne transmettent jamais l’apparence d’un personnage à la place de son ancre. Limite de cinq images, déduplication par chemins puis pixels ; blocs préservés avec les seuls ajouts I7 historiques.
- **Libellé 239 :** « imposée » du fichier checklist conservé ; le livre écrit « imposé ». Écart grammatical sans changement de portée. Coquilles de guillemets du livre corrigées dans les extraits.
- **Rythme et statut :** 40 min 05 s indicatives ; v003 verrouillée sur mandat d’autonomie après deux relectures indépendantes. Ni rendu, ni test humain, ni geste réel exécutés ; cette mission ne lance pas la génération.

## Journal v002 (historique, décisions remplacées au besoin par v003)

Relecture traitée intégralement : `sources/revues/relecture-independante-v001-2026-11-08.md`, 9 importants et 14 mineurs. Décisions de l’orchestrateur appliquées ; 23 constats traités, aucun écarté. Les variantes de correction sont justifiées ci-dessous.

### Importants

- **I1 — traité.** « Fabrication du grand cas », S34-S35, couverture et vigilance : suppression de tous les relevés donnant la réponse. Plan brut h1/h3, paragraphe et gestes au lieu de verdicts ; meta refresh complète pour prouver le mécanisme sans écrire Recharge imposée (solutions/contrôle du livre 239). La grille d’horaires en image remplace le scan PDF (245) ; le PDF textuel conserve une sélection de mots mais aucun accès par signets (241). Les sept objets sont indépendants. Composition aussi riche que P37 exigée, encore à éprouver au rendu.
- **I2 — traité.** Contrat, S02, S30, S32-S33 et couverture : huit questions nouvelles ouvertes, sans paires annoncées. Format erroné, doublon masqué, portée inversée, caption non pertinent, prix dissociés, scan, valeur de meta vide, transmission contradictoire. Évaluation + grand cas couvrent 231, 236 et 242-245. S30 retient la question de contrôle spécifique pour respecter le recoupement de 245 avec 242-243, sans QCM binaire.
- **I3 — traité.** S23, S24, S32 (ancien item retiré), S34-S35, vigilance et contrat du grand cas : les trois moyens du livre 241 sont valables. S23 montre les signets issus des titres ; le grand cas leur absence après affichage. Les réserves sur les signets manuels sont supprimées, sans ajout hors livre nécessaire.
- **I4 — traité.** S07-S10 : Nora trie des notices datées et reçoit un export dégradé ; Odette compare deux lectures hors ligne, caractères brouillés puis lisibles ; Samuel examine les pièces des deux incidents dans la distinction. Préjudices visibles, limites diagnostiques explicites (livre 232-233). Les scènes ne sont plus une chaîne de schémas de code.
- **I5 — traité.** S13, PDS, ancre, illustration, alternative et liste blanche : Malik au clavier entend une liste de deux éléments ; code ul complet conservé. Formule d’annonce explicitement illustrative, non testée (objectif du livre 235 : identification et restitution des listes).
- **I6 — traité.** « Références », contrat et 38 fiches : compositions autorisées N01/N03/N10/N17/S20 ; E35 est l’image à éditer, séparée de la composition S20 de S34. Au plus cinq images distinctes, déduplication des chemins et pixels, toutes les ancres prioritaires ; pas de personnage étranger copié. P37 reste comparateur de richesse.
- **I7 — traité avec écart autorisé.** « Personnages ponctuels » : ajout avant la phrase finale de « Si son image de référence est fournie, il la reproduit exactement. » pour Théo et de la forme « elle » pour Inès et Odette. Les trois autres blocs restent mot pour mot ceux de Présentation. P08 et P26 inspectées, visages en trois quarts lisibles ; copies d’ancre comparées par pixels.
- **I8 — traité.** S21 C : Recharge auto non désactivable, alternative et notes harmonisées. S20 (ancienne S19) garde Recharge imposée. Variante mieux prouvable dans le grand cas : meta refresh exacte et effet temporel, sans notification qui révèle le diagnostic, conformément à I1 et au livre 239.
- **I9 — traité.** S27 : Malik écoute la lecture linéaire ; Reliure et Photo figurent dans la vue initiale. Pastilles de formes et motifs identiques, puis blocs descriptifs, rendent l’ordre de séparation visible. Outil de développement laissé à l’oral, comme proposé.

### Mineurs

- **M1 — traité.** S35 : espaces de part et d’autre des flèches, comme Présentation ; Image → 245 et Plan PDF → 241 désignent deux objets distincts. Titres, Liste, Copie, Menu et Recharge restent entiers ; densité recontrôlée à 160 maximum.
- **M2 — traité.** S34-S35 : suppression des relevés Copie × et Menu × et du symbole × ; aucun équivalent textuel ou pictogramme d’erreur ne livre la réponse. Les gestes et leurs résultats les remplacent (I1).
- **M3 — traité.** S11 A, alternative et notes : Date sans forme programmatique ; absence de toute solution admise, dont schema.org, contenue dans le constat. Distracteur de codage conservé comme confusion d’objet, sans le prétendre équivalent à une date.
- **M4 — traité.** S30 B : Vrai tableau, aucun caption. Les paires sont supprimées ; la question porte explicitement sur le contrôle spécifique, dont les recoupements sont expliqués dans le corrigé et la vigilance.
- **M5 — traité.** S05 oral et S10 illustration : élément head. S06 visible : entêtes HTTP. Les entêtes de tableaux restent nommées ainsi dans leur contexte propre.
- **M6 — traité.** S20, ancienne S19, pièges : redirection HTTP 3xx distinguée du refresh HTTP ; remarque AJAX identifiée comme précision pédagogique hors livre.
- **M7 — traité.** S29 bandeau : Linéariser la mise en page, baliser les données ; renvoi grammatical supprimé.
- **M8 — traité.** S19 et S20 permutées : distinction copie/menu avant recharge. Titres, fichiers prévus, liste des masques, couverture, vigilance et transitions S18-S21 ajustés ; 38 slides et pagination inchangées.
- **M9 — traité.** S18 PDS, illustration et contrôle : appui long du doigt sur le lien, tablette tenue en main ; adaptation tactile explicitée, comportement à vérifier sur le navigateur cible.
- **M10 — traité.** S07 : Publié le 8 novembre dans la page, 8 novembre dans le code time complet. Deux chaînes distinctes autorisées, titre et garantie raccourcis pour tenir la densité ; date réellement visible des deux côtés.
- **M11 — traité.** S34 titre et consigne de fabrication : Grand cas : trouvez sept défauts, comme Présentation.
- **M12 — traité.** S05 oral : structure de titres HTML ou leurs équivalents ARIA, suivant l’entrée du glossaire.
- **M13 — traité.** Vigilance « Libellé 239 » : checklist imposée, livre imposé ; libellé checklist préservé mot pour mot au tableau, contenu du livre conservé.
- **M14 — traité.** En-tête et section « Changements depuis v001 » : la section décrit désormais les véritables corrections v002 ; première rédaction conservée uniquement en Journal v001 historique.

### Contrôles et limites de cette révision

- Auto-vérification PDG, pas une revue indépendante : couverture des 23 constats et des quinze règles ; ancrage des corrections dans le livre et le glossaire ; régression des blocs, masques, listes blanches, corrigés et renvois par le script de session.
- Aucune image créée, aucun prompt définitif, aucune publication, aucun commit. La v001, run.json, l’état courant et les changements étrangers restent préservés.
- Copie ciblée du seul fichier v002 au même chemin sur le Mac Studio ; SHA-256 comparés après transfert. Les scripts et preuves temporaires restent dans `/tmp/structure-storyboard-v002-session/`, sans ajout à la racine des worktrees.
- Le rendu, les gestes réels, les annonces de lecteur d’écran, le test humain des trois secondes et l’édition ImageGen restent non vérifiés. La suite appartient à l’orchestrateur.

## Validation

- **Statut :** `VALIDE_POUR_GENERATION`, version v003, 8 novembre 2026.
- **Autorité :** validation par l’orchestrateur sur mandat d’autonomie d’Alex du 8 novembre 2026, après deux relectures indépendantes : `sources/revues/relecture-independante-v001-2026-11-08.md` et `sources/revues/relecture-independante-v002-2026-11-08.md`. Les corrections suivent les décisions explicites de la mission v003 ; aucun accord humain supplémentaire ni troisième relecture inventés.
- **Portée :** spécification écrite autorisant la future génération ; aucun PNG ni prompt définitif produit dans cette mission. Les images étalons, gestes réels et test humain de la scène nue restent à contrôler lors de la production.
- **Verrou :** chemin, version, statut et SHA-256 du fichier final enregistrés dans `run.json` ; `resume` vérifie la reprise du run. Le hash n’est pas inscrit dans ce document pour éviter une empreinte autoréférente.

## Journal v003

Relecture traitée : `sources/revues/relecture-independante-v002-2026-11-08.md`, 3 importants et 11 mineurs. Quatorze constats traités, aucun écarté. Les variantes rejetées ci-dessous sont remplacées par des corrections plus sûres ; aucune génération.

### Importants

- **I1 — traité.** S34-S35 et Fabrication du grand cas : scène commune raccourcie, sept états présents. Copie : ancien dessin effectivement collé, variante proposée par la relecture. Menu remplacé par deux valeurs id présentes dans une seule page ; le menu passe en S32 Q2, l’unicité quitte cet item. PDF : titres visuels positivement rattachés à une branche de paragraphes P, inspection complète au lieu des signets vides, autre moyen valable du livre 241. Variantes avant/après et volet vide écartées sur décision de l’orchestrateur. Couverture, corrigés, limites et E35 mis à jour. Les sept objets de contrôle sont indépendants ; absence de menu et note inchangée ne prouvent plus rien dans le grand cas.
- **I2 — traité.** S33 Q5 : « Tableau de mise en page, prix à part » ; contexte décisif projeté. Q6-Q8 raccourcis sans perdre les faits. Total contrôlé par script ; aucune exception de densité nécessaire. Notes et alternative alignées.
- **I3 — traité.** S28-S30 et S34-S35 : horaires en image retirés des scènes, items et corrigés ; texte à pipes sélectionnable, rattaché à pre dans le grand cas, conformément aux solutions de 245. L’image n’est plus un objet d’exercice ; une simple mention du recoupement à l’oral n’aurait pas suffi. Le livre reste cité pour sa portée complète, y compris les images, sans mettre un tel défaut dans cette série.

### Mineurs

- **M1 — traité par remplacement.** Ancien S32 Q2 retiré : l’unicité est observée dans la même fenêtre et la même vue source au repère 4, avec deux valeurs a sur deux éléments éditoriaux. Pas de portée « même page » ajoutée après coup. Q2 nomme maintenant le menu contextuel bloqué sur un article ; le geste clavier est dessiné. Q1, Q3 et Q4 sont raccourcis en conservant publication, datetime, scope et caption, les faits décisifs. Contrôle du livre, sans exception applicative.
- **M2 — traité et renforcé.** S33 Q6, vignette, contrôle, corrigé et oral : le PDF interne a des titres structurés corrects mais le corps reste scanné, sans couche de texte. Le constat projeté « PDF : titres balisés, scan » et sa vignette l’expriment avant correction ; la réponse sur les titres est ainsi écartée par une propriété positive, pas seulement par l’oral.
- **M3 — traité.** S33 Q8 : contenu réellement UTF-8 servi sous entête Latin-1. Le checkpoint porte sur un contenu réellement non UTF-8 ; ce nouvel item teste au contraire la mauvaise information HTTP malgré un contenu UTF-8. Correction appuyée sur les trois temps du contrôle 233, sans supposer une meta observée.
- **M4 — traité.** S20 : encadré « Pas de meta refresh, le reste désactivable avant ». Les deux branches du contrôle sont visibles ; notes et oral déjà exacts conservés.
- **M5 — traité.** S21, Ajout : application après la recharge imposée et la distinction copie/menu ; régression de séquence corrigée.
- **M6 — traité.** S04, oral : Théo appelle les actions d’un lien sur sa tablette ; cohérent avec S18, sans préparation de matériel inventée.
- **M7 — traité.** S03, scène et transformation : six postes, cinq usages puis entraînement ; illustration et liste blanche conservées.
- **M8 — traité.** Fabrication et S34-S35 : paragraphe de scène commune identique ; consigne de retrait propre à S34 et ajouts propres à S35 séparés, jamais assemblés ensemble dans un prompt. S35 ne recopie plus une interdiction d’ajouter ses propres repères.
- **M9 — traité.** S10 : « Une déclaration ne prouve pas l’encodage ». S34-S35 : Ctrl, C, V ordinaires ; pictogrammes dessinés, pas de touche Mac. S08-S09 : points d’interrogation ASCII dans les mots brouillés et carrés dessinés, aucun glyphe de remplacement ou symbole de mojibake rare à générer. Les flèches ordinaires déjà éprouvées dans le modèle restent autorisées hors de ces nouveaux libellés.
- **M10 — traité.** Contrat des références : ne jamais reprendre un personnage de composition ni de l’étalon à la place de l’apparence donnée par son bloc et son ancre. E35 actualisé ; les quatre autres étalons restent les mêmes.
- **M11 — traité.** S08 et S13, illustrations : « aucun autre personnage », sans nommer les absents. S09 : Caf? remplace le mojibake rare ; symptôme illustratif, sans nouvel encodage déduit de l’apparence. S08 : ?t? distinct de Été, carrés dessinés autour des points d’interrogation.

### Contrôles et limites de v003

- Auto-vérification PDG, pas une revue indépendante : couverture des 14 constats, ancrage dans les trois sources et régression des blocs, masques, listes blanches, corrigés, renvois, densités et scène commune par script de session.
- Le style, les quatre masques, les six personnages et les durées restent ceux de v002. Les seuls changements de fond d’exercice sont explicités ci-dessus. Les Journaux v001 et v002 sont historiques ; la présente section et les fiches actives priment sur leurs anciens choix de scène et statuts.
- Copie ciblée de storyboard-v003.md et run.json au même chemin sur le Mac Studio, empreintes vérifiées des deux côtés ; originaux préservés. La seconde relecture existante est également recopiée sans modification, car absente sur ce poste et référencée par le manifeste. Les 38 identifiants attendus sont enregistrés, comme dans Présentation ; aucune candidate déclarée. Les scripts et preuves temporaires ne sont pas des livrables de production.
- Aucune image, publication ou commit. Qualité du rendu et observation humaine non vérifiées. Arrêt après le reçu de `resume` et la parité des deux fichiers.
