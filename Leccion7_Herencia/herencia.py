class Producto:
    def __init__(self, referencia, nombre, precio, descripcion):
                
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return """
Referencia\t{}
Nombre\t\t{}
Precio\t\t{}
Descripcion\t{}""".format(self.referencia , self.nombre, self.precio, self.descripcion)

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = " "
    distribuidor = " "

    def __str__(self):
        return """
Referencia\t{}
Nombre\t\t{}
Precio\t\t{}
Descripcion\t{}
Productor\t{}
Distribuidor\t{}""".format(self.referencia , self.nombre, self.precio, self.descripcion, 
                    self.productor, self.distribuidor)

class Libro(Producto):
    isbn = " "
    autor = " "
    def __str__(self):
        return """
Referencia\t{}
Nombre\t\t{}
Precio\t\t{}
Descripcion\t{}
Isbn\t\t{}
Autor\t\t{}""".format(self.referencia , self.nombre, self.precio, self.descripcion, 
                    self.isbn, self.autor)

def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio """
    p.precio = p.precio - (p.precio / 100 * rebaja)
    return p

adorno1 = Adorno(1,"Vaso",5,"Vaso de Vidrio")
#print(adorno1)

alimento1 = Alimento(2,"Botella de Aceite ", 8, "Medio litro")
alimento1.productor="El Campo"
alimento1.distribuidor = "Save Mart"

#print(alimento1)

libro1 = Libro(3,"Harry el potter", 15, "Libro mitico de fantasiar")
libro1.isbn = 5
libro1.autor = "Jota Ka"
#print(libro1)

productos = [adorno1, alimento1]
productos.append(libro1)

for p in productos:
    if ( isinstance (p, Adorno)):
        print(p.referencia , p.nombre)
    elif ( isinstance (p, Alimento)):
        print(p.referencia , p.nombre, p.productor, p.precio)
    elif ( isinstance (p, Libro)):
        print(p.referencia , p.nombre, p.isbn, p.autor)

print("\nProducto Rebajado", rebajar_producto(alimento1, 10))

print(alimento1)

#Copiar lista
listaOriginal = [1,2,3]

listaCopia = listaOriginal[:]
print(listaOriginal)
listaCopia.append(4)
print("Soy la lista Original: ",listaOriginal,"\nSoy la Lista Copia: ",listaCopia)

#Copiar Objeto, se usa un modulo externo

import copy
copiar_adorno = copy.copy(adorno1)
print (copiar_adorno)
copiar_adorno.precio = 50
print("Soy El Objeto Original: ",adorno1,"\nSoy El Objeto Copia: ",copiar_adorno)