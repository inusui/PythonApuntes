import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    cabezeras = ['Nombre','Empleo','Correo']
    writer = csv.DictWriter(csvfile, fieldnames=cabezeras)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            'Nombre':nombre ,'Empleo':empleo ,'Correo': email
        })
    
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print("Nombre: {}, Empleo: {}, Correo: {}".format(contacto["Nombre"],contacto["Empleo"],contacto["Correo"]))