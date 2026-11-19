# Mission 1.8.5 refaite (build 118/155) : vérifier les correctifs et les retours de la Communauté

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona.
Environ 80 gestes, jusqu'à 70 minutes. Une vérification bloquée ne t'arrête pas : note-la et passe.
Aucun achat, même d'essai. Aucune question à HortenIA, aucun diagnostic photo, aucun code de parrainage.
**Ne publie JAMAIS rien dans la Communauté** : aucun post, aucun commentaire, aucune réaction (règle de Pierre, 19/11).
Messagerie : seulement avec des comptes de test ; groupes TOUJOURS « sur invitation », fermés à la fin ; jamais « Signaler ».

## Démarrage
1. Lance l'app. Tout de suite, prends le compte de ta ligne : `python3 outils/site_tests.py compte plus` (Plus) ou
   `python3 outils/site_tests.py compte email` (gratuit) ; mot de passe tapé par `ecrire.py @mdp-compte`, jamais affiché.
2. raymond seulement : `python3 outils/site_tests.py imposer T43=A`, puis relance l'app.
3. Accueil au plus court (lieu de ta ligne, plantes proposées) jusqu'au jardin ; paywall fermé sans rien acheter.
4. Connecte-toi avec le compte de test (Profil > « J'ai déjà un compte » ou « Sauvegarder mon jardin » > e-mail).

## Codes
**C, correctifs du passage d'avant**
- C1 Android 15 : détail d'un calcul, champ « Autre » (correction du pH) puis « Azote à apporter » (Engrais > « Je connais
  le besoin exact ») : le champ remonte au-dessus du clavier, avec une marge.
- C2 Liste des calculs avec le panneau « Votre jardin » ouvert (surface vide : ne la remplis pas avant) : défile en bas,
  ouvre « Mon sol », reviens par la flèche, puis refais avec le retour Android : la liste revient à sa place, panneau ouvert.
- C3 iPhone SE, texte très gros, fin de l'accueil (version A) : photo plus basse, bande des 7 jours entière au-dessus du pied,
  barre de défilement montrée un instant. Glisse depuis la photo ou le titre (pas depuis le pied) : la page défile.
- C4 Allemand, écran du jardin : « Erinnerungen und Frostwarnung » entière au-dessus de « Benachrichtige mich » ;
  « Mein Gemüsegarten » entier, « Öffnen » dessous en texte agrandi.
- C5 Bandeau des calculs en texte agrandi : le type de sol entier sur sa propre ligne.
- C6 Messagerie, groupe sur invitation avec un compte de test : envoi de 2 ou 3 photos d'un coup ; le bloc s'affiche tout de
  suite avec un indicateur d'envoi, puis les photos ; un second envoi fait un second bloc (pas de fusion).
  Photo choisie à la création du groupe : visible tout de suite dans le formulaire. Ferme le groupe à la fin.
- C7 Conversation privée sans message : l'en-tête ne dit pas « Demande envoyée » avant ton premier message.
- C8 Fiche d'un groupe : la dernière ligne est entière, sans barre d'onglets dessous.

**R, retours depuis la Communauté** (le détail attendu est dans `enquetes/RETOURS_COMMUNAUTE_1_8_5.md` : lis-le).
À chaque ligne, trois façons de revenir : flèche, glissé du bord (iPhone), retour Android. Ne fais que naviguer.
- R1 Fil : règles de la communauté, discussion d'un post, page d'un membre, un post de cette page, Messages.
- R2 Messages : une discussion, page d'un membre, fiche d'un groupe, demandes, onglet Groupes, « Créer un groupe » (revenir
  sans créer ; Android : à refaire dans ta langue), « Nouveau message » (revenir sans choisir).
- R3 Changer d'onglet : un écran ouvert dans la Communauté, autre onglet, puis Communauté : le même écran, sans
  rechargement ; Paramètres ouverts dans Profil, Communauté, puis Profil : Paramètres, sans saut ni chargement visible ;
  toucher l'onglet déjà ouvert : son début.
Note pour chaque écart : écran de départ, geste, écran atteint, l'heure, et si un chargement s'est vu.

## Ta ligne
| Persona | Compte | Lieu | À faire |
|---|---|---|---|
| sophie | Plus | Nantes | C1, C2 ; R1, R3 (retour Android) |
| yves | gratuit | Lyon | Android 10, texte x1,3 : C2 (surface vide !), C5 ; R1, R2 |
| lukas | gratuit | Berlin | allemand : R1 à R3 (dont « Neue Gruppe ») ; C5, C7 |
| raymond | gratuit | Le Mans | iPhone SE, très gros texte : C3 (version A), C5 ; R1, R3 |
| hanna | Plus | Köln | iPhone SE, allemand, très gros texte : C4, C6, C8 ; R2 |
| oliver | gratuit | London | anglais : C6, C7, C8 ; R2, R3 |
| kevin | Plus | Toulouse | R1 à R3 (glissé du bord à chaque ligne) ; C7 |

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : un plantage, un écran bloqué ou un retour faux vu ou non ; le plus gênant ; ce que tu as écrit
   dans la messagerie et supprimé.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | ce que tu as vu |`.
3. Autres bugs vus, du plus grave au moins grave.
