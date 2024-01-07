# Operadores Encadenados
'''
* Se pueden encadenas multiples operadores
'''
a = 1 < 2 and 2< 3
#Se puede expresar 
a = 1 < 2 < 3 #se omite el and y el segundo 2, se encadena porque a lo que se compara es igual

a = 3 > 2 > 1 
print (a)

numero = 35

'''
if numero >= 0 and numero <=100:
    print("el numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("el numero {} No se encuentra entre 0 y 100".format(numero))
'''

if 0 <= numero <=100: #debe estar en el centro el comun 
    print("el numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("el numero {} No se encuentra entre 0 y 100".format(numero))

    