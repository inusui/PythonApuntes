""" Unira el programa principal run.py con toda la interfaz 
A traves de este menu se interactuara con la bd
"""

import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_terminal()

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
        helpers.limpiar_terminal()

        if option == '1':
            print("Listando los clientes")
            for cliente in db.Clientes.lista:
                print(cliente)

        elif option == '2':
            print("Buscando un cliente")

            dni = helpers.leer_texto(3, 3, "Introducir DNI").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no existe.")

        elif option == '3':
            print("Añadiendo un cliente")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "Introducir DNI").upper()
                if helpers.validate_dni(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(
                3, 10, "Introducir Nombre").capitalize()
            apellido = helpers.leer_texto(
                3, 10, "Introducir Apellido").capitalize()

            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente agregado")

        elif option == '4':
            print("Modificando un cliente")

            dni = helpers.leer_texto(3, 3, "Cliente a modificar DNI").upper()
            cliente = db.Clientes.buscar(dni)

            if cliente:
                nombre = helpers.leer_texto(2, 30,
                                            f"Nuevo nombre [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30,
                                              f"Nuevo apellifo [{cliente.apellido}]").capitalize()
                db.Clientes.mofificar(dni, nombre, apellido)
                print("Modificado")
            else:
                print("Ese cliente no existe")

        elif option == '5':
            print("Borrar un cliente")

            dni = helpers.leer_texto(3, 3, "Introducir DNI a Borrar").upper()
            print("Ya lo borrate") if db.Clientes.borrar(
                dni) else print("no ta ese cliente")

        elif option == '6':
            print("Cerrar el gestor")
            break

        input("\nPresiona ENTER para continuar....")
