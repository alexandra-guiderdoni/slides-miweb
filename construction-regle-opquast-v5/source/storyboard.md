# Storyboard - Comment se construit une règle Opquast ?

<!-- PDG-LARGE-FILE-JUSTIFICATION: storyboard unique de 16 slides dont les champs de traçabilité, d'acceptation et de rejet doivent rester relus ensemble avant génération. -->

## Identité

- Statut : `VALIDE_POUR_GENERATION` des quatre étalons uniquement.
- Version : `v001`.
- Périmètre : construction pédagogique d'une règle, Opquast V5, édition de contrôle `qualite-numerique`.
- Audience : collègues des métiers numériques préparant la certification Opquast, niveau intermédiaire.
- Objectif : relier préjudice utilisateur, proposition, exigences, discussion, documentation et preuve, sans simuler le processus interne officiel d'Opquast.
- Nombre : 16 slides principales, 0 approfondissement, 0 annexe.
- Parcours : les 16 slides appartiennent à `ESSENTIEL_60`, dans l'ordre 01 à 16.
- Justification du nombre : l'inventaire affecte les 30 informations métier aux 16 slides sans omission ; aucun quota n'a été appliqué.
- Revue primaire : auto-revue Codex du 11 octobre 2026, contrôles structurels et provenance passés.
- Revue croisée : `NOT VERIFIED`, aucune délégation n'étant autorisée.
- Correspondance machine : `run.json` ; une seule version active.

## Paramètres de série

- Guide commun : `docs/05-GUIDE-STYLE.md`, version 2.0.0.
- Header gauche exact : `QUALITÉ WEB`, puis `EXPÉRIENCES DURABLES`.
- Header droit exact : `Opquast`, puis `DES SITES MEILLEURS POUR TOUS`.
- Footer exact : `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`.
- Pagination : `NN / 16`, en bas à droite.
- Badges : uniquement pour une règle V5 précisément citée ; position stable dans la zone de contenu.
- Slogan : aucun. Une phrase de synthèse est autorisée seulement en ouverture et en conclusion.
- Référence visuelle : les 17 premières slides de `navigation-opquast-v5-360`, grammaire visuelle uniquement.
- Référence éditoriale : exclusivement les deux Markdown `SB` et `DA` définis dans la matrice.
- Formes organiques dans les angles : interdites.
- VPTCS : absent, car non demandé par les sources.
- Footer d'annexe : sans objet.
- Exception au guide : aucune.

## Règles contrôlées

- 72 : « Le format de saisie des champs de formulaire qui le nécessitent est indiqué. »
- 87 : « Les processus complexes sont accompagnés de la liste de leurs étapes. »
- 140 : « Les liens sont visuellement différenciés du reste du contenu. »
- 152 : « Tous les liens internes sont valides. »
- 155 : « Il est possible de revenir à la page d’accueil depuis toutes les pages. »
- 156 : « Chaque page affiche une information permettant de connaître son emplacement dans l’arborescence. »
- 159 : « Les icônes de navigation sont accompagnées d’une légende explicite. »
- 168 : « Un moteur de recherche interne est proposé. »
- 223 : « Le serveur envoie une page d’erreur 404 personnalisée. »
- 224 : « Le serveur envoie une page d’interdiction 403 personnalisée. »
- 233 : « Le codage de caractères utilisé est UTF-8. »

Source du contrôle : MCP Opquast, source API, 11 octobre 2026. Détail dans `sources/opquast/verification-regles-2026-10-11.md`.

## Slide 01 - Une idée utile suffit-elle ?

