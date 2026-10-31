# Test complet + fenêtre « Autoriser la mesure des publicités ? » (1.6.5 Android)

Fais la mission complète de CONSIGNES_CLAUDE.md (mêmes outils, mêmes règles, même rapport final), avec ta persona.
En plus, cette version ajoute au premier lancement une fenêtre « Autoriser la mesure des publicités ? » avec deux
boutons, « Refuser » et « Autoriser ». Vérifie ce qui suit et ajoute au rapport une section
« ## Fenêtre de mesure des publicités » (ce que tu as vu, n° de capture, bug ou non).

1. Premier lancement : capture la fenêtre. Note si elle tient à l'écran (texte coupé, bouton hors écran ou sous la
   barre système), si les deux boutons ont le même poids visuel, et si le texte explique clairement le choix.
2. Selon ta persona :
   - sophie, francois, hugo, julie : touche « Autoriser » ;
   - yves, gerard, martine, ines : touche « Refuser » ;
   - amandine, tom : ferme la fenêtre SANS choisir (bouton Retour d'Android), puis relance l'app
     (`adb shell am force-stop com.hortenia.app` puis la commande de lancement) : la fenêtre doit revenir.
     Choisis alors « Refuser » (amandine) ou « Autoriser » (tom).
3. Après le choix : la fenêtre se ferme et l'onboarding continue normalement. Fais ta mission.
4. Une fois ton compte créé, relance l'app (force-stop puis lancement) : la fenêtre ne doit PAS revenir.
5. Profil > « Mesure des publicités » : la ligne affiche-t-elle ton choix ? Touche-la : la fenêtre doit se rouvrir.
   Change ton choix, ferme, et vérifie que la ligne affiche le nouvel état.
6. Signale tout plantage (app fermée, écran blanc), surtout au lancement et juste après « Autoriser » : dans ce cas,
   recopie les lignes de `resultats/<persona>/NN-logcat.txt` qui parlent d'erreur, d'exception, de « ReactNativeJS »,
   de TikTok ou de Facebook, avec leur heure.
