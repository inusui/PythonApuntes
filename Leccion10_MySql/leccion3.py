import sqlite3

conexion = sqlite3.connect("usuarios_autoincrementable.db")
cursor = conexion.cursor()

cursor.execute('''
SELECT * FROM usuarios WHERE edad=5 ''')

usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

#cursor.execute('''UPDATE usuarios SET nombre='Mario Acosta' WHERE dni='a1'  ''')

#Borrar
cursor.execute('''DELETE FROM usuarios where dni='a1' ''')


#lo Agrego denuevo
cursor.execute("INSERT INTO usuarios VALUES (null,'a1','Mario',20,'mario@mail.com')")

conexion.commit()
conexion.close()