- Classement : `ESSENTIEL_60`, position 1.
- Rôle narratif : ouverture et mise en doute d'une attente vague.
- Idée nouvelle : l'accord sur une intention ne produit pas une preuve commune.
- Situation : plusieurs professionnels qualifient un site d'« intuitif » sans partager les mêmes indices.
- Risque utilisateur : le ressenti utile reste inexploité si aucune exigence observable n'en est tirée.
- Principe de prévention : transformer une impression en exigence contrôlable sans disqualifier le ressenti.
- Garantie limitée : l'examen améliore la reproductibilité de l'évaluation ; il ne transforme pas automatiquement une idée en règle.
- Règles concernées : aucune règle numérotée.
- Sources : `CR-001`, `CR-002`, rappel de `CR-003` ; `SB:10-14`, `SB:105-115`, `DA:12-16`, `DA:67-77`.
- Exemple : « Ce site doit être intuitif. », exemple pédagogique fourni par les sources.
- Composition : titre centré ; citation vague au centre ; trois constats contradictoires autour d'une fiche de verdict impossible à remplir ; flèche vers le callout final.
- Textes visibles exacts : `Une idée utile suffit-elle ?` ; `« Ce site doit être intuitif. »` ; `Intention ≠ règle contrôlable` ; en-têtes ; footer ; `01 / 16`.
- Termes ambigus : « intuitif » reste une attente vague, pas un libellé de règle ; « intention » ne signifie pas inutile.
- Interdits : aucun verdict anticipé, aucune règle inventée, aucun slogan supplémentaire, aucun faux logo, aucun pseudo-texte.
- Transition : « Partons de ce qui est arrivé à une personne, pas de l'adjectif utilisé. »
- Préparation orale : même attente et indices différents ; ressenti comme signal initial ; critères d'examen d'une règle ; mémo « Accord sur l'idée ≠ accord sur la preuve. »
- Pré-transcription : reprendre seulement la citation, les trois lectures contradictoires, la fiche de verdict et le callout ; statut `PRETRANSCRIPTION_A_VERIFIER` jusqu'au PNG final.
- Fichier final prévu : `finals/slide-01-idee-utile.png`.
- Acceptation : tous les textes exacts, contradiction lisible sans couleur seule, absence de verdict et de texte parasite.
- Rejet : ajout d'un critère, d'un acteur, d'une conclusion ou d'une procédure absente des sources.
- Statut étalon : ouverture.

## Slide 02 - Ce que l'utilisateur subit avant la règle

- Classement : `ESSENTIEL_60`, position 2.
- Rôle narratif : ancrage utilisateur et fil rouge.
- Idée nouvelle : nommer le préjudice avant la solution.
- Situation : une personne clique sur un lien interne et n'accède pas au contenu attendu.
- Risque utilisateur : temps perdu, interruption, confusion, abandon éventuel ; aucune perte de données n'est affirmée.
- Principe de prévention : partir du besoin d'accès au contenu.
- Garantie limitée : la règle 152 contribue à éviter les erreurs 404 pendant la navigation, sans promettre un parcours sans toute erreur.
- Règle : 152, sans afficher encore le libellé complet.
- Sources : `CR-003`, `CR-004` ; `SB:68-79`, `SB:117-127`, `DA:79-89`.
- Composition : trajet simple de « démarche recherchée » à « lien interne » puis « page introuvable ».
- Textes visibles exacts : `Je clique. Je n'arrive pas.` ; `Besoin : accéder au contenu` ; `Préjudice : temps perdu, parcours interrompu` ; en-têtes ; footer ; `02 / 16`.
- Interdits : perte de données, abandon certain, chiffre, promesse absolue.
- Transition : « Une attente comme “navigation intuitive” comporte plusieurs risques distincts. »
- Préparation orale : distinguer difficulté vécue et défaut technique ; garder l'abandon au conditionnel.
- Fichier final prévu : `finals/slide-02-parcours-interrompu.png`.
- Acceptation : relation lien interne vers interruption explicite ; aucune conséquence ajoutée.

## Slide 03 - D'une attente large à plusieurs règles possibles

