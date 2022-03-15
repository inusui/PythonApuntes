colores = {"amarillo" : "yellow", "azul": "blue", "verde" : "green"}

print( colores["amarillo"]) #print

print ( colores.get('negro','no esta')) #y si no esta...

print ( 'azul' in colores ) #Esta?

print(colores.keys()) #cuales son las llaves
print(colores.values())#Valores?

print(colores.items()) #todos los keys

for c in colores.keys():
    print(c)

for keys, item in colores.items():
    print(keys, " : " , item)


#sustraer el amarillo con pop
print(colores.pop('negro','no se encontro'))
print(colores)

#Vaciar con clear
colores.clear()
print(colores)