from setuptools import setup, find_packages

setup(
    name='Mensajes',
    version='4.1',
    description='Un paquete para saludar y despedir',
    author='Inusui',
    author_email='inusui@mail.com',
    url='https://mypage.com',
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip()
                      for paquete in open("requirements.txt").readlines()]
)
