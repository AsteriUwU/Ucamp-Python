#Probando ambitos

titulo = "Probando abitos"
suma = 10.5

def suma():
    suma = 2 + 2
    print(titulo)
    print("suma en ambito local", suma, id(suma))

print("Antes de llamar a la función.")
print("suma en ambito global", suma, id(suma))
suma()
print("Despues de llamar a la función.")
print("suma en ambito global", suma, id(suma))