## INVARIANTS

- Dépôt : `/Users/alex/Claude/projets-heberges/slides-miweb`, branche de livraison `main`, distant `origin/main`.
- Documentation en français ; uniquement le tiret simple dans les contenus éditoriaux et notes orales.
- Les images e-commerce restent gelées jusqu’à la reprise explicite du chantier, y compris leur optimisation.
- Préserver les branches de sauvegarde et worktrees existants ; leur présence ne signifie pas qu’ils sont à nettoyer.
- Publier l’accueil uniquement avec `matrice-slide-ai/publish_variant.py` ; utiliser `catalog_label` pour un libellé de tuile distinct.
- Corriger les sources puis générer ; ne pas éditer les HTML, alternatives ou ZIP générés à la main.
- Une extension ou un changement de structure devient une nouvelle variante autonome selon `AGENTS.md`.

## ÉTAT AU 29 OCTOBRE 2026

### Livré

- Jeu `ecommerce-opquast-v5/` : 132 slides, publié sur l’accueil et GitHub Pages.
- Publication initiale : `f9b3ae14297ef51cde4cdfc81b95dd191097ffa5` ; correctif après audit : `ce5bee7e9591f477e249c9cfb499562b3c171b2f`, poussé sur `main` et déployé.
- Correctif : navigation/historique dans les 32 générateurs ; lecteur e-commerce et matrice améliorés pour les textes des questions, le clavier, le focus, le zoom et le fonctionnement sans JavaScript ; archives et validateurs durcis.
- Textes associés repris : 120 alts, 132 notes (131 transitions et une conclusion), descriptions et métadonnées ciblées, relecture indépendante et correction des réserves.
- 132 PNG et champs `numero`, `titre`, `image`, `textes_visibles`, `transcription` inchangés par rapport à la base de correction.
- Validation du correctif : 419 tests Python réussis, 1 ignoré, validateurs HTML, recette navigateur ; génération reproductible. Après déploiement, 42 fichiers publics identiques aux locaux, dont les deux ZIP ; lien d’évitement retesté sur le site public depuis la slide 60.
- Documentation structurante actualisée dans le commit contenant ce contexte. Pour connaître le dernier SHA documentaire, utiliser Git plutôt que le SHA de contenu ci-dessus.

### Reporté

- Reprise souhaitée lundi 2 novembre 2026 pour terminer les slides, sur nouvelle instruction du propriétaire.
- [Issue #15](https://github.com/alexandra-guiderdoni/slides-miweb/issues/15) ouverte et alignée avec l’inventaire visuel détaillé : 4 fautes d’en-tête bloquantes, 2 majeurs d’illustration (017 et 070, coche à confirmer), finitions et révisions éditoriales/QCM.
- Les 25 paires QCM représentent 50 images à examiner, pas 50 régénérations déjà décidées. Le total des images à refaire dépend des arbitrages ; ne pas additionner les groupes qui se recoupent.
- Les réponses restent publiques. T0 sert d’amorçage ; le support n’est pas une évaluation confidentielle et T1 - T0 ne mesure pas à lui seul l’apprentissage.
- Aucun blocage technique connu ; le report des PNG est une décision du propriétaire.

## DÉCISIONS À CONSERVER

1. Deux ZIP sur GitHub Pages, chacun sous 100 Mio : `ecommerce-opquast-v5-slides.zip` (1 à 66, 57,94 Mio) et `ecommerce-opquast-v5-slides-partie-2.zip` (67 à 132, 64,04 Mio). Les bornes sont dans `variant.json` ; chaque partie contient les alternatives courantes.
2. Description, transcription et notes sont distinctes. Le lecteur actuel expose deux accordéons : description avec les textes visibles, puis discours oral. La transcription reste dans les exports d’alternatives.
3. Les rubriques `Transition` et `Conclusion` sont autorisées hors des 2 à 4 titres de contenu. Le validateur structurel ne prouve ni leur pertinence ni l’exactitude métier.
4. Les anciens verdicts d’image `VALIDEE_PRODUCTION` sont des traces historiques, pas des preuves indépendantes de réception actuelle.
5. La correction livrée reprend les constats de l’audit ShipGuard ; elle ne constitue pas une nouvelle campagne ShipGuard ni un audit RGAA complet.
6. Préférences IGPDE toujours applicables à ces séries : style bleu illustré, transcription fidèle au PPTX, discours oral distinct. Les anciens libellés d’accueil et le support `catalog_label` sont conservés. La Partie II existe désormais ; l’ancien contexte la disait à tort non créée.

## RÉFÉRENCES

- [README : état et reprise](../README.md#état-et-reprise-du-chantier-e-commerce).
- [Audit initial](../audits/revue-2026-10-28-ecommerce-opquast-v5-f9b3ae1.md).
- [Corrections et réserves](../audits/corrections-2026-10-29-ecommerce-sans-png.md).
- [Portée des revues d’image historiques](../ecommerce-opquast-v5/source/reviews/README.md).
- [Jeu public](https://alexandra-guiderdoni.github.io/slides-miweb/ecommerce-opquast-v5/).
- Preuves détaillées locales de l’audit : `/Users/alex/Claude-worktrees/revue-ecommerce-opquast-v5-20261028/preuves/`.
- Worktree du correctif : `/Users/alex/Claude-worktrees/slides-miweb-corrections-audit`, branche `fix/ecommerce-audit`, conservé. Ne pas le confondre avec le dépôt principal après les commits documentaires suivants.

## PROCHAINE REPRISE

1. Vérifier l’arbre courant, les changements concurrents et les SHA local/distant de `main`.
2. Lire l’issue #15 et les réserves avant toute modification ; arrêter la liste exacte des images et des paires question/correction à traiter.
3. Ne pas refaire les corrections techniques livrées. Revalider les formulations Opquast et les scénarios avant de générer les images concernées.
4. Synchroniser prompts, listes blanches, images et textes associés ; faire une réception indépendante des visuels modifiés en original et en projection.
5. Reprendre les tests, les deux ZIP, la publication racine et la vérification publique selon les guides actifs. Ne pas clore les réserves simplement parce qu’un validateur est vert.
