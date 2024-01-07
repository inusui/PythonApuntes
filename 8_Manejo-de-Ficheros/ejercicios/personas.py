#Ejercicio #1 de manejo de ficheros.
'''
| Leera los datos de un archivo de texto.               |
| Transforma cada fila en un diccionario.               |
| Ese dicionario se añadira a la lista llamada personas |
| Recorrer las personas de la lista.                    |
| Muestra los datos.                                    |
'''# Diccionario en el siguiente Orden [id, nombre, apellido, nacimiento]


# Code
from io import open
personas =[]
fichero = open('personas.txt', 'r', encoding='utf8')

lineas = fichero.readlines()
fichero.close()

for linea in lineas:
    
    campos = linea.replace("\n","").split(";")
    
    persona = {"id":campos[0] , "nombre": campos[1], "apellido": campos[2], "nacimiento":campos[3]}
    personas.append(persona)

for p in personas:
    print(("|Id:{} |nombre: {} {} => {}".format(p["id"],p["nombre"],p["apellido"],p["nacimiento"] )).title())