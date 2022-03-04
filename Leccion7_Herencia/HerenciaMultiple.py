class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("este metodo lo heredo de A")

class B:
    def __init__(self):
        print("Soy de Clase B")
    def b(self):
        print ("Este metodo lo Heredo de B")

class C(B, A):
    def c (self):
        print ("Este metodo es de C")
         

c = C()
print ( c )

print (c.a())

print(c.b())

print (c.c())