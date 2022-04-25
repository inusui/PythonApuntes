# Expresiones Regulares. 

'''
* Son conocidas como Regex o regexp son patrones de busqueda definidos con una sintaxis formal. 
Siempre que se sigan sus reglas podemos realizar busquedas simples o avanzadas que se utilizan con otras funciones. 



'''
import re

#Funcion serarch, un patron en una cadena

texto = "En esta cadena se encuentra una palabra magica"
print(
    re.search('magica', texto)
    #Si no devuelve nada, es que no encontro nada. 
)
encontrado = re.search('magica', texto)
if encontrado is not None:
    print("Se encontro la palabra {}\n".format(encontrado))
else:
    print("No se encontro")

#no retorna un true o un false, su retorno es un objeto re o null

print(encontrado.start(), "# Me da un 40, eso quiere decir que la palabra encontrada inicia en el caracter 40",
"\nAcaba en el caracter:", encontrado.end(),
"\nTupla con las posiciones donde inicia y termina", encontrado.span(),
"\nUna variable String donde recupera la frase que se ha utilizado", encontrado.string, "     # Va sin (), no es una funcion."

)

#Funcion Match.
'''
No servira para buscar un patron al principio de la cadena. 
'''
texto = "Holanda mundillo"
seEncuentra = re.match("Holanda", texto)
print("\nSi devuelve un objeto es poque lo encontro", seEncuentra

)

#Usando Split para dividir la Cadena
texto = "Vamos Dividir esta Cadena"
encontrado = re.split(" ",texto)
print(encontrado)


#re.sub para substituir, para substituir todas las coincidencias.
texto = "Hola Juancito"
print( 
    re.sub("Hola","Adios",texto)
    #DEvuelve la cadena ya cambiada
    )

#findall, buscar todas las coincidencias en una cadena de texto. 

texto = "hola adios hola hola hola hello bye"
#todas las coincidencias de la palbra hola
print(
 re.findall("hola",texto),
 #DEvuelve una lista con todas las coincidencias. 
 "\nInteresante, si uso un len(), me dice la cantidad", len(re.findall("hola",texto)),
 "\nPara buscar varias alternativas '(hola|hello)'", re.findall("(hola|hello)",texto)
)