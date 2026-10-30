# Enquête : écran blanc après la localisation (étape 3/4 de l'onboarding)

Même téléphone et mêmes outils que dans CONSIGNES_CLAUDE.md (section Outils et Règles).
Ne joue pas de persona : va au plus court, une quinzaine de gestes.

1. Commence la création du jardin (« Créer mon jardin »), réponds vite aux 2 premières étapes.
2. À l'étape 3/4 « Où est votre jardin ? », capture, puis touche « Position approximative ».
3. Accepte la localisation (« Pendant l'utilisation de l'appli »), puis capture toutes les 5 s pendant 30 s.
4. Si l'écran est blanc : touche le centre, fais Retour, capture.
5. Relance l'app (`adb shell am force-stop com.hortenia.app` puis la commande de lancement), reviens à l'étape 3/4
   et touche cette fois « Position précise », puis capture toutes les 5 s pendant 30 s.

Écris `resultats/rapport.md` : ce qui s'affiche à chaque étape (n° de capture), et recopie les lignes des fichiers
`resultats/<persona>/NN-logcat.txt` qui parlent d'erreur, d'exception, de « ReactNativeJS », de « hortenia » ou de
location, autour du moment où l'écran devient blanc (garde l'heure de chaque ligne).
