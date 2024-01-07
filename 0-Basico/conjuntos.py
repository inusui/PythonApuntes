conjunto = {1 , 2, 3}

conjunto.add(4)

conjunto.add("Ricardo")
print (conjunto)

print ("\nSe encuentra el 4 dentro del conjunto?" , 4 in conjunto)
grupo = {'Ricardo', 'Ricardo','Ricardo' , 'Raul'}

print ("\nMuentra que dentro de un conjunto elimina los que esta repetidos" , grupo )

l = [1,2,3,3,2,1]
'''
c = set(l) #Transforma a una lista
l = list(c)
'''

#transformar de lista a conjunto en una sola linea de codigo
print ("\nLista con varios numeros repetidos" , l)
l = list( set(l))

print("\n la misma lista pero, se transformó a un conjunto para eliminar los numeros repetidos y luego se volvio a transformar a una lista" , l)

#Ejercicio de Conjuntos
# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# Completa el ejercicio
grupo.add("Ana")
grupo.add("Ramón")
grupo.add("Marta")
grupo.add("Eric")
grupo.add("David")

grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")

print (grupo)