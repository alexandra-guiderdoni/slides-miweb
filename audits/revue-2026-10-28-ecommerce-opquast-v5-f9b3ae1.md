# Revue contradictoire du jeu « E-commerce selon Opquast V5 »

Date : 28 octobre 2026, 23 h 05 à 23 h 50 CET. Dépôt : `/Users/alex/Claude/projets-heberges/slides-miweb`. Jeu : `ecommerce-opquast-v5/`. Version revue : commit `f9b3ae14297ef51cde4cdfc81b95dd191097ffa5` (HEAD = origin/main = commit déployé par GitHub Pages, build 1322678911 terminé le 28 octobre 2026 à 22 h 02 UTC). Parent : `6cbdcd6a57309448d8f2294f38608fca105f31f7`. Une seule version a été observée : le local, l'origine et le site public sont identiques (147 empreintes SHA-256 comparées, 147 identiques).

Dossier de preuves : `/Users/alex/Claude-worktrees/revue-ecommerce-opquast-v5-20261028/preuves/`. Worktree détaché utilisé pour les opérations qui écrivent : `/Users/alex/Claude-worktrees/revue-ecommerce-opquast-v5-20261028/worktree` (f9b3ae1). Le dépôt principal n'a reçu aucune modification ; la note non suivie `cuisine-moi/2026-10-28-serie-opquast-ecommerce.md` est intacte.

## 1. Verdict

**Défauts bloquants constatés**, au sens du contrat du dépôt (contrôle des images caractère par caractère, rejet de tout écart de texte) : quatre images publiées portent une faute dans l'habillage fixe, « EXPÉRIIENCES DURABLES » avec un I doublé (slides 028, 049, 117, 125), validées « VALIDEE_PRODUCTION » par les revues d'image du dossier `source/reviews/`.

Ce verdict est borné :

- La publication est techniquement correcte : HEAD, origine et site servi sont la même version, les deux archives ZIP sont conformes, le générateur est reproductible, les tests du dépôt et les validateurs HTML sont verts, le lecteur fonctionne au clavier, au retour navigateur et en plein écran.
- Le contenu métier est exact : les 39 libellés cités correspondent mot pour mot au snapshot Opquast du 3 septembre 2026, les 39 règles sont couvertes, les 25 bonnes réponses des QCM et les cinq verdicts T0/T1 sont justes. Un libellé (règle 38) a changé dans l'API publique Opquast depuis le snapshot.
- Le jeu est donc **utilisable en formation avec réserves** si le propriétaire assume temporairement la faute d'habillage sur quatre slides, et à condition de traiter les réserves de gravité majeure ci-dessous avant une diffusion large : surface participant sans le texte des questions, alternatives courtes qui résument la leçon au lieu de remplacer l'image, verdicts du diagnostic T0 lisibles sur le site public, notes orales sans transition et répétitives sur les slides de question, liens d'évitement qui ramènent le diaporama à la slide 1 au clavier.

Décompte global : 4 constats bloquants, 12 constats majeurs (dont 5 transversaux, M12 commun aux 30 variantes du site), environ 60 constats mineurs regroupés en 12 familles. Le détail par slide est dans `images/matrice-132-slides.md` (132 lignes) et dans les revues spécialisées.

## 2. Constats classés par gravité

Chaque constat indique l'impact utilisateur, la localisation, la reproduction, l'attendu et l'observé, et la preuve.

### 2.1 Bloquants

#### B1 - Faute d'orthographe dans l'habillage fixe de quatre images : slides 028, 049, 117, 125

