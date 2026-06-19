# Objectifs 2030 - accessibilité numérique

> README causal — 2026-06-19

## Site public [IC]

- Accueil GitHub Pages : <https://alexmacapple.github.io/miweb-objectifs-2030/>
- Version 1 : <https://alexmacapple.github.io/miweb-objectifs-2030/miweb-objectifs-2030-v1/>
- Alternatives textuelles : <https://alexmacapple.github.io/miweb-objectifs-2030/miweb-objectifs-2030-v1/alternatives.html>

## Pourquoi ce projet existe [IC]

Ce dépôt publie une version web, accessible et partageable des slides « Objectifs 2030 - accessibilité numérique » pour MiWeb, juin 2026.

Le problème initial n’était pas de produire une nouvelle note : les slides finales existent déjà sous forme d’images PNG. Le besoin était de rendre ces visuels consultables sans outil bureautique, navigables au clavier, exploitables avec des technologies d’assistance et partageables via une URL stable.

Le dépôt conserve donc une séparation nette entre :

- les images finales des slides ;
- les alternatives textuelles courtes et longues ;
- le générateur statique ;
- la publication GitHub Pages.

## Pourquoi maintenant, pourquoi cette approche [IC]

**Kairos** : les slides finales relues SM du 19 juin 2026 sont disponibles, et le dépôt GitHub Pages `Alexmacapple/miweb-objectifs-2030` est prêt à héberger une version publique.

**Nécessitation** : GitHub Pages impose une sortie statique. Le DSFR impose des composants HTML structurés. L’accessibilité impose une consultation indépendante des images. Ces contraintes conduisent à une architecture simple : source JSON, génération HTML statique, pages dédiées aux alternatives et contrôles natifs.

Cette approche évite un backend, limite la surface technique et permet de versionner les futures variantes dans des répertoires dédiés, comme `miweb-objectifs-2030-v1/`.

## Comment le projet est construit [IC]

**Pattern** : site statique généré depuis une source structurée, avec une version publiée par répertoire.

**Composants** :

- `index.html` — page racine DSFR légère listant les versions disponibles ;
- `miweb-objectifs-2030-v1/slides.json` — source unique des titres, images, textes alternatifs et messages ;
- `miweb-objectifs-2030-v1/build.py` — générateur Python standard pour reconstruire les pages et le ZIP ;
- `miweb-objectifs-2030-v1/index.html` — diaporama DSFR accessible avec pagination, mode toutes les slides et plein écran ;
- `miweb-objectifs-2030-v1/alternatives.html` — lecture continue des alternatives textuelles ;
- `miweb-objectifs-2030-v1/accessibilite.html` — statut d’accessibilité minimal ;
- `miweb-objectifs-2030-v1/assets/slides/` — 10 PNG finaux relus ;
- `miweb-objectifs-2030-v1/tests/` — tests de contrat sur les points d’accessibilité structurants ;
- `prompt-site-dsfr-github-pages.md` et `goal-site-dsfr-github-pages.md` — cadrage de réalisation et définition du done.

## Générer et vérifier [IC]

Depuis la racine du dépôt :

```bash
python3 miweb-objectifs-2030-v1/build.py
python3 -m unittest discover -s miweb-objectifs-2030-v1/tests
npx --yes html-validate miweb-objectifs-2030-v1/index.html miweb-objectifs-2030-v1/alternatives.html miweb-objectifs-2030-v1/accessibilite.html index.html
npx --yes vnu-jar --errors-only miweb-objectifs-2030-v1/index.html miweb-objectifs-2030-v1/alternatives.html miweb-objectifs-2030-v1/accessibilite.html index.html
```

Pour tester localement :

```bash
python3 -m http.server 4173
```

Puis ouvrir :

```text
http://127.0.0.1:4173/miweb-objectifs-2030-v1/
```

## Ce qui reste non résolu [IC]

**Exclusions assumées** :

- Le site ne remplace pas la note source et ne reformule pas librement le fond des slides.
- Le site ne revendique pas une conformité RGAA officielle complète : les tests automatisés et pré-audits ne remplacent pas une revue humaine des 106 critères.
- La page `accessibilite.html` reste volontairement minimale tant qu’un audit formel n’a pas produit de déclaration réglementaire.

**Dettes tracées** :

- Le choix `role="figure"` sur les figures légendées répond au contrôle RGAA 1.9 attendu par le pré-audit, mais Nu/W3C le signale comme rôle redondant en avertissement informatif.
- Les futures versions devront être ajoutées dans de nouveaux répertoires versionnés et référencées depuis la page racine.
- Les alternatives longues doivent rester vérifiées humainement contre les PNG si le contenu visuel évolue.
