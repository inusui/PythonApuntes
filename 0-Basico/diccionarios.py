#cada elemento es unico, solo puede existir uno. en el diccionario. "arreglos asociativos en otros lenguajes"

vacio = {}

print(type(vacio)) #para ver que tipo es el elemento

Colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green'}

print (Colores['amarillo'])

numeros = {10:'Diez', 20:'Veinte'}

print("Esto se refiere no al indice si no al la palabra clave: ", numeros[10])

NumeroTelefonoPerUser = {'Ricardo' :'910-7548', 'Anastasio':'11111111'}
print("Lista Original:" , NumeroTelefonoPerUser['Ricardo'])
NumeroTelefonoPerUser['Ricardo'] = '62809234'

print("\nLuego de cambiar" , NumeroTelefonoPerUser['Ricardo'])

del(Colores['amarillo']) #Eliminar el amarillo que esta dentro del diccionario 


edades = {"Ricardo":24 , "Jeniffer":23}

edades["Ricardo"] += 1
print("Mi Edad luego de sumarle 1 > " , edades["Ricardo"]
    , "\nSumando las edades de Ricardo y Jeni" , edades["Ricardo"] + edades["Jeniffer"])

#por For no se accede a los valores, solo a las claves, como se pueden sacar los valores

for clave in edades:
    print(clave, edades[clave])

# con este se muestra la llave y su valor, pero no es la forma correcta, la forma correcta seria... con un metodo interno de los diccionarios, similar a enumerate

for clave, valor in edades.items():
    print("\n Similar al de arriba pero con mejor Sintaxis", clave, valor)

'''cabe destacar que clave y valor no son variables dentro de la funcion por lo tanto simplemente son nombres los cuales se pueden reemplazar por cualquier otro nombre. 
'''

#Utlizar en conjunto con las Listas, Listas de personajes, con nombre, raza, stats, etc. 

personajes = []

pj = {'Nombre':'Inusui', 'Clase':'Mago del Vacio', 'Ataque':10,'Defenza':5, 'AGI':10}
personajes.append(pj)

pj = {'Nombre':'Hinasuma', 'Clase':'Mago de Hielo', 'Ataque':11,'Defenza':4, 'AGI':9}
personajes.append(pj)
pj = {'Nombre':'Venus', 'Clase':'Guerrera de Martillo', 'Ataque':5,'Defenza':10, 'AGI':5}
personajes.append(pj)


for pj in personajes:
    print("\nNombre:", pj['Nombre'], "Clase:", pj['Clase'],"Ataque:", pj['Ataque'] ) 