- Classement : `ESSENTIEL_60`, position 3.
- Rôle narratif : décomposition.
- Idée nouvelle : plusieurs expériences autonomes peuvent se cacher derrière une attente large.
- Situation : « navigation intuitive » recouvre identifier un lien, revenir à l'accueil, se situer, comprendre une icône et chercher.
- Risque utilisateur : confondre des difficultés distinctes dans un jugement global.
- Principe de prévention : décomposer en exigences évaluables séparément.
- Garantie limitée : les cinq exemples illustrent la décomposition, sans épuiser la navigation.
- Règles : 140, 155, 156, 159, 168 ; labels pédagogiques, pas libellés officiels.
- Sources : `CR-005`, partie de `CR-026` ; `SB:129-139`, `SB:305-310`, `DA:91-99`.
- Composition : un besoin central relié à cinq cartes équivalentes.
- Textes visibles exacts : `« Navigation intuitive »` ; `140 · Identifier les liens` ; `155 · Revenir à l'accueil` ; `156 · Savoir où l'on est` ; `159 · Comprendre les icônes` ; `168 · Trouver par recherche` ; `Labels pédagogiques, pas libellés officiels` ; en-têtes ; footer ; `03 / 16`.
- Interdits : exhaustivité annoncée, hiérarchie entre les cinq règles, libellés pédagogiques présentés comme officiels.
- Transition : « Même décomposée, une idée n'est pas nécessairement admise dans le référentiel. »
- Fichier final prévu : `finals/slide-03-decomposer-attente.png`.

## Slide 04 - Proposition, règle et recommandation

- Classement : `ESSENTIEL_60`, position 4.
- Rôle narratif : contrat du référentiel.
- Idée nouvelle : une idée utile peut connaître plusieurs devenirs.
- Situation : « Contrôlez vos liens chaque lundi. »
- Risque utilisateur : confondre utilité d'un processus et vérifiabilité d'une règle.
- Principe de prévention : examiner avant de retenir.
- Garantie limitée : l'examen permet de motiver une orientation, sans dévaloriser la recommandation.
- Règle : aucune règle numérotée affichée.
- Sources : `CR-006`, correction concernée de `CR-027` ; `SB:141-151`, `DA:101-113`, `DA:346-347`.
- Composition : une proposition entre dans une table de tri ; quatre sorties sans hiérarchie de valeur.
- Textes visibles exacts : `Proposition` ; `Examen` ; `Règle retenue` ; `Recommandation` ; `Non retenue` ; `Évolution d'une fiche existante` ; en-têtes ; footer ; `04 / 16`.
- Interdits : recommander égale échouer ; sortie bonne ou mauvaise ; causalité non documentée.
- Transition : « Regardons un problème de formulation qui rend l'évaluation ambiguë. »
- Fichier final prévu : `finals/slide-04-devenir-proposition.png`.

## Slide 05 - Une règle, une décision

- Classement : `ESSENTIEL_60`, position 5.
- Rôle narratif : vote et unicité.
- Idée nouvelle : deux risques indépendants appellent deux décisions.
- Situation : la page 404 est personnalisée, la 403 ne l'est pas.
- Risque utilisateur : perdre le diagnostic unitaire dans un critère composé.
- Principe de prévention : séparer les contrôles.
- Garantie limitée : l'unicité améliore le diagnostic ; elle ne rend pas toute conjonction logiquement indécidable.
- Règles : 223 et 224.
- Sources : `CR-007`, partie de `CR-026`, correction concernée de `CR-027` ; `SB:153-163`, `SB:311-315`, `DA:115-127`, `DA:316-320`.
- Composition : carte `403 + 404 ?` se divisant en deux fiches avec leur propre case.
- Textes visibles exacts : `403 + 404 ?` ; `Deux situations, deux décisions` ; `223 · Erreur 404 personnalisée` ; `224 · Interdiction 403 personnalisée` ; en-têtes ; footer ; `05 / 16`.
- Interdits : absence de 403 égale non-conformité automatique ; demi-validation ; équivalence 403/404.
- Transition : « Cette exigence d'unicité fait partie du contrat explicite de l'atelier V5. »
- Fichier final prévu : `finals/slide-05-unicite-403-404.png`.

