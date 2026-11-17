# Mission 1.8.2 (build 112/149) : corrections de la 1.8.1 et nouveautés du plan

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad). Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta
persona : tape les textes à toucher dans la langue de l'écran. Compte environ 70 gestes, jusqu'à 60 minutes. Donne un
verdict à chaque ligne avant de rendre le rapport. Une vérification bloquée ne t'arrête pas : note-la et passe.

## Démarrage
- Lance l'app, fais l'onboarding comme ta persona (en traçant la zone du jardin quand l'écran le propose), jusqu'au
  planning. Personas « email » : compte par e-mail après l'onboarding (règles de CONSIGNES). Personas « invite » : pas de
  compte. Ne paie rien, ne fais ni `pm clear` ni réinstallation.
- Si ta persona a choisi « Le gel » à la première question : à l'écran « Votre jardin est prêt », relève la phrase sur le
  gel (V5).

## Vérifications reprises de la 1.8.1
- **T1 Tracé à la création** : carte à l'échelle d'une rue ; 4 coins autour d'un jardin plausible donnent des dizaines
  ou centaines de m² ; longueurs lisibles, jamais l'une sur l'autre (même sur une bande étroite).
- **T2 Tracé abandonné** : rouvre le tracé (Aménager > Tracer ou Retracer), change beaucoup la surface, quitte par la
  flèche retour SANS valider, puis par « Valider la zone » + Fermer > « Quitter sans enregistrer » : la surface d'avant
  revient les deux fois (note avant / après, captures).
- **T4 Pastille des réactions** : sur le post du banc (texte « Banc 1.8.2 : post de test pour les réactions. » ; le seul
  où tu peux réagir, ne réagis jamais ailleurs), appui long sur le cœur : la pastille ne cache pas le texte de CE post.
  Choisis une réaction, puis retire-la. Recouvrir le début du post suivant est voulu : ne le compte pas.
- **R1 Non-régression** : réactions, Calculer, Mes graines, planning : aucun plantage, aucun écran blanc.

## Nouveautés de la 1.8.2
- **V1 En rangs** (Aménager > plan) : pose 50 pieds d'un coup (par ex. 50 tomates dans une serre ou 50 pommiers en
  verger). Le rond blanc se tire pour agrandir ou réduire le bloc ; les places hors de la zone sont sautées (le nombre
  posé est dit). Puis supprime ou annule ce que tu as posé, pour rendre le jardin comme avant.
- **V2 Jardin en plusieurs parties** (Aménager > Taille et forme > « Ajouter une partie ») : ajoute une partie (verger
  ou serre), nomme-la, retrace-la, enregistre, ferme puis rouvre : elle est là avec son nom et sa forme. Supprime-la
  ensuite. Tout message « Taille non enregistrée » est un défaut (capture).
- **V3 Coins dans le désordre** (création ou Retracer) : touche 4 coins dans l'ordre d'un nœud papillon. Attendu : la
  pastille dit que les côtés se croisent ; à « Valider la zone », les coins sont remis dans l'ordre avec une phrase qui
  le dit, et il faut valider de nouveau ; la surface finale est plausible. Jamais « 0 m² » accepté.
- **V4 Nom du jardin et langue** : Profil > Langue, passe dans une autre langue (personas fr : English) : un jardin
  resté « Mon potager » prend le nom proposé dans cette langue (« My veg patch »…) ; un jardin dont tu as écrit le nom
  ne bouge pas (renomme d'abord un 2e jardin si tu en as un, sinon note « non testable »). Reviens à ta langue.
- **V5 Gel et jardin sans lieu** : la phrase de l'écran résultat ne promet AUCUNE alerte gel (« vous prévient » serait
  un défaut ; « vous montre les nuits de gel » est attendu). Personas sans position : l'écran dit que le planning
  dépend de la position et où placer le jardin.
- **V6 Paywall** : sur le paywall et sur la seconde offre (si elle s'affiche), la mention « … dans votre compte App Store »
  (ou Google Play, ou sa traduction) tient sur une ligne, le nom du store jamais coupé. Ne touche à aucun bouton d'achat.
- **V7 Petit iPhone** (SE, mini) : sur l'accueil, la boussole ne passe sur aucun bouton de la 3D ou du plan ; dans
  Aménager avec plusieurs parties, l'en-tête abrège le nom du jardin et garde la mesure lisible.
- **V8 Langue** (personas en/de/es ; personas fr : passe en English pour ces points, puis reviens) : ajoute un sachet
  dans Mes graines : le rappel de semis est écrit dans la langue de l'appli (titre et texte), puis supprime le sachet.
  Ne pose AUCUNE question à HortenIA (déjà vérifié côté serveur).
- **V9 Vrais gestes** : sur le plan d'Aménager, pincement à deux doigts pour rapprocher et éloigner (la page entière ne
  doit pas s'agrandir) ; sur Android, rogne un rang posé (le bloc se réduit sans se casser). Si ton outil ne sait pas
  faire le geste, note « non testable » avec la raison.

Toujours rien de publié dans la Communauté, réaction seulement sur le post du banc et retirée à la fin, aucun code ni
lien de parrainage envoyé, aucune question à HortenIA, pas de diagnostic.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`
   pour T1, T2, T4, R1 et V1 à V9. Bloquant = plantage, écran blanc, jardin déformé ou perdu, impossible d'avancer.
3. Mots français ou mal traduits : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. Autres bugs vus, du plus grave au moins grave.
Distingue ce que tu as vu de ce que tu supposes.
