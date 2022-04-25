# Funciones Lambda
'''
## Son expresiones o funciones anonimas. 
una funcion anonima, no tiene nombre.
No es necesario usar un def

* El contenido de una funcion lambda es una unica accion y no un bloque de acciones. 
 
'''

#con Def


def doblar (numero):
    return numero * 2
print(doblar(5))

#A funcion Lambda
doblar = lambda numero: numero * 2
print(doblar(10))

# en impares
impar = lambda numero: numero%2 != 0 
print(impar(3))

revertir = lambda cadena: cadena[::-1]
print(revertir("Hola"))

sumar = lambda x,y: x + y
print(sumar(15,5))