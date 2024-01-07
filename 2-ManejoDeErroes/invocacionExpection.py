def funcion (algo = None):
    try:
        if algo is None:
            raise ValueError("Error no se permite valor nulo")
    except ValueError:
        print("Error! no se pemite valor nulo desde el EXcept")

funcion()