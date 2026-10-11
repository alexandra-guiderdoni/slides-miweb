# Vérification Opquast — Projets et livrables

## Méthode

- Référence : MCP Opquast, API `qualite-numerique`.
- Date : 11 octobre 2026.
- Usage : confirmation ou rejet du contenu déjà présent dans les Markdown.
- Aucun contenu de cette vérification n’est ajouté aux slides.

## Résultats

| Règle | Libellé du Markdown | Source MCP | Verdict |
|---|---|---|---|
| 234 | Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. | API | Confirmé |
| 77 | Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. | API | Confirmé |
| 69 | Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. | API | Confirmé |
| 85 | La soumission d’un formulaire est suivie d’un message indiquant la réussite ou non de l’action souhaitée. | API | Confirmé |
| 222 | Le serveur envoie un code HTTP 404 pour les ressources non trouvées. | API | Confirmé |

Les synthèses de contrôle présentes dans le storyboard correspondent aux
contrôles API récupérés. L’API confirme aussi la coexistence actuelle de
libellés de phases différents selon les règles étudiées, sans contredire la
prudence formulée en slide 05.

## Verdict

- Affirmation rejetée : 0.
- Contradiction : 0.
- Donnée non vérifiée : 0 parmi les cinq règles.
- Contenu externe ajouté à la production : 0.
