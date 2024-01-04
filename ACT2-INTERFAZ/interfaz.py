from tkinter import *
import re
'''NO PONER INTRO, CONCLU, SOLO CAPTURAS'''

class aplication():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x500')
        self.root.resizable(width=True,height=True)
        self.root.title('Expresiones Regulares')
        label = Label(self.root,text='Validacion de expresiones regulares', font=("Arial Black",12))
        label.pack(side=TOP)

        self.text = Frame(self.root)
        self.text.pack(side=TOP)

        self.bc = Frame(self.root)
        self.bc.pack(ipadx=10, ipady=10)

        self.bt = Frame(self.root)
        self.bt.pack(ipadx=20, ipady=10)

        self.left = Frame(self.root)
        self.left.place(x=60, y=305)

        self.Ans = Frame(self.root)
        self.Ans.place(x=250, y=350)

        self.frameDown = Frame(self.root)
        self.frameDown.pack(side=BOTTOM)
        
        self.text0 = Label(self.text,text='Verificador de palabras')
        self.text0.grid(row=0,column=0)
        self.text1 = Label(self.text,text='Editor de textos', font=("Arial Black",12))
        self.text1.grid(row=1,column=1)
    

        self.t1 = Entry(self.text,width=40)
        self.t1.grid(row=0,column=1,padx=10,pady=10)
        self.t2 = Entry(self.text,width=20)
        self.t2.grid(row=2,column=1,padx=10,pady=10)

        self.b1 = Button(self.text,text='Validar',command=lambda:self.validar(1))
        self.b1.grid(row=0,column=2,padx=10,pady=10)

        self.b2 = Button(self.text,text='Analizar',command=lambda:self.analizar(1))
        self.b2.grid(row=2,column=2,padx=10,pady=10)
        self.b3 = Button(self.Ans,text='Convertir',command=lambda:self.convertir(1))
        self.b3.grid(row=0,column=2,padx=10,pady=10)

        self.l1 = Label(self.text,text='...')
        self.l1.grid(row=0,column=3)
        self.l2 = Label(self.text,text='...')
        self.l2.grid(row=2,column=3)
        self.l3 = Label(self.Ans,text='( )')
        self.l3.config(bg="white")
        self.l3.grid(row=0,column=1,ipadx=10,ipady=10)
        
        self.T = Label(self.bc,text='Color de letra:', font=("Arial",11))
        self.T.grid(row=0,ipadx=5,ipady=5)
        self.selection = IntVar()
        self.rb1 = Radiobutton(self.bc, text='Rojo',variable=self.selection, value=1)
        self.rb1.grid(row=1,column=0,padx=10,pady=5)
        self.rb2 = Radiobutton(self.bc, text='Azul',variable=self.selection, value=2)
        self.rb2.grid(row=1,column=1,padx=10,pady=5)
        self.rb3 = Radiobutton(self.bc, text='Morado',variable=self.selection, value=3)
        self.rb3.grid(row=1,column=2,padx=10,pady=5)
        self.rb4 = Radiobutton(self.bc, text='Verde',variable=self.selection, value=4)
        self.rb4.grid(row=1,column=3,padx=10,pady=5)
        self.rb5 = Radiobutton(self.bc, text='Naranja',variable=self.selection, value=5)
        self.rb5.grid(row=1,column=4,padx=10,pady=5)
        self.rb6 = Radiobutton(self.bc, text='Amarillo',variable=self.selection, value=6)
        self.rb6.grid(row=1,column=5,padx=10,pady=5)
        
        self.T1 = Label(self.bt,text='Fuente de letra:', font=("Arial",11))
        self.T1.grid(row=0,ipadx=5)

        self.selection1 = IntVar()
        self.rb7 = Radiobutton(self.bt, text='Times New Roman',variable=self.selection1, value=1)
        self.rb7.grid(row=4,column=0,padx=10,pady=5)
        self.rb8 = Radiobutton(self.bt, text='Arial',variable=self.selection1, value=2)
        self.rb8.grid(row=4,column=1,padx=10,pady=5)
        self.rb9 = Radiobutton(self.bt, text='Georgia',variable=self.selection1, value=3)
        self.rb9.grid(row=4,column=2,padx=10,pady=5)
        self.rb10 = Radiobutton(self.bt, text='Courier',variable=self.selection1, value=4)
        self.rb10.grid(row=4,column=3,padx=10,pady=5)
        self.rb11 = Radiobutton(self.bt, text='Agency FB',variable=self.selection1, value=5)
        self.rb11.grid(row=4,column=4,padx=10,pady=5)
        self.rb12 = Radiobutton(self.bt, text='Verdana',variable=self.selection1, value=6)
        self.rb12.grid(row=4,column=5,padx=10,pady=5)

        self.font_style = Listbox(self.left, selectmode=SINGLE, width=10)
        self.font_style.grid(row=1, column=2, padx=10,pady=10)
        font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
        for size in font_sizes:
	        self.font_style.insert('end', size)

        self.bsalir = Button(self.frameDown,text='Salir',command=self.root.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar = Button(self.frameDown,text='Limpiar',command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        self.root.mainloop()
        
    def limpiar(self):
        self.t1.delete(first=0,last='end')
        self.l1.config(fg='black',text='...')
        self.t2.delete(first=0,last='end')
        self.l2.config(fg='black',text='...')
        self.l3.config(fg='black',text='( )')
        
    def validar(self,numero):
        if(numero == 1):
            textvalidar = self.t1.get()
            x = re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",textvalidar)
            if (x):
                self.l1.config(fg="green",text='IPv4 valida')
            else:
                self.l1.config(fg="red",text='IPv4 invalida') 

    def analizar(self,numero):
        if(numero==1):
            textContar = self.t2.get()
            x = len(textContar)
            if x==0:
                self.l2.config(fg="red", text=str(x) + " letras")
            else:
                self.l2.config(fg="green", text=str(x) + " letras")

    def convertir(self,numero):
        if(numero==1):
            textIn = self.t2.get()
            if textIn == "":
                self.l3.config(text="( )")
            else: 
                self.Color()
                self.Font()
                self.l3.config(text=textIn)
    
    def Color(self):
        x=self.selection.get()
        if x==1:
            self.l3.config(fg="red")
        elif x==2:
            self.l3.config(fg="blue")
        elif x==3:
            self.l3.config(fg="purple")
        elif x==4:
            self.l3.config(fg="green")
        elif x==5:
            self.l3.config(fg="orange")
        elif x==6:
            self.l3.config(fg="yellow")
    
    def Font(self):
        x=self.selection1.get()
        f=self.font_style.get(self.font_style.curselection())

        if x==1:
            self.l3.config(font=("Times New Roman",f))
        elif x==2:
            self.l3.config(font=("Arial",f))
        elif x==3:
            self.l3.config(font=("Georgia",f))
        elif x==4:
            self.l3.config(font=("Courier",f))
        elif x==5:
            self.l3.config(font=("Agency FB",f))
        elif x==6:
            self.l3.config(font=("Verdana",f))
        else:
            self.l3.config(font=("Arial",f))


app=aplication()