## Slide 06 - Six exigences pour éprouver une proposition

- Classement : `ESSENTIEL_60`, position 6.
- Rôle narratif : éclairage central et regroupement.
- Idée nouvelle : six exigences transforment les préférences en questions examinables.
- Situation : une proposition appréciée doit néanmoins être confrontée à six questions.
- Risque utilisateur : retenir une formulation inutile, locale, arbitraire, invérifiable, irréaliste ou composée.
- Principe de prévention : examiner ensemble universalité, utilité, absence de seuil empirique arbitraire, vérifiabilité, réalisme et unicité.
- Garantie limitée : ce sanity check éprouve une proposition ; le consensus et la rédaction restent traités séparément.
- Règles : aucune règle numérotée.
- Sources : `CR-008`, `CR-009`, `CR-010`, correction concernée de `CR-027` ; `SB:28-34`, `SB:165-175`, `DA:24-30`, `DA:129-148`, `DA:352-353`.
- Composition : six cartes interrogatives équilibrées autour d'une fiche « proposition » ; aucun ordre ni critère prioritaire.
- Textes visibles exacts : `Six exigences pour éprouver une proposition` ; `ATELIER V5 · SIX EXIGENCES` ; `Universelle ?` ; `Utile ?` ; `Sans seuil empirique arbitraire ?` ; `Vérifiable depuis le service ?` ; `Réaliste ?` ; `Unique ?` ; `Consensus et conseils de rédaction : étudiés à part.` ; en-têtes ; footer ; `06 / 16`.
- Termes ambigus : « non numérique » signifie sans valeur empirique arbitraire, pas sans aucun chiffre ; « unique » signifie une seule exigence à évaluer.
- Interdits : septième carte, hiérarchie, numérotation officielle inventée, exemple nouveau, règle numérotée, texte parasite.
- Transition : « Testons la vérifiabilité. »
- Préparation orale : transformer les six exigences en questions ; distinguer seuil mesurable et seuil justifié ; rappeler la différence avec la liste de 2019 ; mémo exact du storyboard.
- Pré-transcription : décrire la fiche centrale et les six cartes, sans les présenter comme étapes successives ; statut `PRETRANSCRIPTION_A_VERIFIER` jusqu'au PNG final.
- Fichier final prévu : `finals/slide-06-six-exigences.png`.
- Acceptation : six cartes seulement, même statut graphique, textes exacts et note de séparation visible.
- Rejet : sept cartes, consensus intégré à la liste, exemple ou définition non sourcée, flèche suggérant une chronologie.
- Statut étalon : éclairage et regroupement.

## Slide 07 - Vote : quelle proposition est vérifiable ?

- Classement : `ESSENTIEL_60`, position 7.
- Rôle narratif : vote sans correction.
- Idée nouvelle : distinguer ce qui est observable depuis le service.
- Situation : choisir entre un état et une procédure.
- Risque utilisateur : confondre une promesse organisationnelle avec un résultat contrôlable.
- Principe de prévention : demander quelle preuve peut être observée.
- Garantie limitée : la slide pose la question et ne montre aucune réponse.
- Sources : `CR-011` ; `SB:177-187`, `DA:150-165`.
- Composition : deux cartes de statut strictement égal, sans vert, rouge, coche ou hiérarchie.
- Textes visibles exacts : `A · Le site est exempt de liens morts.` ; `B · Les liens sont vérifiés chaque semaine.` ; `VOTE A / B` ; `Justifiez par une preuve` ; en-têtes ; footer ; `07 / 16`.
- Interdits : correction, symbole gagnant, règle 152, mise en valeur d'une réponse.
- Transition : « Passons à la preuve, puis à la formulation retenue dans la version actuelle. »
- Fichier final prévu : `finals/slide-07-vote-verifiabilite.png`.

## Slide 08 - La preuve, pas la promesse

