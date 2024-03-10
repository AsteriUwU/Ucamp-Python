def promedio(*numeros):
    return sum(numeros) / len(numeros)

x = promedio(4, 5, 6)
print(x)

def area(**dato):
    """Calcula el área de una figura geométrica y la imprime en pantalla"""
    if dato["figura"] == "Rectangulo":
        return(dato["base"] * dato["altura"])
    elif dato["figura"] == "Triangulo":
        return(dato["base"] * dato["altura"] / 2)
    elif dato["figura"] == "Circulo":
        return(3.141593 * dato["radio"] ** 2)
    else:
        print("Figura desconocida")

triangulo = area(figura = "Triangulo", base = 10, altura = 5)
print(f"El area del triangulo es: {triangulo}")
circulo = area(figura = "Circulo", radio = 10, color = "Rojo")
print(f"El area del circulo es: {circulo}")
decagono = area(figura = "Dodecagono", lado = 10)
print(f"El area del decagono es: {decagono}")

#=-=-= Recursividad de funciones en python

def factorial(numero, intentos = 0):
    if numero == 0:
        return 1
    else:
        intentos += 1
        print(intentos)
        return numero * factorial(numero - 1, intentos)
    
print("El factorial de 0 es (0!): ", factorial(0))
print("El factorial de 1 es (1!): ", factorial(1))
print("El factorial de 3 es (3!): ", factorial(3))
print("El factorial de -1 es (-1!): ", factorial(-1))

#=-=-= Función zip =-=-=

paises = ["Kenia", "Francia", "Mexico", "Japon"]
capitales = ["Mairobi", "Paris", "Ciudad de Mexico", "Tokio"]
poblacion = [54, 66, 130]

for i in zip(paises, capitales, poblacion):
    print(i)