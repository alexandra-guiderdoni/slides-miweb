# Architecture - publication des jeux de slides

Ce document donne une vue d’architecture légère du dépôt. Il sert à réduire les ambiguïtés pour les humains et les LLM qui doivent créer, vérifier ou publier un nouveau jeu de slides.

## Sources lues

- `AGENTS.md` : règles projet, invariants et interdits.
- `README.md` : entrée courte et chemin standard.
- `DEMARCHE-VERSIONS.md` : procédure opérationnelle.
- `GUIDE-REGENERATION-SITES-SLIDES.md` : mode opératoire complet.
- `matrice-slide-ai/README.md` : rôle de la matrice.
- `matrice-slide-ai/MODE-OPERATOIRE.md` : procédure propre à la matrice.
- `matrice-slide-ai/create_variant.py` : création d’un jeu autonome.
- `matrice-slide-ai/publish_variant.py` : publication sur l’accueil racine.
- `matrice-slide-ai/tests/test_matrix_workflow.py` : contrats de création, autonomie et publication séparée.

## Périmètre

Le système en scope est le dépôt `slides-miweb`. Il publie des jeux de slides web statiques, accessibles, autonomes et comparables sur GitHub Pages.

Sont hors scope :

- GitHub Pages comme infrastructure externe ;
- les sources éditoriales amont ;
- les outils de génération d’images ;
- les PRD, prompts et goals historiques dans `docs/`, qui servent de contexte mais pas de procédure active.

## C1 - Contexte

```text
Alex / contributeur
  prépare images, storyboard et transcriptions
        |
        v
[Dépôt slides-miweb]
  crée, vérifie et publie des jeux de slides statiques
        |
        v
GitHub Pages
  sert l’accueil racine et les jeux publiés
        |
        v
Public
  consulte les présentations, alternatives et pages d’accessibilité
```

## C2 - Containers

Ici, un container C4 désigne une grande brique logique, pas un container Docker.

| Container | Technologie | Responsabilité | Données ou sorties |
|---|---|---|---|
| Accueil racine | HTML statique | Liste les jeux publiés et leurs liens | `index.html`, `published-versions.json` |
| Jeu de slides autonome | HTML, CSS, JS, JSON, Python | Sert une présentation, ses alternatives, sa page accessibilité et ses archives ZIP | `<dossier-jeu>/`, `slides.json`, `assets/slides/`, `assets/downloads/` |
| Matrice | Python, fichiers exemples, tests | Crée le squelette autonome des futurs jeux | `matrice-slide-ai/` |
| Générateur du jeu | Python copié dans chaque jeu | Génère les pages et les archives ZIP du jeu seulement | `<dossier-jeu>/build.py` |
| Publication racine | Python | Met à jour le catalogue et régénère l’accueil racine après vérification | `matrice-slide-ai/publish_variant.py` |
| Validation | Shell, unittest, validateurs HTML | Vérifie le contrat du jeu et les pages générées | `scripts/validate_variant.sh`, `tests/` |
| GitHub Pages | Service externe | Héberge les fichiers statiques de la branche publiée | URL publique |

## Flux - publier un nouveau jeu

```text
1. Préparer les images et le storyboard
2. Créer le dossier autonome
   python3 matrice-slide-ai/create_variant.py ...
3. Compléter <dossier-jeu>/slides.json
4. Générer le jeu
   python3 <dossier-jeu>/build.py
5. Vérifier le jeu
   scripts/validate_variant.sh <dossier-jeu>
6. Publier sur l’accueil racine
   python3 matrice-slide-ai/publish_variant.py --slug <dossier-jeu>
7. Revérifier le jeu
   scripts/validate_variant.sh <dossier-jeu>
8. Inspecter le diff
   git status --short
   git diff -- README.md DEMARCHE-VERSIONS.md GUIDE-REGENERATION-SITES-SLIDES.md index.html published-versions.json <dossier-jeu>
9. Pousser
   scripts/push-pages.sh
10. Vérifier l’URL GitHub Pages du jeu et de ses alternatives
```

## Invariants

- Un jeu publié doit rester autonome.
- `create_variant.py` crée un dossier, mais ne publie jamais.
- `<dossier-jeu>/build.py` génère seulement le dossier du jeu.
- `publish_variant.py` est le seul point d’entrée pour modifier `published-versions.json` et `index.html` racine.
- Une version publiée ne sert pas de brouillon pour une variante suivante.
- Une image ne doit pas être publiée sans alternative textuelle.
- Les HTML générés, le Markdown généré et le ZIP ne se corrigent pas à la main.
- `docs/prd/`, `docs/prompts/` et `docs/goals/` sont historiques ; les documents racine et la matrice active priment.

## Contrats du lecteur et des archives

Dans la matrice actuelle et le jeu e-commerce, `slides.json` sépare description, transcription et discours oral. Le lecteur expose la description avec les textes visibles et le discours dans deux accordéons ; les alternatives HTML et Markdown conservent aussi la transcription. Les panneaux restent visibles sans JavaScript. Les corrections d’historique des liens d’évitement ont été propagées aux 32 générateurs ; les autres améliorations ne sont pas rétroactivement appliquées à tous les anciens jeux.

Le découpage `download_parts` est une métadonnée du jeu. Chaque générateur qui le prend en charge produit ses archives de façon autonome ; la publication racine vérifie les parties déclarées et construit leurs liens. Le détail du contrat est dans le [guide](../GUIDE-REGENERATION-SITES-SLIDES.md#archives-en-plusieurs-parties).

L’état du chantier e-commerce et la reprise différée des images sont centralisés dans le [README racine](../README.md#état-et-reprise-du-chantier-e-commerce) et l’[issue #15](https://github.com/alexandra-guiderdoni/slides-miweb/issues/15).

## Limites

Ce schéma ne détaille pas l’intérieur de `build.py`, ni la structure HTML générée. Pour modifier le comportement du diaporama, utiliser les tests du jeu concerné et le guide complet.
