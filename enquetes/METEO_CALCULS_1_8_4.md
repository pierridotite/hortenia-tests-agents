# 1.8.4 : ce qu'il faut essayer sur la page Météo et le détail des calculatrices

Pôle Produit, 18/11/2026. Ces deux écrans sont neufs (PR #72). Ils n'ont été vus
que dans un navigateur, à la taille d'un téléphone : rien de ce qui suit n'a été
jugé sur un simulateur ni sur un vrai téléphone. La liste part de ce que le banc
web ne montre pas (clavier, texte réduit ou agrandi, gestes, moteur du téléphone).

Comptes : un compte Plus et un compte gratuit. Jardin : un jardin placé sur la
carte, avec des plantes et, si possible, plusieurs parties tracées.

## Deux signaux qui bloquent la sortie

1. Un écran crème et figé à l'ouverture de Météo ou d'un calcul.
2. L'écran « Calcul indisponible », ou « Météo indisponible » alors que le réseau
   marche. Ce sont les filets : un bloc n'a pas su se dessiner. Noter l'écran,
   le calcul ouvert, la langue et le compte. La capture de ces deux écrans est
   à côté : `ecrans-de-repli.png`.

Un bloc qui manque sans message (la semaine, les repères, la carte de la réponse)
est le même signal, en plus discret : comparer avec la liste des blocs ci-dessous.

## Page Météo (accueil du jardin, puis Météo)

Blocs attendus, dans l'ordre : la date, le verdict du jour en grand, la ligne du
moment, la carte de l'alerte s'il y en a une (courbe de la nuit, plantes à
protéger, le geste, « Ajouter au planning »), « Au jardin cette semaine », « La
semaine, jour par jour », « Les repères du jardinier », les alertes, le crédit.

1. La page s'ouvre et le verdict se lit en entier, sur un petit iPhone aussi.
2. Les courbes (nuit froide, jour choisi) se dessinent ; les heures sous l'axe
   tombent sous leurs traits et ne débordent pas de la carte.
3. Toucher chaque jour de la semaine : la courbe et la phrase du jour changent.
4. « Ajouter au planning » : le bouton passe à « Ajouté », « Voir dans le
   planning » ouvre le planning au bon jour, le retour revient sur la Météo.
5. Compte gratuit : l'aperçu de l'alerte ouvre le paywall ; le fermer ramène sur
   la page, intacte.
6. Compte Plus : les interrupteurs des alertes répondent ; notifications
   refusées, la ligne orange le dit.
7. Les jours et les heures sont justes : la date du jour en tête, les heures au
   format du téléphone (12 ou 24 heures). En anglais, « 7 AM » ou « 07:00 ».
8. Mode avion : « Pas de connexion » et « Réessayer », qui recharge au retour du
   réseau.
9. Texte agrandi dans les réglages du téléphone : rien ne se chevauche.
10. Anglais, allemand, espagnol : aucun texte coupé, aucun mot resté en français.

## Détail des calculatrices (Calculer, puis chacun des quatre calculs)

La page Calculer et ses cartes photo n'ont pas changé. Le détail, si.

1. Amendement, Correction de pH, Engrais, Besoin en eau : chaque détail s'ouvre.
   Compte Plus : la réponse est en haut et change à chaque choix. Compte gratuit :
   l'en-tête, les choix, le bouton, puis la carte « Votre résultat est prêt » qui
   mène au paywall ; le fermer ramène sur le calcul.
2. Clavier, sur iPhone et sur Android : « pH mesuré », le champ de « Autre », la
   surface (« Modifier » dans le bandeau), le besoin en azote (Engrais, « Je
   connais le besoin »). Le champ reste-t-il visible au-dessus du clavier ? La
   réponse suit-elle la saisie ? Le clavier se ferme-t-il en touchant ailleurs ?
3. Échelle du pH : les deux libellés (« pH mesuré 5,5 » au-dessus, « pH visé 6,5 »
   en dessous) se lisent à taille normale, jamais en tout petit, et leur pointe
   tombe sur la bonne bande. À revoir en allemand (« Gemessener pH 5,5 ») et avec
   le texte agrandi.
4. Les puces (parties du jardin, cultures, produits) : toucher change la réponse ;
   les longues étiquettes passent à la ligne sans sortir de l'écran.
5. « Ajouter au planning » : « Ajouté », puis « Voir dans le planning » au bon
   jour ; le retour revient sur le calcul.
6. Besoin en eau : la réponse parle de la semaine (pluie et évaporation) ;
   l'interrupteur « Sous abri » change le compte ; en mode avion, les puces du
   temps qu'il fait apparaissent.
7. « Modifier » : la surface et le sol. Choisir un autre sol change la réponse.
8. Retour : la flèche ramène du détail à la liste ; le bouton retour d'Android
   aussi.
9. Petit iPhone et texte agrandi : la carte de la réponse reste lisible, le
   bouton ne sort pas de la carte.
10. Anglais, allemand, espagnol : unités et nombres au format de la langue, aucun
    mot resté en français.

## À savoir

- Les heures de la page Météo s'écrivent à l'horloge du téléphone tant que le
  serveur n'est pas mis à jour : c'est voulu, comme en 1.8.3.
- Les plantes « À protéger » n'apparaissent qu'avec le serveur à venir : leur
  absence aujourd'hui n'est pas un défaut.
- Trois calculs donnent d'autres chiffres qu'en 1.8.3, c'est voulu : l'arrosage
  compte la pluie et la semaine, la cendre de bois passe à 100 g par m², la
  chaux et le soufre suivent le sol avec un plafond par an.
