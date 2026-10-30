"""Relais compatible OpenAI (/v1/chat/completions) qui fait répondre Claude Code.

MiroFish et OASIS parlent le format OpenAI, y compris les appels de fonctions
des agents. Chaque requête devient un `claude -p` sans outils, sur l'abonnement
de Pierre (CLAUDE_CODE_OAUTH_TOKEN). Le journal ne contient que des compteurs,
jamais le texte des requêtes ni des réponses.

Variables : RELAIS_MODELE (défaut claude-sonnet-5-5), RELAIS_PARALLELE (8),
RELAIS_PORT (8787).
"""
import json
import os
import re
import subprocess
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MODELE = os.environ.get("RELAIS_MODELE", "claude-sonnet-5-5")
PARALLELE = threading.Semaphore(int(os.environ.get("RELAIS_PARALLELE", "8")))
PORT = int(os.environ.get("RELAIS_PORT", "8787"))
STATS = {"requetes": 0, "outils": 0, "echecs": 0, "secondes": 0.0}
VERROU = threading.Lock()

CONSIGNE_JSON = "\n\nRéponds uniquement par un objet JSON valide, sans texte autour ni bloc de code."


def texte(contenu):
    if isinstance(contenu, str):
        return contenu
    if isinstance(contenu, list):
        return "\n".join(p.get("text", "") for p in contenu if isinstance(p, dict))
    return "" if contenu is None else str(contenu)


def transcrire(messages):
    """Sépare les consignes système et met le reste de la conversation à plat."""
    systeme, tours = [], []
    for m in messages:
        role = m.get("role")
        if role in ("system", "developer"):
            systeme.append(texte(m.get("content")))
        elif role == "user":
            tours.append(f"[Utilisateur]\n{texte(m.get('content'))}")
        elif role == "assistant":
            bloc = texte(m.get("content"))
            for appel in m.get("tool_calls") or []:
                f = appel.get("function", {})
                bloc += f"\n(appel de fonction {f.get('name')} avec {f.get('arguments')})"
            tours.append(f"[Toi, plus tôt]\n{bloc.strip()}")
        elif role == "tool":
            tours.append(f"[Résultat de fonction]\n{texte(m.get('content'))}")
    return "\n\n".join(systeme), "\n\n".join(tours)


def consigne_outils(outils, choix):
    defs = [o.get("function", o) for o in outils]
    lignes = [
        "\n\nTu peux appeler les fonctions suivantes (schémas JSON) :",
        json.dumps(defs, ensure_ascii=False),
        'Réponds uniquement par un objet JSON de la forme {"content": "texte ou null", '
        '"tool_calls": [{"name": "nom_de_fonction", "arguments": {...}}]}, sans texte autour.',
        "Mets une liste vide dans tool_calls si tu n'appelles aucune fonction.",
    ]
    if choix == "required":
        lignes.append("Tu dois appeler au moins une fonction.")
    elif isinstance(choix, dict):
        lignes.append(f"Tu dois appeler la fonction {choix.get('function', {}).get('name')}.")
    return "\n".join(lignes)


def extraire_json(brut):
    brut = brut.strip()
    brut = re.sub(r"^```(?:json)?\s*", "", brut, flags=re.I)
    brut = re.sub(r"\s*```$", "", brut)
    try:
        return json.loads(brut)
    except json.JSONDecodeError:
        debut, fin = brut.find("{"), brut.rfind("}")
        if debut >= 0 and fin > debut:
            return json.loads(brut[debut:fin + 1])
        raise


def claude(systeme, prompt):
    cmd = [
        "claude", "-p", "--model", MODELE, "--output-format", "json",
        "--tools", "", "--max-turns", "1", "--no-session-persistence",
        "--strict-mcp-config", "--disable-slash-commands",
        "--system-prompt", systeme or "Tu es un assistant utile.",
    ]
    for essai in range(4):
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=600)
        try:
            sortie = json.loads(r.stdout)
            if not sortie.get("is_error") and sortie.get("result") is not None:
                return sortie["result"]
        except json.JSONDecodeError:
            pass
        time.sleep(10 * (essai + 1) ** 2)
    raise RuntimeError(f"claude -p a échoué (code {r.returncode})")


def repondre(corps):
    systeme, prompt = transcrire(corps.get("messages", []))
    outils = corps.get("tools") or []
    choix = corps.get("tool_choice")
    if outils and choix != "none":
        systeme += consigne_outils(outils, choix)
    elif (corps.get("response_format") or {}).get("type") in ("json_object", "json_schema"):
        systeme += CONSIGNE_JSON

    with PARALLELE:
        debut = time.time()
        brut = claude(systeme, prompt)
        duree = time.time() - debut

    message = {"role": "assistant", "content": brut}
    fin = "stop"
    if outils and choix != "none":
        try:
            donnees = extraire_json(brut)
            appels = [
                {"id": f"call_{uuid.uuid4().hex[:12]}", "type": "function",
                 "function": {"name": a.get("name"),
                              "arguments": json.dumps(a.get("arguments") or {}, ensure_ascii=False)}}
                for a in donnees.get("tool_calls") or [] if a.get("name")
            ]
            message["content"] = donnees.get("content")
            if appels:
                message["tool_calls"] = appels
                fin = "tool_calls"
        except (json.JSONDecodeError, AttributeError):
            pass
    with VERROU:
        STATS["requetes"] += 1
        STATS["outils"] += fin == "tool_calls"
        STATS["secondes"] += duree
        if STATS["requetes"] % 25 == 0:
            print(f"relais : {STATS['requetes']} réponses, {STATS['outils']} avec fonctions, "
                  f"{STATS['echecs']} échecs, {STATS['secondes'] / STATS['requetes']:.1f} s en moyenne", flush=True)
    return {
        "id": f"chatcmpl-{uuid.uuid4().hex[:16]}", "object": "chat.completion",
        "created": int(time.time()), "model": corps.get("model") or MODELE,
        "choices": [{"index": 0, "message": message, "finish_reason": fin}],
        "usage": {"prompt_tokens": len(prompt) // 4, "completion_tokens": len(brut) // 4,
                  "total_tokens": (len(prompt) + len(brut)) // 4},
    }


class Relais(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def envoyer(self, code, donnees):
        corps = json.dumps(donnees, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            self.envoyer(200, {"object": "list", "data": [{"id": MODELE, "object": "model"}]})
        else:
            self.envoyer(200, {"ok": True, **STATS})

    def do_POST(self):
        if not self.path.rstrip("/").endswith("/chat/completions"):
            self.envoyer(404, {"error": {"message": "route inconnue"}})
            return
        corps = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        try:
            self.envoyer(200, repondre(corps))
        except Exception as e:
            with VERROU:
                STATS["echecs"] += 1
            self.envoyer(500, {"error": {"message": type(e).__name__, "type": "server_error"}})


if __name__ == "__main__":
    print(f"relais Claude ({MODELE}) sur le port {PORT}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), Relais).serve_forever()
