# 1.7 : plan des vérifications par persona

Fichier généré par `python3 outils/plan_1_7.py` (ne pas modifier à la main). Couverture vérifiée : chaque chantier de l'appli et chaque version de chaque test au moins une fois sur Android et une fois sur iPhone/iPad.

## odile (Android) : Pixel 2 (5 pouces), Android 13, texte x1,3
- Persona : Odile, 66 ans, Dunkerque, retraitée, potager de 40 m² venté, lit lentement et grossit le texte de son téléphone.
- Jardin : Dunkerque (nord). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T17 B, T22 B, T25 D, T26 B, T29 B ; toutes les autres en A.
- À vérifier :
  - **T25 D** · Texte du bouton du paywall : « Diagnostiquer mes plantes gratuitement »
  - **T22 B** · Durée de l'essai : 14 jours partout : bouton, frise (rappel 2 jours avant la fin), Profil › Abonnement
  - **T26 B** · Sa 3D sur le paywall : sa 3D floutée « Votre jardin en 3D, avec le Plus » : bien ses plantes (et son dessin si T4 B), pas de lenteur
  - **T29 B** · « J'aime » ouvert aux invités : un invité peut aimer ; publier et commenter demandent toujours un compte
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T4 A** · Essayer avant le paywall : parcours actuel, paywall à la fin de l'onboarding
  - **T17 B** · Premier geste photo : 1re tâche « Prendre une photo de mon potager » ; la photo la coche, puis l'appli propose un diagnostic
  - **T38 A** · Série de semaines : pas de série
  - **L4-demander** · « Demander à la communauté » après un diagnostic incertain : le bouton apparaît pour un diagnostic incertain, pas pour un sûr ; publication préremplie (ne pas publier)
  - **L7-graines** · Grainothèque « Mes graines » : ajouter trois sachets (photo de la galerie), en retirer un, retrouver le rappel de semis dans le planning

## rachid (Android) : Pixel 7 Pro, Android 15, mode sombre
- Persona : Rachid, 41 ans, Perpignan, jardin de 120 m² au soleil, arrosage difficile l'été, pressé, téléphone en mode sombre.
- Jardin : Perpignan (sud). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T4 B, T5 B, T38 B ; toutes les autres en A.
- À vérifier :
  - **T5 B** · Paywall de saison : de novembre à février « Votre jardin en 3D » et « HortenIA sans limite » en tête ; au 1er mars (date imposée) le diagnostic reprend la tête
  - **T13 A** · Heure du rappel du jour : 8 h pour qui n'a pas choisi
  - **T27 A** · Quotas gratuits : 1 diagnostic par mois, le 2e montre la limite
  - **T41 A** · Parrainage : pas de lien
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T4 B** · Essayer avant le paywall : écran « Essayez tout de suite » : diagnostic, dessin 2D ou « Passer », puis paywall
  - **T32 A** · « Une photo de ce geste ? » : rien après une tâche cochée
  - **T38 B** · Série de semaines : « N semaines d'affilée » sur Jardin et dans le récap ; avec la date imposée, 3 semaines actives puis une vide : retour à zéro
  - **L4-filtres** · Filtres par région et par plante : filtrer le fil sur une plante et une région, puis tout effacer
  - **L7-widget** · Widget « À faire cette semaine » : si le banc le permet : petit et grand, clair et sombre ; sinon le noter « non testable »

