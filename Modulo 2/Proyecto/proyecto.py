#=-=-= Proyecto =-=-=

import os #This is for clean the console so you don't so much text
def clr():
   os.system('cls' if os.name == 'nt' else 'clear')

print("\t=-=-= Validacion y operacion de datos =-=-=") #Menú para decidir entre los 2 ejercicios
print("Escriba el numero del programa que desea ejecutar.")
print("1. Longitud de una frase.")
print("2. Encuentra el cuadrante.")
print("3. Salir")
option = input("Opcion: ")
while not option.isnumeric() or int(option) <= 0 or int(option) >= 4: #Validar que el input sea un numero y sea una de las opciónes
    print("Esa no es una opcion valida, intente de nuevo")
    option = input("Opcion: ")

if option == "1": #En caso de opción 1 se ejecuta el primer ejercicio
    clr() #Funcuón para limpiar la pantalla
    print("\t =-=-= Longitud de una frase =-=-=")
    frase = input("Escriba la frase: ")
    while len(frase) < 4 or len(frase) > 8:
        if len(frase) < 4:
            print(f"Hacen falta letras. Solo tiene {len(frase)} letras.")
            frase = input("Escriba la frase: ")
        elif len(frase) > 8:
            print(f"Sobran letras. Tiene {len(frase)} letras.")
            frase = input("Escriba la frase: ")
    print("La frase es correcta.")
elif option == "2":
    clr() #Otra vez limpia la pantalla
    print("\t=-=-= Encuentra el cuadrante =-=-=")
    x = input("Ingrese el valor de x: ")
    while not x.lstrip("-").isnumeric() or int(x) == 0: #Como "isnumeric()" no reconoce a los negativos "lstrip("-")" elimina el simbolo negativo para que lo identifique
        if x == "0":
            print("El valor no puede ser 0.")
        else:
            print("El valor no es correcto, intente de nuevo.")
        x = input("Ingrese el valor de x: ")
    y = input("Ingrse el valor de y: ")
    while not y.lstrip("-").isnumeric() or int(y) == 0:
        if y == "0":
            print("El valor no puede ser 0.")
        else:
            print("El valor no es correcto, intente de nuevo.")
        y = input("Ingrese el valor de y: ")
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    else:
        print("El punto se encuentra en el cuadrante IV.")
else:
    exit()