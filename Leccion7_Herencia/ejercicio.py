'''Trata de Herencia

*Uso variable indeterminada en funcion catalogar()
'''

class Vehiculo():

    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__ (self):
        return "Color {}. {} Ruedas".format(self.color, self.ruedas)
    

class Coche(Vehiculo):

    def __init__ (self, color, ruedas, velocidad, cilindrado):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrado = cilindrado

    def __str__(self):
        return Vehiculo.__str__(self) + ", {}cc, {}Km/h".format(self.cilindrado, self.velocidad)
class Camioneta (Coche):
    
    def __init__(self,color,ruedas,velocidad, cilindrado, carga):
        super().__init__(color,ruedas,velocidad, cilindrado)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {}kg".format(self.carga)

class Bicicleta (Vehiculo):
    def __init__(self,color,ruedas, tipo):
        super().__init__(color,ruedas)
        while(True):
            if (tipo == "urbana" or tipo == "deportiva"):
                self.tipo = tipo
                break
            else:
                tipo = input("Elige entre urbana o deportiva\n")

    def __str__(self):
        return super().__str__() + "Tipo: {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self,color, ruedas, tipo, velocidad, cilindrada ):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "{}Km/h , {}cc".format(self.velocidad, self.cilindrada)

def Catalogar(lista, ArgumentoRuedas = None):
    if (ArgumentoRuedas != None):
        contador = 0
        for i in lista:
            if (i.ruedas == ArgumentoRuedas):
                contador += 1
        print("Se han encontrado {} vechiculos con {} Ruedas".format(contador, ArgumentoRuedas))
    for i in lista:
        if (ArgumentoRuedas == None):
            print ("""Asi muestro su nombre {}\
        Asi muestro sus atributos  {}
        """.format(type(i).__name__, i ))
        elif (i.ruedas == ArgumentoRuedas ):
            print("{}: {}".format(type(i).__name__ , i))


        

carro1 = Coche("Azul",4,120,1200)
print(carro1)

moto1 = Motocicleta("Azul", 2, "urbana", 120, 12000)
print(moto1)

bici1 = Bicicleta("Negro", 2 , "deportiva")
print(bici1)

camion1 = Camioneta("Blanco", 4 , 40, 500,50)
print("Camion", camion1)

vehiculo1 = Vehiculo("Amarillo", 4 )
print("Algun Vehiculo" , vehiculo1)


Catalogar([moto1, camion1, bici1,vehiculo1] , 2 )