- Classement : `ESSENTIEL_60`, position 8.
- Rôle narratif : correction et règle centrale.
- Idée nouvelle : le contrôle constate un état ; une routine peut rester un moyen de maintenance.
- Situation : distinguer le résultat observable de la vérification hebdomadaire.
- Risque utilisateur : des liens internes invalides peuvent interrompre l'accès et décevoir.
- Principe de prévention : vérifier la validité des liens internes.
- Garantie limitée : la règle 152 vise les liens internes ; elle ne garantit pas tous les liens ni une sûreté absolue.
- Règle : 152, libellé exact contrôlé par l'API.
- Sources : `CR-004`, `CR-012`, `CR-013`, partie de `CR-026` ; `SB:70-79`, `SB:189-199`, `SB:306`, `DA:81-87`, `DA:167-177`, `DA:322-326`, `DA:355-356`.
- Composition : grande zone principale où une loupe suit un lien interne vers une page valide ; zone secondaire séparée avec un agenda représentant le processus.
- Textes visibles exacts : `La preuve, pas la promesse` ; `A · Résultat observable` ; `B · Processus interne` ; `RÈGLE 152` ; `Tous les liens internes sont valides.` ; `Contrôle : rechercher les liens internes vers une erreur 404` ; en-têtes ; footer ; `08 / 16`.
- Termes ambigus : « tous » porte sur les liens internes ; « contrôle » n'est pas un audit de tout le référentiel.
- Interdits : liens externes, garantie à 100 %, correction ajoutée dans l'oral seulement, autre code d'erreur, texte parasite.
- Transition : « Une règle peut être vérifiable sans s'appliquer à tous les sites dans toutes les situations. »
- Préparation orale : corriger A/B ; relier la règle au parcours interrompu ; distinguer libellé et moyen de maintenance ; mémo « Le contrôle constate un état, pas la promesse d'un rituel. »
- Pré-transcription : reprendre les deux catégories, le badge, le libellé, le contrôle et la relation entre loupe et agenda ; statut `PRETRANSCRIPTION_A_VERIFIER` jusqu'au PNG final.
- Fichier final prévu : `finals/slide-08-preuve-regle-152.png`.
- Acceptation : libellé exact, numéro exact, `internes` visible, hiérarchie principale/secondaire compréhensible sans couleur.
- Rejet : extension aux liens externes, faute dans le libellé, agenda présenté comme non souhaitable, promesse absolue.
- Statut étalon : règle centrale.

## Slide 09 - Universelle ne signifie pas toujours applicable

- Classement : `ESSENTIEL_60`, position 9.
- Rôle narratif : distinction de concepts.
- Idée nouvelle : portée territoriale et contexte de contrôle sont distincts.
- Situation : un site avec formulaire et un site sans formulaire.
- Risque utilisateur : déclarer non conforme un cas où l'objet de la règle n'existe pas.
- Principe de prévention : établir l'applicabilité avant le verdict.
- Garantie limitée : l'absence d'un objet ne rend pas automatiquement toute règle non applicable.
- Sources : `CR-014`, correction concernée de `CR-027` ; `SB:201-211`, `DA:179-187`.
- Composition : deux sites comparés, l'un avec formulaire et l'autre sans, plus deux définitions courtes.
- Textes visibles exacts : `Universalité = pas de dépendance à une loi locale` ; `Applicabilité = contexte effectivement rencontré` ; `Non applicable ≠ non conforme` ; en-têtes ; footer ; `09 / 16`.
- Interdits : doctrine d'audit universelle, règle de formulaire inventée, automatisme sur l'absence.
- Transition : « Et si notre règle est trop précise, peut-elle devenir périssable ? »
- Fichier final prévu : `finals/slide-09-universalite-applicabilite.png`.

## Slide 10 - Écrire durablement, sans mythifier UTF-8

