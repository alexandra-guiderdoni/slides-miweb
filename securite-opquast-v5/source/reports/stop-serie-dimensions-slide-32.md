# Arrêt de série — Sécurité

## Verdict

`STOP_SERIE` le 12 octobre 2026.

La candidate `slide-32-a001.png` mesure 1671 × 941 px. Une mise à l’échelle proportionnelle à 1672 px de large donne 942 px de haut après arrondi. Le goal autorise uniquement une transformation vers 1672 × 941 lorsque la hauteur proportionnelle s’arrondit déjà à 941 px.

Aucun recadrage, remplissage ou redimensionnement non proportionnel n’a été effectué. La copie placée prématurément dans `finals/` a été retirée ; la candidate originale et son empreinte restent conservées.

## Déviation tracée

La candidate de la slide 35 a été générée dans le même appel orchestré avant observation du résultat dimensionnel de la slide 32. Elle est conservée dans `candidates/`, mais n’a pas été acceptée ni copiée dans `finals/`.

## État des étalons

- Slide 01 : `VALIDEE_PRODUCTION`.
- Slide 09 : `VALIDEE_PRODUCTION`.
- Slide 32 : `STOP_SERIE`.
- Slide 35 : `NOT_REVIEWED_AFTER_STOP_SERIE`.

## Action requise

Arbitrage humain explicite nécessaire avant toute nouvelle tentative ou transformation de la slide 32. L’ordre séquentiel interdit de poursuivre « Sécurité » ou de commencer « Performance » tant que ce blocage n’est pas levé.

