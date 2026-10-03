# Composition de l'étalon 03

La première candidate ImageGen redessinait les documents A et B. Elle est conservée dans `candidates/slide-03-redessinee.png` et n'est pas le visuel retenu.

Le fond retenu est `candidates/slide-03-fond.png`, produit par ImageGen avec deux zones d'insertion vides. Les fichiers de `source-images/` sont des copies octet pour octet des PNG du dépôt source. Les deux originaux ont la même empreinte SHA-256 : `d5f46f9339fae3b26a9f9d8435ccf342d66e4cfeffc74c913f2847524648705d`.

Pour chaque image, la composition retire les marges transparentes par un recadrage de 860 × 1160 pixels à partir de (95, 160), puis la met à l'échelle de 424 × 572 pixels avec le filtre Lanczos. Les insertions sont placées à (227, 293) et (1020, 293). Le même traitement et le même fond sont appliqués aux deux panneaux. Les images sources restent intactes ; seul leur affichage dans la slide est redimensionné.

Le résultat publié est `../assets/slides/slide-03.png` en 1672 × 941 pixels. Il conserve le titre, la question et les libellés du fond ImageGen, et présente les deux aperçus sources sans indice de réponse. La recompression du fichier publié n'a pas modifié ses pixels.
