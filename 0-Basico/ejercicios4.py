#Ejercicio 1 
'''
usuarios = {"Marta", "David", "Elvira", "Juan","Marcos"}

administradores = {"Juan", "Marta"}

print ("Lista de Administradores", administradores, "\n")

administradores.discard("Juan") #Borrar elemento sin salir de el. 
administradores.add("Marcos")

print ("Lista de Administradores", administradores, "\n")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, " Es Administrador")
    else:
        print (usuario, " No es Administrador") 
'''

#Ejercicio 2
'''
caballero = {'vida' : 2, 'ataque' : 2, 'defensa': 2, 'alcance': 2}
guerrero = {'vida' : 2, 'ataque' : 2, 'defensa': 2, 'alcance': 2}
arquero = {'vida' : 2, 'ataque' : 2, 'defensa': 2, 'alcance': 2}

caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2 

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

print ("Clase Caballlero: ", caballero, "\nClase Guerrero: ", guerrero, "\nClase Arquero", arquero)

'''

#Ejercicio 3

tareas = [
    [6,'Distribucion'],
    [2,'Diseño'],
    [1,'Concepcion'],
    [7,'Mantenimiento'],
    [4,'Produccion'],
    [3,'Planificacion'],
    [5,'Pruebas'],
]

print("==Tareas Desordenadas==")

for tarea in tareas:
    print (tarea[0], tarea[1])

from collections import deque

tareas.sort()

cola = deque()
for tarea in tareas:
    cola.append(tarea[1])

print("\n==Tareas Ordenadas==")

for indicador in cola:
    print (indicador)

print("Proxima tarea a Realizar ", cola.popleft())