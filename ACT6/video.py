import cv2 as cv
import numpy as np

minBGR = np.array([110, 80, 0])#azul fuerte
maxBGR = np.array([255, 195, 100])#azul claro

cam = cv.VideoCapture(0)
fondo = cv.imread("fondo.jpg")

while True:
  ret, frame = cam.read()#frame sera como nuestra ventana de imagen de nuestra camara

  #Ajustamos los tamaños de las imagenes a uno solo
  fondo=cv.resize(fondo,(1366,768))
  frame=cv.resize(frame,(1366,768))

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
