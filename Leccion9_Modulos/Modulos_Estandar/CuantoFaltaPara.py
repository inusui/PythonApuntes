import datetime

hoy = datetime.date(2022,3,15)
restara = datetime.date(2022,4,6)

print ("Primer pago en " , restara - hoy )

print ("el segundo pago luego del primero\n", datetime.date(2022,4,29) - datetime.date(2022,4,7) )

print ("el tercer pago luego del 3 de mayo\n", datetime.date(2022,5,25) - datetime.date(2022,5,3) )