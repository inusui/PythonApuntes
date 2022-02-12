def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print (numero)
        cuenta_atras(numero)
    else: print("EEEEEEEEEXPXXXXXXPLOOOOOOOOOOOOOOOOOOOOOOOOOOOOSIIIIIIIIIIIIIION")
    print ('''Acabo la funcion con el numero:{}'''.format(numero))

cuenta_atras(15)

def factorial(numero):
    print ("\nValor inicial =>", numero)
    if numero > 1:
        numero *= factorial(numero - 1)
    print ("\nValor Final =>", numero)
    return numero

print (factorial(5))