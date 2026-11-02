# Mission 1.6.6 : test complet + nouveautés

Fais la mission complète de CONSIGNES_CLAUDE.md (Android) ou CONSIGNES_CLAUDE_IOS.md (iPhone/iPad) :
mêmes outils, mêmes règles, même rapport. Joue ta persona. En plus, vérifie les nouveautés ci-dessous
et donne-leur une section « Nouveautés 1.6.6 » dans le rapport (une ligne par point : OK / problème / pas vu, avec n° de capture).

## Ton parcours de compte
- Personas SANS COMPTE (invité) jusqu'à la fin : sophie, ines, amandine, julie, martine, chloe, emma, antoine, simone, mehdi.
  Choisis l'entrée sans compte dès qu'elle est proposée et ne crée jamais de compte.
- Toutes les autres : crée un compte par e-mail au moment où l'app le propose (règles de CONSIGNES), après l'onboarding.

## Nouveautés à vérifier
1. Entrée sans compte : l'app se lance et on peut créer un jardin sans compte. Le jardin et les plantes restent après une relance
   (Android : `adb shell am force-stop com.hortenia.app` puis relance ; iOS : `bash outils/ios/geste.sh relancer`).
2. Carte « Gardez votre jardin » (invités) : où et quand elle apparaît, si on peut la fermer, si elle revient trop souvent.
3. Communauté sans compte : on peut LIRE les publications ; publier, aimer ou commenter demande un compte, avec un message clair.
   Ne publie rien, même avec un compte.
4. Onboarding en 3 écrans (et non plus 4) puis écran de première réussite : compte les écrans, note le texte de l'écran de réussite
   et compare-le au planning réel (ouvre le planning ensuite : les gestes annoncés y sont-ils ?).
5. Paywall : il affiche des avis et un nombre de potagers. Lisibles, pas coupés, chiffres plausibles ? Ferme-le sans payer.
6. Carte d'essai Plus (jour X sur 7, 3 suggestions, repliable en glissant sur la fiche Mon potager) : elle n'apparaît que pendant
   un essai. Tu ne peux PAS lancer d'essai (aucun achat) : note « pas vu, essai requis » sauf si elle s'affiche quand même.
7. Offre 14 jours à J+2 : non testable en un jour, ne change pas la date du téléphone. Note seulement si elle apparaît.
8. Mode hors ligne (Android seulement, personas hugo, gerard, tom, francois) : une fois le jardin créé,
   `adb shell svc wifi disable` et `adb shell svc data disable`, attends 5 s, navigue (Jardin, fiche Mon potager, planning) :
   une pastille hors ligne doit apparaître au-dessus de la fiche, et rien ne doit planter ni tourner sans fin.
   Puis `adb shell svc wifi enable` et `adb shell svc data enable` : la pastille doit disparaître.
9. Demande d'avis : si une demande d'avis s'affiche, capture-la et ferme-la sans noter. Dis à quel moment elle est venue.
10. Photo du pommier : si le pommier apparaît (suggestions de plantes, recherche « pommier »), dis si la photo montre bien un pommier.

Classe les bugs du plus grave au moins grave : les BLOQUANTS d'abord (plantage, écran blanc, impossible d'avancer, perte du jardin).
