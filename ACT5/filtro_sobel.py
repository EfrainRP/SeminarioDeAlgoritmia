import cv2 as cv
import numpy as np
#leer imagen en el mismo directorio que el archivo de python
imagenOriginal=cv.imread('mando.jpg')
#leer archivo en otro directorio el parametro cero al final es para especificar que sera en escala de grises
imagenEnGris=cv.imread('mando.jpg',2)#El 0 nos indicara en que sera en escala de grises

cv.imshow('Original',imagenOriginal)#Muestra la imagen original
cv.imshow('Imagenen en gris',imagenEnGris)#Muestra la imagen en gris sin filtro
cv.waitKey()#Espera la presion de una tecla antes de continuar

filas, columnas = np.shape(imagenEnGris)#Declaramos las filas y columnas de la imagen en gris
filSobel = np.zeros((filas,columnas))#Creamos una "imagen", matriz con puros ceros para llenarlo del filtro

#Matices para el filtro Sobel de 3x3, tanto en vertical como en horizontal
matrizX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
matrizY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

#Procesado del filtro(se ouede con 7 if, con gaus con 3 if)
for fila in range(0,filas-2):
    for columna in range(0,columnas-2):
        vertical = sum(sum(matrizX*imagenEnGris[fila:fila+3, columna:columna+3]))
        horizontal = sum(sum(matrizY*imagenEnGris[fila:fila+3, columna:columna+3]))
        filSobel[fila+1,columna+1] = np.sqrt(vertical**2 + horizontal**2)

        if filSobel[fila,columna] < 1:#Si el pixel es menor al umbral de grises
            filSobel[fila,columna] = 0 #Se le asigna el negro

cv.imshow('Sobel',filSobel)#Muestra la imagen con el filtro aplicado
cv.waitKey()#Espera la presion de una tecla antes de continuar