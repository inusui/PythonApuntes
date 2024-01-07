# Programacion POO

class Cliente:
    def __init__(self, ID, Nombre, Apellido):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
    def __str__(self):
        return '{} {}'.format(self.Nombre , self.Apellido)

        
class Empresa:
    def __init__(self, Clientes=[]):
        self.Clientes = Clientes
    
    def mostrar_clientes(self, ID = None):
        for c in self.Clientes:
            if c.ID == ID:
                print(c)
                return
        print("Cliente no encontrado")
    
    def borrar_clientes(self, ID = None):
        for i , c in enumerate(self.Clientes):
            if c.ID == ID:
                del(self.Clientes[i])
                print(str(c), "> Borrado")
        print("Cliente no encontrado")

Ricardo = Cliente(Nombre = "Ricardo", Apellido= "Dominguez", ID= 1)

print(Ricardo)

Jeniffer = Cliente(2 , "Jeniffer", "Saavedra")

print(Jeniffer)

Empresa = Empresa(Clientes=[Ricardo, Jeniffer])

Empresa.borrar_clientes(1)