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

#   Argumenos y parametros Indeterminados

def indeterminados_posicion(*args): #Parametro Iterable se lo pone un * y por regla general se le llama args.
    print ("Imprimiendo todo lo que me mandan", args) #  Se crea una Tupla

   #Recorriendolo
    for arg in args:
        print ('''Imprimiendo segun indice   {}'''.format(arg))
    #Aqui arriba lo que hace es recorrerlo por indice e imprimiendolo. 

indeterminados_posicion(5,"Juan",[1,2,3,4,5])

# Argumentos por nombre, por clave. (OYA)

def indeterminados_porNombre (**kwargs):     #Se le indica con 2 ** y com palabra clave se usa kwargs
    for kwarg in kwargs:
        print ('''\nPor Defecto solo muestra las claves {0}
Entonces se Agrega el keyword, pasandole el indice {1}
De Esta manera Quedaria: Llave: {0}  Valor:{1}\n'''.format(kwarg, kwargs[kwarg]))

indeterminados_porNombre(c=4, cadena="hola")

# Una super funcion 
def super_funcion(*argumentos, **argumentosConClave):
    total = 0
    for argumento in argumentos:
        total =+ argumento
    print ("\nSumatorio indeterminado es: {}".format(total))
    for argumento in argumentosConClave: #tambien le puedo llamar diccionario
        print("\n{}:{}".format(argumento, argumentosConClave[argumento]))

super_funcion(10,50,-1,1,56, nombre = "Ricardo", edad = 27)