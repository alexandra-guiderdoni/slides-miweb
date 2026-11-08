# Objectifs 2030 - accessibilité numérique

Site public : <https://alexandra-guiderdoni.github.io/slides-miweb/>

Dépôt GitHub : <https://github.com/alexandra-guiderdoni/slides-miweb>

Ce dépôt publie des jeux de slides web statiques, accessibles et comparables. Il contient les variantes MiWeb « Objectifs 2030 - accessibilité numérique » et des supports thématiques produits avec le même modèle.

![Flux de publication : contribuer, créer un jeu autonome, vérifier, publier l’accueil racine puis servir le public avec GitHub Pages.](flux-de-publication.png)

## État et reprise du chantier e-commerce

Au 2 novembre 2026, le jeu [E-commerce selon Opquast V5](https://alexandra-guiderdoni.github.io/slides-miweb/ecommerce-opquast-v5/) est livré sur `main` et GitHub Pages : 132 slides, dont 74 images corrigées. Les 25 QCM ont été revus et les diagnostics T0/T1 harmonisés. La livraison comprend les commits `fdd7344`, `c139982` et `5165b28` ; 138 fichiers publics ont été comparés aux fichiers locaux, tous identiques.

L’[issue #15](https://github.com/alexandra-guiderdoni/slides-miweb/issues/15) est clôturée à la demande du propriétaire après validation du rendu et [réception visuelle indépendante sur écran](ecommerce-opquast-v5/source/corrections/reception-visuelle-independante-2026-11-02.md) : les 74 images corrigées et trois compléments ont été examinés en résolution originale, couvrant les 25 paires QCM. Aucun défaut graphique majeur ou bloquant relevé. La revue ShipGuard et les contrôles techniques sont consignés dans [le journal du lot](ecommerce-opquast-v5/source/corrections/README.md).

Deux réserves faibles sont conservées : en 047, la multiplicité des signes moins/plus n’est pas entièrement détaillée dans la liste canonique ; en 091, « origines distinctes » peut prêter à une lecture ambiguë, sans invalider la réponse C. Aucun essai sur vidéoprojecteur n’a été réalisé. La clôture ne transforme pas ces limites en contrôles réussis et ne déclenche aucune nouvelle régénération.

Les deux ZIP publiés couvrent les slides 1 à 66 (59,43 Mio) et 67 à 132 (69,65 Mio), avec les alternatives courantes dans chaque archive. Les réponses restent publiques et le diagnostic T0 sert d’amorçage.

Références historiques : [audit initial](audits/revue-2026-10-28-ecommerce-opquast-v5-f9b3ae1.md), [corrections du 29 octobre](audits/corrections-2026-10-29-ecommerce-sans-png.md), [portée des anciennes revues d’image](ecommerce-opquast-v5/source/reviews/README.md). Ces rapports conservent leurs constats datés ; l’état courant est celui décrit ci-dessus.

## Règle à retenir

La description détaillée, la transcription descriptive et le discours oral sont trois champs obligatoires et distincts de `slides.json`. La présentation affiche deux accordéons : description détaillée et discours oral. Dans la matrice actuelle, la description donne aussi les textes affichés dans l’image ; la transcription reste disponible dans les alternatives HTML et Markdown. Les anciens jeux conservent leur générateur. Les liens HTTPS des notes doivent rester cliquables ; la CSP statique utilise des empreintes SHA-256 et le retour navigateur restaure le mode « toutes les slides ».

Un jeu de slides est un dossier autonome. Il contient ses images, ses alternatives textuelles, son storyboard source, son générateur et ses archives ZIP.

La génération du jeu et la publication sur l’accueil racine sont deux actions séparées :

- `python3 <dossier-jeu>/build.py` génère seulement le dossier du jeu ;
- `python3 matrice-slide-ai/publish_variant.py --slug <dossier-jeu>` met à jour `published-versions.json` et `index.html` racine.

Le titre interne vient de `site_title` dans `variant.json`. Si la tuile d’accueil doit porter un libellé différent, renseigner `catalog_label` dans ce même fichier : `publish_variant.py` l’utilise sans renommer la présentation.

Ne pas modifier une version déjà publiée pour fabriquer la suivante. Créer un nouveau dossier avec la matrice.

## Publier un nouveau jeu de slides

Depuis la racine du dépôt, créer le dossier autonome :

```bash
python3 matrice-slide-ai/create_variant.py \
  --slug nouveau-jeu \
  --title "Titre public" \
  --storyboard chemin/storyboard.md \
  --slides-dir chemin/assets/slides
```

Si les images source sont préfixées, déclarer le préfixe au lieu de les renommer :

```bash
python3 matrice-slide-ai/create_variant.py \
  --slug nouveau-jeu \
  --title "Titre public" \
  --storyboard chemin/storyboard.md \
  --slides-dir chemin/assets/slides \
  --slide-prefix prefixe-
```

Compléter ensuite `nouveau-jeu/slides.json`. Ce fichier est la source canonique des titres, alternatives courtes, descriptions complètes, textes visibles et messages.

Avant de générer, refaire une passe avec le skill `alt-text` sur les alternatives courtes : chaque `alt` doit remplacer l’information utile, rester court, éviter les formules comme « image de » et ne pas inventer d’information absente du visuel ou du contexte.

Optimiser les images avec `scripts/optimiser-images.sh nouveau-jeu`, puis lancer :

```bash
python3 nouveau-jeu/build.py
scripts/validate_variant.sh nouveau-jeu
```

Publier seulement après vérification :

```bash
python3 matrice-slide-ai/publish_variant.py --slug nouveau-jeu
scripts/validate_variant.sh nouveau-jeu
```

Avant de pousser :

```bash
git status --short
git diff -- README.md DEMARCHE-VERSIONS.md GUIDE-REGENERATION-SITES-SLIDES.md index.html published-versions.json nouveau-jeu
scripts/push-pages.sh
```

Après le push, vérifier l’URL publique :

```text
https://alexandra-guiderdoni.github.io/slides-miweb/nouveau-jeu/
```

## Contrat d’un jeu publié

Chaque jeu publié doit contenir :

- `index.html` : présentation web et mode projection ;
- `alternatives.html` : alternatives textuelles complètes ;
- `alternatives.md` : version Markdown des alternatives ;
- `accessibilite.html` : état d’accessibilité du support ;
- `assets/slides/` : images publiées ;
- `assets/downloads/` : archive ou parties ZIP générées ;
- `source/` : storyboard et sources utiles ;
- `slides.json` : transcriptions et messages ;
- `build.py` : générateur autonome ;
- `tests/` : tests de contrat.

Le HTML généré, le Markdown généré et le ZIP ne se corrigent pas à la main. Corriger la source, puis relancer `build.py`.

## Points de vigilance

- Ne pas publier d’image sans alternative textuelle.
- Ne pas inventer de chiffre, seuil, engagement, audit ou conformité absent de la source.
- Ne pas déclarer une conformité RGAA sans audit dédié.
- Ne pas faire dépendre un jeu publié de `matrice-slide-ai/` à l’exécution.
- Ne pas modifier `PUBLISHED_VERSIONS`, `LATEST_VERSION_SLUG` ou `ROOT_CATALOG_BOOTSTRAP` dans un `build.py` pour publier l’accueil.
- Relancer `build.py` après `scripts/optimiser-images.sh`, afin de reconstruire le ZIP.
- Conserver la navigation clavier, le mode projection, les alternatives et le swipe horizontal tactile.

## Versions publiées

- Version 1 : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-objectifs-2030-v1/>
- Version 2 : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-objectifs-2030-v2/>
- Version 3 : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-objectifs-2030-v3/>
- Version 4 : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-objectifs-2030-v4/>
- Offre mutualisée de listes de diffusion, version condensée : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-offre-mutualisee-listes-diffusion-2026-condensee/>
- Offre mutualisée de listes de diffusion, version longue : <https://alexandra-guiderdoni.github.io/slides-miweb/miweb-offre-mutualisee-listes-diffusion-2026-longue/>
- SPAN / PAN - accessibilité numérique : <https://alexandra-guiderdoni.github.io/slides-miweb/span-pan/>
- Mise en gouvernance du SPAN : <https://alexandra-guiderdoni.github.io/slides-miweb/mise-en-gouvernance-du-span/>
- Checklist SPAN opérationnel : <https://alexandra-guiderdoni.github.io/slides-miweb/checklist-span-operationnel/>
- Émojis accessibles - réseaux sociaux : <https://alexandra-guiderdoni.github.io/slides-miweb/emojis-accessibles-reseaux-sociaux/>
- Des liens accessibles : <https://alexandra-guiderdoni.github.io/slides-miweb/des-liens-accessibles/>
- Partie IV - Réseaux sociaux accessibles - IGPDE : <https://alexandra-guiderdoni.github.io/slides-miweb/publier-de-facon-accessible-sur-les-reseaux-sociaux-v5/>
- Opquast - la qualité web qui se vérifie : <https://alexandra-guiderdoni.github.io/slides-miweb/opquast-miweb/>
- Projets et livrables selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/projets-livrables-opquast-v5/>
- Sécurité selon Opquast V5 - version 4 : <https://alexandra-guiderdoni.github.io/slides-miweb/securite-opquast-v5-v4/>
- Serveur et Performance selon Opquast - V2 : <https://alexandra-guiderdoni.github.io/slides-miweb/performance-opquast-v5-v2/>
- Newsletter et qualité numérique selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/newsletter-opquast-v5/>
- Images et médias selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/images-medias-opquast-v5/>
- Données personnelles selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/donnees-personnelles-opquast-v5/>
- Internationalisation selon Opquast V5 - V2 : <https://alexandra-guiderdoni.github.io/slides-miweb/internationalisation-opquast-v5-v2/>
- Nouveautés d’Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/nouveautes-opquast-v5/>
- Navigation Opquast V5 - série 360 : <https://alexandra-guiderdoni.github.io/slides-miweb/navigation-opquast-v5-360/>
- Contenus Opquast V5 - série 360 : <https://alexandra-guiderdoni.github.io/slides-miweb/contenus-opquast-v5-360/>
- Partie III - Web accessible - TP - IGPDE : <https://alexandra-guiderdoni.github.io/slides-miweb/web-accessible-points-de-controle-rapides/>
- Partie I - Accessibilité et cadre légal - IGPDE : <https://alexandra-guiderdoni.github.io/slides-miweb/partie-1-accessibilite-numerique-et-cadre-legal/>
- Partie 0 - Introduction et idées reçues - IGPDE : <https://alexandra-guiderdoni.github.io/slides-miweb/introduction-et-idees-recues/>
- Partie II - Documents bureautiques accessibles - IGPDE : <https://alexandra-guiderdoni.github.io/slides-miweb/partie-2-documents-bureautiques-accessibles/>
- Liens et PDF selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/liens-et-pdf-opquast-v5/>
- Octobre, Web et accessibilité : <https://alexandra-guiderdoni.github.io/slides-miweb/accessibilite-web-octobre/>
- E-commerce selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/ecommerce-opquast-v5/>
- Formulaires selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/formulaires-opquast-v5/>
- Identification et contact selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/identification-contact-opquast-v5/>
- Présentation selon Opquast V5 : <https://alexandra-guiderdoni.github.io/slides-miweb/presentation-opquast-v5/>

Dernier jeu inscrit au catalogue : `presentation-opquast-v5/`.
Son storyboard, ses prompts et la planche de la série se trouvent dans `presentation-opquast-v5/source/`.
Le storyboard, les prompts et les vérifications de la série Liens et PDF se trouvent dans `liens-et-pdf-opquast-v5/source/`.

Accès directs :

- présentation plein écran : <https://alexandra-guiderdoni.github.io/slides-miweb/presentation-opquast-v5/?projection=1#slide-01>
- toutes les slides : <https://alexandra-guiderdoni.github.io/slides-miweb/presentation-opquast-v5/?slides=all#diaporama>
- alternatives textuelles et discours oral : <https://alexandra-guiderdoni.github.io/slides-miweb/presentation-opquast-v5/alternatives.html>
- page accessibilité : <https://alexandra-guiderdoni.github.io/slides-miweb/presentation-opquast-v5/accessibilite.html>

## Documents utiles

- `AGENTS.md` : règles projet pour les agents.
- `DEMARCHE-VERSIONS.md` : procédure courte de publication des variantes.
- `GUIDE-REGENERATION-SITES-SLIDES.md` : mode opératoire complet, avec contrôles et inspection locale.
- `docs/architecture.md` : vue d’architecture légère du dépôt et du flux de publication.
- `matrice-slide-ai/README.md` : fonctionnement de la matrice canonique.
- `docs/prd/` : cadrages fonctionnels historiques.
- `docs/prompts/` : prompts de génération et de correction conservés pour référence.
- `docs/goals/` : objectifs de chantier historiques.

En cas de tension, suivre d’abord les documents racine dans cet ordre : `AGENTS.md`, `README.md`, `DEMARCHE-VERSIONS.md`, puis `GUIDE-REGENERATION-SITES-SLIDES.md`. Les dossiers `docs/` servent de contexte historique.

## Développement local

Régénérer le dernier jeu du catalogue :

```bash
python3 formulaires-opquast-v5/build.py
```

Tester un jeu :

```bash
scripts/validate_variant.sh formulaires-opquast-v5
```

Servir le site localement :

```bash
scripts/serve-local.sh 8000
```

URL locale :

```text
http://127.0.0.1:8000/formulaires-opquast-v5/
```

Le script utilise les validateurs npm verrouillés à la racine. Si les dépendances ne sont pas installées, lancer `npm ci` depuis la racine du dépôt, puis relancer la validation.
