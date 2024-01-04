from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 545)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)#Boton para separar palabras
        self.pushButton.setGeometry(QtCore.QRect(380, 30, 95, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.separar_p)#Funcion para separar las palabras utilizando el boton

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)#Cuadro de salida
        self.tableWidget.setGeometry(QtCore.QRect(40, 270, 761, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)#Agrega una columna a la tabla
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Palabras'])#Agrega un nombre a la columna de la tabla

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)#Cuadro de texto
        self.textEdit.setGeometry(QtCore.QRect(40, 40, 250, 200))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)#Segundo cuadro de texto 
        self.textEdit_2.setGeometry(QtCore.QRect(550, 40, 250, 200))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)#Letrero de seleccion de fuente
        self.label.setGeometry(QtCore.QRect(370, 70, 111, 20))
        self.label.setObjectName("label")

        self.comboFontBox = QtWidgets.QFontComboBox(self.centralwidget)#Multi cuadro para seleccionar fuente de letras
        self.comboFontBox.currentFontChanged.connect(self.cambiar_f)#Funcion para cambiar la fuente de texto
        self.comboFontBox.setGeometry(QtCore.QRect(340, 90, 161, 21))
        self.comboFontBox.setObjectName("comboFontBox")

        self.radioButtonG = QtWidgets.QRadioButton(self.centralwidget)#Opcion de color verde
        self.radioButtonG.setGeometry(QtCore.QRect(380, 150, 82, 17))
        self.radioButtonG.setObjectName("radioButton")
        self.radioButtonG.clicked.connect(self.cambiar_c)#Funcion para cambiar el color del texto

        self.radioButtonR = QtWidgets.QRadioButton(self.centralwidget)#Opcion de color rojo
        self.radioButtonR.setGeometry(QtCore.QRect(380, 180, 82, 17))
        self.radioButtonR.setObjectName("radioButton_2")
        self.radioButtonR.clicked.connect(self.cambiar_c)#Funcion para cambiar el color del texto

        self.radioButtonN = QtWidgets.QRadioButton(self.centralwidget)#Opcion de color negro
        self.radioButtonN.setGeometry(QtCore.QRect(380, 210, 82, 17))
        self.radioButtonN.setObjectName("radioButton_3")
        self.radioButtonN.clicked.connect(self.cambiar_c)#Funcion para cambiar el color del texto

        self.label_2 = QtWidgets.QLabel(self.centralwidget)#Letrero de seleccion de color de las letras
        self.label_2.setGeometry(QtCore.QRect(380, 130, 101, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interfaz PyQt"))
        self.pushButton.setText(_translate("MainWindow", "Separar palabras"))
        self.label.setText(_translate("MainWindow", "Seleccione fuente:"))
        self.radioButtonG.setText(_translate("MainWindow", "Verde"))
        self.radioButtonR.setText(_translate("MainWindow", "Rojo"))
        self.radioButtonN.setText(_translate("MainWindow", "Negro"))
        self.label_2.setText(_translate("MainWindow", "Seleccione color:"))

    def separar_p(self): #Funcion para separar las letras
        text = self.textEdit.toPlainText()#Obtiene el texto del cuadro original
        self.textEdit_2.setPlainText(text)#Se copia el texto del cuadro original al otro cuadro
        texto_spliteado=text.split()#Separa las palabras en una lista segun el delimitador preteminado
        for r in range(len(texto_spliteado),self.tableWidget.rowCount()):#Comenzara del final del texto hasta la primera fila de la tabla
            self.tableWidget.removeRow(len(texto_spliteado))#Elimina las filas que sobran
        for r in range(len(texto_spliteado)):
            rowAct=self.tableWidget.rowCount()#Obtenemos el numero de la fila actual
            if rowAct <= r:
                self.tableWidget.insertRow(rowAct)#Se inserta uan fila en el cuadro de texto
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(texto_spliteado[r]))#Se agrega nuestro palabra de la lista ya separada
            else:
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(texto_spliteado[r]))#Se agrega nuestro palabra de la lista ya separada

    def cambiar_f(self):#Funcion para cambiar la fuente del texto
        indice = self.comboFontBox.currentIndex()#Obtenemos el indice de la fuante seleccionada del multicuadro
        f_select = QtGui.QFont(self.comboFontBox.itemText(indice),11)#Obtenemos la fuante para almacenarlo como variable del paquete PYQT
        #Se le aplica la fuente seleccionada a nuestros elementos
        self.textEdit.setFont(f_select)
        self.textEdit_2.setFont(f_select)
        self.tableWidget.setFont(f_select)

    def cambiar_c(self): #Funcion para cambiar el color del texto
        if self.radioButtonG.isChecked():#Si el radio button verde, se le aplica el color
            color='color: green'
        elif self.radioButtonR.isChecked():#Si el radio button rojo, se le aplica el color
            color='color: red'
        elif self.radioButtonN.isChecked():#Si el radio button negro, se le aplica el color
            color='color: black'
        #Sel aplica el color seleccionado a nuestros elementos
        self.textEdit.setStyleSheet(color)
        self.textEdit_2.setStyleSheet(color)
        self.tableWidget.setStyleSheet(color)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
