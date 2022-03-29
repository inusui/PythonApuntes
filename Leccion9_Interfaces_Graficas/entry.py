from tkinter import *

root = Tk()

root.title("Entry")
root.iconbitmap("recursos/dino.ico")


#Nombre
nombre = Label(root, text="Nombre:")
nombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)

inputNombre = Entry(root)
inputNombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")
inputNombre.config(justify="right", state="normal")

#Apellido
apellido = Label(root, text="Contraseña:")
apellido.grid(row=1, column=0, sticky="w", padx=5, pady=5)

inputApellido = Entry(root)
inputApellido.grid(row=1, column=1, padx=5, pady=5, sticky="w")
inputApellido.config(justify="right", show="*")#contenido distintos

# Campo Texto
textComentario = Label(root, text="Comentario:")
textComentario.grid(row=2, column = 0, padx=5, pady = 5)

textoLargo = Text(root)
textoLargo.grid(row=2, column = 1, padx=5, pady = 5)
textoLargo.config(width=30,height=10, font=("Consolas",15), padx=5, pady=5) #Tamaño de la cuadricula, altura x ancho

# Botones
def cerrar():
    print("saliendo")
    exit()

inputBoton = Button(root, text="Cerrar Aplicacion", command=cerrar) #en el command solo va el nombre
inputBoton.grid(row=1, column=1, padx=20)

def crear():
    Label(root, text="Creada con un boton").grid()

inputBoton = Button(root, text="Crear", command=crear) #en el command solo va el nombre
inputBoton.grid(row=1, column=1, padx=20, sticky="e")


root.mainloop()