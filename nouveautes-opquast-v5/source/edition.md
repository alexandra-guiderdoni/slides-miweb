# Édition du support « Nouveautés d’Opquast V5 »

Titre public : Nouveautés d’Opquast V5

Slug de publication : `nouveautes-opquast-v5`

Base éditoriale : storyboard v003 des dix premières slides, conservé dans
`source/storyboard.md`, statut `VALIDE_POUR_GENERATION` du 17 septembre 2026.

Le texte de `source/transcription-et-discours-oral.md` fournit le contenu des deux
accordéons de chaque slide. Il reprend sans réécriture les accordéons rédigés pour la
série ; seules les balises HTML d’accordéon et les niveaux de titre ont été transformés
pour entrer dans le format des séries Opquast V5 déjà publiées. Le storyboard reste
conservé comme trace de conception des visuels et comme source des titres, des textes
visibles et des messages.

## Périmètre et numérotation

Le support publie les 10 premières slides d’une série qui en compte 17. Les slides 11 à
17 n’étaient pas produites au moment de la publication.

Les visuels portent une pagination imprimée qui suit la série complète, de `1 / 17` à
`10 / 17`. La numérotation web va de 1 à 10 et coïncide donc avec le début de cette
pagination, mais le total imprimé annonce sept visuels encore absents. Cet écart est
volontaire : les images n’ont pas été retouchées pour masquer la suite de la série.

Les slides 11 à 17 seront ajoutées à ce même dossier, par mise à jour de `slides.json`
et nouvelle exécution de `build.py`. Le jeu n’est pas figé et ne doit pas être dupliqué
pour accueillir la suite.

## Règles couvertes

Huit nouvelles règles de la version 5 du référentiel, chacune traitée sur une slide du
deck après deux slides de cadrage :

- règle 14, détournement de caractères, thématique Contenus ;
- règle 26, existence d’un compte utilisateur, thématique Données personnelles ;
- règle 68, provenance des produits, thématique E-Commerce ;
- règle 96, relance de la double authentification, thématique Formulaires ;
- règle 97, autocomplétion signalée dans le code source, thématique Formulaires ;
- règle 98, boutons désactivés et lecteurs d’écran, thématique Formulaires ;
- règle 216, affichage de la barre d’adresse, thématique Sécurité ;
- règle 217, authentification du domaine de messagerie, thématique Sécurité.

Les libellés et les thématiques des huit règles ont été contrôlés le 17 septembre 2026
contre l’API Opquast, version `qualite-numerique`. Les citations portées par les visuels
correspondent aux libellés officiels, aux variantes typographiques près décrites plus bas.

La traçabilité des règles est portée par le champ `regles_opquast` de `slides.json` et
par la présente fiche.

Les chiffres de la slide 1, 240 règles en V4 et 245 en V5, deux suppressions, une fusion
et huit ajouts, proviennent du storyboard source. Ils décrivent l’évolution du
référentiel et ne sont pas issus d’un décompte refait pour cette publication.

## Réserves de lecture

La slide 3 illustre le détournement de caractères par un contraste typographique entre
deux panneaux qui affichent tous deux le mot « Bonus ». Le visuel n’emploie pas les
caractères Unicode détournés eux-mêmes, qui ne survivraient pas à toutes les chaînes de
production. La transcription décrit donc un exemple signalé comme tel, sans affirmer que
les deux panneaux emploient des jeux de caractères différents.

Le visuel de la slide 4 ferme la citation de la règle par un guillemet anglais, sans
guillemet ouvrant correspondant : la citation est introduite par un signe typographique
décoratif. Le visuel est conservé en l’état, décision du 17 septembre 2026. Les textes
visibles et la transcription reprennent le libellé sans ces guillemets.

Le titre imprimé de la slide 6 se termine par un point, contrairement aux autres titres
de la série. Le titre web reprend le libellé sans ce point final.

La slide 9 porte le numéro de règle dans une pastille ronde placée dans le corps de la
slide, là où les autres slides de règle utilisent un badge carré près du titre. Cette
variation de gabarit n’a pas d’incidence sur le contenu.

La slide 10 cite la règle 217 entre guillemets droits. Le libellé officiel de cette règle
ne porte pas de point final, ce que le visuel respecte.

Les exemples suivants sont fictifs et servent uniquement la démonstration : les adresses
`alice@example.com` et `bob@example.com`, le domaine `service.example`, ainsi que la
fiche « Produit exemple » à 12,90 € fabriquée au Portugal, qui porte sur le visuel la
mention « Exemple fictif ».

Les annotations « Compte existant » et « Compte inexistant » de la slide 4 sont des
repères pédagogiques ajoutés pour la démonstration. Elles ne font pas partie de
l’interface vue par la personne qui utilise le service.

Ce support n’a fait l’objet d’aucun audit RGAA dédié et ne déclare aucune conformité.

## Choix d’édition

Les champs `textes_visibles` reprennent le pied de page et la pagination de chaque
visuel, parce que cette information varie d’une slide à l’autre et documente le périmètre
partiel de la série. L’en-tête de marque, identique sur les dix visuels, n’y est pas
repris ; il figure dans les descriptions longues.

Les transcriptions de `slides.json` ajoutent, par rapport aux accordéons source, une
section « Message à retenir » sur chaque slide et une section « Point de vigilance » sur
les slides 4, 5, 9 et 10. Ces ajouts signalent les exemples fictifs et les repères
pédagogiques ; ils n’altèrent pas le texte repris de la source.

## Traçabilité des images

Les dix visuels ont été repris le 17 septembre 2026 entre 10h33 et 10h36, après
l’enregistrement du journal de production `run.json` de 06h12. Les empreintes SHA-256 de
ce journal ne décrivent donc plus les fichiers publiés.

Les empreintes des images effectivement publiées sont consignées dans
`source/transcription-et-discours-oral.md`, slide par slide, et ont été vérifiées
identiques entre le dossier source et `assets/slides/` au moment de la copie.
