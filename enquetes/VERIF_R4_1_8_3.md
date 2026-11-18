# Contrôle court 1.8.3 (build 114/151) : réactions sous un commentaire

Même téléphone, mêmes outils et mêmes règles que CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone).
Mission courte : environ 40 gestes, 30 minutes au plus. Ne touche à rien d'autre que ce qui est demandé.

## Démarrage
- Lance l'app et fais l'onboarding au plus court (aucune version à imposer), jusqu'au jardin. Ferme le paywall sans
  rien acheter.
- Va dans Communauté. Le post du banc s'appelle « Banc 1.8.3 : post de test pour les réactions. » (fais défiler, tire
  vers le bas pour rafraîchir si besoin). Ouvre ses commentaires : il y a « Banc 1.8.1 : commentaire de test. » et sa
  réponse. Tu ne réagis QUE sur ce post et sur ces commentaires, jamais ailleurs.

## Vérifications (un verdict par ligne, captures à chaque étape)
- **K1 Invité** : SANS compte, touche le cœur sous le commentaire : l'appli propose de créer un compte (ou de se
  connecter), sans planter et sans poser de réaction. Ferme cette proposition.
- Crée ensuite un compte par e-mail (règles de CONSIGNES pour les personas « email » : Profil > Sauvegarder mon jardin >
  Avec un e-mail), puis reviens aux commentaires du post du banc.
- **K2 Toucher** : avec le compte, un toucher sur le cœur du commentaire pose ❤️ (cœur rouge) et le nombre augmente de 1.
- **K3 Appui long** : appui long sur ce bouton : le choix des six réactions s'ouvre ; choisis « Ça pousse » (🌱) : le
  bouton ne montre plus que 🌱, le nombre ne change pas.
- **K4 Retrait** : un toucher sur le bouton retire ta réaction : cœur en contour, nombre revenu à sa valeur d'avant.
- **K5 Serveur** : remets une réaction (🌱 par appui long), quitte les commentaires, rafraîchis le fil (ou ferme et
  rouvre l'app), rouvre les commentaires : ta 🌱 est toujours là. Puis retire-la d'un toucher, rafraîchis encore : plus
  de réaction de ta part.
- **K6 Réponse** : même chose, en plus court (toucher, puis retrait), sur la réponse au commentaire.
- **K7 Lecture d'écran** (arbre d'accessibilité) : le bouton du commentaire dit la réaction et le nombre de façon
  compréhensible, et ne dit plus « J'aime, 1 » une fois revenu à zéro.

À la fin, aucune réaction de ta part ne reste. Rien de publié, aucun commentaire écrit, aucun achat.

## Rapport (`resultats/rapport.md`, en français)
1. Résumé en 3 lignes.
2. Tableau `| code | verdict (bon / défaut / bloquant / non testable) | capture(s) | ce que tu as vu |` pour K1 à K7.
3. Autres bugs vus. Distingue ce que tu as vu de ce que tu supposes.
