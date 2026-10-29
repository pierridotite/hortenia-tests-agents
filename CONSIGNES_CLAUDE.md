# Mission : tester l'app Hortenia comme de vrais utilisateurs

Tu pilotes un téléphone Android virtuel (émulateur) où l'app Hortenia (potager,
paquet com.hortenia.app) est installée. Tu joues tour à tour chaque persona de
`personas.json` (ou seulement celles de la variable PERSONAS si elle n'est pas
vide), pour trouver les bugs, plantages et blocages qu'un vrai utilisateur
rencontrerait. Tu rends un rapport précis et vérifiable.

## Outils (uniquement ceux-ci)
- Voir l'écran : `python3 outils/ecran.py resultats/<persona> <NN>` (NN = 01, 02…),
  puis lis l'image produite avec Read. Les positions listées sont en pixels réels.
- Toucher : `adb shell input tap X Y`
- Écrire dans le champ actif (remplace son contenu) : `python3 outils/ecrire.py "texte"`
- Faire défiler : `adb shell input swipe 540 1700 540 700 300` (voir la suite), l'inverse pour remonter
- Retour / fermer le clavier : `adb shell input keyevent 4`
- Nouvelle persona : `adb shell pm clear com.hortenia.app` puis
  `adb shell monkey -p com.hortenia.app -c android.intent.category.LAUNCHER 1` et attends 6 s (`sleep 6`).

## Règles (impératives)
- Ne paie jamais rien, n'accepte aucun achat ni abonnement. Tu peux ouvrir l'écran d'abonnement et le fermer.
- Ne publie rien dans la communauté, ne commente pas, ne signale personne, n'envoie aucun avis ni message au support : ce sont de vrais utilisateurs.
- Au plus une question à l'assistant HortenIA et un diagnostic photo par persona (une photo de feuille de tomate est dans la galerie).
- Compte par e-mail uniquement (pas Google, pas Apple) : adresse `success+agent-<persona>-<RUN_ID>@simulator.amazonses.com`, mot de passe `Potager-<6 derniers chiffres de RUN_ID>!`. RUN_ID est dans la variable d'environnement.
- Environ 25 gestes par persona, puis passe à la suivante.
- Joue la persona honnêtement (sa patience, son aisance), mais reste un testeur : note tout ce qui cloche.

## Ce que tu écris
- Après chaque persona : `resultats/<persona>/journal.md`, chaque geste en une ligne (n° de capture, geste, ce qui s'est passé), puis les problèmes vus.
- À la fin : `resultats/rapport.md` en français :
  1. Résumé en 5 lignes.
  2. Bugs et plantages, du plus grave au moins grave. Pour chacun : persona, capture(s), étapes pour reproduire, résultat obtenu, résultat attendu, gravité (bloquant / gênant / mineur).
  3. Blocages et confusions d'usage (même format, plus court).
  4. Ce qui marche bien.
  5. Les 5 corrections prioritaires.
  6. Impressions de la persona, à la première personne et avec sa voix : note sur 10, ce qui plaît, ce qui agace, ce qui manque, garderait-elle l'app au-delà d'une semaine, paierait-elle Hortenia Plus (29,99 €/an ou 4,99 €/mois) et pourquoi, la recommanderait-elle et à qui, et une idée d'amélioration du produit.
  Distingue ce que tu as vu de ce que tu supposes, et signale les limites de l'émulateur (pas de Google Play, appareil photo virtuel…) plutôt que d'en faire des bugs de l'app.
