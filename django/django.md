# Django

framework de angular

mapeador ORM para el manejo de base de datos, autogenera un swagger. 

## para que no usarlo

Manejar microservicios sin backend
aplicaciones de big data
plataformas con sockets en tiempo real.  

## instalacion

```bash
pipenv install django
```

## Crear proyecto

```bash
pipenv run django-admin startproject gettingStartDjango
```

## Notas

el [PipFile](Pipfile) es como el package.json de npm donde puedo poner script para ahorrarme el aprenderme comandos

por ejemplo el siguiente comando `pipenv run python manage.py runserver` se puede reducir a un `pipenv run server` editanto del pipfile de la siguiente forma

```pipfile
[scripts]
server = "python manage.py runserver"
```
## Configuraciones basicas