## colette (Android) : Pixel Tablet (10,9 pouces), Android 14
- Persona : Colette, 58 ans, Strasbourg, potager familial de 60 m², prépare tout sur sa tablette dans la cuisine.
- Jardin : Strasbourg (nord). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T1 B, T9 B, T28 B, T33 B ; toutes les autres en A.
- À vérifier :
  - **T1 B** · Quand demander les notifications : phrase sur « Votre jardin est prêt » puis fenêtre système
  - **T9 B** · Récap du dimanche : avec la photo de la semaine (la toucher ouvre la publication)
  - **T14 A** · Relance d'absence : texte actuel
  - **T28 B** · « Le Plus vous aurait prévenu » : compte gratuit + alerte imposée : carte le lendemain (date imposée), au plus une par semaine ; le paywall s'ouvre seulement sur « Voir le Plus »
  - **L2-e-mail** · E-mail du dimanche (T15) : compte avec e-mail sans notifications : aperçu de l'e-mail ; interrupteur « Recevoir le récap par e-mail » dans Profil › Notifications ; lien de désinscription présent
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T7 A** · Défi photo du lundi : défi épinglé dans le fil seulement
  - **T33 B** · Plusieurs photos au diagnostic : 1 à 3 photos (feuille, plante entière, dessous) : un diagnostic à 3 photos puis à 1 photo
  - **L1-moteur** · Moteur d'A/B tests : versions imposées depuis l'outil, retrouvées après relance de l'appli ; même version après réinstallation pour un compte
  - **L5-suivi** · Suivi à 7 jours avec la photo d'avant : date imposée à J+7 : photo d'avant et nouvelle côte à côte, les deux dans le carnet

## baptiste (Android) : Pixel 6, Android 14
- Persona : Baptiste, 35 ans, Annecy, abonné Hortenia Plus, grand jardin en pente avec serre, curieux de la 3D et d'HortenIA.
- Jardin : Annecy (froid). Compte : compte de test Plus : `python3 outils/site_tests.py compte plus`, puis « J'ai déjà un compte » après l'onboarding.
- Versions imposées avant le lancement : T13 B, T41 B ; toutes les autres en A.
- À vérifier :
  - **T1 A** · Quand demander les notifications : carte de l'accueil
  - **T9 A** · Récap du dimanche : récap actuel
  - **T13 B** · Heure du rappel du jour : heure d'ouverture habituelle pour qui n'a pas choisi ; un compte qui choisit 19 h garde 19 h
  - **T31 A** · Une question près de chez vous : rien
  - **T41 B** · Parrainage : lien d'invitation dans Profil ; filleul de test via l'outil : un mois de Plus des deux côtés ; le même appareil ne compte pas
  - **L2-essai** · Accompagner l'essai (T20) : aperçu à J+1 et à J+5, pour un essai de 7 jours puis de 14 jours : seulement ce qui a vraiment servi
  - **L3-prix** · Prix dans Profil › Abonnement : « Ensuite 29,99 € par an, prélevés le … » pendant l'essai ou l'abonnement (prix en dollars sur simulateur iPhone : pas un bug)
  - **L6-amenagement** · Aménager son jardin avec l'IA (Plus) : photos d'un jardin réel (galerie), d'un jardin vide, une photo sans jardin ; plan 2D puis 3D ; « Garder ce plan » puis « Annuler » ; compte gratuit : le bouton ouvre le paywall
  - **L6-hortenia-plan** · HortenIA modifie le plan (Plus) : une demande simple, une impossible (« un bananier à Lille »), une annulée ; le plan s'affiche avant d'être gardé
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste

## agathe (Android) : Pixel 3a (5,6 pouces), Android 13, texte x1,15
- Persona : Agathe, 24 ans, Rennes, étudiante, 3 bacs sur une terrasse partagée, ne veut pas créer de compte tout de suite.
- Jardin : Rennes (nord). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T6 B, T21 B, T24 B, T39 B, T42 B ; toutes les autres en A.
- À vérifier :
  - **T25 A** · Texte du bouton du paywall : « Commencer l'essai gratuit »
  - **T21 B** · Formule cochée sur le paywall : mensuel coché (4,99 €), la frise annonce 4,99 €
  - **T24 B** · Preuve sociale du paywall : l'avis + « N potagers créés avec Hortenia » (comparer avec /stats/publiques via l'outil)
  - **T28 A** · « Le Plus vous aurait prévenu » : aucune carte
  - **T39 B** · Moment de la carte « Gardez votre jardin » : après 3 tâches cochées
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T6 B** · Notification du lendemain : météo de la nuit chez soi + premier geste du planning (aperçu jardin du Nord et du Sud, avec et sans geste)
  - **T33 A** · Plusieurs photos au diagnostic : 1 photo
  - **T42 B** · Notification d'activité : aperçu : avec 2 publications rien ne part, avec 6 la notification part
  - **L5-carnet** · Diagnostic gardé dans le carnet : « Garder dans le carnet » : note datée et photo dans la fiche de la plante ; plante absente proposée à l'ajout ; HortenIA les cite

