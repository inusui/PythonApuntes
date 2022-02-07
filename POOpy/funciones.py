def saludar():
    print ("Holanda dentro de una funcion\n")

saludar()

def dibujarTabladel5():
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))
        #       ("5 *",i,"=",i*5)


dibujarTabladel5()


def test(x,c):
    return x+c

print (test(5,10))


