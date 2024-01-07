from copy import copy


def e1():
    texto = "un dia que el viento sopla con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondio otro monje#ni las banderolas ni el viento, lo que se mueve son nuestras mentes -dijo el maestro"
    textoSpliteado = texto.split("#")
    
    #Asi lo hice yo 
    print (textoSpliteado[0].capitalize(),"...")
    i = 1
    for i in textoSpliteado:
        print("-",i.capitalize() + ".")

    #Asi lo hizo el profesor
    for i, linea in enumerate(textoSpliteado):
        textoSpliteado[i] = linea.capitalize()
        if i == 0:
           textoSpliteado[i] = textoSpliteado[i] + "..."
        else:
            textoSpliteado[i] =  "- " + textoSpliteado[i] +"."
    for linea in textoSpliteado:
        print(linea)
    

def modificar (NumList):
    CopiaLista = copy(NumList)

    #Borrar los Elementos Duplicados
    CopiaLista = list(set(NumList)) #al convertir en conjunto se borran los duplicados
    NumList = list(set(NumList))
    NumList.sort(reverse=True)
    
    print(CopiaLista)

    #Ordena la lista de mayor a menor
    CopiaLista.sort(reverse=True)
    print("Lista Ordenada", CopiaLista)

    #Eliminar todos los numeros impares
    
    '''for i in CopiaLista:
        if i % 2 != 0:
            CopiaLista.remove(i)'''

    #Agrega a la lista solo los pares
    CopiaLista.clear()
    for i in NumList:
        if i % 2 == 0:
            CopiaLista.append(i)
    
    print (CopiaLista)
    #Sumar todos los elementos que quedan en la lista
    suma = sum(CopiaLista)
    print (suma)

    #la suma se inserta al indice 0
    CopiaLista.insert(0,suma)
    print(CopiaLista)
    return CopiaLista

lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
listaModificada = modificar(lista)
print(listaModificada[0] == sum(listaModificada[1:]))