#mAlumons.py
"""Este modulo contiene la función captura que solicita la información de los alumnos y la función promedio que calcula el promedio de cada alumno"""

def captura_alumnos(numero = 3):
    """
    Registra alumnos y sus calificaciónes
    Recibe como parametro la cantidad de alumnos a registrar
    Si no se especifica el numero de alumnos, se registraran 3
    """
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f"{i + 1}, . Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificación de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre, calificacion1, calificacion2)
    print("Las calificaciónes de los alumnos son: ", lista_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    """
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recive como parametros el nombre y dos calificaciónes del alumno
    """
    promedio = (calificacion1 + calificacion2) / 2
    print(f"El promedio de {nombre} es: {promedio}")