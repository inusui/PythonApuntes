# Contadores

from collections import Counter
import imp
l = [ 1,2,3,4,1,2,3,1,2,1]

print(Counter(l))
print (Counter("palabra"))

animales = "gato perro canario perro canario perro gato perro"
c = Counter (animales.split(" ") ) 
print(c)#Sepera si esta spliteado, osea que contara las Listas de las Colecciones de datos

print("los 2 mas comunes de la lista c" , c.most_common(2)) #los 2 mas comunes de la lista c

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l) 
print(c)

#Counter es una subclase de los diccionarios, por lo tanto puede usar sus funciones. 
print ("hay 4 10, 3 20, 1 unico 40",c.items(),
"\ndictKeys, solo muestra los numeros no la cantidad que hay,", c.keys(),
"\nValues, devuelve la cantidad que se repiten,", c.values())

print("La cantidad de elementos que hay en ese contador(lista), ", sum(c.values()))

#llamar un diccionario vacio con valor default
from collections import defaultdict
d = defaultdict(str)
d["algo"] #acceder a una key que no hemos declarado
print("\nSe crea la un valor por default a la key que no hemos creado", d)



#Ordenar Dict, ya que al introducir nuevas variables estas no se ordenan segun llegan a su variable

from collections import OrderedDict
n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print ("Ordena el diccionario a medida que le introducimos nuevas variables", n)
# no son equivalentes a otros

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

print (n == n1) #no son iguales porque uno es ordenado y el otro no 


#Tuplas con nombre
from collections import namedtuple
persona = namedtuple('Persona', 'nombre apellido edad') #como crear una clase pero un poco mas sencillo 
p = persona(nombre="ricardo", apellido = "dom", edad = 25) #Una tupla es inmutable, no se puede modificar
print(p.nombre, "\n", p)