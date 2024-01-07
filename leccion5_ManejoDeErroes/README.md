# Errores

## Error Semantico
```py
list = [1]
list.pop()

list.pop() #Error Semantico, no hay mas elementos para sacar de la lista
```

### Error no se puede dividir
```py
def dividir (a,b):
    if (b <= 0):
        return "No puedes dividir por cero"
    else:
        return a/b

print (dividir(0,5))
```

## Try Except Else
El else solo se ejecuta cuando no hay ninguna exception
```py 
while (True):
    try:
        n = float(input("Dame numericos"))
        m = 10
        print ('''{}/{} = {} '''.format(n,m,n/m))
        
    except:
        print("Error")
    else: # Solo se ejecutara si no hay ninguna Exception
        print("NICE")
        break
```


## Invocar Exceptions
```raise```
https://docs.python.org/3/library/exceptions.html#base-classes
https://docs.hektorprofe.net/python/errores-y-excepciones/invocacion-de-excepciones/
