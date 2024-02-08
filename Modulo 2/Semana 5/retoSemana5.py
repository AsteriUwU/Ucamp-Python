actualYear = input("Escriba el año actual: ")
while actualYear.isnumeric() == False:
    actualYear = input("Ese dato es incorrecto. Escriba el año actual: ")
if actualYear.isnumeric():
    actualYear = int(actualYear)

year = input("Escriba un año: ")
while year.isnumeric() == False:
    year = input("Ese dato es incorrecto. Escriba un año: ")
if year.isnumeric():
    year = int(year)

time = actualYear - year

if time == 0:
    print("Has introducido el mismo año que el actual.")
elif time == 1:
    print("Desde el año", year, "ha pasado 1 año.")
elif time == -1:
    print("Para llegar a ", year, "hace falta 1 año.")
elif time > 1:
    print("Han pasado ", time, "años desde el año que has introducido.")
else:
    print("Faltan ", -time, "años para llegar al año que has introducido.")