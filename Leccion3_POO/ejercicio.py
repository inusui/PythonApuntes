# Programacion de Graficos
import math

class Punto:
    def __init__(self, X = 0 , Y = 0):
        self.X = X
        self.Y = Y
        print("Se a creado una nueva Coordenada {},{}".format(self.X , self.Y))
        
    
    def __str__(self):
        return( "({}, {})".format(self.X, self.Y) )

    def cuadrante(self):
        try:
            if (self.X == 0 and self.Y == 0):
                print("{} Esta en el Origen".format(self))
            elif (self.X > 0 and self.Y > 0):
                print("{} Primer Cuadrante ambos son positivos".format(self))
            elif (self.X < 0 and self.Y > 0):
                print("{} Segundo Cuadrante, X es negativo, Y es Positivo".format(self))
            elif( self.X < 0 and self.Y < 0):
                print("{} Tercer Cuadrante. Ambos son Negativos".format(self))
            elif (self.X > 0 and self.Y < 0):
                print("{} Cuarto Cuadrante, X es positivo y Y es negativo".format(self))
            else:
                print("No pertenece a ningun cuadrante?\nRevisa que esta mal\nEsto fue lo que introdujo {}".format(self))
        except TypeError:
            print ("Solo se permiten numeros")
        except Exception as e:
            print (e)

    #def vector(self, X2 = 0 , Y2 = 0):
    def vector(self, p):
        #resultado = ((self.Y2 - self.Y) (self.X2 - self.X))
        print ("El Vector entre {} y {} es: ( {} , {})".format(self, p , p.X - self.X, p.Y - self.Y))
    
    def distancia(self, p):
        print("Distancia\nCon las X: {} y {}\nCon las Y: {} y {}".format(self.X , p.X , self.Y, p.Y))
        resultado = math.sqrt ( ( (p.X - self.X)**2 ) + ( (p.Y - self.Y) ** 2 ) )
        print ("Distancia entre ellos " , resultado)
    
        

class Rectangulo:
    def __init__(self, inicial = Punto() , final = Punto() ):
        self.inicial = inicial
        self.final = final
        print("Se a creado un nuevo Rectangulo.\nPunto inicial {}   |Punto Final {}"
                .format(self.inicial, self.final))
                
    def __str__(self):
        return( "({}, {})".format(self.inicial, self.final) )

    def base (self):
        self.base = abs(self.final.X - self.inicial.X)
        return "La base es del Rectangulo {} es : {}".format(self, self.base)

    def altura (self):
        self.altura = abs(self.final.Y - self.inicial.Y)
        return "La altura es del Rectangulo {} es : {}".format(self, self.altura)

    def area(self):
        try:
            self.base = abs(self.final.X - self.inicial.X)
            self.altura = abs(self.final.Y - self.inicial.Y)
            self.area = self.base * self.altura
            return "El area del rectangulo es {}".format(self.area)
        except Exception as e:
            return e
    

print("********************************\nPuntos")
A = Punto(2, 3)
B = Punto(5,5)
C = Punto(-3 , -1)
D = Punto(0,0)

'''.
print("*********************************\nconsulta a que cuadros perteneces A, C y D")
A.cuadrante()
C.cuadrante()
D.cuadrante()

print("********************************\nConsulta los Valores AB y BA")
A.vector(B)
B.vector(A)

print("*********************************\nConsulta la Distancia entre los puntos A->B y B->A")
A.distancia(B)
B.distancia(A)


print("cual de los puntos (ABC) esta mas lejos del origen?")
if ( A.distancia(D) >  B.distancia(D) and A.distancia(D) > C.distancia(D)):
    print("Soy mayor? A")
elif( B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D)):
    print("soy mayor? B")
elif( C.distancia(D) > A.distancia(D) and C.distancia(D) > B.distancia(D)):
    print("Soy mayor C")
else:
    print("nel")

'''

R = Rectangulo(A,B)
print ('''{}
{}
{}'''.format(R.base(), R.altura(), R.area()))
