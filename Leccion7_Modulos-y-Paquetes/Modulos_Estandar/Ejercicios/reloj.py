#Reloj en terminal, no para nunca, no puse ningun break
# Ctrl + c para finalizar la ejecucion

import datetime
import time
import os


while (True):
    os.system('cls')
    hora = datetime.datetime.now()
    print("{}".format(hora.strftime("%H:%M:%S")) ) 
    time.sleep(1)
    