"""Plan de test de la 1.7 (avec les retours de Pierre du 9/11) : qui vérifie quoi, avec quelles versions imposées.
Écrit enquetes/VERSION_1_7_PLAN.md et plan_1_7.json, et vérifie la couverture :
chaque chantier de l'appli et chaque version de chaque test au moins une fois
sur iPhone/iPad et une fois sur Android. Usage : python3 outils/plan_1_7.py"""
import json, itertools, sys

# Tests A/B de la 1.7 joués dans l'appli ou le serveur : code -> (titre, versions, contrainte)
TESTS = {
 "T1": ("Quand demander les notifications", {"A": "carte de l'accueil", "B": "phrase sur « Votre jardin est prêt » puis fenêtre système", "C": "après la 1re tâche cochée, « On vous rappelle le prochain geste ? »"}, {"android13": True}),
 "T4": ("Essayer avant le paywall", {"A": "parcours actuel, paywall à la fin de l'onboarding", "B": "écran « Essayez tout de suite » : diagnostic, dessin 2D ou « Passer », puis paywall"}, {}),
 "T5": ("Paywall de saison", {"A": "« Diagnostic photo illimité » en tête", "B": "de novembre à février « Votre jardin en 3D » et « HortenIA sans limite » en tête ; au 1er mars (date imposée) le diagnostic reprend la tête"}, {"compte": "gratuit"}),
 "T6": ("Notification du lendemain", {"A": "texte actuel", "B": "météo de la nuit chez soi + premier geste du planning (aperçu jardin du Nord et du Sud, avec et sans geste)"}, {}),
 "T7": ("Défi photo du lundi", {"A": "défi épinglé dans le fil seulement", "B": "défi épinglé + carte du défi sur l'écran Jardin qui ouvre la publication avec le défi choisi (ne pas publier)"}, {}),
 "T9": ("Récap du dimanche", {"A": "récap actuel", "B": "avec la photo de la semaine (la toucher ouvre la publication)", "C": "avec un conseil d'HortenIA écrit pour ses plantes et sa météo"}, {"compte": "compte"}),
 "T10": ("Bouton « Fait » sur le rappel du jour", {"A": "rappel actuel", "B": "bouton « Fait » quand le rappel nomme un seul geste : le toucher, puis ouvrir l'appli et trouver le geste coché"}, {"compte": "compte"}),
 "T11": ("Pastille sur l'onglet Communauté", {"A": "pas de pastille", "B": "point après une nouvelle publication, disparaît à l'ouverture de l'onglet ; pas de cloche dans la Communauté"}, {}),
 "T13": ("Heure du rappel du jour", {"A": "8 h pour qui n'a pas choisi", "B": "heure d'ouverture habituelle pour qui n'a pas choisi ; un compte qui choisit 19 h garde 19 h"}, {"compte": "email"}),
 "T14": ("Relance d'absence", {"A": "texte actuel", "B": "geste de saison (« Cette semaine au potager : planter l'ail. »)", "C": "météo qui arrive chez soi, sinon le texte de B"}, {"compte": "compte"}),
 "T17": ("Premier geste photo", {"A": "planning actuel", "B": "1re tâche « Prendre une photo de mon potager » ; la photo la coche, puis l'appli propose un diagnostic"}, {}),
 "T21": ("Formule cochée sur le paywall", {"A": "annuel coché (29,99 €)", "B": "mensuel coché (4,99 €), la frise annonce 4,99 €"}, {"compte": "gratuit"}),
 "T22": ("Durée de l'essai", {"A": "7 jours", "B": "14 jours partout : bouton, frise (rappel 2 jours avant la fin), Profil › Abonnement"}, {"compte": "gratuit"}),
 "T24": ("Preuve sociale du paywall", {"A": "l'avis actuel", "B": "l'avis + « N potagers créés avec Hortenia » (comparer avec /stats/publiques via l'outil)", "C": "deux vrais avis 5 étoiles différents ; jamais la note 3,7, jamais « jardiniers »"}, {"compte": "gratuit"}),
 "T25": ("Texte du bouton du paywall", {"A": "« Commencer l'essai gratuit »", "B": "« Commencer mes 7 jours gratuits » (le nombre suit l'offre)", "C": "« Voir mon jardin en 3D »", "D": "« Diagnostiquer mes plantes gratuitement »"}, {"compte": "gratuit", "petit": True}),
 "T26": ("Sa 3D sur le paywall", {"A": "photo d'illustration actuelle", "B": "sa 3D floutée « Votre jardin en 3D, avec le Plus » : bien ses plantes (et son dessin si T4 B), pas de lenteur"}, {"compte": "gratuit"}),
 "T27": ("Quotas gratuits", {"A": "1 diagnostic par mois, le 2e montre la limite", "B": "3 diagnostics passent, le 4e montre la limite"}, {"compte": "gratuit"}),
 "T28": ("« Le Plus vous aurait prévenu »", {"A": "aucune carte", "B": "compte gratuit + `simuler alerte code=vent_violent` (ou pluie_forte, chaleur_forte ; pas gel) : carte le jour même, sans changer la date (le serveur suit sa propre horloge), au plus une par semaine ; le paywall s'ouvre seulement sur « Voir le Plus »"}, {"compte": "gratuit"}),
 "T29": ("« J'aime » ouvert aux invités", {"A": "le cœur ouvre « Un compte pour participer »", "B": "un invité peut aimer ; publier et commenter demandent toujours un compte"}, {"compte": "invite"}),
 "T31": ("Une question près de chez vous", {"A": "rien", "B": "aperçu de la notification quand un compte de test proche publie sur une de ses plantes"}, {"compte": "compte"}),
 "T32": ("« Une photo de ce geste ? »", {"A": "rien après une tâche cochée", "B": "proposition après une tâche cochée, une seule fois même avec deux tâches la même semaine ; publication préremplie (ne pas publier)"}, {}),
 "T33": ("Plusieurs photos au diagnostic", {"A": "1 photo", "B": "1 à 3 photos (feuille, plante entière, dessous) : un diagnostic à 3 photos puis à 1 photo"}, {}),
 "T34": ("Identifier en premier en hiver", {"A": "l'onglet Diagnostic s'ouvre sur les maladies", "B": "en novembre il s'ouvre sur l'identification ; au 1er mars (date imposée) sur les maladies"}, {}),
 "T36": ("Partage après « Garder ce plan »", {"A": "rien", "B": "l'affiche 3D est proposée ; partage vers la Communauté (annuler avant d'envoyer) et vers les applis du téléphone"}, {}),
 "T37": ("Une vue 3D offerte", {"A": "3D réservée au Plus", "B": "1re ouverture : sa 3D puis paywall à la sortie ; ensuite le bouton ouvre le paywall, même après réinstallation"}, {"compte": "gratuit"}),
 "T38": ("Série de semaines", {"A": "pas de série", "B": "« N semaines d'affilée » sur Jardin et dans le récap ; avec la date imposée, 3 semaines actives puis une vide : retour à zéro"}, {}),
 "T39": ("Moment de la carte « Gardez votre jardin »", {"A": "le lendemain ou dès la 1re tâche cochée", "B": "après 3 tâches cochées", "C": "après une première photo ; jamais deux fois le même jour"}, {"compte": "invite"}),
 "T41": ("Parrainage", {"A": "pas de lien", "B": "lien d'invitation dans Profil ; filleul de test via l'outil : un mois de Plus des deux côtés ; le même appareil ne compte pas"}, {"compte": "email"}),
 "T42": ("Notification d'activité", {"A": "rien", "B": "aperçu : avec 2 publications rien ne part, avec 6 la notification part"}, {}),
}

