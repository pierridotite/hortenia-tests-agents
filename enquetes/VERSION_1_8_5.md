# Mission 1.8.5 (build 117/154) : Profil, photos des posts, badge Plus, messagerie, correctifs Météo et calculatrices

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona.
Environ 90 gestes, jusqu'à 75 minutes. Une vérification bloquée ne t'arrête pas : note-la et passe.
Aucun achat, même d'essai : la fenêtre du store s'ouvre, tu la fermes. Aucune question à HortenIA,
aucun diagnostic photo, aucun code de parrainage.
Ne publie JAMAIS rien dans la Communauté : aucun post, aucun commentaire, aucune réaction (règle de Pierre, 19/11).
Jamais de réaction, de commentaire ni de message à un autre compte que le tien ou celui que ta ligne nomme.

## Démarrage
1. Lance l'app et attends l'écran d'accueil. Tout de suite, avant toute capture, prends le compte de test de ta ligne :
   `python3 outils/site_tests.py compte plus` (compte Plus) ou `python3 outils/site_tests.py compte email`
   (e-mail affiché ; mot de passe tapé par `ecrire.py @mdp-compte`, jamais affiché). Si l'outil répond « identifiant
   d'appareil introuvable », relance l'app et recommence aussitôt.
2. Fais l'accueil au plus court, en plaçant le jardin sur la carte (lieu de ta ligne) et en gardant les plantes
   proposées, jusqu'au jardin. Android : pendant l'accueil, fais les points AC de ta ligne. Ferme le paywall sans rien acheter.
