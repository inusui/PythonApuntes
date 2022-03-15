import random
import math

def leer_numero(ini, fin, mensaje):
    while (True):
        try:
            valor = int ( input(mensaje) )
            #valor = random.randrange(ini, fin + 1)
        except:
            print("Numero no valido")
        else:
            if (valor >= ini and valor <= fin):
                break

    return valor


def generador():
    numeros = leer_numero(1,20,"Cuantos numeros quieres generar? [1-20] ")
    modo = leer_numero(1,3,"Como quieres redondear los numeros?\n[1]Al alza\n[2]A la baja\n[3]Normal: ")
    
    lista = []
    for i in range(numeros):
        x = random.uniform(0,101)
        print("numero antes de redondear", x)
        if (modo == 1 ):
            x = math.ceil(x)
        elif (modo == 2 ):
            x = math.floor(x)
        elif (modo ==3):
            x = round(x)
        print("Numero Redondeado", x)
        lista.append(x)

    print(lista)

generador()