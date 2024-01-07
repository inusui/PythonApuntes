lista = [1,2,3]
def hola():
    def bienvenido():
        return "Hola"
    print (locals() ) #{'bienvenido': <function hola.<locals>.bienvenido at 0x000001A88D8B5CF0>}

    return bienvenido

# No se puede ejecutar bienvenido directamente porque esta en el segundo nivel de las declaraciones. 
# El primer nivel son las funciones globales. 
#por lo tanto bienvenido es una funcion local de hola.

print(globals()['lista'])


#acceder a bienvenido

print(hola()()) #2 parentesis para ejecutar la primera funcion que esta dentro
#por lo regular se se asigna una variable
bienvenido = hola()
#ahora si se accede a bienvenido con
print(bienvenido())

# si de la memoria borramos la funcion hola(), aun podemos seguir usando bienvenido()
del(hola)
print(bienvenido())

#Como argumento de otra funcion
def hola():
    return "Hola!\neviando una funcion como argumento de otra funion"

def test(a):
    print( a() )

test(hola)


def saludo():
    print("Hola")
def adios():
    print("Adios")

def monitorizar(funcion):
    def decorar():
        print("\t Se esta apunto de ejcutar la funcion:", funcion.__name__) #Propiedad avanzada
        funcion()
        print("\tSe a finalizado la ejecucion:",funcion.__name__)
    return decorar

monitorizar(adios)() #Ya que en una se ejecuta la funcion decorar() pero sin poder acceder a saludo().
#usando el segundo parentesis se ejcuta la funcion que se envia como argumento

@monitorizar 
def saludando():
    print("Buenos dais")

saludando() #Solo se llama al saludando que esta dentro
''' con el @monitorizar por encima de la definicion hace que sea parte de la def monitorizar'''

def monitorizar_args(funcion):
    def decorar(*args, **kwargs):
        print("\tSe esta apunto de ejcutar la funcion:", funcion.__name__) #Propiedad avanzada
        funcion(*args, **kwargs)
        print("\tSe a finalizado la ejecucion:",funcion.__name__)
    return decorar

@monitorizar_args   #automatizar que se le asignen las otras funciones
def saludo(nombre):
    print("Hola {}".format(nombre))
@monitorizar_args
def adios(nombre):
    print("Adios {}".format(nombre))

saludo("Ricardo")