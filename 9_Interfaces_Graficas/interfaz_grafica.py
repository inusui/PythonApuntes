from cgitb import text
from tkinter import *

root = Tk() #Base de todo
root.title("Mi Primera intefaz Grafica con Python") #Nombre de la ventana
root.iconbitmap("recursos/dino.ico") #icono de la ventana
#root.resizable(1,1)

#Funciones
def salir():
    exit()

def selec():
    cadena = ""
    if (opcion.get == 1 or 2 or 3):
        monitor.config( text="Opcion: {}".format( opcion.get() ))

    if(leche.get()):
        cadena += "Con Leche"
    elif(azucar.get()):
        cadena += "Con azucar"
    monitor2.config( text= "{}".format(cadena))

def limpiar():
    opcion.set(None)
    monitor.config(text="")
    leche.set(None)
    azucar.set(None)
#Interfaz Raiz
root.config(bd=10)
root.config(relief="ridge")

opcion = IntVar()

# Radio Button
frame1 = Frame(root)
frame1.config(relief="ridge", bd=10)
frame1.pack(side= "left")
Radiobutton(frame1, text="Opcion 1", variable=opcion, value=1, command=selec).pack()
Radiobutton(frame1, text="Opcion 2", variable=opcion, value=2, command=selec).pack()
Radiobutton(frame1, text="Opcion 3", variable=opcion, value=3, command=selec).pack()

monitor = Label(frame1)
monitor.pack()

Button(frame1, text="Limpiar", command=limpiar).pack()

Button(frame1,text="Salir", command=salir).pack()


#CheckButtons
leche = IntVar()
azucar = IntVar()

frame = Frame(root)
frame.config(relief="ridge", bd=10)
frame.pack(side="right")
imagen = PhotoImage(file="recursos/chems.png")
Label(frame, image=imagen).pack(side="left")

Label(frame, text="Como quieres el cafe?").pack(anchor="w")
Checkbutton(frame, text="Leche", variable=leche, onvalue=1, offvalue=0, command=selec).pack(anchor="w")
Checkbutton(frame, text="Azucar", variable=azucar, onvalue=1, offvalue=0 , command=selec).pack(anchor="w")
monitor2 = Label(frame)
monitor2.pack()


root.mainloop() #Mentiene la ventana abierta
