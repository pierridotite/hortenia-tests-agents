# Retours depuis la Communauté : ce qui est attendu (1.8.5, builds iOS 118 et Android 155)

Pour les testeurs, d'après le code de main après la PR #87 (19/11/2026).

Règle de Pierre (19/11) : rien ne se publie dans la Communauté pendant un test. Pas de post, de commentaire ni de réaction, même depuis un compte de test. Ces parcours ne font que naviguer : on ouvre un écran, on revient. On n'écrit aucun message, on ne crée aucun groupe, on n'envoie aucune invitation.

Trois façons de revenir, à essayer à chaque ligne :

- **Flèche** : la flèche en haut à gauche de l'écran.
- **Glisser (iPhone)** : glisser depuis le bord gauche de l'écran. Il n'existe pas sur Android.
- **Retour Android** : le bouton ou le geste de retour du téléphone.

Sauf mention contraire, les trois mènent au même écran.

## 1. Depuis le fil de la Communauté

| On ouvre | Comment | Retour attendu |
|---|---|---|
| Règles de la communauté | lien sous « Quoi de neuf au jardin ? » | le fil, au même endroit. L'onglet Communauté reste allumé (avant la 1.8.5, on arrivait dans Profil) |
| Discussion d'un post | toucher un post ou sa bulle de commentaires | le fil. La barre d'onglets est cachée dans la discussion et revient avec le fil |
| Page d'un membre | toucher son nom ou sa photo | l'écran d'où l'on vient : le fil ou la discussion |
| Un post sur la page d'un membre | toucher le post | la page du membre, puis le fil |
| Un autre membre dans cette discussion | toucher son nom | sa page, puis la discussion, puis la page du premier membre, puis le fil : chaque écran une fois, sans boucle |
| Sa propre photo ou son propre nom | toucher | l'onglet Profil s'ouvre, à sa page de profil (voulu : rien ne s'empile dans la Communauté). Il n'y a pas de flèche. Retour Android : l'onglet Jardin, comme depuis tout onglet. Toucher Communauté rouvre le fil là où on l'avait laissé |
| Un article cité dans un post | toucher la carte de l'article | le fil ou la discussion |
| Messages | l'avion en papier en haut à droite | le fil |

## 2. Dans Messages

| On ouvre | Comment | Retour attendu |
|---|---|---|
| Une discussion | toucher une ligne | Messages. Barre d'onglets cachée dans la discussion |
| Page d'un membre, depuis une discussion à deux | toucher le haut de la discussion ou « Voir le profil » | la discussion |
| Fiche d'un groupe, depuis sa discussion | toucher le haut ou « Infos du groupe » | la discussion. Le bas de la fiche est entier, sans barre d'onglets |
| Membres d'un jardin partagé, depuis sa discussion | toucher le haut ou « Infos du groupe » | une feuille s'ouvre. « Fermer », toucher au-dessus ou Retour Android la ferment et laissent la discussion. Le glissement n'agit pas sur une feuille |
| Page d'un membre, depuis cette feuille | toucher un membre (pas soi) | la feuille se ferme, la page s'ouvre. Retour : la discussion |
| Demandes de message | ligne en tête de Messages | Messages |
| Une demande | toucher une ligne | la liste des demandes, puis Messages |
| Groupes | onglet « Groupes » de Messages | rester dans Messages (c'est un onglet de l'écran, pas un écran de plus) |
| Fiche d'un groupe, depuis Groupes | toucher un groupe | Messages, sur Groupes |
| Créer un groupe | bouton de Groupes | Messages, sur Groupes. **Revenir sans créer.** Sur Android, à refaire dans les quatre langues : un testeur a vu un retour raté depuis « Neue Gruppe », non reproduit (aucun écouteur sur ce chemin). Si cela se reproduit, noter la langue, l'écran atteint et l'heure |
| Ajouter des membres, depuis la fiche d'un groupe que l'on gère | ligne « Ajouter des membres » | la fiche. Revenir sans ajouter personne |
| Nouveau message | crayon en haut à droite de Messages | Messages. Revenir sans choisir personne |

## 3. Changer d'onglet

| Geste | Attendu |
|---|---|
| Un écran ouvert dans la Communauté (règles, discussion, page de membre, Messages...), toucher un autre onglet, puis Communauté | le même écran, tout de suite, sans rechargement visible |
| Paramètres ouverts dans Profil, toucher Communauté, puis Profil | Paramètres, tout de suite, sans saut ni rechargement (c'était le retour de Pierre du 19/11) |
| Toucher l'onglet déjà ouvert (Communauté, Profil ou Jardin) | le début de l'onglet : le fil, la page de profil, l'accueil du Jardin. Fiches ne change pas : l'écran ouvert reste |
| Toucher Diagnostic, le bouton du milieu | toujours la prise de photo, comme avant |
| Retour Android au début d'un onglet autre que Jardin | l'onglet Jardin |
| Retour Android au début de l'onglet Jardin | l'appli se ferme ou passe en arrière-plan, comme toute appli Android |

## Défaut connu, hors de la 1.8.5

- **Rappels de Planifier** : le lien vers les réglages des notifications ouvre l'onglet Profil depuis l'onglet Jardin. C'est un saut d'onglet voulu à l'époque, à revoir plus tard. Ce n'est pas un écran de la Communauté.

## À noter pour chaque écart

Le téléphone, la version d'iOS ou d'Android, la langue, l'écran de départ, le geste, l'écran atteint et l'heure.