3. Connecte-toi avec le compte de test (Profil > « J'ai déjà un compte » ou « Sauvegarder mon jardin » > e-mail).
   Depuis la 1.8.5, l'onglet Profil est la page de profil ; les réglages sont derrière la roue « Paramètres ».

## Codes
**PR, onglet Profil et page de profil (#74, #78)**
- PR1 Onglet Profil : couverture jusqu'en haut (rien sous l'encoche ni l'îlot), nom entier, roue « Paramètres » sur la ligne du nom.
- PR2 Roue > Paramètres > retour (flèche ; glissé du bord sur iPhone ; bouton retour sur Android) : on revient au profil.
- PR3 « Modifier mon profil » : titre de fenêtre entier (« Profil bearbeiten » en allemand), « Jardine depuis » sous la bio
  si une année est mise, quatre chiffres lisibles (deux par deux en texte agrandi), pluriels justes (« 0 Beiträge »).
- PR4 Carte du jardin sur le profil : phrase entière, bascule Plan / 3D visible.
- PR5 Retoucher l'onglet Profil remonte la page. Toucher la photo d'un membre dans la Communauté ouvre son profil ;
  un post ouvert depuis un profil, puis trois retours : on revient dans l'ordre.
**PH, photos des posts (#80)** : dans la fenêtre d'un nouveau post, sans JAMAIS publier : ferme-la avec « Annuler » à la fin.
- PH1 Le sélecteur s'arrête à la place qui reste (4 au plus ; bouton grisé à 4).
- PH2 Bloc de photos sous le texte, croix « Retirer la photo N » de 44 points, photos visibles au-dessus du clavier.
- PH3 Dans le fil, sur un post existant à photos, toucher une tuile ouvre la bonne photo en grand (« Photo N sur T »).
- PH4 Annuler la fenêtre du nouveau post : rien n'est publié.
**BP, badge Plus et couverture (#81)**
- BP1 Compte Plus : pastille « Plus » après le nom sur le profil et sur ton post (VoiceOver / TalkBack : « Membre Hortenia Plus »).
- BP2 « Modifier mon profil » : interrupteur « Montrer mon badge Plus » ; éteint, la pastille disparaît ; rallume-le.
  Compte gratuit : ni pastille ni interrupteur.
- BP3 Profil sans couverture : coin de jardin dessiné, net, rien dessous la barre d'état ni sous « Ajouter une couverture ».
- BP4 Noms longs, texte agrandi : le nom ne perd jamais une lettre.
**MS, messagerie et groupes (#77, #79)** : le serveur isole le banc ; la recherche et « Découvrir » ne te montrent que
des comptes et des groupes de test. Tu peux écrire, créer un groupe et y ajouter ces comptes. Supprime tes messages et
ferme tes groupes avant la fin. Jamais de code d'invitation de jardin.
- MS1 Communauté : icône de la messagerie en haut à droite de « Quoi de neuf » ; liste des discussions (état vide propre).
- MS2 Cherche un membre (un compte de test), ouvre la conversation, écris un long texte : la barre d'écriture reste
  au-dessus du clavier, rien de caché. Ton premier message part dans ses « Demandes » (un seul avant acceptation).
- MS3 Photos : choix de 2 ou 3 photos d'un coup dans la galerie, envoi en un bloc ; toucher une photo ouvre la visionneuse.
- MS4 Double toucher sur un message : cœur ; le défilement et le toucher simple d'une photo marchent toujours.
- MS5 Groupe : créer (nom, description, photo du groupe), ajouter un compte de test, nommer animateur, quitter ou fermer.
  « Découvrir » et recherche par nom.
- MS6 Supprimer un de tes messages ; menu de signalement (ouvre-le, n'envoie pas) ; textes entiers en allemand et en texte agrandi.
- MS7 Page d'un membre (compte de test) : « Envoyer un message » avec la pastille et la couverture.
Non testable ici (Pierre sur TestFlight) : les notifications de messagerie, l'arrivée des nouveaux messages d'un autre compte.
**MC, Météo et calculatrices (#84, #85)**
- MC1 Android : clavier sur « pH mesuré », sur le champ de « Autre » et sur le besoin en azote : le champ reste visible.
- MC2 Android : depuis un calcul, « Voir le planning », puis retour : un appui ferme le planning et revient au calcul ;
  même chose depuis le paywall d'un résultat.
- MC3 Notifications refusées (refuse la demande, ou Réglages du téléphone) : la Météo affiche la ligne orange ; elle ouvre
  les réglages ; autorise, reviens : la ligne a disparu.
- MC4 Mode avion sur la Météo : « Pas de connexion : prévision de … » (ou sa traduction), puis réseau rétabli.
- MC5 Liste des calculs défilée vers le bas, ouvrir un calcul court, revenir : la liste est à la même place ;
  un calcul ouvert depuis une liste défilée commence en haut.
- MC6 Texte agrandi : bandeau de surface entier (« Fermer » / « Schließen »), titre « Amendement organique » loin du bouton retour.
- MC7 Jardin créé à Londres : nom « London » / « Londres », pas « City of Westminster ».
**AC, retour d'Android dans l'accueil (#86)**
- AC1 Accueil neuf jusqu'à « Votre saison », puis retour plusieurs fois : 4/4, 3/4, 2/4, une étape visible par appui.
- AC2 Depuis « Votre saison », « J'ai déjà un compte », puis retour : on revient à « Votre saison » au premier appui.
  Ensuite, termine l'accueil normalement.
**V, vue 3D (#82)** : comme `enquetes/VERIF_3D_1_8_5.md`, P2 (glissé mesuré) et P3 (« Recentrer ») seulement.

## Ta ligne
| Persona | Compte | Lieu | À faire |
|---|---|---|---|
| sophie | Plus | Nantes | AC1, AC2 ; MC1 à MC5 ; PR1, PR2 ; BP1, BP2 |
| lukas | gratuit | Berlin | allemand : PR1 à PR5 ; MS1 à MS7 ; BP2 (sans interrupteur), BP3 ; MC6 |
| yves | gratuit | Lyon | petit écran, texte x1,3 : AC1, AC2 ; PR1 à PR4 ; MC1, MC5, MC6 ; MS1, MS2 |
| lucia | Plus | Madrid | espagnol : PH1 à PH4 ; BP1 à BP4 ; MC3, MC4 |
| baptiste | Plus | Annecy | V (P2, P3) ; MC2, MC5 ; PR2 (bouton retour) ; AC1 |
| raymond | gratuit | Le Mans | iPhone SE, très gros texte : PR1 à PR5 ; BP3, BP4 ; MS1, MS6 ; MC6 |
| hanna | Plus | Köln | iPhone SE, allemand, très gros texte : PH1 à PH4 ; BP1, BP2, BP4 ; MS1 à MS7 |
| kevin | Plus | Toulouse | V (P2, P3) ; PR2, PR5 ; PH1 à PH4 ; MC3, MC4 |
| oliver | gratuit | London | anglais : MC7 (le jardin se crée à Londres) ; PR1, PR3 ; MS1 à MS7 |

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : un plantage ou un écran bloqué vu ou non, le plus gênant, ce que tu as écrit dans la messagerie et supprimé.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable / sans objet) | capture(s) | ce que tu as vu |`
   pour chaque code de ta ligne (avec la mesure pour P2).
3. Autres bugs vus, du plus grave au moins grave.
