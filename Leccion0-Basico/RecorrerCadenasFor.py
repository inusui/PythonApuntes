cadena = "Holanda juan felipe"
for caracter in cadena:
    print(caracter)                   #caracter como variable temporal donde se guarda el caracter a usar. 

###### modificando una cadena con el for
cadenaModificada =""
for caracter in cadena:
    cadenaModificada += "*"
print(cadena, "\n", cadenaModificada)


"""Rango dentro de un ciclo for.        P
Para de este rango a este otro """

for i in range(1, 12):
    print(i)

print( list(range(10)) )