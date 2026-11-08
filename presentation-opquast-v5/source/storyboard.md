# OPQUAST V5 — PRÉSENTATION | STORYBOARD MAÎTRE — FABRIQUE V2

**Édition de travail :** 8 novembre 2026, révision v003 (relecture indépendante de la v002 traitée)
**Référentiel :** Opquast Qualité Numérique V5 (2025-2030), rubrique Présentation, règles 180 à 196
**Finalité :** former à reconnaître, distinguer, vérifier et justifier les 17 règles de la rubrique Présentation, puis les relier aux autres rubriques, pour se préparer à la certification.
**Livrable :** spécification éditoriale et visuelle destinée à la Fabrique V2, pas un diaporama publié ni un jeu de prompts ImageGen définitifs.
**Durée intégrale :** environ 45 minutes (45 min 45 s de durées indicatives cumulées).
**Volume :** 40 slides : ouverture et méthode (6), 17 slides centrées chacune sur une règle, 5 slides de distinction, 4 checkpoints, transversalité, évaluation finale de 8 questions sur deux slides, grand cas et sa correction, mémo, conclusion, ressources.

## Identité

- Statut : `VALIDE_POUR_GENERATION` (validation d’Alex, 8 novembre 2026).
- Version : `v003`. Les v001 et v002 sont conservées sans modification.
- Périmètre : Opquast V5 `qualite-numerique`, rubrique Présentation, règles 180 à 196 ; règles connexes 157, 140, 158, 136 (visibles) et 69 (oral seulement).
- Audience : candidats à la certification Opquast, profils numériques variés.
- Nombre : 40 slides, aucune annexe.
- Revue : relecture indépendante de la v001 du 7 novembre 2026 (`sources/revues/relecture-independante-v001-2026-11-07.md`), constats traités en v002 ; relecture indépendante de la v002 du 8 novembre 2026 (`sources/revues/relecture-independante-v002-2026-11-08.md`), constats traités en v003 (« Journal v003 ») ; validation d’Alex le 8 novembre 2026.
- Correspondance machine : `run.json`, une seule version active ; empreinte à enregistrer seulement au passage à `VALIDE_POUR_GENERATION`.

## Changements depuis v001

Historique de la v002, conservé tel quel ; les changements de la v003 figurent dans « Journal v003 », en fin de document.

### Bloquant

- **B1, masque unique imposant des encadrés** : corrigé. Quatre masques nommés remplacent le masque unique : `MASQUE RÈGLE` (rangée d’encadrés, un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins), `MASQUE COMPARAISON` (panneaux titrés et bandeau final), `MASQUE EXERCICE` (bandeau de question et cartes), `MASQUE LIBRE` (titre et scène, aucun encadré). Chaque fiche nomme son masque et le reproduit mot pour mot. Aucun masque n’impose un cadre sans texte de la liste ; critère de rejet commun : « cadre, carte, bandeau ou encadré vide, ou portant un texte hors liste ».

### Importants

- **I1, tirets demi-cadratins** : corrigé. Les textes visibles et les oraux n’emploient que le tiret simple `-` (forme `IMPACT - …`). Les titres de fiches `### Snn — …` restent des éléments de structure du document, non projetés ; l’intervalle `2025-2030` passe au tiret simple.
- **I2, S26 « à l’écran »** : corrigé. Titre `Pas de texte justifié par les styles` ; le piège dit désormais que le contrôle du livre porte sur tout le CSS et sur le HTML, sans exception de média.
- **I3, S27 copier-coller non vérifié** : corrigé. La scène montre le contrôle du livre (désactivation des styles) ; le copier-coller reste un objectif cité à l’oral, sans démonstration. IMPACT : `IMPACT - Saisies en capitales, elles s’imposent à tous`.
- **I4, bannière exclue de la règle 187** : corrigé. Le défaut 1 du grand cas devient le tableau des dates du trimestre publié en image, contenu éditorial ; étiquette S37 `Image de texte → 187`.
- **I5, S37 « à l’identique » sans méthode** : corrigé. Méthode retenue et justifiée dans la section « Fabrication du grand cas » : S37 (correction) est générée d’abord, puis S36 est obtenue par édition ImageGen du PNG S37 validé, qui retire seulement les repères et remplace le titre. Critères d’acceptation et repli explicites.
- **I6, Nora différente du personnage des références** : corrigé par rapprochement. Nora reprend l’apparence du personnage féminin de `N10` et `S20` (longs cheveux bruns ondulés, pull bleu vif) ; le PNG de l’étalon S01 validé devient l’ancre `A-NORA` de toutes les slides où elle apparaît. Ancres `A-SAMUEL` (S06) et `A-MALIK` (S13) sur le même principe. Les autres personnages portent la phrase « reprendre le style de dessin des références, pas l’apparence de leurs personnages ».
- **I7, densité** : corrigé. Cible de la coordination appliquée : 160 caractères au plus par slide hors en-tête, footer, pagination et badge, encadrés de 60 caractères au plus. Les slides de règle passent à deux encadrés ; S08 perd `* obligatoire` ; S19 n’a plus de libellés de boutons ; S25 n’a plus qu’un personnage ; scènes de S15, S30 et S31 allégées. Toutes les slides tiennent la cible, S37 comprise (titre réduit à `Correction`, étiquettes courtes). Mesures dans « Contrôle final de couverture ».
- **I8, daltonisme représenté en gris** : corrigé. Les étiquettes ordinaires sont vert foncé, l’obligatoire rouge, de même luminosité ; le médaillon en niveaux de gris est présenté comme la page vue lors du contrôle, pas comme la perception de Théo ; alternative « Théo, qui distingue mal le rouge du vert ».
- **I9, piège sur les liens (S10)** : corrigé selon le livre : l’avis de l’expert sur le contraste suggère un contraste entre lien et texte quand les liens ne sont différenciés que par la couleur ; la différenciation des liens relève aussi de la rubrique Liens (S33).
- **I10, même loupe pour 185 et 189** : corrigé. S14 garde la loupe de recherche (`« Rechercher, bouton »`) ; S16 prend l’icône calendrier (`« Agenda, lien »`) ; S18 et S28 ajustés.
- **I11, S18 C à deux réponses** : corrigé. L’item vise le nom d’un bouton icône, qui ne s’affiche jamais sur action : `B. Nom de bouton en display: none`.
- **I12, oral et contrat des notes orales** : corrigé. Consignes au groupe et commentaires sur le support déplacés dans « Contrôle et pièges » (animation) ou supprimés ; oraux réécrits selon les gabarits de `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md` de `slides-miweb` : titres de contenu, puces, « Impact du non-respect » et « Ce que garantit la règle » sur les slides de règle, transition ; tiret simple seulement ; aucun numéro de règle prononcé.

### Mineurs

- **M1, « mesureur »** : corrigé, `Deux contrôles : sans couleurs, puis mesure du ratio`.
- **M2, S11 C « plus de menu »** : corrigé, `C. Paiement : autres couleurs, autre police`.
- **M3, S13 oral infantilisant** : corrigé, l’oral ne prête plus de question à Malik.
- **M4, ordre des annonces** : corrigé, forme « nom, rôle » partout (`« Rechercher, bouton »`, `« Agenda, lien »`).
- **M5, espacement hors règle 186** : corrigé. « Collés » retiré de S23 A et de S19 ; les difficultés motrices et le réflexe des liens de pied de page sont retirés de l’oral, faute d’appui dans le livre.
- **M6, S23 B littéral** : corrigé, `B. Écarter les doigts : la page reste figée`.
- **M7, S24 « promotionnelles »** : corrigé, `LIMITE - Logos et bannières publicitaires exclus` ; l’oral cite les éléments graphiques de promotion.
- **M8, Arial presque toujours installée** : corrigé, `font-family: Optima, sans-serif;`, d’après l’exemple du livre (`Optima, “Trebuchet MS”, sans-serif`).
- **M9, Odette et le cliché de l’âge** : corrigé. Motif unique et neutre : elle aime annoter le programme sur papier ; geste de presbytie supprimé.
- **M10, S34 Q3 et Q4** : corrigé, `3. « Le bouton à droite »` et `4. Plan en aplats de couleur seuls`. La légende des choix est supprimée (voir M11).
- **M11, question des évaluations** : corrigé pour S34 et S35 : `Quelle règle est prouvée enfreinte ?`, qui rend Q5 univoque. Pour tenir 160 caractères, les évaluations n’affichent plus de légende de choix : comme les checkpoints, elles demandent la règle, et les distracteurs attendus figurent dans les corrigés.
- **M12, contraste affirmé à l’œil (S37)** : corrigé, l’oral ajoute « à confirmer par la mesure du ratio ».
- **M13, Théo absent de la conclusion** : corrigé, Théo ajouté en S39.
- **M14, S07 « restent les mêmes »** : corrigé, `GARANTIE - Menus, styles et largeurs restent cohérents`.
- **M15, S32 panneau contredit par l’image** : corrigé, `Les menus disparaissent-ils à l’impression ?`.
- **M16, occurrences de « S’inscrire » (S36)** : sans objet. Le bouton du grand cas n’a plus de libellé lisible ; le critère de rejet fixe le nombre d’occurrences de chaque texte (une).
- **M17, lignes de code exposées** : corrigé, `content: "Complet";` (S15) ; `@media print` et `nav { display: none; }` sur deux lignes (S31). Critère « relecture caractère par caractère » ajouté à toutes les slides à code.
- **M18, slides proches du pictogramme** : corrigé en partie. S02 montre Nora dans trois mini-scènes ; S05, S38 et S40 donnent à Nora une action. Ces slides de structure restent les plus proches du défaut de la série précédente ; à surveiller sur les planches QA.

### Autres changements

- Checkpoint 2 ramené à quatre items (183, 185, 188, 189) pour tenir la densité ; la règle 184 reste corrigée en S34 Q3 et S37.
- Mention de la source MCP : le 7 novembre 2026, ma consultation de la checklist a répondu `source: api` ; celle du relecteur, `source: local` (instantané du 3 septembre 2026, clé API absente). Les libellés concordent dans les deux cas.

## Paramètres de série

- Guide commun : `docs/05-GUIDE-STYLE.md`, version 2.0.0, avec les exceptions déclarées plus bas.
- En-tête exact : haut gauche `QUALITÉ WEB` puis, dessous, `EXPÉRIENCES DURABLES` ; haut droit `Opquast` puis, dessous, `DES SITES MEILLEURS POUR TOUS`. Un seul espace entre chaque mot.
- Footer principal exact : `RÈGLES OPQUAST · PRÉSENTATION` (point médian U+00B7), en bas à gauche.
- Annexes : aucune ; pas de footer d’annexe.
- Pagination : `NN / 40`, en bas à droite.
- Badges : petit cartouche sous le titre, aligné à droite, seulement sur les 17 slides de règle et les 5 slides de distinction, au format `R. 180`, `R. 181 · 182` ou `R. 187 · 188 · 189`. Aucun badge ailleurs. S33 et S37 affichent les numéros en texte, sans cartouche.
- Slogan : `La forme sert le fond, pour chacun` ; visible en S01 et S39 uniquement.
- Navigation : aucune barre, pastille ou fil d’Ariane. Le plan (S03), le sous-titre `Acte N · <libellé>` de la première slide de chaque acte (S07, S12, S19, S24, S30, S33) et les titres situent l’apprenant.
- Tirets : tiret simple `-` seul dans les textes visibles et l’oral ; apostrophes et guillemets typographiques ; les guillemets droits n’apparaissent que dans le code.
- Format : 16:9, 1672 × 941 px.
- Densité : 160 caractères au plus par slide (somme des chaînes de la liste blanche, hors en-tête, footer, pagination et badge), encadrés de 60 caractères au plus ; aucune exception.
- Références visuelles réellement disponibles (lues le 7 novembre 2026 avec l’outil de lecture d’images) :
  - `N01` : `/Users/alex/Claude/projets-heberges/slides-miweb/navigation-opquast-v5-360/assets/slides/slide-01.png` (ouverture : écran central relié à des pastilles, feuillages en bordure).
  - `N03` : `…/navigation-opquast-v5-360/assets/slides/slide-03.png` (comparaison en deux panneaux corail et vert, bandeau final).
  - `N10` : `…/navigation-opquast-v5-360/assets/slides/slide-10.png` (personnage féminin à gauche, interface à droite, trois encadrés à icône).
  - `N17` : `…/navigation-opquast-v5-360/assets/slides/slide-17.png` (parcours en cinq panneaux pastel, personnage qui marche, bandeau final).
  - `S20` : `/Users/alex/Claude/projets-heberges/slides-miweb/securite-opquast-v5-v4/source/etalons/slide-20.png` (même personnage féminin, deux fenêtres comparées, encadrés IMPACT, GARANTIE, CONTRÔLE).
  - Ancres de série, ajoutées après validation : `A-NORA` = `finals/slide-01-ouverture.png` ; `A-SAMUEL` = `finals/slide-06-methode.png` ; `A-MALIK` = `finals/slide-13-forme-position.png`. Tant qu’une ancre n’existe pas, la fiche s’en passe.
  - Ces références transmettent une grammaire graphique, jamais leur en-tête (`QUALITÉ NUMÉRIQUE - OPQUAST V5`), leur footer (`Opquast - présentation Miweb`), leur numérotation ni leur thème.

### Bloc style (à répéter mot pour mot dans chaque prompt)

> Slide de formation institutionnelle française, format paysage 16:9, exactement 1672 × 941 pixels. Fond ivoire presque blanc, structure et titres bleu marine, panneaux pastel arrondis aux aplats doux. Couleurs à sens fixe : corail pour l’impact sur l’utilisateur, vert pour la garantie, bleu clair pour le contrôle, orange pour la limite ; chaque encadré porte aussi son mot et son icône, la couleur n’est jamais le seul repère. Illustration vectorielle plate aux traits fins, avec personnage, dans l’esprit des références fournies. Feuillages vectoriels discrets, très pâles, seulement en bordure de la slide, jamais sous un texte. Typographie sans sérif proche de Marianne, casse de phrase pour le titre. Aucun dégradé, aucune photographie, aucune 3D, aucune ombre lourde, aucun faux logo, aucun texte en dehors de la liste fournie : toute zone d’interface sans texte prévu est composée de lignes et de blocs abstraits, sans lettres ni chiffres. Chaque texte de la liste apparaît une seule fois. Ne reprendre ni l’en-tête, ni le footer, ni la numérotation des images de référence.

### Les quatre masques (chacun à répéter mot pour mot dans les prompts des fiches qui le citent)

Partie commune, incluse au début de chacun des quatre masques ci-dessous et non répétée ici pour ne pas la dédoubler : « En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. »

- `MASQUE RÈGLE` : slides de règle (S07 à S09, S12 à S16, S19 à S21, S24 à S27, S30, S31).
- `MASQUE COMPARAISON` : slides de distinction (S10, S17, S22, S28, S32).
- `MASQUE EXERCICE` : checkpoints, évaluations, grand cas et correction (S11, S18, S23, S29, S34 à S37).
- `MASQUE LIBRE` : ouverture, contrat, plan, fil rouge, glossaire, méthode, transversalité, mémo, conclusion, ressources (S01 à S06, S33, S38 à S40).

Texte complet de chaque masque, reproduit à l’identique dans chaque fiche sous « Masque » :

- `MASQUE RÈGLE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

- `MASQUE COMPARAISON` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

- `MASQUE EXERCICE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

- `MASQUE LIBRE` :

  > En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

Le texte exact de chaque masque est reproduit dans chaque fiche, sous « Masque ».

### Bloc personnage (à répéter mot pour mot dans chaque prompt où Nora apparaît)

> Nora, femme d’une trentaine d’années, cheveux bleu nuit très foncé, mi-longs, s’arrêtant aux épaules, raie sur le côté, peau claire, pull à col rond bleu vif uni, pantalon bleu marine, baskets blanches, sans lunettes. Expression attentive et calme, léger sourire quand la situation se résout. Même style de dessin et même apparence que le personnage féminin des références `N10` et `S20`, en illustration vectorielle plate aux traits fins, sans contour noir épais. Si l’ancre `A-NORA` est fournie, Nora reproduit exactement le personnage de cette image. Nora garde la même apparence d’une slide à l’autre.

### Personnages ponctuels (à répéter mot pour mot dans les prompts concernés)

Chaque bloc se termine par la même phrase : « Reprendre le style de dessin des références, pas l’apparence de leurs personnages. »

- **Samuel**, intégrateur de la Maison des Lisières : homme d’une quarantaine d’années, cheveux courts poivre et sel, barbe courte, chemise bleu ciel aux manches retroussées, pantalon gris anthracite. Si l’ancre `A-SAMUEL` est fournie, il la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Malik**, utilisateur de lecteur d’écran : homme d’une cinquantaine d’années, crâne rasé, peau brune, casque audio gris clair, pull vert sauge, assis droit devant un ordinateur portable, mains sur le clavier, expression concentrée et sereine ; aucun attribut caricatural (ni lunettes noires, ni canne au premier plan, ni geste de tâtonnement). Si l’ancre `A-MALIK` est fournie, il la reproduit exactement. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Théo**, participant qui distingue mal le rouge du vert : jeune homme d’une vingtaine d’années, cheveux châtains en bataille, sweat gris clair, tablette en main ; rien dans son apparence ne signale le daltonisme. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Inès**, lectrice dyslexique : adolescente d’environ quinze ans, longs cheveux noirs attachés en queue-de-cheval, gilet lavande, à l’aise et concentrée ; rien dans son apparence ne signale la dyslexie. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.
- **Odette**, voisine de Nora, qui aime annoter le programme sur papier : femme d’environ soixante-quinze ans, cheveux blancs courts, cardigan beige, un crayon à la main, assise bien droite, alerte. Reprendre le style de dessin des références, pas l’apparence de leurs personnages.

### Critères de rejet communs (à reprendre dans chaque prompt)

- Texte manquant, ajouté, déformé ou répété ; faute d’apostrophe, de guillemet, d’accent ou de tiret.
- Cadre, carte, bandeau ou encadré vide, ou portant un texte hors liste.
- En-tête, footer, pagination ou badge inexacts ; reprise de l’en-tête, du footer ou de la numérotation d’une référence.
- Faux logo, URL, adresse ou numéro lisibles hors liste.
- Personnage différent de son bloc ou de son ancre ; représentation caricaturale d’une personne en situation de handicap ou âgée.
- Pour les slides à code : toute différence, caractère par caractère, avec la ligne de code de la liste.

## Exceptions au guide et justification

- **Feuillages en bordure** : le guide écarte les formes organiques décoratives dans les coins. Exception proposée, conforme à la référence Sécurité v4 choisie par Alex : feuillages vectoriels discrets et très pâles en bordure, jamais sous un texte. Validée par Alex le 8 novembre 2026.
- **Fond ivoire presque blanc** au lieu d’un fond blanc strict : écart de teinte minime, repris de la référence.
- **Titre aligné à gauche** avec les masques RÈGLE, COMPARAISON et EXERCICE, comme `N10` et `S20` ; le guide prévoit un titre centré par défaut, conservé avec le `MASQUE LIBRE`. Validée par Alex le 8 novembre 2026.
- **Corail pour l’impact** : nuance douce du rouge que le guide réserve au risque ; même usage, teinte adoucie comme dans la référence.
- **Lignes de code visibles** : neuf slides (S14, S15, S20, S21, S25, S26, S27, S30, S31) affichent une ligne de code courte, exacte, à relire caractère par caractère.
- **Grand cas sans personnage (S36 et S37)** : la scène se limite à la page et à sa feuille imprimée, pour laisser la place aux sept défauts et aux étiquettes ; décision d’Alex (constat I7 de la relecture v002).

## Contrat de fabrication

- **Storyboard-first :** valider ce document, puis seulement préparer les prompts, générer les cinq étalons, S37 en premier, puis la série.
- **Séparation :** le « Texte visible » est projeté et constitue une liste blanche ; le « Discours oral » reste dans les notes et n’entre jamais dans l’image.
- **Une scène par slide :** un personnage agit dans une situation concrète liée à la présentation ; jamais un gabarit vide ; seules S36 et S37 se passent de personnage. Si la fiche décrit une situation (texte justifié, bouton trop petit), l’image la montre telle quelle.
- **Données fictives :** organisation fictive « Maison des Lisières », aucune marque, adresse, téléphone, URL ou personne réels.
- **Règle → préjudice → garantie :** numéro dans le badge et les métadonnées ; à l’oral, la règle est désignée par son objet.
- **QCM originaux :** réponses cachées pendant la projection ; chaque corrigé figure dans les notes de sa slide, sauf S37, correction projetée du grand cas.
- **Sources :** libellés de la checklist V5 servie par le MCP Opquast ; contenu des règles tiré du livre (4e édition 2026, partie 3, rubrique 11), qui fait foi ; glossaire officiel de la thématique Présentation.
- **Portée :** aucune obligation légale nationale n’est affirmée ; les WCAG sont citées comme recommandations internationales, à la suite du livre.
- **Prompts :** chaque prompt reprend mot pour mot le Bloc style, le masque cité par la fiche, les blocs des personnages présents, la fiche PDS, la liste blanche et les critères de rejet.
- **Liste blanche fournie à ImageGen :** dans l’ordre, l’en-tête (`QUALITÉ WEB`, `EXPÉRIENCES DURABLES`, `Opquast`, `DES SITES MEILLEURS POUR TOUS`), le badge résolu s’il existe (par exemple `R. 186`), les chaînes du « Texte visible », le footer `RÈGLES OPQUAST · PRÉSENTATION` et la pagination résolue (par exemple `07 / 40`). La densité de 160 caractères ne compte que le « Texte visible ».
- **Références fournies à chaque génération :** les quatre slides `N01`, `N03`, `N10` et `N17` de `navigation-opquast-v5-360`, plus l’étalon le plus proche de la série ; tant que les étalons ne sont pas validés, l’étalon Sécurité v4 `S20` (`securite-opquast-v5-v4/source/etalons/slide-20.png`). Étalon le plus proche après validation : S01 pour le `MASQUE LIBRE`, S19 pour les slides de règle sans code et les distinctions, S26 pour les slides de règle avec code, S18 pour les checkpoints et les évaluations, S37 pour le grand cas. Chaque fiche désigne une seule « référence de composition principale », que le prompt nomme comme modèle de composition et qui s’ajoute au jeu si elle n’y figure pas ; l’ancre de personnage s’ajoute quand elle existe. Exception : S36, obtenue par édition du PNG de S37.
- **Oral :** rédigé selon les gabarits de `slides-miweb/docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md` ; les consignes d’animation figurent dans « Contrôle et pièges », jamais dans le discours.

