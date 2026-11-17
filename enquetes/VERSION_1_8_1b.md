# Mission 1.8.1 (build 111/148) : vérification courte des corrections

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad). Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta
persona : tape les textes à toucher dans la langue de l'écran. Compte environ 50 gestes, jusqu'à 45 minutes. Donne un
verdict à chaque ligne avant de rendre le rapport. Une vérification bloquée ne t'arrête pas : note-la et passe.

## Démarrage
- Lance l'app, fais l'onboarding comme ta persona (en traçant la zone du jardin quand l'écran le propose), jusqu'au
  planning. Personas « email » : compte par e-mail après l'onboarding (règles de CONSIGNES). Personas « invite » : pas de
  compte. Ne paie rien, ne fais ni `pm clear` ni réinstallation.

## Corrections à vérifier
- **T1 Tracé à la création** : à l'étape du tracé, la carte s'ouvre assez près pour dessiner un jardin (une maison, une
  rue, pas toute la ville). Pose 4 coins autour d'un jardin plausible : la surface affichée reste de l'ordre de dizaines
  ou centaines de m², pas de milliers. Les longueurs des côtés sont lisibles, jamais cachées sous un coin ou un trait.
- **T2 Tracé abandonné** : rouvre le tracé (Aménager > Tracer ou Retracer sur la carte), pose ou bouge des coins pour une
  surface très différente, puis quitte par la flèche retour ou Fermer, SANS valider. Le jardin garde sa surface d'avant
  (vérifie dans Aménager ou Calculer). Recommence en touchant « Valider la zone » puis Fermer > « Quitter sans
  enregistrer » : la surface d'avant revient aussi. Note les surfaces avant et après, avec captures.
- **T3 Croisement** : dans « Retracer sur la carte » (ou à la création), tire un coin par-dessus le côté opposé pour que
  deux côtés se croisent vraiment : le geste est refusé avec une raison claire dans ta langue, et le contour revient à
  l'état d'avant. Une forme creuse (un coin rentré vers l'intérieur sans croiser de côté) est permise : ce n'est pas un
  défaut. Si tu fais l'essai dans Aménager > Taille et forme, un message qui nomme une allée ou une planche qui sort du
  plan n'est pas un défaut non plus.
- **T4 Pastille des réactions** : sur le post « Banc 1.8.1 : post de test pour les réactions. » (le seul où tu peux
  réagir ; ne pose jamais de réaction ailleurs, un vrai jardinier serait prévenu), appui long sur le cœur : la pastille
  ne cache plus le texte du post. Post tout en haut de l'écran : elle s'ouvre en dessous du bouton s'il n'y a pas la
  place au-dessus. Choisis une réaction, puis retire-la. Sur un autre post, appui long seulement, puis touche à côté pour
  fermer sans rien choisir : la pastille ne cache pas le texte non plus. Captures.
- **T5 Langue** (personas en/de/es ; personas fr : passe l'app en anglais par Profil > Langue à la fin, puis reviens au
  français) : relève tout mot français dans le planning (titres des tâches), Mes graines (ajoute un sachet « Lettuce » ou
  sa traduction : le sachet garde ce nom, le bouton est traduit, puis supprime-le), la fin d'onboarding, le paywall
  ouvert depuis le Profil, l'écran Calculer (« Loamy soil » et ses équivalents), le profil public d'un jardinier (« Diana's
  garden » ou sa traduction), et « Possible until … ». Déjà connus pour la version suivante, à noter sans les compter : noms
  de plantes en français dans les réponses d'HortenIA, titre du rappel de semis d'un sachet (« Semer la laitue… »). Un
  sachet tapé sans fiche garde le nom tapé (voulu).
- **R1 Non-régression** : réactions (toucher, appui long, retrait), écran Calculer, Mes graines, planning : aucun
  plantage, aucun écran blanc.

Toujours rien de publié dans la Communauté, réaction seulement sur le post du banc et retirée à la fin, aucun code ni
lien de parrainage envoyé, aucune question à HortenIA, pas de diagnostic.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`
   pour T1 à T5 et R1. Bloquant = plantage, écran blanc, jardin déformé ou perdu, impossible d'avancer.
3. Mots français ou mal traduits : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. Autres bugs vus, du plus grave au moins grave.
Distingue ce que tu as vu de ce que tu supposes.
