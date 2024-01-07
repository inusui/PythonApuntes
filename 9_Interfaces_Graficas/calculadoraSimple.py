from tkinter import *

root = Tk()

root.title("Calculadora Simple")
root.iconbitmap("recursos/dino.ico")
root.config(bd=20)

def sumar():
    r.set(float(n1.get() ) + float(n2.get() ))
    limpiar()

def limpiar():
    n1.set("")
    n2.set("")
n1 = StringVar()
n2 = StringVar()
r = StringVar()
Label(root, text="Numero 1:").grid(row=0,column=0)
Entry(root, justify="center", textvariable=n1).grid(row=0,column=1) #primero

Label(root, text="Numero 2:").grid(row=1,column=0)
Entry(root, justify="center", textvariable=n2).grid(row=1, column=1) #segundo

Label(root, text="Resultado:").grid(row=2,column=0)
Entry(root, justify="center", textvariable=r, state="disable").grid(row=2, column=1)#resultado

Button(root, text="Sumar", command=sumar).grid( row= 1 , column=2)












root.mainloop()