## lucien (Android) : Pixel 5, Android 12 (ancien téléphone), texte x1,15
- Persona : Lucien, 71 ans, Briançon (1 300 m), potager de montagne, gel tôt et tard, téléphone ancien qu'il garde longtemps.
- Jardin : Briançon (froid). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T10 B, T11 B, T24 C, T25 C, T37 B ; toutes les autres en A.
- À vérifier :
  - **T25 C** · Texte du bouton du paywall : « Voir mon jardin en 3D »
  - **T10 B** · Bouton « Fait » sur le rappel du jour : bouton « Fait » quand le rappel nomme un seul geste : le toucher, puis ouvrir l'appli et trouver le geste coché
  - **T24 C** · Preuve sociale du paywall : deux vrais avis 5 étoiles différents ; jamais la note 3,7, jamais « jardiniers »
  - **T37 B** · Une vue 3D offerte : 1re ouverture : sa 3D puis paywall à la sortie ; ensuite le bouton ouvre le paywall, même après réinstallation
  - **L1-mesures** · Mesures qui manquent : permission des notifications envoyée au 1er lancement (sur Android 12 et moins elle est accordée d'office : l'événement doit quand même partir), raison d'abandon de la fenêtre d'achat (ouvrir puis fermer l'achat), commentaire : retrouver les événements avec `site_tests.py evenements`
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T11 B** · Pastille sur l'onglet Communauté : point après une nouvelle publication, disparaît à l'ouverture de l'onglet ; pas de cloche dans la Communauté
  - **T36 A** · Partage après « Garder ce plan » : rien
  - **L1-7jours** · Correction « 7 jours » : aperçu du message d'essai pour 7 jours puis 14 jours : la durée annoncée suit l'offre
  - **L6-lien-3d** · Lien et QR code sur l'affiche, 3D dans le navigateur : ouvrir le lien de l'affiche dans le navigateur du téléphone : 3D en lecture seule, aucune adresse ni position précise, « Créer le mien » ouvre le store

## maeva (Android) : Pixel 8, Android 15, mode sombre
- Persona : Maëva, 30 ans, Montpellier, balcon plein sud de 5 m², vient d'une vidéo TikTok, très active sur les réseaux.
- Jardin : Montpellier (sud). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T36 B, T39 C ; toutes les autres en A.
- À vérifier :
  - **T5 A** · Paywall de saison : « Diagnostic photo illimité » en tête
  - **T22 A** · Durée de l'essai : 7 jours
  - **T26 A** · Sa 3D sur le paywall : photo d'illustration actuelle
  - **T29 A** · « J'aime » ouvert aux invités : le cœur ouvre « Un compte pour participer »
  - **T39 C** · Moment de la carte « Gardez votre jardin » : après une première photo ; jamais deux fois le même jour
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T17 A** · Premier geste photo : planning actuel
  - **T36 B** · Partage après « Garder ce plan » : l'affiche 3D est proposée ; partage vers la Communauté (annuler avant d'envoyer) et vers les applis du téléphone
  - **L4-photo-semaine** · Photo de la semaine : aperçu du choix sur une semaine factice avec égalité de « j'aime »
  - **L7-agenda** · Ajouter ses gestes à l'agenda : « Ajouter à mon agenda » (sans notifications) : gestes dans l'agenda du téléphone, une seule fois même avec deux appuis

