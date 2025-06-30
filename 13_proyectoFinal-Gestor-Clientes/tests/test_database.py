import copy
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('20J', 'Venus', 'Slytherin'),
            db.Cliente('20Z', 'Jeni', 'Saa'),
            db.Cliente('12A', 'Raul', 'Elric')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('12A')
        cliente_inexistente = db.Clientes.buscar('11A')

        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo = db.Clientes.crear('x21', 'Raul', 'Slytherin')
        self.assertEqual(len(db.Clientes.lista), 4)
        existe = db.Clientes.buscar(nuevo.dni)
        self.assertIsNotNone(existe)

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('12A'))
        cliente_modificado = db.Clientes.mofificar('12A', 'Juan', 'Samsung')
        self.assertEqual(cliente_a_modificar.nombre, 'Raul')
        self.assertEqual(cliente_modificado.nombre, 'Juan')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('12A')
        cliente_inexistente = db.Clientes.buscar('12A')
        self.assertEqual(cliente_borrado.dni, '12A')
        self.assertIsNone(cliente_inexistente, '12A')
