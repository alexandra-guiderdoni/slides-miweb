## INVARIANTS

- working directory : /Users/alex/Claude/projets-heberges/slides-miweb
- branch : main ; distant origin/main. Dernier commit avant cette clôture documentaire : 5165b28.
- Français et tiret simple dans les contenus éditoriaux et notes. Conserver les sources, distinctions alt/description/transcription/notes et les générateurs autonomes.
- Le gel d’octobre a été levé pour la reprise autorisée de l’issue #15 ; ce chantier est terminé. Toute nouvelle correction demande un périmètre explicite.
- Le propriétaire demande une prise en charge autonome des points autorisés, sans validation répétée.
- Préserver les branches et worktrees historiques ; aucun nettoyage de ceux-ci n’est demandé. L’accueil est publié uniquement par publish_variant.py.

## STATE

- [x] completed : 132 slides e-commerce livrées ; 74 PNG corrigés, 25 QCM revus, diagnostics T0/T1 harmonisés. Commits fdd7344, c139982 et 5165b28 poussés sur main.
- [x] completed : 138 fichiers publics identiques aux locaux, y compris les deux ZIP ; site disponible.
- [x] completed : revue ShipGuard, seul écart faible (glyphes du storyboard 070) corrigé et comparé sur les 132 listes.
- [x] completed : réception Codex indépendante sur écran des 74 PNG modifiés + 082/083/087, couvrant les 25 paires QCM ; aucun défaut majeur ou bloquant relevé.
- [x] completed : clôture de l’issue #15 et harmonisation documentaire demandées par le propriétaire dans son « go » après la question sur l’issue et les MD structurants.
- [~] in progress : aucune production d’image ni modification du lecteur.
- [ ] pending : deux réserves faibles conservées (047, multiplicité documentaire des signes moins/plus ; 091, ambiguïté possible de « origines distinctes »). Vidéoprojection non testée. Aucun nouveau chantier lancé pour ces points.

## DECISIONS

- Clôturer le lot livré avec ses réserves explicites, sans transformer la vidéoprojection non effectuée en contrôle réussi.
- Préserver les rapports historiques et ajouter des renvois vers l’état courant ; les anciens verdicts VALIDEE_PRODUCTION ne sont pas une réception actuelle.
- Ne pas régénérer d’image pour cette clôture documentaire. Les réponses restent publiques ; T0 sert d’amorçage, T1 - T0 ne suffit pas à prouver un apprentissage.
- Deux ZIP sous 100 Mio : slides 1-66 (59,43 Mio) et 67-132 (69,65 Mio). Les alternatives courantes sont embarquées.

## ARTIFACTS

- README.md, AGENTS.md, DEMARCHE-VERSIONS.md, GUIDE-REGENERATION-SITES-SLIDES.md : procédures et état courant harmonisés.
- ecommerce-opquast-v5/README.md et source/reviews/README.md : entrées de livraison et périmètre des revues historiques actualisés.
- ecommerce-opquast-v5/source/corrections/README.md : journal et état final ; arbitrages-finitions.md et rapports antérieurs reliés à la réception actuelle.
- ecommerce-opquast-v5/source/corrections/reception-visuelle-independante-2026-11-02.md et .json : rapport indépendant intact, 74 lignes et empreintes.
- visual-tests/_results/audit-results.json et rapport de résolution : trace ShipGuard du commit fdd7344.
- Sources, PNG, HTML, ZIP, catalogue et accueil inchangés par cette dernière passe documentaire.

## ERRORS FIXED

- Les anciens documents présentaient encore le chantier comme reporté, les PNG gelés et la réception manquante ; état remplacé par la livraison du 2 novembre et ses limites.
- Écart de la Vue 070 : ? et ! ajoutés à la liste du storyboard ; égalité exacte des 132 listes vérifiée après correction.
- Les deux réserves faibles de réception restent des réserves ; aucun essai de projection ni audit normatif externe exhaustif n’est inventé.

## NEXT

1. Pour connaître le SHA documentaire final et l’état distant, vérifier git status et git log ; ce contexte appartient au commit de clôture.
2. Si une nouvelle correction est demandée, lire le README et les deux réserves dans le rapport indépendant, puis borner le changement. Aucun travail restant n’est lancé automatiquement.
3. Conserver les rapports historiques et les règles de variante. Refaire seulement les contrôles justifiés par une modification future.
