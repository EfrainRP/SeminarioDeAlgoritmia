import cv2 as cv
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)

#Obtiene acceso a la webcam
video_capture = cv.VideoCapture(0,cv.CAP_DSHOW)

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
            minNeighbors=5,
            minSize=(30, 30)
        )
        #Por cada cara detectada pintara un cuadro
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 250, 0), 5)
        # Mostrar la deteccion
        cv.imshow('Video', frame)
        #Se motraran las caras mientra no presionemos la tecla s
        if cv.waitKey(1) & 0xFF == ord('s'):
            break
    #Liberara la camara
    video_capture.release()
    #Cerrara todas las ventanas
    cv.destroyAllWindows()

