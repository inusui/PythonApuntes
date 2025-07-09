""" Uso general y comunes
Se puede usar en varios scripts

"""
import re
import os
import platform


def limpiar_terminal():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None

    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        else:
            print("Try again")
        
def validate_dni(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print("Invalid DNI")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("Ese ya se uso")
            return False
    return True