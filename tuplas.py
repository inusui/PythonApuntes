tuplas = (100,100 , "Hola", [1, 2, 3], -50)

print (tuplas
        ,"\nPuede usar Slicing", tuplas[2:]
        ,"\nOtra lista del Slicing, Una lista dentro de la otra lista", tuplas[2][-1]
        ,"\nSi se puede mostrar su longitud", len(tuplas)
        ,"\nLo que mide la lista interna", len(tuplas[2])
        )

#Index para buscar el elemento y si no lo encuentra devuelve un error

print ("Lo de dentro del index es el valor que se busca dentro de la Lista \nEl valor 100 se encuentra en el indice>",tuplas.index(100)
        #Count
        ,"\nCantidad de elementos dentro de la Lista", tuplas.count(100)

        )

"""
# completa el ejercicio
print(tupla[-1])
print(len(tupla))
print(tupla.index(123))
print(tupla[:3])
print(tupla[4])
print(tupla.count(4))"""