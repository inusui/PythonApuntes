# Funcion Filter()
'''
## Para filtrar

'''


numeros = [ 2 , 5 , 10 , 23 , 50 , 33]

#Quedarse solo con los multiplos de 5
def multiple(numero):
    if numero % 5 == 0: 
        return True

print(list(filter(multiple, numeros)))

#Se puede usar Lambda
print(list(filter ( lambda numero: numero % 5 ==0, numeros)))

#Dada una lista de varias personas, filtra las menores de edad
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def __str__(self) -> str:
        return "{} de {} años".format(self.nombre, self.edad)

personas = [
    Persona("Juan",25),
    Persona("Sergio",6),
    Persona("Venus",2),
    Persona("Jeniffer",24),
    Persona("Pedro",15),
    Persona("Felipe",40)
]
menores =  filter ( lambda persona : persona.edad < 18,personas)    

for menor in menores:
    print (menor)