# Chantiers sans test (ou outils) vérifiés par les testeurs. contrainte : compte, plateforme...
CHANTIERS = [
 ("L1-moteur", "Moteur d'A/B tests", "versions imposées depuis l'outil, retrouvées après relance de l'appli ; même version après réinstallation pour un compte", {}),
 ("L1-site", "Site hortenia.com/tests", "(Android et iPhone : navigateur du téléphone) ouvrir la page, mauvais mot de passe refusé, page lisible sur petit écran ; ne rien couper ni imposer hors du test factice", {}),
 ("L1-mesures", "Mesures qui manquent", "permission des notifications envoyée au 1er lancement (sur Android 12 et moins elle est accordée d'office : l'événement doit quand même partir), raison d'abandon de la fenêtre d'achat (ouvrir puis fermer l'achat), commentaire : retrouver les événements avec `site_tests.py evenements`", {"android_max": 32}),
 ("L1-outils", "Outils des testeurs", "imposer une version, imposer une date, lire les événements, « Envoyer maintenant », aperçu d'un message : chacun marche", {}),
 ("L1-7jours", "Correction « 7 jours »", "aperçu du message d'essai pour 7 jours puis 14 jours : la durée annoncée suit l'offre", {}),
 ("L2-e-mail", "E-mail du dimanche (T15)", "compte avec e-mail sans notifications : aperçu de l'e-mail ; interrupteur « Recevoir le récap par e-mail » dans Profil › Notifications ; lien de désinscription présent", {"compte": "email"}),
 ("L2-essai", "Accompagner l'essai (T20)", "aperçu à J+1 et à J+5, pour un essai de 7 jours puis de 14 jours : seulement ce qui a vraiment servi", {"compte": "plus"}),
 ("L2-cartes", "Cartes au-dessus de « Mon potager »", "chaque carte s'affiche au-dessus de « Mon potager » ; les outils ne bougent pas quand une carte apparaît ou se ferme ; une grande carte à la fois", {"cartes": True}),
 ("L3-prix", "Prix dans Profil › Abonnement", "« Ensuite 29,99 € par an, prélevés le … » pendant l'essai ou l'abonnement (prix en dollars sur simulateur iPhone : pas un bug)", {"compte": "plus"}),
 ("L4-photo-semaine", "Photo de la semaine", "aperçu du choix sur une semaine factice avec égalité de « j'aime »", {}),
 ("L4-demander", "« Demander à la communauté » après un diagnostic incertain", "le bouton apparaît pour un diagnostic incertain, pas pour un sûr ; publication préremplie (ne pas publier)", {}),
 ("L4-reponse24h", "Réponse sous 24 h", "une question de test reçoit la réponse signée « HortenIA, l'assistant de l'appli » (délai court sur compte de test, via l'outil)", {"compte": "compte"}),
 ("L4-filtres", "Filtres par région et par plante", "filtrer le fil sur une plante et une région, puis tout effacer", {}),
 ("L4-compte-hortenia", "Compte Hortenia officiel", "badge visible sur une publication du compte, en clair et en sombre", {}),
 ("L5-carnet", "Diagnostic gardé dans le carnet", "« Garder dans le carnet » : note datée et photo dans la fiche de la plante ; plante absente proposée à l'ajout ; HortenIA les cite", {}),
 ("L5-suivi", "Suivi à 7 jours avec la photo d'avant", "date imposée à J+7 : photo d'avant et nouvelle côte à côte, les deux dans le carnet", {}),
 ("L5-maladies", "Alertes oïdium, rouille, pucerons", "aperçu avec météo imposée favorable à chaque maladie, jardin avec et sans plante sensible", {}),
 ("L6-amenagement", "Aménager son jardin avec l'IA (Plus)", "photos d'un jardin réel (galerie), d'un jardin vide, une photo sans jardin ; plan 2D puis 3D ; « Garder ce plan » puis « Annuler » ; compte gratuit : le bouton ouvre le paywall", {"compte": "plus"}),
 ("L6-hortenia-plan", "HortenIA modifie le plan (Plus)", "une demande simple, une impossible (« un bananier à Lille »), une annulée ; le plan s'affiche avant d'être gardé", {"compte": "plus"}),
 ("L6-3d-saisons", "3D qui suit les saisons", "date imposée en janvier (givre ou neige) puis en juin (plantes grandies) ; pas de saccade", {}),
 ("L6-lien-3d", "Lien et QR code sur l'affiche, 3D dans le navigateur", "ouvrir le lien de l'affiche dans le navigateur du téléphone : 3D en lecture seule, aucune adresse ni position précise, « Créer le mien » ouvre le store", {}),
 ("L6-sans-ia", "Retirer ce qui fait IA", "textes : plus de « Assistant IA », « notre IA experte », « intelligente », « Découvrez », plus d'étincelle ; la mention « réponse générée par IA » sous HortenIA reste. Icônes des outils et des onglets : Pierre a choisi le 9/11 de garder celles d'avant, ce n'est pas un défaut ; signaler seulement une icône floue, mal alignée ou un mélange d'anciennes et de nouvelles", {"tous": True}),
 ("L7-agenda", "Ajouter ses gestes à l'agenda", "« Ajouter à mon agenda » (sans notifications) : choisir un agenda, les gestes des 8 semaines y arrivent, une seule fois même avec deux appuis", {}),
 ("L7-graines", "Grainothèque « Mes graines »", "ajouter trois sachets (photo de la galerie), en retirer un, retrouver le rappel de semis dans le planning", {}),
 ("L7-widget", "Widget « À faire cette semaine »", "si le banc le permet : petit et grand, clair et sombre ; un jour sans geste, image du jardin sur le petit ; compte Plus avec alerte gel imposée, rappel du gel avec le geste sur le grand ; sinon le noter « non testable »", {}),
 ("L8-dettes", "Petites dettes", "le tutoriel du premier jour ne promet plus « Débloquez des avantages en participant »", {}),
 # Retours de Pierre du 9/11 et Aménager « Taille et forme » (PR #35)
 ("R9-clavier", "Saisie au-dessus du clavier", "sur chaque écran où l'on écrit (HortenIA, publication, commentaire, note du carnet, compte, recherche) : le champ et le bouton d'envoi restent visibles au-dessus du clavier, aussi en texte grand ; rien n'est caché sous le clavier", {}),
 ("R9-admins", "Chaque publication signalée aux administrateurs", "aperçu de la notification des administrateurs avec l'outil (groupée la nuit : « Par Odile et 2 autres ») ; si `liste` ne la propose pas, la noter « non testable »", {}),
 ("R9-parrainage", "Pas de parrainage dans la Communauté", "écrire un code ou un lien de parrainage dans une publication puis dans un commentaire (brouillon) : l'appli le refuse ou prévient ; ne jamais envoyer, noter ce que l'appli dit avant l'envoi", {}),
 ("R9-reactions", "Barres de vues, partage et 8 réactions rapides", "sur une publication : des barres à la place de l'œil, l'icône de partage du téléphone, 8 réactions en emojis qui tiennent sur une ligne (petit écran, texte grand) ; ouvrir le choix puis fermer sans réagir", {}),
 ("R9-gel-gratuit", "Gel réservé à Plus (compte gratuit)", "`apercu meteo_gel_plus` puis `envoyer meteo_gel_plus` : « Hortenia Plus vous aurait prévenu hier soir » (texte et ce que l'appli montre) ; sous une alerte voilée, pas de conseil du même sujet (gel, chaleur, vent) ; le paywall ne s'ouvre que si on le demande", {"compte": "gratuit"}),
 ("R9-gel-plus", "Alerte gel d'un abonné", "compte Plus : l'alerte gel s'affiche normalement, sans voile ; `apercu meteo_gel_plus` doit être refusé pour un compte Plus (jamais de « vous aurait prévenu » pour un abonné)", {"compte": "plus"}),
 ("R9-sans-essai", "Annuel sans essai à 19,99 € la 1re année", "si l'offre « Annuel, sans essai » apparaît (paywall, Profil › Abonnement) : 19,99 € la 1re année puis 29,99 € par an, écrit clairement ; ne jamais acheter ; si elle n'apparaît pas, le noter (prix en dollars sur simulateur iPhone : pas un bug)", {"compte": "gratuit"}),
 ("R9-forme-carte", "Aménager « Taille et forme », jardin tracé sur la carte", "onglets « Plantes et décor » et « Taille et forme » sous le plan ; tirer un coin puis un côté (pas de 25 cm, longueurs en direct, vue recadrée au lâcher) ; croiser deux côtés est refusé ; « Revenir à la forme d'avant » ; « Retracer sur la carte » ; rien n'est gardé sans « Enregistrer »", {}),
 ("R9-forme-rectangle", "Aménager « Taille et forme », jardin sans carte", "Longueur et Largeur sous le plan, au demi-mètre (1 à 50 m) ; réduire jusqu'à ce qu'une plante ne tienne plus : avant d'enregistrer, la feuille dit ce qui est retiré, ce qui reste hors du plan et ce qui est déplacé ; la surface suit sur l'accueil", {}),
]

