# Mission 1.7 : chaque chantier, chaque version de chaque test

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md
(iPhone/iPad), avec les changements ci-dessous. Ta persona, son jardin, son compte, ses versions imposées et
ta liste de vérifications sont dans **ta section** de `enquetes/VERSION_1_7_PLAN.md` (cherche ton identifiant,
variable PERSONAS). Fais **toutes** les vérifications de ta liste, dans l'ordre qui te paraît le plus naturel
pour ta persona. Compte environ 100 gestes (pas 25).

## Outil du site des tests (nouveau)
`python3 outils/site_tests.py …` parle à l'onglet « Testeurs » de hortenia.com/tests (`python3 outils/site_tests.py aide`).
1. **Tout au début**, avant de toucher l'app : `python3 outils/site_tests.py preparer` (impose tes versions à cet
   appareil), puis relance l'app (Android : `adb shell am force-stop com.hortenia.app` puis la commande de lancement ;
   iOS : `bash outils/ios/geste.sh relancer`). Vérifie avec `site_tests.py etat` que tes versions sont actives (l'appli du banc les reprend au lancement et au retour au premier plan).
2. Une date (hiver, 1er mars, J+7…) : `site_tests.py date AAAA-MM-JJ`, relance l'app, vérifie, puis `site_tests.py date aucune`.
3. Les notifications et messages du serveur (rappels, récap, relance, e-mail, essai…) : `site_tests.py liste` pour
   leurs noms, `site_tests.py apercu <message> [version]` pour le texte, `site_tests.py envoyer <notification>` pour la
   recevoir sur le téléphone (comptes de test seulement). Recopie le texte obtenu dans ton rapport.
4. Les situations à deux comptes ou à préparer (filleul, publication proche, question sans réponse, alerte imposée,
   absence de 10 jours, semaine factice…) : `site_tests.py simuler <action>`.
5. Les événements envoyés par l'app : `site_tests.py evenements`.
6. Compte Plus : `site_tests.py compte plus` donne l'adresse ; écris le mot de passe avec `ecrire.py @mdp-compte`.
   Le mot de passe du site : `ecrire.py @mdp-site`. N'écris jamais un mot de passe ou un jeton en clair dans le rapport.
Si l'outil répond « indisponible » ou une erreur, note-le dans le rapport et continue avec ce que tu peux voir dans l'app.

## Règles qui changent pour la 1.7
- Personas invitées : ne crée jamais de compte. Personas « e-mail » : compte par e-mail après l'onboarding
  (règles de CONSIGNES). Personas Plus : compte de l'outil, ne paie jamais rien.
- Toujours rien de publié pour de vrai dans la Communauté : ouvre la publication préremplie, vérifie, puis annule.
  « J'aime » est permis seulement si ta liste le demande (T29). Les réactions rapides : ouvrir le choix, fermer sans réagir.
  Un code ou un lien de parrainage (R9-parrainage) s'écrit dans un brouillon et ne part jamais.
- Au plus 3 diagnostics photo (galerie : feuille de tomate, et les photos de jardin si présentes) et 3 questions à HortenIA.
- Ce que le banc ne peut pas faire (achat, widget, agenda, QR code…) : note « non testable sur le banc » avec la raison.
  Sur le simulateur iPhone, des prix en dollars ne sont pas un bug.

## Règle de Pierre : rien qui fasse IA
Sur **chaque écran** que tu vois, relève ce qui fait encore IA, capture à l'appui. C'est un **défaut** à part entière :
- étincelle (petit symbole à quatre branches), baguette magique, robot ;
- icône générique prise telle quelle dans une banque d'icônes pour ce qui est propre à Hortenia (les flèches, la croix
  et les chevrons du téléphone sont normaux) ;
- emoji dans l'app, dégradé décoratif ;
- textes du genre « Découvrez », « personnalisé », « intelligent », « notre IA experte », « Assistant IA » ;
- image qui se voit générée par une IA.
Exceptions, voulues par Pierre : la mention « réponse générée par IA » sous les réponses d'HortenIA, les 8 réactions
rapides en emojis sous les publications, et les icônes des outils et des onglets (celles d'avant, gardées le 9/11).

## Retours de Pierre du 9/11
Les codes R9-… de ta liste viennent des derniers retours de Pierre (clavier, Communauté, gel réservé à Plus, agenda,
widget, annuel sans essai, Aménager « Taille et forme »). Regarde-les avec autant de soin que le reste : c'est ce que
Pierre n'a encore vu qu'en maquette.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 5 lignes.
2. **Tableau des vérifications** : une ligne par élément de ta liste, dans l'ordre de la liste :
   `| code | verdict (bon / défaut / bloquant / non testable) | appareil | capture(s) | ce que tu as vu |`.
   Bloquant = plantage, écran blanc, impossible d'avancer, perte du jardin ou du compte, mauvais prix, achat possible par erreur.
3. **Ce qui fait IA** : un tableau `| écran | élément | capture |`. « Rien vu » si c'est le cas, avec les écrans parcourus.
4. Autres bugs vus en chemin, du plus grave au moins grave (format de CONSIGNES).
5. **Meilleure capture** de chaque vérification marquée « bon » : son numéro et une phrase (elles serviront à la présentation).
6. Impressions de la persona, à la première personne (format de CONSIGNES).
Distingue ce que tu as vu de ce que tu supposes.