## Fabrication du grand cas (S36 et S37)

- **Méthode retenue : la correction d’abord.** S37 est le cinquième étalon et la première image générée de la série, comme une slide ordinaire, avec ses sept pastilles numérotées, ses traits et ses étiquettes ; elle est montrée à Alex avec les quatre autres étalons. Après décision `VALIDEE_PRODUCTION`, S36 est obtenue par un appel ImageGen d’édition de ce PNG validé, qui retire les sept pastilles numérotées, les traits et les étiquettes, et remplace le titre `Correction` par `Grand cas : trouvez sept défauts`. La scène elle-même ne change pas : la pipette et le cartouche `1,8:1` du défaut 4 en font partie et restent.
- **Composition commune :** aucun personnage. La fenêtre de navigateur occupe les deux tiers gauches de la largeur ; la feuille imprimée, en grand et inclinée, occupe le tiers droit, sa barre de menu bien visible ; entre les deux, une colonne étroite reste vide en S36 et reçoit les étiquettes en S37.
- **Justification :** les sept défauts sont plus faciles à vérifier sur la correction, où chacun est désigné et rattaché à sa règle ; une fois S37 validée, la présence et la place de chaque défaut sont acquises. Retirer des repères demande une édition plus simple qu’en ajouter sept, chacun placé sur le bon défaut avec un texte exact. Chaque appel reste une candidate pour une seule slide, et rien n’est superposé par script : le contrat de la Fabrique est respecté.
- **Critères d’acceptation de S36 :** les sept défauts présents, et eux seuls, au même endroit qu’en S37 ; pipette et cartouche `1,8:1` conservés ; aucune pastille numérotée, aucun trait, aucune étiquette résiduels ; le texte `Voir le bouton à droite` inchangé ; titre exact ; aucun personnage. Inspection des deux PNG côte à côte, en pleine résolution.
- **Repli :** si l’outil exposé ne permet pas l’édition d’une image fournie, ou si deux éditions échouent, régénérer S36 en lui fournissant le PNG S37 comme référence principale, avec ce critère de rejet supplémentaire : « aucune pastille numérotée, aucun trait, aucune étiquette » ; puis inspecter côte à côte.
- **Repli inverse :** si S36 régénérée recopie les repères de S37, générer d’abord S36 nue et la valider, puis générer S37 en lui fournissant S36 comme référence principale, en n’ajoutant que les pastilles numérotées, les traits et les étiquettes. En cas d’écart sur un défaut, régénérer la paire et consigner la décision. L’édition dépend de l’outil réellement exposé lors de la production : à vérifier.

## Arc pédagogique

- Acte 0, S01 à S06 : entrer dans l’histoire, contrat, plan, fil rouge, glossaire et méthode.
- Acte 1, S07 à S11 : percevoir (180, 181, 182), distinction couleur et contraste, checkpoint 1.
- Acte 2, S12 à S18 : lire sans les styles (183, 184, 185, 188, 189), distinction couleur, forme et position, checkpoint 2.
- Acte 3, S19 à S23 : agir et adapter (186, 193, 194), distinction zoom et mobile, checkpoint 3.
- Acte 4, S24 à S29 : typographie (187, 190, 191, 192), distinction image de texte, contenu généré et icône de police, checkpoint 4.
- Acte 5, S30 à S32 : imprimer (195, 196) et leur distinction.
- Acte 6, S33 à S40 : s’entraîner : transversalité, évaluation finale, grand cas et correction, mémo, conclusion, ressources.

Ce découpage en actes est un regroupement pédagogique original, pas une catégorie officielle Opquast.

## Sources et couverture

| Règle | Libellé exact (checklist V5, MCP Opquast, 7 novembre 2026) | Slide dédiée | Exercice corrigé |
|---|---|---|---|
| 180 | La charte graphique est cohérente sur toutes les pages. | S07 | S11 C |
| 181 | L’information n’est pas véhiculée uniquement par la couleur. | S08 | S11 A, S34 Q2, S34 Q4, S37 |
| 182 | Les contenus sont présentés avec un contraste suffisant par rapport à leur arrière-plan. | S09 | S11 B, S34 Q1, S37 |
| 183 | Le contenu et le sens de chaque page ne sont pas altérés lorsque les styles sont désactivés. | S12 | S18 A |
| 184 | Un contenu n’est pas désigné uniquement par sa forme ou par sa position à l’écran. | S13 | S34 Q3, S37 |
| 185 | Un contenu qui doit être restitué dans un lecteur d’écran ne lui est pas dissimulé. | S14 | S18 B |
| 186 | La taille des éléments cliquables est suffisante. | S19 | S23 A, S37 |
| 187 | Les textes pouvant être mis en forme via des styles ne sont pas remplacés par des images. | S24 | S29 A, S37 |
| 188 | Les contenus générés via les styles sont dotés d’une alternative appropriée. | S15 | S18 C |
| 189 | Les pictogrammes typographiques sont dotés d’une alternative appropriée. | S16 | S18 D |
| 190 | Une famille générique de police est indiquée comme dernier élément de substitution. | S25 | S29 B |
| 191 | Les styles ne justifient pas le texte. | S26 | S29 C, S37 |
| 192 | Les mises en majuscules à des fins décoratives sont effectuées à l’aide des styles. | S27 | S29 D |
| 193 | Les fonctionnalités de zoom ne sont pas bloquées. | S20 | S23 B, S35 Q7 |
| 194 | Un ou plusieurs mécanismes dédiés à l’adaptation aux terminaux mobiles sont proposés. | S21 | S23 C, S35 Q8 |
| 195 | Des styles dédiés à l’impression sont proposés. | S30 | S35 Q5 |
| 196 | Le contenu de chaque page est disponible à l’impression sans blocs de navigation. | S31 | S35 Q6, S37 |

Règles connexes, reliées par un passage du livre (rubrique 11), libellés relus dans la checklist V5 :

| Règle | Libellé exact | Lien établi par le livre | Slide |
|---|---|---|---|
| 157 | Les items actifs de menu sont signalés. | Contrôle de la règle sur la couleur : « un menu de navigation où la rubrique en cours ne se différencie que par sa couleur ». | S33 |
| 140 | Les liens sont visuellement différenciés du reste du contenu. | Avis de l’expert sur le contraste : exigence de contraste entre liens et texte courant « si ces liens ne sont différenciés que par la couleur ». | S33 |
| 158 | Les blocs de navigation de même nature sont affichés aux mêmes emplacements sur toutes les pages. | Contrôle de la charte graphique : « la présence et l’emplacement des menus de navigation ». | S33 |
| 136 | Chaque lien est doté d’un intitulé dans le code source. | Avis de l’expert sur les pictogrammes typographiques : « inclure dans le contenu du lien un libellé explicite masqué à l’affichage ». | S33 |
| 69 | Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. | Avis de l’expert sur les styles désactivés : champs et étiquettes placés à l’écran « sans qu’ils soient effectivement associés dans le code HTML ». | S12 et S33 (oral) |

Sources détaillées, par ordre d’autorité : `sources/opquast/livre-rubrique-11-presentation.md` (fait foi) ; `sources/opquast/libelles-180-196-2026-11-07.md` ; checklist V5 servie par le MCP Opquast le 7 novembre 2026 pour les libellés connexes ; `sources/opquast/glossaire-presentation-2026-11-07.md`.

## Storyboard détaillé

### S01 — Présentation selon Opquast V5

- **Acte :** 0. Entrer dans l’histoire
- **Type :** ouverture
- **Durée indicative :** 1:00
- **Objectif pédagogique :** faire ressentir qu’une page peut être juste sur le fond et pourtant illisible selon le contexte de lecture.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : ouvrir la série par une situation vécue, avant toute règle.
- Idée principale : la présentation d’une page sert ou dessert le contenu selon la personne et le contexte.
- Scène : qui, Nora ; où, sur un banc en plein soleil, devant la Maison des Lisières ; objet, son téléphone affichant le programme des ateliers ; tension, le texte pâle s’efface au soleil ; action, elle plisse les yeux et écarte deux doigts sur l’écran ; résultat, la page ne s’agrandit pas, un petit point d’interrogation corail apparaît près de l’écran.
- Transformation visible : aucune encore ; la slide pose la question, la série y répondra.
- Test des trois secondes : « Elle n’arrive pas à lire ce site sur son téléphone. »
- Ajout par rapport à la slide précédente : première slide.

**Référence de composition principale :** `N01` (composition d’ouverture centrée, feuillages).

**Texte visible (projection)**

- `Présentation selon Opquast V5`
- `La forme sert le fond, pour chacun`
- `17 règles · 180 à 196`

**Illustration :** titre et slogan centrés en haut. Au centre, Nora (Bloc personnage) assise sur un banc de bois, un soleil stylisé jaune pâle en haut à droite. Son téléphone, agrandi en médaillon à côté d’elle, montre des lignes gris très pâle sur fond blanc, presque effacées ; Nora plisse les yeux et écarte le pouce et l’index sur l’écran. Derrière, la façade simplifiée d’une petite maison culturelle aux volets bleu marine, sans enseigne. `17 règles · 180 à 196` dans un cartouche bleu clair sous la scène.

**Alternative textuelle à fournir :** Nora, assise au soleil, plisse les yeux devant le texte pâle de son téléphone et tente en vain de l’agrandir.

**Règle → préjudice utilisateur :** une page dont la présentation ignore le contexte de lecture devient illisible ou inutilisable, même si son contenu est juste.

**Garantie recherchée (matière de l’oral)**

La présentation vise à rendre le même contenu lisible et utilisable par chacun, quel que soit son écran, sa vue ou son outil.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : demander au public ce qui pourrait empêcher Nora de lire cette page.
- Piège certification : la rubrique Présentation ne juge pas le goût graphique ; le livre le dit dès la première règle, « beau ou moche, c’est subjectif ».

**Discours oral du présentateur (non projeté)**

#### Une page juste peut rester illisible

- Nora veut s’inscrire à un atelier depuis un banc, en plein soleil.
- Le texte gris pâle s’efface, et la page refuse de s’agrandir.
- Le contenu est complet et exact, et pourtant il ne lui parvient pas.
- La rubrique Présentation ne parle pas de beauté, qui reste subjective.
- Elle parle de ce qui permet au contenu d’arriver jusqu’à chacun : couleurs, contrastes, styles, tailles, typographie, impression.

#### Transition

- Lire une page avec d’autres yeux s’apprend : reconnaître, distinguer, vérifier.

**Mémo oral :** la forme sert le fond, pour chacun.

**Fichier final prévu :** `finals/slide-01-ouverture.png` (devient l’ancre `A-NORA` après validation).

---

### S02 — Notre contrat : reconnaître, distinguer, vérifier

- **Acte :** 0. Entrer dans l’histoire
- **Type :** objectif
- **Durée indicative :** 0:45
- **Objectif pédagogique :** annoncer les compétences visées pour la certification sans promettre le résultat de l’examen.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : poser le contrat d’apprentissage.
- Idée principale : reconnaître une situation, la distinguer d’une situation voisine, la vérifier.
- Scène : qui, Nora, trois fois ; où, dans trois mini-scènes côte à côte ; objet, une page du site ; tension, trois gestes à acquérir ; action, à gauche Nora observe une page à la loupe, au centre elle compare deux pages posées côte à côte, à droite elle coche une case sur une fiche de contrôle ; résultat, trois gestes enchaînés par des flèches fines.
- Transformation visible : de l’observation à la vérification.
- Test des trois secondes : « Trois étapes : reconnaître, distinguer, vérifier. »
- Ajout par rapport à la slide précédente : après la situation, le programme de travail.

**Référence de composition principale :** `N17` (progression horizontale avec personnage). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Notre contrat : reconnaître, distinguer, vérifier`
- `17 règles · 4 checkpoints · 8 questions · 1 grand cas`

**Illustration :** trois panneaux pastel reliés par des flèches fines, sans texte. Panneau bleu clair : Nora (Bloc personnage) penchée avec une loupe sur une page abstraite. Panneau lavande : Nora tient deux pages abstraites côte à côte et les compare. Panneau vert : Nora coche une case sur une fiche. Le compteur `17 règles · 4 checkpoints · 8 questions · 1 grand cas` dans un bandeau bleu clair en bas.

**Alternative textuelle à fournir :** Nora reconnaît, compare puis vérifie : trois étapes d’apprentissage pour 17 règles, 4 checkpoints, 8 questions et un grand cas.

**Règle → préjudice utilisateur :** mémoriser des libellés sans reconnaître les situations mène aux confusions entre règles voisines.

**Garantie recherchée (matière de l’oral)**

Les cas concrets et les choix argumentés construisent une compréhension durable.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : annoncer que chaque checkpoint a son corrigé.
- Piège certification : les questions de cette formation sont des exercices originaux, pas des questions officielles d’examen.

**Discours oral du présentateur (non projeté)**

#### Reconnaître, distinguer, vérifier

- Face à une page réelle, il s’agit d’abord de reconnaître la situation en jeu.
- Il faut ensuite la distinguer d’une situation voisine, par exemple la couleur seule et le contraste.
- Enfin, chaque règle a son contrôle : désactiver, mesurer, inspecter, zoomer ou imprimer.
- Distinguer évite d’appliquer le bon correctif au mauvais défaut.

#### Transition

- Pour reconnaître, il faut d’abord savoir où regarder.

**Mémo oral :** reconnaître, distinguer, vérifier.

**Fichier final prévu :** `finals/slide-02-contrat.png`

---

### S03 — Six actes pour parcourir la présentation

- **Acte :** 0. Entrer dans l’histoire
- **Type :** plan
- **Durée indicative :** 0:40
- **Objectif pédagogique :** donner la carte de la séance.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : plan.
- Idée principale : cinq gestes de lecture, puis l’entraînement.
- Scène : qui, Nora ; où, sur un sentier qui traverse six panneaux pastel ; objet, le sentier ondulé ; tension, aucune ; action, Nora marche vers le premier panneau ; résultat, le sentier mène à un panneau final vert.
- Transformation visible : du premier acte au dernier.
- Test des trois secondes : « La séance avance en six étapes. »
- Ajout par rapport à la slide précédente : l’ordre du parcours.

**Référence de composition principale :** `N17` (composition très proche). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Six actes pour parcourir la présentation`
- `1. Percevoir`
- `2. Lire sans les styles`
- `3. Agir et adapter`
- `4. Typographie`
- `5. Imprimer`
- `6. S’entraîner`

**Illustration :** composition proche de la référence N17. Six panneaux pastel alignés, chacun titré de son acte et illustré d’une mini-scène sans texte : 1, un œil et un soleil devant un écran ; 2, une page sans mise en forme, lignes empilées ; 3, une main qui touche un téléphone ; 4, un bloc de lignes alignées à gauche et un petit pinceau ; 5, une imprimante et une feuille ; 6, une coche verte et un carnet. Un sentier ondulé relie les panneaux par des pastilles colorées. Nora (Bloc personnage) marche sur le sentier, devant le premier panneau.

**Alternative textuelle à fournir :** plan en six actes : percevoir, lire sans les styles, agir et adapter, typographie, imprimer, s’entraîner.

**Règle → préjudice utilisateur :** sans carte, les dix-sept règles paraissent une liste sans logique.

**Garantie recherchée (matière de l’oral)**

Regrouper les règles par geste de lecture aide à les retrouver.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : vérifier sur le PNG les six libellés et leur ordre.
- Piège certification : ce regroupement en actes est pédagogique ; la checklist Opquast ne connaît pas ces catégories.

**Discours oral du présentateur (non projeté)**

#### Cinq gestes de lecture, puis l’entraînement

- Percevoir : couleurs, contrastes, cohérence graphique.
- Lire sans les styles : ce qui reste quand la mise en forme disparaît, pour un lecteur d’écran ou un robot.
- Agir et adapter : toucher, zoomer, changer d’écran.
- Typographie : textes en image, polices, alignement, majuscules.
- Imprimer : le passage de l’écran au papier.
- S’entraîner : relier les règles entre elles, puis les éprouver sur des cas.
- La checklist Opquast ne regroupe pas les règles ainsi : ces gestes servent seulement à les retenir.

#### Transition

- Ces gestes s’exercent tous sur un même lieu et son site.

**Mémo oral :** cinq gestes, puis l’entraînement.

**Fichier final prévu :** `finals/slide-03-plan.png`

---

### S04 — Le fil rouge : la Maison des Lisières

- **Acte :** 0. Entrer dans l’histoire
- **Type :** fil rouge
- **Durée indicative :** 1:00
- **Objectif pédagogique :** installer le terrain fictif commun à toute la série.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : présenter l’organisation fictive et son site.
- Idée principale : toutes les situations se passent sur le site d’un lieu culturel fictif.
- Scène : qui, Nora ; où, devant la façade de la Maison des Lisières ; objet, son téléphone et trois pages du site ; tension, aucune ; action, Nora consulte le programme ; résultat, trois vignettes de pages s’ouvrent en éventail.
- Transformation visible : du lieu au site qui le représente.
- Test des trois secondes : « Un lieu culturel et son site, avec trois pages. »
- Ajout par rapport à la slide précédente : le terrain des exercices.

**Référence de composition principale :** `N01` (pastilles autour d’un écran central). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Le fil rouge : la Maison des Lisières`
- `Un lieu culturel fictif et son site`
- `Programme`
- `Inscription`
- `Plan d’accès`

**Illustration :** à gauche, la façade d’une petite maison culturelle, volets bleu marine, auvent vert pâle, sans enseigne ni texte. Nora (Bloc personnage) devant la porte, téléphone en main. À droite, trois vignettes de pages en éventail, chacune titrée : `Programme` (cartes d’ateliers abstraites), `Inscription` (formulaire abstrait), `Plan d’accès` (petit plan stylisé). Aucun logo, aucune adresse, aucune URL.

**Alternative textuelle à fournir :** la Maison des Lisières, lieu culturel fictif, et trois pages de son site : programme, inscription et plan d’accès ; Nora le consulte sur son téléphone.

**Règle → préjudice utilisateur :** sans terrain commun, chaque exemple repart de zéro.

**Garantie recherchée (matière de l’oral)**

Un même site vu sous des angles différents montre que les règles se combinent.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : aucun texte, logo ou coordonnée réels sur le PNG.
- Piège certification : aucun.

**Discours oral du présentateur (non projeté)**

#### Un lieu, un site, six personnes

- La Maison des Lisières est un lieu culturel imaginaire : ateliers de reliure, de photo, de lecture.
- Son site compte trois pages utiles : le programme, l’inscription et le plan d’accès.
- Nora le consulte surtout sur son téléphone ; Samuel, l’intégrateur, le maintient.
- Théo distingue mal le rouge du vert ; Malik utilise un lecteur d’écran ; Inès est dyslexique.
- Odette, la voisine de Nora, aime annoter le programme sur papier.

#### Transition

- Ce que vivent ces personnes se décrit avec quelques mots précis.

**Mémo oral :** un lieu, un site, six personnes.

**Fichier final prévu :** `finals/slide-04-fil-rouge.png`

---

### S05 — Six mots pour toute la séance

- **Acte :** 0. Entrer dans l’histoire
- **Type :** glossaire
- **Durée indicative :** 1:00
- **Objectif pédagogique :** partager le vocabulaire officiel utile aux règles.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : glossaire.
- Idée principale : six notions du glossaire officiel reviennent dans toute la rubrique.
- Scène : qui, Nora ; où, à une table de la bibliothèque de la Maison des Lisières ; objet, un carnet ouvert ; tension, aucune ; action, Nora épingle la sixième vignette au-dessus de la table ; résultat, six vignettes illustrées et titrées alignées.
- Transformation visible : les six notions réunies.
- Test des trois secondes : « Six mots à connaître. »
- Ajout par rapport à la slide précédente : le vocabulaire.

**Référence de composition principale :** `N17` (panneaux pastel titrés). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Six mots pour toute la séance`
- `Charte graphique`
- `Désactivation des styles`
- `Linéarisation`
- `Ratio de contraste`
- `Zoom graphique`
- `Point de rupture`

**Illustration :** Nora (Bloc personnage) debout à gauche, bras levé, épinglant une vignette sur une grande planche claire. Six vignettes pastel en deux rangées de trois, chacune avec son terme et une mini-illustration sans texte : une palette et une page aux couleurs communes ; une page sans mise en forme, lignes empilées ; des blocs qui se déroulent en une seule colonne ordonnée ; deux pastilles, sombre et claire, sur une petite balance ; une loupe sur une page entière ; un téléphone et un ordinateur dont la page passe d’une colonne à trois.

**Alternative textuelle à fournir :** six notions du glossaire : charte graphique, désactivation des styles, linéarisation, ratio de contraste, zoom graphique et point de rupture.

**Règle → préjudice utilisateur :** un terme mal compris produit un contrôle mal ciblé.

**Garantie recherchée (matière de l’oral)**

Parler le vocabulaire du glossaire Opquast évite les contresens.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : définitions reprises du glossaire officiel de la thématique Présentation, résumées sans en changer le sens.
- Piège certification : zoom graphique et zoom typographique sont distincts ; la règle sur le zoom vise le zoom graphique.

**Discours oral du présentateur (non projeté)**

#### Six notions du glossaire officiel

- Charte graphique : l’ensemble des signes qui forment l’identité visuelle, logo, polices, couleurs.
- Désactivation des styles : la page rendue avec les seuls styles par défaut du navigateur, qui donne une idée de ce qu’exploite un robot ou un lecteur d’écran.
- Linéarisation : la page lue dans l’ordre du code source, et non dans l’ordre visible à l’écran.
- Ratio de contraste : la mesure de l’écart de luminosité entre un texte et son fond, selon l’algorithme des WCAG 2.0.
- Zoom graphique : il agrandit tout, textes et images, à la différence du zoom typographique, limité aux caractères.
- Point de rupture : le palier où une page adaptative bascule d’un ensemble de styles à un autre.

#### Transition

- Ces notions servent à des gestes de contrôle précis.

**Mémo oral :** six mots, une langue commune.

**Fichier final prévu :** `finals/slide-05-glossaire.png`

---

### S06 — Cinq gestes de vérification

