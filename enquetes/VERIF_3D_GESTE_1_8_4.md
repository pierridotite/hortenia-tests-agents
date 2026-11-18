# Contrôle court 1.8.4 : la vue 3D suit le doigt (correctif des saccades), avec Plus

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
   Vérifie dans Profil que Plus est actif. Si le compte n'a pas de jardin, crée-en un avec au moins un arbre.
4. Onglet Jardin, vue 3D ouverte, jardin cadré (touche « Recentrer » une fois).

## Gestes mesurés
Glisser d'un doigt, lentement, depuis le milieu de la vue 3D :
- iPhone : `bash outils/ios/geste.sh glisser X1 Y1 X2 Y2` (en points).
- Android : `adb shell input swipe X1 Y1 X2 Y2 800` (en pixels) ; 100 points = 100 × densité / 160 pixels
  (densité lue par `adb shell wm density`). Note la densité dans le rapport.

Mesure entre deux captures : `python3 -I outils/mesure_glisse.py A.png B.png [échelle]`
(échelle : rien si les captures sont à 1 pixel par point, `0.5` à 2 pixels par point ; Android : 160 / densité).
Si l'outil répond « terrain introuvable », mesure à l'œil sur les captures et dis-le.

- **G1** Capture A. Glisser de 100 points vers la droite et 50 vers le haut. Capture B. Attendu : (+100, -50) à 3 points près
  (l'ancien build donnait (+150, -75)).
- **G2** Glisser encore de 100 points vers la gauche. Capture C. Attendu contre A : (0, -50).
- **G3** « Recentrer ». Capture D. Attendu contre A : (0, 0).
- **G4** Glisser de 100 points, puis Plan, puis 3D. Capture E. Attendu contre A : (0, 0), jardin cadré.
- **G5** Pendant et juste après chaque glissé (capture tout de suite après le lâcher, puis 2 s après) : le jardin ne saute
  pas et ne bouge plus au lâcher ; le dessin reste net.
- **G6** Quitter la 3D (autre onglet) puis y revenir : pas d'écran blanc, pas de plantage.

Le pincement n'est pas demandé (aucun outil ne le fait ici).

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : Plus actif (preuve), mesures de G1 à G4, saut ou non au lâcher.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | mesure | ce que tu as vu |` pour G1 à G6.
3. Autres bugs vus, du plus grave au moins grave.
