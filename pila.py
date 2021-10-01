pila =  [ 3, 4 , 5] # esto es una lista tradicional
pila.append(6)
pila.append(7)

#para sacar el ultimo elemento
pila.pop() #lo saca y lo borra

NumeroDeLaPilaqueSaque = pila.pop()
'''Print 6'''
print("Numero que saque de la pila: ", NumeroDeLaPilaqueSaque, "La Lista Concurrente", pila)

#Al sacar todos los elementos de la pila con pop devuelve un error si no hay nada que sacar

######Colas  - Ques - Estructura FiFo - First In First Out
#se debe importar ya que no se usa con frecuencia
from collections import deque

cola = deque(['Juan','Pedro','Alonso']) #Se le de izquierda a Derecha, Juan llego primero que pedro
cola.append('Juliano') #para agregar

#Se sacan por el primero por tanto es como un pop pero inverso, 
#dicho elemento seria> popleft, hacer un pop por la izquierda

print (cola.popleft()) 
print (cola)