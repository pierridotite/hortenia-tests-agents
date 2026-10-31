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
