import sys

'''
print ("Buenas tardes")

print (sys.argv)
'''
if len(sys.argv) == 3:
    texto = sys.argv[1]

    repeticiones = int(sys.argv[2])

    for r in range (repeticiones):
        print(texto)
else:
    print("No se cumplio \n[R] Ejemplo: py salidad.py 'Juan' 5\nUsa Comillas dobles no detecta correctamente las simples.")

# Se comprueba antes de entrar al script para prevenir errores. por ello el if