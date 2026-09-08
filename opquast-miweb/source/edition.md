# Édition web Opquast Miweb

La version web reprend les 44 slides du PowerPoint `opquast-presentation-miweb-2026.pptx`, dans le même ordre. Les images sont conservées. Leur optimisation PNG est sans perte, avec comparaison des dimensions et de tous les pixels RGBA.

`slides.json` est la source de génération des pages et du Markdown téléchargé. Chaque slide comporte une alternative courte, une description du visuel, une transcription structurée, un relevé des textes visibles, un message et le discours oral extrait des notes du PPTX.

Les textes visibles ont été relus sur les 44 images. Ils conservent les chiffres et les formulations du visuel, avec normalisation des sauts de ligne et de la typographie des apostrophes. Les descriptions expliquent les relations représentées. Les discours sont distincts de ces transcriptions.

## Structuration des transcriptions

À la demande de l’utilisateur, les 44 transcriptions sont organisées par idées, avec des sous-titres et, si nécessaire, un second niveau de titres. Les correspondances entre lettres, dimensions, métiers, rubriques et valeurs sont présentées en tableaux. Les étapes restent dans leur ordre. Les mots qui forment une même idée sont réunis en phrases, notamment pour les responsabilités, les modalités de formation et les consignes d’examen.

Le champ `transcription` porte cette structure dans `slides.json`. Le relevé `textes_visibles` est conservé pour la traçabilité ; il n’est plus affiché comme une longue liste de mots isolés. Les mêmes regroupements sont rendus sous chaque slide, dans la page des transcriptions et dans le Markdown du ZIP. Les notes orales conservent leur formulation et restent dans un bloc distinct.

Tous les tirets cadratins des textes du jeu sont remplacés par des tirets simples, y compris dans les copies des storyboards publiées. Les notes orales n’en contenaient aucun. Les documents de préparation originaux et le PowerPoint restent conservés dans le dossier de travail Opquast, hors du dépôt publié.

## Correction demandée sur le tarif

La slide 44 reste inchangée et affiche **450 euros HT**. Le discours oral et le message de la version web indiquent **485 € HT**, tarif vérifié sur la [page officielle de la certification](https://www.opquast.com/certification/) le 8 septembre 2026. Une précision explicite signale l’écart entre le visuel et le tarif corrigé.

Les notes du PPTX sont conservées hors correction du tarif. Le discours original de la slide 44 reste conservé dans [le document de préparation](storyboard.md#slide-44). Aucune actualisation générale des images ni des modalités de certification n’a été demandée.

## Complément du discours de la slide 15

À la demande de l’utilisateur, dix autres formules mnémotechniques ont été ajoutées après les notes originales de la slide 15. Les formulations fournies sont conservées telles quelles, de « Emphatique » à « Philosophe ». Le visuel et sa transcription restent inchangés.

## Traçabilité

- [Provenance et empreintes](provenance.json) : correspondances entre l’ordre du PPTX, les images sources et les PNG publiés.
- [Consignes et notes originales](storyboard.md) : les 44 entrées de préparation.
- `origines/` : les six storyboards sources et leurs exports de prompts disponibles.

Les exports signalent que les appels complets au générateur d’images n’ont pas été retrouvés. Les storyboards sont des consignes conservées, sans attestation des prompts exacts exécutés.

## Génération et contrôles

Le jeu est créé depuis `matrice-slide-ai/create_variant.py`. Son générateur autonome ajoute le discours oral, la précision tarifaire et les transcriptions structurées au modèle existant. L’accueil racine est géré séparément par `matrice-slide-ai/publish_variant.py`.

Les pages HTML, `alternatives.md`, le README du jeu et le ZIP se régénèrent avec `python3 opquast-miweb/build.py`. Les contrôles standard passent par `scripts/validate_variant.sh opquast-miweb` depuis la racine du dépôt.

Le statut d’accessibilité reste « non audité ». Les contrôles techniques et l’inspection locale ne constituent pas un audit RGAA complet.

## PDG pass

Contrôle ciblé des sorties générées et de la conservation des sources : `PDG self-check, not independent review`. Les générateurs de la matrice, le générateur du jeu et ses tests ont été inspectés. Les ajouts au modèle portent sur les discours, la précision tarifaire et les transcriptions structurées ; le code de navigation et les anciennes variantes sont conservés.

| Vérification | Preuve | Résultat |
| --- | --- | --- |
| Couverture | `slides.json`, `source/provenance.json`, comparaison au PPTX | 44 images dans l’ordre, 44 transcriptions et 44 discours. |
| Fidélité | Comparaison de tous les pixels RGBA et empreintes des notes | Images identiques ; notes originales conservées avec les deux adaptations demandées aux slides 15 et 44. |
| Régression | `scripts/validate_variant.sh opquast-miweb` | 17 tests réussis ; HTML validé par html-validate et vnu. |
| Structure | Tests des transcriptions et contrôle des exports | En-têtes de tableaux associés aux données, titres imbriqués sans dépasser le niveau 6, Markdown du ZIP conforme au rendu courant. |
| Parcours local | `/opquast-miweb/`, `#slide-15`, `#slide-44`, `?slides=all#diaporama` | Navigation par bouton et flèche clavier, accordéons et dix formules de la slide 15 observés dans Chrome. |

Une recompression sans perte des PNG a été détectée après un premier build. Les empreintes et le ZIP ont été régénérés ; le test de provenance vérifie désormais les fichiers et les notes.

NOT VERIFIED: l’activation du plein écran n’a pas abouti dans le navigateur automatisé. Le geste tactile sur appareil physique, le rendu mobile dédié et l’audit RGAA complet n’ont pas été exécutés. La publication distante et les URL GitHub Pages ne sont pas couvertes par cette recette locale.

PDG-LARGE-FILE-JUSTIFICATION: `slides.json` réunit les 44 entrées exigées par le générateur canonique, avec leurs discours ; le format JSON reste sans commentaire. Les exports complets et le générateur autonome suivent le contrat existant du dépôt.

PDG-BINARY-ASSET-JUSTIFICATION: les 44 PNG sont les visuels du support sélectionné. Le ZIP duplique ces images pour le téléchargement hors ligne prévu par le dépôt et inclut les transcriptions ainsi que le discours oral. Le PPTX n’est pas dupliqué dans le site.