- **Acte :** 0. Entrer dans l’histoire
- **Type :** méthode
- **Durée indicative :** 1:00
- **Objectif pédagogique :** montrer les gestes de contrôle que le livre associe aux règles de la rubrique.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : méthode de contrôle.
- Idée principale : cinq gestes concrets mènent la plupart des contrôles de la rubrique.
- Scène : qui, Samuel ; où, à son bureau, deux écrans côte à côte ; objet, la même page avec et sans mise en forme ; tension, il faut voir la page autrement ; action, Samuel compare les deux écrans ; résultat, cinq cartes de gestes s’alignent en bas.
- Transformation visible : de la page vue normalement à cinq façons de l’éprouver.
- Test des trois secondes : « On vérifie en désactivant, en mesurant, en inspectant, en zoomant et en imprimant. »
- Ajout par rapport à la slide précédente : après les mots, les gestes.

**Référence de composition principale :** `S20` (personnage devant deux fenêtres).

**Texte visible (projection)**

- `Cinq gestes de vérification`
- `Désactiver couleurs et styles`
- `Mesurer le contraste`
- `Inspecter le code`
- `Zoomer sur un écran tactile`
- `Prévisualiser l’impression`

**Illustration :** Samuel (bloc Samuel) assis à un bureau, deux écrans : à gauche la page mise en forme, à droite la même page en niveaux de gris et sans mise en forme, lignes empilées. En bas, cinq cartes pastel à icône, chacune portant un geste : interrupteur, deux pastilles comparées, chevrons de code, deux doigts qui écartent, imprimante.

**Alternative textuelle à fournir :** Samuel compare une page avec et sans mise en forme ; cinq gestes de contrôle : désactiver couleurs et styles, mesurer le contraste, inspecter le code, zoomer sur un écran tactile, prévisualiser l’impression.

**Règle → préjudice utilisateur :** un contrôle mené seulement sur son propre écran ne voit pas ce que vivent les autres.

**Garantie recherchée (matière de l’oral)**

Changer de point de vue sur la page révèle des pertes d’information autrement invisibles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : chaque geste vient des contrôles du livre (couleurs et styles désactivés, outil de contraste, inspecteur de code, zoom tactile, aperçu avant impression).
- Piège certification : l’aperçu avant impression ne suffit pas à confirmer la présence de styles d’impression ; le livre demande aussi l’examen du code.

**Discours oral du présentateur (non projeté)**

#### Cinq gestes tirés du livre

- Désactiver les couleurs, puis les styles, et comparer : le livre conseille un double écran.
- Mesurer le contraste avec un outil dédié plutôt qu’à l’œil.
- Inspecter le code : polices, alignement, contenus masqués ou générés.
- Zoomer du bout des doigts sur un écran tactile.
- Prévisualiser l’impression, puis confirmer au code quand la règle le demande.
- Dans les cas concrets, c’est souvent le geste qui révèle le défaut qui désigne la règle.

#### Transition

- Le premier repère est ce que l’on perçoit.

**Mémo oral :** désactiver, mesurer, inspecter, zoomer, imprimer.

**Fichier final prévu :** `finals/slide-06-methode.png` (devient l’ancre `A-SAMUEL` après validation).

---

### S07 — Une même identité, de page en page

- **Acte :** 1. Percevoir
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une rupture de charte graphique entre pages, notamment due à un service tiers.
- **Badge :** `R. 180`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la cohérence de la charte graphique, ouverture de l’acte 1.
- Idée principale : une page qui change d’univers graphique donne l’impression d’avoir quitté le site.
- Scène : qui, Nora ; où, chez elle, devant son ordinateur portable ; objet, la page Programme puis la page de paiement fournie par un prestataire ; tension, la seconde page n’a plus les couleurs, la police ni la largeur du site ; action, Nora s’arrête, la main suspendue ; résultat, elle hésite à poursuivre.
- Transformation visible : deux pages sans rien de commun, reliées par une flèche corail interrompue.
- Test des trois secondes : « Ces deux pages ne semblent pas venir du même site. »
- Ajout par rapport à la slide précédente : premier contrôle appliqué, comparer les pages entre elles.

**Référence de composition principale :** `S20` (personnage et deux fenêtres). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Acte 1 · Percevoir`
- `Une même identité, de page en page`
- `IMPACT - Je crois avoir quitté le site`
- `GARANTIE - Menus, styles et largeurs restent cohérents`

**Illustration :** Nora (Bloc personnage) à gauche, devant un ordinateur portable, regard perplexe. À droite, deux fenêtres côte à côte. Gauche : page aux couleurs du site, bandeau bleu marine, cartes vert pâle, colonne de largeur moyenne. Droite : page de paiement d’un prestataire, fond gris, champs violet vif, pleine largeur, blocs plus étroits suggérant une autre police. Une flèche corail en pointillés, interrompue au milieu, relie les deux. Blocs abstraits sans texte.

**Alternative textuelle à fournir :** Nora passe de la page Programme à une page de paiement tierce aux couleurs, à la police et à la largeur différentes, et croit avoir quitté le site.

**Règle → préjudice utilisateur :** un changement brutal d’univers graphique fait douter de l’identité du service et peut interrompre la visite.

**Garantie recherchée (matière de l’oral)**

Homogénéité et continuité de la visite, identification permanente du service visité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : au fil des autres contrôles, vérifier des éléments graphiques communs à toutes les pages : présence et emplacement des menus, couleur des sections, largeur des pages, charte des titres et des textes ; vérifier aussi après l’intégration de services tiers.
- Piège certification : la règle ne juge pas la beauté. Selon l’avis de l’expert, elle peut ne pas être retenue pour des contenus archivés qu’une refonte de la charte n’a pas couverts.

**Discours oral du présentateur (non projeté)**

#### Un service tiers qui casse la continuité

- La page de paiement est fournie par un prestataire et n’a plus les couleurs, la police ni la largeur du site.
- Beau ou non, c’est subjectif ; mais l’univers graphique doit rester cohérent d’une page à l’autre.
- La solution : des feuilles de styles communes à tout le site.
- L’avis de l’expert insiste sur la rigueur du wireframing et des maquettes, et sur une intégration transparente des services embarqués.

##### Impact du non-respect

- L’utilisateur croit avoir quitté le service et hésite à poursuivre.

##### Ce que garantit la règle

- Une visite homogène et continue, et un service identifiable à chaque page.
- Exception possible : des contenus archivés qu’une refonte n’a pas couverts.

#### Transition

- La couleur sert l’identité ; elle peut aussi porter une information.

**Mémo oral :** une page, un même site.

**Fichier final prévu :** `finals/slide-07-charte-coherente.png`

---

### S08 — Obligatoire, pas seulement en rouge

- **Acte :** 1. Percevoir
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une information portée uniquement par la couleur et connaître les compléments possibles.
- **Badge :** `R. 181`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur l’information véhiculée par la couleur.
- Idée principale : une information que seule la couleur porte échappe à qui ne distingue pas cette couleur.
- Scène : qui, Théo ; où, dans le hall de la Maison des Lisières, sur une tablette ; objet, le formulaire d’inscription ; tension, l’étiquette du champ obligatoire est rouge et les autres vert foncé, de même luminosité, et Théo distingue mal le rouge du vert ; action, il envoie le formulaire sans remplir ce champ ; résultat, à droite, l’étiquette porte un astérisque, Théo remplit le champ, coche verte.
- Transformation visible : la même étiquette, d’abord distinguée par la seule teinte, puis doublée d’un astérisque.
- Test des trois secondes : « Le rouge ne suffit pas, l’astérisque oui. »
- Ajout par rapport à la slide précédente : de la cohérence d’ensemble à une information précise.

**Référence de composition principale :** `N10` (personnage et formulaire).

**Texte visible (projection)**

- `Obligatoire, pas seulement en rouge`
- `Nom *`
- `IMPACT - Sans distinguer le rouge, je rate le champ`
- `GARANTIE - Un signe ou un mot double la couleur`

**Illustration :** Théo (bloc Théo) à gauche, tablette en main. Deux panneaux. Panneau corail pâle : formulaire de trois champs, étiquettes en barres abstraites, deux vert foncé et une rouge de même luminosité ; champ rouge resté vide, petite croix corail. Panneau vert pâle : même formulaire, l’étiquette du deuxième champ lisible `Nom *`, champ rempli, coche verte.

**Alternative textuelle à fournir :** Théo, qui distingue mal le rouge du vert, ne repère pas un champ obligatoire signalé par la seule couleur ; avec un astérisque, il le remplit.

**Règle → préjudice utilisateur :** sans distinguer la couleur, l’utilisateur ne reçoit pas l’information, ici le caractère obligatoire d’un champ, et échoue dans sa démarche.

**Garantie recherchée (matière de l’oral)**

L’information reste accessible quand la couleur n’est pas perçue ou pas restituée : daltonisme, aide technique, navigateur, robot d’indexation.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : comparer la page normale et la même page sans couleurs, images en niveaux de gris, de préférence sur deux écrans ; chercher les pertes d’information, comme un menu où la rubrique en cours ne diffère que par sa couleur ou une carte en aplats sans bordure ni motif.
- Piège certification : une infobulle `title` ne compte pas comme complément, son accès au clavier n’étant pas assuré partout. La règle n’interdit pas la couleur : elle interdit qu’elle soit seule.
- Revue : aucune vue en niveaux de gris dans l’image ; le contrôle sans couleurs reste à l’oral.

**Discours oral du présentateur (non projeté)**

#### Un champ obligatoire signalé en rouge

- Le livre prend cet exemple : un champ obligatoire signalé en rouge pourra ne pas être perçu par tous.
- Théo distingue mal le rouge du vert : pour lui, cette étiquette ne se détache pas des autres.
- La couleur reste utile à l’ergonomie ; la règle demande seulement qu’elle ne soit pas seule.
- Compléments cités par le livre : un balisage d’emphase, une mention textuelle comme l’astérisque, des hachures, motifs ou bordures dans les cartes et graphiques.
- Une infobulle ne suffit pas : son accès au clavier n’est pas assuré dans tous les navigateurs.

##### Impact du non-respect

- L’information échappe à qui ne distingue pas la couleur, et la démarche échoue.

##### Ce que garantit la règle

- Une information indépendante de la perception des couleurs et de la restitution de la mise en forme.

#### Transition

- Même bien codée, une information doit encore être lisible sur son fond.

**Mémo oral :** la couleur aide, elle ne parle pas seule.

**Fichier final prévu :** `finals/slide-08-couleur-seule.png`

---

### S09 — Lisible même en plein soleil

- **Acte :** 1. Percevoir
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître un contraste insuffisant et connaître le seuil retenu par le livre et sa mesure.
- **Badge :** `R. 182`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur le contraste du texte avec son arrière-plan.
- Idée principale : un texte trop pâle sur son fond s’efface, pour tout le monde.
- Scène : qui, Nora ; où, debout à un arrêt de bus en plein soleil ; objet, les horaires des ateliers sur son téléphone ; tension, les horaires gris pâle sur ivoire disparaissent ; action, Nora approche l’écran ; résultat, à droite, horaires bleu marine nets, elle lit sans effort.
- Transformation visible : du texte presque effacé au texte net, départagés par une pastille de ratio.
- Test des trois secondes : « Texte pâle illisible, texte foncé lisible. »
- Ajout par rapport à la slide précédente : après le sens porté par la couleur, la lisibilité du texte.

**Référence de composition principale :** `N03` (deux panneaux). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Lisible même en plein soleil`
- `Ratio visé : au moins 3:1`
- `IMPACT - Le texte pâle s’efface au soleil`
- `CONTRÔLE - Mesurer le ratio avec un outil dédié`

**Illustration :** Nora (Bloc personnage) au centre, debout près d’un poteau d’arrêt de bus stylisé sans aucune inscription, soleil stylisé jaune pâle en haut à gauche. Deux médaillons de téléphone. Gauche, cadre corail pâle : lignes gris très pâle sur ivoire, presque invisibles. Droite, cadre vert pâle : mêmes lignes en bleu marine foncé, nettes, coche verte. Entre les deux, une petite pipette, deux pastilles comparées et le cartouche `Ratio visé : au moins 3:1`. Horaires en barres abstraites, sans chiffres.

**Alternative textuelle à fournir :** à un arrêt de bus, en plein soleil, Nora ne lit pas des horaires gris pâle sur ivoire ; en bleu marine, avec un contraste mesuré d’au moins 3 pour 1, ils deviennent lisibles.

**Règle → préjudice utilisateur :** un contraste faible rend la lecture difficile et fatigante, davantage encore pour les personnes malvoyantes ou dans une lumière forte.

**Garantie recherchée (matière de l’oral)**

Bonne lisibilité, charge mentale limitée, meilleure accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : repérer les textes au contraste douteux ; relever les couleurs avec un outil du type Colour Contrast Analyser ; vérifier un ratio d’au moins 3:1 (algorithme WCAG 2.0) ; sur fond en dégradé, motif ou photo, mesurer au point le plus défavorable ; tenir compte du zoom texte.
- Piège certification : le livre retient 3:1 quelles que soient taille et graisse ; les WCAG 2.0 au niveau AA exigent 4,5:1 pour le texte courant et réservent 3:1 aux textes agrandis et en gras.

**Discours oral du présentateur (non projeté)**

#### Un seuil mesuré, pas une impression

- On croit souvent le contraste réservé aux personnes malvoyantes ; le livre rappelle qu’un contraste suffisant est plus agréable pour tout le monde.
- La règle retient un ratio minimal de 3 pour 1, mesuré avec l’algorithme des WCAG 2.0.
- On relève couleur du texte et couleur du fond avec un outil dédié ; sur un fond en dégradé ou photographique, au point le plus défavorable.
- Ce seuil est plus souple que celui des WCAG au niveau AA, qui demandent 4,5 pour 1 pour le texte courant : un objectif de conformité WCAG appelle ce seuil-là.

##### Impact du non-respect

- Le texte s’efface, la lecture fatigue, et une partie du public ne lit plus.

##### Ce que garantit la règle

- Un texte qui se détache de son fond selon un seuil mesurable, sans valoir conformité WCAG.

#### Transition

- Couleur seule et contraste se confondent souvent ; ce sont pourtant deux défauts distincts.

**Mémo oral :** on mesure, on ne devine pas.

**Fichier final prévu :** `finals/slide-09-contraste.png`

---

### S10 — Couleur seule ou contraste : deux défauts

- **Acte :** 1. Percevoir
- **Type :** distinction
- **Durée indicative :** 0:50
- **Objectif pédagogique :** distinguer l’information portée par la seule couleur et le texte trop peu contrasté.
- **Badge :** `R. 181 · 182`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : distinction entre deux règles de perception.
- Idée principale : dans un cas la couleur porte seule un sens ; dans l’autre, le texte se détache mal de son fond.
- Scène : qui, Nora ; où, devant deux écrans posés sur une table ; objet, à gauche un calendrier d’ateliers, à droite un paragraphe ; tension, deux « problèmes de couleur » différents ; action, Nora pose une carte de contrôle sous chaque écran ; résultat, chaque défaut est nommé.
- Transformation visible : une même impression se sépare en deux diagnostics.
- Test des trois secondes : « Deux problèmes de couleur qui ne sont pas les mêmes. »
- Ajout par rapport à la slide précédente : la comparaison des deux règles.

**Référence de composition principale :** `N03` (deux panneaux et bandeau final). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Couleur seule ou contraste : deux défauts`
- `La couleur porte seule le sens`
- `Le texte se détache mal du fond`
- `Deux contrôles : sans couleurs, puis mesure du ratio`

**Illustration :** Nora (Bloc personnage) au centre, de trois quarts, entre deux panneaux. Panneau lavande, titré `La couleur porte seule le sens` : un calendrier de cases abstraites, pastilles rouges et vertes de même luminosité, sans autre signe. Panneau bleu clair, titré `Le texte se détache mal du fond` : un paragraphe de lignes gris très pâle sur blanc. Bandeau vert pâle à icône de coche : `Deux contrôles : sans couleurs, puis mesure du ratio`.

**Alternative textuelle à fournir :** deux défauts distincts : un calendrier où seule la couleur distingue les dates, et un texte trop pâle sur son fond ; deux contrôles différents.

**Règle → préjudice utilisateur :** confondre les deux règles conduit à un mauvais correctif.

**Garantie recherchée (matière de l’oral)**

Choisir le bon contrôle pour le bon défaut.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : couleur seule, désactiver les couleurs et chercher une perte d’information ; contraste, mesurer le ratio.
- Piège certification : pour un lien différencié du texte par la seule couleur, l’avis de l’expert sur le contraste suggère alors un contraste entre lien et texte ; la différenciation des liens relève aussi de la rubrique Liens (S33).

**Discours oral du présentateur (non projeté)**

#### Deux défauts que l’on résume trop vite

- À gauche, la couleur porte seule une information : rouge, complet ; vert, libre.
- Sans percevoir la différence, l’information disparaît : on vérifie en supprimant les couleurs.
- À droite, rien n’est codé par la couleur, mais le texte se détache mal de son fond : on vérifie en mesurant.
- Un texte peut être bien contrasté et porter une information par la seule couleur ; l’inverse existe aussi.

#### Transition

- Une information perdue, un texte illisible, une identité rompue : trois pertes, trois règles.

**Mémo oral :** sens porté par la couleur, ou lisibilité du texte ?

**Fichier final prévu :** `finals/slide-10-distinction-couleur-contraste.png`

---

### S11 — Checkpoint 1 : percevoir

- **Acte :** 1. Percevoir
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** réactiver les trois règles de l’acte 1 par des situations.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : checkpoint de l’acte 1.
- Idée principale : rattacher chaque situation à sa règle.
- Scène : qui, Nora ; où, à une table ; objet, trois cartes de situation ; tension, trois défauts à classer ; action, Nora réfléchit, crayon en main ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Un exercice en trois cas. »
- Ajout par rapport à la slide précédente : l’apprenant applique.

**Référence de composition principale :** `N17` (cartes pastel alignées). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Checkpoint 1 : percevoir`
- `Quelle règle est en jeu ?`
- `A. Champ obligatoire en rouge seul`
- `B. Horaires gris pâle sur ivoire`
- `C. Paiement : autres couleurs, autre police`

**Illustration :** question dans un bandeau bleu clair sous le titre. Trois cartes pastel A, B, C, chacune portant sa ligne et une mini-scène sans autre texte : A, un formulaire dont une étiquette est une barre rouge ; B, des lignes gris très pâle sur ivoire ; C, deux pages côte à côte, la seconde d’autres couleurs. Nora (Bloc personnage) à gauche, crayon levé. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** exercice : trois situations du site à rattacher chacune à une règle de perception.

**Règle → préjudice utilisateur :** une situation mal rattachée mène à un mauvais correctif.

**Garantie recherchée (matière de l’oral)**

Rattacher le défaut à sa règle avant de chercher la solution.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 45 secondes de réflexion avant le corrigé.
- Piège certification : en B, aucune information n’est codée par la couleur ; répondre « couleur seule » est le distracteur attendu.

**Discours oral du présentateur (non projeté)**

#### Trois pertes différentes

- Dans chaque cas, l’utilisateur perd quelque chose : une information, la lisibilité, ou le sentiment d’être sur le même site.
- Cette perte désigne la règle.

#### Transition

- Que reste-t-il d’une page quand la mise en forme disparaît ?

**Corrigé (notes du présentateur, non projeté) :** A → 181 : le caractère obligatoire n’est porté que par la couleur (distracteur : 182, le rouge peut être bien contrasté). B → 182 : contraste insuffisant (distracteur : 181). C → 180 : rupture de charte graphique sur une page de service tiers (distracteur : 183, les styles ne sont pas désactivés).

**Mémo oral :** une perte, une règle.

**Fichier final prévu :** `finals/slide-11-checkpoint-1.png`

---

### S12 — Sans les styles, la page garde son sens

- **Acte :** 2. Lire sans les styles
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** comprendre pourquoi le contenu et son ordre doivent tenir sans la couche CSS, et comment le contrôler.
- **Badge :** `R. 183`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la page lue avec les styles désactivés, ouverture de l’acte 2.
- Idée principale : sans la couche de présentation, le contenu doit rester dans un ordre logique et compréhensible.
- Scène : qui, Samuel ; où, à son bureau, deux écrans ; objet, le formulaire d’inscription avec et sans styles ; tension, sans styles, les étiquettes s’empilent en haut et les champs en bas ; action, Samuel désactive les styles ; résultat, des flèches corail croisées montrent que les étiquettes ne suivent plus leurs champs.
- Transformation visible : d’un formulaire rangé à une suite de blocs sans ordre de sens.
- Test des trois secondes : « Sans mise en forme, le formulaire ne veut plus rien dire. »
- Ajout par rapport à la slide précédente : on quitte la perception visuelle pour la page sans sa couche de présentation.

