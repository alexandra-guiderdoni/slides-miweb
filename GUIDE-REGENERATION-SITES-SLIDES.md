# Guide - Régénérer un site GitHub Pages depuis un jeu de slides

PDG-LARGE-FILE-JUSTIFICATION: ce guide dépasse 200 lignes parce qu’il sert de mode opératoire autonome pour régénérer un site complet depuis un jeu de slides, avec contrat de résultat, structure de fichiers, schéma `slides.json`, transcriptions, génération, validation HTML, inspection locale, publication GitHub Pages et checklist finale. Le découper ferait perdre le fil d’exécution attendu pour les prochaines variantes.

Ce document est le mode opératoire réutilisable pour publier un nouveau site statique à partir d’un jeu de slides images. Il reprend le modèle MiWeb existant : présentation web, mode projection, téléchargement ZIP, page d’accessibilité et transcriptions complètes.

Il doit être utilisé pour les prochaines variantes thématiques ou versions nommées du dépôt, sans modifier les variantes déjà publiées `miweb-objectifs-2030-v1` à `miweb-objectifs-2030-v4`.

## Positionnement

Ce guide est volontairement plus détaillé que le README racine et que `DEMARCHE-VERSIONS.md`.

- `README.md` donne l’entrée courte et les commandes principales.
- `DEMARCHE-VERSIONS.md` donne la procédure opérationnelle.
- Ce guide détaille les entrées, les fichiers attendus, les vérifications, l’inspection locale, la prévisualisation et le push.
- `matrice-slide-ai/README.md` décrit la matrice qui crée les dossiers autonomes.
- `docs/prd/`, `docs/prompts/`, `docs/goals/` conservent les cadrages et objectifs historiques sans encombrer la racine.

## Déclencheur

Utiliser ce guide quand il faut publier un nouveau site GitHub Pages à partir :

- d’un dossier contenant des images `slide-01.png`, `slide-02.png`, etc., ou des images préfixées comme `checklist-span-slide-01.png` ;
- d’un storyboard ou d’une note source ;
- d’une demande de publication avec alternatives textuelles ;
- d’une variante thématique qui ne remplace pas V1, V2, V3 ou V4.

Ne pas utiliser ce guide pour modifier une slide isolée dans une version déjà publiée, corriger une faute dans un HTML généré, ou créer un nouveau framework de site.

## Contrat de résultat

Chaque variante publiée doit produire un dossier autonome contenant :

- `index.html` : présentation web accessible avec navigation clavier ;
- `alternatives.html` : transcriptions complètes des slides ;
- `alternatives.md` : version Markdown des transcriptions ;
- `accessibilite.html` : état d’accessibilité du site ;
- `assets/slides/` : images publiées ;
- `assets/downloads/` : ZIP des slides et transcriptions ;
- `assets/favicons/` : favicon locale ;
- `source/` : source éditoriale, storyboard, contact sheet et reçus utiles ;
- `slides.json` : source canonique des titres, descriptions, textes visibles et messages ;
- `build.py` : générateur autonome de la variante ;
- `tests/` : tests de contrat du site.

La variante doit être listée sur l’accueil racine seulement après génération, vérification et passage explicite par `matrice-slide-ai/publish_variant.py`.

## Invariants

- Ne jamais modifier `miweb-objectifs-2030-v1`, `miweb-objectifs-2030-v2`, `miweb-objectifs-2030-v3` ou `miweb-objectifs-2030-v4` pour publier une nouvelle variante.
- Ne jamais publier une image sans transcription dans `slides.json`.
- Ne jamais inventer de chiffre, seuil, engagement, audit ou conformité absents de la source.
- Ne jamais déclarer la variante conforme RGAA sans audit dédié.
- Ne jamais livrer uniquement les images : `alternatives.html` et `alternatives.md` sont obligatoires.
- Ne jamais hand-edit `index.html`, `alternatives.html`, `alternatives.md`, `accessibilite.html` ou le ZIP après génération ; modifier la source puis relancer `build.py`.
- Ne pas ajouter de framework, de route, de page ou de composant décoratif hors besoin de publication.

## Parcours court