## denis (Android) : Pixel 4 (5,7 pouces), Android 13, texte x1,3
- Persona : Denis, 52 ans, Pontarlier, jardinier confirmé, hiver très froid, veut un planning fiable et des alertes.
- Jardin : Pontarlier (froid). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T7 B, T9 C, T14 B, T25 B, T31 B ; toutes les autres en A.
- À vérifier :
  - **T25 B** · Texte du bouton du paywall : « Commencer mes 7 jours gratuits » (le nombre suit l'offre)
  - **T9 C** · Récap du dimanche : avec un conseil d'HortenIA écrit pour ses plantes et sa météo
  - **T14 B** · Relance d'absence : geste de saison (« Cette semaine au potager : planter l'ail. »)
  - **T31 B** · Une question près de chez vous : aperçu de la notification quand un compte de test proche publie sur une de ses plantes
  - **L2-cartes** · Cartes au-dessus de « Mon potager » : chaque carte s'affiche au-dessus de « Mon potager » ; les outils ne bougent pas quand une carte apparaît ou se ferme ; une grande carte à la fois
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T7 B** · Défi photo du lundi : défi épinglé + carte du défi sur l'écran Jardin qui ouvre la publication avec le défi choisi (ne pas publier)
  - **T34 A** · Identifier en premier en hiver : l'onglet Diagnostic s'ouvre sur les maladies
  - **L1-site** · Site hortenia.com/tests : (Android et iPhone : navigateur du téléphone) ouvrir la page, mauvais mot de passe refusé, page lisible sur petit écran ; ne rien couper ni imposer hors du test factice
  - **L5-maladies** · Alertes oïdium, rouille, pucerons : aperçu avec météo imposée favorable à chaque maladie, jardin avec et sans plante sensible

## salome (Android) : Pixel 7, Android 16
- Persona : Salomé, 37 ans, Bordeaux, jardin de ville de 30 m² avec ses enfants, aime les défis photo.
- Jardin : Bordeaux (sud). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T27 B, T32 B ; toutes les autres en A.
- À vérifier :
  - **T21 A** · Formule cochée sur le paywall : annuel coché (29,99 €)
  - **T24 A** · Preuve sociale du paywall : l'avis actuel
  - **T27 B** · Quotas gratuits : 3 diagnostics passent, le 4e montre la limite
  - **T39 A** · Moment de la carte « Gardez votre jardin » : le lendemain ou dès la 1re tâche cochée
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T6 A** · Notification du lendemain : texte actuel
  - **T32 B** · « Une photo de ce geste ? » : proposition après une tâche cochée, une seule fois même avec deux tâches la même semaine ; publication préremplie (ne pas publier)
  - **T42 A** · Notification d'activité : rien
  - **L4-compte-hortenia** · Compte Hortenia officiel : badge visible sur une publication du compte, en clair et en sombre
  - **L8-dettes** · Petites dettes : le tutoriel du premier jour ne promet plus « Débloquez des avantages en participant »

