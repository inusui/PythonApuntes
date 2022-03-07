lista = [1,2,3]
lista.append(4)
print ("lista.append(4)\nAgrega a la lista" , lista)

lista.clear()
print("\nlista.clear()\nVacia la lista",lista)
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)

print("\nlista1.extend(lista2)\npara unir una segunda lista a la lista1", lista1)

print("\n['lista','lista'].count('lista')\nContar dentro de una lista:",["Hola","Hola"].count("Hola"))

print("\nlista.index('DeQue?')\nBuscar indice de lista",lista1.index(2))

lista1.insert(0,0)
print("\nlista1.insert(0,0)\nInserta en el indice 0 un 0",lista1)
lista = [5,10,15,25]
lista.insert(-1,20)#1 antes del ultimo
print(lista)

lista.pop()
print("\nSaca el ultimo elemento de la lista|lista.pop()",lista)

lista.remove(10)
print("Remueve la variable que se le indica\nlista.remove(10) ", lista)

lista.reverse()
print("Dar vuelta a la lista\nlista.reverse()", lista)
#No sirve con str directamente
l = list("Hola Mundo")
l.reverse()
print("Si asignamos un string a una lista el .reverse() si funciona\n",l)

cadena = "".join(l)
print("\nUsamos un .join para volver a obtener un str\ncadena = "".join(l)",cadena)


#Ordenar los elementos
l = [9,10,65,111,85]
l.sort()
print("\nOrdena la lista\nl.sort()",l)
l.sort(reverse=True)
print("Ordena de forma inversa\nl.sort(reverse=True)", l)