**Référence de composition principale :** `S20` (personnage devant deux fenêtres). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Acte 2 · Lire sans les styles`
- `Sans les styles, la page garde son sens`
- `IMPACT - Étiquettes et champs se séparent`
- `CONTRÔLE - Désactiver les styles, puis relire`

**Illustration :** Samuel (bloc Samuel) à gauche, main sur la souris. Écran gauche : formulaire mis en forme, trois paires étiquette et champ alignées. Écran droit, cadre corail pâle : la même page sans styles, trois barres d’étiquettes empilées en haut, trois champs empilés en bas, trois flèches corail fines qui se croisent. Un petit interrupteur basculé entre les écrans. Barres abstraites.

**Alternative textuelle à fournir :** Samuel désactive les styles du formulaire : les étiquettes se retrouvent toutes en haut et les champs en bas, sans lien visible entre eux.

**Règle → préjudice utilisateur :** quand les styles ne s’appliquent pas, ou que l’accès n’est pas visuel, un contenu ordonné par la seule CSS devient incompréhensible.

**Garantie recherchée (matière de l’oral)**

Compréhension sans les feuilles de styles du site, séparation du contenu et de la présentation, référencement, accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : comparer chaque page avec et sans styles ; vérifier l’absence de perte d’information, la lisibilité (par exemple une image transparente qui dépend d’un `background-color`) et la cohérence de l’ordre ; confirmer la cause à l’inspecteur de code.
- Piège certification : un organigramme construit par positionnement CSS peut devenir une suite de blocs sans sens. L’association code entre champ et étiquette relève aussi de la rubrique Formulaires (règle 69, oral).

**Discours oral du présentateur (non projeté)**

#### Le sens doit tenir dans le HTML

- Les styles sont une couche de présentation ; le contenu doit rester lisible et compréhensible sans elle.
- Un lecteur d’écran, un robot ou un navigateur qui n’applique pas les styles lisent la page dans l’ordre du code.
- Le livre cite le menu coupé en deux et l’organigramme réduit à des blocs sans sens.
- L’avis de l’expert vise aussi les formulaires dont champs et étiquettes ne sont placés côte à côte que par la CSS.
- Ce cas rejoint la rubrique Formulaires, qui demande d’associer chaque champ à son étiquette dans le code.

##### Impact du non-respect

- Sans la mise en forme, l’utilisateur ne sait plus quelle étiquette décrit quel champ.

##### Ce que garantit la règle

- Le même contenu, dans le même ordre, avec ou sans styles.

#### Transition

- Le sens peut aussi se perdre dans la façon de désigner un contenu.

**Mémo oral :** le sens tient dans le HTML.

**Fichier final prévu :** `finals/slide-12-styles-desactives.png`

---

### S13 — « En haut à droite », pour qui ?

- **Acte :** 2. Lire sans les styles
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une désignation par la forme ou la position et connaître les moyens complémentaires.
- **Badge :** `R. 184`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la désignation d’un contenu par sa forme ou sa position.
- Idée principale : « le bouton rond en haut à droite » ne désigne rien pour qui n’a pas accès à l’affichage, ou dont l’affichage a changé.
- Scène : qui, Malik et Nora ; où, Malik à son bureau, Nora dans la rue ; objet, la consigne de la page d’aide ; tension, la synthèse vocale lit la consigne à Malik, et sur le téléphone de Nora le bouton est passé en bas ; action, tous deux cherchent ; résultat, deux points d’interrogation corail.
- Transformation visible : une même consigne échoue dans deux contextes.
- Test des trois secondes : « Cette consigne ne mène nulle part sans la vue ou sur mobile. »
- Ajout par rapport à la slide précédente : après l’ordre du contenu, la façon de le désigner.

**Référence de composition principale :** `N10` (personnage et interface). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `« En haut à droite », pour qui ?`
- `« Le bouton rond en haut à droite »`
- `IMPACT - Sans la vue, la consigne échoue`
- `GARANTIE - Un nom ou un lien désigne le contenu`

**Illustration :** à gauche, Malik (bloc Malik) devant son ordinateur, casque sur les oreilles ; une bulle de synthèse vocale bleu clair porte `« Le bouton rond en haut à droite »` ; un point d’interrogation corail près de la bulle. À droite, Nora (Bloc personnage), téléphone en main : la même page réorganisée en une colonne, un petit bouton rond tout en bas ; second point d’interrogation corail. Pages en blocs abstraits.

**Alternative textuelle à fournir :** la consigne « le bouton rond en haut à droite » ne sert ni à Malik, qui l’entend par sa synthèse vocale, ni à Nora, dont le téléphone a déplacé le bouton.

**Règle → préjudice utilisateur :** désigner un contenu par sa forme ou sa position présuppose l’accès à l’affichage prévu ; sinon, le contenu reste introuvable.

**Garantie recherchée (matière de l’oral)**

Compréhension de l’information sans accès au support visuel, ou quand son rendu est altéré.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : pour chaque contenu qui suppose l’affichage graphique pour être retrouvé (aide renvoyant à des captures, texte renvoyant à une illustration ou un tableau), vérifier qu’un autre moyen existe : identifiant explicite (« voir la figure n° 1 »), lien vers une ancre, mention textuelle.
- Piège certification : mentionner une position n’est pas interdit ; c’est le seul moyen qui pose problème.

**Discours oral du présentateur (non projeté)**

#### Une consigne qui suppose de voir l’écran

- Désigner un contenu par sa forme ou sa position, c’est présumer que le lecteur voit l’écran tel qu’il a été conçu.
- Malik reçoit la consigne par synthèse vocale : la forme et la position du bouton ne lui sont pas restituées.
- Sur le téléphone de Nora, la page s’est réorganisée : le bouton n’est plus en haut à droite.
- Le livre demande un autre moyen, en plus : le nom du contenu, un identifiant comme « figure 1 », un lien vers une ancre.

##### Impact du non-respect

- L’utilisateur ne retrouve pas le contenu désigné, ici le bouton de l’aide.

##### Ce que garantit la règle

- Une désignation qui fonctionne sans l’affichage graphique ou quand il change.

#### Transition

- Ce qui est caché à l’écran peut aussi manquer à l’oreille.

**Mémo oral :** nommer, pas seulement situer.

**Fichier final prévu :** `finals/slide-13-forme-position.png` (devient l’ancre `A-MALIK` après validation).

---

### S14 — Caché à l’écran, pas à l’oreille

- **Acte :** 2. Lire sans les styles
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** distinguer les techniques qui masquent un contenu pour tous de celles qui le masquent seulement à l’affichage.
- **Badge :** `R. 185`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur le contenu dissimulé au lecteur d’écran.
- Idée principale : un nom de bouton masqué avec `display: none` disparaît aussi pour le lecteur d’écran.
- Scène : qui, Malik ; où, à son bureau ; objet, le bouton loupe de la recherche, dont le nom « Rechercher » est masqué à l’écran ; tension, avec `display: none`, la synthèse vocale n’annonce pas ce nom ; action, Malik atteint le bouton au clavier ; résultat, à droite, avec un masquage seulement visuel, la synthèse annonce « Rechercher, bouton ».
- Transformation visible : la même loupe, muette à gauche, nommée à droite.
- Test des trois secondes : « Mal caché, le nom du bouton disparaît aussi pour Malik. »
- Ajout par rapport à la slide précédente : après la désignation, ce qui est caché.

**Référence de composition principale :** `N10` (personnage et interface). Ancre de personnage : `A-MALIK` si disponible.

**Texte visible (projection)**

- `Caché à l’écran, pas à l’oreille`
- `display: none;`
- `« Rechercher, bouton »`
- `IMPACT - J’ignore à quoi sert ce bouton`
- `GARANTIE - Caché à l’écran, le nom reste annoncé`

**Illustration :** Malik (bloc Malik) à gauche, casque sur les oreilles, mains sur le clavier. Fenêtre gauche, cadre corail pâle : un bouton loupe, une étiquette fantôme en pointillés barrée d’un trait corail, la ligne de code `display: none;` barrée sobrement, une bulle de synthèse vocale vide. Fenêtre droite, cadre vert pâle : le même bouton loupe, l’étiquette fantôme reliée à une bulle `« Rechercher, bouton »`, coche verte.

**Alternative textuelle à fournir :** masqué par display: none, le nom du bouton de recherche n’est plus annoncé à Malik ; masqué seulement à l’écran, il est annoncé « Rechercher, bouton ».

**Règle → préjudice utilisateur :** l’information prévue pour les utilisateurs de lecteur d’écran ne leur parvient pas.

**Garantie recherchée (matière de l’oral)**

Adaptation du rendu aux besoins et accessibilité : ce qui doit être restitué l’est.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : à l’inspecteur de code, repérer les contenus masqués à l’affichage, hors ceux révélés par une action (onglets, menus déroulants) ; vérifier que ceux destinés au lecteur d’écran n’utilisent ni `display`, ni `visibility`, ni l’attribut `hidden`, ni `aria-hidden="true"`.
- Piège certification : un contenu affiché sur action peut être masqué avec ces techniques. Techniques adaptées selon le livre : positionnement hors écran (`position`, `text-indent`), rognage (`clip`), `aria-label`, `aria-labelledby`, `aria-describedby`, ou `title` pour une étiquette de champ.

**Discours oral du présentateur (non projeté)**

#### Deux façons de cacher

- Le bouton de recherche n’affiche qu’une loupe ; son nom, « Rechercher », est prévu pour la synthèse vocale.
- Masqué avec `display: none`, ce nom disparaît pour tout le monde, lecteur d’écran compris.
- Les propriétés qui retirent un contenu, `display`, `visibility`, l’attribut `hidden` ou `aria-hidden`, sont admises pour ce qui s’affichera sur action : un onglet, un menu déroulant.
- Pour ce qui doit rester restitué, le livre cite le positionnement hors écran, le rognage ou les attributs ARIA de libellé.
- L’avis de l’expert ajoute qu’une page peut généralement se passer de contenus réservés aux lecteurs d’écran : l’information pertinente est le plus souvent la même pour tous.

##### Impact du non-respect

- Le nom du bouton n’est pas annoncé ; Malik ne sait pas à quoi il sert.

##### Ce que garantit la règle

- Un contenu destiné au lecteur d’écran lui reste restitué, même masqué à l’affichage.

#### Transition

- Après ce que l’on cache, ce que les styles ajoutent.

**Mémo oral :** caché à l’œil, pas à l’oreille.

**Fichier final prévu :** `finals/slide-14-lecteur-ecran.png`

---

### S15 — Ce que la CSS écrit, le HTML le dit

- **Acte :** 2. Lire sans les styles
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une information produite par la CSS et l’alternative attendue.
- **Badge :** `R. 188`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur les contenus générés via les styles.
- Idée principale : une information ajoutée par la feuille de styles disparaît quand les styles ne sont pas restitués.
- Scène : qui, Samuel ; où, à son bureau ; objet, la carte de l’atelier Reliure marquée « Complet » par la CSS ; tension, sans styles, la mention a disparu ; action, Samuel compare les deux affichages ; résultat, la carte semble encore ouverte à l’inscription.
- Transformation visible : la carte « Complet » devient une carte sans mention.
- Test des trois secondes : « Sans les styles, “Complet” a disparu. »
- Ajout par rapport à la slide précédente : après le contenu caché, le contenu fabriqué par les styles.

**Référence de composition principale :** `S20` (deux fenêtres comparées, code court). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Ce que la CSS écrit, le HTML le dit`
- `Complet`
- `content: "Complet";`
- `IMPACT - Sans styles, l’atelier paraît ouvert`
- `GARANTIE - Une alternative existe dans le HTML`

**Illustration :** Samuel (bloc Samuel) à gauche, de trois quarts. Écran gauche : une carte d’atelier pastel avec un petit ruban bleu marine portant `Complet` en blanc, relié par un trait fin à la ligne de code `content: "Complet";` sur une bande bleu clair. Écran droit, cadre corail pâle : la même carte sans ruban, petite croix corail. Barres abstraites pour le reste de la carte. Le ruban écrit et la ligne de code sont deux chaînes distinctes de la liste ; le mot ne figure nulle part ailleurs.

**Alternative textuelle à fournir :** avec les styles, la carte de l’atelier porte un ruban « Complet » produit par la propriété content ; sans les styles, le ruban disparaît.

**Règle → préjudice utilisateur :** dans un navigateur texte ou avec les styles désactivés, l’utilisateur perd une information que seule la CSS produisait.

**Garantie recherchée (matière de l’oral)**

Accès à l’information générée en CSS quand les styles ne sont pas restitués, et exploitation par les robots.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : examiner les feuilles de styles (`background-image`, `content`, `:before`, `:after`) ; désactiver les images d’arrière-plan ; comparer avec et sans elles.
- Piège certification : une image décorative en arrière-plan n’est pas visée ; seule une information absente par ailleurs du HTML l’est. Solution du livre : un contenu masqué à l’affichage via CSS, donc présent dans le HTML.
- Revue : le ruban de l’écran gauche porte `Complet`, chaîne distincte de la ligne de code ; l’écran droit n’a ni ruban ni mot.

**Discours oral du présentateur (non projeté)**

#### Une information fabriquée par la feuille de styles

- Le ruban « Complet » est écrit par la propriété `content` de la CSS.
- Le livre vise de la même façon les images d’arrière-plan et les pseudo-éléments `:before` et `:after`.
- Sans les styles, cette information disparaît, alors qu’une image ou un texte HTML seraient restés.
- L’avis de l’expert reconnaît l’intérêt de l’astuce pour personnaliser des boutons, mais elle ne permet pas une intégration robuste et accessible.

##### Impact du non-respect

- L’atelier semble ouvert à qui consulte la page sans styles ; robots et outils d’indexation ignorent l’information.

##### Ce que garantit la règle

- Toute information produite par la CSS existe aussi, sous forme d’alternative, dans le HTML.

#### Transition

- Une police peut, elle aussi, fabriquer un faux contenu.

**Mémo oral :** ce que la CSS écrit, le HTML le dit aussi.

**Fichier final prévu :** `finals/slide-15-contenu-genere.png`

---

### S16 — Une icône de police n’a pas de nom

- **Acte :** 2. Lire sans les styles
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** comprendre pourquoi un pictogramme typographique doit être doté d’une alternative.
- **Badge :** `R. 189`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur les pictogrammes typographiques.
- Idée principale : une icône produite par une police repose sur un caractère arbitraire ; restitué, ce caractère n’a pas de sens.
- Scène : qui, Malik ; où, à son bureau ; objet, le lien calendrier de la barre d’outils, icône produite par une police ; tension, la synthèse vocale annonce seulement « Lien » ; action, Malik atteint le lien au clavier ; résultat, à droite, avec un libellé masqué dans le lien, elle annonce « Agenda, lien ».
- Transformation visible : une icône muette, puis nommée.
- Test des trois secondes : « Sans libellé, l’icône n’est qu’un “lien” anonyme. »
- Ajout par rapport à la slide précédente : après la CSS, la police d’icônes.

**Référence de composition principale :** `N10` (personnage et interface). Ancre de personnage : `A-MALIK` si disponible.

**Texte visible (projection)**

- `Une icône de police n’a pas de nom`
- `« Lien »`
- `« Agenda, lien »`
- `IMPACT - Le lien n’annonce pas sa fonction`
- `GARANTIE - Un libellé masqué nomme l’icône`

**Illustration :** Malik (bloc Malik) à gauche, casque sur les oreilles. Au centre, une icône de calendrier au trait, agrandie, et à côté une petite case de caractère en pointillés, illisible, qui suggère le caractère de police détourné. Deux bulles de synthèse vocale : gauche, cadre corail pâle, `« Lien »` avec un point d’interrogation corail ; droite, cadre vert pâle, `« Agenda, lien »` avec une coche verte. Aucune loupe.

**Alternative textuelle à fournir :** l’icône calendrier produite par une police n’est annoncée que « Lien » à Malik ; avec un libellé masqué, elle devient « Agenda, lien ».

**Règle → préjudice utilisateur :** l’utilisateur de lecteur d’écran ignore la fonction de l’icône ; le référencement ne la comprend pas non plus.

**Garantie recherchée (matière de l’oral)**

Accessibilité et prise en compte par les moteurs de recherche des informations portées par une police d’icônes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : examiner le code pour vérifier que chaque icône affichée via une police est dotée d’une alternative dans le contenu HTML.
- Piège certification : solution du livre, un contenu masqué à l’affichage via CSS ; l’avis de l’expert cite un libellé explicite masqué dans le contenu du lien. Le lien sans intitulé relève aussi de la rubrique Liens (S33).

**Discours oral du présentateur (non projeté)**

#### Un caractère détourné en icône

- Les polices téléchargeables permettent de remplacer des images d’icônes par un caractère graphique, une astuce appréciée pour les performances.
- Ce caractère est arbitraire : restitué par une synthèse vocale, il n’a aucun sens.
- Le livre demande une alternative pour chaque information portée par une police spécifique, par exemple un libellé explicite masqué dans le contenu du lien.

##### Impact du non-respect

- Malik entend « lien » sans savoir où il mène ; les moteurs de recherche ne comprennent pas davantage.

##### Ce que garantit la règle

- Chaque icône de police est nommée dans le HTML.

#### Transition

- Couleur, forme, position : trois repères visuels à ne jamais laisser seuls.

**Mémo oral :** une icône de police se nomme dans le HTML.

**Fichier final prévu :** `finals/slide-16-pictogramme-typographique.png`

---

### S17 — Couleur, forme, position : jamais seules

- **Acte :** 2. Lire sans les styles
- **Type :** distinction
- **Durée indicative :** 0:50
- **Objectif pédagogique :** distinguer les deux règles qui interdisent de désigner un contenu par un seul repère visuel.
- **Badge :** `R. 181 · 184`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : distinction entre la couleur seule et la forme ou la position seules.
- Idée principale : même logique, deux règles.
- Scène : qui, Nora ; où, devant un panneau d’affichage du hall ; objet, trois consignes du site ; tension, trois consignes qui supposent de voir l’écran ; action, Nora les barre une à une, feutre en main ; résultat, un bandeau vert rappelle de nommer le contenu.
- Transformation visible : trois repères visuels barrés.
- Test des trois secondes : « Couleur, forme, position ne suffisent pas, il faut nommer. »
- Ajout par rapport à la slide précédente : synthèse entre l’acte 1 et l’acte 2.

**Référence de composition principale :** `N03` (panneaux et bandeau final). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Couleur, forme, position : jamais seules`
- `« les ateliers en vert »`
- `« le bouton rond »`
- `« la colonne de droite »`
- `Nommer le contenu, en plus de le montrer`

**Illustration :** Nora (Bloc personnage) debout à gauche, feutre en main. Trois panneaux pastel côte à côte, titrés chacun d’une consigne : `« les ateliers en vert »` avec une petite pastille verte, `« le bouton rond »` avec un cercle, `« la colonne de droite »` avec une flèche vers la droite ; chaque consigne barrée d’un trait corail fin. Bandeau vert pâle à icône de coche : `Nommer le contenu, en plus de le montrer`.

**Alternative textuelle à fournir :** trois consignes à éviter, « les ateliers en vert », « le bouton rond », « la colonne de droite », barrées ; il faut nommer le contenu en plus de le montrer.

**Règle → préjudice utilisateur :** quel que soit le repère visuel, l’utilisateur qui ne le perçoit pas ne trouve pas le contenu désigné.

**Garantie recherchée (matière de l’oral)**

Une désignation par le nom, un identifiant ou un lien fonctionne dans tous les contextes.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : couleur, comparaison sans couleurs ; forme ou position, relecture des consignes et des renvois.
- Piège certification : « les ateliers en vert » relève de la couleur seule ; « le bouton rond » et « la colonne de droite » relèvent de la forme et de la position.

**Discours oral du présentateur (non projeté)**

#### Même logique, deux règles

- « Les ateliers en vert » : la couleur seule désigne, c’est la règle sur la couleur.
- « Le bouton rond » et « la colonne de droite » : la forme et la position désignent, c’est la règle voisine.
- Dans les deux cas, un repère visuel ne doit pas être le seul moyen.
- Le remède est commun : nommer le contenu, ajouter un identifiant ou un lien.
- Pour choisir la règle, il suffit de repérer quel repère visuel est en jeu.

#### Transition

- Sans styles, chaque mécanisme laisse une trace différente.

**Mémo oral :** couleur, une règle ; forme ou position, une autre ; le nom, toujours.

**Fichier final prévu :** `finals/slide-17-distinction-couleur-forme-position.png`

---

### S18 — Checkpoint 2 : sans styles

- **Acte :** 2. Lire sans les styles
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** réactiver quatre règles de l’acte 2.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : checkpoint de l’acte 2.
- Idée principale : rattacher chaque constat à sa règle.
- Scène : qui, Samuel ; où, à son bureau ; objet, quatre cartes de constats épinglées au-dessus de ses écrans ; tension, quatre défauts proches ; action, Samuel les relit ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Un exercice en quatre cas. »
- Ajout par rapport à la slide précédente : l’apprenant applique.

**Référence de composition principale :** `N17` (cartes pastel). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Checkpoint 2 : sans styles`
- `Quelle règle est en jeu ?`
- `A. Sans CSS, menu coupé`
- `B. Nom de bouton en display: none`
- `C. « Complet » par la CSS`
- `D. Icône de police sans nom`

**Illustration :** question dans un bandeau bleu clair sous le titre. Quatre cartes pastel A à D portant chacune sa ligne et une mini-scène sans autre texte : A, une barre de menu brisée en deux morceaux décalés ; B, un bouton loupe et une étiquette fantôme en pointillés ; C, une carte d’atelier avec un ruban bleu marine vide ; D, une icône de calendrier à côté d’une case de caractère en pointillés. Samuel (bloc Samuel) à gauche. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** exercice : quatre constats faits sans les styles ou au code, à rattacher chacun à une règle.

**Règle → préjudice utilisateur :** confondre ces règles mène à corriger le mauvais mécanisme.

**Garantie recherchée (matière de l’oral)**

Rattacher le constat à sa règle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : une minute de réflexion avant le corrigé.
- Piège certification : B et C concernent tous deux le lecteur d’écran, mais l’un cache un contenu existant, l’autre fabrique un contenu en CSS. En B, le nom d’un bouton icône ne s’affiche jamais sur action : l’exception du livre ne s’applique pas.

**Discours oral du présentateur (non projeté)**

#### Quatre mécanismes

- Un contenu peut être mal ordonné, mal caché, fabriqué par la CSS ou porté par une police d’icônes.
- Le mécanisme en cause désigne la règle.

#### Transition

- Lire la page ne suffit pas : il faut aussi pouvoir agir sur elle.

**Corrigé (notes du présentateur, non projeté) :** A → 183 : l’ordre et le sens changent sans styles (distracteur : 180). B → 185 : `display: none` dissimule au lecteur d’écran le nom qui lui est destiné (distracteur : 188). C → 188 : information générée par la CSS sans alternative (distracteur : 185, rien n’est masqué). D → 189 : pictogramme typographique sans alternative (distracteur : 187, ce n’est pas une image de texte).

**Mémo oral :** ordonner, bien cacher, doubler en HTML, nommer l’icône.

**Fichier final prévu :** `finals/slide-18-checkpoint-2.png`

---

### S19 — Un bouton à la taille du doigt

- **Acte :** 3. Agir et adapter
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une cible cliquable trop petite et connaître les dimensions retenues par le livre.
- **Badge :** `R. 186`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la taille des éléments cliquables, ouverture de l’acte 3.
- Idée principale : une cible trop petite fait toucher le mauvais élément.
- Scène : qui, Nora ; où, debout dans un tram, une main sur la barre ; objet, son téléphone, deux boutons minuscules à icônes, une coche et une croix ; tension, son pouce couvre les deux ; action, elle touche ; résultat, c’est la croix qui s’active ; à droite, les deux boutons ont une taille suffisante, le pouce touche la coche.
- Transformation visible : du pouce qui couvre deux cibles au pouce qui en touche une.
- Test des trois secondes : « Bouton trop petit, mauvais clic. »
- Ajout par rapport à la slide précédente : on passe de la lecture à l’action.

