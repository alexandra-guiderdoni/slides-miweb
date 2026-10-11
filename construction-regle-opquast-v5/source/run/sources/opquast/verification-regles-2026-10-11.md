# Vérification Opquast - Construction d'une règle

## Provenance du contrôle

- Date : 11 octobre 2026.
- Outil : MCP Opquast.
- Version demandée : `qualite-numerique`.
- État du serveur : API publique et privée disponibles ; 245 règles locales ; alignement local indiqué au 3 septembre 2026.
- Source effectivement retournée pour chaque règle : `api`.
- Usage : contrôle uniquement. Aucun contenu absent des deux Markdown n'est ajouté à la série.

## Résultats

### Règle 72

- Libellé API : « Le format de saisie des champs de formulaire qui le nécessitent est indiqué. »
- Verdict : conforme à `SB:303` et au cas décrit dans `SB:237-247` et `DA:220-239`.
- Contrôle utile : la réponse détaillée évoque explicitement les champs de mots de passe dans l'explication.

### Règle 87

- Libellé API : « Les processus complexes sont accompagnés de la liste de leurs étapes. »
- Verdict : conforme à `SB:304`, `SB:273-283` et `DA:284-298`.
- Contrôle utile : les objectifs API confirment la visibilité sur l'ordre et la durée du processus ; le contrôle porte sur la présence de la liste des étapes.

### Règle 140

- Libellé API : « Les liens sont visuellement différenciés du reste du contenu. »
- Verdict : conforme à `SB:305`.

### Règle 152

- Libellé API : « Tous les liens internes sont valides. »
- Verdict : conforme à `SB:306`, `SB:189-199` et `DA:167-175`.
- Contrôle utile : l'API confirme la recherche de liens internes menant à une erreur 404 et distingue le résultat des contrôles périodiques proposés comme solution.

### Règle 155

- Libellé API : « Il est possible de revenir à la page d’accueil depuis toutes les pages. »
- Verdict : conforme à `SB:307`.

### Règle 156

- Libellé API : « Chaque page affiche une information permettant de connaître son emplacement dans l’arborescence. »
- Verdict : conforme à `SB:308`.

### Règle 159

- Libellé API : « Les icônes de navigation sont accompagnées d’une légende explicite. »
- Verdict : conforme à `SB:309`.

### Règle 168

- Libellé API : « Un moteur de recherche interne est proposé. »
- Verdict : conforme à `SB:310`.

### Règle 223

- Libellé API : « Le serveur envoie une page d’erreur 404 personnalisée. »
- Verdict : conforme à `SB:311` et au contraste décrit dans `SB:153-163`.

### Règle 224

- Libellé API : « Le serveur envoie une page d’interdiction 403 personnalisée. »
- Verdict : conforme à `SB:312` et au contraste décrit dans `SB:153-163`.

### Règle 233

- Libellé API : « Le codage de caractères utilisé est UTF-8. »
- Verdict : conforme à `SB:313`, `SB:213-223` et `DA:189-199`.
- Limite : l'API confirme le libellé et le contrôle, mais la distinction entre nom du codage et seuil empirique reste sourcée uniquement dans les deux Markdown.

## Recherche documentaire complémentaire

- Requête sur les six exigences du sanity check V5 : aucun passage trouvé dans le corpus documentaire MCP.
- Requête sur le consensus et la gestion des conflits : aucun passage trouvé dans le corpus documentaire MCP.
- Décision : ne pas enrichir ni corriger les deux Markdown. Les affirmations correspondantes restent rattachées à `SB:28-34`, `SB:165-175`, `SB:225-235`, `DA:24-30`, `DA:129-148` et `DA:201-218`.

## Verdict de contrôle

- Règles contrôlées : 11 sur 11.
- Libellés en contradiction : 0.
- Affirmations rejetées : 0.
- Données de contrôle injectées dans les slides : 0.
- Statut : `PASS` pour préparer le storyboard ; revue documentaire des ateliers V5 limitée aux deux Markdown.
