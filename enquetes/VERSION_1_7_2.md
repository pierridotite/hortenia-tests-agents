# Mission 1.7.2 : la carte, la boussole, le parrainage, les Mentions légales et Aménager

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad), avec les changements ci-dessous. Ta persona (appareil, jardin, type de compte) est dans `personas.json`
(cherche ton identifiant, variable PERSONAS). La 1.7.2 est une petite version : vérifie **chaque ligne** de la liste
ci-dessous, puis le tour rapide de non-régression. Compte environ 60 gestes, jusqu'à 60 minutes. Ne rends pas le rapport
avant d'avoir donné un verdict à chaque ligne. Une vérification bloquée ne t'arrête pas : note-la et passe à la suivante.

## Démarrage
- Lance l'app et attends l'écran d'accueil. Fais l'onboarding comme ta persona (adresse ou position de son jardin,
  contour du jardin sur la carte), jusqu'au planning.
- Personas « invite » : ne crée jamais de compte. Personas « email » : compte par e-mail après l'onboarding (règles de
  CONSIGNES). Personas « plus » : `python3 outils/site_tests.py compte plus` donne l'adresse ; écris le mot de passe avec
  `ecrire.py @mdp-compte`. Ne paie jamais rien. N'écris jamais un mot de passe ou un jeton en clair dans le rapport.
- Ne fais jamais `pm clear`, de réinstallation ni d'effacement des données de l'app.

## Liste des vérifications (1.7.2)
- **C1 Carte, logo Mapbox** : sur la fiche du jardin (« Mon potager ») et sur la carte de l'onboarding, le logo Mapbox
  et le petit (i) sont blancs, discrets, alignés entre eux et avec le bord de la fiche. Rien ne déborde, rien ne « fait tache ».
- **C2 Photo satellite** : en vue Satellite, l'image est un peu plus chaude, nette ; les allées, le sable, les toits clairs
  et les champs ne sont pas brûlés en blanc. Compare avec ton souvenir d'une photo satellite ordinaire. Capture.
- **C3 Boussole** : nord en haut, aucune boussole. Tourne la carte à deux doigts (en Plan ou en 3D) : une petite boussole
  ronde crème apparaît, aiguille terracotta ; la toucher remet le nord en haut et elle disparaît. Si le geste de rotation
  est impossible sur le banc, note « non testable sur le banc » et la raison.
- **C4 Mentions légales** : depuis le Profil (ou les réglages), ouvre l'écran Mentions légales. Il existe, il se lit en
  entier (défile jusqu'en bas), les crédits (Mapbox, OpenStreetMap, images) y sont, le retour marche.
- **C5 Parrainage** : ouvre « Inviter un ami ». Plus de visuel de coupon ; le code et le lien sont clairs ; le bouton de
  partage ouvre le partage du téléphone (ferme-le sans envoyer). Ouvre aussi l'endroit où l'on saisit un code d'invitation :
  écris un faux code dans le champ, regarde le message, puis efface sans valider si un vrai envoi est possible.
- **C6 Aménager, Taille et forme** : ouvre Aménager puis « Taille et forme ». Le contour du jardin se voit **en entier**,
  centré, sans être coupé ; les mesures (côtés, surface) sont cohérentes avec le jardin dessiné. Puis agrandis le contour
  (ou redessine un très grand jardin, plusieurs milliers de m²) et rouvre « Taille et forme » : **aucune fermeture de
  l'app** (sur Android, c'était le plantage corrigé dans cette version). Reviens ensuite à un jardin normal.
- **C7 Non-régression** : le planning s'affiche ; une fiche de plante s'ouvre ; un diagnostic photo (galerie, feuille de
  tomate, un seul) va au bout ; la Communauté se lit (rien publié, aucune réaction) ; l'écran Hortenia Plus montre des prix
  lisibles (sur le simulateur iPhone, des dollars ne sont pas un bug).
- **C8 Rien qui fasse IA** : sur chaque écran vu, relève ce qui fait IA : étincelle, baguette magique, robot, icône de banque
  d'images prise telle quelle pour ce qui est propre à Hortenia, emoji dans l'app, dégradé décoratif, textes « Découvrez »,
  « personnalisé », « intelligent », « Assistant IA », image visiblement générée. Exceptions voulues par Pierre : la mention
  « réponse générée par IA » sous HortenIA, les 8 réactions rapides en emojis, les icônes des outils et des onglets.

Toujours rien de publié pour de vrai dans la Communauté, aucun code ni lien de parrainage envoyé, au plus 1 diagnostic et
1 question à HortenIA.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. **Tableau des vérifications** C1 à C8, dans l'ordre :
   `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`.
   Bloquant = plantage, écran blanc, impossible d'avancer, perte du jardin ou du compte, mauvais prix, achat possible par erreur.
3. **Ce qui fait IA** : `| écran | élément | capture |`, ou « Rien vu » avec les écrans parcourus.
4. Autres bugs vus en chemin, du plus grave au moins grave (format de CONSIGNES).
5. **Meilleure capture** de chaque vérification « bon » : son numéro et une phrase.
6. Impressions de la persona, à la première personne (format de CONSIGNES).
Distingue ce que tu as vu de ce que tu supposes.
