import cv2 as cv
import numpy as np
#leer imagen en el mismo directorio que el archivo de python
imagenOriginal=cv.imread('mando.jpg')
#leer archivo en otro directorio el parametro cero al final es para especificar que sera en escala de grises
imagenEnGris=cv.imread('mando.jpg',0)#El 0 nos indicara en que sera en escala de grises
cv.imshow('Original',imagenOriginal)#Muestra la imagen original
cv.imshow('Imagenen en gris',imagenEnGris)#Muestra la imagen en gris sin filtro
cv.waitKey()#Espera la presion de una tecla antes de continuar

filas, columnas = np.shape(imagenEnGris)#Declaramos las filas y columnas de la imagen en gris
filSobel = imagenEnGris.copy()#Creamos la copia de la imagen en gris
#Matices para el filtro Sobel de 3x3,
matrizX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) #tanto en vertical

#matrizY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) #como en horizontal

#Procesado del filtro
for fila in range(1,filas-1):
    for columna in range(1,columnas-1):
        suma=0#Inicializamos en 0 nuestra variables como para la suma del centro de Kernel y
        i=0     #de la fila de la matriz de Sobel
        for filaK in range(fila-1,fila+2):
            j=0#Inicializamos el contador de las columnas de la matriz de Sobel
            for colK in range(columna-1,columna+2):
                suma+=(imagenEnGris[filaK][colK]*matrizX[i][j])#Aparte de la suma de cada coordenada se le aplico la multiplicacion
                j+=1                                            #segun la coordenada de Sobel
            i+=1
        
        filSobel[fila][columna]=abs(suma) #Evitamos los numeros negativos de las operaciones dadas

cv.imshow('Sobel',filSobel)#Muestra la imagen con el filtro aplicado
cv.waitKey()#Espera la presion de una tecla antes de continuar