PERSONAS = [
 # Android
 dict(id="odile", plateforme="android", compte="invite", ville="Dunkerque", pos=[51.0343, 2.3768], zone="nord",
      appareil={"profil": "pixel_2", "android_api": 33, "taille_texte": 1.3, "theme": "clair", "nom": "Pixel 2 (5 pouces), Android 13, texte x1,3"}, petit=True,
      profil="Odile, 66 ans, Dunkerque, retraitée, potager de 40 m² venté, lit lentement et grossit le texte de son téléphone."),
 dict(id="rachid", plateforme="android", compte="email", ville="Perpignan", pos=[42.6887, 2.8948], zone="sud",
      appareil={"profil": "pixel_7_pro", "android_api": 35, "taille_texte": 1.0, "theme": "sombre", "nom": "Pixel 7 Pro, Android 15, mode sombre"},
      profil="Rachid, 41 ans, Perpignan, jardin de 120 m² au soleil, arrosage difficile l'été, pressé, téléphone en mode sombre."),
 dict(id="colette", plateforme="android", compte="email", ville="Strasbourg", pos=[48.5839, 7.7455], zone="nord",
      appareil={"profil": "pixel_tablet", "android_api": 34, "taille_texte": 1.0, "theme": "clair", "nom": "Pixel Tablet (10,9 pouces), Android 14"},
      profil="Colette, 58 ans, Strasbourg, potager familial de 60 m², prépare tout sur sa tablette dans la cuisine."),
 dict(id="baptiste", plateforme="android", compte="plus", ville="Annecy", pos=[45.8992, 6.1294], zone="froid",
      appareil={"profil": "pixel_6", "android_api": 34, "taille_texte": 1.0, "theme": "clair", "nom": "Pixel 6, Android 14"},
      profil="Baptiste, 35 ans, Annecy, abonné Hortenia Plus, grand jardin en pente avec serre, curieux de la 3D et d'HortenIA."),
 dict(id="agathe", plateforme="android", compte="invite", ville="Rennes", pos=[48.1173, -1.6778], zone="nord",
      appareil={"profil": "pixel_3a", "android_api": 33, "taille_texte": 1.15, "theme": "clair", "nom": "Pixel 3a (5,6 pouces), Android 13, texte x1,15"}, petit=True,
      profil="Agathe, 24 ans, Rennes, étudiante, 3 bacs sur une terrasse partagée, ne veut pas créer de compte tout de suite."),
 dict(id="lucien", plateforme="android", compte="email", ville="Briançon", pos=[44.8986, 6.6436], zone="froid",
      appareil={"profil": "pixel_5", "android_api": 31, "taille_texte": 1.15, "theme": "clair", "nom": "Pixel 5, Android 12 (ancien téléphone), texte x1,15"}, petit=True,
      profil="Lucien, 71 ans, Briançon (1 300 m), potager de montagne, gel tôt et tard, téléphone ancien qu'il garde longtemps."),
 dict(id="maeva", plateforme="android", compte="invite", ville="Montpellier", pos=[43.6108, 3.8767], zone="sud",
      appareil={"profil": "pixel_8", "android_api": 35, "taille_texte": 1.0, "theme": "sombre", "nom": "Pixel 8, Android 15, mode sombre"},
      profil="Maëva, 30 ans, Montpellier, balcon plein sud de 5 m², vient d'une vidéo TikTok, très active sur les réseaux."),
 dict(id="denis", plateforme="android", compte="email", ville="Pontarlier", pos=[46.9046, 6.3543], zone="froid",
      appareil={"profil": "pixel_4", "android_api": 33, "taille_texte": 1.3, "theme": "clair", "nom": "Pixel 4 (5,7 pouces), Android 13, texte x1,3"}, petit=True,
      profil="Denis, 52 ans, Pontarlier, jardinier confirmé, hiver très froid, veut un planning fiable et des alertes."),
 dict(id="salome", plateforme="android", compte="invite", ville="Bordeaux", pos=[44.8378, -0.5792], zone="sud",
      appareil={"profil": "pixel_7", "android_api": 36, "taille_texte": 1.0, "theme": "clair", "nom": "Pixel 7, Android 16"},
      profil="Salomé, 37 ans, Bordeaux, jardin de ville de 30 m² avec ses enfants, aime les défis photo."),
 dict(id="henri", plateforme="android", compte="email", ville="Lille", pos=[50.6292, 3.0573], zone="nord",
      appareil={"profil": "pixel_fold", "android_api": 34, "taille_texte": 1.0, "theme": "clair", "nom": "Pixel Fold (pliable, écran intérieur), Android 14"},
      profil="Henri, 45 ans, Lille, jardin ombragé au nord de 50 m², technophile, utilise son téléphone pliable déplié."),
 # iPhone / iPad
 dict(id="margaux", plateforme="ios", compte="invite", ville="Caen", pos=[49.1829, -0.3707], zone="nord",
      appareil={"simulateur": "iPhone SE (3rd generation)", "ios": "18", "taille_texte": "accessibility-medium", "theme": "light", "nom": "iPhone SE 3 (4,7 pouces), iOS 18, texte très grand"}, petit=True,
      profil="Margaux, 63 ans, Caen, petit potager de 20 m², vue fatiguée, texte très grand, n'aime pas créer des comptes."),
 dict(id="yannick", plateforme="ios", compte="email", ville="Toulon", pos=[43.1242, 5.928], zone="sud",
      appareil={"simulateur": "iPhone 17 Pro Max", "ios": "26", "taille_texte": "large", "theme": "dark", "nom": "iPhone 17 Pro Max, iOS 26, mode sombre"},
      profil="Yannick, 39 ans, Toulon, jardin de 80 m² en restanques, chaleur et sécheresse, mode sombre."),
 dict(id="brigitte", plateforme="ios", compte="email", ville="Orléans", pos=[47.9029, 1.9093], zone="nord",
      appareil={"simulateur": "iPad (A16)", "ios": "26", "taille_texte": "large", "theme": "light", "nom": "iPad 11 pouces (A16), iOS 26"},
      profil="Brigitte, 61 ans, Orléans, grand potager de 150 m², planifie sur son iPad le soir."),
 dict(id="theo", plateforme="ios", compte="plus", ville="Grenoble", pos=[45.1885, 5.7245], zone="froid",
      appareil={"simulateur": "iPhone 17", "ios": "26", "taille_texte": "large", "theme": "light", "nom": "iPhone 17, iOS 26"},
      profil="Théo, 33 ans, Grenoble, abonné Hortenia Plus, jardin partagé de 70 m², veut aménager son jardin à partir de photos."),
 dict(id="solene", plateforme="ios", compte="invite", ville="Brest", pos=[48.3904, -4.4861], zone="nord",
      appareil={"simulateur": "iPhone 13 mini", "ios": "18", "taille_texte": "small", "theme": "dark", "nom": "iPhone 13 mini (5,4 pouces), iOS 18, mode sombre, petit texte"}, petit=True,
      profil="Solène, 28 ans, Brest, jardinière en pots sur un rebord de fenêtre, pluie et vent, curieuse mais pressée."),
 dict(id="pascal", plateforme="ios", compte="email", ville="Gérardmer", pos=[48.0727, 6.8771], zone="froid",
      appareil={"simulateur": "iPhone 16", "ios": "18", "taille_texte": "extra-large", "theme": "light", "nom": "iPhone 16, iOS 18, texte grand"}, petit=True,
      profil="Pascal, 57 ans, Gérardmer (670 m), potager de montagne, neige de novembre à mars, prépare ses graines l'hiver."),
 dict(id="anais", plateforme="ios", compte="invite", ville="Nice", pos=[43.7102, 7.262], zone="sud",
      appareil={"simulateur": "iPhone Air", "ios": "26", "taille_texte": "large", "theme": "light", "nom": "iPhone Air, iOS 26"},
      profil="Anaïs, 26 ans, Nice, balcon de 8 m², découvre le jardinage, partage tout sur les réseaux."),
 dict(id="gilles", plateforme="ios", compte="email", ville="Amiens", pos=[49.8941, 2.2958], zone="nord",
      appareil={"simulateur": "iPhone 16 Plus", "ios": "18", "taille_texte": "extra-extra-large", "theme": "light", "nom": "iPhone 16 Plus, iOS 18, texte très grand"}, petit=True,
      profil="Gilles, 68 ans, Amiens, jardin ouvrier de 200 m², confirmé, lit tout en très grand."),
 dict(id="jeanne", plateforme="ios", compte="invite", ville="Avignon", pos=[43.9493, 4.8055], zone="sud",
      appareil={"simulateur": "iPad mini (A17 Pro)", "ios": "18", "taille_texte": "extra-large", "theme": "light", "nom": "iPad mini (A17 Pro), iOS 18, texte grand"},
      profil="Jeanne, 49 ans, Avignon, jardin de 60 m² très chaud, utilise l'iPad mini de sa fille."),
 dict(id="victor", plateforme="ios", compte="email", ville="Besançon", pos=[47.2378, 6.0241], zone="froid",
      appareil={"simulateur": "iPhone 17 Pro", "ios": "26", "taille_texte": "large", "theme": "dark", "nom": "iPhone 17 Pro, iOS 26, mode sombre"},
      profil="Victor, 42 ans, Besançon, jardin de 90 m², invite volontiers ses amis, mode sombre."),
]

