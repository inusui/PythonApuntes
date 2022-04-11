import sqlite3


#Conexiones

conexion = sqlite3.connect("usuarios_autoincrementable.db")
cursor = conexion.cursor()

'''
# Llaves Primarias
'''
cursor.execute('''
CREATE TABLE  IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR(9) UNIQUE,
    nombre VARCHAR(16),
    edad INTEGER,
    email VARCHAR(50)
    )   
''')

InsertUsuario = [
    ('a1','Mario',20,'mario@mail.com'),
    ('b2','Lucho',5,'lucho@mail.com'),
    ('c3','Venus',2,'venus@mail.com'),
    ('d4','Jeniffer',25,'jeni@mail.com'),
]
cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", InsertUsuario)

cursor.execute("SELECT * FROM usuarios")

selectUsuarios = cursor
for usuario in selectUsuarios:
    print (usuario)


def oldcode():
    '''Codigo de la base de datos llamada usuarios'''
    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        marca VARCHAR(25) NOT NULL,
        precio FLOAT NOT NULL
    ) 
    ''')

    productos = [
        ('Teclado','Logitech', 19.95),
        ('Mouse','Redragon', 15.99)
    ]

    #cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
    #Se envia null el primer dato para que se autoincremente en la base de datos

    cursor.execute("SELECT * FROM productos")

    outputProductos = cursor
    for producto in outputProductos:
        print (producto)






#Cerrar conexion
conexion.commit()
conexion.close()