def For():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    print("\nLista Original", numeros,"\n")
    for indice, numero in enumerate(numeros):
        numeros[indice]*=10
        print("Iteracion N",indice," Es ",numero) 
        # indice+=1         Si uso enumerate no lo necesito, es una linea de codigo que me ahorro. 
    print ("Luego del Ciclo\n" ,numero, numeros)

def ForEnumerate():
    elementos = ["Hola", 1, 2, [1,2,3]]
    for i,e in enumerate(elementos):
	    print(i, e)
         
def ForIn():
     tabla = [
          [0, 0, 0],
          [1, 1, 1],
          [2, 2, 2]
     ]
     print("Por cada columna dentro de la fila de la tabla")
     for fila in tabla:
        #print(fila)
        for columna in fila:
              print(columna, end=" ")
        print()
        
def While():
     a = 0
     print("Ciclo While")
     while(a < 2):
        a = a + 1
        print("Iteracion: {}".format(a))    

def cubo():
     tabla = [
          [0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]
     ]
     tabla2 = [
          [9, 10, 11],
          [12, 13,14],
          [15, 16, 17]
     ]
     cubo = [
          tabla, tabla2
     ]
     print(cubo[0][1][0]) # Print 3
     
     for profundidad, tabla in enumerate(cubo):
          for altura, fila in enumerate(tabla):
               for ancho, columna in enumerate (fila):
                    print(cubo[profundidad][altura][ancho], end=" ")
          print("")

def ejericioBuclesAnidados():
    matriz= [
      [8,  7,  0],
      [34, 2, -1],
      [5, -5, 12]
    ]
    for fila in matriz:
        for columna in fila:
            if (columna % 2 == 0):
              print("la fila es par... {} par".format(columna))
            else:
              print("lo que sobra... {}".format(columna))

ejericioBuclesAnidados()