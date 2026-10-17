# Prompt ImageGen - slide 14

## Fiche PDS

- Rôle : distinguer création d’un nouveau secret et interdiction de divulguer l’ancien.
- Scène : un lien temporaire mène à un nouveau formulaire tandis qu’une enveloppe ne contient jamais le secret.
- Transformation : la récupération du compte aboutit à un nouveau mot de passe, pas à la restitution de l’ancien.
- Continuité : répond au cas de l’oubli et prépare la solution de repli de la règle 215.
- Contrainte critique : aucun mot de passe lisible dans l’image.

## Prompt complet

Cas d’usage : infographic-diagram.
Type d’actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Reprendre exactement le masque clair des étalons validés : fond blanc, en-tête et chapitre en haut, badge bleu clair, titre bleu marine, scène centrale, contrôle bleu clair en bas, limite orange, footer bas gauche et pagination bas droite. Illustration plate, traits fins, bleu institutionnel, vert de validation et corail uniquement pour l’interdit. Marianne obligatoire, Arial en fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : flux de gauche à droite. Une enveloppe contient uniquement un lien temporaire, puis une flèche mène à un formulaire où la personne crée un nouveau mot de passe. À côté, l’ancien secret est masqué et barré en corail. Faire comprendre visuellement `Réinitialiser ≠ restituer` sans afficher de secret réel. Le contrôle et la limite occupent deux cartouches alignés en bas.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `B - MAÎTRISE DU COMPTE`
- `RÈGLES 204 ET 205`
- `Réinitialiser n'est pas restituer l'ancien secret`
- `204 - Créer un nouveau mot de passe`
- `205 - Ne jamais envoyer le mot de passe en clair`
- `Réinitialiser ≠ restituer`
- `CONTRÔLE - Suivre la procédure sans être connecté et examiner le courriel reçu`
- `LIMITE - Ne jamais utiliser de compte réel ou de donnée personnelle dans la démonstration`
- `Opquast - présentation Miweb`
- `14 / 30`

Contraintes critiques : ne montrer aucun mot de passe, même fictif ; ne pas écrire que l’ancien secret est récupéré ; conserver le symbole `≠` ; aucun texte parasite.
