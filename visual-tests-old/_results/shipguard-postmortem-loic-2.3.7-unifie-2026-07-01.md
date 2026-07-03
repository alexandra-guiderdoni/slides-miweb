# Post-mortem unifié ShipGuard 2.3.7

Date : 2026-07-01

Destinataire : Loïc, pour amélioration générique du dépôt ShipGuard.

Périmètre : consolidation des retours de recette ShipGuard 2.3.7. Ce document
filtre volontairement les détails propres à un poste, un dépôt client ou une
configuration locale. Les points ci-dessous sont formulés comme contrats produit,
DX, testabilité ou traçabilité utiles pour ShipGuard lui-même.

## Message court à envoyer

```text
ShipGuard 2.3.7 est utilisable sur les flux principaux : smokes OK, review
visuelle complète OK, recorder preflight OK, Stop écrit un manifest.

Les priorités génériques restantes sont :
1. monitor live : empêcher agents.undefined et réconcilier r1:z1 avec z1 ;
2. runs visuels ciblés : préserver le scope dans le JSON et le dashboard ;
3. matching de "/" : éviter que la racine sélectionne toute la suite ;
4. routes non HTML : écrire skipped/uncovered avec une raison ;
5. recorder : prouver Check puis Stop en E2E avec assert_text dans le manifest ;
6. DX : clarifier skill slash-command versus commande shell native ;
7. dashboard : distinguer bugs actifs, historique, état done, source et fraîcheur du rapport.
```

## État validé
Les flux principaux sont bons : rapport visuel complet à `31/31` routes
réussies, sans échec, erreur, obsolescence ou route ignorée. Le rapport d'audit
régénéré indique `0` bug actif et un risque `0`.

Les smokes couverts sont ceux de la review, du monitor, de `sg-visual-fix` en
dry-run, de `sg-scout` offline, de `sg-improve` en dry-run et du rollback.

La seule nuance à conserver est la provenance : le rapport d'audit final a été
régénéré par réconciliation locale, faute d'entrypoint ShipGuard natif
exécutable depuis l'environnement agentique utilisé. Ce n'est pas un bug métier
du dépôt testé ; c'est un sujet de reproductibilité produit si ShipGuard veut
garantir le même usage hors slash-command interactive.

## P0 - Monitor live
### `agent-update` ne doit jamais produire `agents.undefined`
Constat générique : un endpoint monitor peut accepter un payload avec `id`,
répondre en succès, puis stocker l'agent sous une clé `undefined`.

Impact : le dashboard montre un agent fantôme, l'état monitor devient faux, et
les smokes peuvent passer si le cas testé utilise seulement `agent_id`.

Attendu : normaliser `id`, `agent_id` et `zone_id`, refuser tout update sans
identifiant normalisable, et ajouter un test qui échoue si une clé `undefined`
apparaît dans `agents`.

### `r1:z1` et `z1` doivent être réconciliés
Constat générique : les agents préremplis sous forme `r1:z1` / `r1:z2` peuvent
rester `pending` quand les updates arrivent sous `z1` / `z2`.

Impact : l'activité est reçue mais n'est pas rattachée à l'agent affiché.

Attendu : définir un identifiant canonique monitor, documenter les alias
acceptés, et tester le cas `start r1:z1` puis `update z1`.

## P1 - Runs visuels ciblés
### Le scope doit survivre au rebuild de la review
Constat générique : un run ciblé peut être correct dans son rapport immédiat
(`13/13` ou `4/4`), puis être réinterprété comme une suite globale après rebuild
de la review.

Impact : le dashboard peut afficher des tests hors scope comme `STALE` ou revenir
à un total global, ce qui brouille la validation réelle.

Attendu : persister `run_id`, `scope`, `selected_routes`, `selected_manifests`
et `uncovered_routes` dans `visual-results.json`, distinguer `selected_total`
et `full_suite_total`, afficher le type de run, et ne pas transformer une route
hors scope en `STALE` sans raison.

### La route `/` doit être un cas spécial
Constat générique : un matching par préfixe fait que `/` peut sélectionner tous
les manifests.

Impact : `--from-audit` ou `--from-process` peut relancer toute la suite alors
que seule la racine est impactée.

Attendu :

```text
"/" matches only the root page manifest
```

ou une règle différente, mais explicite et testée.