Pour un cas standard, le parcours attendu est :

```bash
python3 matrice-slide-ai/create_variant.py \
  --slug <dossier> \
  --title "Titre public" \
  --storyboard /chemin/vers/storyboard.md \
  --slides-dir /chemin/vers/images
python3 <dossier>/build.py
scripts/validate_variant.sh <dossier>
python3 matrice-slide-ai/publish_variant.py --slug <dossier>
scripts/validate_variant.sh <dossier>
scripts/push-pages.sh
```

Si les images source sont préfixées, ajouter `--slide-prefix <prefixe>` à la commande de création.

## Entrées attendues

Avant de générer le site, vérifier que les éléments suivants existent :

- dossier d’images validées ;
- nombre exact de slides ;
- source éditoriale validée ;
- storyboard ou trame de génération ;
- contact sheet si plusieurs images ont été générées ;
- nom du dossier public de variante ;
- libellé public à afficher sur l’accueil racine.

Exemple de nommage :

```text
miweb-offre-mutualisee-listes-diffusion-2026-condensee
miweb-offre-mutualisee-listes-diffusion-2026-longue
```

## Préparation du dossier avec la matrice

Créer le dossier de variante depuis la matrice, sans écraser une variante publiée :

```bash
python3 matrice-slide-ai/create_variant.py \
  --slug <dossier> \
  --title "Titre public" \
  --storyboard /chemin/vers/storyboard.md \
  --slides-dir /chemin/vers/images
```

La commande copie `build.py`, les tests, le favicon, le storyboard, `slides.json` et les images `slide-*.png`. Elle ne change ni `index.html` racine ni `published-versions.json`.

Si les images source sont préfixées, déclarer ce préfixe au lieu de renommer à la main :

```bash
python3 matrice-slide-ai/create_variant.py \
  --slug <dossier> \
  --title "Titre public" \
  --storyboard /chemin/vers/storyboard.md \
  --slides-dir /chemin/vers/images \
  --slide-prefix checklist-span-
```

La matrice copie alors `checklist-span-slide-01.png` vers `assets/slides/slide-01.png`.

## `slides.json`

`slides.json` est la source canonique des transcriptions. Le HTML, le Markdown et le ZIP doivent être régénérés depuis ce fichier.

Chaque entrée doit contenir :

```json
{
  "numero": 1,
  "titre": "Titre de la slide",
  "image": "assets/slides/slide-01.png",
  "alt": "Alternative courte.",
  "description": "Description complète de l’image et de sa structure.",
  "textes_visibles": [
    "Texte visible 1",
    "Texte visible 2"
  ],
  "message": "Message à retenir.",
  "transcription": "### Idée principale\n\nContenu affiché sur la slide.",
  "notes_orateur": "### Situation utilisateur\n\n- Première idée.\n- Deuxième idée.\n\n### Transition\n\nPhrase vers l’idée suivante."
}
```

Règles :

- `numero` commence à 1 et suit l’ordre réel des images ;
- `image` pointe vers un fichier existant dans `assets/slides/` ;
- `alt` reste court, idéalement moins de 60 caractères ;
- avant génération, refaire une passe avec le skill `alt-text` sur tous les `alt` : ils doivent remplacer l’information utile, éviter les formules comme « image de », rester courts et ne pas inventer d’information absente du visuel ou du contexte ;
- `description` décrit la scène, la structure et les informations utiles non portées par l’alt court ;
- `textes_visibles` reprend les textes de la slide, sans corriger silencieusement le sens ;
- `message` formule l’idée à retenir sans inventer de conclusion ;
- `transcription` restitue le contenu affiché et sa structure ;
- `notes_orateur` complète la transcription sans la répéter et reste directement prononçable.

## Discours oral et cohérence des exports

