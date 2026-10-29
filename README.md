# Hortenia : tests par agents IA

Des agents IA, chacun avec un profil de jardinier, utilisent l'app Hortenia sur
un téléphone virtuel comme le ferait un vrai utilisateur, et notent les bugs,
plantages et blocages qu'ils rencontrent.

- `personas.json` : les profils et leurs buts.
- `agent.py` : la boucle de l'agent (capture d'écran, choix du geste, geste via adb).
- `.github/workflows/android.yml` : émulateur Android, lancé à la main (Actions, « Run workflow »).

Le dépôt ne contient pas le code de l'app : il télécharge le dernier build chez
Expo. Les résultats sont chiffrés avec `cle_publique.pem` avant d'être publiés
comme artefact ; seul le détenteur de la clé privée peut les lire.

Les agents ne paient rien, ne publient rien dans la communauté et s'inscrivent
avec des adresses du simulateur d'e-mails d'Amazon SES (aucun e-mail réel).