**Référence de composition principale :** `N10` (personnage et interface agrandie). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Acte 3 · Agir et adapter`
- `Un bouton à la taille du doigt`
- `44 × 44 px au moins`
- `IMPACT - Je touche le bouton voisin`
- `GARANTIE - La cible est assez grande pour le doigt`

**Illustration :** Nora (Bloc personnage) debout à gauche dans un tram stylisé, téléphone dans la main droite. Deux médaillons de l’écran. Gauche, cadre corail pâle : deux boutons minuscules à icônes (coche et croix), le pouce de Nora les recouvre ; la croix s’allume. Droite, cadre vert pâle : les deux mêmes boutons à taille suffisante, le pouce sur la coche, coche verte ; une cote fine autour d’un bouton avec le cartouche `44 × 44 px au moins`. Aucun libellé de bouton.

**Alternative textuelle à fournir :** dans le tram, le pouce de Nora couvre deux boutons minuscules et active le mauvais ; avec des boutons d’au moins 44 pixels de côté, elle touche le bon.

**Règle → préjudice utilisateur :** des cibles trop petites provoquent fausses manipulations et manipulations inutiles.

**Garantie recherchée (matière de l’oral)**

Pouvoir cliquer sur les éléments interactifs, limiter les fausses manipulations, mieux servir les mobiles et l’accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : vérifier que la taille par défaut de chaque élément cliquable (boutons, liens) est d’au moins 44 × 44 pixels, et 48 × 48 pixels pour Android.
- Piège certification : l’avis de l’expert rattache cette valeur aux recommandations WCAG du W3C ; c’est la taille par défaut qui compte. L’espacement entre cibles n’est pas un critère de la règle.

**Discours oral du présentateur (non projeté)**

#### Pouvoir toucher sans viser

- Les écrans tactiles ont imposé une contrainte simple : pouvoir cliquer sans difficulté avec les doigts.
- La règle s’appuie sur une valeur chiffrée des recommandations d’accessibilité : au moins 44 pixels sur 44 par défaut, 48 sur 48 pour Android.
- Elle vise chaque élément cliquable, boutons comme liens.

##### Impact du non-respect

- Le doigt active l’élément voisin : action annulée, manipulation à refaire.

##### Ce que garantit la règle

- Une cible de taille suffisante par défaut, qui limite les erreurs de manipulation.

#### Transition

- Toucher, c’est aussi pouvoir agrandir.

**Mémo oral :** une cible, un doigt.

**Fichier final prévu :** `finals/slide-19-taille-cliquable.png`

---

### S20 — Ne pas bloquer le zoom

- **Acte :** 3. Agir et adapter
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître un blocage du zoom et connaître les attributs en cause.
- **Badge :** `R. 193`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur le blocage du zoom.
- Idée principale : interdire le zoom tactile enferme l’utilisateur dans un rendu qu’il ne peut pas lire.
- Scène : qui, Nora ; où, sur un quai de gare stylisé ; objet, le plan d’accès sur son téléphone, aux légendes minuscules ; tension, elle écarte deux doigts, la page reste figée ; action, elle insiste ; résultat, à droite, la même page s’agrandit sous ses doigts.
- Transformation visible : deux doigts sans effet, puis la page agrandie.
- Test des trois secondes : « Elle ne peut pas zoomer, puis elle peut. »
- Ajout par rapport à la slide précédente : après toucher, agrandir.

**Référence de composition principale :** `N10` (personnage et écran). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Ne pas bloquer le zoom`
- `user-scalable=no`
- `IMPACT - Le texte reste trop petit pour moi`
- `CONTRÔLE - Zoomer avec les doigts sur un écran tactile`

**Illustration :** Nora (Bloc personnage) à gauche, sur un quai stylisé. Médaillon gauche, cadre corail pâle : un petit plan aux légendes en barres minuscules, deux doigts écartés dessus, carte immobile ; sous le médaillon, `user-scalable=no` barré sobrement. Médaillon droit, cadre vert pâle : le même plan agrandi, coche verte. Légendes en barres abstraites.

**Alternative textuelle à fournir :** sur son téléphone, Nora ne peut pas agrandir le plan d’accès, le zoom étant bloqué par user-scalable=no ; sans blocage, le plan s’agrandit.

**Règle → préjudice utilisateur :** face à un texte trop petit sur smartphone ou tablette, l’utilisateur ne peut pas l’agrandir.

**Garantie recherchée (matière de l’oral)**

Adapter le rendu à ses besoins par le zoom graphique ; compatibilité mobile et accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : sur un périphérique tactile, vérifier qu’il est possible d’agrandir la vue avec la commande de zoom tactile du navigateur.
- Piège certification : le livre nomme `minimum-scale`, `maximum-scale` et `user-scalable` dans l’élément `meta viewport` ; une page adaptée au mobile ne dispense pas du zoom (S22).

**Discours oral du présentateur (non projeté)**

#### Un réglage qui appartient à l’utilisateur

- Le livre le dit simplement : il est toujours décevant de ne pas pouvoir agrandir un texte trop petit sur sa tablette ou son smartphone.
- La règle demande de ne pas utiliser de mécanisme qui bloque le zoom, en particulier les attributs `minimum-scale`, `maximum-scale` et `user-scalable` de la balise `meta viewport`.
- L’avis de l’expert écarte une illusion : une mise en forme adaptée aux mobiles ne garantit pas la lisibilité pour tous.

##### Impact du non-respect

- Le texte reste trop petit, et l’utilisateur n’a aucun moyen de l’agrandir.

##### Ce que garantit la règle

- La possibilité d’agrandir la vue par le zoom tactile, quel que soit le rendu prévu.

#### Transition

- Agrandir est un geste de l’utilisateur ; s’adapter est une tâche du site.

**Mémo oral :** l’utilisateur garde la main sur la taille.

**Fichier final prévu :** `finals/slide-20-zoom.png`

---

### S21 — Une page pensée pour chaque écran

- **Acte :** 3. Agir et adapter
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître l’absence de mécanisme d’adaptation mobile et connaître les solutions citées par le livre.
- **Badge :** `R. 194`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur l’adaptation aux terminaux mobiles.
- Idée principale : sans mécanisme dédié, la page bureau s’affiche en miniature sur un téléphone.
- Scène : qui, Nora ; où, dans le hall de la Maison des Lisières ; objet, son téléphone ; tension, trois colonnes minuscules débordent, il faut faire défiler de côté ; action, Nora fait glisser la page ; résultat, à droite, la page se réorganise en une colonne lisible.
- Transformation visible : de trois colonnes réduites à une colonne lisible.
- Test des trois secondes : « La même page, réduite puis adaptée au téléphone. »
- Ajout par rapport à la slide précédente : après agrandir, adapter.

**Référence de composition principale :** `N10` (personnage et écran). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Une page pensée pour chaque écran`
- `@media (max-width: 600px)`
- `IMPACT - Sur mobile, la page bureau devient illisible`
- `GARANTIE - Le rendu s’adapte à l’écran`

**Illustration :** Nora (Bloc personnage) à gauche, téléphone en main. Médaillon gauche, cadre corail pâle : trois colonnes en miniature, débordant à droite, petite flèche de défilement horizontal. Médaillon droit, cadre vert pâle : une seule colonne aux blocs lisibles, coche verte. Entre les deux, sur une bande de code bleu clair, `@media (max-width: 600px)`. Blocs abstraits.

**Alternative textuelle à fournir :** sans adaptation, la page en trois colonnes s’affiche en miniature sur le téléphone de Nora ; avec une media query, elle passe en une colonne lisible.

**Règle → préjudice utilisateur :** une page non adaptée oblige à zoomer et à faire défiler dans tous les sens.

**Garantie recherchée (matière de l’oral)**

Consultation facilitée sur mobile ; contribution au positionnement dans les outils d’indexation qui en tiennent compte.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : comparer l’affichage sur plusieurs tailles d’écran (ordinateur, tablette, smartphone) et vérifier que le rendu s’adapte.
- Piège certification : plusieurs mécanismes sont admis, media queries, design adaptatif ou version mobile dédiée ; l’avis de l’expert juge la détection du navigateur (browser-sniffing) la plus risquée.

**Discours oral du présentateur (non projeté)**

#### Un contenu, plusieurs écrans

- Chaque service en ligne devrait être consultable dans de bonnes conditions, quel que soit le terminal.
- Le livre cite deux familles de solutions : des styles adaptés à la taille de l’écran, par les media queries ou le design adaptatif, ou une version mobile dédiée.
- L’avis de l’expert pense prioritairement au responsive design, prévoit que les moyens évolueront, et juge la détection du navigateur la plus risquée.

##### Impact du non-respect

- Sur un téléphone, la page bureau se lit mal et oblige à défiler de côté.

##### Ce que garantit la règle

- Au moins un mécanisme qui adapte la page aux terminaux mobiles.

#### Transition

- Zoom et adaptation se complètent ; aucun ne remplace l’autre.

**Mémo oral :** un contenu, des écrans.

**Fichier final prévu :** `finals/slide-21-adaptation-mobile.png`

---

### S22 — Zoom libre et page adaptée : il faut les deux

- **Acte :** 3. Agir et adapter
- **Type :** distinction
- **Durée indicative :** 0:50
- **Objectif pédagogique :** distinguer le zoom laissé à l’utilisateur et l’adaptation fournie par le site.
- **Badge :** `R. 193 · 194`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : distinction entre zoom et adaptation mobile.
- Idée principale : le site s’adapte ; l’utilisateur garde le zoom.
- Scène : qui, Nora ; où, à une table de café ; objet, deux téléphones ; tension, l’un adapte sa page, l’autre se laisse agrandir ; action, Nora écarte les doigts sur le second ; résultat, deux panneaux nommant chacun le rôle.
- Transformation visible : deux mécanismes, deux acteurs.
- Test des trois secondes : « Adapter ne suffit pas, il faut aussi laisser zoomer. »
- Ajout par rapport à la slide précédente : la relation entre les deux règles.

**Référence de composition principale :** `N03` (deux panneaux et bandeau final). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Zoom libre et page adaptée : il faut les deux`
- `Adapter : le site s’ajuste`
- `Zoomer : l’utilisateur agrandit`
- `Une page adaptée ne dispense pas du zoom`

**Illustration :** Nora (Bloc personnage) assise à une petite table de café. Panneau lavande, titré `Adapter : le site s’ajuste` : un téléphone en une colonne, petite icône d’engrenage. Panneau bleu clair, titré `Zoomer : l’utilisateur agrandit` : un téléphone dont la page s’agrandit sous deux doigts, petite loupe. Bandeau vert pâle à icône de coche : `Une page adaptée ne dispense pas du zoom`.

**Alternative textuelle à fournir :** deux mécanismes complémentaires : le site adapte sa page à l’écran, l’utilisateur garde le zoom ; une page adaptée ne dispense pas du zoom.

**Règle → préjudice utilisateur :** se reposer sur l’adaptation pour bloquer le zoom prive l’utilisateur d’un réglage nécessaire.

**Garantie recherchée (matière de l’oral)**

Le site s’adapte, l’utilisateur garde la main.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : adaptation, plusieurs tailles d’écran ; zoom, écarter les doigts sur un écran tactile.
- Piège certification : une page responsive qui bloque le zoom respecte la règle sur l’adaptation et enfreint celle sur le zoom.

**Discours oral du présentateur (non projeté)**

#### Deux acteurs différents

- L’adaptation, c’est le site qui s’ajuste à l’écran.
- Le zoom, c’est l’utilisateur qui agrandit selon ses besoins.
- Une page responsive qui bloque le zoom respecte la première règle et enfreint la seconde.
- L’avis de l’expert sur le zoom : mieux vaut admettre que l’affichage ne sera pas exactement celui prévu.

#### Transition

- Sur un téléphone, toucher, agrandir et s’adapter échouent chacun à sa façon.

**Mémo oral :** le site s’adapte, l’utilisateur agrandit.

**Fichier final prévu :** `finals/slide-22-distinction-zoom-mobile.png`

---

### S23 — Checkpoint 3 : sur le téléphone

- **Acte :** 3. Agir et adapter
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** réactiver les trois règles de l’acte 3.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : checkpoint de l’acte 3.
- Idée principale : rattacher chaque obstacle à sa règle.
- Scène : qui, Nora ; où, debout dans un tram ; objet, trois cartes de situation ; tension, trois obstacles ; action, Nora les regarde tour à tour ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Un exercice en trois cas, sur téléphone. »
- Ajout par rapport à la slide précédente : l’apprenant applique.

**Référence de composition principale :** `N17` (cartes pastel). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Checkpoint 3 : sur le téléphone`
- `Quelle règle est en jeu ?`
- `A. Boutons de 30 px de côté`
- `B. Écarter les doigts : la page reste figée`
- `C. La page bureau, en miniature`

**Illustration :** question dans un bandeau bleu clair sous le titre. Trois cartes pastel portant chacune sa ligne et une mini-scène sans autre texte : A, deux petits boutons à icônes sous un pouce ; B, deux doigts écartés sur une page immobile ; C, un téléphone affichant trois colonnes réduites. Nora (Bloc personnage) à gauche, téléphone en main. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** exercice : trois obstacles sur téléphone à rattacher chacun à une règle.

**Règle → préjudice utilisateur :** sans le bon rattachement, on corrige l’adaptation alors que le zoom est bloqué, ou l’inverse.

**Garantie recherchée (matière de l’oral)**

Rattacher l’obstacle à sa règle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : 45 secondes de réflexion.
- Piège certification : B et C se ressemblent (« on ne lit rien sur mobile ») mais relèvent de deux règles.

**Discours oral du présentateur (non projeté)**

#### Toucher, agrandir, s’adapter

- Chacun de ces gestes a sa règle.
- Le bon rattachement dépend de ce qui empêche l’utilisateur : la taille de la cible, le blocage du zoom ou l’absence d’adaptation.

#### Transition

- Le texte lui-même a une forme : image, police, alignement, casse.

**Corrigé (notes du présentateur, non projeté) :** A → 186 : cibles inférieures à 44 × 44 pixels (distracteur : 194). B → 193 : zoom bloqué (distracteur : 194, l’adaptation peut exister). C → 194 : aucun mécanisme d’adaptation mobile (distracteur : 193, le zoom peut fonctionner).

**Mémo oral :** toucher, agrandir, adapter.

**Fichier final prévu :** `finals/slide-23-checkpoint-3.png`

---

### S24 — Un programme en texte, pas en image

- **Acte :** 4. Typographie
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître un texte remplacé par une image alors que les styles pouvaient le mettre en forme, et connaître les exclusions.
- **Badge :** `R. 187`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur les textes remplacés par des images, ouverture de l’acte 4.
- Idée principale : publié en image, le tableau des dates ne s’agrandit pas proprement et ne s’adapte pas.
- Scène : qui, Nora ; où, dans le canapé de son salon ; objet, le tableau des dates du trimestre publié en image sur son téléphone ; tension, agrandie, l’image devient pixellisée ; action, Nora zoome ; résultat, à droite, le même tableau en texte stylé reste net à l’agrandissement.
- Transformation visible : des lettres en escaliers de pixels, puis des lignes nettes.
- Test des trois secondes : « En image, le texte devient flou ; en texte, il reste net. »
- Ajout par rapport à la slide précédente : on entre dans la typographie.

**Référence de composition principale :** `N10` (personnage et écran). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Acte 4 · Typographie`
- `Un programme en texte, pas en image`
- `IMPACT - Agrandi, le texte en image devient flou`
- `LIMITE - Logos et bannières publicitaires exclus`

**Illustration :** Nora (Bloc personnage) assise dans un canapé, téléphone en main. Médaillon gauche, cadre corail pâle : le tableau des dates du trimestre publié en image, agrandi, aux formes de lettres abstraites nettement pixellisées en escaliers de carrés. Médaillon droit, cadre vert pâle : le même tableau en blocs de texte nets à l’agrandissement, coche verte. Aucune lettre lisible. En bas, un encadré IMPACT corail et un encadré LIMITE orange.

**Alternative textuelle à fournir :** publié en image, le tableau des dates du trimestre devient pixellisé quand Nora l’agrandit ; en texte stylé, il reste net. Logos et bannières publicitaires sont exclus de la règle.

**Règle → préjudice utilisateur :** un texte en image ne s’adapte pas : agrandissement pixellisé, police, couleur et justification impossibles à modifier, mauvaise prise en compte par les aides techniques et les moteurs de recherche.

**Garantie recherchée (matière de l’oral)**

Adaptation du rendu au média et aux besoins, accessibilité, prise en compte par les moteurs de recherche.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : passer en revue les images, HTML et d’arrière-plan CSS simulant un contenu éditorial, et vérifier que les textes mis en image correspondent à des mises en forme impossibles en CSS.
- Piège certification : logos, bannières publicitaires et éléments graphiques de promotion sont exclus ; l’avis de l’expert demande de prendre la règle avec un certain recul. Le tableau des dates est un contenu éditorial, pas un élément de promotion.

**Discours oral du présentateur (non projeté)**

#### Un beau texte est possible sans image

- Une belle police est aujourd’hui possible sur le web : textes HTML, styles CSS, polices téléchargeables.
- La règle demande de ne pas remplacer par une image un texte que les styles pouvaient mettre en forme.
- Sont exclus les logos, les bannières publicitaires et les éléments graphiques de promotion.
- L’avis de l’expert demande du recul : remplacer quand c’est possible, pas à tout prix.

##### Impact du non-respect

- Agrandi, le texte devient flou ; l’utilisateur ne peut ni l’adapter ni le faire lire correctement par ses outils.

##### Ce que garantit la règle

- Un texte éditorial qui reste du texte, adaptable par l’utilisateur, hors exceptions de logos et de promotion.

#### Transition

- Quand le texte est du texte, encore faut-il qu’il s’affiche dans une police prévue.

**Mémo oral :** un texte se met en forme, pas en image.

**Fichier final prévu :** `finals/slide-24-texte-en-image.png`

---

### S25 — Une police de secours en fin de liste

- **Acte :** 4. Typographie
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une déclaration de police sans famille générique et savoir où la placer.
- **Badge :** `R. 190`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la famille générique de police.
- Idée principale : si la police prévue manque, la famille générique en fin de liste évite un rendu imprévu.
- Scène : qui, Nora ; où, devant un ordinateur de la bibliothèque, un peu ancien ; objet, la page Programme ; tension, la police prévue manque et le texte s’affiche dans la police par défaut, à empattements, inattendue ; action, Nora regarde l’écran, surprise ; résultat, à droite, avec la famille générique, le texte reste sans empattements, cohérent.
- Transformation visible : du rendu à empattements inattendu au rendu sans empattements.
- Test des trois secondes : « Police absente : avec un secours en fin de liste, le rendu reste proche du prévu. »
- Ajout par rapport à la slide précédente : après le texte en image, la police du texte.

**Référence de composition principale :** `S20` (fenêtres et code court). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Une police de secours en fin de liste`
- `Reliure`
- `Photo`
- `font-family: Optima, sans-serif;`
- `IMPACT - Police absente, rendu imprévu`
- `CONTRÔLE - Famille générique en dernier`

**Illustration :** Nora (Bloc personnage) à gauche devant un ordinateur de bibliothèque. Fenêtre gauche, cadre corail pâle : le mot `Reliure` en grande police à empattements bien visibles, au-dessus de lignes abstraites, petite icône de police barrée. Fenêtre droite, cadre vert pâle : le mot `Photo` en police sans empattements aérée, au-dessus de lignes abstraites, coche verte. Sous les fenêtres, sur une bande de code bleu clair, `font-family: Optima, sans-serif;`, avec la famille générique finale soulignée en vert.

**Alternative textuelle à fournir :** la police prévue manque sur l’ordinateur de la bibliothèque et le texte s’affiche en police à empattements par défaut ; avec la famille générique sans-serif en fin de liste, le rendu reste sans empattements.

**Règle → préjudice utilisateur :** quand les polices prévues manquent, le navigateur applique sa police par défaut et le contenu peut s’afficher mal.

**Garantie recherchée (matière de l’oral)**

Un affichage correct même sans les polices prévues.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : dans toutes les feuilles de styles, pour tous les médias (`screen`, `print`…), vérifier que chaque `font` ou `font-family` contient une famille générique (`serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`), placée en fin de liste et pertinente ; le validateur CSS du W3C signale aussi son absence.
- Revue : rejeter la candidate si `Reliure` n’a pas d’empattements visibles, ou si `Photo` en a.
- Piège certification : la famille doit correspondre au type de police ; `monospace` est surtout réservé aux exemples de code. Exemple du livre : `font-family: Optima, “Trebuchet MS”, sans-serif`.

**Discours oral du présentateur (non projeté)**

#### Prévoir le cas où la police manque

- Sur le poste de conception, tout va bien ; mais que se passe-t-il pour l’utilisateur qui n’a pas la police installée ?
- La règle demande d’indiquer en dernier élément de chaque liste de polices une famille générique : `serif`, `sans-serif`, `monospace`, `cursive` ou `fantasy`.
- Pour une police sans empattements, comme Optima dans l’exemple du livre, on termine par `sans-serif`.
- En pratique, `serif` et `sans-serif` couvrent l’essentiel ; `monospace` sert surtout au code.

##### Impact du non-respect

- Le navigateur choisit seul une police de remplacement, et l’affichage peut se dégrader.

##### Ce que garantit la règle

- Un rendu de la bonne famille de police, même sans la police prévue.

#### Transition

- La police posée, reste l’alignement du texte.

**Mémo oral :** une famille générique en dernier.

**Fichier final prévu :** `finals/slide-25-famille-generique.png`

---

### S26 — Pas de texte justifié par les styles

- **Acte :** 4. Typographie
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître un texte justifié par les styles et comprendre la gêne qu’il cause.
- **Badge :** `R. 191`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur la justification du texte.
- Idée principale : justifié, le texte perd les fins de lignes irrégulières qui servent de repères à l’œil.
- Scène : qui, Inès ; où, à une table de la bibliothèque ; objet, la présentation de l’atelier Lecture sur une tablette ; tension, le paragraphe justifié forme des espaces irréguliers et des rivières blanches ; action, Inès lit, l’air contrarié ; résultat, à droite, le même paragraphe aligné à gauche, elle lit à l’aise.
- Transformation visible : un bloc rectangulaire troué d’espaces, puis un bloc aux fins de lignes irrégulières.
- Test des trois secondes : « Le texte justifié se lit mal, le texte aligné à gauche mieux. »
- Ajout par rapport à la slide précédente : après la police, l’alignement.

**Référence de composition principale :** `N10` (personnage et écran).

**Texte visible (projection)**

- `Pas de texte justifié par les styles`
- `text-align: justify;`
- `IMPACT - Justifié, le texte fait perdre la ligne`
- `GARANTIE - Aligné à gauche, l’œil garde ses repères`

**Illustration :** Inès (bloc Inès) assise à gauche, tablette posée devant elle. Panneau gauche, cadre corail pâle : un paragraphe justifié, toutes les lignes de même longueur, blocs de mots séparés par des espaces très inégaux qui dessinent des rivières blanches verticales ; sous le panneau, `text-align: justify;` barré sobrement. Panneau droit, cadre vert pâle : le même paragraphe aligné à gauche, espaces réguliers, fins de lignes irrégulières, coche verte ; Inès sourit. Mots en blocs abstraits, sans lettres.

**Alternative textuelle à fournir :** dans un paragraphe justifié aux espaces irréguliers, Inès perd sa ligne ; aligné à gauche, avec des fins de lignes irrégulières, le même paragraphe se lit facilement.

**Règle → préjudice utilisateur :** la justification rend la lecture plus difficile pour de nombreux publics, notamment les personnes dyslexiques.

**Garantie recherchée (matière de l’oral)**

Lecture facilitée, notamment pour les personnes dyslexiques ; accessibilité.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : vérifier l’absence de `text-align: justify` dans le CSS et d’attributs `align="justify"` dans le HTML.
- Piège certification : le contrôle porte sur tout le CSS et sur le HTML, sans exception de média.

**Discours oral du présentateur (non projeté)**

#### Des fins de lignes qui servent de repères

- La justification est souvent jolie, notamment sur papier ; selon le livre, plusieurs études ont montré qu’elle rend la lecture plus difficile pour de nombreux publics.
- L’avis de l’expert l’explique : un texte justifié fait perdre à l’œil les repères fournis par les fins de lignes irrégulières.
- La gêne est particulièrement forte pour les personnes dyslexiques.
- Le contrôle cherche `text-align: justify` dans le CSS et l’attribut `align="justify"` dans le HTML.

##### Impact du non-respect

- Le lecteur perd sa ligne et relit ; certains renoncent.

##### Ce que garantit la règle

- Un texte dont les fins de lignes restent irrégulières, donc plus facile à suivre.

#### Transition

- Après l’alignement, la casse : les capitales décoratives.

**Mémo oral :** des fins de lignes libres pour garder ses repères.

**Fichier final prévu :** `finals/slide-26-texte-justifie.png`

---

### S27 — Capitales : par les styles, pas au clavier

- **Acte :** 4. Typographie
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître une mise en majuscules décorative saisie dans le contenu et connaître la propriété CSS adaptée.
- **Badge :** `R. 192`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur les majuscules décoratives.
- Idée principale : saisi en capitales dans le HTML, un titre reste en capitales même sans styles ; saisi normalement, il ne prend les capitales que par les styles.
- Scène : qui, Samuel ; où, à son bureau ; objet, deux titres d’ateliers qui s’affichent pareillement en capitales ; tension, impossible de voir à l’écran lequel a été saisi en capitales ; action, Samuel désactive les styles ; résultat, l’un reste `ATELIER RELIURE`, l’autre redevient `Atelier reliure`.
- Transformation visible : sans styles, un titre reste en capitales, l’autre non.
- Test des trois secondes : « Sans styles, on voit qui a été tapé en capitales. »
- Ajout par rapport à la slide précédente : après l’alignement, la casse.

**Référence de composition principale :** `S20` (deux fenêtres et code court). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Capitales : par les styles, pas au clavier`
- `ATELIER RELIURE`
- `Atelier reliure`
- `text-transform: uppercase;`
- `IMPACT - Saisies en capitales, elles s’imposent à tous`

