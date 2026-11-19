# Contrôle court 1.8.5 : vue 3D (cadrage des parties, glissé, netteté), avec Plus

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Mission courte : environ 70 gestes, 50 minutes au plus. Ne touche à rien d'autre que ce qui est demandé.
Aucun achat, même d'essai : Plus vient d'un compte de test.

## Démarrage
1. Lance l'app et attends l'écran d'accueil. Tout de suite (avant toute capture), prends le compte de test :
   `python3 outils/site_tests.py compte plus` (e-mail affiché ; mot de passe tapé par `ecrire.py @mdp-compte`,
   jamais affiché). Si l'outil répond « identifiant d'appareil introuvable », relance l'app et recommence aussitôt.
2. Fais l'onboarding au plus court (version libre), en traçant la zone du jardin sur la carte et en ajoutant les
   plantes proposées, jusqu'au jardin. Ferme le paywall sans rien acheter.
3. Connecte-toi avec le compte de test (Profil > « J'ai déjà un compte » ou « Sauvegarder mon jardin » > e-mail).
   Vérifie que Plus est actif (badge « Membre Hortenia Plus » ou Paramètres > Abonnement).
4. **Le jardin en parties.** Onglet Jardin > Aménager > « Ajouter une partie » : trace au moins deux parties
   en plus de la première, avec une plante ou un arbre dans chacune. Une des parties doit être **loin** des
   autres : 60 m ou plus (sur la carte, déplace-toi avant de tracer ; l'appli refuse au-delà de 150 m).
   Si tracer la partie éloignée prend plus de 15 minutes, garde des parties proches et dis-le : seul P1 en a besoin.
5. Onglet Jardin, vue 3D.

## Captures
Comme d'habitude, plus une copie en pleine définition quand c'est demandé :
- iPhone : `python3 outils/ios/ecran.py resultats/<persona> <NN> pleine` (écrit `<NN>.png` et `<NN>-pleine.png`).
- Android : `python3 outils/ecran.py resultats/<persona> <NN> pleine`.

Glisser d'un doigt, lentement, depuis le milieu de la vue 3D :
- iPhone : `bash outils/ios/geste.sh glisser X1 Y1 X2 Y2` (en points).
- Android : `adb shell input swipe X1 Y1 X2 Y2 800` (en pixels) ; 100 points = 100 × densité / 160 pixels
  (densité lue par `adb shell wm density`). Note la densité dans le rapport.

Mesure entre deux captures : `python3 -I outils/mesure_glisse.py A.png B.png [échelle]`
(échelle : rien pour les captures `<NN>.png` d'iPhone, à 1 pixel par point ; Android, `<NN>.png` à la moitié de
l'écran : 320 / densité). Si l'outil répond « terrain introuvable », mesure à l'œil et dis-le.

## Points (P1 à P3 sur iPhone et Android ; P4 à P6 sur iPhone seulement)
- **P1 Ouverture.** Capture pleine définition. Attendu : la vue montre le groupe de parties principal, lisible ;
  la partie éloignée n'est pas à l'écran (l'ancien build montrait tout le jardin, minuscule).
- **P2 Le jardin suit le doigt (décisif).** Capture A. Glisser de 100 points vers la droite et 50 vers le haut.
  Capture B. Attendu : (+100, -50) à 3 points près. Glisser encore de 100 points vers la gauche. Capture C,
  attendu contre A : (0, -50). Capture tout de suite après chaque lâcher, puis 2 s après : aucun saut.
- **P3 « Recentrer »** (le dernier bouton rond en bas à droite de la vue, icône aux quatre coins ; l'autre rond
  tourne le jardin). Un appui par seconde, une capture après chaque appui. Attendu : d'abord le cadrage de P1,
  puis chaque partie l'une après l'autre, puis tout le jardin, puis de nouveau P1 (autant de cadrages que de
  parties, plus deux). Passage animé, sans saut à l'arrivée.
- **P4 Netteté.** Sur une partie cadrée par « Recentrer », sans pincer : capture pleine définition. Attendu :
  plantes, traits du sol et bords du socle nets au pixel (pas de pavés). Ouvre la capture et regarde un détail.
- **P5 Quart de tour** (le rond à la flèche) sur cette partie cadrée. Capture pleine définition. Attendu : la même
  partie reste cadrée, nette.
- **P6 Plan, puis 3D.** Capture. Attendu : retour au cadrage de P1, de face.
- **P7** Quitter la 3D (autre onglet) puis y revenir : pas d'écran blanc, pas de plantage.

Le pincement n'est pas demandé (aucun outil ne le fait ici). Sur Android, les animaux sont figés au banc : c'est voulu.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : Plus actif (preuve), nombre de parties et distance de la partie éloignée, mesures de P2.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | mesure | ce que tu as vu |` pour P1 à P7.
3. Autres bugs vus, du plus grave au moins grave.
