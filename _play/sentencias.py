""" Sentencias de control """
print("""Welcome\n
      Esto es un simple programa que tiene 2 opciones
      1. Imprime Hola
      2. una suma toda pendeja
      3. sale del ciclo while infinito""")

while True:
    print(""" Menu de opciones
        1) holanda
        2) sumatoria
        3) Adios""")
    opcion = input()

    if opcion == '1':
        print("esto es un hola")
    elif opcion == '2':
        n1 = float(input("Introduce un numero"))
        n2 = float(input("Introduce otro numero"))
        print("El resultado es: ", n1+n2)
    elif opcion == '3':
        print("Adios")
        break
    else:
        print("Mal comando we")
