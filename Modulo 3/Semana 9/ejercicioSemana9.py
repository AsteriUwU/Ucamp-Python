#Utilizar al menos 2 funciones
#Preguntar cuantos alumnos se registraran, en caso de no ingresar cantidad, se asume que se registraran 3 alumnos
#Preguntara el nombre y 2 calificaciónes
#Mostrar nombre en pantalla con inicial en mayuscula y promedio
#Al finalizar el programa se mostrara una lista con el nombre de cada alumno y sus calificaciónes

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

numero_alumnos = input("¿Cuantos alumnos desea registrar?: ")

if numero_alumnos.isnumeric():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()