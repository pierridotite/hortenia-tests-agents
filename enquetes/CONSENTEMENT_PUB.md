# Vérification rapide 1.6.5 Android : lancement et fenêtre « Autoriser la mesure des publicités ? »

Même téléphone et mêmes outils que dans CONSIGNES_CLAUDE.md (section Outils et Règles). Ne joue pas de persona :
va au plus court, une vingtaine de gestes au plus, puis écris le rapport.

1. Premier lancement : capture. La fenêtre « Autoriser la mesure des publicités ? » doit s'afficher. Note si elle tient
   à l'écran (texte coupé, bouton hors écran ou sous la barre système) et si les deux boutons ont le même poids.
2. Selon ta persona :
   - sophie, francois, hugo, julie : touche « Autoriser » ;
   - yves, gerard, martine, ines : touche « Refuser » ;
   - amandine, tom : ferme la fenêtre SANS choisir (bouton Retour d'Android), relance l'app
     (`adb shell am force-stop com.hortenia.app` puis la commande de lancement) : la fenêtre doit revenir.
     Choisis alors « Refuser » (amandine) ou « Autoriser » (tom).
3. La fenêtre se ferme et l'accueil s'affiche : touche « Créer mon jardin » et passe les 2 premières étapes de l'onboarding (capture).
4. Relance l'app (force-stop puis lancement) : la fenêtre ne doit PAS revenir (capture).
5. Signale tout plantage (app fermée, écran blanc) : recopie alors les lignes de `resultats/<persona>/NN-logcat.txt` qui
   parlent d'erreur, d'exception, de « ReactNativeJS », de TikTok ou de Facebook, avec leur heure.

Écris `resultats/rapport.md` en 10 lignes au plus : fenêtre vue (oui/non, capture), choix fait, onboarding OK, relance OK,
plantage (oui/non), défauts d'affichage.
