# Mission 1.8.1 : barre Android, code, notifications, avatars, Mes graines, tracé du jardin

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad), avec les changements ci-dessous. Ta persona (appareil, jardin, langue, type de compte) est dans
`personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona (champ « langue » ; fr-FR
si absent) : tape les textes à toucher dans la langue de l'écran. Compte environ 60 gestes, jusqu'à 60 minutes. Ne rends
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

## Non-régression (toutes les personas)
- **R1** : planning, fiche plante, Communauté en lecture, écran Plus aux prix lisibles. Aucun plantage, aucun écran blanc.
- **R2 Langue** (personas en/de/es) : relève tout mot français vu dans l'app (écran, mot exact, capture). Les points déjà
  connus de la 1.8.0 (« Possible jusqu'au … », mois en français dans le planning, prix à deux formats, deux paywalls
  enchaînés) sont à noter à nouveau s'ils sont toujours là, sans les compter comme nouveaux.
- **C8 Rien qui fasse IA** : étincelle, baguette magique, robot, emoji (hors les 8 réactions rapides), dégradé décoratif,
  textes « Discover », « personalized », « smart », « AI assistant » et équivalents. Exception voulue : la mention
  « réponse générée par IA » sous HortenIA. Les nouveaux avatars de couleur ne doivent pas faire « généré ».

Toujours rien de publié pour de vrai dans la Communauté, aucun code ni lien de parrainage envoyé, au plus 1 diagnostic et
1 question à HortenIA.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. **Tableau des vérifications** (N1 à N6, R1, R2, C8), dans l'ordre :
   `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`.
   Bloquant = plantage, écran blanc, impossible d'avancer, perte du jardin ou du compte, jardin déformé après le tracé,
   mauvais prix, achat possible par erreur.
3. **Mots français ou mal traduits** (personas en/de/es) : `| écran | texte affiché | ce qu'un natif écrirait | capture |`,
   ou « Rien vu ».
4. Autres bugs vus en chemin, du plus grave au moins grave (format de CONSIGNES).
5. Impressions de la persona, à la première personne (format de CONSIGNES).
Distingue ce que tu as vu de ce que tu supposes.
