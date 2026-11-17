# Hortenia : tests par agents IA

Des agents IA, chacun avec un profil de jardinier, utilisent l'app Hortenia sur
un téléphone virtuel comme le ferait un vrai utilisateur, et notent les bugs,
plantages et blocages qu'ils rencontrent.

- `personas.json` : les profils et leurs buts.
- `CONSIGNES_CLAUDE.md` : la mission donnée à Claude Code (outils, règles, rapport attendu).
- `outils/ecran.py`, `outils/ecrire.py` : voir l'écran et écrire, pour Claude.
- `.github/workflows/android-claude.yml` : un émulateur Android par persona, en parallèle, piloté par Claude Code (abonnement Claude de Pierre).
- `.github/workflows/ios-claude.yml` : un simulateur iPhone ou iPad par persona (5 Mac à la fois), consignes `CONSIGNES_CLAUDE_IOS.md`, outils `outils/ios/` (AXe).
- `.github/workflows/android-build.yml` : build Android de l'app sur les machines Linux gratuites de ce dépôt (aab déposé chez Expo pour les tests, envoi en test interne Google Play).
- `.github/workflows/ios-build.yml` : build iOS de l'app sur les Mac gratuits de ce dépôt (simulateur pour les tests, ipa pour TestFlight). Le code de l'app est lu avec un jeton en lecture seule (secret `APP_REPO_TOKEN`) et n'est jamais affiché ; les journaux de build sont chiffrés.

Chaque version de l'app passe par ces testeurs avant sa sortie, et tous les builds iOS et Android de l'app se font ici (décisions de Pierre, 29/10/2026).

Le dépôt ne contient pas le code de l'app : il télécharge le dernier build chez
Expo. Les résultats sont chiffrés avec `cle_publique.pem` avant d'être publiés
comme artefact ; seul le détenteur de la clé privée peut les lire.

Les agents ne paient rien, ne publient rien dans la communauté et s'inscrivent
avec des adresses du simulateur d'e-mails d'Amazon SES (aucun e-mail réel).

## Relevé des écrans des apps concurrentes

Workflow `concurrents.yml` (lancement manuel) : un émulateur Android par app de
`concurrents.json`, en parallèle. L'APK public est récupéré sur le miroir
APKPure avec [apkeep](https://github.com/EFForg/apkeep) (sans compte Google),
puis Claude Code parcourt l'app comme une nouvelle utilisatrice, **sans achat**
(compte e-mail jetable mail.tm seulement si l'app l'exige, accord de Pierre du 31/10), et capture chaque écran (onboarding, paywall, essai, écrans clés)
selon `CONSIGNES_CONCURRENTS.md`. Hortenia est relevée dans les mêmes
conditions comme référence. Les résultats sont chiffrés comme ceux des tests.

## Parcours Maestro rejoués à chaque build (sans modèle, gratuit)

Cinq parcours dans `maestro/` : création du jardin (avec tracé de 4 coins), inscription
par e-mail, paywall sans achat, réactions de la Communauté, écran Calculer. Chacun repart
d'un téléphone neuf (`maestro/sous/arrivee.yaml`, onboarding jusqu'à l'accueil).

- Lancer : workflow « Maestro - parcours rejoués » avec `build_android=gh:<run>` et/ou
  `build_ios=gh:<run>` (builds du banc), `parcours` vide pour les cinq ou p. ex. `04-reactions`.
- Durée : environ 13 min par plateforme. Verdict de chaque parcours dans le résumé du run ;
  captures, journal et hiérarchies d'écran chiffrés (artefact `resultats-chiffres-maestro-*`).
- Le post des réactions est créé par un compte de test au début (`outils/maestro_post.py`) et
  supprimé à la fin ; l'adresse d'inscription est `success+maestro-<plateforme>-<run>@simulator.amazonses.com`
  et le mot de passe est tiré au hasard à chaque passage.
- Écrire un sélecteur : `"(.*[,.] )?(Texte)([,.] .*)?"`. L'iPhone fusionne les libellés
  (« Jardin, icône », « Mon sol. Trois tests… ») ; l'appli met une espace insécable avant
  « ? », « : » et « ! » : mettre `.` à la place de cette espace.

## agent-device (option des testeurs IA)

Entrée `appareil=agent-device` de android-claude et ios-claude : le testeur pilote l'appareil
par l'arbre d'accessibilité (CONSIGNES_AGENT_DEVICE.md) au lieu des captures et coordonnées.
Essai du 17/11 sur la mission 1.8.1b : mêmes constats qu'en classique ; Android 200 tours et
2,9 $ (classique : 108 tours, 1,4 $), iPhone 145 tours et 1,3 $ en 12 min (classique : 108 tours,
1,4 $, 19 min). L'appli n'a ni testID ni libellés sur la plupart des boutons : l'outil retombe
souvent sur les coordonnées. Valeur par défaut : classique.