COMPTES = {"invite": "invité, ne crée jamais de compte",
           "email": "compte par e-mail, créé après l'onboarding",
           "plus": "compte de test Plus : `python3 outils/site_tests.py compte plus`, puis « J'ai déjà un compte » après l'onboarding"}

def compatible(p, c):
    k = c.get("compte")
    if k == "gratuit" and p["compte"] == "plus": return False
    if k == "compte" and p["compte"] == "invite": return False
    if k in ("email", "plus", "invite") and p["compte"] != k:
        if not (k == "email" and p["compte"] == "plus"): return False
    if c.get("android_max") and p["plateforme"] == "android" and p["appareil"].get("android_api", 34) > c["android_max"]: return False
    if c.get("android13") and p["plateforme"] == "android" and p["appareil"].get("android_api", 34) < 33: return False
    return True

def plan():
    rows = {p["id"]: {"versions": {t: "A" for t in TESTS}, "verifs": []} for p in PERSONAS}
    for plat in ("android", "ios"):
        ps = [p for p in PERSONAS if p["plateforme"] == plat]
        items = []
        for code, (titre, vers, c) in TESTS.items():
            for v in vers:
                items.append(("test", code, v, c))
        for cid, titre, quoi, c in CHANTIERS:
            items.append(("chantier", cid, None, c))
        # contraintes fortes d'abord
        items.sort(key=lambda it: -(len(it[3]) + (2 if it[3].get("petit") else 0)))
        for kind, code, v, c in items:
            if c.get("tous"):
                for p in ps: rows[p["id"]]["verifs"].append(code)
                continue
            cands = [p for p in ps if compatible(p, c)]
            if kind == "test":
                cands = [p for p in cands if rows[p["id"]]["versions"][code] == "A" or v == "A"]
                cands = [p for p in cands if not (v == "A" and any(x == code for x in rows[p["id"]]["verifs"]))]
                cands = [p for p in cands if not any(x.startswith(code + ":") for x in rows[p["id"]]["verifs"])]
                if c.get("petit"):
                    pet = [p for p in cands if p.get("petit")]
                    cands = pet or cands
            if not cands:
                sys.exit(f"aucune persona {plat} pour {code} {v or ''}")
            p = min(cands, key=lambda p: (len(rows[p["id"]]["verifs"]), p["id"]))
            r = rows[p["id"]]
            if kind == "test":
                r["versions"][code] = v; r["verifs"].append(f"{code}:{v}")
            else:
                r["verifs"].append(code)
    return rows