**Illustration :** Samuel (bloc Samuel) à gauche, main sur un petit interrupteur de styles basculé. Une fenêtre agrandie « styles désactivés », en deux lignes. Ligne corail pâle : le titre `ATELIER RELIURE`, resté en capitales, petite croix corail. Ligne vert pâle : le titre `Atelier reliure`, en casse normale, coche verte, relié par un trait fin à la ligne de code `text-transform: uppercase;` sur une bande bleu clair, qui l’affiche en capitales quand les styles sont actifs. Aucun autre titre lisible.

**Alternative textuelle à fournir :** styles désactivés, un titre saisi en capitales reste « ATELIER RELIURE », tandis qu’un titre saisi normalement et mis en capitales par text-transform: uppercase redevient « Atelier reliure ».

**Règle → préjudice utilisateur :** un texte saisi en capitales impose sa forme : il ne s’adapte pas pour qui lit difficilement les textes entièrement en majuscules, et il se copie en capitales.

**Garantie recherchée (matière de l’oral)**

Un copier-coller indépendant de la mise en majuscules et une mise en forme adaptable aux difficultés de lecture.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : pour les contenus entièrement en majuscules, désactiver les styles, repérer ceux qui restent en majuscules et vérifier qu’ils respectent les conventions typographiques de la langue.
- Piège certification : sigles et noms d’auteurs dans une bibliographie peuvent rester en majuscules. Le comportement du copier-coller d’un texte transformé par `text-transform` varie selon les navigateurs (`NOT VERIFIED`) : l’objectif du livre est cité à l’oral, sans démonstration.

**Discours oral du présentateur (non projeté)**

#### Écrire normalement, décorer par les styles

- Il est possible d’écrire un texte en minuscules et de l’afficher en capitales avec `text-transform: uppercase`.
- L’utilisateur reste alors libre d’adapter la mise en forme ; le livre vise aussi un copier-coller indépendant de la mise en majuscules.
- Le livre rappelle qu’un texte en majuscules se lit moins rapidement.
- Le contrôle passe par la désactivation des styles : ce qui reste en majuscules a été saisi ainsi.
- Les sigles et les noms d’auteurs d’une bibliographie restent des usages typographiques normaux.

##### Impact du non-respect

- La mise en capitales s’impose à tous, y compris à qui lit mal les textes tout en majuscules.

##### Ce que garantit la règle

- Des capitales décoratives qui relèvent des styles, donc adaptables.

#### Transition

- Image, styles, police : trois façons de perdre un texte, à bien distinguer.

**Mémo oral :** on écrit normalement, les styles décorent.

**Fichier final prévu :** `finals/slide-27-majuscules.png`

---

### S28 — Image, style ou police : trois pertes

- **Acte :** 4. Typographie
- **Type :** distinction
- **Durée indicative :** 0:50
- **Objectif pédagogique :** distinguer trois façons de perdre un texte : figé dans une image, fabriqué par la CSS, détourné en icône.
- **Badge :** `R. 187 · 188 · 189`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : distinction entre trois règles techniques.
- Idée principale : trois mécanismes différents, une même exigence : que le sens existe en HTML.
- Scène : qui, Samuel ; où, devant un tableau blanc ; objet, trois éléments du site épinglés : le tableau des dates publié en image, la carte « Complet », l’icône calendrier ; tension, trois défauts qui se ressemblent ; action, Samuel trace sous chacun le mécanisme ; résultat, trois panneaux distincts et un bandeau commun.
- Transformation visible : trois objets, trois diagnostics.
- Test des trois secondes : « Trois façons de perdre un texte. »
- Ajout par rapport à la slide précédente : synthèse entre l’acte 2 et l’acte 4.

**Référence de composition principale :** `N17` (panneaux titrés). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Image, style ou police : trois pertes`
- `Texte figé dans une image`
- `Texte ajouté par les styles`
- `Caractère détourné en icône`
- `Dans les trois cas, le sens vit en HTML`

**Illustration :** Samuel (bloc Samuel) à gauche, feutre en main, devant un tableau blanc. Trois panneaux pastel titrés : bleu clair, `Texte figé dans une image`, le tableau des dates du trimestre en image, aux lettres pixellisées abstraites ; lavande, `Texte ajouté par les styles`, une carte d’atelier avec un ruban bleu marine vide et une petite accolade ; vert d’eau, `Caractère détourné en icône`, une icône calendrier à côté d’une case de caractère en pointillés. Bandeau vert pâle à icône de coche : `Dans les trois cas, le sens vit en HTML`.

**Alternative textuelle à fournir :** trois défauts distincts : un texte figé dans une image, un texte ajouté par les styles, un caractère détourné en icône ; dans les trois cas, le sens doit exister en HTML.

**Règle → préjudice utilisateur :** se tromper de mécanisme conduit à un correctif inopérant.

**Garantie recherchée (matière de l’oral)**

Identifier le mécanisme pour choisir le bon remède.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : image de texte, revue visuelle des images ; contenu généré, lecture du CSS (`content`, `background-image`, pseudo-éléments) et désactivation des images d’arrière-plan ; icône de police, examen du code des icônes.
- Piège certification : une image d’arrière-plan CSS qui simule un texte éditorial est d’abord une image de texte ; si elle porte une information absente du HTML, la règle sur les contenus générés est aussi concernée.

**Discours oral du présentateur (non projeté)**

#### Trois mécanismes, trois remèdes

- Le texte figé dans une image se remplace par du texte stylé.
- Le texte écrit par la feuille de styles reçoit une alternative dans le HTML.
- Le caractère de police détourné en icône reçoit un libellé masqué dans le lien.
- Les trois règles se rejoignent sur un principe : le sens doit exister dans le HTML.
- Le mécanisme en cause désigne la règle.

#### Transition

- Chaque défaut typographique se loge à un endroit précis.

**Mémo oral :** image, style ou police : trouver le mécanisme.

**Fichier final prévu :** `finals/slide-28-distinction-image-style-police.png`

---

### S29 — Checkpoint 4 : typographie

- **Acte :** 4. Typographie
- **Type :** checkpoint
- **Durée indicative :** 1:20
- **Objectif pédagogique :** réactiver les quatre règles de l’acte 4.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : checkpoint de l’acte 4.
- Idée principale : rattacher chaque constat typographique à sa règle.
- Scène : qui, Samuel ; où, à son bureau ; objet, quatre cartes de constats ; tension, quatre défauts typographiques ; action, Samuel les compare ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Un exercice en quatre cas. »
- Ajout par rapport à la slide précédente : l’apprenant applique.

**Référence de composition principale :** `N17` (cartes pastel). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Checkpoint 4 : typographie`
- `Quelle règle est en jeu ?`
- `A. Programme en image JPG`
- `B. font-family: "Lisières Sans";`
- `C. text-align: justify;`
- `D. Titres saisis en capitales`

**Illustration :** question dans un bandeau bleu clair sous le titre. Quatre cartes pastel portant chacune sa ligne et une mini-scène sans autre texte : A, le tableau des dates du trimestre en image, aux lettres pixellisées abstraites ; B, une petite icône de police ; C, un bloc de lignes de même longueur aux espaces irréguliers ; D, un titre en grandes capitales abstraites. Samuel (bloc Samuel) à gauche. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** exercice : quatre constats typographiques à rattacher chacun à une règle.

**Règle → préjudice utilisateur :** sans le bon rattachement, on corrige la casse alors que le texte est une image, ou l’inverse.

**Garantie recherchée (matière de l’oral)**

Rattacher le constat à sa règle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : une minute de réflexion.
- Revue : relire les lignes de code B et C caractère par caractère sur le PNG.
- Piège certification : en B, la police citée est fictive ; ce qui manque, c’est la famille générique en fin de liste.

**Discours oral du présentateur (non projeté)**

#### Où se trouve le défaut ?

- Dans une image, dans une déclaration de police, dans l’alignement ou dans la saisie du texte.
- Chaque emplacement correspond à une règle.

#### Transition

- Et quand la page passe au papier ?

**Corrigé (notes du présentateur, non projeté) :** A → 187 : texte mis en image alors que les styles pouvaient le mettre en forme (distracteur : 188). B → 190 : aucune famille générique en fin de liste (distracteur : 187). C → 191 : texte justifié par les styles (distracteur : 192). D → 192 : majuscules décoratives saisies dans le contenu au lieu des styles (distracteur : 187).

**Mémo oral :** image, police, alignement, casse.

**Fichier final prévu :** `finals/slide-29-checkpoint-4.png`

---

### S30 — Prévoir la page sur papier

- **Acte :** 5. Imprimer
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître l’absence de styles d’impression et connaître les façons de les déclarer.
- **Badge :** `R. 195`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur les styles dédiés à l’impression, ouverture de l’acte 5.
- Idée principale : imprimée sans styles prévus pour le papier, la page sort comme une copie d’écran, mal adaptée.
- Scène : qui, Odette ; où, dans le salon de Nora ; objet, le programme imprimé qu’elle veut annoter ; tension, la feuille sort comme l’écran : aplats de couleur, gros boutons d’interface, typographie d’écran ; action, Odette approche son crayon ; résultat, à droite, la page imprimée avec des styles d’impression, sobre et lisible, qu’elle annote.
- Transformation visible : d’une copie d’écran sur papier à une feuille sobre.
- Test des trois secondes : « Sans styles prévus pour le papier, l’impression est ratée. »
- Ajout par rapport à la slide précédente : on quitte l’écran pour le papier.

**Référence de composition principale :** `N10` (personnage et objet).

**Texte visible (projection)**

- `Acte 5 · Imprimer`
- `Prévoir la page sur papier`
- `@media print`
- `IMPACT - Imprimée telle quelle, la page sort mal adaptée`
- `CONTRÔLE - Aperçu, puis code print`

**Illustration :** Odette (bloc Odette) assise à une table, crayon en main. Feuille gauche, cadre corail pâle : larges aplats de couleur d’écran et gros boutons d’interface en blocs abstraits, sans place pour annoter. Feuille droite, cadre vert pâle : mise en page sobre en noir sur blanc, une colonne, blocs de texte aérés, quelques annotations au crayon en traits abstraits, coche verte. Entre les deux, sur une bande de code bleu clair, `@media print`. Feuilles en blocs abstraits.

**Alternative textuelle à fournir :** imprimé sans styles d’impression, le programme sort comme à l’écran, chargé d’aplats de couleur et de boutons ; avec des styles dédiés au papier, Odette reçoit une feuille sobre qu’elle peut annoter.

**Règle → préjudice utilisateur :** sans styles d’impression, le contenu s’imprime sous une forme inadaptée au papier.

**Garantie recherchée (matière de l’oral)**

Impression des contenus sous une forme appropriée au support.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : un aperçu avant impression permet une évaluation rapide ; la confirmation exige l’examen du code : `link` ou `style` avec `media="print"`, règle `@media print {…}` ou `@import url("print.css") print;`.
- Piège certification : les styles d’impression peuvent corriger une feuille globale ou s’appliquer seuls ; un aperçu propre ne prouve pas à lui seul leur présence. Le livre contient des guillemets altérés dans ses exemples de code (`=”`) : citer la syntaxe corrigée.

**Discours oral du présentateur (non projeté)**

#### Prévoir le passage au papier

- Il est possible de prévoir comment le contenu d’une page doit s’imprimer : c’est le rôle des feuilles de styles pour le média print.
- L’avis de l’expert en cite des usages : adapter la typographie au papier, ne garder que le contenu propre de la page, afficher l’adresse de chaque lien.
- Une feuille d’impression dispense de publier une version HTML spécifique pour l’impression.
- L’aperçu avant impression donne une première idée ; la confirmation passe par le code.

##### Impact du non-respect

- La feuille sort comme une copie d’écran : aplats de couleur, éléments d’interface, typographie peu adaptée au papier.

##### Ce que garantit la règle

- La présence de styles dédiés à l’impression ; leur qualité se juge ensuite à l’aperçu.

#### Transition

- Le premier usage attendu de ces styles : retirer la navigation.

**Mémo oral :** l’écran et le papier ont chacun leurs styles.

**Fichier final prévu :** `finals/slide-30-styles-impression.png`

---

### S31 — Sur papier, les menus ne servent à rien

- **Acte :** 5. Imprimer
- **Type :** règle
- **Durée indicative :** 1:05
- **Objectif pédagogique :** reconnaître l’impression des blocs de navigation et connaître le contrôle par l’aperçu.
- **Badge :** `R. 196`

**Masque :** `MASQUE RÈGLE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, à gauche, le sous-titre d’acte s’il figure dans la liste, puis le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène illustrée de la fiche, avec ses lignes de code et ses libellés d’interface s’ils figurent dans la liste. En bas, une seule rangée d’encadrés pastel à icône, de hauteur égale : exactement un encadré par ligne IMPACT, GARANTIE, CONTRÔLE ou LIMITE de la liste, ni plus ni moins.

**Fiche PDS**

- Rôle : règle sur l’impression sans blocs de navigation.
- Idée principale : imprimés, les menus, la recherche et le formulaire de newsletter n’ont plus de fonction et gaspillent du papier.
- Scène : qui, Odette ; où, dans le salon de Nora ; objet, deux feuilles imprimées pour une seule page web ; tension, elle pose le doigt sur un menu imprimé, rien ne se passe ; action, elle met la feuille de côté ; résultat, à droite, une seule feuille avec le seul contenu.
- Transformation visible : deux feuilles encombrées de menus, puis une feuille de contenu.
- Test des trois secondes : « Imprimer les menus ne sert à rien. »
- Ajout par rapport à la slide précédente : l’usage le plus attendu des styles d’impression.

**Référence de composition principale :** `N10` (personnage et objet).

**Texte visible (projection)**

- `Sur papier, les menus ne servent à rien`
- `@media print`
- `nav { display: none; }`
- `IMPACT - Les menus imprimés gaspillent le papier`
- `GARANTIE - Seul le contenu s’imprime`

**Illustration :** Odette (bloc Odette) assise à gauche, index posé sur une feuille où l’on reconnaît une barre de menu, un champ de recherche et un petit formulaire d’inscription, en blocs abstraits ; une seconde feuille presque vide dépasse derrière ; cadre corail pâle. À droite, cadre vert pâle : une seule feuille ne portant que le titre et le contenu en blocs abstraits, coche verte. Sous la scène, sur une bande de code bleu clair, deux lignes : `@media print` puis, en retrait, `nav { display: none; }`.

**Alternative textuelle à fournir :** imprimée avec ses menus, sa recherche et son formulaire de newsletter, la page tient sur deux feuilles ; avec les blocs de navigation masqués à l’impression, une feuille de contenu suffit.

**Règle → préjudice utilisateur :** les blocs de navigation imprimés occupent une place inutile, nuisent à la lisibilité et gaspillent du papier.

**Garantie recherchée (matière de l’oral)**

Contenus imprimés plus lisibles et pertinents, économie de papier, impact énergétique moindre.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : dans l’aperçu avant impression, vérifier qu’aucun menu ni autre bloc de navigation ne s’affiche : menus `nav`, éléments d’en-tête ou de pied de page comme un formulaire de recherche, des liens annexes ou un formulaire d’inscription à une newsletter.
- Piège certification : solution du livre, une feuille de styles print qui masque ces blocs via la propriété `display`. Ici, l’aperçu suffit au contrôle, contrairement à la règle sur les styles d’impression.

**Discours oral du présentateur (non projeté)**

#### La navigation n’a de sens qu’à l’écran

- Sur papier, toucher un menu ne déclenche rien : le livre en fait l’expérience avec une feuille A4.
- Formulaire de recherche, liens annexes, inscription à la newsletter : tous ces blocs de navigation sont inutiles à l’impression.
- La solution du livre : une feuille de styles print qui les masque par la propriété `display`.
- Le contrôle est immédiat : l’aperçu avant impression.

##### Impact du non-respect

- Des feuilles encombrées, moins lisibles, et du papier gaspillé.

##### Ce que garantit la règle

- Un document imprimé limité au contenu propre de la page.

#### Transition

- Les deux règles d’impression se vérifient de deux façons différentes.

**Mémo oral :** sur papier, seulement le contenu.

**Fichier final prévu :** `finals/slide-31-impression-sans-navigation.png`

---

### S32 — Impression : deux contrôles

- **Acte :** 5. Imprimer
- **Type :** distinction
- **Durée indicative :** 0:50
- **Objectif pédagogique :** distinguer la présence de styles d’impression et l’impression effective sans navigation.
- **Badge :** `R. 195 · 196`

**Masque :** `MASQUE COMPARAISON`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes ; sous le titre, aligné à droite, le badge de règle dans un petit cartouche bleu clair. Au centre, la scène de la fiche organisée en panneaux pastel côte à côte, un panneau par ligne de la liste située entre le titre et la dernière ligne, chaque panneau titré de sa ligne. En bas, un seul bandeau pleine largeur, à icône, portant la dernière ligne de la liste. Aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : distinction entre les deux règles d’impression.
- Idée principale : on peut avoir des styles print et imprimer encore les menus ; le code juge l’une, l’aperçu l’autre.
- Scène : qui, Samuel ; où, entre son écran et l’imprimante ; objet, à gauche le code avec une feuille print, à droite l’aperçu avant impression ; tension, la feuille print existe mais l’aperçu montre encore le menu ; action, Samuel pointe le menu dans l’aperçu ; résultat, deux panneaux nommant chacun son contrôle.
- Transformation visible : une coche verte sur le code, un point d’interrogation corail sur l’aperçu.
- Test des trois secondes : « Avoir des styles print ne suffit pas à masquer les menus. »
- Ajout par rapport à la slide précédente : la relation entre les deux règles.

**Référence de composition principale :** `N03` (deux panneaux et bandeau final). Ancre de personnage : `A-SAMUEL` si disponible.

**Texte visible (projection)**

- `Impression : deux contrôles`
- `Il existe des styles print`
- `Les menus disparaissent-ils à l’impression ?`
- `Une feuille print peut encore imprimer les menus`

**Illustration :** Samuel (bloc Samuel) au centre. Panneau bleu clair, titré `Il existe des styles print` : une fenêtre de code en lignes abstraites avec une accolade, coche verte. Panneau lavande, titré `Les menus disparaissent-ils à l’impression ?` : un aperçu de feuille où une barre de menu apparaît encore, point d’interrogation corail. Bandeau orange pâle à icône d’avertissement : `Une feuille print peut encore imprimer les menus`.

**Alternative textuelle à fournir :** deux contrôles distincts : au code, des styles d’impression existent ; à l’aperçu, les menus doivent disparaître. Une feuille print peut encore laisser imprimer les menus.

**Règle → préjudice utilisateur :** conclure de la seule présence d’une feuille print que l’impression est propre laisse passer des pages encombrées.

**Garantie recherchée (matière de l’oral)**

Chaque règle se vérifie avec son propre contrôle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Contrôle : styles d’impression, examen du code ; blocs de navigation, aperçu avant impression.
- Piège certification : l’absence de style print dans le code suffit à constater le défaut de la règle sur les styles d’impression ; pour celle sur les blocs de navigation, il faut regarder l’aperçu.

**Discours oral du présentateur (non projeté)**

#### Le code d’un côté, l’aperçu de l’autre

- Une feuille de styles print existe : la règle sur les styles d’impression est respectée, le code le montre.
- L’aperçu montre pourtant le menu : la règle sur l’impression sans navigation ne l’est pas.
- Une même feuille print peut satisfaire l’une et manquer l’autre.

#### Transition

- Ces défauts ne s’arrêtent pas aux frontières de la rubrique.

**Mémo oral :** le code pour les styles, l’aperçu pour les menus.

**Fichier final prévu :** `finals/slide-32-distinction-impression.png`

---

### S33 — D’autres rubriques en écho

- **Acte :** 6. S’entraîner
- **Type :** transversalité
- **Durée indicative :** 1:00
- **Objectif pédagogique :** relier quatre règles de la rubrique à des règles voisines d’autres rubriques, telles que le livre les évoque.
- **Badge :** aucun ; numéros en texte

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : transversalité, ouverture de l’acte 6.
- Idée principale : plusieurs défauts de présentation se prolongent dans les rubriques Navigation et Liens.
- Scène : qui, Nora ; où, au centre du hall de la Maison des Lisières ; objet, quatre portes ouvertes vers d’autres salles ; tension, aucune ; action, Nora regarde les portes ; résultat, quatre liens visibles entre une règle de la rubrique et une règle voisine.
- Transformation visible : de la rubrique isolée à ses voisines.
- Test des trois secondes : « Ces règles ont des voisines dans d’autres rubriques. »
- Ajout par rapport à la slide précédente : on sort de la rubrique.

**Référence de composition principale :** `N01` (centre relié à des pastilles). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Acte 6 · S’entraîner`
- `D’autres rubriques en écho`
- `181 → 157 Item actif de menu`
- `182 → 140 Liens différenciés`
- `180 → 158 Mêmes emplacements`
- `189 → 136 Intitulé de lien`