- Classement : `ESSENTIEL_60`, position 10.
- Rôle narratif : vigilance rédactionnelle.
- Idée nouvelle : un chiffre dans un nom technique n'est pas un seuil empirique arbitraire.
- Situation : comparer un seuil inventé et la règle 233.
- Risque utilisateur : appliquer mécaniquement un principe de rédaction et déformer la portée d'une règle.
- Principe de prévention : juger la précision par sa portée et son contexte.
- Garantie limitée : la règle 233 est contrôlable ; elle ne justifie aucun seuil arbitraire.
- Règle : 233.
- Sources : `CR-015`, `CR-016`, partie de `CR-026` ; `SB:36-38`, `SB:213-223`, `SB:313`, `DA:189-199`, `DA:328-331`, `DA:358-359`.
- Composition : comparaison en deux colonnes entre seuil à justifier et codage documenté.
- Textes visibles exacts : `À éviter : seuil arbitraire ; recette fragile ; norme entière en guise de règle` ; `Règle 233 : « Le codage de caractères utilisé est UTF-8. »` ; `UTF-8 : nom de codage, pas seuil de performance` ; en-têtes ; footer ; `10 / 16`.
- Interdits : présenter UTF-8 comme exception, autoriser tout chiffre, inventer la justification historique.
- Transition : « Une bonne formulation n'est que le début : Opquast est un commun discuté. »
- Fichier final prévu : `finals/slide-10-ecriture-durable-utf8.png`.

## Slide 11 - On ne fabrique pas un commun tout seul

- Classement : `ESSENTIEL_60`, position 11.
- Rôle narratif : construction collective.
- Idée nouvelle : la robustesse se discute et la sélection s'argumente.
- Situation : plusieurs métiers défendent des réponses opposées.
- Risque utilisateur : qu'une préférence particulière entre dans le socle commun sans contradiction.
- Principe de prévention : proposer, discuter, reformuler et arbitrer.
- Garantie limitée : le consensus est recherché, sans promettre l'unanimité ; une décision finale peut être expliquée.
- Sources : `CR-017`, `CR-018`, rappel de `CR-010` ; `SB:225-235`, `SB:358-366`, `DA:201-218`, `DA:349-353`.
- Composition : proposition circulant entre plusieurs métiers, arguments consignés, décision documentée.
- Textes visibles exacts : `Proposer → Discuter → Reformuler → Arbitrer` ; `Consensus recherché, pas unanimité garantie` ; `Décision et justification` ; `2005 · 2019 · 2021 · 2025` ; en-têtes ; footer ; `11 / 16`.
- Interdits : consensus comme septième exigence, unanimité automatique, procédure secrète, chronologie non datée.
- Transition : « Regardons un débat réel. »
- Fichier final prévu : `finals/slide-11-construction-collective.png`.

## Slide 12 - Parfois, la meilleure règle est déjà là

- Classement : `ESSENTIEL_60`, position 12.
- Rôle narratif : cas documenté.
- Idée nouvelle : une proposition peut enrichir une fiche existante ou devenir recommandation.
- Situation : contraintes de création d'un mot de passe discutées en 2025.
- Risque utilisateur : créer un doublon ou attribuer une causalité historique non démontrée.
- Principe de prévention : examiner le référentiel existant avant d'ajouter une règle.
- Garantie limitée : les échanges documentent une recommandation et un rapprochement avec la règle 72, pas l'origine exclusive de son texte final.
- Règle : 72.
- Sources : `CR-019`, rappel de `CR-006`, partie de `CR-026` ; `SB:237-247`, `SB:303`, `DA:220-239`, `DA:333-336`.
- Composition : une proposition est rapprochée d'une fiche existante, sans flèche causale vers le texte final.
- Textes visibles exacts : `Proposition 2025 : contraintes de mot de passe indiquées` ; `Nouveau doublon ou enrichissement ?` ; `Issue documentée : recommandation` ; `Rapprochement avec la règle 72` ; en-têtes ; footer ; `12 / 16`.
- Interdits : causalité exclusive, règle 72 créée par cette discussion, recommandation présentée comme échec.
- Transition : « Quand une règle est retenue, son libellé seul ne suffit pas à l'appliquer. »
- Fichier final prévu : `finals/slide-12-regle-deja-la.png`.

