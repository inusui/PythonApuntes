from tkinter import E


def ejercicio1 ():
    try:
        resultado = 10 / 0
    except Exception as e:
        print ("Error, no se puede dividir entre 0\n")

def ejercicio2():
    try:
        lista = [1, 2, 3, 4, 5]
        lista[10]
    except IndexError:
        print("Error, index fuera del rango")
    except Exception as e:
        print ( type(e).__name__ ,"\n", e)
    
def ejercicio3():
    try:
        colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
        print ( colores['blanco'])
    except KeyError as e:
        print ('Estas intentanto imprimir una key que no existe\nRazon=> [{}]'.format(str(e)))
    except Exception as E:
        print ("Error\n", type(E).__name__, "\n", type(E))

def ejercicio4():
    try:
        resultado = 15 + "20"
        print (resultado)
    except TypeError as E:
        print ("Error no puedes multiplicar un String con un Integger\n" , E)
    except Exception as E:
        print (type(E).__name__)



def ejercicio5(lista,el):
    try:
        if el in lista:
            raise ValueError
        else: 
            lista.append(el)
            print (el," añadido a la lista\n",lista)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados => [{}].".format(el))
    except Exception as E:
        print (type(E).__name__)
elementos = [1,5,-2]

ejercicio5(elementos,10)
ejercicio5(elementos,-2)
ejercicio5(elementos,"Hola")