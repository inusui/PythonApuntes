from tkinter import *

root = Tk()

menubar = Menu(root) #el menu no se empaqueta
#se tiene que añadir a la raiz
root.config(menu=menubar)

#submenus
filemenu = Menu(menubar, tearoff=0)#es submenu de menubar
#add elementos
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca De")

#texto del menubar
menubar.add_cascade(label="Archivo", menu=filemenu) #primer
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

#******************************** Popups
from tkinter import messagebox as MessageBox #lo ultimo es opcional
from tkinter import colorchooser as ColorChoose #Elegir color
from tkinter import filedialog 

def boton():
    #MessageBox.showinfo("Titulo de la Ventana","Un Mensaje")
    #MessageBox.showwarning("Alerta","Alerta")
    #MessageBox.showerror("Error","Tienes un error") 

    #Preguntar si o no 
    '''alt = MessageBox.askquestion("Salir","Estas seguro de salir?")
    print (alt)
    if alt =="yes":
        root.destroy()'''
    
    #Pregunta aceptar o cancelar
    #alternativa = MessageBox.askokcancel("Salir","Salir sin guardar?")

    #si o no, devolviendo True o False
    '''alternativa = MessageBox.askyesno("Salir?", "salir?")
    if alternativa:
        root.destroy()
    '''

    #Preguntar si quiere volver a intentar
    ''' alt = MessageBox.askretrycancel("Reintenta", "No se conecta")
    if alt:
        root.destroy() #Para comprobar si funciona o no '''
    #alt = ColorChoose.askcolor(title="ELige")
    ''' 
    ruta = filedialog.askopenfile(title="Abrir Fichero" , initialdir="D:", filetypes=(("Ficheros de Texto","*.txt"), 
    ("Fichero de Texto Avanzado","*txt2"),
    ("Todos los Ficheros","*.*")))
    #Se debe dejar una , enter la primer tupla y la finalizacion del argumento en caso tal solo se filte con 1 tipo de dato
    # lo recomentable es hacer 2, el filtro y "todo lo demas"
    print (ruta)
    '''
    fichero = filedialog.asksaveasfile(title="Guardar Archivo", mode="a+", defaultextension=".txt")
    #Equivalente a open('ruta', 'w')
    if fichero is not None:
        fichero.write("desde codigo")
        fichero.close()


unboton = Button(root, text="Veamos el popup", command=boton)
unboton.pack()
Label(root).pack()
def salir():
    root.destroy()
cierrame = Button(root, text="Cierrame", command=salir).pack()
Label(root).pack()

root.mainloop()