## Slide 13 - Une règle est aussi une fiche de preuves

- Classement : `ESSENTIEL_60`, position 13.
- Rôle narratif : documentation.
- Idée nouvelle : libellé, objectifs, solution et contrôle remplissent des fonctions distinctes.
- Situation : compléter la fiche de la règle 152.
- Risque utilisateur : confondre l'exigence, le bénéfice, le moyen et la preuve.
- Principe de prévention : documenter chaque fonction séparément.
- Garantie limitée : une fiche exploitable n'implique pas un contrôle intégralement automatisable.
- Règle : 152.
- Sources : `CR-020`, rappels de `CR-012` et `CR-013` ; `SB:249-259`, `DA:241-253`.
- Composition : fiche centrale avec trois volets « Pourquoi ? », « Comment ? », « Quelle preuve ? ».
- Textes visibles exacts : `Libellé : Tous les liens internes sont valides.` ; `Objectif : éviter les impasses de navigation` ; `Solution : prévenir ou corriger les liens internes invalides` ; `Contrôle : vérifier l'absence de liens internes aboutissant à une 404` ; `Objectif, solution, contrôle : résumés pédagogiques` ; en-têtes ; footer ; `13 / 16`.
- Interdits : présenter les résumés comme citations, promettre une automatisation complète.
- Transition : « À vous de rédiger et surtout de contester votre propre proposition. »
- Fichier final prévu : `finals/slide-13-fiche-preuves.png`.

## Slide 14 - Mettez une idée à l'épreuve

- Classement : `ESSENTIEL_60`, position 14.
- Rôle narratif : activité sans correction.
- Idée nouvelle : une proposition doit survivre à la question du contrôle.
- Situation : une personne commence une longue démarche sans connaître les étapes restantes.
- Risque utilisateur : ne pas anticiper la longueur ou les étapes de la démarche.
- Principe de prévention : formuler une proposition unitaire et une preuve observable.
- Garantie limitée : l'exercice produit une proposition discutable, jamais une règle officielle.
- Sources : `CR-021`, rappel de `CR-029` ; `SB:261-271`, `DA:255-282`.
- Composition : cas central puis quatre cartes à compléter ; aucune correction ni règle 87.
- Textes visibles exacts : `CAS : « Je commence une longue démarche et j'ignore les étapes restantes. »` ; `1 · Préjudice` ; `2 · Proposition unitaire` ; `3 · Contrôle depuis le service` ; `4 · Premier verdict` ; `Exercice pédagogique, non officiel` ; en-têtes ; footer ; `14 / 16`.
- Interdits : règle 87, correction, réponse préremplie, consigne de durée, animation ou régie.
- Transition : « Est-ce vraiment une règle nouvelle ? »
- Fichier final prévu : `finals/slide-14-mettre-idee-epreuve.png`.

## Slide 15 - Le bon verdict est parfois : retravailler

- Classement : `ESSENTIEL_60`, position 15.
- Rôle narratif : correction formative.
- Idée nouvelle : éviter le doublon et bien placer l'exigence est un résultat utile.
- Situation : comparer la proposition de l'atelier à la règle 87.
- Risque utilisateur : produire une nouvelle règle alors que le besoin est déjà couvert.
- Principe de prévention : motiver le verdict et examiner la règle existante.
- Garantie limitée : plusieurs formulations pédagogiques peuvent être discutées ; aucune validation officielle n'est produite.
- Règle : 87.
- Sources : `CR-022`, `CR-023`, rappel de `CR-029`, partie de `CR-026` ; `SB:273-283`, `SB:304`, `DA:284-298`, `DA:338-342`.
- Composition : une fiche de proposition entourée de trois sorties non hiérarchisées, avec renvoi explicite vers la règle 87.
- Textes visibles exacts : `Verdicts possibles : retravailler · recommander · rapprocher d'une règle existante` ; `Règle 87 · Les processus complexes sont accompagnés de la liste de leurs étapes.` ; `Ne jamais prétendre valider une règle officielle en classe.` ; en-têtes ; footer ; `15 / 16`.
- Interdits : un verdict unique imposé, atelier présenté comme officiel, règle 87 révélée avant cette slide.
- Transition : « Reprenons la méthode utilisable demain dans vos projets. »
- Fichier final prévu : `finals/slide-15-verdict-motive.png`.

