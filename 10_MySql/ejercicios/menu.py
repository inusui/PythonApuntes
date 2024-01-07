import sqlite3
from tkinter import *

#Configuracion de la raiz
root = Tk()
root.title("Restaurante - Menu")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="  Restaurante MySQL   ", fg="darkblue", font=("Arial",28,"bold italic")).pack()
Label(root, text="  Menu del Dia   ", fg="black", font=("Arial",24,"bold italic")).pack()

#Separacion de titulos y categorias
Label(root, text="").pack()

#conexion DB

conexion = sqlite3.connect("restaurante.db").cursor()
#cursor = conexion

#Buscar categoria y platos

conexion.execute('''SELECT * FROM categoria''')
    
allcategories = conexion.fetchall()
for categorie in allcategories:
    Label(root, text=categorie[1], fg="black",font=("Arial",20,"bold")).pack()
    platos = conexion.execute("SELECT * FROM plato WHERE categoria_id={}".format(categorie[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="black",font=("Arial",15,"italic")).pack()

conexion.close()
Label(root, text="15USD", fg="darkblue",font=("Arial",18,"bold italic")).pack(side="right")

#Bucle de aplicacion
root.mainloop()