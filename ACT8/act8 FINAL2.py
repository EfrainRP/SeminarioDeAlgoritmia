import cv2 as cv
#Se carga el clasificador de rostros dada por el maestro
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)

#Se almacena nuestras imagenes (lentes y bigote)
coolGlass = cv.imread("lentes.png",cv.IMREAD_UNCHANGED)
bigote = cv.imread("bigote.png",cv.IMREAD_UNCHANGED)
coolGlass = cv.cvtColor(coolGlass,cv.COLOR_BGR2BGRA)
bigote = cv.cvtColor(bigote,cv.COLOR_BGR2BGRA)

def filtro(f,PNG,PNG2,x,y,face_w,face_h): #Definicion de funcion para colocar los lentes
    PNG = cv.resize(PNG,(face_w,int(face_h//2.5))) #Se ajusta el tamaño de nuestros lentes
    PNG2 = cv.resize(PNG2,(face_w,(face_h//2))) #Se ajusta el tamaño de nuestros lentes

    #Se recorrera la imagen de los lentes para ajustarlo a la cara
    for i in range(PNG.shape[0]): #Recorrera las filas de la matriz de imagen
        for j in range(PNG.shape[1]): #Recorrera las columnas de la matriz de imagen
            if(PNG[i][j][3] != 0):
                f[y+i+(face_h//4), x+j]=PNG[i][j] 

    #Se recorrera la imagen del bigote para ajustarlo a la cara
    for i in range(PNG2.shape[0]): #Recorrera las filas de la matriz de imagen 2
        for j in range(PNG2.shape[1]): #Recorrera las columnas de la matriz de imagen 2
            if(PNG2[i][j][3] != 0): 
                f[y+i+int(2*face_h/4), x+j+int(face_w//22)]=PNG2[i][j]
    return f

#Obtiene acceso a la webcam
video_capture = cv.VideoCapture(2)

if not video_capture.isOpened():#Verifica si no se conecto a la webcam
        print('No se pudo acceder a la camara')
else:
    while True:
        #Revisara si se pudo leer imagenes de la camara
        ret, frame = video_capture.read()
        frame=cv.flip(frame,1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=15,
            minSize=(30, 30)
        )
        #Por cada cara detectada pintara un cuadro
        for (x, y, w, h) in faces:
            frame = cv.cvtColor(frame,cv.COLOR_BGR2BGRA) #Se le agrega otro nivel, el de opacidad
            frame = filtro(frame,coolGlass,bigote,x,y,w,h) #Funcion donde se le agrega las imagenes filtro

        # Mostrar la deteccion
        cv.imshow('Video', frame)

        #Se motraran las caras mientra no presionemos la tecla s
        if cv.waitKey(1) & 0xFF == ord('s'):
            break

    video_capture.release() #Liberara la camara
    cv.destroyAllWindows() #Cerrara todas las ventanas