## Slide 16 - Construire une règle, c'est construire une preuve partagée

- Classement : `ESSENTIEL_60`, position 16.
- Rôle narratif : synthèse et transfert.
- Idée nouvelle : trois questions relient le besoin, la preuve et la discussion collective.
- Situation : challenger une proposition de règle dans un projet.
- Risque utilisateur : revenir à une préférence, une promesse ou une validation simulée.
- Principe de prévention : interroger le préjudice, l'exigence observable et la discussion documentée.
- Garantie limitée : la méthode aide à argumenter ; elle ne simule pas une validation Opquast et ne remplace pas un référentiel spécialisé.
- Règles : aucune règle numérotée.
- Sources : `CR-002`, `CR-024`, `CR-025`, `CR-028`, `CR-029`, `CR-030` ; `SB:25`, `SB:285-295`, `SB:330`, `SB:332-354`, `SB:382-385`, `DA:300-312`, `DA:361-365`.
- Composition : trois grandes questions autour d'une fiche commune ; sous les questions, un parcours discret de la difficulté vers la règle documentée, sans le présenter comme officiel.
- Textes visibles exacts : `Construire une règle, c'est construire une preuve partagée` ; `1 · Quel préjudice utilisateur ?` ; `2 · Quelle exigence, quelle preuve ?` ; `3 · Qui peut la discuter, la documenter et la maintenir ?` ; `Une règle utile, contrôlable, argumentée et durable.` ; `Synthèse pédagogique interne` ; en-têtes ; footer ; `16 / 16`.
- Termes ambigus : « partagée » signifie discutée et documentée, pas unanimité ; « construire » décrit la synthèse pédagogique.
- Interdits : processus officiel, sigle nouveau, promesse de conformité, quiz, règle ou exemple ajouté, texte parasite.
- Conclusion : « Une bonne proposition n'est pas forcément retenue ; une règle Opquast est une exigence pensée pour être utile, contrôlable, discutée et maintenable. »
- Préparation orale : reprendre les trois questions ; rappeler la limite non officielle ; mémo « Le besoin donne le sens ; la preuve et le débat rendent la règle partageable. »
- Pré-transcription : restituer les trois questions, la phrase de synthèse et la mention pédagogique ; statut `PRETRANSCRIPTION_A_VERIFIER` jusqu'au PNG final.
- Fichier final prévu : `finals/slide-16-preuve-partagee.png`.
- Acceptation : trois questions exactes, aucune quatrième étape, synthèse claire, mention pédagogique visible.
- Rejet : ajout d'un organisme, d'une certification, d'une promesse ou d'un processus officiel.
- Statut étalon : synthèse.

## Revue avant génération

- [ ] Vérifier les 30 identifiants de l'inventaire contre la matrice.
- [ ] Vérifier caractère par caractère les listes blanches des slides 01, 06, 08 et 16.
- [ ] Vérifier que chaque phrase orale des quatre étalons possède une ligne source.
- [ ] Vérifier que les slides 07 et 14 n'affichent aucune correction.
- [ ] Vérifier que la règle 152 reste limitée aux liens internes.
- [ ] Vérifier que les six exigences restent distinctes du consensus.
- [ ] Vérifier que UTF-8 n'autorise aucun seuil arbitraire.
- [ ] Vérifier que la chaîne finale est signalée comme synthèse pédagogique.
- [ ] Enregistrer le SHA-256 et la preuve de revue dans `run.json`.

Le passage à `VALIDE_POUR_GENERATION` autorise uniquement les quatre étalons. Le reste de la série demeure bloqué par le gate humain.
