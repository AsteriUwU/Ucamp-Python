# =-=-= La sentencia if =-=-=
animal = input("Dime un animal: ")
if animal == "perro":
    print("-guau.")
print("Conozco pocos animales.")

num = int(input("Ingrese un numero entero: "))
if num < 0:
    num = -num
print("Su valor absoluto es: ", num)

# =-=-= La sentencia if else =-=-=
animal = input("Dime un animal: ")
if animal == "perro":
    print("-guau.")
else:
    print("No conosco su sonido.")
print("Conozco pocos animales.")

# =-=-= La sentencia elif =-=-=
animal = input("Dime un animal: ")
if animal == "perro":
    print("-guau.")
elif animal == "gato":
    print("-miau.")
elif animal == "vaca":
    print("-muu.")
else:
    print("No conozco su sonido.")
print("Conozco pocos animales.")

# =-=-= El ciclo while =-=-=
print("Impares mensores a 10")
x = 1
while x <= 10:
    print(x)
    x += 2

factorial = 5
contador = factorial - 1
while contador > 0:
    factorial *= contador
    contador -= 1
print("El factorial de 5 es: ", factorial)