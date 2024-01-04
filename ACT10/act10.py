import networkx as nx
import matplotlib.pyplot as plt

#Se crea el grafo
graph = nx.Graph() #Inicializa el grafo

for i in range(1,11):#Creacion de 10 vertices, del 1 al 10
    graph.add_node(i)

#Creacion de las aristas, 5x5=25 aristas 
for i in range(1,6):
    for j in range(6,11):
        graph.add_edge(j,i,weight=j-i)

"""Configura el posicionamiento de nodos, k y scale ajusta la distancia de 
equilibrio entre los nodos y la escala de la imagen de salida y seed tendra
la misma disposición visual cada vez que se usa"""
pos = nx.spring_layout(graph,k=3,scale=3,seed=21)

plt.figure() #Inicializa una ventana
nx.draw(graph,pos, with_labels=True,width=1) #Dibuja el grafo original, con las etiquetas del vertice
labels = nx.get_edge_attributes(graph,'weight') #Regresa los atributos de weight del grafo
nx.draw_networkx_edge_labels(graph, pos,labels) #Dibujara las etiquetas de las aristas con sus pesos

k = nx.minimum_spanning_tree(graph) #Encuentra el árbol generador mínimo (kruscal)

plt.figure() #Inicializa una ventana
nx.draw(graph,pos, with_labels=True,width=1)#Dibuja el grafo original, con las etiquetas del vertice
nx.draw_networkx_edges(k, pos, edge_color='#FFA500',width=1) #Dibuja las aristas de color naranja del kruscal
nx.draw_networkx_edge_labels(graph,pos,labels) #Dibuja todas las aristas del grafo original con sus etiquetas

plt.show() #Muestra en pantalla los grafos resultantes



