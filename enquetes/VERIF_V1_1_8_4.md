# Contrôle court 1.8.4 (build 115/152) : vue 3D nette au pincement, avec Plus

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Mission courte : environ 50 gestes, 40 minutes au plus. Ne touche à rien d'autre que ce qui est demandé.
Aucun achat, même d'essai : Plus vient d'un compte de test.

## Démarrage
1. Lance l'app et attends l'écran d'accueil. Tout de suite (avant toute capture), prends le compte de test :
   `python3 outils/site_tests.py compte plus` (e-mail affiché ; mot de passe tapé par `ecrire.py @mdp-compte`,
   jamais affiché). Si l'outil répond « identifiant d'appareil introuvable », relance l'app et recommence aussitôt.
2. Fais l'onboarding au plus court (version libre), en traçant la zone du jardin sur la carte et en ajoutant les
   plantes proposées, jusqu'au jardin. Ferme le paywall sans rien acheter.
3. Connecte-toi avec le compte de test (Profil > « J'ai déjà un compte » ou « Sauvegarder mon jardin » > e-mail).
   Vérifie dans Profil que Plus est actif. Si le compte n'a pas de jardin, crée-en un (Aménager ou « + »), avec au
   moins un arbre fruitier (pommier) et une serre si l'appli le propose.

## Vérifications (un verdict par ligne, capture avant et après chaque geste)
- **V1a Ouverture** : sur l'écran du jardin, passe en vue 3D. La vue s'ouvre, le jardin est cadré, rien ne clignote.
- **V1b Zoom au plus près** : pince pour zoomer jusqu'au maximum sur un arbre, puis sur la serre (ou sur une planche
  s'il n'y a pas de serre). Les contours restent nets (pas de flou, pas d'escaliers marqués, pas de texture pâteuse).
  Compare avec la capture d'avant le zoom.
- **V1c Déplacer** : après le zoom, fais glisser le jardin d'un doigt : il suit le doigt sans saut, et reste net.
- **V1d Recentrer** : touche « recentrer » (ou le bouton qui recadre) : le jardin revient entier, cadré.
- **V1e Retour** : quitte la 3D puis reviens-y : pas d'écran blanc, pas de plantage.

Outil de pincement : `bash outils/ios/geste.sh` (iPhone) ou deux doigts via `adb shell input` si ton outil le permet ;
si le pincement est impossible avec tes outils, essaie les boutons de zoom de la vue s'il y en a, et dis-le.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : Plus actif (preuve), 3D ouverte, netteté au zoom.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | ce que tu as vu |` pour V1a à V1e.
3. Autres bugs vus, du plus grave au moins grave.
