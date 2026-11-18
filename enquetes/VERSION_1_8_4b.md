# Mission 1.8.4 refaite (build 116/153) : page Météo, détail des calculatrices, vue 3D

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Ta persona est dans `personas.json` (variable PERSONAS). Le téléphone est déjà réglé dans la langue de ta persona.
Environ 80 gestes, jusqu'à 70 minutes. Une vérification bloquée ne t'arrête pas : note-la et passe.
Aucun achat, même d'essai : la fenêtre du store s'ouvre, tu la fermes. Rien de publié, aucune question à HortenIA,
aucun diagnostic photo, aucun code de parrainage.

## Démarrage
1. Lance l'app et attends l'écran d'accueil. Si ta ligne dit « compte Plus » : tout de suite, avant toute capture,
   `python3 outils/site_tests.py compte plus` (e-mail affiché ; mot de passe tapé par `ecrire.py @mdp-compte`, jamais
   affiché). Si l'outil répond « identifiant d'appareil introuvable », relance l'app et recommence aussitôt.
2. Impose le parcours B de l'accueil avant « Créer mon jardin » : `python3 outils/site_tests.py imposer T43=B`, puis
   relance l'app. Fais l'accueil au plus court, en plaçant le jardin sur la carte (lieu de ta ligne) et en gardant les
   plantes proposées, jusqu'au jardin. Ferme le paywall sans rien acheter.
3. Compte Plus : connecte-toi avec le compte de test (Profil > « J'ai déjà un compte ») et vérifie dans Profil que
   Plus est actif. Compte gratuit : reste invité.
4. Si le jardin n'a qu'une partie, trace-en une seconde si l'appli le propose simplement (sinon passe).

## Ce que tu essaies
La liste du Pôle Produit est dans `enquetes/METEO_CALCULS_1_8_4.md` : lis-la en entier avant de commencer.
Elle donne les deux signaux qui bloquent la sortie (écran crème figé, « Calcul indisponible » ou « Météo
indisponible » avec le réseau, ou un bloc qui manque sans message) : si tu en vois un, capture, note l'écran, le calcul,
la langue et le compte, puis continue.
Codes : M1 à M10 pour la page Météo, K1 à K10 pour le détail des calculatrices, dans l'ordre de la liste.
Regarde d'abord le plus fragile : le clavier sur les champs des calculs (pH mesuré, surface, azote), les libellés de
l'échelle du pH, les courbes de la Météo et le toucher d'un jour, « Ajouter au planning » puis le retour.
Voulu, à ne pas compter comme défaut : les heures de la Météo à l'horloge du téléphone, l'absence des plantes
« À protéger », et trois calculs aux chiffres différents de la 1.8.3 (arrosage, cendre de bois, chaux et soufre).

| Persona | Compte | Lieu | Particularité |
|---|---|---|---|
| sophie | Plus | Draveil | Météo entière (M1 à M10, mode avion pour M8) ; puis K1, K2, K5 |
| lukas | gratuit | Berlin | allemand : K1 à K10 (paywall des résultats), échelle du pH en allemand (K3) ; puis M1, M5, M10 |
| yves | gratuit | Lyon | petit écran, texte x1,3 : K1 à K4, K9 ; M1, M9 |
| lucia | Plus | Madrid | espagnol : K1 à K10 ; M1 à M4, M10 |
| baptiste | Plus | Nantes | d'abord la vue 3D : G1 à G7 de `enquetes/VERIF_3D_GESTE_1_8_4.md` ; puis M3, M4, K2, K5, K8 (bouton retour d'Android) |
| raymond | gratuit | Le Mans | iPhone SE, très gros texte : M1, M2, M9 ; K1 à K3, K9 |
| hanna | Plus | Köln | iPhone SE, allemand, très gros texte : K1 à K10 (clavier !) ; M1 à M4, M9, M10 |
| kevin | Plus | Toulouse | M1 à M10 (12/24 h : M7) ; K2, K5, K6 |
| oliver | gratuit | London | anglais : M1, M5, M7, M10 ; K1, K3, K10 |

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes : un signal bloquant vu ou non, le plus gênant, ton avis sur les deux écrans.
2. Tableau : `| code | verdict (bon / défaut / bloquant / non testable / sans objet) | capture(s) | ce que tu as vu |`
   pour chaque code de ta ligne (et G1 à G7 avec la mesure pour baptiste).
3. Autres bugs vus, du plus grave au moins grave.
