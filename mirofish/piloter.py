"""Pilote une simulation MiroFish de bout en bout par son API.

Usage : python mirofish/piloter.py <dossier du lot> <dossier MiroFish> <dossier de sortie>

Le lot contient hortenia.md et panel.md (documents du graphe), videos.json
(les vidéos à tester) et consigne.md (la demande de simulation). Les vidéos
sont publiées par la page Hortenia comme premiers messages du fil : le
générateur de configuration de MiroFish les réécrirait, on les remplace donc
dans simulation_config.json avant le démarrage. À la fin, chaque jardinier
est interrogé sur les vidéos qui lui donnent envie d'installer l'app.

Tout est écrit dans le dossier de sortie, qui est chiffré ensuite : rien de
ce que produisent les agents ne passe dans le journal public.
"""

import json
import os
import shutil
import sys
import time

import requests

API = os.environ.get("MIROFISH_API", "http://127.0.0.1:5001")
TOURS = int(os.environ.get("TOURS", "6"))
PLATEFORME = "reddit"  # fil avec commentaires, le plus proche de Facebook


def log(msg):
    # Journal public : uniquement des étapes et des compteurs
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def appel(methode, chemin, **kw):
    r = requests.request(methode, API + chemin, timeout=kw.pop("timeout", 120), **kw)
    try:
        corps = r.json()
    except ValueError:
        raise RuntimeError(f"{chemin} : réponse {r.status_code} illisible")
    if not corps.get("success", r.ok):
        raise RuntimeError(f"{chemin} : {str(corps.get('error'))[:300]}")
    return corps.get("data", corps)


def attendre_tache(chemin, corps=None, limite=3 * 3600):
    debut, dernier = time.time(), None
    while time.time() - debut < limite:
        d = appel("POST", chemin, json=corps) if corps else appel("GET", chemin)
        etat, prog = d.get("status"), d.get("progress")
        if (etat, prog) != dernier:
            log(f"  {etat} {prog}")
            dernier = (etat, prog)
        if etat in ("completed", "ready"):
            return d
        if etat == "failed":
            raise RuntimeError(f"tâche en échec : {str(d.get('error') or d.get('message'))[:300]}")
        time.sleep(10)
    raise TimeoutError(chemin)


