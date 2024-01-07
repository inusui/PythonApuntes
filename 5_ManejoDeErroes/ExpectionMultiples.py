try:
    n = float (input("Dame un numero "))
    print (5/n)
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debe introducir un numero")
except ZeroDivisionError:
    print("No se puede dividir entre 0 ")
except Exception as e:
    print( type(e).__name__ ,"\n", e)