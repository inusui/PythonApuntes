from email.errors import StartBoundaryNotFoundDefect
from telnetlib import GA


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


galleta1 = Galleta()