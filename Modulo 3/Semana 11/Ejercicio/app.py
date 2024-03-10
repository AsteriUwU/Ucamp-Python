import mAlumons as m3

numero_alumnos = input("¿Cuantos alumnos desea registrar?: ")

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    m3.captura_alumnos(numero_alumnos)
else:
    m3.captura_alumnos()