## henri (Android) : Pixel Fold (pliable, écran intérieur), Android 14
- Persona : Henri, 45 ans, Lille, jardin ombragé au nord de 50 m², technophile, utilise son téléphone pliable déplié.
- Jardin : Lille (nord). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T1 C, T14 C, T34 B ; toutes les autres en A.
- À vérifier :
  - **T1 C** · Quand demander les notifications : après la 1re tâche cochée, « On vous rappelle le prochain geste ? »
  - **T10 A** · Bouton « Fait » sur le rappel du jour : rappel actuel
  - **T14 C** · Relance d'absence : météo qui arrive chez soi, sinon le texte de B
  - **T37 A** · Une vue 3D offerte : 3D réservée au Plus
  - **L4-reponse24h** · Réponse sous 24 h : une question de test reçoit la réponse signée « HortenIA, l'assistant de l'appli » (délai court sur compte de test, via l'outil)
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T11 A** · Pastille sur l'onglet Communauté : pas de pastille
  - **T34 B** · Identifier en premier en hiver : en novembre il s'ouvre sur l'identification ; au 1er mars (date imposée) sur les maladies
  - **L1-outils** · Outils des testeurs : imposer une version, imposer une date, lire les événements, « Envoyer maintenant », aperçu d'un message : chacun marche
  - **L6-3d-saisons** · 3D qui suit les saisons : date imposée en janvier (givre ou neige) puis en juin (plantes grandies) ; pas de saccade

## margaux (iPhone/iPad) : iPhone SE 3 (4,7 pouces), iOS 18, texte très grand
- Persona : Margaux, 63 ans, Caen, petit potager de 20 m², vue fatiguée, texte très grand, n'aime pas créer des comptes.
- Jardin : Caen (nord). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T24 C, T25 B, T29 B, T34 B, T39 C ; toutes les autres en A.
- À vérifier :
  - **T25 B** · Texte du bouton du paywall : « Commencer mes 7 jours gratuits » (le nombre suit l'offre)
  - **T22 A** · Durée de l'essai : 7 jours
  - **T24 C** · Preuve sociale du paywall : deux vrais avis 5 étoiles différents ; jamais la note 3,7, jamais « jardiniers »
  - **T29 B** · « J'aime » ouvert aux invités : un invité peut aimer ; publier et commenter demandent toujours un compte
  - **T39 C** · Moment de la carte « Gardez votre jardin » : après une première photo ; jamais deux fois le même jour
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T11 A** · Pastille sur l'onglet Communauté : pas de pastille
  - **T34 B** · Identifier en premier en hiver : en novembre il s'ouvre sur l'identification ; au 1er mars (date imposée) sur les maladies
  - **L1-outils** · Outils des testeurs : imposer une version, imposer une date, lire les événements, « Envoyer maintenant », aperçu d'un message : chacun marche
  - **L6-3d-saisons** · 3D qui suit les saisons : date imposée en janvier (givre ou neige) puis en juin (plantes grandies) ; pas de saccade

## yannick (iPhone/iPad) : iPhone 17 Pro Max, iOS 26, mode sombre
- Persona : Yannick, 39 ans, Toulon, jardin de 80 m² en restanques, chaleur et sécheresse, mode sombre.
- Jardin : Toulon (sud). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T4 B, T5 B, T13 B, T38 B, T41 B ; toutes les autres en A.
- À vérifier :
  - **T5 B** · Paywall de saison : de novembre à février « Votre jardin en 3D » et « HortenIA sans limite » en tête ; au 1er mars (date imposée) le diagnostic reprend la tête
  - **T13 B** · Heure du rappel du jour : heure d'ouverture habituelle pour qui n'a pas choisi ; un compte qui choisit 19 h garde 19 h
  - **T27 A** · Quotas gratuits : 1 diagnostic par mois, le 2e montre la limite
  - **T41 B** · Parrainage : lien d'invitation dans Profil ; filleul de test via l'outil : un mois de Plus des deux côtés ; le même appareil ne compte pas
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T4 B** · Essayer avant le paywall : écran « Essayez tout de suite » : diagnostic, dessin 2D ou « Passer », puis paywall
  - **T32 A** · « Une photo de ce geste ? » : rien après une tâche cochée
  - **T38 B** · Série de semaines : « N semaines d'affilée » sur Jardin et dans le récap ; avec la date imposée, 3 semaines actives puis une vide : retour à zéro
  - **L4-filtres** · Filtres par région et par plante : filtrer le fil sur une plante et une région, puis tout effacer
  - **L8-dettes** · Petites dettes : le tutoriel du premier jour ne promet plus « Débloquez des avantages en participant »

## brigitte (iPhone/iPad) : iPad 11 pouces (A16), iOS 26
- Persona : Brigitte, 61 ans, Orléans, grand potager de 150 m², planifie sur son iPad le soir.
- Jardin : Orléans (nord). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T1 B, T6 B, T9 B, T42 B ; toutes les autres en A.
- À vérifier :
  - **T1 B** · Quand demander les notifications : phrase sur « Votre jardin est prêt » puis fenêtre système
  - **T9 B** · Récap du dimanche : avec la photo de la semaine (la toucher ouvre la publication)
  - **T14 A** · Relance d'absence : texte actuel
  - **T28 A** · « Le Plus vous aurait prévenu » : aucune carte
  - **L1-mesures** · Mesures qui manquent : permission des notifications envoyée au 1er lancement (sur Android 12 et moins elle est accordée d'office : l'événement doit quand même partir), raison d'abandon de la fenêtre d'achat (ouvrir puis fermer l'achat), commentaire : retrouver les événements avec `site_tests.py evenements`
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T6 B** · Notification du lendemain : météo de la nuit chez soi + premier geste du planning (aperçu jardin du Nord et du Sud, avec et sans geste)
  - **T33 A** · Plusieurs photos au diagnostic : 1 photo
  - **T42 B** · Notification d'activité : aperçu : avec 2 publications rien ne part, avec 6 la notification part
  - **L5-carnet** · Diagnostic gardé dans le carnet : « Garder dans le carnet » : note datée et photo dans la fiche de la plante ; plante absente proposée à l'ajout ; HortenIA les cite

## theo (iPhone/iPad) : iPhone 17, iOS 26
- Persona : Théo, 33 ans, Grenoble, abonné Hortenia Plus, jardin partagé de 70 m², veut aménager son jardin à partir de photos.
- Jardin : Grenoble (froid). Compte : compte de test Plus : `python3 outils/site_tests.py compte plus`, puis « J'ai déjà un compte » après l'onboarding.
- Versions imposées avant le lancement : T10 B ; toutes les autres en A.
- À vérifier :
  - **T9 A** · Récap du dimanche : récap actuel
  - **T10 B** · Bouton « Fait » sur le rappel du jour : bouton « Fait » quand le rappel nomme un seul geste : le toucher, puis ouvrir l'appli et trouver le geste coché
  - **T31 A** · Une question près de chez vous : rien
  - **T41 A** · Parrainage : pas de lien
  - **L2-essai** · Accompagner l'essai (T20) : aperçu à J+1 et à J+5, pour un essai de 7 jours puis de 14 jours : seulement ce qui a vraiment servi
  - **L3-prix** · Prix dans Profil › Abonnement : « Ensuite 29,99 € par an, prélevés le … » pendant l'essai ou l'abonnement (prix en dollars sur simulateur iPhone : pas un bug)
  - **L6-amenagement** · Aménager son jardin avec l'IA (Plus) : photos d'un jardin réel (galerie), d'un jardin vide, une photo sans jardin ; plan 2D puis 3D ; « Garder ce plan » puis « Annuler » ; compte gratuit : le bouton ouvre le paywall
  - **L6-hortenia-plan** · HortenIA modifie le plan (Plus) : une demande simple, une impossible (« un bananier à Lille »), une annulée ; le plan s'affiche avant d'être gardé
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **L7-graines** · Grainothèque « Mes graines » : ajouter trois sachets (photo de la galerie), en retirer un, retrouver le rappel de semis dans le planning

## solene (iPhone/iPad) : iPhone 13 mini (5,4 pouces), iOS 18, mode sombre, petit texte
- Persona : Solène, 28 ans, Brest, jardinière en pots sur un rebord de fenêtre, pluie et vent, curieuse mais pressée.
- Jardin : Brest (nord). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T22 B, T25 D, T36 B ; toutes les autres en A.
- À vérifier :
  - **T25 D** · Texte du bouton du paywall : « Diagnostiquer mes plantes gratuitement »
  - **T22 B** · Durée de l'essai : 14 jours partout : bouton, frise (rappel 2 jours avant la fin), Profil › Abonnement
  - **T26 A** · Sa 3D sur le paywall : photo d'illustration actuelle
  - **T37 A** · Une vue 3D offerte : 3D réservée au Plus
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T4 A** · Essayer avant le paywall : parcours actuel, paywall à la fin de l'onboarding
  - **T17 A** · Premier geste photo : planning actuel
  - **T36 B** · Partage après « Garder ce plan » : l'affiche 3D est proposée ; partage vers la Communauté (annuler avant d'envoyer) et vers les applis du téléphone
  - **L4-photo-semaine** · Photo de la semaine : aperçu du choix sur une semaine factice avec égalité de « j'aime »
  - **L7-agenda** · Ajouter ses gestes à l'agenda : « Ajouter à mon agenda » (sans notifications) : gestes dans l'agenda du téléphone, une seule fois même avec deux appuis

## pascal (iPhone/iPad) : iPhone 16, iOS 18, texte grand
- Persona : Pascal, 57 ans, Gérardmer (670 m), potager de montagne, neige de novembre à mars, prépare ses graines l'hiver.
- Jardin : Gérardmer (froid). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T11 B, T14 C, T25 C, T31 B ; toutes les autres en A.
- À vérifier :
  - **T25 C** · Texte du bouton du paywall : « Voir mon jardin en 3D »
  - **T10 A** · Bouton « Fait » sur le rappel du jour : rappel actuel
  - **T14 C** · Relance d'absence : météo qui arrive chez soi, sinon le texte de B
  - **T31 B** · Une question près de chez vous : aperçu de la notification quand un compte de test proche publie sur une de ses plantes
  - **L2-cartes** · Cartes au-dessus de « Mon potager » : chaque carte s'affiche au-dessus de « Mon potager » ; les outils ne bougent pas quand une carte apparaît ou se ferme ; une grande carte à la fois
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T11 B** · Pastille sur l'onglet Communauté : point après une nouvelle publication, disparaît à l'ouverture de l'onglet ; pas de cloche dans la Communauté
  - **T36 A** · Partage après « Garder ce plan » : rien
  - **L1-7jours** · Correction « 7 jours » : aperçu du message d'essai pour 7 jours puis 14 jours : la durée annoncée suit l'offre
  - **L6-lien-3d** · Lien et QR code sur l'affiche, 3D dans le navigateur : ouvrir le lien de l'affiche dans le navigateur du téléphone : 3D en lecture seule, aucune adresse ni position précise, « Créer le mien » ouvre le store

## anais (iPhone/iPad) : iPhone Air, iOS 26
- Persona : Anaïs, 26 ans, Nice, balcon de 8 m², découvre le jardinage, partage tout sur les réseaux.
- Jardin : Nice (sud). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T27 B, T32 B ; toutes les autres en A.
- À vérifier :
  - **T1 A** · Quand demander les notifications : carte de l'accueil
  - **T21 A** · Formule cochée sur le paywall : annuel coché (29,99 €)
  - **T24 A** · Preuve sociale du paywall : l'avis actuel
  - **T27 B** · Quotas gratuits : 3 diagnostics passent, le 4e montre la limite
  - **T39 A** · Moment de la carte « Gardez votre jardin » : le lendemain ou dès la 1re tâche cochée
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T6 A** · Notification du lendemain : texte actuel
  - **T32 B** · « Une photo de ce geste ? » : proposition après une tâche cochée, une seule fois même avec deux tâches la même semaine ; publication préremplie (ne pas publier)
  - **T42 A** · Notification d'activité : rien
  - **L4-compte-hortenia** · Compte Hortenia officiel : badge visible sur une publication du compte, en clair et en sombre

## gilles (iPhone/iPad) : iPhone 16 Plus, iOS 18, texte très grand
- Persona : Gilles, 68 ans, Amiens, jardin ouvrier de 200 m², confirmé, lit tout en très grand.
- Jardin : Amiens (nord). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T9 C, T14 B, T28 B, T33 B ; toutes les autres en A.
- À vérifier :
  - **T25 A** · Texte du bouton du paywall : « Commencer l'essai gratuit »
  - **T9 C** · Récap du dimanche : avec un conseil d'HortenIA écrit pour ses plantes et sa météo
  - **T14 B** · Relance d'absence : geste de saison (« Cette semaine au potager : planter l'ail. »)
  - **T28 B** · « Le Plus vous aurait prévenu » : compte gratuit + alerte imposée : carte le lendemain (date imposée), au plus une par semaine ; le paywall s'ouvre seulement sur « Voir le Plus »
  - **L2-e-mail** · E-mail du dimanche (T15) : compte avec e-mail sans notifications : aperçu de l'e-mail ; interrupteur « Recevoir le récap par e-mail » dans Profil › Notifications ; lien de désinscription présent
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T7 A** · Défi photo du lundi : défi épinglé dans le fil seulement
  - **T33 B** · Plusieurs photos au diagnostic : 1 à 3 photos (feuille, plante entière, dessous) : un diagnostic à 3 photos puis à 1 photo
  - **L1-moteur** · Moteur d'A/B tests : versions imposées depuis l'outil, retrouvées après relance de l'appli ; même version après réinstallation pour un compte
  - **L5-suivi** · Suivi à 7 jours avec la photo d'avant : date imposée à J+7 : photo d'avant et nouvelle côte à côte, les deux dans le carnet

## jeanne (iPhone/iPad) : iPad mini (A17 Pro), iOS 18, texte grand
- Persona : Jeanne, 49 ans, Avignon, jardin de 60 m² très chaud, utilise l'iPad mini de sa fille.
- Jardin : Avignon (sud). Compte : invité, ne crée jamais de compte.
- Versions imposées avant le lancement : T1 C, T7 B, T21 B, T24 B, T39 B ; toutes les autres en A.
- À vérifier :
  - **T1 C** · Quand demander les notifications : après la 1re tâche cochée, « On vous rappelle le prochain geste ? »
  - **T21 B** · Formule cochée sur le paywall : mensuel coché (4,99 €), la frise annonce 4,99 €
  - **T24 B** · Preuve sociale du paywall : l'avis + « N potagers créés avec Hortenia » (comparer avec /stats/publiques via l'outil)
  - **T29 A** · « J'aime » ouvert aux invités : le cœur ouvre « Un compte pour participer »
  - **T39 B** · Moment de la carte « Gardez votre jardin » : après 3 tâches cochées
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T7 B** · Défi photo du lundi : défi épinglé + carte du défi sur l'écran Jardin qui ouvre la publication avec le défi choisi (ne pas publier)
  - **T34 A** · Identifier en premier en hiver : l'onglet Diagnostic s'ouvre sur les maladies
  - **L1-site** · Site hortenia.com/tests : (Android et iPhone : navigateur du téléphone) ouvrir la page, mauvais mot de passe refusé, page lisible sur petit écran ; ne rien couper ni imposer hors du test factice
  - **L5-maladies** · Alertes oïdium, rouille, pucerons : aperçu avec météo imposée favorable à chaque maladie, jardin avec et sans plante sensible

