pip install pyinstaller

* Si se manda el programa a otro dispositivo no es necesario que ese  dispositivo tenga python instalado. 
* su unica limitante es que debe ser del mismo sintema operativo que el origen

## uso

pyinstaller programa.py

## Enpaquetado en un solo fichero

--windowed: De ventana o aplicacion grafica
--onefile: un solo fichero
--clean: Limpio que borre todo lo anterior
--add-data res:res => para añadir recursos como imagenes
--ico res/dino.ico => para añadir un icono // la verdad lo dejaria sin esta vaina

```sh
pipenv run pyinstaller programa.py --windowed --onefile --clean

# para añadir recursos
pipenv run pyinstaller programa.py --windowed --onefile --clean --add-data res:res
```
## Optimizar tamaño del paquete

### Instalar entorno virtual con el pyinstaller

```
$ pipenv install pyinstaller 
```

### Ejecutar

```
$ pipenv run pyinstaller programa.py 
```

## Cuando hay recursos

