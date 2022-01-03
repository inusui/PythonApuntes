import random

lower ="qwertyuiopasdfghjklzxcvbnm"
mayus = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+=/*-|\}{[];:?.>,<"

all = lower + mayus + numbers + symbols
lenght = 16

password = "".join(random.sample(all, lenght))
print (password)


#pasalo a un archivo txt por lo menos ¿No?

file1 = open("pass.txt", "a")
file1.write("\n"+ password)
file1.close()