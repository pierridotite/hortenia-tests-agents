# Vérification du SDK TikTok (build de vérification, mode debug)

Même téléphone et mêmes outils que dans CONSIGNES_CLAUDE.md (section Outils et Règles).
Ne joue pas de persona : va au plus court. Pierre regarde en même temps l'écran « Test events » de TikTok.

1. Au premier lancement, la fenêtre « Autoriser la mesure des publicités ? » s'affiche : capture, puis touche « Autoriser ».
2. Attends 30 s sur l'écran suivant (capture), sans rien toucher : c'est le moment où le SDK envoie l'installation et le lancement.
3. Fais l'onboarding jusqu'au bout et crée un compte par e-mail (adresse de CONSIGNES_CLAUDE.md), en notant l'heure (`date`)
   de la fin de l'onboarding et de la création du compte.
4. Attends 60 s sur l'écran Jardin, capture, puis ferme et relance l'app (force-stop puis lancement), attends 30 s.

Écris `resultats/rapport.md` : heure de chaque étape (Autoriser, fin de l'onboarding, compte créé, relance), et recopie les lignes de
`resultats/<persona>/NN-logcat.txt` qui contiennent TikTok, « tiktok », « TTSDK », « business-api » ou une erreur ReactNativeJS,
avec leur heure.
