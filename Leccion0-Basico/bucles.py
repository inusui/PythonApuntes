def For():
    numeros = [1,2,3,4,5,6,7,8,9,10]

    print("\nLista Original", numeros,"\n")
    for indice,numero in enumerate(numeros):
        numeros[indice]*=10
        print("Iteracion N",indice," Es ",numero) 
        # indice+=1         Si uso enumerate no lo necesito, es una linea de codigo que me ahorro. 
    print ("Luego del Ciclo\n" ,numero, numeros)

def ForEnumerate():
    elementos = ["Hola", 1, 2, [1,2,3]]
    for i,e in enumerate(elementos):
	    print(i, e)
         
def While():
     a = 0
     while(a < 2):
        a = a + 1
        print("Iteracion: {}".format(a))

While()