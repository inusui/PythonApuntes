from operaciones import * 

a , b , c , d = (10, 5, 0 , "Hola")

print("{} + {} = {}".format(a, b ,  Suma(a, b)))

print("{} - {} = {}".format(b ,d , Resta(b,d) ) )
print("{} * {} = {}".format(b,b , Producto(b,b)))
print("{} / {} = {}".format(a,c , Division(a,c)))
