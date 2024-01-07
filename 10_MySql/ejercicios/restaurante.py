# Crear planos de un restaurante
'''
#   Uso el Sleep() para poder hacer el programa de mas simple visualizacion
#   Hasta para mi mismo, me costaba ver donde estana el output en el terminal 

'''
import sqlite3
import time #Por el Sleep() al salir 😂
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()



def crear_bd():
        
    
    try:
        cursor.executescript('''
        CREATE TABLE categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(10) UNIQUE NOT NULL
        );
        CREATE TABLE plato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        )
        ''')
    except sqlite3.OperationalError:
        print ("La tabla Categoria ya Existe")
    else:
        print("Las tablas Categoria y Plato se han Creado correctamente")

    conexion.close()

def agregar_categoria():
    categoriaNueva =  input("Nombre de Categoria:\n>")
    if categoriaNueva != "":
        try:
            cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(categoriaNueva))
        except sqlite3.IntegrityError:
            print("Error: La Categoria {} Ya fue creada con aterioridad".format(categoriaNueva))
        else:
            print("Categoria {} Creada Satisfactiamente".format(categoriaNueva))
        conexion.commit()
        time.sleep(3)
    else:
        print("No puede ser null")

def agregar_plato():
    print("Elija una de las siguientes Categorias")
    cursor.execute("SELECT * FROM categoria")
    lista = cursor.fetchall()
    i=0
    for a in lista:
        print ("[{}] ".format(i+1) , lista[i][1])
        i += 1
    opcion_cat = int(input(">"))
    addplato = input("\nCual es el nombre del plato a Anexar\n>")
    try:
        cursor.execute('''
        INSERT INTO plato VALUES (null, '{}', '{}' )
        '''.format(addplato , opcion_cat))
    except sqlite3.IntegrityError as E:
        print("\nError￣へ￣" , type(E).__name__ , "\nEl platao '{}' Ya existe".format(addplato))
    else:
        print("Plato {} anexado al menu satisfactoriamente".format(addplato))
    conexion.commit()
    time.sleep(2)

def mostrarMenu():
    cursor.execute('''
    SELECT * FROM categoria
    ''')
    
    allcategories = cursor.fetchall()
    for categorie in allcategories:
        print(categorie[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categorie[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))

    
    print("Saliendo de la funcion")
    time.sleep(3)
#crear_bd()

#Menu del programa
while True:
    print("\nBienvenido al gestor del Restaurante")
    
    opcion = input("\nIntroduce una opcion\n[1] Agregar una Categoria\n[2] Agregar Plato\n[3] Mostrar Menu\n[4] Salir del Programa\n>")
    if opcion == "1":
        agregar_categoria()
    elif opcion =="2":
        agregar_plato()
    elif opcion == "3":
        mostrarMenu()
    elif opcion =="4":
        print("Nos Vemos!")
        time.sleep(1)
        break
    else:
        print("\nOpcion Incorrecta")
        
conexion.close()