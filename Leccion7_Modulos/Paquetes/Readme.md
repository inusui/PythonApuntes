el __pycache__ simplemente guarda informacion sobre la ejecucion del fichero

## Paquetes
se pueden instalar dentro del python de tu computadora. 

### primero se crean
este seria un ejemplo del setup.py, necesario para la creacion de paquetes distribuibles

```py
from setuptools import setup

setup (
    name="paquete",
    version= "0.1",
    description="Paquete de testeo",
    author="SoyInusui",
    author_email="inusui@protonmail.com",
    url="https://mypage.com",
    scripts=[],
    packages=['paquetes', 'paquetes.adios', 'paquetes.hola']
)
```

## se ejecuta el setup.py
desde terminal
```python setup.py sdist```
esto creara una carpeta dist, dentro de dicha carpeta hay un fichero comprimido con nuestro paquete

### instalacion en nuestro python 
```pip install <Nombre de tu paquete.extension>```
en caso tal no funcione con pip, usa pip3
* debes estar dentro de la carpeta dist para ejecutarlo

con esto tu codigo funciona en cualquier lado de tu computadora, sin importar los url o directorios.
esto es porque en el setup ( se importaron los paquetes necesarios para le ejecucion del codigo )

## desinstalar paquete
```pip uninstall <paquete>```

al desintalarlo, ya no se ejecutara en cualquier lado del Sistema Operativo

## Instalar paquetes automaticamente

Se debe importar el modulo ```find_package```

dentro del ```setup()```
en ```packages``` se llama a la funcion

```py
setup(
    #... other code
    package = find_package(),
    #... code
)
```