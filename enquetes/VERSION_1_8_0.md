# Mission 1.8.0 : Hortenia en anglais, allemand et espagnol (et les corrections de la 1.7.3)

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad), avec les changements ci-dessous. Ta persona (appareil, jardin, langue, type de compte) est dans
`personas.json` (cherche ton identifiant, variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona
(champ « langue » ; fr-FR si absent). Compte environ 70 gestes, jusqu'à 70 minutes. Ne rends pas le rapport avant
d'avoir donné un verdict à chaque ligne. Une vérification bloquée ne t'arrête pas : note-la et passe à la suivante.

Les outils qui touchent un texte (toucher_texte.py) cherchent le texte tel qu'il est affiché : tape-le dans la langue
de l'écran, pas en français.

## Démarrage
- Lance l'app et attends l'écran d'accueil. Fais l'onboarding comme ta persona, jusqu'au planning.
- Personas « invite » : ne crée jamais de compte. Personas « email » : compte par e-mail après l'onboarding (règles de
  CONSIGNES). Ne paie jamais rien. N'écris jamais un mot de passe ou un jeton en clair dans le rapport.
- Ne fais jamais `pm clear`, de réinstallation ni d'effacement des données de l'app.

## Personas en anglais, allemand ou espagnol (langue différente de fr-FR) : vérifications L1 à L9
Tu ne lis pas le français : tout mot français vu dans l'app est un défaut (note l'écran, le mot exact, la capture).
- **L1 Langue au démarrage** : dès le premier écran, l'app est dans la langue du téléphone. Aucun mot français, aucune
  clé technique (`onboarding.title`, `{{name}}`, `undefined`), aucun texte vide.
- **L2 Onboarding et inscription** : chaque étape (questions, carte et tracé du jardin, adresse, autorisations) est
  traduite, naturelle (pas mot à mot du français), sans faute. Inscription par e-mail (ou invité) : messages d'erreur
  traduits aussi (essaie une adresse invalide une fois).
- **L3 Création du jardin** : le jardin se crée à ta position (ton pays), les unités et les dates sont dans le format
  local (date, jour de la semaine, m²).
- **L4 Planning** : les tâches de la semaine sont traduites et cohérentes avec ton climat et la saison (novembre, ton pays).
- **L5 Fiche plante** : ouvre une fiche de plante que tu as ajoutée ; nom, description, conseils traduits, sans phrase
  française restée.
- **L6 Notification** : si une notification arrive (ou dans la liste des notifications de l'app), elle est dans ta langue.
  Si aucune n'arrive pendant le test, note « aucune notification reçue » sans attendre plus de 2 minutes.
- **L7 Paywall Plus** : ouvre l'offre Plus. Textes traduits, prix lisibles dans une devise cohérente (sur le simulateur
  iPhone, des dollars ne sont pas un bug), rien de coupé. Ne paie pas.
- **L8 Profil > Langue** : ouvre le réglage de langue, passe l'app en français, vérifie que l'accueil et le planning
  passent en français, puis reviens à ta langue : tout revient, sans redémarrage forcé ni écran blanc.
- **L9 Textes trop longs** : sur chaque écran, relève tout texte coupé, débordant, sur trois lignes dans un bouton, ou
  un mot allemand long qui casse la mise en page.

## Champ « J'ai un code » (toutes les personas, une fois)
- **K1** : trouve le champ « J'ai un code » (ou sa traduction) pour un code Plus. Tape `TEST0000`, valide une seule fois :
  un message clair dit que le code n'est pas valable, rien ne plante. N'essaie aucun autre code.

## Personas en français (odile, gilles) : corrections de la 1.7.3 et non-régression
- **F1 Grand jardin** : dans Aménager, retrace un jardin au-delà de 5 000 m². L'écran du tracé demande d'abord
  (garder sans plan, ou retracer). Si tu gardes : Aménager montre la surface et un bouton Retracer, plus d'écran presque
  vide ; « 5 000 m² » tient sur une ligne ; on quitte sans question d'enregistrement. Reviens ensuite à un jardin normal.
- **F2 Retracer** : Retracer repart du contour en cours, pas de l'ancien.
- **F3 Taille et forme** : agrandis deux fois le contour par les coins ; à chaque glissement relâché, le contour reste
  entier et visible au-dessus de la feuille.
- **F4 Parrainage** : « Inviter un ami » en gros texte : le code et le lien passent à la ligne, rien de rogné. N'envoie rien.
- **F5 Langue** : Profil > Langue existe ; passe en anglais puis reviens au français ; tout revient en français.
- **F6 Non-régression** : planning, fiche plante, un diagnostic photo (galerie, un seul), la Communauté se lit (rien
  publié), l'écran Plus montre des prix lisibles. Aucune trace d'anglais ou d'allemand dans l'app en français.

## Pour tous
- **C8 Rien qui fasse IA** : relève étincelle, baguette magique, robot, emoji dans l'app (hors les 8 réactions rapides),
  dégradé décoratif, textes « Discover », « personalized », « smart », « AI assistant » (et équivalents allemands et
  espagnols), image visiblement générée. Exception voulue : la mention « réponse générée par IA » sous HortenIA.

Toujours rien de publié pour de vrai dans la Communauté, aucun code ni lien de parrainage envoyé, au plus 1 diagnostic et
1 question à HortenIA.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes, dont : la langue de l'app est-elle crédible pour un natif ?
2. **Tableau des vérifications** (L1 à L9 et K1, ou F1 à F6 et K1, puis C8), dans l'ordre :
   `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`.
   Bloquant = plantage, écran blanc, impossible d'avancer, app en français pour un téléphone étranger, perte du jardin
   ou du compte, mauvais prix, achat possible par erreur.
3. **Mots français ou mal traduits** : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. **Ce qui fait IA** : `| écran | élément | capture |`, ou « Rien vu » avec les écrans parcourus.
5. Autres bugs vus en chemin, du plus grave au moins grave (format de CONSIGNES).
6. Impressions de la persona, à la première personne (format de CONSIGNES).
Distingue ce que tu as vu de ce que tu supposes.
