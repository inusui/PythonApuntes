from tkinter import PhotoImage, Tk, Label
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
imagen = PhotoImage(file=resource_path("res/chems.png"))
Label(text="Mi Programa Ejecutable").pack(padx=20, pady=20)
Label(root,image=imagen, bd=0).pack(padx=20, pady=20)

root.mainloop()
