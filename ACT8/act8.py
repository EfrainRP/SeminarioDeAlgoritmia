import cv2 as cv
#Se carga el clasificador de rostros dada por el maestro
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)

#Se almacena nuestras imagenes (lentes y bigote)
coolGlass = cv.imread("coolGlasses.png",cv.IMREAD_UNCHANGED)
bigote = cv.imread("bigote.png",cv.IMREAD_UNCHANGED)

def coolGlasses(f,PNG,x,y,face_w,face_h): #Definicion de funcion para colocar los lentes
    glass_w = face_w + 1            #ancho
    glass_h = int(0.49*face_h) + 1  #Se calcula la altura de la cara para colocar la imagen

    PNG = cv.resize(PNG,(glass_w,glass_h)) #Se ajusta el tamaño de nuestros lentes

    #Se recorrera la imagen de los lentes para ajustarlo a la cara
    for i in range(glass_h):
        for j in range(glass_w):
            for p in range(3):
                if(PNG[i][j][p] < 235):
                    f[y+i-int(-0.20*face_h)][x+j][p]=PNG[i][j][p]  
    return f

def Bigote(f,PNG,x,y,face_w,face_h): #Definicion de funcion para colocar el bigote
    big_w = face_w + 1    #ancho
    big_h = int(0.29*face_h) + 1 #Se calcula la altura de la cara para colocar la imagen

    PNG = cv.resize(PNG,(big_w,big_h)) #Se ajusta el tamaño de nuestros lentes

    #Se recorrera la imagen del bigote para ajustarlo a la cara
    for i in range(big_h):
        for j in range(big_w):
            for p in range(3):
                if(PNG[i][j][p] < 235):
                    f[y+i-int(-0.6*face_h)][x+j][p]=PNG[i][j][p]  
    return f

#Obtiene acceso a la webcam
video_capture = cv.VideoCapture(0)

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
            minNeighbors=7,
            minSize=(30, 30)
        )
        #Por cada cara detectada pintara un cuadro
        for (x, y, w, h) in faces:
            #cv.rectangle(frame, (x, y), (x+w, y+h), (0, 250, 0), 5)
            frame = coolGlasses(frame,coolGlass,x,y,w,h)
            frame = Bigote(frame,bigote,x,y,w,h)

        # Mostrar la deteccion
        cv.imshow('Video', frame)

        #Se motraran las caras mientra no presionemos la tecla s
        if cv.waitKey(1) & 0xFF == ord('s'):
            break
    #Liberara la camara
    video_capture.release()
    #Cerrara todas las ventanas
    cv.destroyAllWindows()