def ecrire(sortie, nom, donnees):
    with open(os.path.join(sortie, nom), "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)


def texte_video(v):
    return (
        f"[Vidéo {v['id']} · {v['titre']}]\n"
        f"Texte à l'écran : {v['accroche']}\n"
        f"Voix off : {v['voix']}\n"
        f"À l'image : {v['images']}\n"
        f"Lien : hortenia.com/facebook"
    )


def main():
    lot, mirofish, sortie = sys.argv[1:4]
    os.makedirs(sortie, exist_ok=True)
    videos = json.load(open(os.path.join(lot, "videos.json"), encoding="utf-8"))
    consigne = open(os.path.join(lot, "consigne.md"), encoding="utf-8").read()

    for _ in range(60):
        try:
            if requests.get(API + "/health", timeout=5).ok:
                break
        except requests.RequestException:
            pass
        time.sleep(5)
    log("MiroFish prêt")

    # 1. Ontologie puis graphe à partir des documents du lot
    fichiers = [("files", (n, open(os.path.join(lot, n), "rb"), "text/markdown"))
                for n in ("hortenia.md", "panel.md")]
    d = appel("POST", "/api/graph/ontology/generate", files=fichiers, timeout=900,
              data={"simulation_requirement": consigne, "project_name": os.path.basename(lot)})
    projet = d["project_id"]
    log(f"ontologie faite ({len(d.get('ontology', {}).get('entity_types', []))} types)")
    d = appel("POST", "/api/graph/build", json={"project_id": projet}, timeout=300)
    attendre_tache(f"/api/graph/task/{d['task_id']}")
    graphe = appel("GET", f"/api/graph/project/{projet}")["graph_id"]
    log("graphe construit")

    # 2. Simulation : profils et configuration
    d = appel("POST", "/api/simulation/create", json={
        "project_id": projet, "graph_id": graphe,
        "enable_twitter": False, "enable_reddit": True})
    sim = d["simulation_id"]
    d = appel("POST", "/api/simulation/prepare", timeout=900, json={
        "simulation_id": sim, "use_llm_for_profiles": True, "parallel_profile_count": 16})
    if d.get("task_id"):
        attendre_tache("/api/simulation/prepare/status",
                       {"task_id": d["task_id"], "simulation_id": sim})
    dossier_sim = os.path.join(mirofish, "backend", "uploads", "simulations", sim)

    # 3. Les vidéos deviennent les premiers messages, publiés par la page Hortenia
    profils = json.load(open(os.path.join(dossier_sim, "reddit_profiles.json"), encoding="utf-8"))
    page = next((p for p in profils if "hortenia" in
                 f"{p.get('name', '')} {p.get('username', '')}".lower()), profils[0])
    chemin_config = os.path.join(dossier_sim, "simulation_config.json")
    config = json.load(open(chemin_config, encoding="utf-8"))
    config["event_config"]["initial_posts"] = [
        {"content": texte_video(v), "poster_type": "Hortenia",
         "poster_agent_id": page.get("user_id", 0)} for v in videos]
    json.dump(config, open(chemin_config, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    log(f"{len(profils)} agents, {len(videos)} vidéos publiées par l'agent {page.get('user_id', 0)}")

    # 4. Simulation
    appel("POST", "/api/simulation/start", json={
        "simulation_id": sim, "platform": PLATEFORME, "max_rounds": TOURS,
        "enable_graph_memory_update": False, "force": True})
    debut, dernier = time.time(), None
    while True:
        d = appel("GET", f"/api/simulation/{sim}/run-status")
        etat, tour = d.get("runner_status"), d.get("current_round")
        if (etat, tour) != dernier:
            log(f"  {etat} tour {tour}/{d.get('total_rounds')}")
            dernier = (etat, tour)
        if etat in ("completed", "stopped", "failed"):
            break
        if time.time() - debut > 4 * 3600:
            log("  simulation trop longue, arrêt")
            appel("POST", "/api/simulation/stop", json={"simulation_id": sim})
            break
        time.sleep(20)

    # 5. Ce que les agents ont fait
    for nom, chemin in (("posts", f"/api/simulation/{sim}/posts?platform={PLATEFORME}&limit=1000"),
                        ("commentaires", f"/api/simulation/{sim}/comments?limit=5000"),
                        ("actions", f"/api/simulation/{sim}/actions?limit=10000"),
                        ("stats_agents", f"/api/simulation/{sim}/agent-stats")):
        try:
            ecrire(sortie, f"{nom}.json", appel("GET", chemin))
        except Exception as e:
            log(f"  {nom} indisponible : {type(e).__name__}")

    # 6. Entretien final de chaque jardinier
    liste = "\n\n".join(texte_video(v) for v in videos)
    question = (
        "Tu as vu passer ces 10 vidéos de la page Hortenia dans ton fil Facebook :\n\n"
        f"{liste}\n\n"
        "Réponds en français, en restant toi-même. 1) Quelles vidéos t'auraient arrêté "
        "en faisant défiler ton fil (donne les numéros) ? 2) Ton top 3, du meilleur au moins bon, "
        "pour te donner envie d'installer Hortenia, avec pour chacune la raison en une phrase. "
        "3) La vidéo qui t'agace ou te fait fuir, et pourquoi. 4) Aurais-tu cliqué sur le lien "
        "et installé l'app gratuite ? Termine par une ligne exacte au format "
        "TOP3: Vxx, Vxx, Vxx | PIRE: Vxx | INSTALLE: oui/non")
    try:
        d = appel("POST", "/api/simulation/interview/all", timeout=1900, json={
            "simulation_id": sim, "prompt": question, "platform": PLATEFORME, "timeout": 1800})
        ecrire(sortie, "entretiens.json", d)
        log("entretiens faits")
    except Exception as e:
        log(f"entretiens en échec : {type(e).__name__}")

    try:
        appel("POST", "/api/simulation/close-env", json={"simulation_id": sim, "timeout": 30})
    except Exception:
        pass
    # Copie brute (base SQLite du fil, profils, configuration) pour l'analyse
    shutil.copytree(dossier_sim, os.path.join(sortie, "simulation"), dirs_exist_ok=True)
    log("terminé")


if __name__ == "__main__":
    main()
