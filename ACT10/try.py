"""import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()
G.add_edges_from([(1, 2, {'weight': 4}),
                  (1, 3, {'weight': 1}),
                  (1, 4, {'weight': 3}),
                  (2, 3, {'weight': 2}),
                  (2, 4, {'weight': 5}),
                  (3, 4, {'weight': 6}),
                  (3, 5, {'weight': 1}),
                  (4, 5, {'weight': 5}),
                  (4, 6, {'weight': 3}),
                  (5, 6, {'weight': 2})])

# Calcular el árbol de expansión mínimo de Kruskal
kruskal_edges = nx.minimum_spanning_edges(G, algorithm='kruskal', data=True)

# Convertir el generador en una lista de aristas
kruskal_edges_list = list(kruskal_edges)

# Dibujar el grafo con el recorrido de Kruskal resaltado
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=kruskal_edges_list, edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Mostrar el grafo
plt.show()"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo
graph = nx.Graph()

# Agregamos los nodos
graph.add_nodes_from(range(1,11))

# Agregamos las aristas con pesos aleatorios
for i in range(1,6):
    for j in range(6,11):
        graph.add_edge(i, j, weight=i+j)

# Aplicamos el algoritmo de Prim
T = nx.minimum_spanning_tree(graph)

# Obtenemos la lista de aristas del árbol de expansión mínima
edges = T.edges()

# Obtenemos la lista de pesos de las aristas del árbol de expansión mínima
weights = [T[u][v]['weight'] for u, v in edges]

# Dibujamos el grafo con las aristas del árbol de expansión mínima en rojo
pos = nx.spring_layout(graph, seed=42)
nx.draw(graph, pos=pos, with_labels=True)
nx.draw_networkx_edges(T, pos=pos, edgelist=edges, edge_color='r', width=2)
nx.draw_networkx_edge_labels(T, pos=pos, edge_labels=nx.get_edge_attributes(T,'weight'), font_size=10)

# Mostramos el grafo
plt.show()


