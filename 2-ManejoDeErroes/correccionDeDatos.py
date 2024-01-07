while (True):
    try:
        n = float(input("Dame numericos"))
        m = 10
        print ('''{}/{} = {} '''.format(n,m,n/m))
        
    except:
        print("Error")
    else: # Solo se ejecutara si no hay ninguna Exception
        print("NICE")
        break
    finally:#Siempre salgo haya o no error
        print("Fin de la iteracion")