# AGENTS.md - recette ShipGuard propre

## Mission

Ce dossier est un harnais propre pour retester ShipGuard sur le site statique
MiWeb après clean install.

## Règles locales

- Répondre et documenter en français.
- Ne pas recopier les résultats de `visual-tests-old/` dans ce dossier.
- Les fichiers `_results/` doivent provenir des commandes relancées dans cette
  recette.
- Les blocages à remonter concernent ShipGuard, Codex, Claude ou leurs
  contrats d'installation, pas le workflow personnel d'Alex.
- Ne pas faire de commit pendant la recette.

## Vérifications attendues

```bash
node visual-tests/review-smoke-test.mjs --port=23101
node visual-tests/monitor-smoke-test.mjs --port=23102
node visual-tests/sg-record.mjs --check
node visual-tests/build-review.mjs --serve --port=23113
```
