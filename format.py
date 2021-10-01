v = "Juanito"

n = 10

print ("Texto", v, " numero :", n)

#Formato de texto de las cadenas se pasa a una forma

c = "Texto {} y numero {}".format(v,n)

print ("\n", c)

#Cambiar orden que entran al "print"

print( "Alterando Orden por indice \n -> Texto {1} y numero {0}".format(v,n) )

#Referenciando don una clave


print( "Usando Variables \n -> Texto {text} y numero {num} \n Tambien se pueden poner varias veces \n {text} {text} {text}".format(text = v,num = n) )

#ordenando

print("Luego de esto hay 30 caracteres {:>30}".format("palabra"))
print("{:30} antes  de esto hay 30 caracteres ".format("palabra"))

print("Esta en el centro de 30 caracteres {:^30} si al centro ".format("palabra"))

#Truncamiento solo muestra 3 caracteres
print("Muestro 3 letras de la variable ->{:.3}".format("palabra"))

print("Espacios 30 a al derecha y 'truncamiento' ->{:>30.3}".format("palabra"))

#Alinear numeros. 
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#Format con Floats se rellenan con espacios

print("{:08.4f}".format(3.1415926))
print("{:7.4f}".format(465.12228))


nombre ="RIcardo"
cadena = f"HOlanda {nombre}"
print (cadena)