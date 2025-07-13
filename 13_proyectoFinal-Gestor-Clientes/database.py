"""Controlador de datos
e interfaz para crear, eliminar y modificar informacion
"""
import csv
import config
class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido}"


class Clientes:
    """Clase que maneja la lista de clientes"""
    lista = []
    with open(config.DATABASE_PATH) as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            dni, nombre, apellido = row
            lista.append(Cliente(dni, nombre, apellido))


    @staticmethod
    def buscar(dni):
        """Buscar un cliente por su DNI"""
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()  # Guardar cambios en el archivo CSV
        return cliente

    @staticmethod
    def mofificar(dni, nombre, apellido):

        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                listaCliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return listaCliente
                

    @staticmethod
    def guardar():
        """Guardar la lista de clientes en el archivo CSV"""
        with open(config.DATABASE_PATH, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow([cliente.dni, cliente.nombre, cliente.apellido])