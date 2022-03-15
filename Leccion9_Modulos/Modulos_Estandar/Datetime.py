import datetime
import imp

fecha1 = datetime.datetime.now()
print(fecha1)

print("{}:{}:{}".format(fecha1.hour, fecha1.minute, fecha1.second))
print("{}/{}/{}".format(fecha1.day, fecha1.month, fecha1.year))

dt = datetime.datetime(2000,1,1) 
dt.replace(year=3000)#se puede reemplazar para cambiar la fecha que queremos
# Esto nos muetra una copia pero no lo reemplaza como tal en el objeto orginal

print(dt)

# Formateos
dt = datetime.datetime.now()

dt.isoformat() #Formato iso para la fecha
print(dt)

# Formato personalizado

print(dt.strftime("%b %d, %Y - %H:%M:%S"))

print(dt.strftime("%A %d %B %Y - %I:%M"))

print(dt.year - 2016) #restar fecha 

import locale
print(locale.setlocale(locale.LC_ALL, 'es')) #Espa;ol, espa;a
print(dt.strftime("%A %d %B %Y - %I:%M")) #Luego de cambiar la localizacion cambia el idioma de la fecha

locale.setlocale(locale.LC_ALL, 'ja_JP')
print(dt.strftime("%A %d %B %Y - %I:%M")) 

locale.setlocale(locale.LC_ALL, 'es')

t = datetime.timedelta(days=14, hours=4, seconds=1000)
en2 = dt + t
print("Sumar 2 semanas a este dia", en2)

hace2 = dt - t
print("Hace 2 semanas" , hace2)

import pytz
dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
print(dt.strftime("%A %d %B del %Y - %H:%M")) 