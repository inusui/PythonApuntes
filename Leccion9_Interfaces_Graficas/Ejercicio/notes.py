from tkinter import *
from tkinter import filedialog
from io import open

ruta = "" #almacenar la ruta de un fichero

root = Tk()
root.title("Editor de Texto")
root.iconbitmap("recursos/note.ico")

#Funciones del Fichero
def nuevo ():
    global ruta #Para asignar una variable que esta fuera de la clase. 
    mensaje.set("Nuevo Archivo")
    ruta = ""
    texto.delete(1.0, "end")#Borrar desde el 1 hasta el final no es desde el 0 para mantener el salto de linea que es el primer caracter

def abrir ():
    global ruta
    mensaje.set("Abrir Archivo")
    ruta = filedialog.askopenfilename(initialdir='.', 
    filetypes=(("Ficheros de Texto","*.txt"),
    ), title="Abrir Fichero de Texto")
    
    if ruta != None:
        file = open(ruta,"r")
        contenido = file.read()
        texto.delete(1.0,"end")
        texto.insert('insert', contenido)
        file.close()
        mensaje.set(ruta+" - Editor de Texto")

def guardar ():
    mensaje.set("Guardar Archivo")
    if ruta != "":
        contenido = texto.get(1.0, 'end')#desde el caracter 1
        file = open(ruta, "w+")
        file.write(contenido)
        file.close()
        mensaje.set("El fichero se a guardado correctamente - Editor de Texto")


def guardarComo ():
    mensaje.set("Guardar Como Archivo")
    fichero = filedialog.asksaveasfile(title="Guardar Archivo", mode="a+", defaultextension="txt")
    #Equivalente a open('ruta', 'w')
    if fichero is not None:
        fichero.write(texto.get(1.0, 'end-1c') )
        fichero.close()

#Menu bar
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como",command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)

menubar.add_cascade(label="Archivo", menu=filemenu) 

#Caja de Texto
texto = Text(root)
texto.pack(fill=BOTH, expand=1)
texto.config(padx=6, pady=4, bd=5, font=("Consolas",12))




#************************* Footer y botones para Guardar
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
footer = Label(root, textvar=mensaje, justify="right")
footer.pack(side="left")
Label(root, text="By: Inusui", justify="right").pack(side="right")
imagen = PhotoImage(file="recursos/dog.png")
Label(root, image=imagen, justify="right").pack(side="right")

root.mainloop()