- Impact : texte fautif projeté et publié dans quatre images ; contradiction directe avec la règle du dépôt (« contrôler chaque image en résolution originale, caractère par caractère, et rejeter tout texte parasite ») et avec les revues d'image qui les ont validées.
- Fichiers : `ecommerce-opquast-v5/assets/slides/slide-028.png`, `slide-049.png`, `slide-117.png`, `slide-125.png` ; revues `source/reviews/slide-028.json`, `slide-049.json`, `slide-117.json`, `slide-125.json` (décision `VALIDEE_PRODUCTION`).
- Reproduction : ouvrir l'image en résolution originale, agrandir l'en-tête supérieur gauche (zone 30-520 x 10-85 px).
- Attendu : « EXPÉRIENCES DURABLES » (liste blanche du storyboard et de `slides.json`). Observé : « EXPÉRIIENCES DURABLES ».
- Preuves : découpes agrandies x4 `images/resultats/preuve-slide-117-entete.png` et `preuve-slide-125-entete.png` (lot 111-132), zooms x3 du lot 023-044 (`images/resultats/zooms-lot-023-044/`), découpes du lot 045-066 (`images/resultats/crops-lot-045-066/`), et contrôle indépendant du relecteur principal sur les 132 slides par planches des quatre zones d'habillage, `images/habillage/habillage-*.png` (12 planches, 132 x 4 zones relues : seules ces quatre slides portent la faute ; pagination « NNN / 132 » exacte sur 132 ; pied « RÈGLES OPQUAST · E-COMMERCE » exact sur 132 ; en-tête droit exact sur 132).
- Remarque : la faute est petite en projection (texte d'en-tête) ; elle est nette en résolution originale et dans le ZIP téléchargé. Les 128 autres images ont un habillage exact.

### 2.2 Majeurs

#### M1 - La surface participant du lecteur ne donne pas le texte des questions ni des propositions

- Impact : un participant qui ne voit pas l'image (lecteur d'écran, image non chargée, consultation sans visuel) n'obtient dans la page du diaporama ni l'énoncé ni les propositions A, B, C des 25 questions QCM, ni les cinq affirmations T0/T1. Il doit aller dans `alternatives.html` ou `alternatives.md`, où la transcription (textes visibles) est publiée.
- Localisation : `slides.json`, champs `alt` et `description` des slides 082 à 130 (questions) et 006 à 010, 071 à 075 ; `build.py` `render_slide` (ligne 1258) qui n'expose dans le lecteur que `alt`, `description` et `notes_orateur`.
- Mesure : sur les 655 textes visibles de corps (hors habillage, pagination, titre), 436 sont absents de la description détaillée ; pour les 25 questions QCM, 125 sur 125 sont absents ; pour les corrections QCM, 145 sur 151. Exemple slide 090 : alt « Question 5 sur 25 avec une situation et trois propositions, sans corrigé. », description « L'énoncé sur une marque française et un vendeur situé à Lyon précède trois propositions de même style bleu sur la provenance du produit. Aucun verdict n'est affiché. », alors que l'image contient l'énoncé complet et trois propositions de deux lignes.
- Attendu : une information équivalente à l'image dans la surface où l'image est consultée (règle Opquast 118 et principe du dépôt « ne pas publier d'image sans alternative »). Observé : l'équivalent n'existe que dans la page d'alternatives, par conception (deux accordéons seulement).
- Preuve : script de couverture exécuté sur `slides.json` (sortie dans ce rapport, section 4.3) ; 14 alternatives marquées `a_confirmer` par les lots d'images pour cette raison (007, 008, 090 à 110 impairs, 132).
- Reproduction : ouvrir `https://alexandra-guiderdoni.github.io/slides-miweb/ecommerce-opquast-v5/#slide-090`, ouvrir les deux accordéons : aucune proposition A, B, C n'est lisible en texte.

#### M2 - Alternatives courtes qui résument le message au lieu de remplacer l'image (71 slides)

- Impact : l'attribut `alt` lu par les lecteurs d'écran annonce la leçon (par exemple le champ `message` copié mot pour mot sur 011, 019, 026, 046 à 062) au lieu de ce que montre l'image ; sur les slides question, l'alt générique ne restitue pas l'énoncé.
- Localisation : `slides.json`, champ `alt` ; verdicts par slide dans `images/resultats/slide-NNN.json` (71 `corriger`, 47 `garder`, 14 `a_confirmer`), chacun avec une proposition de 80 caractères au plus.
- Attendu (skill alt-text du workspace et AGENTS.md) : l'alt remplace l'information utile de l'image, sans transformer l'alt en résumé de slide ou commentaire pédagogique, et reprend les textes visibles quand ils portent l'information. Observé : alt = message ou titre adjacent sur la majorité des slides de contenu ; aucun alt inventé ni inexact sauf 070.
- Nuance : si le propriétaire décide qu'un alt de slide de formation porte la leçon, ces 71 verdicts redescendent en mineur ; la décision est de lot, pas slide par slide. Le skill `alt-text` n'était pas disponible dans la session des agents ; ses critères (SKILL.md lu par le relecteur principal) ont été transmis dans la consigne d'inspection.

#### M3 - Libellé de la règle 38 cité entre guillemets et devenu obsolète (slides 047, 056, 125)

- Impact : la slide 047 cite « La modification de la quantité de chaque article, l'ajout et la suppression d'un ou plusieurs articles restent possibles avant la validation définitive de la commande. » ; l'API publique Opquast du 28 octobre 2026 donne « La modification de la quantité, l'ajout et la suppression d'un ou plusieurs articles restent possibles avant la finalisation de la commande. » Le moment (« finalisation ») et l'objet (« de chaque article ») diffèrent ; les notes de 047 et 056 reprennent les deux éléments disparus.
- Preuve : `opquast/libelles-live-vs-snapshot.md` (39 libellés comparés, 3 divergents : 38 substantiel, 63 et 66 « mail » devenu « e-mail »), `opquast/checklist-publique-api-live.json` (HTTP 200, 245 règles), `opquast/revue-regles-30-68.md` M1.
- Observation : le storyboard déclare son snapshot (« fiches MCP consultées le 28 octobre 2026, à partir du snapshot local du 3 septembre 2026. Aucun contrôle de l'API en direct n'est revendiqué ») et la note de cadrage signalait « R38 à reprendre exactement pour la série complète ». La citation reste présentée comme le texte de la règle, sans date.

#### M4 - Notes orales : aucune transition sur 131 slides, et contradiction interne du harnais

- Impact : le contrat (`AGENTS.md`, « transition courte entre les slides, conclusion sur la dernière » ; gabarit `### Transition` de `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`) n'est pas respecté : 0 section de transition sur 132 slides. Cause probable : `scripts/check_notes_orales_opquast.py` liste `"transition"` dans `FORBIDDEN_HEADINGS` (ligne 36), donc le validateur vert interdit ce que le contrat exige.
- Preuve : comptage mécanique (0 titre « Transition »), `editorial/revue-notes-orales.md` M1, lecture du script.
- Recommandation : trancher dans le harnais avant toute correction des notes.

#### M5 - Notes orales répétitives et métapédagogiques sur les slides de question et de bilan

- Impact : les 25 slides question QCM portent la même note (« Choisissez une seule proposition parmi A, B et C... »), paraphrase du message et du bandeau ; les dix slides T0/T1 décrivent le protocole (« Les mêmes énoncés permettront de comparer votre compréhension à deux moments. ») ; les slides 080 et 081 commentent la méthode d'évaluation et la gestion du groupe (« Chaque score va de zéro à cinq et la progression se calcule par T1 moins T0 », « Les résultats peuvent être rapprochés collectivement sans afficher de résultats nominatifs »), ce que le contrat interdit et que les expressions régulières du script ne détectent pas.
- Preuve : `editorial/revue-notes-orales.md` M2 à M5, avec citations exactes ; 9 majeurs et 20 mineurs au total, 0 bloquant ; tableau de couverture des 132 slides.
- Autres majeurs de la même revue : section de R65 égarée dans la slide 014 (R64), slide 034 qui récite huit numéros, redites en chaîne (contrôle de R65 donné cinq fois ; slides 062 et 063 quasi identiques).

#### M6 - Les verdicts du diagnostic T0 sont lisibles en clair sur le site public

- Impact : la mesure « Progression = T1 - T0 » n'est interprétable que si l'URL n'est pas diffusée avant la passation. Les cinq verdicts figurent dans l'attribut `alt` des corrections 076 à 080 (`index.html` ligne 2696 : « Faux : un lien vers les conditions depuis chaque page peut convenir. »), dans les textes visibles des images, et sont enseignés dans le discours oral public des slides de contenu. La commande « Ouvrir les accordéons » en mode toutes les slides ouvre description et discours de toutes les slides en un clic (mesuré : 264 panneaux).
- Preuve : `editorial/revue-questions-corrections.md` Majeur 1, cartographie complète des paires (différé respecté : aucune correction entre 006 et 075, énoncés T0, T1 et corrections identiques caractère pour caractère).
- Nuance : les surfaces participant des slides question (image, alt, description, message) ne révèlent rien (75 slides contrôlées, 0 révélation) ; le risque vient de la publication intégrale du support sur une seule page.

#### M7 - QCM : indices de rédaction et distracteurs non fonctionnels

- Impact : 25 distracteurs sur 50 portent un marqueur absolu (nécessairement, toujours, exclusivement, jamais) contre 1 bonne réponse sur 25 ; 10 bonnes réponses sur 25 portent un modal (« peut être satisfaite ») ; séquence des bonnes réponses BCABCBACBACABCABCABCABCAB sans répétition consécutive et cycle A-B-C strict de Q12 à Q25 ; cinq distracteurs ne sont pas défendables (Q4 C « R41 remplace R40 », Q5 B « Lyon n'est pas une zone de livraison », Q9 C, Q15 C, Q19 C). Les 25 bonnes réponses sont exactes.
- Preuve : `editorial/revue-questions-corrections.md` Majeurs 2 et 3, mesures par script sur `slides.json`.

#### M8 - Slide 017 : la carte R65 illustre ce que la règle juge insuffisant

- Impact : sous « R65 : produits indisponibles repérables sans confusion », le produit indisponible n'est distingué que par un grisé, sans mention textuelle (le mot « Épuisé » a été retiré par la correction ciblée `source/prompts/slide-017-correction.txt` sans remplacement). Un apprenant peut en déduire qu'un grisé suffit, alors que la règle exige une différenciation visuelle et textuelle.
- Preuve : image lue par le relecteur principal ; `images/resultats/slide-017.json` ; `images/resultats/synthese-lot-001-022.md`. Gravité à arbitrer entre bloquant et mineur selon la lecture de la carte.

#### M9 - Slide 070 : alternative inexacte et enveloppe à coche apparente

- Impact : l'alt « R39 et R33 sont observables ; R63 reste à vérifier par un test d'envoi. » reprend les notes orateur et non la correspondance affichée A · R39, B · R33, C · R63 ; dans la loupe de la carte C, l'enveloppe porte un tracé blanc qui se lit comme une coche, contradictoire avec « envoi non vérifié » (analyse pixel du lot 067-088, lecture plausible, non certaine).
- Preuve : `images/resultats/slide-070.json`, `images/resultats/synthese-lot-067-088.md`.

#### M10 - Accordéons inaccessibles sans JavaScript, contrairement à ce que laisse entendre le README du jeu

- Impact : le README du jeu affirme « la page principale reste lisible sans JavaScript ». Les 132 sections, images, alternatives et titres sont bien dans le HTML statique (aucun attribut `hidden` au chargement, 0 `noscript`), mais les panneaux `fr-collapse` de description et de discours sont masqués par la CSS DSFR (mesuré au chargement : `visibility: hidden`, `max-height: 0px`) et ne s'ouvrent que par script. Sans JavaScript, description et discours sont donc invisibles dans le lecteur ; ils restent disponibles dans `alternatives.html`.
- Preuve : `navigateur/parcours-agent-browser.log` section A (état initial), analyse statique de `index.html`. Limite : aucun navigateur sans JavaScript n'a été piloté ; la conclusion repose sur l'état mesuré avant toute exécution de l'ouverture et sur la CSS DSFR.

#### M11 - Revues d'image du dossier `source/reviews/` non fiables comme preuve

- Impact : les 132 revues concluent `VALIDEE_PRODUCTION` avec la mention « inspection visuelle » ; quatre fautes d'habillage, une carte R65 contradictoire, une coche apparente et un bandeau vide (099) leur ont échappé. Le dépôt exige que « aucun agent ne valide seul sa propre production » ; le champ `reviewer` indique « assistant principal, inspection visuelle après affichage de la candidate » pour les 132.
- Preuve : comparaison des 132 JSON de revue avec les 132 fiches d'inspection de cette revue (`images/matrice-132-slides.md`).

#### M12 - Un lien d'évitement activé au clavier ramène le diaporama à la slide 1 (défaut du lecteur, commun aux 30 variantes)

- Impact : un utilisateur clavier ou lecteur d'écran qui, sur la slide 60, active « Accéder au sommaire », « Accéder au pied de page » ou « Accéder aux descriptions détaillées » perd sa position : le diaporama revient à la slide 1 et l'URL est réécrite en `#slide-01`. Le lien d'évitement défile bien vers sa cible, mais le lecteur a changé de slide en même temps.
- Localisation : `ecommerce-opquast-v5/build.py` ligne 750 (gestionnaire `popstate` : `currentIndex = getIndexFromHash()` puis `showSlide(currentIndex, { replace: true })`) ; code identique dans `matrice-slide-ai/build.py` ligne 738 et dans les 31 autres `build.py` du dépôt (32 fichiers contiennent ce gestionnaire) : le défaut touche toutes les variantes publiées.
- Reproduction (site public) : ouvrir `https://alexandra-guiderdoni.github.io/slides-miweb/ecommerce-opquast-v5/#slide-60`, donner le focus au lien « Accéder au sommaire » (Tab depuis le haut de page ou focus programmé), appuyer sur Entrée. Attendu : défilement vers le sommaire, slide 60 conservée. Observé : hash `#slide-01`, statut « Slide 1 sur 132 », seule la section `slide-01` visible (mesuré). Même résultat trouvé par l'agent sg-code-audit depuis `#slide-50` vers `#footer` et depuis `#slide-40` vers `#description-active` en Chromium headless. Un clic souris par sélecteur CSS sur le lien masqué n'a pas déclenché la navigation (lien visible seulement au focus), ce qui explique que le défaut ne se voie pas à la souris.
- Preuve : `navigateur/contre-epreuve-liens-evitement.log`, capture `navigateur/K-apres-lien-evitement-sommaire-depuis-slide-60.png` (sommaire affiché, statut « Slide 1 sur 132 »), `shipguard/code-audit/runs/.../zone-z01-r1-r1-z01-a1.json` r1-z01-001.
- Les tests du jeu n'exercent que le texte du script (`assertIn('window.addEventListener("popstate"', ...)`), pas son comportement : le validateur vert ne couvre pas ce cas.

### 2.3 Mineurs (familles)

- m1 Habillage hétérogène d'une slide à l'autre : couleur (bleu roi ou bleu marine), graisse, filets supplémentaires sous l'en-tête (038, 044, 053), filet collé au bord (032, 036), statut « Exercice original non officiel » rendu de trois façons (091, 093, 095, 097). Preuve : planches `images/habillage/`, fiches par slide.
- m2 Slide 099 : bandeau bleu pâle entièrement vide en bas de slide ; slide 130 : point gris parasite devant « Opquast » (`images/resultats/preuve-slide-130-entete-droit.png`).
- m3 Slides 043 (cartes de trois couleurs sur une question, prompt imposant des cartes identiques), 081 (maquette à quatre options radio alors que les QCM ont trois choix), 088 (proposition B seule sur deux lignes), 096 (proposition C collée au bord).
- m4 Métadonnées `regles` incohérentes : 083 déclare 56 et 68 sans trace dans l'image ni les notes ; 123 déclare 66 ; 125 déclare 38 ; 059 cite R30 dans les notes sans le déclarer ; les 25 slides question ne déclarent aucune règle alors que leurs textes citent R39, R40, etc. (`opquast/revue-regles-30-68.md`, section 3.3).
- m5 Libellés 63 et 66 cités avec « mail » alors que l'API publique dit « e-mail » (slides 058, 060) ; dix règles ont reçu des objectifs supplémentaires dans l'API publique sans contredire les slides.
- m6 Inférences non nommées comme telles dans les notes : gratuité (048, 049), articulation 30 et 62 attribuée aux règles (054), « impose » pour R62 (131), « pertinentes » ajouté à R39 (083), R43 rapprochée de la joignabilité du SAV qui relève de la règle 112 (105), contrôle de R38 étendu à l'ajout et la suppression (047).
- m7 Règles 31 et 54 sans aucun exercice ; rappel C (055) « Assurance ajoutée sans choix » défendable en R32 comme en R33 alors que la slide 050 présente cette distinction comme un piège ; Q16 situe le manque dans « le panier » alors que R41 vise le récapitulatif ; Q14 ne mentionne que le mode de dépôt alors que R53 exige aussi la procédure de traitement.
- m8 Page `accessibilite.html` : « Date : Juin 2026 » pour un jeu publié le 28 octobre 2026 (valeur codée en dur dans `build.py` ligne 1495, commune à toutes les variantes) ; badge « Accessibilité : non auditée », cohérent avec cette revue.
- m9 Avertissements DSFR en console sur chaque page : « Modal #modal-menu - missing accessible name », « missing required title, fallback to primary button », « add reference to primary for accessible name (aria-labelledby) » (gabarit d'en-tête de `build.py`, commun au site). Aucune erreur console, aucune requête en échec, aucune violation CSP (`navigateur/parcours-agent-browser.log` section H).
- m10 Lien d'accueil « Présentation plein écran » (`?projection=1#slide-01`) : à l'arrivée, le plein écran ne s'active pas (restriction navigateur : geste utilisateur requis), la page défile jusqu'au diaporama et le focus est posé sur le bouton « Activer le plein écran » (mesuré, section G). Le libellé promet plus que ce qui se produit.
- m11 Deux parties de même libellé dans `download_parts` fusionneraient en un seul lien sur l'accueil (dictionnaire indexé par libellé) ; `write_zip` ne vérifie ni l'union ni l'intersection des parties, la couverture 1-132 n'est garantie que par le test du jeu aux bornes codées en dur. Données actuelles correctes. (`shipguard/logic-audit/logic-report.md`, `shipguard/process-check/footer-avant-apres.log`.)
- m12 Un hash invalide (`#slide-133`, `#slide-00`, `#Slide-01`) renvoie silencieusement à la slide 1 et réécrit l'URL ; comportement volontaire et testé.
- m13 Apostrophes droites sur certaines images (008, 009, 074), conformes à leur liste blanche mais incohérentes avec les autres slides ; slide 022 montre un t-shirt pour un bien numérique ; 016 affiche « Pointure 42 : disponible » en double (prévu par la composition).

## 3. Matrice de couverture

### 3.1 Les 132 slides

Chaque image a été lue individuellement en résolution originale par un agent d'inspection (six lots de 22, modèle Fable, effort maximal, une image par appel), confrontée à son dossier (liste blanche, alt, description, message, composition, notes, prompt, revue existante), avec un fichier JSON par slide. Le relecteur principal a relu indépendamment les quatre zones d'habillage des 132 slides (planches agrandies) et les images 017, 117 et 125 en original.

| Contrôle | Résultat sur 132 |
|---|---|
| Image lue en résolution originale | 132 |
| Pagination « NNN / 132 » exacte | 132 |
| Numéros de règles visibles conformes au champ `regles` | 132 |
| Habillage fixe exact (en-tête gauche et droit, pied gauche) | 128 (défaut : 028, 049, 117, 125) |
| Lisibilité en projection | 132 |
| Textes de la liste blanche manquants | 0 slide |
| Textes parasites lisibles | 4 slides à vérifier (057, 070, 080, 130 : pictogrammes ou point, pas de mot) |
| Description détaillée cohérente avec l'image | 129 (écarts : 026, 029, 046) |
| Alternative courte : garder / corriger / à confirmer | 47 / 71 / 14 |
| Révélation de la réponse sur les 75 slides question ou correction (image, alt, description, message) | 0 |
| Gravité : RAS / mineur / majeur / bloquant | 27 / 85 / 16 / 4 |
| Confiance de l'inspecteur : haute / moyenne | 128 / 4 |

Tableau complet, une ligne par slide : `images/matrice-132-slides.md` ; données : `images/matrice-132-slides.json` ; fiches : `images/resultats/slide-NNN.json` ; synthèses : `images/resultats/synthese-lot-*.md`.

### 3.2 Les parcours

| Parcours | Méthode | Résultat | Preuve |
|---|---|---|---|
| Accueil vers le jeu (tuile) | ShipGuard manifeste 01 (local) et agent-browser (public) | PASS ; 30 tuiles, dernière « E-commerce selon Opquast V5 », favicon pointé sur le jeu | `shipguard/visual-run/visual-results.json`, `navigateur/public-telechargements-agent-browser.log` |
| Première et dernière slides, précédente, suivante, sommaire, Début, Fin | manifeste 02 (local), agent-browser | PASS ; `#slide-01`, `#slide-02`, `#slide-82`, `#slide-132`, retour `#slide-01` | captures `ecommerce-02-*.png` |
| Question puis correction (082 puis 083) | manifeste 02, captures relues | PASS ; « Slide 82 sur 132 », « Question 1 / 25 : correction », « Bonne réponse : B » | `ecommerce-02-slide-82-question.png`, `ecommerce-02-slide-83-correction.png` |
| Ouverture et fermeture des deux accordéons | manifeste 03 puis mesure directe | FAIL du manifeste = faux positif (assertion avant mise à jour du libellé ; la capture d'échec montre « Fermer les accordéons ») ; mesure directe : commande groupée ouvre et ferme les deux panneaux, libellé et `aria-expanded` synchronisés, persistance sur la slide suivante, ouverture individuelle au clavier (Entrée) | `03-accordeons-135334713a03.png`, `navigateur/complement-agent-browser.log` |
| Mode toutes les slides par le bouton | manifeste 04 | PASS ; « Toutes les slides affichées (132) », retour au diaporama | `ecommerce-04-toutes-bouton.png` |
| Accès direct `?slides=all` puis retour et avance navigateur | manifeste 04 (actions back et forward natives) | PASS ; après retour l'URL `?slides=all#diaporama` et le mode toutes les slides sont restaurés ; après avance, `#slide-50` | `ecommerce-04-toutes-apres-retour.png`, `ecommerce-04-slide-50-apres-avance.png` |
| Commande groupée en mode toutes les slides | agent-browser | 132 commandes ouvertes, 264 panneaux ouverts, contexte « de toutes les slides » | `complement-agent-browser.log` |
| Entrée et sortie du plein écran | manifeste 06 et mesure directe (Chromium headless) | `document.fullscreenElement` = `diaporama`, bouton « Mode projection actif », focus sur « Quitter le plein écran » ; sortie : focus de retour sur « Activer le plein écran » | `F-plein-ecran-actif.png`, `ecommerce-06-apres-clic-plein-ecran.png` |
| Alternatives HTML, retour vers une slide, page accessibilité, export Markdown | manifeste 05 (local) et agent-browser (public) | PASS ; lien « Voir la slide 47 » mène à `#slide-47` ; Markdown servi en `text/markdown` | `ecommerce-05-*.png`, `public-telechargements-agent-browser.log` |
| Deux téléchargements depuis les surfaces qui les proposent | HEAD depuis la page du jeu (fetch same-origin), curl HEAD, liens de l'accueil et du pied de page | 200, `application/x-zip-compressed`, 60 745 516 et 67 141 865 octets ; 6 liens dans la page du jeu, 2 dans le pied de l'accueil ; fichiers publics identiques aux locaux | `public/head-telechargements.log`, `empreintes/comparaison-public-local.json` |
| Clavier : ordre de tabulation, focus visible, flèches | agent-browser | Tab depuis l'ancre : commande groupée, deux accordéons, pied de page, puis liens d'évitement ; contour visible 2 px sur tous ; flèche droite : slide suivante, focus sur le titre, statut « Slide 12 sur 132 » | `parcours-agent-browser.log` sections B, B2, C ; `B-apres-fleche-droite-focus-titre.png` |
| Annonce du changement de slide | DOM | `aria-live="polite"` sur le statut, statut de projection avec le titre | section C |
| Zoom et petit écran | agent-browser, viewport 320 x 568 et 640 x 480 | aucun débordement horizontal (scrollWidth = innerWidth), image et contrôles à 288 px de large | `E-320px-slide-11.png`, `E-640px-slide-11.png` |
| Contraste | mesure des couleurs calculées | liens du pied de page 11,37:1, bouton du fil d'Ariane 5,74:1, liens du sommaire 15,6:1, liens d'alternatives 14,91:1 | `complement-agent-browser.log` section D |
| Erreurs console, réseau, CSP (site public) | agent-browser et chrome-devtools | 0 erreur, 0 requête en échec, 0 violation CSP ; 3 avertissements DSFR (modal menu) ; avis Chrome « Lazy-loaded images should have explicit dimensions » (les images ont width et height) | section H, console chrome-devtools |
| Sans JavaScript | analyse statique et CSS mesurée | sections, images, alt et titres présents ; panneaux d'accordéon masqués par la CSS DSFR (voir M10) | section A |
| Audit automatique accesslint (4 pages publiques) | accesslint audit_live | 5 à 7 « color-contrast 1:1 » sur les liens du pied de page : contredits par la mesure des couleurs calculées (11,37:1) ; artefact de l'outil, non retenu ; `alternatives.html` : échec d'analyse de l'outil (JSON tronqué) | ce rapport |

### 3.3 Dépôt, publication, archives

| Contrôle | Résultat | Preuve |
|---|---|---|
| HEAD, origin/main, commit déployé | f9b3ae14, identique, divergence 0/0, Pages status built | `gh api` dans la session, section 4 |
| Arbre de travail | propre hors `cuisine-moi/...` non suivi, préservé | `git status --short -uall` |
| 147 fichiers publics contre locaux (index racine, catalogue, 8 fichiers du jeu, favicon, 2 ZIP, 132 PNG, 2 variantes d'URL) | 147 identiques (SHA-256) | `empreintes/comparaison-public-local.json`, `empreintes/local-head.sha256` |
| ZIP 1 et 2, local et public | 66 PNG + `alternatives.md` chacun, couverture exacte 1-132, 0 doublon, PNG identiques aux images du jeu, `alternatives.md` identique, 57,93 et 64,03 Mio, `unzip -t` sans erreur, horodatage figé 2026-01-01 | `zip/controle-zip.json` |
| Reproductibilité de `build.py` (worktree détaché) | 7 sorties byte-identiques, aucun fichier créé ou modifié hors `ecommerce-opquast-v5/` (seuls `__pycache__` ignorés) | `build/reproductibilite-build.log` |
| `publish_variant.py` (worktree) | idempotent sur l'état publié : aucun diff de `index.html` ni de `published-versions.json`, 30 variantes conservées, 30 tuiles | `build/publish-variant-worktree.log` |
| Accueil : deux liens de téléchargement, anciennes variantes | 2 liens dans le pied, 30 tuiles, favicon basculé sur le jeu | `navigateur/public-telechargements-agent-browser.log`, diff du commit |
| CSP | empreintes SHA-256 du script (18 541 caractères) et du style (3 010) intégrés présentes dans la CSP ; aucun attribut `nonce` ; pas d'`unsafe-inline` | contrôle statique, section 4 |
| Sources publiées | `source/storyboard.md`, `source/prompts/*`, `tests/*.py`, `slides.json` sont servis publiquement (dépôt public) ; aucun contenu de fiche participant, d'annexe K, de corrigé ou de barème détecté dans `slides.json`, le storyboard, les prompts et les revues (recherche textuelle) | `editorial/revue-questions-corrections.md` section 5 |

## 4. Commandes exécutées, outils, empreintes et résultats

### 4.1 Environnement

| Outil | Version |
|---|---|
| Python | 3.14.7 (`python3`, `-I` pour les scripts qui lisent des fichiers téléchargés) |
| Node | 24.18.0 ; npm 11.16.0 |
| html-validate / vnu-jar (verrouillés à la racine) | 11.5.3 / 26.6.24 |
| ShipGuard | 2.18.0 (plugin `shipguard@shipguard`, cache `~/.claude/plugins/cache/shipguard/shipguard/2.18.0`) |
| agent-browser (Chromium headless, session nommée `revue-ecommerce-v5`) | 0.31.1 |
| Chrome piloté par chrome-devtools MCP | 156.0.8078.48 |
| accesslint audit_live (Chrome headless dédié, port 9222) | serveur MCP de la session |
| Pillow (planches d'habillage) | 12.3.0 |
| MCP Opquast | API publique en direct (HTTP 200, 245 règles) ; API privée HTTP 403 (clé absente) ; snapshot local du 3 septembre 2026 |
| gh | authentifié, lecture seule de l'API Pages |

### 4.2 Empreintes auditées

- Commit revu : `f9b3ae14297ef51cde4cdfc81b95dd191097ffa5` (auteur 16 h 15, commit 22 h 56 le 28 octobre 2026) ; origin/main identique ; build GitHub Pages 1322678911 sur ce commit, statut `built`, 22 h 02 UTC.
- `ecommerce-opquast-v5-slides.zip` : `69e0b8f0c3a794cd348f5ca35aa27871f0a827b4b2d9e8275c089c5257751e23`, 60 745 516 octets.
- `ecommerce-opquast-v5-slides-partie-2.zip` : `6d094a8fa488739957e0826d96ec01273068e5738cabdce655c51ada5de36bf2`, 67 141 865 octets.
- `index.html` du jeu : `32474303bc7c1f7fb0f7d3167c9d7ef7339d4bbbe3d6c9c59135cd80804ccdbe` ; `alternatives.md` : `7d68592d37235cf2b6e7314772ed4f6a562289ba1decf7032867c34a5857f565` (identiques avant et après régénération).
- 438 fichiers suivis du jeu et de la racine : `empreintes/local-head.sha256` ; 147 comparaisons public/local : `empreintes/comparaison-public-local.json`.
- Storyboard : empreinte déclarée du storyboard v3 source `d0ca4c6c...` non vérifiable (source hors dépôt).

### 4.3 Commandes et résultats

| Commande (worktree détaché f9b3ae1 sauf mention) | Résultat | Journal |
|---|---|---|
| `python3 scripts/check_notes_orales_opquast.py ecommerce-opquast-v5` | 132 slides, 0 erreur, 0 avertissement, exit 0 | `tests/tests-python.log` |
| `python3 -m unittest discover -s scripts/tests` | 12 tests OK | idem |
| `python3 -m unittest discover -s ecommerce-opquast-v5/tests` | 14 tests OK | idem |
| `python3 -m unittest discover -s matrice-slide-ai/tests` | 28 tests OK, 1 ignoré | idem |
| `scripts/validate_variant.sh ecommerce-opquast-v5` (html-validate puis vnu sur index, alternatives, accessibilite et index racine) | 14 tests OK, validateurs silencieux, exit 0 | `tests/validate-variant.log` |
| `python3 ecommerce-opquast-v5/build.py` puis comparaison des empreintes et inventaire des fichiers | 7 sorties identiques, aucune écriture hors du jeu | `build/reproductibilite-build.log` |
| `python3 matrice-slide-ai/publish_variant.py --slug ecommerce-opquast-v5` puis `git diff` | aucun diff, 30 variantes ; worktree restauré | `build/publish-variant-worktree.log` |
| Suites communes (`miweb-objectifs-2030-v1..v4`, offres, span-pan, gouvernance, checklist) | non exécutées : le commit ne modifie que `matrice-slide-ai/build.py::footer` (branche `not version_context`) dont le comportement avant/après a été mesuré sur trois variantes (`process-check/footer-avant-apres.log`) ; voir section 6 | |
| `curl` de 147 fichiers publics avec en-têtes | tous 200 ; `last-modified` 22 h 02 UTC | `journaux/telechargement-public.log`, `journaux/telechargement-slides-publics.log`, `public/entetes/` |
| `unzip -t` des deux ZIP, extraction locale et publique, comparaison des PNG | 0 erreur, 132 PNG identiques | `zip/controle-zip.json` |
| Script de couverture description / textes visibles sur `slides.json` | 436 textes de corps sur 655 absents de la description ; QCM questions 125/125 | section 2, M1 |
| Script de comparaison storyboard / `slides.json` | 132 vues, titres et listes blanches identiques, 0 tiret cadratin, alt 49 à 80 caractères | session (sortie reproduite dans `editorial/sequence-etats.txt`) |
| `curl https://api.opquast.com/checklist/public/?version=qualite-numerique` puis comparaison des 39 libellés | 3 libellés divergents (38, 63, 66) | `opquast/libelles-live-vs-snapshot.md` |
| `node seams-lecteur.js` (fonctions extraites de `index.html`) | aller-retour hash 132/132, hashs invalides vers slide 1, `slideUrl` retire `slides` et garde `projection` | `shipguard/logic-audit/seams-lecteur-resultats.json` |
| `gh api repos/alexandra-guiderdoni/slides-miweb/pages/builds/latest` | commit f9b3ae14, status built | session |

### 4.4 ShipGuard 2.18.0 : ce qui a été réellement exécuté

- Capacités découvertes : 21 skills du plugin, CLI `cli/shipguard.mjs` (init, serve, stop, crawl, run, review, status), agent-browser 0.31.1 présent. Aucun manifeste `visual-tests/` n'existait pour ce dépôt (seul `visual-tests-old/` historique, trois manifestes d'un autre périmètre, non réutilisés). Aucune installation ni modification des hooks ShipGuard.
- `shipguard init` et six manifestes YAML écrits dans le worktree isolé (`shipguard/visual-run/manifests/ecommerce/01` à `06`), serveur local `python3 -m http.server 8731` sur le worktree, démarré et arrêté par cette revue.
- `shipguard crawl --base-url=http://127.0.0.1:8731/ecommerce-opquast-v5/ --max-pages=400` : 123 pages, 879 ressources, 0 lien ou ressource cassé (`shipguard/crawl.log`, `shipguard/visual-run/crawl-results.json`).
- `shipguard run --profile=ecommerce --no-crawl` : 6 manifestes, 5 PASS, 1 FAIL (03-accordeons, assertion « Fermer les accordéons » exécutée avant la mise à jour du libellé : test périmé par synchronisation, produit conforme à la mesure directe), 1 étape agent (`llm-check` du plein écran) évaluée par le relecteur principal : PASS (capture relue, contrôles de projection et « Quitter le plein écran » visibles). 14 captures produites, 12 relues individuellement (`shipguard/visual-run/screenshots/`, `shipguard/run-ecommerce.log`, `shipguard/visual-run/visual-results.json`, `findings.json`, `review.html` construit). Exit CLI 1 = « findings » (le faux positif).
- sg-logic-audit (mode hybrid, profondeur standard) : 3 candidats (lecteur, partition ZIP, publication racine), 11 obligations, 0 violation confirmée, 3 risques faibles, 1 question, 1 non couvert (tactile) ; 9 mesures, 5 raisonnements (`shipguard/logic-audit/logic-results.json`, `logic-report.md`).
- sg-process-check (mode execute sur une couture pure) : `footer()` de la matrice avant (6cbdcd6) et après (f9b3ae1) sur trois variantes et deux contextes : seul le pied de page racine du jeu e-commerce change (deux liens au lieu d'un), les variantes sans `download_parts` sont identiques ; nom d'archive invalide refusé, parties vides conservent le lien historique, libellé échappé, doublon de libellé fusionné (`shipguard/process-check/footer-avant-apres.log`).
- sg-code-audit (mode quick, report-only, diff 6cbdcd6...f9b3ae1, 2 zones, modèle opus, worktrees isolés créés par l'outil Agent) : voir section 5.
- sg-visual-review (tableau de bord) : non servi ; `review.html` construit par `run` et copié dans les preuves. sg-pre-review, sg-ship, sg-record : non utilisés, hors périmètre.

## 5. Audit de code sg-code-audit (run audit-20261028-223500000-f9b3ae14)

Dispatch : `shipguard/code-audit/dispatch.json`. Zones : z01 = `ecommerce-opquast-v5/build.py` et ses tests ; z02 = `matrice-slide-ai/build.py`, `publish_variant.py`, test de la matrice et `index.html` racine. Report-only, aucune modification de source.

### 5.1 Zone z02 (matrice et accueil) : 19 constats, 0 critique, 0 élevé, 5 moyens, 14 faibles

Moyens :

- `matrice-slide-ai/build.py` ligne 1051 : pied de page indexé par libellé ; deux parties de même libellé n'en donnent qu'une, et une partie nommée « Alternatives textuelles » remplacerait ce lien de navigation (mesuré).
- ligne 1044 : `download_parts` lu sans contrôle de forme ; `KeyError`, `TypeError` ou `AttributeError` non interceptées dans `main()` (mesuré) ; aucune corruption car `render_root` précède les écritures.
- `publish_variant.py` ligne 195 : la publication n'exige que `{slug}-slides.zip` ; une partie déclarée mais absente donnerait un lien 404 sur l'accueil (les deux ZIP existent aujourd'hui).
- ligne 1621 : la matrice ne gère `download_parts` que sur l'accueil ; un futur jeu créé par `create_variant.py` avec `download_parts` ne produirait qu'un seul ZIP alors que l'accueil afficherait des parties.
- ligne 319 : le motif `#slide-(\d{2})` de la matrice ne reconnaît pas `#slide-100` et au-delà ; le jeu e-commerce a corrigé sa copie (`\d{2,}`), pas la matrice dont hériteront les futurs jeux.

Faibles (sélection) : contrôle du nom d'archive perméable à l'antislash, `?`, `#` et `.zip` seul ; libellé vide accepté ; test du pied de page sans cas d'erreur ; dates impossibles acceptées (« 31 février 2026 ») ; écritures non atomiques du catalogue et de l'accueil ; modale `#modal-menu` sans `aria-labelledby` ; `accessibilite.html` générée mais sans lien entrant ; liens ZIP sans indication de poids ; paramètre `root_latest_zip_name` inutilisé ; favicon du dernier jeu non vérifié.

Vérifications positives de la zone : accueil recalculé identique au fichier versionné ; empreinte CSP conforme au style intégré ; aucun id en double ; hiérarchie h1, h2, h3 ; `lang` et `viewport` présents ; pyflakes vierge ; 28 tests OK.

Artefact : `shipguard/code-audit/runs/audit-20261028-223500000-f9b3ae14/zone-z02-r1-r1-z02-a1.json` (copié depuis le worktree de l'agent, rétention intent-to-add confirmée, exit 0).

### 5.2 Zone z01 (générateur du jeu et tests)

Résultat : 29 constats, 0 critique, 1 élevé, 8 moyens, 20 faibles. Les 14 tests de la zone passent ; les fichiers HTML et Markdown sur disque sont identiques à la sortie de `build.py` (comparaison exécutée par l'agent).

Élevé, reproduit par l'agent en Chromium headless et contre-éprouvé par le relecteur principal sur le site public (voir M12) : `build.py` ligne 750, le gestionnaire `popstate` appelle `getIndexFromHash()`, qui renvoie 0 pour tout fragment autre que `#slide-NN`, puis réécrit l'URL en `#slide-01` ; les cinq liens d'évitement (`#contenu`, `#sommaire`, `#diaporama`, `#description-active`, `#footer`) ramènent donc le diaporama à la slide 1.

Moyens :

- ligne 759 : Début, Fin et les flèches sont interceptés sur toute la page (Fin saute à la slide 132 et bloque le défilement natif) ; reproduit.
- ligne 170 : `touch-action: pan-y` sur l'image empêche le zoom par pincement (déduit du code).
- ligne 1627 : parties ZIP de `variant.json` non contrôlées : un trou dans les plages fait disparaître des slides sans erreur, un chevauchement produit des doublons (sonde exécutée) ; cohérent avec le risque logic-003.
- ligne 1624 : nom d'archive non validé dans le build du jeu (écriture possible hors de `assets/downloads`), alors que la matrice le valide pour l'accueil.
- ligne 81 : `KeyError` brute à l'import si `variant.json` n'a pas `download_parts`.
- ligne 1631 : taille du ZIP contrôlée après écriture : archive trop lourde et pages déjà réécrites conservées en cas d'échec.
- ligne 1326 : URL nue contenant `&` doublement échappée (`&amp;amp;`), lien cassé ; latent, aucune slide actuelle n'est concernée (sonde exécutée).
- ligne 878 : le build n'impose pas que description, transcription et discours soient distincts, contrairement à AGENTS.md ; seul le script des notes compare discours et transcription.

Faibles (sélection) : « Juin 2026 » codé en dur dans la page Accessibilité ; README généré avec les plages 1-66 / 67-132 en dur ; anciens ZIP jamais supprimés quand le découpage change ; code de l'accueil racine mort dans le jeu ; repli sur `slides.example.json` absent ; CSP autorisant tout `cdn.jsdelivr.net` et DSFR chargé sans `integrity` ; descriptions et discours repliés sans JavaScript (constaté, cohérent avec M10) ; défauts mineurs du parseur Markdown interne ; `?projection=1` conservé dans les URL suivantes ; `#slide-5` ramène sans message à la slide 1 ; focus laissé dans une slide masquée après balayage ; tests aux plages ZIP écrites en dur et assertions sur le texte du script plutôt que sur son comportement (ce qui a laissé passer le bug élevé).

Artefact : `shipguard/code-audit/runs/audit-20261028-223500000-f9b3ae14/zone-z01-r1-r1-z01-a1.json` (rétention intent-to-add confirmée, exit 0).

### 5.3 Agrégation

`shipguard/code-audit/audit-results.json` : 2 zones, 48 constats, 0 critique, 1 élevé, 13 moyens, 34 faibles ; 0 corrigé ; aucune phase de vérification croisée (mode quick, un tour). Le constat élevé a été contre-éprouvé indépendamment (M12) ; les constats moyens sont des lectures et sondes locales d'un seul agent.

## 6. Points non vérifiés et incidence sur le verdict

- Lecteur d'écran réel : aucune session VoiceOver ou NVDA n'a été conduite ; les constats d'accessibilité reposent sur l'arbre d'accessibilité (snapshots), le DOM, les couleurs calculées et un outil automatique. Aucune conformité RGAA n'est affirmée ; la page `accessibilite.html` du jeu dit « non auditée », ce qui reste exact.
- Navigateur sans JavaScript : non piloté ; conclusion M10 fondée sur le HTML statique et l'état mesuré des panneaux au chargement. Incidence : M10 reste une déduction forte, pas une observation d'un navigateur réellement sans script.
- Gestes tactiles (balayage) : non mesurés, raisonnement seulement.
- Plein écran dans un navigateur de bureau avec fenêtre visible : mesuré en Chromium headless seulement (activation effective) ; le comportement de Safari ou Firefox n'a pas été observé.
- API privée Opquast (solution, contrôle, explication) : inaccessible (HTTP 403) ; les champs solution et contrôle n'ont été vérifiés que contre le snapshot du 3 septembre 2026 ; les 39 libellés et objectifs ont été vérifiés contre l'API publique du 28 octobre 2026.
- Suites de tests des neuf jeux historiques listées par AGENTS.md pour une modification commune : non exécutées (seule la matrice a été exercée, 28 tests, plus la mesure avant/après de la fonction modifiée). Incidence faible : le changement commun ne touche qu'une branche de `footer()` inactive pour les variantes sans `download_parts`, ce qui a été mesuré.
- Fiche participant : le fichier lui-même n'a pas été fourni ; seule l'absence de fuite dans les sources et exports a été recherchée par mots-clés.
- Images : les illustrations ont été lues à l'échelle rendue par l'outil de lecture, avec agrandissements ciblés (habillage des 132 slides, zones litigieuses). Un pseudo-texte minuscule dans une illustration pourrait avoir échappé ; aucun n'a été observé.
- Alternatives courtes : le skill `alt-text` n'était pas chargé dans les sessions des agents d'inspection ; ses critères ont été transmis par la consigne, ce qui n'équivaut pas à une exécution du skill.
- Interférence navigateur : la fenêtre Chrome ouverte par chrome-devtools MCP a été manipulée par un tiers pendant la revue (activation utilisateur détectée, hash changeant de #slide-08 à #slide-10 sans action de la session). Les parcours ont donc été exécutés dans une session agent-browser possédée et séquentielle ; la page chrome-devtools n'a pas été fermée pour ne pas interrompre son utilisateur.
- ShipGuard sg-code-audit : exécuté en mode quick (1 tour, 2 zones) et sans phase de vérification croisée 5.6/5.7 ; les constats de code sont des lectures et des sondes locales, pas des bugs confirmés par un second agent.
- Lighthouse, performance, SEO : hors périmètre, non exécutés.

## 7. Corrections recommandées (non appliquées)

Par ordre de priorité :

1. Régénérer avec ImageGen les quatre images 028, 049, 117, 125 (en-tête « EXPÉRIENCES DURABLES »), puis relancer `build.py` pour reconstruire les deux ZIP, les tests, `validate_variant.sh` et la publication. Mettre à jour les revues correspondantes dans `source/reviews/` avec un relecteur distinct du producteur.
2. Donner l'équivalent textuel des questions dans la surface du lecteur : soit intégrer les textes visibles (énoncé et propositions) dans la `description` des 25 questions QCM et des 10 affirmations T0/T1 et des corrections, soit ajouter un lien explicite « Transcription » par slide vers `alternatives.html#alternative-slide-NN` depuis le lecteur. Décision d'architecture à prendre par le propriétaire (le dépôt fige deux accordéons).
3. Trancher la calibration des alternatives courtes (alt = ce que montre l'image, ou alt = leçon) puis appliquer en lot les 71 propositions des fiches `images/resultats/slide-NNN.json` et arbitrer les 14 `a_confirmer`.
4. Règle 38 : aligner la citation des slides 047 et 056 sur l'API publique ou dater explicitement la source (« libellé du 3 septembre 2026 ») ; même traitement pour « mail » / « e-mail » (058, 060).
5. Harnais : retirer `transition` de `FORBIDDEN_HEADINGS` dans `scripts/check_notes_orales_opquast.py` ou retirer l'exigence de transition du contrat, puis rédiger les transitions ; réécrire les notes des 35 slides de question (une note par énoncé) et retirer la métapédagogie des slides 080 et 081.
6. Dispositif T0 : documenter dans le README du jeu que le T0 est un amorçage et non une mesure si l'URL est diffusée avant la séance, ou passer le T0 hors ligne sur la fiche participant.
7. QCM : réécrire les cinq distracteurs non fonctionnels, retirer les marqueurs absolus des distracteurs, casser la rotation A-B-C des bonnes réponses.
8. Slide 017 : réintroduire une mention textuelle sur le produit indisponible de la carte R65 ou signaler la carte comme contre-exemple ; slide 070 : corriger l'alt et vérifier l'enveloppe de la carte C en original.
9. Lecteur (toutes variantes) : dans le gestionnaire `popstate`, ignorer les fragments qui ne sont pas `#slide-NN` (ou ne réagir qu'aux fragments de slide et à `?slides=all`) et ajouter un test comportemental (Node ou navigateur) du lien d'évitement ; appliquer d'abord à la matrice puis aux jeux à régénérer, en respectant l'immuabilité des jeux publiés (décision du propriétaire).
10. Matrice : aligner `matrice-slide-ai/build.py` sur le jeu (motif `#slide-(\d{2,})`, génération des parties ZIP, validation de forme de `download_parts`, vérification des archives déclarées dans `publish_variant.py`) ; corriger la date codée en dur de `accessibilite.html` ; donner un nom accessible à la modale du menu.
11. Compléter `regles` sur les slides question et corriger 083, 123, 125, 059 ; ajouter un exercice pour les règles 31 et 54 si la série est prolongée.
12. Revues d'image : exiger un relecteur distinct et une découpe agrandie de l'habillage dans le dossier `source/reviews/` (grille : promesse, preuve externe, cas négatif, verdict, limites).

## 8. Intégrité des sources et des ressources étrangères

- Dépôt principal : `git status --short -uall` avant et après la revue ne montre que `?? cuisine-moi/2026-10-28-serie-opquast-ecommerce.md` (préexistant, intact) ; HEAD inchangé f9b3ae14. Aucun commit, push, déploiement, changement de configuration ni installation globale.
- Worktree étranger `/Users/alex/Claude-worktrees/slides-miweb-ecommerce-etalons` (branche `feat/ecommerce-etalons`, 152e022) : non touché.
- Ressources créées par la revue : dossier de preuves ; worktree détaché `.../revue-ecommerce-opquast-v5-20261028/worktree` (lien symbolique `node_modules`, `visual-tests/` et `.gitignore` modifié par `shipguard init`, restaurés ou supprimés à la clôture, voir journal de clôture) ; serveur `python3 -m http.server 8731` (arrêté) ; session agent-browser `revue-ecommerce-v5` (fermée) ; Chrome headless lancé par accesslint sur le port 9222 (arrêté) ; deux worktrees d'agents sg-code-audit sous `.claude/worktrees/` du dépôt principal (artefacts collectés puis worktrees retirés). La page chrome-devtools ouverte sur le site public a été laissée ouverte (utilisée par un tiers).
- Journal de clôture : `journaux/cloture.log`.

## 9. Dossier de preuves

- `RAPPORT-REVUE-ECOMMERCE-OPQUAST-V5.md` : ce rapport.
- `images/` : consigne d'inspection, 132 dossiers par slide (`bundles/`), 132 fiches JSON et 6 synthèses (`resultats/`), découpes et zooms, 12 planches d'habillage (`habillage/`), matrice (`matrice-132-slides.md` et `.json`).
- `editorial/` : notes continues, extraits questions et corrections, séquence des états, `revue-notes-orales.md`, `revue-questions-corrections.md`.
- `opquast/` : snapshot des règles 30 à 68, API publique en direct, comparaison des libellés, règles et slides, `revue-regles-30-68.md`.
- `empreintes/`, `public/`, `zip/`, `build/`, `tests/` : empreintes, téléchargements publics et en-têtes HTTP, extractions des ZIP, reproductibilité, publication, journaux de tests.
- `navigateur/` : journaux agent-browser et captures (accordéons, focus, 320 px, 640 px, plein écran).
- `shipguard/` : crawl, run (manifestes, résultats, captures, review.html), logic-audit, process-check, code-audit (dispatch et artefacts de zone).
- `scripts/` : scripts de téléchargement ; `journaux/` : téléchargements, serveur local, clôture.
