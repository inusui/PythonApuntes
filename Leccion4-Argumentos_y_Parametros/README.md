# Texteando aqui un rato

Cuando enviamos valores a una funcion ```def``` estos valores se envian como una copia, se usan y se destrullen luego de utilizarse.

Esto no ocurre con las listas, estas se envian como referencias.
Que se envien como Referencias nos quiere decir que, el lugar de la copia nos enviara el dato original. por lo tanto si se modifican dentro de la funcion asi se quedan. 


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