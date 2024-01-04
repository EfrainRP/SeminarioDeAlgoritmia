import cv2 as cv
import numpy as np
'''
imagenOriginal=cv.imread('persona.jpg')
imagenPlaya=cv.imread('fondo.jpg')
cv.imshow('yanet',imagenOriginal)
cv.imshow('playa',imagenPlaya)
cv.waitKey()
minBGR = np.array([30, 150, 30])
maxBGR = np.array([130, 255, 130])

imagenPlaya=cv.resize(imagenPlaya,(640,480))
imagenOriginal=cv.resize(imagenOriginal,(640,480))

maskBGR = cv.inRange(imagenOriginal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara',maskBGR)
cv.imshow('mascara_inv',mask_inv)

resultBGR = cv.bitwise_and(imagenOriginal, imagenOriginal, mask = mask_inv)
result_inv = cv.bitwise_and(imagenPlaya, imagenPlaya, mask = maskBGR)

total=cv.add(resultBGR,result_inv)
cv.imshow('resultado total',total)

cv.imwrite('resultado.jpg',total)
cv.waitKey()
cv.destroyAllWindows()
minBGR = np.array([90, 60, 0])#verde claro
maxBGR = np.array([255, 195, 100])#verde fuerte
([120, 110, 0])

'''
minBGR = np.array([48, 100, 48])#verde claro
maxBGR = np.array([144, 207, 144])#verde fuerte

minBGR = np.array([110, 80, 0])#azul claro
maxBGR = np.array([255, 195, 100])#azul fuerte

cam = cv.VideoCapture(1)
fondo = cv.imread("fondo.jpg")
while True:
  ret, frame = cam.read()#frame sera como nuestra ventana de imagen de nuestra camara

  #Ajustamos los tamaños de las imagenes a uno solo
  fondo=cv.resize(fondo,(900,768))
  frame=cv.resize(frame,(900,768))

  if ret == False: break

  maskBGR = cv.inRange(frame,minBGR,maxBGR)#aplicamos la mascara, cambio los pone en verdadero
  mask_inv = cv.bitwise_not(maskBGR)#lo invertimos la variable anterior

  resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)#Excluimos los colores de la marcara
  result_inv = cv.bitwise_and(fondo, fondo, mask = maskBGR)#Sustituimos los colores detectados para cambiarlos por el fondo

  total=cv.add(resultBGR,result_inv)#Juntamos los resultados para una sola imagen

  cv.imshow('Camara', total)#Mostramos en ventana la imagen resultante
  if cv.waitKey(1) & 0xFF == ord('s'): break #Condicion para salir del bucle infinito, con un delay y si es la tecla s

frame.release()#Cerramos el archivo de video de nuestra camara
cv.destroyAllWindows()#Cerramos todas las ventanas creadas
