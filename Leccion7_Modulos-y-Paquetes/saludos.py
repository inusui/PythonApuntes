# Este es un modulo con funciones.
def saludar():
    print("Imprimo saludar desde saludos.py en la raiz de Leccion7_Modulos")

if __name__ == '__main__':
    saludar()

class Saludo():
    def __init__(self):
        print("Te saludo desde saludos.__init__()")