###1            Format

'''
print ("{:>20}".format("Hola Mundillo"))
print ("{:.3}".format("Hola Mundillo"))
print ("{:^20.1}".format("Hola Mundillo"))

print ("{:05d}".format(150))
print ("{:7d}".format(7887))
print ("{:07.3f}".format(20.02))

'''

###2    
'''
import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columna = int(sys.argv[1])

    if filas < 1 or filas > 9 or columna < 1 or columna > 9:
        print("Flas o columnas incorrectas")
    else:
        for f in range (filas):
            print("")
            for c in range (columna):
                print(" * ", end='')
else:
    print("Error\n Ejemplo:tabla.py[1-9] [1-9]")

'''
###3 

import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])

    if numero < 0 or numero > 9999:
        print("Esta ma, sobre pasaa el rango")
    else:
        ## la logica del programa
        cadena = str (numero)
        long = len(str (numero) )

        print (long)
        for i in range(long):

            print( "{:04d}".format( int(cadena[long - 1 - i]) * 10 ** i ) )
            num = long -1 -i
            
            print (num , 10 ** i )
    
else:
    print("escribe bien")
