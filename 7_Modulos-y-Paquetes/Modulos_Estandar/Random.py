import random
#aleatorios

print (random.random()) #numero random ente >=0 y < 1

print(random.uniform(1,10)) #numero mayor o igual que 1 y menor a 10

print(random.randrange(10)) # >=0 y <10

print(random.randrange(0,101, 2)) #entre >=0 y <101 solo los multiplos de 2 

#colecciones
c = "Hola mundillo"

print(random.choice(c)) #Elige caracter aleatorio dentro de c 

l = [1,2,3,4,5,6]
print(random.choice(l))

#baraja de forma aleatoria y los mantiene guardados
random.shuffle(l)  #no funciona con str
print( "la lista desordenada", l)

print(random.sample(l,2)) #Escoje de la lista 2 elementos