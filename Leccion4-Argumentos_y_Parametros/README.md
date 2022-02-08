# Texteando aqui un rato

Cuando enviamos valores a una funcion ```def``` estos valores se envian como una copia, se usan y se destrullen luego de utilizarse.

Esto no ocurre con las listas, estas se envian como referencias.
Que se envien como Referencias nos quiere decir que, el lugar de la copia nos enviara el dato original. por lo tanto si se modifican dentro de la funcion asi se quedan. 

* Le puedo enviar la cantidad de valores que desee.

# Codigo
```py
def resta (a=None,b=None):
    if a == None or b ==None:
        return "Error, no enviaste valores a la funcion"
    return a - b

print (resta(1,5))

#Especificando

print ("La Resta Especificando seria=> {}".format(resta(b=2,a=5)))

print (resta())#Viendo la declaracion de Error


##############  Paso por Valor

def Doblar_valor(numero):
    numero *=2
    return numero

n=10
print ("Valor de N dentro de la funcion Doblar_valor {}".format(Doblar_valor(n)))
print(n)
#no Afecta nada al exterior de la Funcion

#   Ahora con listas
def Doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2
    return numeros    

ns = [10 , 50 , 100]

print("Se envia la lista a la funcion y se imprime => {}".format(Doblar_valores(ns)))
print("\nAhora por fuera de la funcion queda asi nuestra lista {}\nCambio!".format(ns))

print('''De que manera enviar una lista a una funcion y que no se modifique
Bueno, se manda una copia.
Al llamar la funcion se hace Slicing
Cambia dentro de la funcion => {}
Pero no Afuera! => {}'''.format(Doblar_valores(ns[:]),ns))
```
## Argumentos Indeterminados
Quiere decir que se le ponen variables a la lista sin tener en cuanta el tipo o algo asi. 

```py
#   Argumenos y parametros Indeterminados

def indeterminados_posicion(*args): #Parametro Iterable se lo pone un * y por regla general se le llama args.
    print ("Imprimiendo todo lo que me mandan", args) #  Se crea una Tupla

   #Recorriendolo
    for arg in args:
        print ('''Imprimiendo segun indice   {}'''.format(arg))
    #Aqui arriba lo que hace es recorrerlo por indice e imprimiendolo. 
```
*   args es una variable, solo que asi se le llama. obviamente se puede cambiar por cualquier nombre. 

## Argumentos indeterminados con llave (palabra clave)

Identificar cada argumento bajo una clave. 
se aplica poniendo ```**``` en lo que recibe la funcion
```py
def indeterminados_porNombre (**kwargs):
        print (kwargs)
indeterminados_porNombre(c=4, cadena="hola")
```
output ```{'c': 4, 'cadena': 'hola'}```
### Recorriendo
* Por defecto solo muestra las claves
Por ello se usa la misma varible y usando un indice para imprimir lo que contiene
```py
def indeterminados_porNombre (**kwargs):     
    for kwarg in kwargs:
        print ('''\nPor Defecto solo muestra las claves {0}
Entonces se Agrega el keyword, pasandole el indice {1}
De Esta manera Quedaria: Llave: {0}  Valor:{1}\n'''.format(kwarg, kwargs[kwarg]))

indeterminados_porNombre(c=4, cadena="hola")
```
_OutPut_ ```Por Defecto solo muestra las claves c
Entonces se Agrega el keyword, pasandole el indice 4
De Esta manera Quedaria: Llave: c  Valor:4


Por Defecto solo muestra las claves cadena
Entonces se Agrega el keyword, pasandole el indice hola
De Esta manera Quedaria: Llave: cadena  Valor:hola```

## Argumentos indeterminados y Diccionarios Indetermiandos en una sola funcion
Esto es utilizado frecuentemente

en una misma funcion se aplican ambos conceptos, python sabe diferenciarlos segun lo que se le envie
```py
def super_funcion(*argumentos, **argumentosConClave):
    total = 0
    for argumento in argumentos:
        total =+ argumento
    print ("\nSumatorio indeterminado es: {}".format(total))
    for argumento in argumentosConClave: #tambien le puedo llamar diccionario
        print("\n{}:{}".format(argumento, argumentosConClave[argumento]))

super_funcion(10,50,-1,1,56, nombre = "Ricardo", edad = 27)
```
output
```Sumatorio indeterminado es: 56

nombre:Ricardo

edad:27```