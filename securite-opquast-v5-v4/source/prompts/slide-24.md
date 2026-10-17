# Prompt ImageGen - slide 24 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-20.png` - étalon V4 le plus proche

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : atelier de synthèse du chapitre C.
- Idée principale : chercher des preuves complémentaires dans les entêtes et le code source.
- Scène : une développeuse inspecte deux panneaux de même importance.
- Transformation visible : les indices convergent vers un verdict prudent.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement les cinq références : fond ivoire presque blanc, titre bleu marine massif, composition aérée, aplats pastel doux, illustration vectorielle plate aux traits fins, typographie proche de Marianne. Aucun dégradé, photographie, effet 3D, ombre lourde ni faux logo.

Masque V4 stable : micro-entête haut gauche, repère de chapitre haut droit, grand titre, deux panneaux centraux équilibrés, verdict bleu clair, footer et pagination.

Scène : une développeuse inspecte à gauche un panneau `ENTÊTES` et à droite un panneau `CODE SOURCE`. Les quatre lignes d'entêtes et l'unique extrait HTML sont grands, exacts et lisibles. Des loupes sobres convergent vers le verdict. Afficher clairement une référence discrète aux règles 206, 207, 210, 211, 212 et 214, sans ajouter de texte au-delà de la liste blanche : utiliser le repère exact `RÈGLES 206 · 207 · 210 · 211 · 212 · 214`.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLES 206 · 207 · 210 · 211 · 212 · 214`
- `Atelier : lire les entêtes et le code source`
- `ENTÊTES`
- `Content-Type`
- `X-Content-Type-Options: nosniff`
- `Content-Security-Policy`
- `X-Frame-Options ou frame-ancestors`
- `CODE SOURCE`
- `integrity="sha384-..."`
- `VERDICT - Présent, valide ou indéterminé ?`
- `Opquast - présentation Miweb`
- `24 / 30`

Critères de rejet : texte manquant ou ajouté, faute, mauvais numéro ou pagination, références de règles absentes, ponctuation technique altérée, code supplémentaire, capture illisible, faux logo.
