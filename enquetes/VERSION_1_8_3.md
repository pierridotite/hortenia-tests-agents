# Mission 1.8.3 (build 114/151) : parcours d'accueil B (test T43) et réactions refaites

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad). Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta
persona : tape les textes à toucher dans la langue de l'écran. Compte environ 80 gestes, jusqu'à 70 minutes. Donne un
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

| Persona | Version | Réponse à la question | Particularité |
|---|---|---|---|
| sophie | B | Le gel | lieu : Draveil ; mode sombre (U10) |
| yves | B | Passer | refuse la localisation, aucun lieu (S6) ; jardin d'exemple (U6, U7) |
| tom | B | Les maladies et les ravageurs | lieu : Toulouse (S5, U5) |
| lucia | B | Savoir quand semer et planter (en espagnol) | lieu : Madrid (S12) ; mode sombre |
| lukas | B | Penser à tout au bon moment (en allemand) | lieu : Berlin (S12) ; mots longs, pied des plantes (C6) |
| emily | A | (parcours actuel, en anglais) | A inchangé, voir A3 |
| oliver | B | Le gel (en anglais) | lieu : Londres (S12) ; va jusqu'à la fenêtre d'achat (D5, F1), la ferme sans acheter |
| raymond | B | Passer | lieu : Le Mans (S1 « au Mans ») ; jardin d'exemple sur le plus petit écran (U7, D6) |
| hanna | B | Le gel (en allemand) | ne coche aucune plante, sans rien cocher, relève d'abord le pied (« Diese 3 Saisonpflanzen hinzufügen », « Ohne Pflanze weiter », C3) ; puis cherche une plante et ferme le clavier (pied du point C6), et continue avec « Ohne Pflanze weiter » (C5, S9, S10) ; lieu : Köln (S12) |
| kevin | A | (parcours actuel) | A inchangé, mode sombre |

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
- C4. À l'étape du lieu, « Je le ferai plus tard » suit les deux cartes de position : il n'est plus fixé au bas de l'écran et, en très gros texte, il se lit en faisant défiler. La carte touchée dit « Recherche de votre position… » pendant l'attente (corrections de la PR #58).
- C5. Sans plante cochée, pendant une recherche de plante, « Ajouter ces 3 plantes de saison » ne se montre pas (PR #58) : le pied dit « Continuer sans plante » et « Voir ma saison », et les deux mènent à « Votre saison » avec les plantes de saison proposées. Recherche effacée, la proposition revient.
- C6. Le pied de l'étape des plantes (1.8.3). Le lien (« Passer » ou « Continuer sans plante ») et le bouton « Voir ma saison » sont côte à côte tant que leurs libellés tiennent chacun sur une ligne ; sinon le bouton passe au-dessus, sur toute la largeur, et le lien dessous, au milieu. Le libellé du bouton est toujours entier, à l'intérieur du bouton. À regarder surtout en allemand (« Meine Saison ansehen » avec « Ohne Pflanze weiter » : empilé sur presque tous les téléphones ; avec « Überspringen » : côte à côte), en anglais et en espagnol sur un petit écran, et en très gros texte, où le bouton peut grandir sur deux lignes sans rien couper. Pour voir « Continuer sans plante » à côté de « Voir ma saison » : ne rien cocher, chercher une plante, puis fermer le clavier (le pied est caché tant que le clavier est ouvert). Noter sur chaque appareil : côte à côte ou empilé. Vérifié sur la version web (quatre langues, de 320 à 440 points de large) et par calcul avec le moteur de mise en page de l'appli, pas encore sur un téléphone. Dans la version fusionnée avant la 1.8.3, ce libellé sortait du bouton en allemand sur les petits écrans.

### La préparation (P)

- P1. Trois lignes : la météo du lieu, le calendrier des plantes, les premiers gestes. Sans plante choisie, deux lignes : la météo du lieu et « Des plantes de saison ».
- P2. Une ligne ne se coche que quand son chargement est fini. L'écran ne dure jamais plus de 6 secondes.
- P3. Sans réseau, l'écran se retire quand même et le résultat s'affiche sans planter.
- P4. Rien qui fasse « IA » : pas d'étincelles, pas de pourcentage inventé, pas de phrase du genre « analyse en cours ».

### « Votre saison » (S)

- S1. Le titre nomme la ville. Les villes à article sont accordées : « au Mans », « aux Sables-d'Olonne », « à La Rochelle ».
- S2. La bande de la semaine montre les nuits de gel quand il y en a. Elle n'en invente pas. Le mot et le chiffre du gel restent lisibles et centrés dans leur colonne, même sur le petit iPhone et en allemand.
- S3. « Dans votre planning » : les gestes affichés sont ceux qu'on retrouve ensuite dans le planning du jardin, aux mêmes dates.
- S4. Le calendrier montre chaque plante sur 12 mois (semis, plantation, récolte) et une phrase par plante (« Semis dès mi-février », « Récolte en cours, jusqu'à fin novembre »).
- S5. Les dates suivent le climat du lieu : Toulouse est en avance sur Draveil, Lille en retard.
- S6. Sans lieu : ni semaine ni climat, et l'écran dit « Dates de référence ».
- S7. Le sous-titre répond à la réponse donnée (gel, maladies, oubli, semis). Après « Passer », il reste neutre.
- S8. Avec plus de plantes que l'écran n'en montre, « Et N autres plantes dans votre jardin » est juste.
- S9. Sans plante choisie : l'écran montre le calendrier des plantes de saison proposées à l'étape d'avant, sous le titre « Des plantes de saison », et dit qu'aucune plante n'est encore choisie. Il ne parle ni de « vos gestes » ni de « vos plantes ».
- S10. Sans plante choisie, le jardin créé ensuite est bien vide : les plantes de saison montrées n'y sont pas ajoutées, et aucun de leurs gestes n'entre au planning.
- S11. Le bloc qui répond à la réponse passe en premier : « Le gel », la météo de la semaine et ses nuits de gel ; « Penser à tout au bon moment », le planning ; « Savoir quand semer et planter », le calendrier ; « Les maladies et les ravageurs », le bloc « À surveiller sur vos plantes », tiré des fiches. L'écran n'a plus de photo d'en-tête.

- S12. Jardin hors de France : sous le titre du calendrier de « Votre saison », une ligne nomme le climat du lieu et dit l'avance ou le retard de la saison, dans la langue du téléphone. Recopie la phrase exacte et dis si elle paraît juste à quelqu'un du lieu (attendu à peu près : Köln « Nördliches Klima », ~16 jours de retard ; Berlin « Ozeanisches Klima », ~27 ; London « Oceanic climate », ~11 jours de retard ; Madrid « Clima mediterráneo », ~15 jours d'avance). Le nom du climat peut surprendre : note-le sans en faire un bloquant. Relève aussi toute faute dans les noms de maladies et ravageurs (connue : « Möhrefliege » au lieu de « Möhrenfliege »).

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
- U10. En mode sombre, les preuves restent lisibles (l'alerte, le diagnostic, le cadre pâle du jardin).

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

### La version A (A)

- A1. Avec `T43=A`, le parcours est celui de la 1.8.1 : même ordre, mêmes textes, même paywall.
- A2. Aucun écran de B n'apparaît.
- A3. Seules différences admises dans A, en anglais, allemand et espagnol, sur l'écran du premier résultat : la fin de fenêtre d'un geste (« until… », « bis… », « hasta… ») passe sur sa propre ligne, comme en français ; dans la bande de la semaine, le mot du gel (« frost », « Frost », « helada ») est au-dessus du chiffre, centré ; en espagnol, la phrase du meilleur jour commence par le jour (« Martes, el mejor día para el huerto… »).

### Partout (G)

- G1. Aucun texte coupé ni chevauché sur le petit iPhone, en très gros texte, en mode sombre.
- G2. Aucune phrase en français dans l'appli en anglais, en allemand ou en espagnol. Les prix ont le format de la langue.
- G3. Le retour du téléphone (Android) et le geste de retour (iPhone) ne perdent pas les choix déjà faits.
- G4. L'appli fermée puis rouverte au milieu du parcours reprend sans planter et sans rejouer un paywall au lancement.
- G5. Rien qui fasse « IA » : icônes génériques, visuels stéréotypés, phrases creuses. À relever sur chaque écran.
- G6. Dans les quatre langues, le titre d'un geste et sa fin de fenêtre (« jusqu'à fin novembre », « until the end of November ») sont sur deux lignes, sans virgule orpheline.

## Réactions refaites (1.8.3) : un verdict par ligne
Uniquement sur le post du banc « Banc 1.8.2 : post de test pour les réactions. » et sur les commentaires de CE post
(ne réagis jamais ailleurs). Retire chaque réaction posée avant la fin. Personas en A comme en B.
- **R1 Bouton** : sous le post, un seul bouton. Sans réaction de ta part, il montre un cœur ❤️ rouge « J'aime » ; le
  nombre à côté est terracotta. Après « Ça pousse », le bouton ne montre QUE ton 🌱 (une seule image, jamais « 🌱❤️ »).
- **R2 Choix** : appui long sur le bouton : le choix des six réactions s'ouvre sans cacher le texte du post visé ; chaque
  réaction y montre son nombre. Sur Android, note où il s'ouvre (au-dessus ou au-dessous, place dans l'écran).
- **R3 Changer et retirer** : change de réaction (une autre que la première) ; puis un toucher sur le bouton retire ta
  réaction et le bouton revient au ❤️.
- **R4 Commentaires** : ouvre les commentaires du post du banc. Sous un commentaire : bouton ❤️ rouge, appui long =
  choix des six réactions, change, puis retire d'un toucher.
- **R5 Invité** : si tu n'as pas de compte, réagir (post ou commentaire) demande un compte, sans planter. Ne crée pas
  de compte : ferme.
- **R6 Lecture d'écran** (si l'outil le permet : arbre d'accessibilité) : le bouton dit la réaction et le nombre de façon
  compréhensible (« J'aime, 3 » et pas « coeur coeur 3 »).

## Non-régression (NR)
- **NR1** : jardin, plan (En rangs, Taille et forme), Calculer, planning, Mes graines : aucun plantage, aucun écran blanc.
- **NR2** : rien de ce qui était bon dans la 1.8.2 n'a reculé (tracé, « Angles droits », point décimal en anglais).

Toujours rien de publié dans la Communauté, réaction seulement sur le post du banc et ses commentaires, retirée à la
fin, aucun code ni lien de parrainage envoyé, aucune question à HortenIA, pas de diagnostic, aucun achat.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes, dont : ta version (A ou B) et la preuve (`banc_versions`).
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable / sans objet) | capture(s) | ce que tu as vu |`
   pour chaque ligne (Q, C, P, S, U, D, F, A, G, R, NR). Bloquant = plantage, écran blanc, jardin perdu, impossible
   d'avancer, paiement possible sans le vouloir.
3. Mots français ou mal traduits : `| écran | texte affiché | ce qu'un natif écrirait | capture |`, ou « Rien vu ».
4. Autres bugs vus, du plus grave au moins grave. Distingue ce que tu as vu de ce que tu supposes.
