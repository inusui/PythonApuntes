""" Unira el programa principal run.py con toda la interfaz 
A traves de este menu se interactuara con la bd
"""

import os


def iniciar():
    while True:
        os.system('clear') # cls en powershell

        print('''
              =========================
              Bienvenido al gestor
              =========================
              [1] Listar clientes
              [2] Buscar un cliente
              [3] Añadir un cliente
              [4] Modificar un cliente
              [5] Borrar un cliente
              [6] Cerrar el gestor
              =========================
              ''')
        option = input("> ")
        os.system('clear') # cls en powershell

        if option == '1':
            print("Listando los clientes")
        elif option == '2':
            print("Buscando un cliente")
        elif option == '3':
            print("Añadiendo un cliente")
        elif option == '4':
            print("Modificando un cliente")
        elif option == '5':
            print("Borrar un cliente")
        elif option == '6':
            print("Cerrar el gestor")
            break

        input("\nPresiona ENTER para continuar....")