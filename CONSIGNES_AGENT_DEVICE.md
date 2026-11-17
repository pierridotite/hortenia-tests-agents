# Outil d'appareil : agent-device (remplace les touchers par coordonnées)

Pour ce test, l'appareil se pilote avec `agent-device` (CLI de Callstack, licence MIT).
Il lit l'arbre d'accessibilité de l'écran et donne à chaque élément une référence
(`@e12`) : tu touches l'élément par sa référence ou par son libellé, sans calculer de
coordonnées. Les règles, la mission et le rapport restent ceux des consignes.

## Démarrage (une fois)
- Android : `agent-device open com.hortenia.app --platform android`
- iPhone : `agent-device open com.hortenia.app --platform ios`

## Gestes
- Lire l'écran (textes, boutons, champs, avec leurs références) : `agent-device snapshot -i`
- Toucher : `agent-device press @e12 --settle` (ou par libellé : `agent-device press 'label="Continuer"' --settle`)
- Appui long : `agent-device longpress @e12 800`
- Écrire dans un champ (remplace son contenu) : `agent-device fill @e5 "texte"`
- Faire défiler : `agent-device scroll down` (ou `up`) ; jusqu'à un élément : `agent-device scroll down --until 'label="Mes graines"'`
- Retour : `agent-device back` ; fermer le clavier : `agent-device keyboard dismiss`
- Fenêtre système (autorisation, alerte) : `agent-device alert get`, puis `alert accept` ou `alert dismiss`
- Toucher par coordonnées, seulement si l'élément n'a pas de référence (carte, dessin du
  jardin) : `agent-device press X Y` (points de l'écran, lus sur une capture `--overlay-refs`)

`--settle` attend que l'écran se calme et renvoie ce qui a changé : souvent, pas besoin
d'un nouveau `snapshot -i`. Une référence n'est plus valable après un geste : reprends
celle du dernier `snapshot -i` ou de la dernière réponse `--settle`.

## Captures (toujours, pour le rapport)
- `agent-device screenshot resultats/<persona>/<NN>.png` (NN = 01, 02…), puis lis l'image
  avec Read quand l'aspect compte (texte coupé, chevauchement, couleurs). Le `snapshot`
  ne montre pas la mise en page : une capture reste la preuve de ce que tu décris.

## Mesures en plus (à joindre au rapport quand elles éclairent un défaut)
- Journal de l'app : `agent-device logs clear --restart` avant un geste, puis
  `agent-device logs path` et un `grep` ciblé dans ce fichier (jamais tout le journal).
- Requêtes réseau récentes : `agent-device network dump 20`
- Fluidité (images perdues) : `agent-device perf frames --json` juste après un défilement
  ou une animation lente.

## Ce qui ne change pas
- Nouvelle persona : les commandes des consignes (Android : `pm clear` puis relance ;
  iPhone : celles de CONSIGNES_CLAUDE_IOS.md), puis `agent-device open … --relaunch`.
- Les outils des consignes restent permis si agent-device bloque sur un écran : note-le
  dans le journal (écran, commande, message).
- Dans le rapport, ajoute une ligne « Outil » : nombre de gestes faits avec agent-device,
  écrans où il a fallu des coordonnées, blocages de l'outil.
