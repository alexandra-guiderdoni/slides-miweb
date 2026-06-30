# PRD-008 : Parser le rapport visuel francisé

**Statut** : Implémenté localement
**Date** : 2026-07-01
**Auteur** : Alex
**Source** : ShipGuard `SG-Z5-007`, inspection de `visual-tests/build-review.mjs` et `visual-tests/_results/report.md`

---

## Vision

Le quoi : le tableau de bord ShipGuard doit comprendre le rapport Markdown visuel
dans le format réellement produit aujourd'hui, en français, quand
`visual-results.json` est absent ou invalide.

Le pourquoi : `visual-results.json` reste la source structurée prioritaire, mais
`report.md` est le repli lisible par humain. Un repli qui ne comprend pas le
format courant transforme une source utile en illusion de robustesse : les
statuts de lignes peuvent remonter, tandis que la synthèse, la date et la durée
restent perdues.

Le comment : renvoyé au Plan d'implémentation Superpowers.

## Exemple bout-en-bout (réel)

Le smoke test `visual-tests/report-parser-smoke-test.mjs` crée un dossier
temporaire `visual-tests/_results/` contenant seulement un `report.md` avec :

```markdown
# Rapport visuel ShipGuard - 2026-06-30 20:49:05

## Synthèse
- Tests : 28 exécutés, 28 réussis, 0 échecs, 0 obsolète, 0 erreurs, 0 ignoré
- Durée : 35.8s
- Base URL : http://127.0.0.1:8001
```

`visual-results.json` n'existe pas encore ou est invalide. L'utilisateur lance :

```bash
node visual-tests/build-review.mjs
```

Résultat attendu : `review.html` et `visual-results.json` sont reconstruits sans
perdre la synthèse du rapport Markdown. La synthèse contient `28` tests, `28`
réussites, `0` échec, `0` obsolète, `0` erreur, `0` ignoré, une durée de
`35800` millisecondes et une date de dernier run `2026-06-30 20:49:05`.

---

## Contexte

ShipGuard signale `SG-Z5-007` sur `visual-tests/build-review.mjs:158`. Le code
local montre que `parseVisualResults()` lit d'abord `visual-results.json`, puis
`parseReport()` sert de repli historique.

Le rapport Markdown courant est francisé :

```markdown
# Rapport visuel ShipGuard - 2026-06-30 20:49:05
- Tests : 28 exécutés, 28 réussis, 0 échecs, 0 obsolète, 0 erreurs, 0 ignoré
```

Mais `parseReport()` cherche encore :

```js
/Tests:\s*(\d+)\s*run,\s*(\d+)\s*pass,\s*(\d+)\s*fail/
/# Visual Report — (\S+ \S+)/
```

Les statuts du tableau Markdown restent partiellement lus car ils utilisent les
valeurs `PASS`, `FAIL`, `ERROR`, `STALE` et `SKIPPED`. La synthèse, elle, est
ignorée.

## Problème

Le repli Markdown n'est plus aligné avec le format émis par le runner visuel. En
mode normal, le JSON masque le problème. En mode dégradé ou lors d'une reprise
depuis un `report.md` seul, le dashboard perd la synthèse et la date du run.

## Solution

Étendre `parseReport()` pour supporter explicitement deux formats :

- le format historique anglais ;
- le format français actuel.

Le format français doit extraire au minimum :

- `total`, `pass`, `fail`, `stale`, `error`, `skipped` ;
- `durationMs` depuis `Durée : Ns` ;
- `lastRun` depuis le titre `Rapport visuel ShipGuard - ...` ;
- `baseUrl` depuis `Base URL : ...` quand présent.

La priorité reste inchangée : `visual-results.json` prévaut sur `report.md`
quand il est valide.

## Options évaluées

### Option A (retenue) : rendre `parseReport()` bilingue et testé par fixture

**Avantages** :
- changement localisé dans `visual-tests/build-review.mjs` ;
- conserve la priorité du JSON structuré ;
- couvre le mode dégradé réel sans ajouter de dépendance ;
- vérifiable par un smoke test qui force l'absence de `visual-results.json`.

**Inconvénients** :
- ajoute des regex de compatibilité dans un fichier déjà dense ;
- doit maintenir deux formats tant que l'ancien format anglais reste accepté.

### Option B : supprimer le fallback Markdown et exiger le JSON

**Avantages** :
- contrat plus simple : une seule source machine ;
- moins de parsing fragile.

**Inconvénients** :
- dégrade la reprise depuis artefacts humains ;
- rend `report.md` moins utile alors qu'il est déjà produit ;
- ne répond pas à l'alerte ShipGuard, qui vise précisément le fallback.

### Option C : convertir `report.md` en JSON dans une étape séparée

**Avantages** :
- sépare conversion et rendu du dashboard ;
- pourrait servir à d'autres outils plus tard.

**Inconvénients** :
- crée un flux supplémentaire pour un bug faible et localisé ;
- augmente le nombre d'artefacts à maintenir ;
- n'apporte pas de bénéfice immédiat au dashboard existant.

## Décision

Retenir l'option A.

Le bug est un désalignement de parsing, pas un problème d'architecture de
reporting. La correction minimale robuste consiste à accepter le format
français actuel dans le fallback existant, avec un test qui prouve le cas sans
`visual-results.json`.

Plan associé :

`docs/superpowers/plans/2026-07-01-parser-rapport-visuel-francise.md`

## Plan d'implémentation

1. Ajouter un smoke test dédié qui crée un fixture `visual-tests` temporaire,
   écrit un `report.md` français et ne crée pas `visual-results.json`.
2. Lancer ce test et vérifier qu'il échoue sur la durée ou la date du run.
3. Étendre `parseReport()` pour reconnaître la synthèse française, la date, la
   durée et la base URL.
4. Relancer le smoke test dédié, puis `review-smoke-test.mjs`.
5. Lancer `node visual-tests/build-review.mjs` sur le dépôt réel pour confirmer
   que la priorité JSON reste intacte.
6. Vérifier le diff, mettre à jour `CHANGELOG.MD`, puis committer localement
   sans push.

## Métriques de succès

- Avec `visual-results.json` absent, un `report.md` français de fixture produit
  un `visual-results.json` avec `summary.duration_ms === 35800`.
- Le HTML généré contient `2026-06-30 20:49:05` comme dernier run.
- Les statuts `PASS`, `FAIL`, `ERROR`, `STALE` et `SKIPPED` du tableau Markdown
  restent mappés sur les manifests.
- `node visual-tests/review-smoke-test.mjs --debug` passe.
- `node visual-tests/build-review.mjs` passe dans le dépôt réel.
- Aucun changement de priorité : un `visual-results.json` valide continue de
  prévaloir sur `report.md`.

## Changelog

| Date | Auteur | Changement |
|------|--------|------------|
| 2026-07-01 | Alex + Codex | Implémentation locale du PRD |
| 2026-07-01 | Alex + Codex | Création du PRD |
