# Prompt ImageGen - slide 20 - étalon d'éclairage V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`

Ces quatre images sont fournies directement à ImageGen. Reprendre leur grammaire visuelle, leur hiérarchie typographique, leur respiration et leur niveau de finition sans recopier leur contenu.

## Fiche PDS

- Rôle : montrer qu'une ancienne réponse technique ne satisfait plus la règle 210.
- Idée principale : contrôler une protection XSS actuelle et applicable, pas rechercher mécaniquement un ancien entête.
- Scène : une développeuse inspecte deux réponses serveur, écarte l'ancien mécanisme et vérifie une politique actuelle.
- Transformation visible : ancien mécanisme barré, mécanisme actuel inspecté, contrôle explicite.
- Ce que l'image doit faire comprendre : les deux mécanismes ne sont pas équivalents.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement la direction artistique des quatre références fournies : fond ivoire presque blanc, titre bleu marine, composition éditoriale aérée, aplats pastel doux, illustrations vectorielles plates aux traits fins, formes organiques discrètes, hiérarchie immédiate en trois secondes. Typographie française sans sérif proche de Marianne. Aucun dégradé, aucune photographie, aucune 3D, aucune ombre lourde, aucun faux logo.

Masque stable : micro-entête en haut à gauche, grand titre sous le micro-entête, petit repère de chapitre et badge de règle en haut à droite, comparaison centrale, bande d'impact corail et bande de garantie verte bien distinctes, callout bleu très clair en bas, footer bas gauche et pagination bas droite.

Scène centrale : une développeuse devant un panneau d'inspection des entêtes HTTP. À gauche, une petite carte ancienne `X-XSS-Protection` barrée sobrement en corail. À droite, une carte actuelle `Content-Security-Policy active` reliée à un navigateur et cochée en vert. Une flèche à sens unique va de l'ancien mécanisme vers le contrôle actuel. Ne jamais suggérer une équivalence entre les deux cartes.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 210`
- `La règle 210 ne demande plus X-XSS-Protection`
- `IMPACT - Un script injecté peut s'exécuter dans la page.`
- `X-XSS-Protection - obsolète ou déprécié`
- `Content-Security-Policy active`
- `GARANTIE - Une protection explicite et actuelle est transmise.`
- `CONTRÔLE - Vérifier un mécanisme transmis et applicable`
- `Opquast - présentation Miweb`
- `20 / 30`

Priorités de lecture : 1. le titre ; 2. l'opposition ancien et actuel ; 3. impact et garantie ; 4. le contrôle.

Critères de rejet : texte manquant ou ajouté, faute dans `X-XSS-Protection` ou `Content-Security-Policy`, recommandation de l'ancien entête, promesse qu'une CSP présente est forcément efficace, faux logo, mauvais numéro, mauvaise pagination, composition dense ou éloignée des références.
