numerador = 10
denominador = 0
cadena = '3'
numerico = 5

print(numerador / denominador)
print(cadena + numerico)

try:
    print(numerador / denominador)
except ZeroDivisionError:
    print("Ha ocurrido una división entre cero")

try:
    print(cadena + numerico)
except TypeError:
    print("ha ocurrido un error de tipo")

print("Fin del programa")

try:
    print(10 / 0)
except TypeError:
    print("Ha ocurrido un error de tipo")
except:
    print("Ha ocurrido un error desconocido")

#Error 1 ZeroDivisionError
#Error 2 TypeError
    
#=-=-== Manejo de errores con escepciones y ciclos =-=-=

while True:
    try:
        dividiendo = int(input("Ingrese el dividendo: "))
        divisior = int(input("Ingrese el divisor: "))
        print("El resultado es: ", dividiendo / divisior)
        break
    except ValueError:
        print("Debe ingresarse un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

print("Fin del programa")