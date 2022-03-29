import pickle

lista = [1,2,3,4,5]

fichero = open('lista.pckl','wb')
#wb porque es binario, escritura binaria

pickle.dump(lista, fichero)#volcar dentro del fichero

fichero.close()

fichero = open('lista.pckl', 'rb')
print("Dentro de pickle", pickle.load(fichero))
#una vez se hace el load, el puntero esta al final. hay que volver a pocisionarse al inicio

fichero.seek(0) #puntero al 0
print("La lista pickle", pickle.load(fichero))

fichero.close()


class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

nombre = ['Ricardo', 'Jeniffer', 'Venus']

personas = []

for n in nombre:
    p = Persona(n)
    personas.append(p)

fichero = open ('personas.pckl', 'wb')
pickle.dump(personas, fichero)

fichero.close()

fichero = open('personas.pckl', 'rb')
personas = pickle.load(fichero)
fichero.close()

for i in personas:
    print(i)