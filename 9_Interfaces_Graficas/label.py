from tkinter import *

root = Tk()

'''#Configuracion de marco
frame = Frame(root, width=480, height=320)
frame.pack()

#Etiqueta de Texto o label
label = Label(frame, text="Veamos")
#label.pack() #No respeta el tamaño del marco, el tamaño lo reinicia. 
label.place(x=0,y=0)# se le da al label una ubicacion
'''
#Variables Dinamicas
'''texto = StringVar()
texto.set("Nuevo texto dice")

Label(root, text="Si").pack(anchor="nw")
label = Label(root, text="al centro")
Label(root, text="al sur este").pack(anchor="se")


label.pack(anchor="center") #el empaquetado se hace afuera para no asignar a label "algo" innecesario
label.config(bg="gray", fg="red", font=("Verdana", 24))
label.config(textvariable=texto)
'''
#Mostrar imagen o gif
imagen = PhotoImage(file="recursos/rain.gif")
Label(root, image=imagen, bd=0).pack(side="left")
imagen2 = PhotoImage(file="recursos/chems.png")
Label(root,image=imagen2, bd=0).pack(side="right")

#Blucle para mantener la ventana abierta
root.mainloop()