import random

lower ="qwertyuiopasdfghjklzxcvbnm"
mayus = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "0123456789"
symbols = "~!@#$%^&*()_+=/*-|\}{[];:?.>,<"
#mathSymbols = "⨀⨃⨆⨉⨌⨏⨒⨕⨖⨓⨐⨍⨊⨇⨄⨁⨂⨅⨈⨋⨎⨑⨔⨗⨭⨪⨧⨤⨡⨞⨛⨘⨙⨜⨟⨢⨥⨨⨫⨮⨬⨩⨦⨣⨠⨝⨚⨰⨳⨶⨹⨼⨿⩂⩅⩆⩃⩀⨽⨺⨷⨴⨱⨲⨵⨸⨻⨾⩁⩄⩇⩝⩚⩗⩔⩑⩎⩋⩈⩉⩌⩏⩒⩕⩘⩛⩞⩟⩜⩙⩖⩐⩓⩍⩊⩠⩣⩦⩩⩬⩯⩲⩵"
#langSymbols ="ΔδηκλΛθΘεβΓζμτπΠΞξΨΩφΦΣχἉἁἙᾁΈέΉἑήΉήἹἱὀΌἺἳὅόῡὛώΏ·ᾤϷϞϘϽϛϠϕϙ"

all = lower + mayus + numbers + symbols #+ mathSymbols + langSymbols
lenght = 16

password = "".join(random.sample(all, lenght))
print (password)


#pasalo a un archivo txt por lo menos ¿No?

file1 = open("pass.md", "a")
file1.write("\n"+ password)
file1.close()

#Leer lineas
file1 = open ("pass.md", "r")
lines = file1.readlines()
print ("Soy la variable lines> " , lines)
c = 0
for line in lines:
    c +=1
print (c) #imprimo en integer la cantidad de lineas. 