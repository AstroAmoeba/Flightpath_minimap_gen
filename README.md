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
