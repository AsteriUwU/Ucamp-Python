numHuevos = 12

# print('Tengo ' + numHuevos + ' huevos') # Error!

print('Tengo ' + str(numHuevos) + ' huevos')
print('Tengo %s huevis' %numHuevos)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Calcular la superficie o area de un cuadro
lado = int(input('Ingrese la medida del lado del cuadrado: '))

superficie = lado * lado

print('La superficie del cuadrado es: ' + str(superficie))