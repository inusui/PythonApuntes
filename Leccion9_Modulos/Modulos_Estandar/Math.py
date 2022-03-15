import math

pi = 3.14159

print ("Redondeo", round(pi))

print("Redondeo a la baja: ", math.floor(pi)) #siempre se reondea hacia abajo

print("Redondea hacia arriba: ", math.ceil(pi)) #Siempre hacia arriba

print ("Valor absoluto" , abs(-10)) #Valor absoluto -> Distanicia entre -10 al 0? 

n= [0.9999999999999999999, 1,2,3]
print ("Elementos sumados con la libreria math", math.fsum(n))

print("devuelve siempre el entero" , math.trunc(50.45648946))

print("Potenciacion ", math.pow(2,5))

print("Raiz cuadrada", math.sqrt(9))

print("Constantes", math.pi, "\nla e", math.e)