## victor (iPhone/iPad) : iPhone 17 Pro, iOS 26, mode sombre
- Persona : Victor, 42 ans, Besançon, jardin de 90 m², invite volontiers ses amis, mode sombre.
- Jardin : Besançon (froid). Compte : compte par e-mail, créé après l'onboarding.
- Versions imposées avant le lancement : T17 B, T26 B, T37 B ; toutes les autres en A.
- À vérifier :
  - **T5 A** · Paywall de saison : « Diagnostic photo illimité » en tête
  - **T13 A** · Heure du rappel du jour : 8 h pour qui n'a pas choisi
  - **T26 B** · Sa 3D sur le paywall : sa 3D floutée « Votre jardin en 3D, avec le Plus » : bien ses plantes (et son dessin si T4 B), pas de lenteur
  - **T37 B** · Une vue 3D offerte : 1re ouverture : sa 3D puis paywall à la sortie ; ensuite le bouton ouvre le paywall, même après réinstallation
  - **L4-reponse24h** · Réponse sous 24 h : une question de test reçoit la réponse signée « HortenIA, l'assistant de l'appli » (délai court sur compte de test, via l'outil)
  - **L6-sans-ia** · Retirer ce qui fait IA : plus d'étincelle (10 endroits, dont l'onglet et l'écran d'HortenIA), icônes des 4 outils et des 4 onglets redessinées, textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez » ; la mention « réponse générée par IA » sous HortenIA reste
  - **T17 B** · Premier geste photo : 1re tâche « Prendre une photo de mon potager » ; la photo la coche, puis l'appli propose un diagnostic
  - **T38 A** · Série de semaines : pas de série
  - **L4-demander** · « Demander à la communauté » après un diagnostic incertain : le bouton apparaît pour un diagnostic incertain, pas pour un sûr ; publication préremplie (ne pas publier)
  - **L7-widget** · Widget « À faire cette semaine » : si le banc le permet : petit et grand, clair et sombre ; sinon le noter « non testable »
