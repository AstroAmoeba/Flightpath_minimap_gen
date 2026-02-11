### Algoritmo para Extraer Mini-Mapas de Niveles Conectados

Este algoritmo, basado en BFS, permite partir de un nodo de tipo **level** para identificar todos los nodos tipo **level** que están inmediatamente conectados a él o que están conectados exclusivamente a través de nodos tipo **connector**.  
Cuando se alcanza un nodo tipo **level** distinto al inicial, la exploración se detiene y ya no se continúa expandiendo a partir de ese nodo.

**Entradas:**
- Lista de nodos del grafo
- ID del nodo inicial (de tipo 'level')

**Salidas:**
- Lista de nodos level alcanzados (con título/id/camino)
- Subgrafo: nodos y conexiones necesarios para representar los caminos encontrados

Se puede consultar el código (Python) en: [`BFS test/MinimapGenerator.py`](https://github.com/AstroAmoeba/Flightpath_minimap_gen/blob/main/BFS%20test/MinimapGenerator.py)

#### Ejemplo:

Nodo de inicio: Obreras

<img width="779" height="736" alt="image" src="https://github.com/user-attachments/assets/d4a1bbcf-6028-45ce-be9c-9724a9254b89" />

Conexiones:

Directas:

- Colonización (ID 134) -> Camino: [131, 134] 

- Radionovela (ID 136) -> Camino: [131, 136] 

Mediante nodos connector: 

- Feromonas (ID 133) -> Camino: [131, 130, 133]

- Limpiadoras (ID 138) -> Camino: [131, 149, 138]

- Organización (ID 125) -> Camino: [131, 130, 126, 125]

- Forrajera (ID 200) -> Camino: [131, 149, 139, 200]

- Nodriza (ID 202) -> Camino: [131, 149, 139, 201, 202]

- Guardiana (ID 203) -> Camino: [131, 149, 139, 201, 203]

Minimapa:

<img width="489" height="323" alt="image" src="https://github.com/user-attachments/assets/c2126610-cfa5-4d50-ad1d-58351e1d2a27" />

