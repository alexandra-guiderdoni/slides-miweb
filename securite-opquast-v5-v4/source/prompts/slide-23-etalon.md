# Prompt ImageGen - slide 23 - étalon de règle V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`

Ces quatre images sont fournies directement à ImageGen. Reprendre leur grammaire visuelle, leur hiérarchie typographique, leur respiration et leur niveau de finition sans recopier leur contenu.

## Fiche PDS

- Rôle : expliquer la règle 214 sans supposer que le public connaît SRI.
- Idée principale : l'origine autorisée ne suffit pas, le navigateur compare l'empreinte du fichier reçu à celle attendue.
- Scène : une chaîne courte entre serveur tiers, fichier, calcul d'empreinte et navigateur.
- Transformation visible : le fichier n'est accepté que lorsque les deux empreintes correspondent.
- Ce que l'image doit faire comprendre : `integrity` vérifie le fichier exact, pas seulement son domaine d'origine.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement la direction artistique des quatre références fournies : fond ivoire presque blanc, titre bleu marine, composition éditoriale aérée, aplats pastel doux, illustrations vectorielles plates aux traits fins, formes organiques discrètes, hiérarchie immédiate en trois secondes. Typographie française sans sérif proche de Marianne. Aucun dégradé, aucune photographie, aucune 3D, aucune ombre lourde, aucun faux logo.

Masque stable : micro-entête en haut à gauche, grand titre sous le micro-entête, petit repère de chapitre et badge de règle en haut à droite, mécanisme central en trois étapes, bande d'impact corail et bande de garantie verte, callout technique bleu très clair en bas, footer bas gauche et pagination bas droite.

Mécanisme central très simple : à gauche, un serveur tiers envoie un fichier JavaScript ; au centre, le navigateur calcule une empreinte `sha384` ; à droite, deux empreintes identiques s'alignent puis une coche verte autorise le fichier. Ajouter une petite croix corail sur un second fichier dont l'empreinte diffère. Ne pas représenter le hachage comme un chiffrement ou un secret.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 214`
- `Vérifier le fichier exact, pas seulement son origine`
- `IMPACT - Une ressource tierce modifiée peut être exécutée.`
- `Empreinte reçue = empreinte attendue`
- `GARANTIE - Le navigateur accepte le fichier attendu.`
- `integrity="sha384-..."`
- `SRI - Subresource Integrity`
- `Opquast - présentation Miweb`
- `23 / 30`

Priorités de lecture : 1. le titre ; 2. la comparaison d'empreintes ; 3. impact et garantie ; 4. le code `integrity`.

Critères de rejet : texte manquant ou ajouté, mauvais numéro, mauvaise pagination, faute dans `sha384`, `integrity` ou `Subresource Integrity`, confusion entre hachage et chiffrement, faux logo, schéma technique surchargé ou composition éloignée des références.
