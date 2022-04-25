def cuadrados(n_maximo):
    for numero in range(1 , n_maximo + 1):
        if numero != 0:
            yield numero, numero **2

print(list(cuadrados(5)))