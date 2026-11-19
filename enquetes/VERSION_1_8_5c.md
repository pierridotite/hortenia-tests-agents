# Contrôle court 1.8.5 (build 119/156) : photos de la messagerie et retour depuis la page d'un membre

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Ta persona est dans `personas.json` (variable PERSONAS). Environ 50 gestes, 40 minutes au plus.
Aucun achat. Aucune question à HortenIA. **Ne publie JAMAIS rien dans la Communauté** (aucun post, commentaire ni réaction).
Messagerie : groupes TOUJOURS « sur invitation », fermés à la fin ; jamais « Signaler ».

## Démarrage
1. Lance l'app. Tout de suite : `python3 outils/site_tests.py compte plus` (Plus) ou `python3 outils/site_tests.py compte email`
   (gratuit), UNE SEULE FOIS ; mot de passe tapé par `ecrire.py @mdp-compte`, jamais affiché.
2. Connecte-toi directement (Profil > « J'ai déjà un compte » > e-mail), sans refaire tout l'accueil si l'appli le permet.

## Codes
- P1 Photos (iPhone) : crée un groupe sur invitation, puis envoie 3 photos d'un coup (dont la photo rose de la galerie), attends
  la fin de l'indicateur, puis envoie 2 autres photos. Attendu : les envois qui se suivent peuvent se regrouper en UN bloc
  (voulu, façon Instagram), mais le compte final est juste : 5 photos, aucune ne disparaît (lis « N photos » et ouvre la
  visionneuse jusqu'à la dernière). Si une photo ne part pas, un message d'erreur le dit (pas de disparition silencieuse).
  Quitte la discussion, reviens : toujours 5. Ferme le groupe à la fin.
- P2 Retour depuis un post ouvert sur la page d'un membre : Communauté > discussion d'un post > page d'un membre > un post
  de sa page. Retour (flèche, puis à refaire avec le glissé du bord sur iPhone ou le retour Android) : la page du membre,
  à la même place ; un retour de plus : la discussion ; encore un : le fil. Fais-le 3 fois.
Note pour chaque écart : écran de départ, geste, écran atteint, l'heure.

## Ta ligne
| Persona | Compte | À faire |
|---|---|---|
| hanna | Plus | iPhone SE, allemand : P1 ; P2 (glissé) |
| oliver | gratuit | P1 ; P2 (flèche) |
| kevin | Plus | P2 (glissé, 3 fois) |
| lukas | gratuit | Android, allemand : P2 (flèche et retour Android) |
| yves | gratuit | Android 10, texte x1,3 : P2 (retour Android) |

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : plantage ou écran bloqué ; nombre de photos envoyées et vues ; ce que tu as créé et fermé.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | ce que tu as vu |`.
3. Autres bugs vus.
