#!/usr/bin/env bash
# Gestes sur le simulateur iOS (positions en points, lues sur ecran.py).
# Usage :
#   geste.sh toucher X Y          un appui
#   geste.sh appui-long X Y       appui de 1 s
#   geste.sh glisser X1 Y1 X2 Y2  glissement (faire défiler : du bas vers le haut)
#   geste.sh defiler bas|haut     défilement d'un écran
#   geste.sh retour               glissement depuis le bord gauche (retour iOS)
#   geste.sh clavier-entree       touche Entrée du clavier
#   geste.sh accueil              bouton principal (l'app passe en arrière-plan)
#   geste.sh ouvrir               relance l'app au premier plan
set -euo pipefail
: "${UDID:?UDID manquant}"
# Taille de l'écran en points (pour défiler et revenir en arrière)
taille() {
  read -r L H < <(python3 -c "import json,subprocess
a=json.loads(subprocess.run(['axe','describe-ui','--udid','$UDID'],capture_output=True,text=True).stdout or '[]')
a=a[0] if isinstance(a,list) and a else a
f=a.get('frame',{}) if isinstance(a,dict) else {}
print(int(f.get('width',390)),int(f.get('height',844)))" 2>/dev/null || echo "390 844")
}
case "${1:-}" in
  toucher) axe tap -x "$2" -y "$3" --udid "$UDID" ;;
  appui-long) axe touch -x "$2" -y "$3" --down --up --delay 1 --udid "$UDID" ;;
  glisser) axe swipe --start-x "$2" --start-y "$3" --end-x "$4" --end-y "$5" --duration 0.5 --udid "$UDID" ;;
  defiler)
    taille; x=$((L / 2))
    if [ "${2:-bas}" = bas ]; then axe swipe --start-x $x --start-y $((H * 3 / 4)) --end-x $x --end-y $((H / 4)) --duration 0.5 --udid "$UDID"
    else axe swipe --start-x $x --start-y $((H / 4)) --end-x $x --end-y $((H * 3 / 4)) --duration 0.5 --udid "$UDID"; fi ;;
  retour) taille; axe swipe --start-x 2 --start-y $((H / 2)) --end-x $((L * 2 / 3)) --end-y $((H / 2)) --duration 0.4 --udid "$UDID" ;;
  clavier-entree) axe key 40 --udid "$UDID" ;;
  accueil) axe button home --udid "$UDID" ;;
  ouvrir) xcrun simctl launch "$UDID" com.hortenia.app >/dev/null ;;
  *) echo "geste inconnu : ${1:-}"; exit 2 ;;
esac
sleep 1
echo "fait : $*"
