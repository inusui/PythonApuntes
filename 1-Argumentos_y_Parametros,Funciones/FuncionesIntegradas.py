
import imp
import re


n = 25

print ('''Binario {}
Hex {}
Valor Absoluto {}
Redondeo {}
Evaluar {}
Tamaño de una cadena len=> {} \n'''.format(bin(10), hex(10), abs(10), round(5.6), eval('n*5') , len("Una cadena")
                    ))

def relacin(a,b):
    if (a>b):
        print (a , " Es mayor que ", b)
    elif (a<b):
        print (a , " a es menor que ", b)
    elif (a == b):
        print (a, " y " , b , " Son iguales")

relacin(10,5)
relacin(5,10)
relacin(5,5)

def intermedio (a,b):
    return (a+b) / 2
print (intermedio(-12,24))

def recortar (numero, minimo, maximo):
    if (numero < minimo):
        print("menor que el minimo")
    elif(numero > maximo):
        print ("mayor que el maximo")
    elif (numero > minimo and numero < maximo):
        print ("no supera ningun limite , " , numero)
recortar(-10,0,10)


def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
            
        else:
            impares.append(n)
    print('''Lista Par {}
lista impar {}'''.format(pares, impares))
    return pares, impares
            
    

separar([6,5,2,1,7])
pares, impares = separar([6,5,2,1,7])
