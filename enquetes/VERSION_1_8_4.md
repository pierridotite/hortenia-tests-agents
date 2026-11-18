# Mission 1.8.4 (build 115/152) : « Votre saison » refaite, Communauté et profil, paywall sur iPhone

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad). Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta
persona : tape les textes à toucher dans la langue de l'écran. Compte environ 90 gestes, jusqu'à 80 minutes. Donne un
verdict à chaque ligne qui te concerne avant de rendre le rapport (« sans objet » pour les autres, sans t'y attarder).
Une vérification bloquée ne t'arrête pas : note-la et passe.

## Démarrage : imposer ta version du parcours AVANT de toucher « Créer mon jardin »
Le parcours se décide une seule fois, au toucher de « Créer mon jardin ». Touché trop tôt, l'installation reste en A
pour de bon : dans ce cas, dis-le dans le rapport et teste A.
1. Lance l'app et attends l'écran d'accueil (elle écrit son identifiant d'appareil dans le journal). Ne touche rien.
2. Impose ta version (colonne « Version » du tableau ci-dessous) : `python3 outils/site_tests.py imposer T43=B`
   (ou `T43=A`). Tape la commande seule. N'utilise PAS `site_tests.py preparer` (il imposerait d'anciens tests).
   La réponse doit contenir `T43` : sinon note « T43 absent du serveur » dans le rapport et continue (tu seras en A).
3. Relance l'app (Android : `adb shell am force-stop com.hortenia.app` puis la commande de lancement ; iOS :
   `bash outils/ios/geste.sh relancer`). Vérifie avec `python3 outils/site_tests.py evenements` que `banc_versions`
   montre `T43` à ta version. Puis seulement, touche « Créer mon jardin ».
4. Fais le parcours comme ta persona (tableau), en traçant la zone du jardin quand l'écran le propose. Ne paie rien :
   la fenêtre du store s'ouvre, tu la fermes sans acheter (sauf mention, ne touche même pas le bouton d'essai).
   Pas de compte par e-mail dans cette mission, sauf ligne F5 (proposition d'inscription : regarde, ne crée rien).


Le test T43 tourne pour de vrai depuis le 18/11 : sans version imposée, ton téléphone tirerait A ou B au sort. Le
démarrage ci-dessous reste donc obligatoire.

| Persona | Version | Réponse à la question | Particularité |
|---|---|---|---|
| sophie | B | Le gel | lieu : Draveil ; F6 passage (1) : quitter l'appli pendant le paywall ; mode sombre du téléphone (l'appli reste claire : voulu) |
| yves | B | Passer | refuse la localisation, aucun lieu (S6, note des dates sans lieu) ; jardin d'exemple (U6, U7) |
| tom | B | Les maladies et les ravageurs | lieu : Toulouse (S5, « À surveiller ») ; puis Communauté : CP1 à CP3 avec un compte de test |
| lucia | B | Savoir quand semer et planter (en espagnol) | lieu : Madrid (S12) ; grille de saison (C7) |
| lukas | B | Penser à tout au bon moment (en allemand) | lieu : Berlin ; mots longs (C6, S3 en allemand) ; puis profil : PR1 à PR3 avec un compte de test |
| emily | A | (parcours actuel, en anglais) | A inchangé (A1, A3) ; réactions R1 à R4 |
| oliver | B | Le gel (en anglais) | lieu : Londres ; va jusqu'à la fenêtre d'achat et la ferme sans acheter (D5, F1) ; U11 ; V1 avec le compte Plus de test (voir V1 plus bas) |
| raymond | B | Passer | lieu : Le Mans ; plus petit écran, très gros texte (S3, S8, U11, D6) |
| hanna | B | Le gel (en allemand) | ne coche aucune plante (C3, C5, S9) ; lieu : Köln ; puis Communauté : CP4 et réactions en texte agrandi (R2) |
| kevin | A | (parcours actuel) | A inchangé ; U11 et F6 dans A ; puis profil : PR1 à PR4 avec un compte de test |

