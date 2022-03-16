from io import open
#para trabajar con el open 

texto = "contexto\notra linea contexto\n"

fichero = open('fichero.txt', 'w')

fichero.write(texto)

fichero.close()

#Leer fichero

fichero = open('fichero.txt', 'r')
texto = fichero.read()
print(texto)
fichero.close()

#? reemplazar elemento de un fichero

fichero = open('fichero.txt', 'r')
lineas = fichero.readlines()
print(lineas[0])

#Abrir en modo append
fichero = open('fichero.txt' , 'a')
fichero.write('3era linea del fichero\n')
fichero.close()

fichero = open('fichero.txt', 'r')
l = fichero.readline()

with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)

# Punteros => apuntar al caracter 10
fichero = open('fichero.txt' , 'r')
fichero.seek(14)
print("usando seek", fichero.read())
fichero.seek(0)

print("<leer 5 caracteres=>", fichero.read(5))
print("<luego de leer, el resto=>", fichero.read())

# leer fichero desde la mitad
leer = fichero.read()
fichero.seek( len( leer ) / 2 ) #Pongo el puntero a la mitad segun len fichero.read()
print("leer fichero desde la mitad,\n", fichero.read() )
fichero.seek(0) # nos ponemos al inicio del fichero

# leer desde la segunda linea
fichero.seek(   len(fichero.readline()))
print("<Sin leer la primera linea> : " , fichero.read())

fichero.close()
#para cerrarlo


fichero = open('fichero.txt', 'r+') #lectura mas escritura
#es como un append pero con el puntero al inicio
fichero.write('cualquier cosa')
fichero.close()

#modificar linea en especial

fichero = open('fichero.txt', 'r+')
lineas = fichero.readlines()
print( linea )

#modificar de la 3era linea

lineas[1] = "Ahora es otra cosa heho\n"
print(lineas)

fichero.seek(0)
#porque el puntero esta al final luego de leer todas las lineas

fichero.writelines(lineas)
fichero.close()
