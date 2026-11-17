# Mission 1.8.2 (build 113/150) : vérification courte des corrections

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad). Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta
persona : tape les textes à toucher dans la langue de l'écran. Compte environ 50 gestes, jusqu'à 45 minutes. Donne un
verdict à chaque ligne avant de rendre le rapport. Une vérification bloquée ne t'arrête pas : note-la et passe. Une
ligne qui ne concerne pas ton appareil : « sans objet », sans t'y attarder.

## Démarrage
- Lance l'app, fais l'onboarding comme ta persona (en traçant la zone du jardin quand l'écran le propose), jusqu'au
  planning. Personas « email » : compte par e-mail après l'onboarding (règles de CONSIGNES). Personas « invite » : pas de
  compte. Ne paie rien, ne fais ni `pm clear` ni réinstallation.

## Corrections à vérifier
- **C1 Lieu du jardin** (surtout petit iPhone en gros texte) : à « Où est votre jardin ? », « Je le ferai plus tard » vient
  après les deux cartes (Position précise, Position approximative) et ne recouvre aucun texte. Après avoir touché une
  carte, son titre devient « Recherche de votre position… » pendant l'attente (capture toutes les 5 s).
- **C2 Plantes de saison** : à l'étape « Qu'est-ce qu'on y cultive ? », cherche une plante dans le champ de recherche :
  le bouton « Ajouter ces 3 plantes de saison » (ou sa traduction) ne s'affiche PAS sous les résultats. Sans recherche
  et sans rien coché, il peut s'afficher : le nombre annoncé doit être celui que l'écran suivant confirme.
- **C3 Tracé** : « Angles droits » est sur la ligne de la surface, plus sur la carte ; la longueur du côté du haut et
  ses coins restent visibles.
- **C4 Décimales** (personas en) : « Size and shape », plan et calculatrices écrivent « 12.47 m », jamais « 12,47 m ».
- **C5 En-tête d'Aménager** : avec une 2e partie ajoutée (Taille et forme > Ajouter une partie), le nom du jardin reste
  lisible dans l'en-tête ; « en 2 parties » n'apparaît que s'il reste de la place. Supprime la partie ensuite.
- **C6 Plan à l'accueil** (iPhone surtout) : dans Aménager, ajoute une partie ou change la taille, enregistre, reviens
  à l'accueil : le plan est cadré entre les boutons du haut et la fiche du jardin, rien n'est coupé. Rends le jardin
  comme avant.
- **C7 Pots** (jardin en pots, jardinière ou balcon ; sinon sans objet) : quand tous les pots posés sont pris, toucher
  une plante de la palette dit « Vos pots sont pleins : ajoutez un pot ou une jardinière ». Pose une plante « En rangs »,
  puis « Annuler la pose », puis ferme Aménager : plus de « Quitter sans enregistrer ? ».
- **C8 Réactions** : sur le post du banc « Banc 1.8.2 : post de test pour les réactions. » (le seul où tu peux réagir),
  appui long sur le cœur : la pastille s'ouvre sous le bouton et ne cache pas le texte de CE post (le post suivant peut
  être recouvert, c'est voulu). Choisis une réaction, puis retire-la.
- **C9 Langue** : allemand, le nom du jardin sur la fiche de l'accueil et les titres du planning se coupent avec un
  trait d'union (« Gemüse-garten »), jamais au milieu d'un mot sans trait ; la tâche photo s'appelle « Gemüsegarten
  fotografieren », son bouton passe sous le titre sur écran étroit ; phrase de fin d'onboarding naturelle. Espagnol :
  jours de la semaine sans majuscule (« el domingo »). Relève tout texte coupé ou maladroit dans ta langue.
- **R1 Non-régression** : plusieurs parties, coins dans le désordre remis dans l'ordre, nom du jardin selon la langue,
  En rangs, Calculer, Mes graines, planning : aucun plantage, aucun écran blanc.

Toujours rien de publié dans la Communauté, réaction seulement sur le post du banc et retirée à la fin, aucun code ni
lien de parrainage envoyé, aucune question à HortenIA, pas de diagnostic.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable / sans objet) | appareil | capture(s) | ce que tu as vu |`
   pour C1 à C9 et R1. Bloquant = plantage, écran blanc, jardin déformé ou perdu, impossible d'avancer.
3. Mots français ou mal traduits : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. Autres bugs vus, du plus grave au moins grave.
Distingue ce que tu as vu de ce que tu supposes.
