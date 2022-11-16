#informacion sobre este paquete
from setuptools import setup

setup (
    name="mensajes",
    version= "2",
    description="Paquete para saludar y despedir",
    author="Inusui",
    author_email="inusui@protonmail.com",
    url="https://mypage.com",
    packages=['paquetes', 'paquetes.adios', 'paquetes.hola'],
    scripts=['test.py']
)

