"""Vérification des réactions de la Communauté (1.8.1) contre le serveur en ligne,
avec deux comptes de test (marqués compteTest : leurs posts restent dans le banc,
invisibles des vrais jardiniers, et leurs notifications ne vont qu'aux comptes de test).

  A publie un post, B réagit : PUT /reaction {"reaction":"pousse"}, puis {"reaction":null},
  puis deux fois l'ancien PUT /like. Les réponses du serveur sont affichées, sans jeton.
  GARDER=1 laisse le post en place (pour les testeurs), sinon A le supprime.
Jeton : secret TESTS_JETON. Aucun mot de passe ni jeton n'est affiché."""
import json, os, sys
import requests

BANC = (os.environ.get("TESTS_API") or "https://admin.hortenia.com/tests/banc").rstrip("/")
API = os.environ.get("HORTENIA_API", "https://admin.hortenia.com").rstrip("/")
JETON = os.environ["TESTS_JETON"]
GARDER = os.environ.get("GARDER") == "1"
TEXTE = os.environ.get("TEXTE") or "Banc 1.8.1 : post de test pour les réactions."


def montrer(titre, r):
    try:
        corps = r.json()
    except Exception:
        corps = r.text[:500]
    if isinstance(corps, dict):
        for k in ("token", "jeton", "mot_de_passe", "password"):
            corps.pop(k, None)
    print(f"\n## {titre}\nHTTP {r.status_code}\n" + json.dumps(corps, ensure_ascii=False, indent=1)[:3000])
    return corps


def compte(nom):
    r = requests.post(BANC + "/compte-test", json={"type": "email", "persona": nom},
                      headers={"Authorization": "Bearer " + JETON}, timeout=60)
    r.raise_for_status()
    c = r.json()
    if not c.get("ok"):
        sys.exit(f"compte de test refusé : {c.get('erreur')}")
    l = requests.post(API + "/users/login", json={"email": c["email"], "password": c["mot_de_passe"]}, timeout=60)
    if l.status_code != 200:
        sys.exit(f"connexion du compte {nom} : HTTP {l.status_code} {l.text[:200]}")
    print(f"compte {nom} : {c['compte']}")
    return c["compte"], {"Authorization": "Bearer " + l.json()["token"]}


ida, a = compte("reactions-auteur")
idb, b = compte("reactions-lecteur")

p = requests.post(API + "/community/messages", headers=a, data={"message": TEXTE}, timeout=60)
post = montrer("A publie un post", p)
pid = (post.get("data") or post.get("message") or post) if isinstance(post, dict) else None
pid = pid.get("_id") if isinstance(pid, dict) else None
if not pid:
    sys.exit("identifiant du post introuvable dans la réponse")
print(f"post {pid}")

base = f"{API}/community/messages/{pid}"
montrer("B : PUT /reaction {\"reaction\":\"pousse\"}", requests.put(base + "/reaction", headers=b, json={"reaction": "pousse"}, timeout=60))
montrer("B : PUT /reaction {\"reaction\":null}", requests.put(base + "/reaction", headers=b, json={"reaction": None}, timeout=60))
montrer("B : PUT /like (1re fois)", requests.put(base + "/like", headers=b, timeout=60))
montrer("B : PUT /like (2e fois)", requests.put(base + "/like", headers=b, timeout=60))
montrer("B relit le post", requests.get(base, headers=b, timeout=60))
montrer("Un visiteur sans compte cherche le post (doit être absent ou refusé)", requests.get(base, timeout=60))

if GARDER:
    print(f"\npost gardé pour les testeurs : {pid}")
else:
    montrer("A supprime le post", requests.delete(base, headers=a, timeout=60))
