# Programacion estructurada vs Programacion Orientada a Objetos

## Ejemplo Programacion Estructurada 
```py
clientes = [
    {'Nombre': 'Ricardo', 'Apellido' : 'Dominguez'},
    {'Nombre': 'Jeni', 'Apellido' : 'Saavedra'}

]
```

## Clases
las son como el molde para crear objetos 

* Instanciacion
es cuando el objeto se crea.
* instancia
es un objeto que mientras esta el programa corriendo, existe. 

## __init__
* Se ejecuta al crear un Objeto nuevo
* Permite enviar argumentos durante la Instanciacion. 

### Ejemplo 
```py
class Galleta():
    chocolate = False
    def __init__(self):#se ejecuta al crear un nuevo Objeto
        print("se acaba de crear una galleta.")
    
    def chocolatear (self):
        self.chocolate = True

    def tiene_chocolate (self):
        if self.chocolate:
            print("Galleta con Chocolate")
        else:
            print("No tiene chocolate ")
g1 = Galleta()
g1.chocolatear()
g1.tiene_chocolate()
```