# Titulo
print('\t=-=-= Calculadora de índice de masa corporal =-=-=')

# Pedir datos y revisarlos
name = str(input('Introduce tu nombre: '))
while len(name) == 0 or not name.isalpha():
    name = input('No escribió datos, introduce tu nombre: ')

pSurname = input('Introduce tu apellido paterno: ')
while len(pSurname) == 0 or not pSurname.isalpha():
    pSurname = input('No escribió datos, introduce tu apellido paterno: ')

mSurname = input('Introduce tu apellido materno: ')
while len(mSurname) == 0 or not mSurname.isalpha():
    mSurname = input('No escribió datos, introduce tu apellido materno: ')


age = int(input('Introduce tu edad: '))
while age <= 0 or age > 116:
    age = int(input('No escribió datos, introduce tu edad: '))

weight = float(input('Introduce tu peso (en Kg.): '))
while weight <= 14:
    weight = float(input('No escribió datos, introduce tu peso en (Kg.): '))


height = float(input('Introduce tu estatura (en m.): '))
while height <= 0.54:
    height = float(input('No escribió datos, introduce tu edad (en m.): '))

# Calcular IMC
imc = weight / (height**2)
imc = float(imc)

# Mostrar datos
print('\n=-=-= Datos del usuario =-=-=')
print('Nombre: ' + str(name.capitalize()))
print('Apellido paterno: ' + str(pSurname.capitalize()))
print('Apellido materno: ' + str(mSurname.capitalize()))
print('Edad: ' + str(age) + ' años')
print('Peso: ' + str(weight) + ' Kg.')
print('Altura: ' + str(height) + ' m.')
print('Índice de Masa Corporal (IMC): {:.2f}'.format(imc))

# Condición en la que se encuentra el usuario
print('\n=-=-= Condición en la que se encuentra el usuario =-=-=')

if imc <= 18.99:
    print('El usuario tiene peso bajo')

if imc >= 19 and imc <= 24.99:
    print('El usuario tiene peso normal')

if imc >= 25 and imc <= 29.99:
    print('El usuario tiene sobrepeso')

if imc >= 30 and imc <= 34.99:
    print('El usuario tiene obesidad leve')

if imc >= 35 and imc <= 39.99:
    print('El usuario tiene obesidad media')

if imc >= 40:
    print('El usuario tiene obesidad media')