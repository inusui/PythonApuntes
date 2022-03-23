#Ejercicio 2 de manejo de ficheros
'''
| Comprobar si el fichero existe, si no crearlo con el numero 0 |  *
| if existe se lee el valor del contador                        |
    | Se envia argumento [inc] para incrementarlo 1, mostrar    |
    | Se envia argumento [dec] se decrementa 1 , mostrar        |
    | Si no se envia argumento solo se muestra                  |
| Finalmente se guarda el nuevo valor de nuevo en el fichero    |
| Utiliza excepciones en caso que sea necesario con el error    |
| Error: Fichero Corrupto                                       |
'''
# code
from io import open
import sys #Prque va a usar argumentos en el script
import os

fichero = open("contador.txt","a+")#si no existe lo crea
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)
fichero.close()

try:
    contador = int(contenido)
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador +=1
        elif sys.argv[1] == "dec":
            contador -=1
    print(contador)
    fichero = open("contador.txt", "w")
    fichero.write( str(contador))
    fichero.close()

except Exception as e:
    if os.path.exists("contador.txt"):
        os.remove("contador.txt")
        print("Archivo corrputo, borrando")
    
    