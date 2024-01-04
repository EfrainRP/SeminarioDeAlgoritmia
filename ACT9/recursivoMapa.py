import cv2 as cv
import numpy as np
import math as m

nombreMapa="2"

mapa=cv.imread('mapa'+nombreMapa+'.png') #Se guarda la imagen del mapa

vertices=np.load("verticeMapa"+nombreMapa+".npy") # Cargar la lista de indices definidas
#vertices = np.array([[398, 14],[253,14], [115,14]])

gray = cv.cvtColor(mapa,cv.COLOR_BGR2GRAY) #Pasamos la imagen a escala de grises

#cv.imshow('Mapa',gray) #Muestra la imagen en escala de grises

#obtengo un binarizacion en blaco todos lo pixeles cuyo valor en sea entre 254 y 255
ret,th1 = cv.threshold(gray,254,255,cv.THRESH_BINARY)
#hago un kernel de 11x11 de unos. Los Kernels se acostumbra hacerse d3e tamaño no par y cuadrados
    
"""def blackPoint (start, next,th2):
    #y = start[0]+ ((next[1]-start[1])/(next[0]-start[0]))*(x-start[0])
    xm = int((start[0]+next[0])/2)
    ym = int((start[1]+next[1])/2)
    if np.all(th2[xm, ym] < 150):
        return False
    vertexM=(xm,ym)
    bP(start,vertexM,th2)
    bP(vertexM,next,th2)
    return bP(start, next,th2)

def bP(vertexS, vertexN, th2):
    if vertexS[0] == vertexN[0] and vertexS[1] == vertexN[1]:
        return False
    xm = int((start[0]+next[0])/2)
    ym = int((start[1]+next[1])/2)
    if np.all(th2[xm, ym] < 150):
        return False
     
    return True"""

def blackPoint(start,next,th2):
    xm = int((start[0]+next[0])/2)
    ym = int((start[1]+next[1])/2)
    if np.any(th2[xm, ym] != 255):
        #cv.circle(th2,(ym,xm),2,(200,100,255),-1)
        return False
    #cv.circle(th2,(ym,xm),3,(0,0,255),-1)
    return bP(start,next,th2)

def bP(start,next,th2):
    xm = int((start[0]+next[0])/2)
    ym = int((start[1]+next[1])/2)
    middle = (xm,ym)
    
    if np.any(th2[xm, ym] < 150):
        #cv.circle(th2,(ym,xm),2,(0,0,255),-1)
        return False
    if (start[0]==middle[0] and start[1]==middle[1]) or (next[0]==middle[0] and next[1]==middle[1]):
        return True
    flag = bP(start,middle,th2)
    flag = bP(middle,next,th2)
    return flag

       

kernel = np.ones((11,11), np.uint8) #aplico un filtro de dilatacion. Este filtro hace que los puntos blancos se expandan 

th1 = cv.dilate(th1,kernel,1)#probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado

kernel = np.ones((11,11), np.uint8) 

th1 = cv.erode(th1,kernel,1) #Despues aplico uno de erosion que hace lo opuesto al de dilatacion

th1 = cv.GaussianBlur(th1,(5,5),cv.BORDER_DEFAULT) #aplico un flitro gausiando de 5x5  para suavisar los bordes 

ret,th2 = cv.threshold(th1,235,255,cv.THRESH_BINARY) #binariso la imagen
th2 = cv.dilate(th2,kernel,1)
th2 = cv.cvtColor(th2,cv.COLOR_GRAY2BGR)

CantVer = len(vertices)
listEdge =[] #Lista de aristas CORRECTAS
print (th2.shape)
for i in range(CantVer):
    for j in range(i+1, CantVer):
        start = vertices[i]
        next = vertices[j]

        flag = blackPoint(start,next,th2) #Verfica si algun punto de la recta en un punto negro
        if flag: listEdge.append([start,next]) #Se agrega la arista


for list in listEdge:
    p1=list[0]
    p2=list[1]
    print("Arista: ", list[0],list[1])
    cv.line(th2,(p1[1],p1[0]),(p2[1],p2[0]),(0,255,0),1)

#listEdgeSort = sorted(listEdge, key=lambda x: x[2])

#------------Algoritmo de Prim----------------#
"""vStart = vertices[0]
vertVisited = set


while len(vertVisited) < len(vertices):
    for edge in listEdgeSort:
        edgeO = edge[0]
        if edge[0] in vertVisited and edge[1] not in vertVisited:"""


#################################################################
"""for list in listEdgeSort:
    p1=list[0]
    p2=list[1]
    print("AristaOr: ", list[0],list[1],list[2])"""

for vertice in vertices:
    # Los parametros de la funcion circle son:
    # - imagne donde se van a pintar
    # - coordenada del centro del cisculo (x,y)
    # - radio del circulo
    # - color
    # - grosor de la linea (-1 es para pintar un circulo relleno)
    # Como los vertices vienen en fila columna para pintarlos en la imagen paso sus valores al reves 
    cv.circle(th2,(vertice[1],vertice[0]),3,(255,0,0),-1)
    #print("vertice ",vertice)

cv.imshow('thres2',th2)

cv.waitKey()
# Acuerdense que las funciones de opencv esperan x y
# y las de arreeglos esperan fila columna

"""if edge[0] in visited and edge[1] in visited:
            del listEdgeSort[p]

        if edge[0] in visited:
            visited.add(edge[1])
            primEdge.append((edge[0],edge[1]))
            noVisited.remove(edge[1])
            del listEdgeSort[p]
            break
        
        if edge[1] in visited:
            visited.add(edge[0])
            primEdge.append((edge[1],edge[0]))
            noVisited.remove(edge[0])
            del listEdgeSort[p]
            break"""

