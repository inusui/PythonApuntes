# Programacion Estructurada
 
clientes = [
    {'Nombre': 'Ricardo', 'Apellido' : 'Dominguez', 'ID': 1},
    {'Nombre': 'Jeni', 'Apellido' : 'Saavedra', 'ID': 2}

]

def Mostrar(clientes, ID):
    for c in clientes:
        if (ID == c['ID']):
            print('{} {}'.format( c['Nombre'] , c['Apellido'] ) )
            return
    print("No encontre cliente") 

def borrar(clientes, ID):
    for i,c in enumerate(clientes):
        if(ID == c['ID']):
            del( clientes[i] )
            print(str(c), "> Borrado")
            return
    print("Cliente no encontrado")

borrar(clientes, 1)
