numeros = [1,2,3,4,5,6,7,8,9,10]

print("\nLista Original", numeros,"\n")
for indice,numero in enumerate(numeros):
    numeros[indice]*=10
    print("Iteracion N",indice," Es ",numero) 
    # indice+=1         Si uso enumerate no lo necesito, es una linea de codigo que me ahorro. 
print ("Luego del Ciclo\n" ,numero, numeros)

