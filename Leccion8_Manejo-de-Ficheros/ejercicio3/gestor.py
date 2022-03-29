# Ejercicio #3
'''
|*************** añadir y borrar informacion de los personajes  *******************|
------------------------------------------------------------------------------------ 
| 2 Clases [Personaje]      [Gestor]                                               |
| [Personaje], crear personaje que seran las clases (caballero, guerrero, arquero) |
|       -  los valores de las estadisticas deben ser si o si mayor que 0           |
| [Gestor], Añadir Personajes, mostrarlos, borrarlos (a partir de su nombre)       |
|       - Si el personaje (clase) ya existe, no se creará                          |
------------------------------------------------------------------------------------
'''
from distutils.log import error
from io import open
import pickle

class Personaje:
    def __init__(self, clase = 0 , vida = 0 , ataque = 0 , defensa = 0, alcance= 0):
        if  vida <= 0 :
            self.no("vida")
        elif ataque <= 0:
            self.no("ataque")
        elif defensa <= 0:
            self.no(defensa)
        elif alcance <= 0:
            self.no ("alcance")
        else:
            self.clase = clase
            self.vida = vida
            self.ataque = ataque
            self.defensa = defensa
            self.alcance = alcance
            print ("Se creo la personaje", self.clase)

    def no(self, argumento):
        print("Error: El valor de {} debe ser mayor que 0".format(argumento))
        
    def __str__(self):
        return "{} [ Vida {}, Atk {}, Def {}, Alc {} ]".format(self.clase,  self.vida, self.ataque, self.defensa, self.alcance)
        

class Gestor:
    personajes=[]

    def __init__(self):
        self.cargar()

    def agregar(self, add):
        try:
            for pTemp in self.personajes:
                if pTemp.clase == add.clase:
                    return
            self.add = add
            self.personajes.append(self.add)
            self.guardar()
        except Exception as e:
            print("**************************************\nERROR: No puedo agregar a la clase si al crearla alguno de los valores es 0\n**************************************")

    def mostrar(self):
        if ( len(self.personajes) == 0):
            print("Gestor vacio")
            return
        else: 
            for i in self.personajes:
                print(i)
    
    def cargar(self):
        fichero = open('personajes.pckl' , 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print ("El fichero esta vacio")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))
        

    def guardar(self):
        fichero = open('personajes.pckl' , 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()


    def borrar(self, argumentoBorrar):
        
        for pTemp in self.personajes:
            if pTemp.clase == argumentoBorrar.clase:
                self.personajes.remove(pTemp)
                self.guardar()
                print("\nSe ha borrado el personaje {}".format(argumentoBorrar))
                return 
        print("No se borro ningun personaje")
        return
personajes = Gestor()
caballero = Personaje("Caballero",4,2,4,2)

guerrero = Personaje("Guerrero", 2, 5, 2, 3)
arquero = Personaje("Arquero", 2,  4,  1,  5)


personajes.agregar(caballero)
personajes.agregar(guerrero)
personajes.agregar(arquero)

personajes.mostrar()

personajes.borrar(arquero)
personajes.mostrar()