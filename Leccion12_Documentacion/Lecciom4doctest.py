def suma(a,b):
    ''' trata de ejecutar un comando cuando se ejecuta el help
    
    >>> suma(5,10)
    15
    '''
    return a+b

def palindromo (argumento):
    '''
        Trata de que la palabra se escribe igual de derecha a izquierda y viceversa

    >>> palindromo("Ana")
    True

    >>> palindromo("Holah") 
    False

    >>> palindromo("Atar a la rata")
    True
    '''

    if argumento.lower().replace(" ","") == argumento[::-1].lower().replace(" ",""):
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Notar que mod significa módulo


 