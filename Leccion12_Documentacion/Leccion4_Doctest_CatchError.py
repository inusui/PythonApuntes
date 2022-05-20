def suma (a,b):
    '''Funcion que suma 2 parametros
    
    >>> suma('a','b')
    'ab'

    >>> suma(10,"hola")
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    '''
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()