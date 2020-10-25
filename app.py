# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:44:59 2020

@author: ASUS
"""

import qrcode
from PIL import Image as imagen, ImageTk as imagenTk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

correctionDict = {'L7%': qrcode.constants.ERROR_CORRECT_L, 'M15%': qrcode.constants.ERROR_CORRECT_M, 'Q25%': qrcode.constants.ERROR_CORRECT_Q, 'H30%': qrcode.constants.ERROR_CORRECT_H}
elegirColor = {'Blanco&Negro':['white','black'], 'Blanco&Azul':['white','blue'] , 'Blanco&Rojo':['white','red'], 'Negro&Amarillo':['yellow','black'], 'Amarillo&Azul':['yellow','blue'], 'Amarillo&Rojo':['yellow','red'], 'Blanco&Verde':['white','green'], 'Amarillo&Verde':['yellow','green']}

root= Tk()
root.title('Codificador y decodificador de QR')

#----------------imagen al inicio------------------

miFrame1=Frame(root)
miFrame1.pack()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, #Porcentaje de error L 7%, M 15%, Q 25%, H 30%
    box_size=5, #Se elige el tamaño del array o pixeles por fila y columna
    border=4, #Se elige el tamaño entre el borde de la ventana y el codigo QR generado
)
    
qr.add_data("testing 123@789?") #https://medium.com/@ngwaifoong92
qr.make(fit=True)
    
#img = qr.make_image(fill_color=color1, back_color=color2)
imag = qr.make_image(fill_color="red", back_color="white")
imag.save("qrcode.png")

miImagen= imagen.open("/home/alex/Documents/ws-sts/Bitbucket/qr-app/qrcode.png")
miImagen = miImagen.resize((150,150), imagen.ANTIALIAS)
miFoto = imagenTk.PhotoImage(miImagen)
        
foto = Label(miFrame1, image=miFoto)
foto.grid(row=0, column=0,padx=10,pady=10)
'''
def crearImagenArchivo(nombreArchivoQR):
    miImagen= imagen.open(nombreArchivoQR) #"C:/Users/ASUS/Downloads/qrcode.png"
    miImagen = miImagen.resize((150,150), imagen.ANTIALIAS)
    miFoto = imagenTk.PhotoImage(miImagen)
            
    foto = Label(miFrame1, image=miFoto)
    foto.grid(row=0, column=0,padx=10,pady=10)
    
crearImagenArchivo("C:/Users/ASUS/Downloads/qrcode.png")
'''

#----------------comienzo de funciones------------------
def crearQRConEntradas(nombreArchivoQR, mensaje, capacidadDatos, nivelCorreccion, cambiarColor1, cambiarColor2):
    qr = qrcode.QRCode(
        version=capacidadDatos,
        error_correction=nivelCorreccion, #Porcentaje de error L 7%, M 15%, Q 25%, H 30%
        box_size=5, #Se elige el tamaño del array o pixeles por fila y columna
        border=4, #Se elige el tamaño entre el borde de la ventana y el codigo QR generado
    )
    
    qr.add_data(mensaje) #https://medium.com/@ngwaifoong92
    qr.make(fit=True)
    
    #img = qr.make_image(fill_color=color1, back_color=color2)
    imag = qr.make_image(fill_color=cambiarColor1, back_color=cambiarColor2)
    imag.save(nombreArchivoQR)

'''
def CrearArchivoImagen(nombreArchivoQR):
    print('crear archivo imagen {}', nombreArchivoQR)
    miImagen= imagen.open(nombreArchivoQR + ".png")
    miImagen = miImagen.resize((150,150), imagen.ANTIALIAS)
    miFoto = imagenTk.PhotoImage(miImagen)
    
    foto = Label(miFrame1, image=miFoto)
    foto.grid(row=0, column=0,padx=10,pady=10)
'''
def salirAplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?") devuelve yes or no
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?") #devuelve True or False
    if valor== True:
        root.destroy()
        
def infoAdicional():
    messagebox.showinfo("Taller3", "Codificar y decodificar código QR")

def avisoLicencia():
    messagebox.showwarning("Licencia","producto bajo licencia GNU - Software libre")
   
def verificar(entrada, valor):
    if entrada == "":
        return valor
    else:
        return entrada
        

def crearQR():
    nombreArchivoQR = verificar(NombreArchivo.get(), "qrcode.png")
    mensaje = verificar(mensajeText.get('1.0', END), "testing 123@789?")
    capacidadDatos = verificar(capacidadDatosCombo.get(), "1")
    nivelCorreccion = verificar(nivelCorreccionCombo.get(), "L7%")
    cambiarColor = verificar(cambiarColorCombo.get(), "Blanco&Negro")
    
    crearQRConEntradas(nombreArchivoQR, mensaje, capacidadDatos, correctionDict[nivelCorreccion],elegirColor[cambiarColor][0], elegirColor[cambiarColor][1])
    #CrearArchivoImagen(nombreArchivoQR)
    
    messagebox.showinfo("Registro QR", "Registro insertado con éxito")
    
def cargarArchivoQR():
    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    
    miImagen2= imagen.open("C:/Users/ASUS/Downloads/qrcode.png")
    miImagen2 = miImagen2.resize((150,150), imagen.ANTIALIAS)
    im = imagenTk.PhotoImage(miImagen2)
    #im = img.imread("qrcode.png")
    foto2 = Label(miFrame5, image=im)
    foto2.grid(row=0, column=0,padx=10,pady=10)

    messagebox.showinfo("Registro QR", "Archivo cargado con éxito: " + filename)
    plt.imshow(im)

def leerQR():
    
    imag = imagen.open('qrcode.png')
    result = decode(imag)
    decoded = ''
    for i in result:
        decoded += i.data.decode("utf-8")
    
    textoComentario2.delete(1.0, END)
    textoComentario2.insert(1.0, decoded)


#----------------Valores iniciales------------------


crearQRConEntradas("qrcode", "testing 123@789?", 1, qrcode.constants.ERROR_CORRECT_L,'black','white')
#CrearArchivoImagen("qrcode")


#----------------comienzo barra Menu------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,height=300)

archivoBBDD=Menu(barraMenu, tearoff=0)
archivoBBDD.add_command(label="Salir", command=salirAplicacion)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="File",menu=archivoBBDD)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


#----------------comienzo de campos------------------

miFrame2=Frame()
miFrame2.pack()

NombreArchivo = StringVar()


#----------------columna 2------------------

mensajeText=Text(miFrame2,width=16,height=5)
mensajeText.grid(row=0, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame2, command=mensajeText.yview)
scrollVert.grid(row=0, column=2, sticky="nsew")
mensajeText.config(yscrollcommand=scrollVert.set)

capacidadDatosCombo = ttk.Combobox(miFrame2, width=16)
capacidadDatosCombo.grid(row=1, column=1,padx=10,pady=10)
opciones2 = [i for i in range(1, 41)]
capacidadDatosCombo['values']=opciones2

nivelCorreccionCombo= ttk.Combobox(miFrame2, width=16)
nivelCorreccionCombo.grid(row=2, column=1,padx=10,pady=10)
opciones = ['L7%', 'M15%', 'Q25%', 'H30%']
nivelCorreccionCombo['values']=opciones

cambiarColorCombo= ttk.Combobox(miFrame2, width=16)
cambiarColorCombo.grid(row=3, column=1,padx=10,pady=10)
opciones3 = ['Blanco&Negro', 'Blanco&Azul', 'Blanco&Rojo', 'Negro&Amarillo', 'Amarillo&Azul', 'Amarillo&Rojo', 'Blanco&Verde', 'Amarillo&Verde']
cambiarColorCombo['values']=opciones3

nombreArchivoEntry=Entry(miFrame2, textvariable=NombreArchivo)
nombreArchivoEntry.grid(row=4, column=1,padx=10,pady=10)


#----------------columna 1------------------

comentarioLabel=Label(miFrame2, text="Mensaje: ")
comentarioLabel.grid(row=0, column=0, sticky="e",padx=10,pady=10)

erroresLabel=Label(miFrame2, text="Nivel de correción de errores: ")
erroresLabel.grid(row=2, column=0, sticky="e",padx=10,pady=10)

capacidadLabel=Label(miFrame2, text="Conf capacidad de datos: ")
capacidadLabel.grid(row=1, column=0, sticky="e",padx=10,pady=10)

colorLabel=Label(miFrame2, text="Cambiar colores QR: ")
colorLabel.grid(row=3, column=0, sticky="e",padx=10,pady=10)

idLabel=Label(miFrame2, text="Nombre Archivo: ")
idLabel.grid(row=4, column=0, sticky="e",padx=10,pady=10)


#----------------botones al final------------------

miFrame3=Frame(root)
miFrame3.pack()

botonCreate=Button(miFrame3,text="Codificar", width="10", height="1", command=crearQR)
botonCreate.grid(row=0, column=0, padx=10, pady=10)
botonLoad=Button(miFrame3,text="Cargar archivo QR", width="15", height="1", command=cargarArchivoQR)
botonLoad.grid(row=0, column=1, padx=10, pady=10)
botonDecypher=Button(miFrame3,text="Leer QR", width="10", height="1", command=leerQR)
botonDecypher.grid(row=0, column=2, padx=10, pady=10)


#----------------lectura mensaje------------------

miFrame4=Frame()
miFrame4.pack()

textoComentario2=Text(miFrame4,width=40,height=3)
textoComentario2.grid(row=0, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame4, command=textoComentario2.yview)
scrollVert.grid(row=0, column=2, sticky="nsew")
textoComentario2.config(yscrollcommand=scrollVert.set)


root.mainloop()