def couverture(rows):
    manque = []
    for plat in ("android", "ios"):
        ids = [p["id"] for p in PERSONAS if p["plateforme"] == plat]
        fait = set(itertools.chain.from_iterable(rows[i]["verifs"] for i in ids))
        for code, (_, vers, _) in TESTS.items():
            for v in vers:
                if f"{code}:{v}" not in fait: manque.append(f"{plat} {code}:{v}")
        for cid, *_ in CHANTIERS:
            if cid not in fait: manque.append(f"{plat} {cid}")
    return manque

if __name__ == "__main__":
    rows = plan()
    manque = couverture(rows)
    if manque: sys.exit("couverture incomplète : " + ", ".join(manque))
    nomc = {c[0]: c for c in CHANTIERS}
    out = ["# 1.7 : plan des vérifications par persona", "",
           "Fichier généré par `python3 outils/plan_1_7.py` (ne pas modifier à la main). "
           "Couverture vérifiée : chaque chantier de l'appli et chaque version de chaque test au moins une fois sur Android et une fois sur iPhone/iPad.", ""]
    for p in PERSONAS:
        r = rows[p["id"]]
        imposees = {t: v for t, v in r["versions"].items() if v != "A"}
        out += [f"## {p['id']} ({'Android' if p['plateforme']=='android' else 'iPhone/iPad'}) : {p['appareil']['nom']}",
                f"- Persona : {p['profil']}",
                "- Jardin : " + p['ville'] + " (" + p['zone'] + "). Compte : " + COMPTES[p['compte']] + ".",
                "- Versions imposées avant le lancement : " + (", ".join(f"{t} {v}" for t, v in imposees.items()) or "aucune (toutes en A)") + " ; toutes les autres en A.",
                "- À vérifier :"]
        for x in r["verifs"]:
            if ":" in x:
                t, v = x.split(":"); titre, vers, _ = TESTS[t]
                out.append(f"  - **{t} {v}** · {titre} : {vers[v]}")
            else:
                _, titre, quoi, _ = nomc[x]
                out.append(f"  - **{x}** · {titre} : {quoi}")
        out.append("")
    open("enquetes/VERSION_1_7_PLAN.md", "w", encoding="utf-8").write("\n".join(out))
    json.dump({p["id"]: {"plateforme": p["plateforme"], "compte": p["compte"], "versions": rows[p["id"]]["versions"], "verifs": rows[p["id"]]["verifs"]} for p in PERSONAS},
              open("plan_1_7.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # personas.json : ajoute ou met à jour les 20 personas de la 1.7
    allp = json.load(open("personas.json", encoding="utf-8"))
    ids = {p["id"] for p in PERSONAS}
    allp = [x for x in allp if x["id"] not in ids]
    for p in PERSONAS:
        allp.append({"id": p["id"], "plateforme": p["plateforme"], "version": "1.7",
                     "nom": p["profil"].split(",")[0] + ", " + p["ville"], "profil": p["profil"],
                     "but": "Mission 1.7 : voir enquetes/VERSION_1_7.md et ta section de enquetes/VERSION_1_7_PLAN.md.",
                     "compte": p["compte"], "position": p["pos"], "appareil": p["appareil"]})
    json.dump(allp, open("personas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = {pl: sum(len(rows[p["id"]]["verifs"]) for p in PERSONAS if p["plateforme"] == pl) for pl in ("android", "ios")}
    print("OK", n, {p["id"]: len(rows[p["id"]]["verifs"]) for p in PERSONAS})
