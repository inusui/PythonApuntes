from io import open
import pickle

class Pelicula:
    def __init__(self,titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print ("Se creo la pelicula", self.titulo)

    def __str__(self):
        return ("{} ({})".format(self.titulo, self.lanzamiento))

class Catalogo:

    peliculas = []
    def __init__(self):
        self.cargar()
    
    def agregar(self, add):
        self.add = add
        self.peliculas.append(self.add)
        self.guardar()
        

    def mostrar(self):
        if ( len(self.peliculas) == 0):
            print("Catalogo vacio")
            return
        else: 
            for i in self.peliculas:
                print(i)
    
    def cargar(self):
        fichero = open('catalogo.pckl' , 'ab+')#append binario + lectura
        fichero.seek(0) #como es append el puntero estara al final por ello se pone al inicio siempre
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print ("El fichero esta vacio")
        finally:
            fichero.close()
            print("Se han cargado {} peliculas".format(len(self.peliculas)))
        

    def guardar(self):
        fichero = open('catalogo.pckl' , 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()



c = Catalogo()
pelicula1 = Pelicula("Batman 2022", 120, 2022)

c.agregar( pelicula1 )
c.mostrar()