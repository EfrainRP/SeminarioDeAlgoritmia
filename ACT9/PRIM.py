import cv2 as cv
import numpy as np
import math as m

nombreMapa="1"

mapa=cv.imread('mapa'+nombreMapa+'.png') #Se guarda la imagen del mapa

vertex=np.load("verticeMapa"+nombreMapa+".npy") # Cargar la lista de indices definidas
#vertices = np.array([[398, 14],[253,14], [115,14]])
gray = cv.cvtColor(mapa,cv.COLOR_BGR2GRAY) #Pasamos la imagen a escala de grises
png = cv.cvtColor(mapa,cv.COLOR_BGR2BGRA) #Pasamos la imagen a escala de grises

#cv.imshow('Mapa',gray) #Muestra la imagen en escala de grises

#obtengo un binarizacion en blaco todos lo pixeles cuyo valor en sea entre 254 y 255
ret,th1 = cv.threshold(gray,254,255,cv.THRESH_BINARY)
#hago un kernel de 11x11 de unos. Los Kernels se acostumbra hacerse d3e tamaño no par y cuadrados

"""Funcion que se basa en el algoritmo de Bresenham, en donde se movera en el mapa por incrementos 
proporcionales al eje mas grande de ambas coordenadas, en forma de triangula para recorrer la linea
recta, hacia el pixel mas cercano triangularmente"""
def blackPoint (start, next,th2): 
    #Se saca la direccion de la recta, siendo tambien la distancia segun sus ejes
    dx = (next[0] - start[0])
    dy = (next[1] - start[1])

    #Se decide la distancia mas larga de los ejes X y Y
    D_max = max(abs(dx),abs(dy))
    #max() obtendra el valor maximo de los argumentos que tenga dentro
    
    """Se calcula el incremento por cada paso, segun la distancia mas larga, siendo uno con un 
    incremento de 1, ya que se movera como en un triangulo dentro de la grafica de pixeles"""
    x_inc = dx/D_max
    y_inc = dy/D_max

    x,y=start #Inicializa las coordenas que se recorrera
    #Recorrera toda la recta de acuerdo al eje mas largo, con un rango de 0 hasta el eje mas largo
    for i in range(D_max): 
        if np.all(th2[round(x),round(y)]!=255): #Verifica el pixel de la coordenada en todos los canales que no sea negro
            return False
        #Pueden valores flotantes pero se usan solo enteros para la verificacion
        x = x + x_inc #Incremento proporcional de las x
        y = y + y_inc #Incremento proporcional de las y
    
    return True

kernel = np.ones((11,11), np.uint8) #aplico un filtro de dilatacion. Este filtro hace que los puntos blancos se expandan 
th1 = cv.dilate(th1,kernel,1)#probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado
kernel = np.ones((11,11), np.uint8) 
th1 = cv.erode(th1,kernel,1) #Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv.GaussianBlur(th1,(5,5),cv.BORDER_DEFAULT) #aplico un flitro gausiando de 5x5  para suavisar los bordes 
ret,th2 = cv.threshold(th1,235,255,cv.THRESH_BINARY) #binariso la imagen
th2 = cv.dilate(th2,kernel,1)
th2 = cv.cvtColor(th2,cv.COLOR_GRAY2BGR)

countVertex = len(vertex) #Longitud del arreglo de todos los vertices
listEdge = [] #Lista de aristas CORRECTAS
PosVertex= set() #Coleccion sin repeticion de vertices que estan conectadas, basicamente guarda el indice del arreglo vertex
for i in range(countVertex):
    for j in range(i+1, countVertex):
        start = vertex[i]
        next = vertex[j]
 
        if blackPoint(start,next,th2): #Verfica si algun punto de la recta es un punto negro
            d = m.sqrt((next[0]-start[0])**2 + (next[1]-start[1])**2) #Calcula la distancia entre los 2 puntos en el mapa
            listEdge.append((i,j,d)) #Numero del vertice 1, Numero del vertice 2 en el arreglo de vertices y su respectivo peso
            PosVertex.update([i,j]) #Agrega a la lista de coleccion el indice de los arr de vertices que se conectan sin repetirse

#--------------------------Algoritmo Prim------------------------------#
listEdgeSort = sorted(listEdge, key=lambda cost: cost[2])#Regresa una lista ordenada de tuplas segun el costo
#print("Arista: ", listEdgeSort)

# Lista de vértices visitados
visited = set([PosVertex.pop()]) #Iniciado con el primer elemento de vertices, el POP elimina y devuelve el primer elemento del set pasandolo como una lista de conjunto
primEdge=[] # Inicializa la lista de aristas de Prim, cada elemento sera una tupla
#weight = 0 #Varible para el peso del grafo final
while len(visited) < countVertex: #Siempre y cuando la cantidad de elementos de visitados sea menor a la cantidad de vertices total
    for p, edge in enumerate(listEdgeSort): #edge es un indice del arreglo de vertices
        if edge[0] in visited and edge[1] not in visited: #Verfica si el num del vertice 0 este en visitado y del vertice 1 este en no visitados
            visited.add(edge[1]) #Agrega el nuevo vertice sin visitar                   
            primEdge.append((edge[0],edge[1])) #Agrega la arista para el recorrido Prim
  #          weight = weight + edge[2]
            break
        elif edge[1] in visited and edge[0] not in visited: #Verfica si el num del vertice 1 este en visitado y del vertice 0 este en no visitados
            visited.add(edge[0]) #Agrega el nuevo vertice sin visitar                   
            primEdge.append((edge[0],edge[1])) #Agrega la arista para el recorrido Prim
 #           weight = weight + edge[2]
            break
#print(listEdgeSort)
#print(weight)
#-------------------------------------------------------------------------#
"""for list in listEdgeSort:
    p1=list[0]
    p2=list[1]
    cv.line(th2,(vertex[p1][1],vertex[p1][0]),(vertex[p2][1],vertex[p2][0]),(0,0,255),1)
"""

for list in primEdge:
    p1=list[0]
    p2=list[1]
    cv.line(th2,(vertex[p1][1],vertex[p1][0]),(vertex[p2][1],vertex[p2][0]),(0,0,255),1)
    cv.line(png,(vertex[p1][1],vertex[p1][0]),(vertex[p2][1],vertex[p2][0]),(0,255,0),2)

for vertice in vertex:
    cv.circle(th2,(vertice[1],vertice[0]),3,(255,0,0),-1)
    cv.circle(png,(vertice[1],vertice[0]),3,(255,0,0),-1)


#Muestra la imagen resultante
cv.imshow('thres2',th2)
cv.imshow('Full',png)
cv.waitKey()


