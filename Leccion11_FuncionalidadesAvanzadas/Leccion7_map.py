# Funcion Map()
'''
* Similar a Filter
En lugar de aplicar una lista o una funcion en secuencia, aplica una funcion sobre todos los elementos y devuelve un itereable
* Es recomendable usarlos con lambdas
para asi ahorrarse el proceso de usar ciclos for
'''

numeros = [2,5,10,23,50,33]
#doblar todos los elementos. 
def doblar (numero):
    return numero *2 
#Map aplica todos los elementos de la lista numeros a la funcion doblar()
objeto_map = map(doblar, numeros)

print(next(objeto_map), list(objeto_map))


#Se puede hacer con un Lambda
objeto_map = list (map( lambda x: x*2, numeros ))

print(objeto_map)


lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]
#Siempre y cuando tengan la misma logitud se pueden incluir en una funcion lambda, si hay algun otro elemento este simplemente se omite
print("Multiplica una lista con la otra\n",
    list(map(lambda x,y: x*y, lista_a, lista_b))
)

# Aumentar la edad de las personas en +1
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def __str__(self) -> str:
        return "{} de {} años".format(self.nombre, self.edad)

def createPersonas():
    #Es que no queria volver a recrear la lista personas para el segundo ejemplo [Linea: 66]
    personas = [
        Persona("Juan",25),
        Persona("Sergio",6),
        Persona("Venus",2),
        Persona("Jeniffer",24),
        Persona("Pedro",15),
        Persona("Felipe",40)
    ]
    return personas


def incrementar (persona):
    persona.edad +=1
    return persona

personas = map (incrementar, createPersonas())

def recorrer(personas):
    #un poco de lo mismo que la funcion createPersonas(), como al final es el mismo codigo mejor lo reutilizo
    for persona in personas:
        print("\n",persona)
        
recorrer(personas)


# se puede hacer con lambda
personas_0 = map(lambda persona: Persona(persona.nombre, persona.edad+1),createPersonas())
print("***********")
recorrer(personas_0)

numeros = list(filter(lambda num: num%5==0, map(lambda num: num/2, numeros)))