### Les routes non HTML doivent être tracées
Constat générique : une archive ZIP ou une route interne comme `/review.html`
n'a pas toujours de manifest visuel HTML, mais disparaît du JSON machine.

Impact : on ne distingue pas "non testable visuellement" de "oublié".

Attendu :

```text
route: /assets/downloads/file.zip
status: skipped
reason: non_html_asset
```

et :

```text
route: /review.html
status: uncovered
reason: no_visual_manifest
```

## P1 - Dashboard et audit
### Le dashboard doit séparer actif, historique et métadonnées
Constat générique : un identifiant de bug retiré de `bugs[]` peut rester dans
des champs historiques ou de provenance. Une recherche texte peut alors laisser
croire que le bug est encore actif.

Impact : perte de confiance dans le rapport ; confusion entre constat actif,
trace de régénération et historique.

Attendu : considérer `bugs[]` comme source canonique des constats actifs,
afficher les métadonnées historiques dans une zone séparée, et marquer les
constats corrigés ou archivés.

### La fraîcheur du rapport doit être visible
Constat générique : un dashboard peut afficher un ancien `audit-results.json`
alors que le code a changé ou que des corrections ont été faites.

Impact : l'utilisateur ne sait pas s'il regarde un audit frais ou un artefact
historique.

Attendu : afficher la date, le mode et la source du dernier audit, signaler si
le code a changé depuis la génération, et distinguer "audit absent", "audit
invalide", "audit à zéro bug" et "bugs trouvés".

### Besoins UX utiles
Ces points ne sont pas bloquants mais amélioreraient fortement le suivi :

- trier et filtrer le tableau par catégorie, par exemple `security`,
  `logic-error`, `type-mismatch` ;
- ajouter une case `done` locale pour marquer un point corrigé avant rerun ;
- permettre d'associer un commit de correction à un constat ;
- conserver le statut `done` séparément du résultat du dernier audit, pour ne
  pas confondre "corrigé localement" et "vérifié par rerun".

## P2 - Recorder
### `Check` doit être validé en E2E complet
Constat générique : `Stop` est validable en E2E et écrit un manifest. En
revanche, `Check` peut être prouvé en isolation sans que le flux complet prouve
que le manifest final contient une assertion.

Impact : la partie assertion humaine du recorder reste insuffisamment couverte.

Attendu : ajouter un test E2E officiel qui ouvre le recorder, clique `Check`,
clique `Stop`, vérifie que le manifest contient un `assert_text` ou équivalent,
et vérifie que le compteur console correspond au contrat YAML.

## P2 - DX et entrypoints
### Clarifier slash-command, skill et CLI
Constat générique : une commande comme `sg-ship` ou `/sg-code-audit` peut être
comprise comme une commande shell native alors qu'elle est exposée comme skill ou
slash-command dans certains runtimes.

Impact : un utilisateur peut croire lancer ShipGuard alors qu'il déclenche une
revue générique, ou ne régénère aucun artefact canonique.

Attendu : documenter quelles surfaces sont natives, fournir un entrypoint
reproductible pour générer `audit-results.json`, par exemple
`shipguard code-audit --report-only`, et indiquer dans le dashboard si le rapport
vient d'un vrai rerun ShipGuard, d'un fallback ou d'une régénération locale.

## À ne pas remonter comme bug ShipGuard

Les points suivants ne doivent pas être présentés comme bugs produit :

- absence de `node_modules` dans un dépôt consommateur ;
- blocage sandbox ou autorisation locale, sauf si la documentation ShipGuard
  promet un usage sans préciser ces droits ;
- résultats propres au contenu du dépôt testé ;
- absence de test réel d'écriture GitHub, de correction source automatique, ou
  d'écriture effective dans `.shipguard/` pendant cette recette ;
- correction locale prouvée sans rerun ShipGuard natif, sauf comme friction de
  traçabilité.

## Sources locales utilisées

- `visual-tests/_results/shipguard-postmortem-loic-2.3.7-final.md`
- `visual-tests/_results/shipguard-postmortem-loic-2.3.7-suite.md`
- `visual-tests/_results/shipguard-note-loic.md`
- `visual-tests/_results/audit-results.json`
- `visual-tests/_results/visual-results.json`
- `visual-tests/_results/report.md`
