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


# Buscar patrones por letras repetidas. 

texto = "hla hola hoola hoooooooooooooooooooola holaaaaaaaaaaaaaaaaaaaa ola"

def buscar(patron, texto):
    for pat in patron:
        print (re.findall(pat, texto))
        if (len(re.findall(pat,texto)) > 1):
            print("Se encontro", len(re.findall(pat,texto)), "Veces")
        else:
            print("Se encontro", len(re.findall(pat,texto)), "Vez")

patronesABuscar = ['hla', 'hola', 'hoola']
buscar(patronesABuscar,texto)


#Meta-Caracter * 
# null o mas de 1
print( "\nNinguna o mas veces de la letra de la izquierda")
patronesABuscar = ['ho', 'ho*', 'ho*la']
buscar(patronesABuscar, texto)

#Meta-caracter +
# Una o mas repeticiones de la letra de la izquierda
# desde 1

print("\nMeta-Caracter +")
patronesABuscar = ['ho*', 'ho+']
buscar(patronesABuscar, texto)

#Meta Caracter ?
# Una o ninguna repeticion del caracter a su izquierda
# 1 o null
print("\nMeta-Caracter ?")
patronesABuscar = ['ho*', 'ho?', 'ho?la']
buscar(patronesABuscar, texto)

#Numero x de repeticiones
print("\nX cantidad de Repeticiones con {n}")
patronesABuscar = ['ho{0}la'] #la O se reptite 0 veces
buscar(patronesABuscar, texto)

# Rango de busqueda 

print("\nUn rango de veces que me aparezca el caracter anterior")
patronesABuscar = ['ho{0,2}la'] #Aparezca la o de 0 hasta 2 veces
buscar(patronesABuscar, texto)


#! Caracteres Regulares III
#Patrones con diferentes Conjuntos de Caracteres
print("\n\nPatrones en conjunto de Caracteres")
texto = "hala hela hila hola hula"
patronesABuscar = ['h[ou]la']#Buscara en la posicion 2 los caracteres que coincidan con lo que esta dentro del []
buscar(patronesABuscar,texto)

#Patrones diferentes + cantidad
print("\nBuscar segun conjunto y con Meta-caracteres")
texto = "haala heeeeela hiiiiiila hooooooooola"
patronesABuscar = ['h[ae]la', 'h[ae]*la', 'h[io]{3,9}la']
buscar(patronesABuscar,texto)

#Busqueda contraria con ^
print("\nBuscar segun negar un caracter [^]")
texto = "hala hela hila hola hula"
patronesABuscar = ['h[^o]la'] 
#Se niega a la o
buscar(patronesABuscar,texto)


#Busqueda con [-] Rangos especiales 
'''
[A-Z] Cualquier caracter en mayusculas
[a-z] Caracter alfabetico en minusculas
[A-Za-z] o [A,z] Caracter alfabetico minuculas o mayusculas
[0-9] Caracter Numerico
[a-zA-Z0-9] Cualquier Caracter no especial
'''
print("\nBuscar Segun rangos  [^]")
texto = "hola h0la Hola Mola m0la M0la ;;"
patronesABuscar = ['h[a-z]la' , 'h[0-9]la', '[A-z]{4}', '[\W]{2}' ]
                                            #Cualquier cosa con mas de 4 letras
buscar(patronesABuscar,texto)

# Codigo Escapado o con \
'''
Caracteres Escapados 
\d Numerico         \D No Numerico          \s Espacio en Blanco
\s no Espacio en blanco     \w Alfanumerico     \W No alfanumerico
'''

print("\nCon codigos 'Escapado\'")
texto="Este curso de python 3 lo estoy haciendo en el 2022, me siento un anciano pip"
patronesABuscar = ['\d','\d+','p[\D]', '\D+']
# if \S+ o \w+ todas las palabras
buscar(patronesABuscar,texto)