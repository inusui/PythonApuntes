##Ejercicio #1
'''
Numero1 = float(input("Introduce un Numero"))
Numero2 = float(input("Introduce otro numero"))

Seleccion = input ("""Ahora que quieres hacer con esos numeros? \n
1) Sumar
2) Restar
3) Multiplicar""")

if (Seleccion == "1"):
    print("La suma es: ", Numero1 + Numero2)
elif(Seleccion == "2"):
    print("LA resta es:", Numero1 - Numero2)
elif (Seleccion == "3"):
    print ("La Multiplicacion es: ", Numero1 * Numero2)
else:
    print ("Error no elegiste un numero del 1 al 3")
'''
##Ejercicio #2
'''
numero = 0
while numero % 2 == 0:
    numero = float(input("Introduce un numero impar para salir"))
print ("Saliste con exito")
'''

##Ejercicio #3
'''
print (list (range(0,101, 2)))
print ( sum(range(0 , 101 , 2)) )
    ##Ejercicio #3 con bucle

num = 0
sumatoria = 0
while num <= 100:
    if num % 2 == 0:
        sumatoria += num
    num +=1
print (sumatoria)
'''
## Ejercicio #4
'''
numeroTotal = int(input("Cuantos numeros quieres?: "))

suma = 0

for contador in range(numeroTotal):
    suma += float(input ("Introduce un numero: "))

print ("La media de " ,numeroTotal, " numeros es: ", suma / numeroTotal )
'''

#Ejercicio #5
'''
numero = [1, 3, 6, 9]

while True:
    nuemero = int (input ("Dame un numero del 0 al 9 "))
    if (nuemero >= 0 and nuemero <= 9):
        break
if nuemero in numero:
    print ("si esta yei")
else:
    print ("no ta en la lista" , numero)

'''

#Ejercicio #6
'''
print ("Primera Lista" , list (range(0 , 11 )))
print ("Segundo Lista", list (range(-10 , 1 )))
print ("Tercero Lista", list (range(0, 21, 2 )))
print ("Cuarto Lista" , list (range(-19 , 0 , 2 )))
print ("Quinta Lista" ,list (range(0 , 51, 5 )))

'''

#Ejercicio #7
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for letras in lista_1:
    if letras in lista_2 and letras not in lista_3:
        lista_3.append(letras)
        
print (lista_3)