# Mission 1.8.1 : barre Android, code, notifications, avatars, Mes graines, tracé du jardin

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad), avec les changements ci-dessous. Ta persona (appareil, jardin, langue, type de compte) est dans
`personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona (champ « langue » ; fr-FR
si absent) : tape les textes à toucher dans la langue de l'écran. Compte environ 80 gestes, jusqu'à 75 minutes. Ne rends
pas le rapport avant d'avoir donné un verdict à chaque ligne. Une vérification bloquée ne t'arrête pas : note-la et passe
à la suivante.

## Démarrage
- Lance l'app et attends l'écran d'accueil. Fais l'onboarding comme ta persona, jusqu'au planning.
- Personas « invite » : ne crée jamais de compte. Personas « email » : compte par e-mail après l'onboarding (règles de
  CONSIGNES). Ne paie jamais rien. N'écris jamais un mot de passe ou un jeton en clair dans le rapport.
- Ne fais jamais `pm clear`, de réinstallation ni d'effacement des données de l'app.

## Ce qui change dans la 1.8.1 (toutes les personas)
- **N1 Barre de navigation Android** (Android seulement ; iPhone : « non testable ») : en bas de l'écran, la barre système
  est crème (ou transparente sur l'app) avec des boutons foncés et bien visibles, jamais une barre grise à boutons blancs.
  Si ta persona est en thème sombre, vérifie-le aussi : note la couleur de la barre et des boutons, avec une capture, sur
  l'accueil, le planning et une feuille ouverte (par exemple une fiche plante).
- **N2 Champ « J'ai un code »** (ou sa traduction) : tape `TESTCODE0000LONG2026XYZ`, sans valider. Le texte reste dans le
  champ, rien ne dépasse ni ne passe sous un bouton. Efface, tape `TEST0000`, valide une seule fois : message clair « code
  non valable », rien ne plante. N'essaie aucun autre code.
- **N3 Notifications** : ouvre la liste des notifications de l'app. Une notification qui vient d'une personne (commentaire,
  réponse, « j'aime », nouveau post) montre sa photo ou son initiale dans un rond de couleur, plus le logo Hortenia. Les
  notifications de l'app (rappels, météo) gardent leur icône. Si une bannière apparaît dans l'app pendant le test, même
  vérification. Liste vide : « aucune notification », sans attendre plus de 2 minutes.
- **N4 Avatars de la Communauté** : dans le fil, les personnes sans photo ont un rond de couleur avec leur initiale. Les
  couleurs varient d'une personne à l'autre (potiron, blé, canard, sauge, brique, lavande, ardoise, betterave : des tons
  doux, jamais fluo ni dégradé) ; la même personne a la même couleur dans le fil, sur un commentaire et sur son profil.
  Ouvre ton propre profil : ton avatar suit la même règle.
- **N5 Mes graines** : Mes graines n'est plus dans le Planning (les rappels de semis y restent). Dans le contenu du
  jardin, sous la liste des plantes, une section Mes graines a la même mise en page que les plantes. Ajoute un sachet
  si c'est possible sans payer, vérifie qu'il apparaît, puis supprime-le.
- **N6 Tracé du jardin** : dans Aménager, touche « Retracer sur la carte » (ou sa traduction).
  - La carte se cadre sur ton jardin : le contour occupe environ la moitié de la carte, la photo est nette.
  - Tire un coin vers l'extérieur : le coin suit le doigt, le contour reste entier.
  - Tire le milieu d'un côté : le côté avance parallèlement, et sa longueur affichée change par pas de 25 cm.
  - Chaque côté affiche sa longueur, dans l'unité de ton pays, lisible et non coupée.
  - Tire un coin par-dessus le côté opposé pour croiser le contour : le geste est refusé avec une raison claire dans ta
    langue, et le contour revient à l'état d'avant.
  - Annule ou valide pour revenir à un jardin de taille normale, comme au départ.
  Personas qui créent leur jardin à l'onboarding : regarde aussi le tracé à la création (mêmes gestes, sans forcer).

## Réactions de la Communauté et écran Calculer (toutes les personas)
**Une seule cible pour réagir** : le post « Banc 1.8.1 : post de test pour les réactions. » (posté par un compte de test,
visible seulement des comptes de test ; cherche-le en haut du fil ou fais défiler). Ne pose jamais une réaction (toucher
ou choix dans la pastille) sur un autre post : son auteur, un vrai jardinier, recevrait une notification. Sur les autres
posts, tu peux ouvrir la pastille par un appui long et la refermer en touchant à côté, sans rien choisir. Si le post du
banc est introuvable, fais S1 à S3 sans rien poser (ouvrir et refermer seulement) et note-le. Retire ta réaction à la fin.
- **S1 Réagir à un post** (fil de la Communauté) : toucher le cœur d'un post sans ma réaction le remplit tout de suite et
  le nombre monte de 1 ; un second toucher retire la réaction. Appui long (un tiers de seconde) : une pastille s'ouvre
  au-dessus du bouton avec six réactions nommées (J'aime, Bravo, Ça pousse, Bon à savoir, Courage, Drôle, ou leur
  traduction). Choisir « Ça pousse » : la pastille se ferme, le bouton montre la pousse, le nombre devient terre cuite.
  Rouvrir : « Ça pousse » est surlignée. Toucher à côté ferme la pastille sans rien changer. Tirer pour rafraîchir : la
  réaction est toujours là. Puis retire-la.
- **S2 Place de la pastille** : collée juste au-dessus du bouton (quelques points d'écart), jamais trop haute au point de
  recouvrir le texte du post. Regarde sur le premier post de l'écran et sur un post du bas. Petit écran et iPhone SE : la
  pastille tient dans l'écran, les six noms sont lisibles (« Bon à savoir » sur deux lignes, c'est voulu). Post tout en
  haut sans place au-dessus : la pastille s'ouvre en dessous. Thème sombre du téléphone : la pastille reste lisible (fond
  crème voulu). Capture de chaque cas.
- **S3 La première fois** : le tout premier « j'aime » du téléphone ouvre la pastille d'elle-même, une seule fois, avec la
  ligne « Appui long sur le cœur pour retrouver ces réactions » (ou sa traduction) ; le « j'aime » est déjà posé. Un
  second « j'aime » sur un autre post ne la rouvre pas.
- **S4 Discussion et profil** : ouvre un post : même bouton, même appui long ; plus de rangée d'émojis au-dessus du champ
  « Répondre » ; les cœurs des commentaires restent de simples cœurs. Profil public d'un jardinier : « réactions reçues »
  (pas « j'aime reçus »).
- **S8 Invité** (personas « invite ») : tu ne vois pas le post du banc, donc ne touche aucun cœur. Fais un appui long
  sur le cœur d'un post : soit la pastille s'ouvre (referme-la en touchant à côté, sans rien choisir), soit l'appli propose
  de créer un compte (ne le crée pas, ferme). Jamais d'écran figé.
- **S9 Écran Calculer** (Jardin, puis Calculer) : chaque calcul est une carte avec une photo : « Mon sol » en grande carte
  en haut, puis Amendement, Correction de pH, Engrais, Besoin en eau en deux colonnes ; cadenas « Plus » sur la photo des
  calculs payants. Aucune carte grise, chaque carte ouvre le bon calcul. Allemand : la carte de l'amendement s'appelle
  « Boden verbessern », aucun titre coupé au milieu d'un mot ; anglais, espagnol : aucun titre coupé. Très gros texte :
  les titres passent à la ligne sans sortir de la carte.
- **S10 Barre d'onglets** (Android) : « Communauté » (ou sa traduction) écrit en entier sous son icône, jamais
  « Communau… ».

## Non-régression (toutes les personas)
- **R1** : planning, fiche plante, Communauté en lecture, écran Plus aux prix lisibles. Aucun plantage, aucun écran blanc.
- **R2 Langue** (personas en/de/es) : relève tout mot français vu dans l'app (écran, mot exact, capture). Les points déjà
  connus de la 1.8.0 (« Possible jusqu'au … », mois en français dans le planning, prix à deux formats, deux paywalls
  enchaînés) sont à noter à nouveau s'ils sont toujours là, sans les compter comme nouveaux.
- **R3 Téléphone français, appli en anglais** (personas en fr-FR seulement ; les autres : « non testable ») : à la fin du
  test, Profil > Langue, passe l'app en anglais. Dans le planning, le mois en tête est en anglais (« November 2026 », pas
  « Novembre »), une tâche à date limite écrit « Possible until … » en anglais, les jours et les dates sont en anglais.
  Relève tout mot français. Puis reviens au français et vérifie que tout revient en français.
- **R4 Santé des plantes** (personas en/de/es) : si un ravageur apparaît (par exemple limaces, « Slugs »), il n'est pas
  rangé parmi les maladies (note l'étiquette affichée).
- **C8 Rien qui fasse IA** : étincelle, baguette magique, robot, emoji (hors les 8 réactions rapides), dégradé décoratif,
  textes « Discover », « personalized », « smart », « AI assistant » et équivalents. Exception voulue : la mention
  « réponse générée par IA » sous HortenIA. Les nouveaux avatars de couleur ne doivent pas faire « généré ».

Toujours rien de publié pour de vrai dans la Communauté (réaction permise sur le seul post du banc, retirée à la fin), aucun code ni lien de parrainage envoyé, au plus 1 diagnostic et
1 question à HortenIA.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. **Tableau des vérifications** (N1 à N6, S1 à S4, S8 à S10, R1 à R4, C8), dans l'ordre :
   `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`.
   Bloquant = plantage, écran blanc, impossible d'avancer, perte du jardin ou du compte, jardin déformé après le tracé,
   mauvais prix, achat possible par erreur.
3. **Mots français ou mal traduits** (personas en/de/es) : `| écran | texte affiché | ce qu'un natif écrirait | capture |`,
   ou « Rien vu ».
4. Autres bugs vus en chemin, du plus grave au moins grave (format de CONSIGNES).
5. Impressions de la persona, à la première personne (format de CONSIGNES).
Distingue ce que tu as vu de ce que tu supposes.
