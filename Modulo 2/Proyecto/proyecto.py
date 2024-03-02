#=-=-= Proyecto =-=-=

import os #This is for clean the console so you don't so much text
def clr():
   os.system('cls' if os.name == 'nt' else 'clear')

def check(variable): #Esta función sirve para revisar si el ususario puso un numero correcto en el punto 2 de la actividad
    while not variable.lstrip("-").isnumeric() or int(variable) == 0: #Como "isnumeric()" no reconoce a los negativos "lstrip("-")" elimina el simbolo negativo para que lo identifique
        if variable == "0":
            print("El valor no puede ser 0.")
        else:
            print("El valor no es correcto, intente de nuevo.")
        variable = input("Ingrese el valor de x: ")
    return variable

print("\t=-=-= Validacion y operacion de datos =-=-=") #Menú para decidir entre los 2 ejercicios
print("Escriba el numero del programa que desea ejecutar.")
print("1. Longitud de una frase.")
print("2. Encuentra el cuadrante.")
print("3. Salir")
option = input("Opcion: ")
while not option.isnumeric() or int(option) <= 0 or int(option) >= 4: #Validar que el input sea un numero y sea una de las opciónes
    print("Esa no es una opcion valida, intente de nuevo")
    option = input("Opcion: ")

#PUNTO UNO:
#Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las siguientes consideraciones:
#Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta
#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))

#PUNTO UNO QUE SI ESTABA APUNTO DE APARECER
    
#AQUÍ VIENE EL PUNTO UNO
    
#PUNTO UNO AUÍ ABAJO    |
#                       |
#                       v

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

#AQUÍ TERMINÓ EL PUNTO UNO  ^
#                           |
#                           |
    
#EL PUNTO UNO ESTABA DESDE LA PRIMERA VERSIÓN

elif option == "2":
    clr() #Otra vez limpia la pantalla
    print("\t=-=-= Encuentra el cuadrante =-=-=")
    x = input("Ingrese el valor de x: ")
    check(x)
    y = input("Ingrse el valor de y: ")
    check(y)
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