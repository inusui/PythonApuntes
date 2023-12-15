def Suma(a,b):
    try:
        r = a + b

    except TypeError:
        return ("Error: Tipo de dato no valido")

    except Exception as e :
        return (e)
    else:
        return r

def Resta (a,b):
    try:
        r = a - b

    except TypeError:
        return ("Error: Tipo de dato no valido")

    except Exception as e :
        return (e)
    else:
        return r

def Producto (a,b):
    try:
        r =a * b 

    except TypeError:
        return ("Error: Tipo de dato no valido")

    except Exception as e :
        return (e)
    else:
        return r

def Division(a,b): 
    try:
        r= a / b

    except TypeError:
        return ("Error: Tipo de dato no valido")

    except ZeroDivisionError:
        return ("Error:no es posible dividir entre 0")

    except Exception as e :
        return (e)
    else:
        return r



