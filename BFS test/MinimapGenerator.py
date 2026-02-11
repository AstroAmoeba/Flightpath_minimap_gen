import json
import re

def find_immediate_levels(master_data, start_id):
    nodes = master_data["worlds"][0]["nodes"]
    nodes_by_id = {n["id"]: n for n in nodes}
    results = []
    # Para reconstruir el submapa
    all_path_node_ids = set()
    all_path_edges = set()
    # Cola contiene tuplas: (nodo_actual, camino_hasta_aqui)
    queue = [(start_id, [start_id])]
    visited_paths = set()  # Para evitar loops por caminos
    while queue:
        curr_id, path = queue.pop(0)
        curr_node = nodes_by_id.get(curr_id)
        if not curr_node:
            continue
        # Si llegamos a un nodo tipo 'level' (no el inicial), lo anotamos y NO lo exploramos más allá
        if curr_node["type"] == "level" and curr_id != start_id:
            results.append({"id": curr_id, "title": curr_node["title"], "path": path.copy()})
            all_path_node_ids.update(path)
            for i in range(len(path)-1):
                all_path_edges.add((path[i], path[i+1]))
            continue  # no expandimos más allá de un "level"

        # Expandimos solo desde connectors o desde el node inicial
        for dir, target_id in (curr_node.get("connections") or {}).items():
            if target_id not in path:  # Evita loops
                queue.append((target_id, path + [target_id]))

    # Construye el mini mapa sólo con los nodos y edges que aparecen en los caminos
    mini_nodes = [nodes_by_id[nid] for nid in all_path_node_ids]
    mini_edges = [{"from": f, "to": t} for (f, t) in all_path_edges]
    return {
        "connected_levels": results,   # Lista de nodos nivel conectados y su camino
        "minimap": {
            "nodes": mini_nodes,
            "edges": mini_edges
        }
    }

# ---- Ejemplo de uso ----
with open("BFS test/mapa.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

# Nodo de inicio (Obreras en tu ejemplo: id 131)
start_id = 147
info = find_immediate_levels(master_data, start_id)

# Nombre del nodo
start_node = next((n for n in master_data["worlds"][0]["nodes"] if n["id"] == start_id), None)
start_name = start_node["title"] if start_node and start_node["title"] else str(start_id)
safe_name = re.sub(r'[^\w\d-]+', '_', start_name)
filename = f"BFS test/minimap_{safe_name}.json"

# Exporta solo el mini-mapa (con nodos y edges alcanzados según tus reglas)
with open(filename, "w", encoding="utf-8") as f_out:
    json.dump(info["minimap"], f_out, indent=2, ensure_ascii=False)
print(f"Mini-mapa exportado a {filename}")

# Imprime la lista de niveles conectados directamente, cada uno con el camino para llegar:
for lvl in info["connected_levels"]:
    print(f"Nivel: {lvl['title']} (ID {lvl['id']}) -> Camino: {lvl['path']}")