## Lo basico
import sqlite3 

conexion = sqlite3.connect("nombre_basededatos.db") #coneccion 

cursor = conexion.cursor() #Se necesita para escribir SQL

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(20), edad INTEGER, email VARCHAR(30) )") #Consulta SQL

#cursor.execute("INSERT INTO usuarios VALUES ('Ricardo',25,'inusui@mail.com')")

#recuperar el registro
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchone() #pasar todos los cursores 
print(usuarios)

InsertUsuario = [
    ('Mario',20,'mario@mail.com'),
    ('Lucho',5,'lucho@mail.com'),
    ('Venus',2,'venus@mail.com'),

]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", InsertUsuario)

usuarios = cursor.fetchall()
c=0
for usuario in usuarios:
    c+=1
    print(c, usuario)


conexion.commit() #para confirmar los datos que entran

conexion.close()