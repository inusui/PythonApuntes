# Herencia

```py
class Producto:
    def __init__(self, referencia, tipo, nombre, precio, descripcion, 
                productor = None, distribuidor = None, 
                isbn = None, autor = None):
                
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
```
de tener una clase con tantos atributos que declarar hace que el codigo sea confuso, por lo tanto lo mejor es separar en grupos estos atributos.
ademas, el mismo objeto no necesariamente va a usar todos los atributos, por lo tanto se generará aun mas variables que nunca se usaran.
por ejemplo. un alimento no necesita un autor, asi mismo un libro no va a usar un productor. 

Los Objetos se pasan por referencia por lo tanto si se cambia un atributo en el tambien se cambie dentro del objeto.
```py
ObjetoOriginal.atributo = 1
objetoCopia = objetoOriginal #en teoria hacemos una copia, pero estamos asignando
objetoCopia.atributo = 2
print (objetoOriginal)
```
output ```ObjetoOriginal.atributo=2``` esto se da porque se cambio tambien el objeto original. 

pero en la linea ```objetoCopia = objetoOriginal``` estamos asignando, por lo tanto todo lo que se haga en objetoCopia se cambia en ObjetoOriginal.

## Copiar Objeto
```py

#Copiar Objeto, se usa un modulo externo

import copy
copiar_adorno = copy.copy(adorno1)
print (copiar_adorno)
copiar_adorno.precio = 50
print("Soy El Objeto Original: ",adorno1,"\nSoy El Objeto Copia: ",copiar_adorno)
```

## Polimorfia
Propiedad de la herencia en que objetos de distintas subclases pueden responder a una misma accion. 

```py
def rebajar_producto(p, rebaaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio """
    p.precio = p.precio - (p.precio / 100 * rebaja)
    return p
```

El metodo ```rebajar_producto``` Recibe objetos de distintas clases y accede el atributo ```precio``` dando por hecho que existe en ellos. 

## Llamar y usar Metodos de la super clase.
En ocaciones necesitamos usar los mismos argumentos de la super clase en las sub clases, por ello se deben llamar en la subclase y asi no reescribir codigo. 

```py
class SuperClase():
    def __init__(self,nombre):
        self.nombre = nombre
    
class Hija(SuperClase):
    def __init__ (self, nombre, Id )
    SuperClase.__init__(self, nombre)
    self.Id = Id

```
de esa manera podemos acceder a los elementos de la clase padre desde la clase hija, se aplica la herencia

#### Usando Super()
```py
class SuperClase():
    def __init__(self,nombre):
        self.nombre = nombre
    
class Hija(SuperClase):
    def __init__ (self, nombre, Id )
    super().__init__(nombre)
    self.Id = Id
    
```
