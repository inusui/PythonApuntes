class Galleta():
    chocolate = False
    def __init__(self, sabor= None, forma = None):#se ejecuta al crear un nuevo Objeto
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("se acaba de crear una galleta de {} y {}.".format(sabor, forma))
        else:
            print("se creo una galleta sin elementos")
    
    def chocolatear (self):
        self.chocolate = True

    def tiene_chocolate (self):
        if self.chocolate:
            print("Galleta con Chocolate")
        else:
            print("No tiene chocolate ")


#galleta1 = Galleta()

#Metodos especiales
class Pelicula:
    #Metodo Constructor
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se a creado la pelicula", self.titulo,"\n")
    
    #Destructor de Clase
    ''' def __del__ (self):
        print("Se esta borrando la pelicula", self.titulo)'''
    
    def __str__(self):
        return "{} lanzada el {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion) + "\n"

    '''def __len__ (self):
        return self.duracion'''

class Catalogo:
    peliculas = []
    def __init__(self, peliculas = [] ):
        self.peliculas = peliculas

    def agregar (self,p):
        self.peliculas.append(p)

    def mostrar (self):
        for p in self.peliculas:
            print(p)

p1 = Pelicula("Harry", 120, "Hoy")
c = Catalogo([p1])

c.agregar(Pelicula("Lord of the Ring", 150 , 2003))

c.mostrar()
# print (str(p1))

# print(len(p1))