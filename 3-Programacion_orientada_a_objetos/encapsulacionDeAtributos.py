class Ejemplo:
    contador = 0
    __atributo_privado = "Soy inalcanzable"

    def __init__(self):
        Ejemplo.contador += 1
        print ("Instancias creadas : ", Ejemplo.contador)

    def __metodo_privado(self):
        print ("Metodo inalcanzable")
    
    def atributo_publico(self):
        return self.__atributo_privado


a = Ejemplo()

print(a.atributo_publico())

for a in range (10):
    Ejemplo()