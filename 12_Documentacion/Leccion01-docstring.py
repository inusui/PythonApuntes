#Doc String
'''
* Cadenas de Documentacion
* Por defecto no tienen ningun valor
'''

def hola (argumento):
    '''Docstring de la funcion, Recibe un como argumento tu nombre e imprime un hola con tu nombre.'''
    print("Hola " , argumento, "\nComo estas?")
help(hola)

class Clase:
    '''Docstring de la clase
    Aqui escribiria que hace la clase'''

    def __init__(self) -> None:
        '''Iniciador o metodo contructor de la clase'''
        pass
    
    def metodo (self):
        '''Metodo de la clase'''
        pass

o = Clase()
help(o)
import mi_modulo
mi_modulo.saludar()

help(mi_modulo)
import paquetes

help(paquetes)