**Illustration :** composition proche de la référence N01. Sous-titre d’acte puis titre centrés. Au centre, Nora (Bloc personnage) debout dans un hall clair. Quatre portes ouvertes, deux à gauche, deux à droite, reliées à Nora par une ligne fine et une pastille, chacune surmontée de son panneau (une ligne de liens par porte). Derrière chaque porte, une mini-scène sans texte : un menu dont un item est marqué d’un trait et d’une couleur ; un paragraphe avec un lien souligné ; deux pages avec le menu au même endroit ; une icône calendrier accompagnée d’une étiquette en pointillés.

**Alternative textuelle à fournir :** quatre liens vers d’autres rubriques : couleur seule et items actifs de menu, contraste et liens différenciés, charte graphique et blocs de navigation aux mêmes emplacements, pictogrammes typographiques et intitulé de lien.

**Règle → préjudice utilisateur :** auditer une rubrique isolément fait manquer les défauts qui se prolongent ailleurs.

**Garantie recherchée (matière de l’oral)**

Un même constat peut appeler plusieurs règles ; les relier évite les oublis.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : libellés relus dans la checklist V5 ; chaque lien s’appuie sur un passage du livre (tableau des règles connexes).
- Piège certification : ces rapprochements sont pédagogiques ; un même défaut ne viole pas automatiquement les deux règles reliées.

**Discours oral du présentateur (non projeté)**

#### Des passages du livre qui ouvrent sur d’autres rubriques

- La règle sur la couleur cite le menu où la rubrique en cours ne se distingue que par sa couleur : la rubrique Navigation demande de signaler les items actifs de menu.
- L’avis de l’expert sur le contraste évoque les liens non soulignés : la rubrique Liens demande de les différencier visuellement du contenu.
- Le contrôle de la charte graphique regarde l’emplacement des menus : en Navigation, les blocs de même nature restent aux mêmes emplacements.
- Le libellé masqué d’une icône de police rejoint la règle qui demande un intitulé à chaque lien.
- Le formulaire sans styles rejoint, en Formulaires, l’association de chaque champ à son étiquette dans le code.
- Ces rapprochements sont pédagogiques : un défaut n’enfreint pas automatiquement les deux règles.

#### Transition

- Un constat précis désigne une règle précise.

**Mémo oral :** un constat, parfois plusieurs rubriques.

**Fichier final prévu :** `finals/slide-33-transversalite.png`

---

### S34 — Évaluation 1/2

- **Acte :** 6. S’entraîner
- **Type :** évaluation
- **Durée indicative :** 2:00
- **Objectif pédagogique :** évaluer la distinction entre couleur seule, contraste et désignation par la forme ou la position.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : première moitié de l’évaluation finale.
- Idée principale : quatre constats, une seule règle prouvée enfreinte par constat.
- Scène : qui, Nora ; où, à une table, carnet ouvert ; objet, quatre cartes de constats ; tension, des constats voisins ; action, Nora note ses réponses ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Quatre questions d’évaluation. »
- Ajout par rapport à la slide précédente : l’évaluation commence.

**Référence de composition principale :** `N17` (cartes pastel). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Évaluation 1/2`
- `Quelle règle est prouvée enfreinte ?`
- `1. « Complet » à 2:1`
- `2. « En orange : complets »`
- `3. Seul repère : « à droite »`
- `4. Plan en aplats colorés seuls`

**Illustration :** question dans un bandeau bleu clair sous le titre. Quatre cartes pastel numérotées portant chacune sa ligne et une mini-illustration sans autre texte : 1, une ligne gris très pâle sur fond blanc et une petite pipette ; 2, des cartes d’ateliers dont certaines teintées d’orange ; 3, une flèche vers la droite ; 4, un plan de salles en aplats de couleur, sans bordure ni motif. Nora (Bloc personnage) à gauche, carnet ouvert. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** évaluation, première partie : quatre constats de perception et de désignation, à rattacher chacun à la règle qu’ils prouvent enfreinte.

**Règle → préjudice utilisateur :** sans distinction fine, on applique le mauvais contrôle.

**Garantie recherchée (matière de l’oral)**

Choisir la règle selon ce qui est perdu : le sens codé par la couleur, la lisibilité, ou le repère visuel.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : demander une réponse écrite par question, puis corriger après les deux slides ; environ deux minutes.
- Piège certification : en 2, le mot « orange » est écrit, mais c’est la couleur seule qui désigne les ateliers complets. En 1 et 3, le constat apporte sa preuve : un ratio mesuré, un repère unique.

**Discours oral du présentateur (non projeté)**

#### Ce qui est perdu désigne la règle

- Un texte dont le ratio mesuré est sous le seuil relève du contraste.
- Une information portée par la seule couleur relève de la couleur seule, même quand la couleur est nommée dans le texte.
- Une désignation dont la position est le seul repère relève de la forme et de la position.

#### Transition

- La même exigence de preuve vaut pour le téléphone et l’impression.

**Corrigé (notes du présentateur, non projeté) :** Q1 → 182 : ratio de 2:1, inférieur au seuil de 3:1 retenu par le livre ; le mot existe, seule sa lisibilité est en cause (distracteur : 181, aucune information n’est codée par la couleur). Q2 → 181 : les ateliers complets ne sont désignés que par leur couleur (distracteur : 184, la consigne ne parle ni de forme ni de position). Q3 → 184 : la position est le seul repère donné (distracteur : 181). Q4 → 181 : zones distinguées par de simples aplats de couleur, exemple du contrôle du livre (distracteur : 182, le contraste des aplats n’est pas la question).

**Mémo oral :** ce qui est perdu désigne la règle.

**Fichier final prévu :** `finals/slide-34-evaluation-1.png`

---

### S35 — Évaluation 2/2

- **Acte :** 6. S’entraîner
- **Type :** évaluation
- **Durée indicative :** 1:45
- **Objectif pédagogique :** évaluer la distinction entre styles d’impression, impression sans navigation, zoom et adaptation mobile.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : seconde moitié de l’évaluation finale.
- Idée principale : quatre constats, une seule règle prouvée enfreinte par constat.
- Scène : qui, Nora ; où, à la même table ; objet, quatre cartes de constats ; tension, des constats voisins deux à deux ; action, Nora poursuit ses réponses ; résultat, aucune réponse visible.
- Transformation visible : aucune ; les réponses restent dans les notes.
- Test des trois secondes : « Quatre autres questions. »
- Ajout par rapport à la slide précédente : les distinctions d’adaptation et d’impression.

**Référence de composition principale :** `N17` (cartes pastel). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Évaluation 2/2`
- `Quelle règle est prouvée enfreinte ?`
- `5. Code : aucun style print`
- `6. Style print, menus imprimés`
- `7. Site adapté, zoom bloqué`
- `8. Téléphone : page bureau`

**Illustration :** même composition que S34. Quatre cartes pastel numérotées 5 à 8, chacune portant sa ligne et une mini-illustration sans autre texte : 5, une fenêtre de code aux lignes abstraites et une loupe ; 6, une feuille imprimée portant une barre de menu ; 7, un téléphone sous deux doigts écartés, page figée ; 8, un téléphone affichant trois colonnes réduites. Nora (Bloc personnage) à gauche, crayon en main. Aucune coche, aucune croix, aucun numéro de règle.

**Alternative textuelle à fournir :** évaluation, seconde partie : quatre constats d’impression et d’adaptation mobile, à rattacher chacun à la règle qu’ils prouvent enfreinte.

**Règle → préjudice utilisateur :** confondre ces règles fait conclure trop vite, ou corriger le mauvais mécanisme.

**Garantie recherchée (matière de l’oral)**

Un constat ne prouve que ce qu’il observe.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : corriger les huit questions avant le grand cas.
- Piège certification : en 5, le constat au code prouve le défaut des styles d’impression ; il ne dit rien de l’aperçu, donc rien de prouvé sur les menus imprimés.

**Discours oral du présentateur (non projeté)**

#### Un constat ne prouve que ce qu’il observe

- Un constat au code renseigne sur la présence de styles d’impression, pas sur ce que montre l’aperçu.
- Un aperçu qui imprime les menus prouve un défaut même quand une feuille print existe.
- Un zoom bloqué reste un défaut sur un site adapté ; une page bureau sur téléphone signale l’absence d’adaptation.

#### Transition

- Toutes ces règles se retrouvent dans une même page.

**Corrigé (notes du présentateur, non projeté) :** Q5 → 195 : aucun style dédié à l’impression dans le code (distracteur : 196, l’aperçu n’a pas été observé). Q6 → 196 : des styles print existent, mais les blocs de navigation s’impriment (distracteur : 195, respectée). Q7 → 193 : zoom bloqué malgré l’adaptation (distracteur : 194, l’adaptation existe). Q8 → 194 : aucun mécanisme d’adaptation mobile (distracteur : 193, rien n’indique que le zoom soit bloqué).

**Mémo oral :** un constat ne prouve que ce qu’il observe.

**Fichier final prévu :** `finals/slide-35-evaluation-2.png`

---

### S36 — Grand cas : trouvez sept défauts

- **Acte :** 6. S’entraîner
- **Type :** grand cas
- **Durée indicative :** 4:00
- **Objectif pédagogique :** mobiliser toutes les distinctions sur une scène intégratrice.
- **Badge :** aucun

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : grand cas de synthèse.
- Idée principale : une seule scène du fil rouge contient sept défauts de présentation à retrouver.
- Scène : qui, aucun personnage (exception déclarée) ; où, un plan de travail neutre ; objet, la page Programme dans une fenêtre de navigateur et sa feuille imprimée ; tension, sept défauts discrets ; action, une pipette a mesuré les horaires ; résultat, aucun repère numéroté visible.
- Transformation visible : aucune ; c’est la scène de S37 sans ses repères.
- Test des trois secondes : « Une page à auditer, avec son impression. »
- Ajout par rapport à la slide précédente : toutes les règles dans une seule scène.

**Fabrication :** obtenue par édition ImageGen du PNG validé de S37 (voir « Fabrication du grand cas ») : retirer les sept pastilles numérotées, les traits et les étiquettes, conserver la pipette et le cartouche `1,8:1`, remplacer le titre `Correction` par `Grand cas : trouvez sept défauts`, ne rien changer d’autre.

**Référence de composition principale :** le PNG validé de S37, image à éditer ; en repli, les références du contrat de fabrication et S37 (voir « Fabrication du grand cas »).

**Texte visible (projection)**

- `Grand cas : trouvez sept défauts`
- `Voir le bouton à droite`
- `1,8:1`

**Illustration :** identique à S37, sans pastilles numérotées, traits ni étiquettes. Aucun personnage. La fenêtre de navigateur occupe les deux tiers gauches de la largeur ; la feuille imprimée, en grand et inclinée, occupe le tiers droit ; entre les deux, une colonne étroite reste vide. Les sept défauts, dans l’ordre de S37 : (1) en haut de la page, le tableau des dates du trimestre publié comme une image, formes de lettres abstraites nettement pixellisées ; (2) un paragraphe de présentation justifié, lignes de même longueur aux espaces irréguliers ; (3) trois cartes d’ateliers : une pastille rouge marque l’atelier complet, une pastille verte un atelier libre, sans autre signe, de sorte que seule la couleur porte l’information ; (4) sous les cartes, des lignes d’horaires gris très pâle sur ivoire, avec une petite pipette posée dessus et, tout près, le cartouche `1,8:1` ; (5) le bouton d’inscription minuscule, sans libellé lisible, à droite de l’encadré d’aide, à côté d’un second bouton de taille normale, lui aussi sans libellé, qui donne l’échelle ; (6) l’encadré d’aide, à gauche de ces deux boutons, portant `Voir le bouton à droite` ; (7) dans le tiers droit, la feuille imprimée de la page, avec en haut une barre de menu bien visible, puis un champ de recherche et un petit formulaire en bas.

**Alternative textuelle à fournir :** grand cas : la page Programme de la Maison des Lisières et son impression, présentant sept défauts de présentation à identifier ; sur les horaires, un ratio de contraste mesuré de 1,8 pour 1.

**Règle → préjudice utilisateur :** chaque défaut paraît mineur ; ensemble, ils rendent la page difficile à lire, à utiliser et à imprimer.

**Garantie recherchée (matière de l’oral)**

Auditer une page et son impression, pas un détail isolé.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : quatre minutes en binôme, puis correction en S37.
- Revue : critères d’acceptation de la section « Fabrication du grand cas » ; aucun repère numéroté, trait ou étiquette résiduel ; pipette et cartouche `1,8:1` conservés ; aucun personnage ; chaque texte une seule fois.
- Piège certification : la scène ne permet de juger ni la famille générique de police, ni le zoom, ni l’adaptation mobile.

**Discours oral du présentateur (non projeté)**

#### Une page et son impression

- La page Programme de la Maison des Lisières réunit des défauts de présentation de toute la rubrique.
- Une page se juge aussi sur papier : sa version imprimée porte ses propres défauts.
- Une mesure figure déjà sur la page : le ratio relevé sur les horaires.
- Seul compte ce qui s’observe ; ce qui demande le code ou un autre appareil ne se juge pas à l’œil.

#### Transition

- Chaque défaut observé désigne une règle.

**Corrigé (notes du présentateur, non projeté) :** voir S37.

**Mémo oral :** auditer ce que l’on voit, rien de plus.

**Fichier final prévu :** `finals/slide-36-grand-cas.png`

---

### S37 — Correction

- **Acte :** 6. S’entraîner
- **Type :** correction projetée
- **Durée indicative :** 1:45
- **Objectif pédagogique :** corriger le grand cas en reliant chaque repère à sa règle.
- **Badge :** aucun ; numéros en texte

**Masque :** `MASQUE EXERCICE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine aligné à gauche, sur une ou deux lignes. Une ligne de la liste terminée par un point d’interrogation occupe un bandeau bleu clair pleine largeur sous le titre ; sans une telle ligne, il n’y a pas de bandeau. Au centre, la composition décrite par la fiche, cartes d’items alignées ou scène unique ; chaque autre texte de la liste est placé où la fiche l’indique. Aucun badge, aucun encadré IMPACT, GARANTIE, CONTRÔLE ou LIMITE, aucune réponse visible hors de la liste.

**Fiche PDS**

- Rôle : correction projetée du grand cas, seule slide avec corrigé visible.
- Idée principale : chaque défaut repéré correspond à une règle.
- Scène : qui, aucun personnage (exception déclarée) ; où, la même composition qu’en S36 ; objet, la page Programme et sa feuille imprimée ; tension, sept défauts ; action, sept pastilles numérotées se posent sur les défauts ; résultat, chaque défaut est relié à une étiquette verte, dans la colonne réservée.
- Transformation visible : la scène du grand cas, annotée.
- Test des trois secondes : « Sept défauts, chacun nommé et rattaché à sa règle. »
- Ajout par rapport à la slide précédente : les réponses.

**Fabrication :** cinquième étalon, première image générée de la série (voir « Fabrication du grand cas »). Après sa validation, son PNG sert d’image à éditer pour S36.

**Référence de composition principale :** `S20` (fenêtre détaillée et repères sobres), sans reprendre son personnage.

**Texte visible (projection)**

- `Correction`
- `Voir le bouton à droite`
- `1,8:1`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `Image de texte → 187`
- `Justifié → 191`
- `Couleur seule → 181`
- `Ratio → 182`
- `Petite cible → 186`
- `Position → 184`
- `Impression → 196`

**Illustration :** Aucun personnage. La fenêtre de navigateur occupe les deux tiers gauches de la largeur ; la feuille imprimée, en grand et inclinée, occupe le tiers droit ; entre les deux, une colonne étroite est réservée aux étiquettes. Page Programme en blocs abstraits, avec exactement sept défauts : (1) en haut de la page, le tableau des dates du trimestre publié comme une image, formes de lettres abstraites nettement pixellisées ; (2) un paragraphe de présentation justifié, lignes de même longueur aux espaces irréguliers ; (3) trois cartes d’ateliers : une pastille rouge marque l’atelier complet, une pastille verte un atelier libre, sans autre signe, de sorte que seule la couleur porte l’information ; (4) sous les cartes, des lignes d’horaires gris très pâle sur ivoire, avec une petite pipette posée dessus et, tout près, le cartouche `1,8:1` ; (5) le bouton d’inscription minuscule, sans libellé lisible, à droite de l’encadré d’aide, à côté d’un second bouton de taille normale, lui aussi sans libellé, qui donne l’échelle ; (6) l’encadré d’aide, à gauche de ces deux boutons, portant `Voir le bouton à droite` ; (7) dans le tiers droit, la feuille imprimée de la page, avec en haut une barre de menu bien visible, puis un champ de recherche et un petit formulaire en bas. Sur chaque défaut, une pastille bleu marine portant son chiffre, reliée par un trait fin à une étiquette verte placée dans la colonne réservée : 1 `Image de texte → 187`, 2 `Justifié → 191`, 3 `Couleur seule → 181`, 4 `Ratio → 182`, 5 `Petite cible → 186`, 6 `Position → 184`, 7 `Impression → 196`. Les étiquettes ne masquent aucun défaut, pour que leur retrait en S36 n’oblige pas à redessiner la page.

**Alternative textuelle à fournir :** correction du grand cas : sept défauts numérotés, chacun associé à sa règle : texte en image, texte justifié, couleur seule, ratio de contraste de 1,8 pour 1 sous le seuil, cible trop petite, désignation par la position, menus imprimés.

**Règle → préjudice utilisateur :** une correction sans rattachement ne prépare pas à l’examen.

**Garantie recherchée (matière de l’oral)**

Chaque repère corrigé rend la page plus lisible, plus utilisable ou mieux imprimée.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Animation : comparer les réponses des binômes et compter les règles trouvées.
- Revue : sept défauts présents et seuls, sept pastilles, sept étiquettes exactes dans la colonne réservée ; cartouche `1,8:1` près des horaires ; aucun personnage.
- Piège certification : ce que la scène ne permet pas de juger ne se déclare pas non conforme : famille générique de police, zoom, adaptation mobile, contenus générés ou masqués.

**Discours oral du présentateur (non projeté)**

#### Sept défauts, sept règles

- Le tableau des dates est une image de texte : un contenu éditorial qui devait rester du texte stylé.
- Le paragraphe est justifié par les styles.
- Seule une pastille rouge signale l’atelier complet : la couleur porte seule l’information.
- Sur les horaires gris pâle, le ratio mesuré, 1,8 pour 1, est sous le seuil.
- Le bouton d’inscription est trop petit pour un doigt.
- L’aide désigne un bouton par sa position.
- L’impression emporte le menu, la recherche et le formulaire.

#### Ce que l’observation ne permet pas de juger

- La police de secours, le zoom, l’adaptation mobile, les contenus générés ou masqués demandent le code ou un autre appareil.

#### Transition

- Derrière ces réponses, cinq distinctions reviennent sans cesse.

**Mémo oral :** corriger, rattacher, ne pas conclure sans voir.

**Fichier final prévu :** `finals/slide-37-correction-grand-cas.png`

---

### S38 — Cinq distinctions à retenir

- **Acte :** 6. S’entraîner
- **Type :** mémo
- **Durée indicative :** 0:45
- **Objectif pédagogique :** offrir une fiche de révision.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : mémo de révision.
- Idée principale : cinq paires ou triplets de règles à ne pas confondre.
- Scène : qui, Nora ; où, devant un tableau de liège ; objet, cinq fiches ; tension, aucune ; action, Nora épingle la dernière fiche ; résultat, cinq fiches alignées.
- Transformation visible : les cinq distinctions réunies.
- Test des trois secondes : « Cinq confusions à éviter. »
- Ajout par rapport à la slide précédente : la synthèse des distinctions.

**Référence de composition principale :** `N17` (panneaux alignés). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Cinq distinctions à retenir`
- `Couleur seule / contraste`
- `Couleur / forme ou position`
- `Image / style / icône de police`
- `Zoom / adaptation mobile`
- `Styles print / sans menus`

**Illustration :** titre centré. Nora (Bloc personnage) à droite, bras levé, épinglant la cinquième fiche sur un tableau de liège clair. Cinq fiches pastel en rangée, chacune portant une distinction et une mini-icône : deux pastilles ; une pastille et un cercle ; une image, une accolade, une icône calendrier ; deux doigts et un téléphone ; une imprimante et une barre de menu barrée.

**Alternative textuelle à fournir :** mémo des cinq distinctions : couleur seule et contraste ; couleur et forme ou position ; image de texte, contenu généré par les styles et icône de police ; zoom et adaptation mobile ; styles d’impression et impression sans menus.

**Règle → préjudice utilisateur :** ces confusions mènent au mauvais rattachement.

**Garantie recherchée (matière de l’oral)**

Une distinction, un contrôle.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : barres obliques et ordre des cinq fiches sur le PNG.
- Piège certification : aucun nouveau.

**Discours oral du présentateur (non projeté)**

#### Cinq confusions fréquentes