## Parcours d'accueil : points à vérifier, un verdict par ligne

### La question (Q)

- Q1. Après « Créer mon jardin », la question arrive seule, avec le repère « 1/4 ».
- Q2. Quatre réponses et « Passer ». Une seule touche suffit : la réponse se coche et l'écran suivant arrive seul, sans bouton à chercher.
- Q3. « Retour » ramène à l'accueil. Revenir de l'écran du type ramène à la question, avec la réponse encore cochée.
- Q4. Le titre tient sur l'écran sans mot seul sur la dernière ligne, dans les quatre langues.

### Type, lieu, plantes (C)

- C1. Les trois écrans sont ceux d'avant, numérotés 2, 3 et 4 sur 4.
- C2. Le bouton des plantes dit « Voir ma saison ».
- C3. Sans rien cocher, l'écran propose jusqu'à trois plantes de saison. « Ajouter ces 3 plantes de saison » les ajoute. « Continuer sans plante » mène quand même à la préparation puis à « Votre saison ».
- C4. À l'étape du lieu, « Je le ferai plus tard » est en bas de l'écran quand tout tient, même s'il reste du vide sous les deux cartes de position : c'est voulu, ne pas le signaler. Quand tout ne tient pas (petit écran, très gros texte), il vient après les deux cartes et se lit en faisant défiler ; il ne couvre jamais une carte. La carte touchée dit « Recherche de votre position… » pendant l'attente (corrections de la PR #58).
- C5. Sans plante cochée, pendant une recherche de plante, « Ajouter ces 3 plantes de saison » ne se montre pas (PR #58) : le pied dit « Continuer sans plante » et « Voir ma saison », et les deux mènent à « Votre saison » avec les plantes de saison proposées. Recherche effacée, la proposition revient.
- C6. Le pied de l'étape des plantes (1.8.3). Le lien (« Passer » ou « Continuer sans plante ») et le bouton « Voir ma saison » sont côte à côte tant que leurs libellés tiennent chacun sur une ligne ; sinon le bouton passe au-dessus, sur toute la largeur, et le lien dessous, au milieu. Le libellé du bouton est toujours entier, à l'intérieur du bouton. À regarder surtout en allemand (« Meine Saison ansehen » avec « Ohne Pflanze weiter » : empilé sur presque tous les téléphones ; avec « Überspringen » : côte à côte), en anglais et en espagnol sur un petit écran, et en très gros texte, où le bouton peut grandir sur deux lignes sans rien couper. Pour voir « Continuer sans plante » à côté de « Voir ma saison » : ne rien cocher, chercher une plante, puis fermer le clavier (le pied est caché tant que le clavier est ouvert). Noter sur chaque appareil : côte à côte ou empilé. Vérifié sur la version web (quatre langues, de 320 à 440 points de large) et par calcul avec le moteur de mise en page de l'appli, pas encore sur un téléphone. Dans la version fusionnée avant la 1.8.3, ce libellé sortait du bouton en allemand sur les petits écrans.
- C7. La grille « De saison en [mois] », sous les plantes proposées, commence par les plantes les plus connues, dans le même ordre dans les quatre langues. En novembre : ail, petit pois, framboisier, cerisier, pommier, figuier, puis les autres par ordre alphabétique ; les trois plantes proposées au-dessus n'y sont pas répétées. Correction de la PR #62, pour le build qui suit la 1.8.3. Sur la 1.8.3, la grille est rangée par ordre alphabétique en anglais, en allemand et en espagnol : connu. En novembre, elle propose surtout des arbres fruitiers, même pour un jardin en pots : connu aussi.

### La préparation (P)

- P1. Trois lignes : la météo du lieu, le calendrier des plantes, les premiers gestes. Sans plante choisie, deux lignes : la météo du lieu et « Des plantes de saison ».
- P2. Une ligne ne se coche que quand son chargement est fini. L'écran ne dure jamais plus de 6 secondes.
- P3. Sans réseau, l'écran se retire quand même et le résultat s'affiche sans planter.
- P4. Rien qui fasse « IA » : pas d'étincelles, pas de pourcentage inventé, pas de phrase du genre « analyse en cours ».

### « Votre saison » (S)

- S1. Le titre nomme la ville. Les villes à article sont accordées : « au Mans », « aux Sables-d'Olonne », « à La Rochelle ».
- S2. La bande de la semaine montre les nuits de gel quand il y en a. Elle n'en invente pas. Le mot et le chiffre du gel restent lisibles et centrés dans leur colonne, même sur le petit iPhone et en allemand.
Depuis la PR #63, « Vos plantes » remplace « Dans votre planning » et le calendrier en barres (Pierre, 18/11, sur la 1.8.3 : la page « chargée », « pas très incitative » et « très brouillon »). Planches de cette version : `/mnt/project-files/produit/votre-saison/`.

- S3. « Vos plantes » : une carte claire, une ligne par plante, quatre plantes au plus. Chaque ligne a la photo de la plante, son nom, ce qu'il y a à faire, puis quand récolter. Ce qui se fait maintenant est écrit en vert (« Planter maintenant, jusqu'à fin décembre ») ; sinon, la prochaine étape (« Semer dès début mars ») ; dessous, en gris, la récolte (« Récolter dès début juin »). Les plantes à mettre en terre maintenant viennent d'abord, puis celles à récolter maintenant, puis celles de toute l'année, puis les plus proches. Relever toute photo absente, floue ou qui ne montre pas la plante.
- S4. La récolte. Jamais « Récolter maintenant » sous « Semer maintenant » ou « Planter maintenant ». Une plante à récolter maintenant n'a qu'une ligne (« Récolter maintenant, jusqu'à fin novembre »). Une plante qui se récolte toute l'année dit « Récolter toute l'année ». Pour un arbre ou une vivace plantés maintenant, la date est celle de la prochaine saison de récolte, sans dire qu'un jeune arbre ne donne qu'après quelques années : relever si cela paraît trompeur. Connu, sans effet en novembre : après un semis du printemps, la date de récolte peut tomber l'année suivante ; corrigé pour la version d'après.
- S5. Les dates suivent le climat du lieu : Toulouse est en avance sur Draveil, Lille en retard.
- S6. Sans lieu : pas de météo de la semaine, et une seule note sous la carte des plantes : « Dates moyennes : placez le jardin sur la carte pour les régler sur votre climat et recevoir vos rappels. » Plus de paragraphes d'avertissement. Avec un lieu, cette note nomme le climat du lieu et dit l'avance ou le retard de la saison.
- S7. Le sous-titre. « Le gel » (quand la météo du lieu est lue) et « Les maladies et les ravageurs » gardent leur phrase (« Le gel d'abord : … », « Maladies et ravageurs : … »). Pour les autres réponses et après « Passer », une accroche tirée des lignes : « 2 plantes à mettre en terre maintenant, et déjà de quoi récolter. », « Une plante à mettre en terre maintenant, premières récoltes en juin. », « De quoi récolter dès maintenant. » ou « Vos prochains gestes en mars. ». Elle doit dire vrai : le nombre est celui des lignes en vert, et « déjà de quoi récolter » demande une ligne « Récolter maintenant ».
- S8. Avec plus de quatre plantes, la note sous la carte commence par « Et N autres plantes dans votre jardin. », avec le bon nombre.
- S9. Sans plante choisie : sous le titre « Des plantes de saison », les plantes proposées à l'étape d'avant (trois au plus), dans la même carte, puis la note « Vous n'avez pas encore choisi de plantes : vous pourrez en ajouter depuis votre jardin. ». L'écran ne parle ni de « vos gestes » ni de « vos plantes ».
- S10. Sans plante choisie, le jardin créé ensuite est bien vide : les plantes de saison montrées n'y sont pas ajoutées, et aucun de leurs gestes n'entre au planning.
- S11. L'ordre des blocs suit la réponse : « Le gel », la météo de la semaine et ses nuits de gel, puis « Vos plantes » ; « Les maladies et les ravageurs », « À surveiller sur vos plantes » (photo, nom, et ce que la fiche dit de surveiller, dans une carte pareille à celle de « Vos plantes »), puis « Vos plantes », puis la météo ; « Penser à tout au bon moment », « Savoir quand semer et planter » et « Passer », « Vos plantes », puis la météo. L'écran n'a pas de photo d'en-tête.
- S12. Jardin placé hors de France (ajouté le 17/11 à 23 h 10 UTC). Dans la note sous la carte des plantes, une phrase nomme le climat du lieu et dit l'avance ou le retard de la saison, dans la langue du téléphone. Relever la phrase exacte et dire si elle paraît juste à quelqu'un du lieu. Ce que le serveur en ligne répond aujourd'hui : Cologne, « Nördliches Klima », environ 16 jours de retard ; Berlin, « Ozeanisches Klima », 27 jours de retard ; Munich, « Ozeanisches Klima », 24 ; Vienne, « Feuchtes Subtropenklima », 17 ; Londres, « Oceanic climate », 11 jours de retard ; Madrid, « Clima mediterráneo », 15 jours d'avance. Le nom du climat vient d'un découpage pensé pour la France (Cologne et Francfort y sont rangées avec le nord de la France) ou d'une classification mondiale (Vienne « subtropicale ») : c'est le retard ou l'avance qui compte pour les dates, mais le nom peut surprendre. À noter, sans bloquer. Les noms de maladies et de ravageurs viennent des fiches traduites : relever toute faute (connue : « Möhrefliege » pour « Möhrenfliege » sur la carotte, en allemand).
- S13. Au pied de « Votre saison », la phrase « On vous rappelle chaque geste le jour venu. » est au-dessus de « Continuer », dans la langue du téléphone. « Continuer » fait alors demander l'accord des notifications par le téléphone, avant Plus : c'est voulu, la raison est cette phrase. Relever seulement si la phrase manque, ou si la boîte du téléphone arrive sans elle.
- S14. L'avis d'ensemble, sur chaque appareil : faut-il faire défiler pour voir « Continuer » ? La page donne-t-elle envie de continuer, ou paraît-elle encore chargée ou brouillon ? Un avis franc, avec ce qui gêne en premier.

### Plus, temps 1 (U)

- U1. La croix de fermeture est visible dès l'arrivée. « Continuer avec la version gratuite » aussi.
- U2. L'écran se lit d'un regard : la marque « Hortenia Plus », un titre, une seule preuve et sa légende, le tableau Gratuit / Plus des cinq avantages, la note « Toujours gratuit ». Rien ne change de place après l'arrivée sur l'écran.
- U3. La preuve suit la réponse à la question. « Le gel » et « Penser à tout au bon moment » : une alerte comme elle arrive sur le téléphone. « Les maladies et les ravageurs » : un résultat du diagnostic photo. « Savoir quand semer et planter » : les questions qu'HortenIA propose. « Passer » : un jardin en 3D.
- U4. L'alerte. Si un gel est annoncé dans la semaine pour la ville, elle donne la température de la prévision et le nom du jardin, et la légende donne le soir où elle partirait (« si le gel se confirme »). Sans gel annoncé, elle porte la mention « Exemple ». Pour « Penser à tout », la légende dit que les rappels de gestes restent gratuits.
- U5. Le diagnostic. C'est un exemple, dit comme tel (« Exemple »). La légende reprend ce que la fiche d'une plante choisie dit de surveiller, dans la langue du téléphone ; sans plante choisie, elle reste générale. Le crédit de la photo est en bas de l'écran.
- U6. Le jardin d'exemple (question passée). Un jardin complet et net : serre, pommier, bacs, terrasse et banc. L'étiquette « Exemple » est en bas à gauche, rien ne déborde du cadre arrondi, et l'image n'est ni floue ni étirée. Le titre dit « Votre jardin en 3D » ; relever si l'étiquette suffit à comprendre que ce n'est pas encore le sien.
- U7. La place du jardin d'exemple. Il occupe la hauteur libre entre le titre et le tableau : pas de grand vide sous la note « Toujours gratuit », et le tableau n'est pas poussé sous le pied. Sur un petit écran, ou quand un intitulé du tableau passe sur deux lignes (allemand, très gros texte), le jardin est plus petit et le tableau reste entier. Noter sur chaque appareil la hauteur approximative du jardin, et s'il faut faire défiler pour lire la note. Ce point a été vérifié sur la version web et par calcul avec le moteur de mise en page de l'appli, pas encore sur un téléphone.
- U8. Le tableau : cinq lignes, celle de la preuve en premier. Aucune valeur sur deux lignes dans les colonnes « Gratuit » et « Plus ».
- U9. Le pied : le prix du store, son équivalent par mois, le bouton d'essai. Visible sans faire défiler, sans coupure au milieu d'un prix.
- U10. L'appli n'a qu'un thème, clair, même quand le téléphone est en mode sombre : c'est voulu, ne pas le signaler. Regarder seulement que les boîtes du système, qui passent en sombre (accord des notifications, fenêtre du store), restent lisibles par-dessus l'appli.
- U11. Sur iPhone, dans le paywall de A comme dans le temps 1 de B : chaque ligne du tableau Gratuit / Plus a la même taille de texte que ses voisines, aucune ne s'affiche en tout petit. Sur la 1.8.3, Pierre a vu la ligne « Questions à HortenIA » dessinée minuscule ; corrigé par la PR #63 (un texte trop long rapetisse au plus aux trois quarts de sa taille). À regarder surtout en allemand, sur le petit iPhone et en très gros texte. Sur Android, rien ne change.

### Plus, temps 2 (D)

- D1. « Rien à payer aujourd'hui » : la frise datée (aujourd'hui, rappel, fin de l'essai) avec de vraies dates, calculées depuis le jour du test.
- D2. Une seule formule en avant : l'annuel avec ses 7 jours d'essai, au prix du store. « Voir toutes les formules » montre le mensuel et, là où le store la propose (Android aujourd'hui), la formule à 19,99 € sans essai.
- D3. Sur Android, la phrase sur le moyen de paiement nomme Google Play. Sur iPhone, aucun autre store n'est nommé, nulle part.
- D4. « Revenir à ce que Plus ajoute » ramène au temps 1.
- D5. Le bouton d'achat ouvre la fenêtre du store avec la bonne formule.
- D6. Sur le petit iPhone en très gros texte, le pied (prix, bouton, lien de la version gratuite, mention de renouvellement) ne prend pas tout l'écran : la frise et la formule se lisent encore en faisant défiler au-dessus. Sur le web, dans une fenêtre de 375 × 470, il reste 225 points de haut pour le contenu du temps 2 et 243 pour celui du temps 1 (essai du 17/11, texte à sa taille normale).

### Après la fenêtre du store (F)

- F1. Fenêtre fermée sans achat : « Aucun paiement n'a été fait », « Réessayer » rouvre la fenêtre, « Continuer gratuitement » mène à l'écran « 14 jours » puis à la suite, comme dans A.
- F2. Achat fait : « Plus est actif », avec la date de fin de l'essai et la date du rappel.
- F3. Si les notifications ne sont pas encore accordées, l'accord est demandé ici, avec sa raison. « Plus tard » ne bloque rien.
- F4. Sur « Plus est actif », le jardin dessiné en 3D est celui de la personne, avec les plantes qu'elle a choisies, jamais le jardin d'exemple. Sans plante choisie, pas de dessin, et le bouton dit « Voir mon jardin ». « Voir mon jardin en 3D » ouvre bien la vue 3D du jardin, et pas la vue satellite ni le plan.
- F5. L'inscription reste proposée après, sans bloquer.
- F6. Le jardin retrouvé (PR #63, en A comme en B). Le compte invité et le potager sont créés dès le toucher de « Continuer » (sur « Votre saison » en B, sur « Votre jardin est prêt » en A), pendant la boîte des rappels et le paywall. Deux passages : (1) arriver sur le paywall, fermer tout à fait l'appli, la rouvrir : le jardin s'ouvre, avec le lieu et les plantes choisies, sans repasser par l'accueil ni revoir le paywall ; (2) parcours normal jusqu'au jardin : un seul jardin dans la liste des jardins, pas de doublon. Hors ligne au toucher de « Continuer », rien n'est créé d'avance : l'accueil se termine comme avant, au retour du paywall.

### La version A (A)

- A1. Avec `T43=A`, le parcours est celui de la 1.8.1 : même ordre, mêmes textes, même paywall. Seuls changements de la PR #63 dans A : le tableau du paywall sur iPhone (U11) et le jardin retrouvé après une sortie pendant le paywall (F6).
- A2. Aucun écran de B n'apparaît.
- A3. Seules différences admises dans A, en anglais, allemand et espagnol, sur l'écran du premier résultat : la fin de fenêtre d'un geste (« until… », « bis… », « hasta… ») passe sur sa propre ligne, comme en français ; dans la bande de la semaine, le mot du gel (« frost », « Frost », « helada ») est au-dessus du chiffre, centré ; en espagnol, la phrase du meilleur jour commence par le jour (« Martes, el mejor día para el huerto… »).

### Le jardin en 3D (V)

- V1. La 3D au pincement (PR #63 ; Pierre, 18/11 : « La 3D quand tu es très loin est pas net »). Sur l'écran du jardin, en vue 3D (avec Plus, ou la vue 3D offerte une fois ; sans elles, la vue est fixe et ne se zoome pas) : pincer pour zoomer jusqu'au plus près, puis déplacer le jardin. À la fin du geste, les traits et les plantes sont nets, jamais flous ni pixelisés ; pendant le geste, l'image peut s'affiner par petits à-coups. Le zoom s'arrête de lui-même (environ 3,5 fois au plus), et dézoomer ramène le jardin entier. Un jardin en plusieurs parties ou en L remplit mieux la vue à l'ouverture qu'avant. Noter sur chaque appareil si le geste reste fluide.

### Partout (G)

- G1. Aucun texte coupé ni chevauché sur le petit iPhone et en très gros texte.
- G2. Aucune phrase en français dans l'appli en anglais, en allemand ou en espagnol. Les prix ont le format de la langue.
- G3. Le retour du téléphone (Android) et le geste de retour (iPhone) ne perdent pas les choix déjà faits.
- G4. L'appli fermée puis rouverte au milieu du parcours reprend sans planter et sans rejouer un paywall au lancement.
- G5. Rien qui fasse « IA » : icônes génériques, visuels stéréotypés, phrases creuses. À relever sur chaque écran.
- G6. Dans les quatre langues, le titre d'un geste et sa fin de fenêtre (« jusqu'à fin novembre », « until the end of November ») sont sur deux lignes, sans virgule orpheline.

Pour V1, oliver ne paie rien : après le parcours, `python3 outils/site_tests.py compte plus` donne un compte de test
avec Plus actif ; connecte-toi avec (Profil, « J'ai déjà un compte », mot de passe tapé par `ecrire.py @mdp-compte`).
Aucun achat, même d'essai, dans aucune ligne de cette mission.

## Communauté et profil (PR #65) : un verdict par ligne

Pour ces lignes seulement, crée un compte de test : `python3 outils/site_tests.py compte email` (e-mail affiché, mot de
passe tapé par `ecrire.py @mdp-compte`). Un compte de test reste dans le banc : ses posts, réactions et changements de
profil ne sont jamais vus des vrais jardiniers. Pas de vraie adresse, pas de vrais liens de réseaux.

Réactions (sur le post du banc « Banc 1.8.4 : post de test pour les réactions. » et ses commentaires seulement ;
retire chaque réaction avant la fin) :
- **R1 Pile** : sous un post qui a des réactions, le bouton montre de nouveau celles des autres, en petites pastilles
  rondes, trois au plus, la plus donnée devant, avec le total. Ta propre réaction seule, si tu en as posé une.
- **R2 Choix** : appui long : les six réactions, lisibles aussi en texte agrandi (hanna), sans cacher le texte visé.
- **R3 Changer et retirer** : change de réaction, puis retire-la d'un toucher.
- **R4 Commentaires** : sous un commentaire, le cœur et « Répondre » se touchent du premier coup (cadres de 44 points),
  sans toucher le voisin.

Fil (CP, avec le compte de test) :
- **CP1 Modifier dans l'heure** : publie « Banc 1.8.4 : post de test de tom. » (texte seul, sans photo). Menu « … »
  puis « Modifier » : la fenêtre d'écriture se rouvre avec le texte ; change un mot, « Enregistrer » ; le post montre
  « (modifié) ». Sur iPhone : la fenêtre s'ouvre bien depuis le menu (une fenêtre qui s'ouvre pendant qu'une autre se
  ferme).
- **CP2 Modifier un commentaire** : sur ton post, commente « Commentaire de test. », puis modifie-le : la barre du bas
  passe en modification, clavier ouvert, sans être cachée par le clavier. « (modifié) » s'affiche.
- **CP3 Supprimer** : supprime ton commentaire puis ton post. Plus rien de toi ne reste dans le fil.
- **CP4 Place dans le fil** : descends dans le fil, ouvre une discussion, reviens : le fil revient au même endroit
  (pas tout en haut). Sur iPhone, le fil ne saute pas de la hauteur du bandeau d'en-tête pendant qu'il se charge.
- **CP5 Photo vers profil** : toucher la photo d'un auteur ouvre son profil (sur un post et sous un commentaire).

Profil (PR, avec le compte de test) :
- **PR1 Modifier le profil** : Profil, « Modifier mon profil » : nom, bio, « Je jardine depuis », façons de jardiner
  (quatre au plus : une cinquième est refusée). « Enregistrer » reste inactif tant que rien ne change.
- **PR2 Couverture et photo** : choisis une couverture et une photo dans la galerie (photo de tomate déjà sur le
  téléphone) ; elles s'affichent sur le profil public.
- **PR3 Réseaux** : tape `@banc_test` pour Instagram, avec le clavier ouvert : le champ reste visible. Un lien de groupe
  Facebook (`facebook.com/groups/test`) est refusé sous son champ. Enregistre, puis touche le lien Instagram du profil :
  note ce qui s'ouvre (appli Instagram absente sur le banc : navigateur ou rien), sans te connecter nulle part.
- **PR4 Profil public** : le profil montre couverture, année, façons et réseaux, et se lit bien en mode sombre du
  téléphone (l'appli reste claire).

## Non-régression (NR)
- **NR1** : jardin, plan (En rangs, Taille et forme), Calculer, planning, Mes graines : aucun plantage, aucun écran blanc.
- **NR2** : rien de ce qui était bon dans la 1.8.3 n'a reculé (tracé, « Angles droits », point décimal en anglais,
  nom du climat hors de France).

Rien de publié dans la Communauté hors du post de test de CP1 (supprimé en CP3), réaction seulement sur le post du banc
et ses commentaires, retirée à la fin, aucun code ni lien de parrainage envoyé, aucune question à HortenIA, pas de diagnostic, aucun achat.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes, dont : ta version (A ou B) et la preuve (`banc_versions`).
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable / sans objet) | capture(s) | ce que tu as vu |`
   pour chaque ligne (Q, C, P, S, U, D, F, A, V, G, R, CP, PR, NR). Bloquant = plantage, écran blanc, jardin perdu, impossible
   d'avancer, paiement possible sans le vouloir.
3. Mots français ou mal traduits : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. Autres bugs vus, du plus grave au moins grave. Distingue ce que tu as vu de ce que tu supposes.
