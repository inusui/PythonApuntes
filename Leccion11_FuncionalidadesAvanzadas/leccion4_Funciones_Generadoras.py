lista = [numero for numero in [0,1,2,3,4,5] if numero%2 == 0]
print (lista)
lista = [numero for numero in range(0,6) if numero%2 == 0]
print (lista)
'''
Por norma general las funciones retornan "return" algun dato, osea que se almacena.
las funciones generadoras no almacenan datos. 
"Sede" el dato al siguiente. 
# Se ocupa el minimo de memoria y se pueden instanciar infinidad de elementos sin ocupar la memoria. 
'''

#una funcion que genere x cantidad de numeros pares. 

#del 0 al 10

def pares(n_maximo):
    for numero in range(n_maximo + 1):
        if numero%2 ==0:
            #en lugar de hacer return
            yield numero

print(pares(10))
#se obtiene un objeto del tipo generador. Se pueden recorrer como un range, es como una lista
for numero in pares(10):
    print(numero)

#en una lista
print(  [numero for numero in pares(10)]    )       #se esta ejecutando, mas no guardando o asignando a una variable

#! 

#si me excedo de 3, da un error asi que se debe hacer una exception para que el programa no se detenga
try:
    pares = pares(3)
    print(next(pares))
    print(next(pares))
    print(next(pares))
except Exception as quepaso:
    print(type(quepaso).__name__)

#! Iterar lista

lista = [1,2,3,4,5,6]

#No se pueden Iterar Listas o Cadenas como si fuese una secuancia, pero se pueden convertir en itaradores. 

lista_iterale = iter(lista)
print(next(lista_iterale))

print(next( iter("Hola") ))