import random

#Funciones 
def GeneradorPassword():
    lower ="qwertyuiopasdfghjklzxcvbnm"
    mayus = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    numbers = "0123456789"
    symbols = "~!@#$%^&*()_+=/*-|\}{[];:?.>,<"

    lenght = int ( input ("Dame la cantidad de caracteres que quieres en tu contraseña\nSe recomiendan 16"))

    all = lower + mayus + numbers + symbols
    password = "".join(random.sample(all, lenght))
    print ("Contraseña Generada=> " , password)

    Guardar()
    

def Guardar():
    guardar = input("¿Desea Guardar la contraseña?\n [Y/N]")

    if guardar == "Y":
        print ("Eligio que Si.")
    elif guardar == "N":
        print ("Eligio que No")
    else:
        print("No eligio ni [Y/N]\nERROR\nSu Eleccion fue=>" , guardar)
        Guardar()#Deberia iniciar de nuevo esta misma Funcion?


controlador = 1


while controlador == 1: 

    x = int(input('''***********Menu de Opciones**************\n
    Opcion 1 > Generador de Contraseñass\n
    Opcion 2 > Salir
    Solo inserte numeros, de otro modo dara error. 
Opcion:'''))

    if x == 1:
        GeneradorPassword()

        #pasalo a un archivo txt por lo menos ¿No?

        file1 = open("pass.md", "a")
        file1.write("\n"+ password)
        file1.close()

        #Leer lineas
        file1 = open ("pass.md", "r")
        lines = file1.readlines()
        print ("Soy la variable lines> " , lines)
        c = 0
        for line in lines:
            c +=1
        print (c) #imprimo en integer la cantidad de lineas. 

    elif x == 2:
        print ("Saliendo... ")
        controlador = 2

    else:
        print("\n(X) Error, no elegiste ninguna de las opciones")
        controlador = 1