- Couleur seule ou contraste : le sens porté par la couleur, ou la lisibilité du texte.
- Couleur ou forme et position : quel repère visuel désigne le contenu.
- Image de texte, contenu généré ou icône de police : quel mécanisme fait perdre le texte.
- Zoom ou adaptation mobile : le geste de l’utilisateur, ou le travail du site.
- Styles d’impression ou impression sans menus : le code, ou l’aperçu.

#### Transition

- Une dernière question résume toute la rubrique.

**Mémo oral :** une distinction, un contrôle.

**Fichier final prévu :** `finals/slide-38-memo.png`

---

### S39 — Dernière question : ma page sert-elle chacun ?

- **Acte :** 6. S’entraîner
- **Type :** conclusion
- **Durée indicative :** 0:40
- **Objectif pédagogique :** conclure sur le principe commun à la rubrique.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : conclusion, écho de l’ouverture.
- Idée principale : la même page, cette fois lisible par chacun.
- Scène : qui, Nora, Théo, Malik, Inès et Odette ; où, dans le jardin de la Maison des Lisières ; objet, chacun son support : téléphone au soleil, tablette, ordinateur et casque, tablette, feuille imprimée ; tension, résolue ; action, chacun lit ; résultat, cinq petites coches vertes.
- Transformation visible : la scène de S01 inversée : Nora lit au soleil sans plisser les yeux.
- Test des trois secondes : « Tout le monde lit la même page, chacun à sa manière. »
- Ajout par rapport à la slide précédente : le sens de tout le parcours.

**Référence de composition principale :** `A-NORA`, PNG validé de l’étalon S01 (écho de composition avec l’ouverture), qui sert aussi d’ancre de personnage.

**Texte visible (projection)**

- `Dernière question : ma page sert-elle chacun ?`
- `La forme sert le fond, pour chacun`

**Illustration :** jardin stylisé devant la façade de la Maison des Lisières. Nora (Bloc personnage) sur le même banc qu’en S01, au soleil, lisant un écran net. Autour, à distance confortable : Théo (bloc Théo) avec sa tablette ; Malik (bloc Malik) à une table, casque sur les oreilles ; Inès (bloc Inès) assise dans l’herbe avec sa tablette ; Odette (bloc Odette) dans un fauteuil de jardin, crayon en main sur une feuille imprimée. Une petite coche verte près de chacun. Le slogan dans un bandeau vert pâle à icône de coche, centré en bas.

**Alternative textuelle à fournir :** Nora, Théo, Malik, Inès et Odette lisent chacun la même page du site : au soleil, sur tablette, au lecteur d’écran ou sur papier.

**Règle → préjudice utilisateur :** une présentation pensée pour un seul contexte exclut tous les autres.

**Garantie recherchée (matière de l’oral)**

Une présentation qui sert le contenu permet à chacun d’y accéder.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : cohérence des cinq personnages avec leurs blocs et leurs ancres.
- Piège certification : aucun.

**Discours oral du présentateur (non projeté)**

#### La même page pour chacun

- Nora lit au soleil, Théo repère les champs obligatoires, Malik entend le nom de chaque bouton.
- Inès suit un texte aligné à gauche, Odette annote une feuille limitée au contenu.
- C’est la même page, dont la présentation sert le contenu au lieu de le retenir.
- Toute la rubrique tient dans une question à poser à chaque maquette et à chaque intégration : cette page sert-elle chacun ?

#### Conclusion

- La forme sert le fond, pour chacun.

**Mémo oral :** ma page sert-elle chacun ?

**Fichier final prévu :** `finals/slide-39-conclusion.png`

---

### S40 — Pour aller plus loin

- **Acte :** 6. S’entraîner
- **Type :** ressources
- **Durée indicative :** 0:30
- **Objectif pédagogique :** orienter vers les sources officielles.
- **Badge :** aucun

**Masque :** `MASQUE LIBRE`

> En haut à gauche, sur deux lignes en petites capitales bleu marine : `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES`. En haut à droite, sur deux lignes : `Opquast` puis `DES SITES MEILLEURS POUR TOUS`. Tout en bas à gauche : `RÈGLES OPQUAST · PRÉSENTATION` ; tout en bas à droite : la pagination `NN / 40`. Sous l’en-tête, le titre bleu marine centré, sur une ou deux lignes. Au centre, la scène illustrée de la fiche ; chaque autre texte de la liste est placé où la fiche l’indique, dans un cartouche, une carte ou un bandeau. Aucun badge, aucune rangée d’encadrés IMPACT, GARANTIE, CONTRÔLE ou LIMITE.

**Fiche PDS**

- Rôle : ressources.
- Idée principale : revenir aux sources officielles pour réviser.
- Scène : qui, Nora ; où, à une table de la bibliothèque ; objet, un ordinateur ouvert sur une liste cochée, un dictionnaire et un livre ; tension, aucune ; action, Nora ouvre le livre et prend des notes ; résultat, trois ressources devant elle.
- Transformation visible : du parcours aux sources.
- Test des trois secondes : « Trois sources pour réviser. »
- Ajout par rapport à la slide précédente : la suite.

**Référence de composition principale :** `N10` (personnage). Ancre de personnage : `A-NORA` si disponible.

**Texte visible (projection)**

- `Pour aller plus loin`
- `Checklist Opquast V5 : checklists.opquast.com`
- `Glossaire : training.opquast.com`
- `Livre : Qualité et conformité des services numériques`

**Illustration :** titre centré. Nora (Bloc personnage) assise à une table de bibliothèque, un livre ouvert, un crayon à la main. Trois cartes pastel au-dessus de la table, chacune avec un pictogramme et sa ligne : liste cochée, dictionnaire ouvert, livre fermé. Aucune couverture reproduite, aucun logo.

**Alternative textuelle à fournir :** trois ressources pour approfondir : la checklist officielle Opquast V5, le glossaire Opquast et le livre Qualité et conformité des services numériques.

**Règle → préjudice utilisateur :** sans source officielle, les révisions reposent sur des résumés.

**Garantie recherchée (matière de l’oral)**

Revenir aux libellés et aux fiches officielles.

**Contrôle et pièges (matière de l’oral et de la revue)**

- Revue : URL complètes dans l’accordéon et les métadonnées, domaines seuls sur l’image.
- Piège certification : aucun.

**Discours oral du présentateur (non projeté)**

#### Trois sources officielles

- La checklist Opquast V5 et ses fiches donnent les libellés, objectifs et contrôles de chaque règle.
- Le glossaire de la thématique Présentation précise le vocabulaire.
- Le livre d’Élie Sloïm et Laurent Denis, quatrième édition, développe chaque règle avec l’avis de l’expert.

#### Conclusion

- Les libellés officiels restent la référence pour réviser.

**Mémo oral :** revenir aux sources.

**Fichier final prévu :** `finals/slide-40-ressources.png`

## Contrôle final de couverture

- **17/17 règles 180 à 196** présentes chacune dans une slide de règle dédiée et bonne réponse d’au moins un exercice corrigé (tableau « Sources et couverture »). Vérification par script sur ce fichier : pour chaque numéro, un badge `R. NNN` sur une slide de type règle, et au moins une occurrence `→ NNN` dans un corrigé ou dans le texte visible de S37.
- **Mesures par script** (`verif-v003.py`, `python3 -I`, somme des chaînes du « Texte visible », hors en-tête, footer, pagination et badge) : plus long texte visible 160 caractères (S29, S35), aucune slide au-delà de 160 ; plus long encadré 56 caractères (S30), aucun au-delà de 60 ; durée cumulée 45 min 45 s ; tirets demi-cadratins ou cadratins dans les textes visibles et les oraux : 0 ; numéros de règles dans les oraux hors corrigés : 0 ; masques identiques au masque canonique : 40 sur 40 ; chaînes entre accents graves des illustrations absentes de la liste blanche : 0.
- **Règles connexes :** 157, 140, 158 (Navigation et Liens), 136 (Liens) visibles en S33 ; 69 (Formulaires) à l’oral en S12 et S33.
- **6 termes** du glossaire officiel Présentation : charte graphique, désactivation des styles, linéarisation, ratio de contraste, zoom graphique, point de rupture.
- **Vérification pédagogique :** 4 checkpoints (S11, S18, S23, S29), 8 questions finales (S34, S35), grand cas S36 et S37, 5 distinctions (S10, S17, S22, S28, S32).
- **Limite :** ce storyboard ne reproduit pas les questions officielles de l’examen et ne peut en garantir le résultat.

## Cinq slides étalons proposées

À générer et montrer à Alex côte à côte avec une slide de Sécurité v4 avant toute série ; S37 est générée la première, puisque S36 en dépend (décision d’Alex, relecture v002, constat I7) :

- Ouverture : S01 (`MASQUE LIBRE`, personnage, scène extérieure, slogan ; devient l’ancre `A-NORA`).
- Règle avec comparaison : S19 (`MASQUE RÈGLE`, situation physique montrée telle quelle).
- Règle avec code : S26 (`MASQUE RÈGLE`, texte justifié montré tel quel, ligne de code).
- Checkpoint : S18 (`MASQUE EXERCICE`, bandeau de question et quatre cartes).
- Grand cas corrigé : S37 (`MASQUE EXERCICE`, scène sans personnage, sept défauts, cartouche `1,8:1` et sept étiquettes ; son PNG validé produit S36).

## Revue avant génération

- 7 novembre 2026 : v001, rédaction par Claude (Opus 5.5) à partir du livre local (rubrique 11), des libellés et de la checklist V5 servis par le MCP Opquast et du glossaire officiel ; références `N01`, `N03`, `N10`, `N17`, `S20` lues en image.
- 7 novembre 2026 : relecture indépendante de la v001 (session Claude Opus 5.5 distincte) : 1 bloquant, 12 importants, 18 mineurs (`sources/revues/relecture-independante-v001-2026-11-07.md`).
- 7 novembre 2026 : v002, constats traités (section « Changements depuis v001 ») ; aucun constat écarté sans raison. Nom du fil rouge : recherches web du 7 novembre 2026 (rédaction et relecture), aucune organisation « Maison des Lisières » trouvée ; présenté comme fictif.
- 8 novembre 2026 : relecture indépendante de la v002 (session Claude Opus 5.5 distincte) : 0 bloquant, 7 importants, 18 mineurs (`sources/revues/relecture-independante-v002-2026-11-08.md`).
- 8 novembre 2026 : v003, rédaction par Claude (Opus 5.5) ; constats traités selon les décisions d’Alex pour I6, I7, M5, M10, M12, M13 et M18 ; détail dans « Journal v003 ».
- 8 novembre 2026 : validation d’Alex de la v003 et des sept décisions ci-dessous (« go codex ») ; statut `VALIDE_POUR_GENERATION`, empreinte enregistrée dans `run.json`.

## Décisions d’Alex, validées le 8 novembre 2026

Toutes les options ci-dessous sont retenues telles que recommandées.

- **Feuillages en bordure** : exception au guide commun, reprise de Sécurité v4.
- **Titre aligné à gauche** avec les masques RÈGLE, COMPARAISON et EXERCICE ; centré avec le `MASQUE LIBRE`.
- **Cinq distinctions** au lieu de quatre (S10, S17, S22, S28, S32) ; option : fusionner S17 dans S13 et ramener la série à 39 slides.
- **Titre de S37 réduit à `Correction`** pour tenir la densité (157 caractères) : accepter, ou rallonger le titre et dépasser la cible.
- **Nora alignée sur le personnage des références** plutôt que d’une apparence propre ; ancres `A-NORA`, `A-SAMUEL`, `A-MALIK` après validation des slides S01, S06 et S13.
- **Deux encadrés au lieu de trois** sur les slides de règle, le contrôle ou la garantie restant à l’oral quand il n’est pas affiché.
- **Évaluations sans légende de choix** : les distracteurs passent dans les corrigés.

## Points de vigilance pour la relecture

- **Seuil de contraste (S09, S10, S34)** : le livre retient 3:1 quelles que soient taille et graisse ; les WCAG 2.0 niveau AA demandent 4,5:1 pour le texte courant. Le visible affiche `Ratio visé : au moins 3:1` et l’oral signale l’écart.
- **Copier-coller et `text-transform` (S27)** : non démontré dans l’image ; comportement des navigateurs `NOT VERIFIED`. La scène s’appuie sur le contrôle du livre.
- **Contenus générés (S15)** : des lecteurs d’écran actuels restituent une partie du contenu `content` ; la scène s’appuie sur la désactivation des styles, contrôle du livre (à vérifier si l’on veut montrer un lecteur d’écran).
- **Coquilles du livre** : `aria-hidden=“true=”` (185) et les exemples `link` et `style` de 195 portent des guillemets altérés ; le storyboard cite les formes corrigées (`aria-hidden="true"`, `media="print"`).
- **Nom de l’outil de contraste** : le livre écrit « Colour Contrast Analyzer » ; nom courant Colour Contrast Analyser (à vérifier).
- **Règle 186** : valeur 44 × 44 px rattachée par le livre aux WCAG, sans niveau précisé (non affirmé).
- **S15, deux chaînes « Complet »** : le ruban porte `Complet` et la ligne de code `content: "Complet";` contient le mot ; ce sont deux chaînes distinctes de la liste blanche. À vérifier sur la candidate : un seul ruban écrit, à gauche, et aucun « Complet » ailleurs.
- **S18 C** : `C. « Complet » par la CSS` ne dit pas que l’alternative manque ; avec la question « Quelle règle est en jeu ? », la réponse 188 reste juste. Item laissé tel quel, sans « seule », pour rester sous 160 caractères (décision d’Alex, constat M5).
- **Grand cas** : composition sans personnage, fenêtre sur les deux tiers gauches et feuille imprimée à droite ; risque génératif sur les sept défauts et sur le faux texte ; l’édition qui retire les repères peut altérer la scène (critères d’acceptation dans « Fabrication du grand cas »). La possibilité d’éditer une image fournie dépend de l’outil exposé : à vérifier avant production.
- **Grand cas, défaut 4** : le ratio `1,8:1` est une mesure fictive montrée dans la scène, sous le seuil de 3:1 retenu par le livre ; pipette et cartouche doivent survivre à l’édition qui produit S36.
- **S30, impact** : l’encadré s’en tient au livre (« forme appropriée au support ») ; la scène montre une feuille chargée d’aplats et de boutons, sans troncature inventée.
- **Durée** : 45 min 45 s cumulées après le passage de S36 à 4:00 et de S34 à 2:00, compensés par S05 et S06 à 1:00 ; le glossaire de S05 tient en une minute si chaque définition reste à une phrase.
- **Checkpoint 2** : quatre items au lieu de cinq ; la règle 184 n’y figure plus, elle reste corrigée en S34 Q3 et S37.
- **Règles connexes** : rapprochements tirés de passages du livre, qui ne cite pas les numéros ; présentés comme pédagogiques.
- **Source MCP** : libellés obtenus en `source: api` à la rédaction et en `source: local` (instantané du 3 septembre 2026) à la relecture ; concordants.
- **Représentation** : Malik, Théo, Inès et Odette sont décrits sans attribut caricatural ; à contrôler sur chaque PNG avec le critère de rejet commun.
- **Références** : chaque génération reçoit `N01`, `N03`, `N10`, `N17` et l’étalon le plus proche ; à vérifier que l’outil exposé accepte cinq ou six images par appel (`NOT VERIFIED`).
- **Slides de structure** (S02, S05, S38, S40) : les plus proches du défaut « pictogrammes » de la série précédente ; à surveiller sur les planches QA.
- **Oral** : mis en titres et puces selon les gabarits de `REVISION-NOTES-ORALES-OPQUAST.md` ; le contrôle automatique `check_notes_orales_opquast.py` ne pourra porter que sur `slides.json`, pas encore créé (`NOT VERIFIED`).

## Sources principales

- **Référentiel officiel Opquast V5 (245 règles)** : https://checklists.opquast.com/fr/qualite-numerique/ ; fiche de chaque règle : `https://checklists.opquast.com/fr/qualite-numerique/<numéro>`.
- **Glossaire Opquast, thématique Présentation** : https://training.opquast.com/digital-quality/glossaire/glossaire-presentation/ (extrait du 7 novembre 2026, `sources/opquast/glossaire-presentation-2026-11-07.md`).
- **Livre :** Élie Sloïm et Laurent Denis, *Qualité et conformité des services numériques*, 4e édition (2026), partie 3, rubrique 11 « Présentation ».
- **Contrat des notes orales :** `/Users/alex/Claude/projets-heberges/slides-miweb/docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`.
- **Attribution et licence :** règles et objectifs officiels du référentiel sous licence Creative Commons BY-SA selon Opquast. Les oraux, synthèses, scènes et exercices sont des créations pédagogiques nouvelles.

## Journal v003

Relecture traitée : `sources/revues/relecture-independante-v002-2026-11-08.md` (0 bloquant, 7 importants, 18 mineurs). Tous les constats sont traités ; M5 l’est par décision de laisser l’item tel quel.

### Importants

- **I1** : S15. `Complet` ajouté à la liste blanche et écrit sur le ruban de l’écran gauche, ruban bleu marine au lieu d’orange ; encadré `IMPACT - Sans styles, l’atelier paraît ouvert` ; revue et point de vigilance mis à jour. S18 C et S28 : ruban bleu marine, sans texte.
- **I2** : S16. Encadré `IMPACT - Le lien n’annonce pas sa fonction` ; la phrase du livre sur le caractère restitué reste à l’oral.
- **I3** : S25. `Reliure` (à empattements, fenêtre gauche) et `Photo` (sans empattements, fenêtre droite) ajoutés à la liste blanche et à l’illustration ; `CONTRÔLE - Famille générique en dernier` ; critère de rejet ajouté en revue.
- **I4** : S24 (scène, idée principale, illustration, alternative), S28 (scène et panneau 1), S29 (mini-scène A). « Affiche » remplacée par le tableau des dates du trimestre publié en image ; `A. Programme en image JPG` conservé pour tenir 160 caractères.
- **I5** : S34. `1. « Complet » à 2:1`, `3. Seul repère : « à droite »`, `4. Plan en aplats colorés seuls` ; corrigés Q1 et Q3, oral et piège ajustés.
- **I6** : S36 et S37. Pipette et cartouche `1,8:1` près des horaires, dans les deux listes blanches ; S37 `Ratio → 182` et `Impression → 196` ; oral S37 « le ratio mesuré, 1,8 pour 1, est sous le seuil » ; « Fabrication du grand cas » et points de vigilance mis à jour.
- **I7** : S36, S37, « Exceptions au guide », « Contrat de fabrication », « Fabrication du grand cas », étalons. Nora retirée ; fenêtre sur les deux tiers gauches, feuille imprimée en grand et inclinée à droite avec sa barre de menu, colonne vide réservée aux étiquettes ; S37 devient le cinquième étalon, généré en premier.

### Mineurs

- **M1** : S08. `IMPACT - Sans distinguer le rouge, je rate le champ`.
- **M2** : S08. Médaillon en niveaux de gris retiré de l’illustration et de l’alternative ; le contrôle sans couleurs reste à l’oral.
- **M3** : S14. `IMPACT - J’ignore à quoi sert ce bouton` et `GARANTIE - Caché à l’écran, le nom reste annoncé` ; « nom » retenu dans l’idée principale, comme en S18 B.
- **M4** : S14, oral. Les propriétés qui retirent un contenu « sont admises » pour ce qui s’affichera sur action.
- **M5** : S18 C laissé tel quel (décision d’Alex) ; justification dans les points de vigilance.
- **M6** : S24, piège. Phrase sur la rubrique Images et médias supprimée, remplacée par le rappel que le tableau des dates est un contenu éditorial.
- **M7** : S26, oral. « Selon le livre, plusieurs études ont montré ».
- **M8** : S30. `IMPACT - Imprimée telle quelle, la page sort mal adaptée` ; troncature retirée de la scène, de l’illustration, de l’alternative et de l’oral.
- **M9** : S27. Transformation visible : « sans styles, un titre reste en capitales, l’autre non ».
- **M10** : S09. Scène, illustration et alternative déplacées à un arrêt de bus en plein soleil ; le banc reste pour S01 et S39.
- **M11** : S03, oral. Titre « Cinq gestes de lecture, puis l’entraînement » et puce sur l’entraînement ; mémo oral ajusté.
- **M12** : transitions de sens dans les oraux de S01, S02, S03, S04, S06, S09, S10, S11, S17, S18, S22, S23, S28, S29, S32, S33, S34, S36 et S37 ; S02 perd la puce sur les exercices de la formation, S03 celle sur le découpage, S36 celle sur la feuille « qui fait partie du cas » ; S37 « Ce que l’observation ne permet pas de juger ». Recherche par script de « acte », « slide », « formation », « voyons », « vérifions », « place à », « retenons », « séance », « module », « support », « nous allons », « exercice », « séparons » dans les oraux hors corrigés : 0 occurrence.
- **M13** : S36 à 4:00, S34 à 2:00 pour son animation d’environ deux minutes ; compensation S05 et S06 à 1:00. Total 45 min 45 s, en tête du document et dans « Contrôle final de couverture ».
- **M14** : S36 et S37. Pastille verte sur une autre carte pour lire un code couleur ; second bouton de taille normale, sans libellé, pour l’échelle ; bouton d’inscription minuscule à droite de l’encadré d’aide.
- **M15** : « Fabrication du grand cas ». Critère de rejet du repli « aucune pastille numérotée, aucun trait, aucune étiquette » ; repli inverse ajouté (S36 nue, puis S37 à partir de S36).
- **M16** : Bloc personnage. Chevelure décrite comme sur `N10` et `S20` : cheveux bleu nuit très foncé, mi-longs, aux épaules.
- **M17** : « Contrat de fabrication ». Liste blanche fournie à ImageGen dans l’ordre : en-tête, badge résolu, « Texte visible », footer, pagination résolue.
- **M18** : « Contrat de fabrication » et les 40 fiches. Chaque génération reçoit `N01`, `N03`, `N10`, `N17` et l’étalon le plus proche (`S20` avant validation des étalons) ; chaque fiche désigne une seule « référence de composition principale », plus l’ancre de personnage quand elle existe ; S36 garde le PNG de S37 comme image à éditer.

### Autres mises à jour

- En-tête, « Identité » et « Revue avant génération » : version v003, 8 novembre 2026, statut `BROUILLON`.
- Tableau de couverture : inchangé, aucun corrigé n’ayant changé de règle.
- « Décisions à soumettre à Alex » : retrait de l’ordre de fabrication du grand cas, désormais tranché ; densité de S37 ramenée à 157 caractères.
- S03 et S33 : les noms de références de l’illustration ne sont plus écrits entre accents graves, pour ne pas ressembler à une chaîne de la liste blanche.
