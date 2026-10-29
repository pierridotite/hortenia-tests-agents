# Essai des outils iOS (sans l'app Hortenia)

Le simulateur montre l'app Réglages. Vérifie que les outils marchent, en une
quinzaine de gestes au plus, avec les commandes de CONSIGNES_CLAUDE_IOS.md
(section Outils), captures dans `resultats/essai`.

1. Capture l'écran : la langue est-elle le français ? Les centres listés tombent-ils sur les bons éléments de l'image ?
2. Touche une ligne (par exemple « Général »), capture, puis reviens avec `geste.sh retour` et capture.
3. Fais défiler vers le bas puis vers le haut.
4. Touche le champ de recherche, capture : le clavier à l'écran est-il visible ?
5. Écris « tomates cerises » avec ecrire.py, capture : le texte est-il bien écrit ? Le clavier est-il toujours visible ?
6. Réécris « basilic » : l'ancien texte est-il bien remplacé ?
7. `geste.sh accueil`, capture.

Écris `resultats/rapport.md` : pour chaque point, OK ou le problème exact
(avec le n° de capture), puis les réglages à corriger dans les outils.
