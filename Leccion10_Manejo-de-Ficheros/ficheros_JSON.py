import email
import json
#la estructura se maneja en listas y diccionarios

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []
for nombre, empleo, email in contactos:
    datos.append({"Nombre" : nombre, "Empleo": empleo, "Correo" : email})

with open ("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

datos = None
with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print("Nombre: {}, Empleo: {}, Correo: {}".format(contacto["Nombre"],contacto["Empleo"],contacto["Correo"]))