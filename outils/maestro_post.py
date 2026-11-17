"""Post du banc pour le parcours Maestro des réactions (04-reactions.yaml).

  python3 outils/maestro_post.py creer "<texte>"   un compte de test publie le post
  python3 outils/maestro_post.py supprimer         le même compte le supprime

Compte marqué compteTest : le post reste dans le banc, invisible des vrais
jardiniers. Le jeton de connexion reste dans $RUNNER_TEMP (jamais affiché ni
déposé). Jeton du banc : secret TESTS_JETON."""
import json, os, sys
import requests

BANC = (os.environ.get("TESTS_API") or "https://admin.hortenia.com/tests/banc").rstrip("/")
API = os.environ.get("HORTENIA_API", "https://admin.hortenia.com").rstrip("/")
ETAT = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "maestro_post.json")


def creer(texte):
    r = requests.post(BANC + "/compte-test", json={"type": "email", "persona": "maestro-auteur"},
                      headers={"Authorization": "Bearer " + os.environ["TESTS_JETON"]}, timeout=60)
    r.raise_for_status()
    c = r.json()
    if not c.get("ok"):
        sys.exit(f"compte de test refusé : {c.get('erreur')}")
    l = requests.post(API + "/users/login", json={"email": c["email"], "password": c["mot_de_passe"]}, timeout=60)
    l.raise_for_status()
    h = {"Authorization": "Bearer " + l.json()["token"]}
    p = requests.post(API + "/community/messages", headers=h, data={"message": texte}, timeout=60)
    p.raise_for_status()
    post = p.json()
    d = post.get("data") or post.get("message") or post
    pid = d.get("_id") if isinstance(d, dict) else None
    if not pid:
        sys.exit("identifiant du post introuvable")
    json.dump({"pid": pid, "h": h}, open(ETAT, "w"))
    print(f"post du banc {pid} publié par le compte de test {c['compte']}")


def supprimer():
    try:
        e = json.load(open(ETAT))
    except Exception:
        print("aucun post à supprimer")
        return
    r = requests.delete(f"{API}/community/messages/{e['pid']}", headers=e["h"], timeout=60)
    print(f"post {e['pid']} supprimé : HTTP {r.status_code}")


if __name__ == "__main__":
    creer(sys.argv[2]) if sys.argv[1] == "creer" else supprimer()
