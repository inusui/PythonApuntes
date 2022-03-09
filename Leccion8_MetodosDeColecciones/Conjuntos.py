c = set()
c.add(1)
c.add(2)
c.add(3)

print("Conjunto: ",c)

c.discard(1)
print(c)
c.add(1)

c2 = set()
#las colecciones estan referenciadas por tanto, no se pueden copiar asignando a otra variable.

c2 = c.copy()

c2.discard(1)
print(c2,c)

c2.clear()
print(c2)
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print("Es disjunto?", c.isdisjoint(c2))

print("Es un subconjunto O tiene algo parecido" , c3.issubset(c4))

print("Es un contenedor?", c4.issuperset(c2))

## metodos mas avanzados 

print(c.union(c2) ) #Solo se muestra no se asigna a ninguno

c.update(c2) #solo se le asigna a c
print( c , c2 )

C = {1,2,3}
print (c.difference(c2)) #solo muestra

c.difference_update(c2) #Asigna la diferencia a c
print (c)
c = {1,2,3}

print(c.intersection(c2)) #elementos en comun se le puede hacer un _update

'''cupdate = c.intersection(c2)
print(cupdate)'''

print(c.symmetric_difference(c2)) #Simetricamente diferente

