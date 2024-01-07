def par_o_impar(numero):
    r = numero %2
    if (r == 0):
        print ("PAR\n")
    else:
        print ("IMPAR\n")

par_o_impar(11)
par_o_impar(20)
par_o_impar(111)
par_o_impar(25)
par_o_impar(78)


def recortar(numero, minimo, maximo):
    if(numero < minimo):
        return minimo
    elif(numero > maximo):
        return maximo
    else:
        return numero