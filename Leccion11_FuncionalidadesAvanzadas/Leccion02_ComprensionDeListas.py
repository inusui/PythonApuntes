#Lineas avanzadas en la misma linea de codigo

#metodo tradicional
lista = []
for letra in 'casa':
    lista.append(letra)

#metodo con comprension de listas

lista2 = [  letra for letra in 'casa'] 
#a la izquierda se guarda cada iteracion del bucle fory por ultimo se le asigna a la lista2 como si fuese un append
print (lista2)



#   
#tradicional, las potencias del 0 al 10
lista = []
for numero in range(0,11):
    lista.append(numero**2)

#Comprension de listas
lista=[ numero**2 for numero in range(0,11)]
print(lista)
#

#Lista con los multiplos de 2 entre o y 10 
lista = []
for numero in range (0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

#comprension de listas 

lista =[numero for numero in range(0,11) if numero %2 ==0] #la condicion iria de ultimo, despues del for
print(lista)

#lista de numeros pares, desde una lista con las potencias
lista=[ numero**2 for numero in range(0,11)]

pares =[]
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#en una sola linea 
pares = [ numero for numero in [numero ** 2 for numero in range (0,11)] if numero % 2 == 0]
print(pares)

#/ Todos los numeros multiplos de 2, 3, 4 y 8 entre 0 y 500. no puede contener numeros repetidos y deben estar ordenados de menor a mayor

primera = []
for numero in range (0,501):
    if numero % 2 == 0:
        if numero % 3 == 0:
            if numero % 4 == 0:
                if numero % 8 == 0:
                    primera.append(numero)

segunda = [numero for numero in range (0,501) if numero %2 ==0 and numero % 3 == 0 and numero % 4 == 0 and numero % 8 == 0]

print (primera == segunda)
# Ni yo mismo se que estoy haciendo, solo segui la indicacion del ejercicio.