La transcription descriptive et le discours oral sont deux champs obligatoires de slides.json, distincts l’un de l’autre, de l’alternative textuelle et des textes visibles. Chacun doit figurer dans son propre accordéon de la présentation, ainsi que dans alternatives.html et alternatives.md. Pour les sources, préférer un lien explicite au format [libellé de la source](https://exemple.fr/source) ; une URL HTTPS en clair est aussi cliquable en HTML. Le balisage **gras** est rendu sémantiquement.

Vérifier au navigateur qu’un retour ou une avance vers une URL ?slides=all réaffiche toutes les slides. La CSP des pages statiques doit autoriser les scripts et styles intégrés par empreintes SHA-256, sans nonce fixe.

## Notes orales des séries Opquast

Pour une série consacrée au référentiel Opquast, utiliser le prompt canonique `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`.

Ne pas rédiger toute la série immédiatement. Commencer par quatre slides étalons :

- une ouverture de partie ;
- une slide de règle ;
- une slide d’éclairage ;
- une synthèse.

Faire valider explicitement ces quatre résultats avant de généraliser le style ou de répartir les autres slides entre plusieurs agents.

Le discours oral attendu :

- complète la transcription sans la répéter ;
- se lit directement à voix haute ;
- porte des titres liés au contenu ;
- utilise des listes à puces pour faciliter le scan ;
- exclut les intentions pédagogiques, les consignes d’animation et la gestion du groupe ;
- distingue le préjudice concret de ce que garantit réellement chaque règle ;
- conserve une transition courte entre les idées ;
- limite le RGAA aux éclairages nécessaires ;
- utilise uniquement le tiret simple `-`.

Avant la génération, lancer :

```bash
python3 scripts/check_notes_orales_opquast.py <dossier-jeu>
```

Ce script contrôle les champs obligatoires, la hiérarchie Markdown, les listes, les sections attendues pour les règles, les transitions, les principaux marqueurs de métapédagogie et les tirets longs.

Il ne valide pas le fond Opquast. Les numéros, libellés, objectifs, contrôles et limites doivent être vérifiés séparément auprès du skill ou du MCP Opquast. Il ne remplace pas non plus la relecture croisée des agents ni la lecture globale de la série.

## Série Opquast essentielle générée avec ImageGen

Cette fabrique s’applique aux séries courtes qui couvrent une thématique Opquast complète avec une progression par problèmes utilisateur. Elle complète les règles générales du présent guide et le contrat des notes orales.

### Référence validée

La série `navigation-opquast-v5-essentielle-v2/` constitue le précédent local accepté :

- 17 slides pour les vingt règles Navigation 153 à 172 ;
- regroupement des règles en cinq blocs d’usage ;
- images finales générées intégralement avec ImageGen ;
- textes visibles rendus directement dans les images ;
- alternatives, descriptions, transcriptions et discours oraux distincts ;
- prompts complets et critères de rejet conservés dans `source/prompts/`.

S’en servir pour reproduire la méthode, la densité et la grammaire visuelle. Ne pas recopier ses numéros, formulations ou illustrations dans une autre thématique.

### Grammaire visuelle commune

Sauf demande explicite d’une autre direction, conserver les caractéristiques suivantes :

- canevas paysage 16:9 de 1672 x 941 pixels ;
- fond blanc lumineux ;
- typographie sans serif bleu marine, très lisible en projection ;
- formes organiques très pâles dans les angles ;
- cartes pastel arrondies, ombres discrètes et pictogrammes vectoriels plats ;
- hiérarchie nette entre repère de bloc, titre, règles concernées, impact, garantie et formule de mémorisation ;
- espace blanc généreux et densité limitée ;
- en-tête discret `QUALITÉ NUMÉRIQUE - OPQUAST V5` ;
- pied de page texte `Opquast - présentation Miweb` ;
- pagination exacte et stable ;
- aucun logo réel ou inventé, filigrane, sceau, photographie, rendu 3D ou personnage de banque d’images ;
- aucun pseudo-texte dans les interfaces ou les illustrations.

La slide reste une composition visuelle complète, pas un fond destiné à recevoir ensuite des éléments HTML, SVG, Canvas ou du texte ajouté par script.

### 1. Verrouiller le périmètre Opquast

Avant le storyboard :

1. Interroger le skill ou le MCP Opquast.
2. Établir la liste exhaustive des règles de la thématique.
3. Vérifier pour chaque règle son numéro, son libellé, son objectif, ses contrôles et ses limites.
4. Écarter les règles seulement connexes qui appartiennent à une autre thématique.
5. Marquer `à vérifier` toute contradiction qui ne peut pas être arbitrée.

La série ne commence pas par un nombre de slides cible. Elle commence par un périmètre de règles prouvé.

### 2. Construire une architecture courte

Regrouper les règles par problème utilisateur, sans suivre mécaniquement l’ordre numérique. Chaque bloc doit répondre à une capacité identifiable, par exemple se situer, accéder, retrouver, agir ou garder la main.

Pour chaque slide, le storyboard précise :

- son rôle dans le raisonnement ;
- les règles concernées ;
- l’idée nouvelle apportée ;
- la transition vers la slide suivante ;
- la liste blanche exhaustive des textes visibles.

Une règle peut disposer de sa propre slide quand son enjeu exige une explication distincte. Plusieurs règles peuvent partager une slide si elles répondent au même problème et si leur portée reste identifiable. Chaque slide cite explicitement les règles qu’elle couvre.

### 3. Valider quatre slides étalons

Avant toute production en série, concevoir et faire valider :

- une ouverture ;
- une slide de règle ;
- un éclairage ou un regroupement de règles ;
- une synthèse.

La validation porte sur la hiérarchie, la densité, le vocabulaire, la grammaire visuelle, le niveau de détail et la complémentarité entre transcription et discours oral. Après validation, ces quatre slides deviennent le patron de la série.

### 4. Écrire un prompt contrôlable par slide

Conserver chaque prompt dans `<dossier-jeu>/source/prompts/slide-XX.md`. Le fichier contient :

- les références visuelles utilisées uniquement pour le style ;
- la taille exacte du canevas ;
- l’instruction de générer une seule slide finale ;
- la direction visuelle commune ;
- la composition propre à la slide ;
- la liste blanche numérotée des chaînes visibles ;
- l’interdiction de tout autre texte, numéro, logo ou pseudo-texte ;
- les contraintes de marges, lisibilité et projection ;
- les critères précis d’acceptation et de rejet.

Ne pas réserver d’espace vide pour un ajout ultérieur. Ne pas utiliser ImageGen comme simple générateur d’illustration à intégrer ensuite dans une composition séparée.

### 5. Générer et contrôler les images

Pour chaque image :

1. Générer la slide complète avec ImageGen.
2. Ouvrir le résultat en résolution originale.
3. Vérifier les dimensions 1672 x 941.
4. Comparer chaque chaîne visible caractère par caractère avec la liste blanche.
5. Vérifier les accents, apostrophes, numéros de règles, repères de bloc et pagination.
6. Vérifier que les pictogrammes et scènes ne contiennent aucun pseudo-texte.
7. Rejeter l’image en cas de texte parasite, faux logo, mot manquant, composition ambiguë ou lisibilité insuffisante.

Une correction doit être régénérée avec ImageGen. Ne pas masquer une erreur et ne pas corriger le texte par composition ou retouche après génération.

### 6. Produire les contenus accessibles

Après stabilisation des images :

- rédiger un `alt` court qui remplace l’information essentielle ;
- rédiger une `description` fidèle à la scène et à son organisation ;
- transcrire la structure et les textes réellement visibles ;
- formuler un `message` cohérent avec la slide ;
- rédiger des notes orales directement prononçables, complémentaires de la transcription ;
- appliquer le skill `alt-text` avant le build ;
- vérifier qu’aucun contenu accessible n’invente une information absente du visuel ou des sources.

Le discours oral suit `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`. La génération des images et la rédaction des notes peuvent être parallélisées seulement après validation des quatre slides étalons.

### 7. Organiser les contrôles croisés

Quand plusieurs agents interviennent :

- un agent vérifie le périmètre et les formulations Opquast ;
- des agents distincts peuvent travailler sur des blocs séparés ;
- aucun agent ne valide seul sa propre production ;
- une relecture croisée compare le visuel, la transcription, les notes et les règles citées ;
- l’agent principal réconcilie les contributions et relit la série comme un seul discours.

La parallélisation accélère la production, mais ne remplace pas l’arbitrage éditorial final ni l’inspection visuelle en résolution originale.

### 8. Versionner les annexes et les nouvelles thématiques

Un jeu publié reste immuable. Ne pas lui ajouter ultérieurement des annexes ou modifier son architecture en place.

- Pour prolonger Navigation, créer une nouvelle variante autonome à partir du kit validé, avec un slug distinct.
- Pour traiter Contenus ou une autre thématique, créer un nouveau dossier autonome avec `matrice-slide-ai/create_variant.py`.
- Copier dans le nouveau dossier son propre storyboard et ses propres prompts.
- Ne pas faire dépendre la nouvelle variante du dossier Navigation à l’exécution.

Le kit de base publié reste ainsi consultable, comparable et réversible pendant que les extensions évoluent séparément.

### 9. Définition de terminé

Une série Opquast essentielle est terminée seulement si :

- le périmètre des règles est validé ;
- chaque règle est couverte et citée ;
- les quatre slides étalons ont été approuvées ;
- toutes les images sont complètes, lisibles et contrôlées en résolution originale ;
- les prompts et le storyboard sont conservés dans `source/` ;
- les alternatives, descriptions, transcriptions, messages et notes orales sont distincts et cohérents ;
- les contrôles Opquast, les tests du jeu et les validateurs HTML passent ;
- la recette navigateur locale est concluante ;
- après publication autorisée, le commit local et le distant sont synchronisés et la page publique répond correctement.

## Métadonnées du jeu

La création écrit `variant.json` avec les libellés publics du jeu. Adapter ce fichier seulement si le titre, la description ou le libellé de source doivent changer.

Ne plus modifier `PUBLISHED_VERSIONS`, `LATEST_VERSION_SLUG` ou `ROOT_CATALOG_BOOTSTRAP` dans un `build.py` de variante pour publier l’accueil racine. Le catalogue racine appartient à `published-versions.json` et se met à jour avec `publish_variant.py`. Dans la matrice, `ROOT_CATALOG_BOOTSTRAP` sert seulement de graine de compatibilité si le catalogue racine n’existe pas encore.

Conserver le comportement existant :

- navigation clavier ;
- mode projection ;
- affichage de toutes les slides ;
- accordéons d’alternatives dans la présentation ;
- page `alternatives.html` ;
- génération `alternatives.md` ;
- ZIP contenant les slides et `alternatives.md` ;
- page `accessibilite.html` marquée non auditée.

## Génération

Depuis la racine du dépôt :

```bash
python3 <dossier>/build.py
```

Optimiser les images avec `scripts/optimiser-images.sh <dossier>` avant cette étape. Si des PNG sont optimisés ou remplacés après génération, relancer `python3 <dossier>/build.py` pour reconstruire le ZIP.

### Ordre des opérations sur les images

L'ordre compte, et il est contre-intuitif. Détail et mesures dans `PRD-009`.

**Toujours recompresser sans perte.** C'est gratuit et vérifiable. Le script le fait par
défaut et refuse de se déclarer terminé si les pixels ont changé : il compare l'empreinte
SHA-256 des données décodées avant et après.

**Ne rééchantillonner que si les dimensions du lot diffèrent visiblement.** Le
rééchantillonnage **alourdit** le PNG, parce qu'il transforme des aplats de couleur
uniforme, très compressibles, en dégradés à forte entropie. Sur les 40 visuels de
`navigation-opquast-v5`, le 28 septembre 2026, ramener 38 images de 1672 par 941 à 1600
par 900 a fait passer le lot de 37,5 à 39,1 mégaoctets, soit 4,3 pour cent de plus. La
recompression `oxipng` qui a suivi l'a ramené à 36,2 mégaoctets.

**Ne pas attendre de miracle d'une recompression sans perte sur un lot bien produit.** Sur
les PNG d'origine du même lot, non rééchantillonnés, `oxipng` ne gagne que 0,31 pour cent.
Le gain de 7,5 pour cent observé après normalisation rattrapait surtout l'encodage PNG de
Pillow, moins efficace.

**La quantification en palette n'est pas une optimisation sans perte.** Une palette
adaptative de 256 couleurs réduirait le poids de 35 à 55 pour cent selon l'image, pour un
écart colorimétrique moyen mesuré à 0,98 sur 255 et un léger banding dans les halos
dégradés, visible au zoom. Ces visuels comptent entre 17 000 et 99 000 couleurs uniques.
Cette piste n'est pas retenue par défaut ; elle demande une décision explicite.

`oxipng` est une dépendance externe facultative, non verrouillée, installée par
`brew install oxipng`. Aucune génération n'en dépend : le script échoue proprement en
donnant la ligne d'installation quand il est absent.

Le script doit générer :

- `<dossier>/index.html` ;
- `<dossier>/alternatives.html` ;
- `<dossier>/accessibilite.html` ;
- `<dossier>/alternatives.md` ;
- `<dossier>/README.md` ;
- `<dossier>/assets/downloads/<dossier>-slides.zip`.

Le build ordinaire ne doit pas écrire `index.html` racine.

## Publication racine

Après génération, tests et validation HTML :

```bash
python3 matrice-slide-ai/publish_variant.py --slug <dossier>
scripts/validate_variant.sh <dossier>
```

La commande vérifie le jeu, met à jour `published-versions.json`, puis régénère uniquement `index.html` racine. Le second passage de `validate_variant.sh` vérifie le jeu après changement du catalogue racine.

Après publication racine, contrôler que le diff correspond au périmètre attendu :

```bash
git status --short
git diff --stat
git diff -- README.md DEMARCHE-VERSIONS.md GUIDE-REGENERATION-SITES-SLIDES.md index.html published-versions.json <dossier>
```

## Vérifications obligatoires

Contrôles de contenu :

```bash
python3 -m json.tool <dossier>/slides.json >/dev/null
find <dossier>/assets/slides -name 'slide-*.png' | sort | wc -l
```

Pour une série Opquast :

```bash
python3 scripts/check_notes_orales_opquast.py <dossier>
python3 -m unittest discover -s scripts/tests
```

Tests de contrat :

```bash
scripts/validate_variant.sh <dossier>
```

Ce script lance les tests de contrat, `html-validate` et `vnu-jar` depuis les dépendances npm verrouillées à la racine. Si elles ne sont pas installées, lancer `npm ci` depuis la racine du dépôt.

Validation HTML directe si nécessaire :

```bash
node_modules/.bin/html-validate <dossier>/index.html <dossier>/alternatives.html <dossier>/accessibilite.html index.html
node_modules/.bin/vnu --errors-only <dossier>/index.html <dossier>/alternatives.html <dossier>/accessibilite.html index.html
```

Contrôle des transcriptions :

```bash
rg "Alternatives textuelles|Textes visibles|Message à retenir" <dossier>/index.html <dossier>/alternatives.html <dossier>/alternatives.md
```

Contrôle qualité des alternatives courtes :

- [ ] une passe `alt-text` a été faite sur `slides.json` avant `build.py` ;
- [ ] chaque `alt` remplace l’information utile plutôt que l’apparence ;
- [ ] aucun `alt` ne commence par « image de », « photo de », « icône de » ou équivalent ;
- [ ] les images complexes disposent d’une `description` longue quand l’alt court ne suffit pas.

Contrôle des chemins :

```bash
rg '<img src="assets/slides/slide-' <dossier>/index.html
rg 'href="#"' <dossier>/index.html <dossier>/alternatives.html <dossier>/accessibilite.html
```

Contrôle des accents après modification de Markdown :

```bash
bash /Users/alex/Claude/scripts/check-accents.sh <fichier.md>
```

## Inspection locale

Démarrer un serveur local depuis la racine du dépôt :

```bash
scripts/serve-local.sh 8000
```

Inspecter au navigateur :

```text
http://127.0.0.1:8000/<dossier>/
http://127.0.0.1:8000/<dossier>/?projection=1#slide-01
http://127.0.0.1:8000/<dossier>/?slides=all#diaporama
http://127.0.0.1:8000/<dossier>/alternatives.html
http://127.0.0.1:8000/
```

Vérifier manuellement :

- la variante apparaît sur l’accueil racine ;
- les images s’affichent ;
- le mode projection reste accessible ;
- chaque slide dispose d’un accordéon d’alternative ;
- `alternatives.html` liste toutes les slides ;
- la navigation par swipe horizontal fonctionne et reste couverte par les tests de contrat ;
- le ZIP est téléchargeable ;
- aucune version publiée ne change hors décision explicite.

## Prévisualisation depuis un autre Mac du réseau local

Utiliser cette section quand Alex veut tester depuis un MacBook Air, un iPad ou un autre poste avant publication GitHub Pages.

Le serveur ne doit pas être lié à `127.0.0.1`, car cette adresse ne répond que depuis la machine qui lance le serveur. Il faut écouter sur toutes les interfaces réseau avec `0.0.0.0`, puis utiliser l’adresse IP locale du Mac qui héberge le dépôt.

Depuis la racine du dépôt, vérifier d’abord si un port est déjà occupé :

```bash
lsof -nP -iTCP:8000 -sTCP:LISTEN
```

Si le port `8000` est déjà utilisé, choisir un autre port, par exemple `8001`.

Récupérer l’adresse IP locale du Mac Studio :

```bash
for iface in en0 en1 en2 bridge0; do
  ip=$(ipconfig getifaddr "$iface" 2>/dev/null || true)
  [ -n "$ip" ] && printf '%s %s\n' "$iface" "$ip"
done
```

Démarrer le serveur accessible sur le réseau local :

```bash
python3 -m http.server 8001 --bind 0.0.0.0
```

Tester depuis le Mac qui héberge le serveur avec l’adresse IP locale, pas seulement avec `127.0.0.1` :

```bash
curl -I http://<ip-locale>:8001/<dossier>/
curl -I http://<ip-locale>:8001/<dossier>/alternatives.html
```

URL à donner pour test depuis le MacBook Air :

```text
http://<ip-locale>:8001/<dossier>/
http://<ip-locale>:8001/<dossier>/?projection=1#slide-01
http://<ip-locale>:8001/<dossier>/?slides=all#diaporama
http://<ip-locale>:8001/<dossier>/alternatives.html
```

Points de vigilance :

- si `127.0.0.1:<port>` répond mais pas `<ip-locale>:<port>`, le serveur n’est probablement pas lié à `0.0.0.0` ou un pare-feu bloque l’accès ;
- si un autre service répond sur `127.0.0.1:<port>`, tester avec l’IP locale permet de confirmer le serveur réellement exposé sur le réseau ;
- les deux machines doivent être sur le même réseau local ;
- ne pas utiliser cette URL locale comme preuve de publication GitHub Pages : elle sert seulement à la prévisualisation avant push.

## Prévisualisation hors réseau local avec tunnel public

Utiliser cette section quand Alex n’est pas sur le même réseau local que le Mac Studio. Dans ce cas, l’URL `http://<ip-locale>:<port>/...` ne suffit pas : il faut exposer temporairement le serveur local via un tunnel public.

Préférer un serveur local lié à `127.0.0.1`, puis exposer seulement ce port avec le tunnel :

```bash
python3 -m http.server 8010 --bind 127.0.0.1
```

Dans un autre terminal, lancer un tunnel temporaire :

```bash
npx --yes localtunnel --port 8010 --local-host 127.0.0.1
```

Le tunnel affiche une URL publique de type :

```text
https://<nom-temporaire>.loca.lt
```

Tester systématiquement les pages utiles avant de communiquer l’URL :

```bash
curl -L --max-time 30 -s -o /tmp/preview-index.html -w '%{http_code} %{size_download}\n' \
  https://<nom-temporaire>.loca.lt/<dossier>/

curl -L --max-time 30 -s -o /tmp/preview-alternatives.html -w '%{http_code} %{size_download}\n' \
  https://<nom-temporaire>.loca.lt/<dossier>/alternatives.html
```

Les commandes doivent répondre `200` avec une taille non nulle. Vérifier aussi que le serveur Python local reçoit les requêtes.

Exemple historique de tunnel temporaire utilisé pour la prévisualisation du 24 juin 2026 :

```text
https://forty-flies-cross.loca.lt/miweb-offre-mutualisee-listes-diffusion-2026-condensee/
https://forty-flies-cross.loca.lt/miweb-offre-mutualisee-listes-diffusion-2026-longue/
```

Validation iPhone hors réseau local du 25 juin 2026 :

- serveur local : `python3 -m http.server 8010 --bind 127.0.0.1` ;
- tunnel public temporaire : `npx --yes localtunnel --port 8010 --local-host 127.0.0.1` ;
- chemins validés sur iPhone : `miweb-offre-mutualisee-listes-diffusion-2026-condensee/#slide-06` et `miweb-offre-mutualisee-listes-diffusion-2026-longue/#slide-06` ;
- objectif du test : vérifier la navigation par swipe horizontal des jeux 5 et 6 avant généralisation aux variantes 1 à 4 et push.

Points de vigilance :

- l’URL `loca.lt` est temporaire et reste active seulement tant que le serveur local et le tunnel restent ouverts ;
- ce tunnel n’est pas une preuve de publication GitHub Pages ;
- si un tunnel Cloudflare rapide renvoie `404` sans requête visible dans le serveur Python, ne pas le communiquer : relancer le tunnel ou utiliser `localtunnel`.

## Git et publication

Avant commit :

```bash
git status --short
git diff --stat
git diff -- DEMARCHE-VERSIONS.md README.md GUIDE-REGENERATION-SITES-SLIDES.md index.html published-versions.json <dossier>/slides.json <dossier>/build.py
```

Ne pas ajouter :

- `.DS_Store` ;
- `__pycache__/` ;
- captures temporaires ;
- caches de tests ;
- sorties locales non liées à la variante.

Après push GitHub Pages, vérifier l’URL publique :

```text
https://alexandra-guiderdoni.github.io/slides-miweb/<dossier>/
https://alexandra-guiderdoni.github.io/slides-miweb/<dossier>/alternatives.html
```

Pour éviter un push silencieux bloqué par une invite Git, pousser avec :

```bash
scripts/push-pages.sh
```

Ne pas considérer le push comme preuve suffisante. Après GitHub Pages, ouvrir ou vérifier les URL publiques du jeu et de ses alternatives.

## Checklist finale

- [ ] Le dossier de variante est autonome.
- [ ] Les images validées sont dans `assets/slides/`.
- [ ] `slides.json` contient une entrée par slide.
- [ ] Une passe `alt-text` a été faite sur les alternatives courtes de `slides.json`.
- [ ] Pour une série Opquast, les quatre slides étalons ont été validées avant la rédaction complète.
- [ ] Pour une série Opquast essentielle, chaque image est une slide complète générée avec ImageGen, texte compris, sans composition après génération.
- [ ] Pour une série Opquast essentielle, les règles citées sur chaque slide correspondent au storyboard validé.
- [ ] Pour une série Opquast essentielle, les prompts complets et leurs critères de rejet sont conservés dans `source/prompts/`.
- [ ] Pour une série Opquast essentielle, chaque image a été contrôlée en résolution originale et comparée à sa liste blanche.
- [ ] Pour une série Opquast, `scripts/check_notes_orales_opquast.py <dossier>` passe.
- [ ] Chaque image a un `alt`, une `description`, des `textes_visibles` et un `message`.
- [ ] `build.py` a été lancé.
- [ ] Le build ordinaire n’a pas publié l’accueil racine.
- [ ] `alternatives.html` et `alternatives.md` existent.
- [ ] Le ZIP contient les images et `alternatives.md`.
- [ ] `scripts/validate_variant.sh <dossier>` passe, ou l’écart réseau sandbox est documenté.
- [ ] `publish_variant.py` a été lancé après les vérifications.
- [ ] `published-versions.json` contient la nouvelle variante.
- [ ] L’accueil racine liste la nouvelle variante.
- [ ] Le README racine liste le jeu si c’est un support public durable.
- [ ] V1, V2, V3 et V4 n’ont pas été modifiées.
- [ ] Les Markdown modifiés passent `check-accents.sh`.
- [ ] Les URL GitHub Pages du jeu et des alternatives ont été vérifiées après push.
