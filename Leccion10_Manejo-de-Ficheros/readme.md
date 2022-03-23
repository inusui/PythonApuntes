# Ficheros

## Operaciones
Creacion -> Abrir -> Cierre -> Extension. 

## Puntero del fichero
como el ordenador procede y accede al fichero.

## Fichero de texto o Fichero Binario
Los ficheros de texto guardan datos en texto plano. 
Ficheros binarios lo guardan en bits.
> Abrir un mp3 con el bloc de notas abrirá caracteres extraños

* Los ficheros deben existir antes de poder escribirlo. 
> ya sea abriendolo en modo append o write

### recorrer en un ciclo 
```py
with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)
```
no se usa un for i in fichero.linea() ya que recorre solo la primera linea caracter por caracter dentro

ejemplo, tenemos en la primera linea "hola"
el output seria:
```h
o
l
a
```

* para usar un cliclo for simple se usa read.lines()

## Json
es importante saber como se guarda el json para cargarlos