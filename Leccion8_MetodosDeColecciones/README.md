# Cadenas

### Dividir Cadenas segun espacios
```py
print("Hola mundo Que tal ".split()) 
```
output ```['Hola', 'mundo', 'Que', 'tal'] ```
* Se le puede agregar indice
```py
print("Hola mundo Que tal ".split()[1]) 
```
Output ```mundo```
* Splitear segun un caracter ','
```py
print("Hola mundo, Que tal ".split(',')) 
```
output ```['Hola mundo', ' Que tal ']```

### Dividir La cadena segun un caracter

```py
print(  ",".join("Hola mundo"))
```
Output ```H,o,l,a, ,m,u,n,d,o```

### reemplazar la cadena por otra

```"cadena".replace('a',"@")```
* con un tercer parametro reemplaza x cantidad de veces
* se puede borrar reemplazando con un ""
```"cadena cadena candena".replace('cadena',"",3)```
### Devolver toda la cadena en mayuscula
```py
"cadena".upper()
```

### Toda la cadena en minuscula
```py
"CADENA".lower()
```

### Primera letra de la primera palabra en mayus
```py
print("Hola mundo".capitalize()) 
```
### Todas las primeras letras en mayus
```py
print("hola mundo".title()) 
```

### Cuantas veces aparece X letra o palabra
```print("Hola mundo".count('o')) ```

### desde que indice inicia x cadena
```print("Hola mundo".find("mundo")) ```
* Si ya la encontro no sigue buscando
Ejem: si pongo ```o``` el output sera 1 

### Buscar el Ultimo indice
```print("Hola mundo".rfind("o")) ```

### Comprobar si todos los caracteres dentro de una cadena son Digito

```py
c="100"
c.isdigit()
```

### Comprobar si todos los caracteres dentro Son Alfanumericos

Numeros o Letras

```
c="ABCDE123"
print(  c.isalnum() )
```
Tira Falso 
* El espacio es un caracter especial

### empieza/Acaba con 
"Cadena".startwith("C")
        .endwith("a")
### Borrar  espacios delante y atras y o Caracte
print("-------Borrar  espacios delante y atras y o Caracter -------".strip("-"))
output ```Borrar  espacios delante y atras y o Caracter```