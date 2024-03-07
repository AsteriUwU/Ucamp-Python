def sumar(parametro1, parametro2):
    """Función que suma dos parametros y los imprime en pantalla"""
    print("Suma: ", parametro1 + parametro2)

argumento1 = 5
argumento2 = 7

#Invocando a la función por medio de parametro variables
sumar(argumento1, argumento2)

#Invocando a la función por medio de parametros de valor
sumar("mundo", "Hola")
sumar("Hola", "mundo")

#=-=-= Parametros opcionales =-=-=
def muestra_alumno(nombre, edad = 18, sexo = "F"):
    """
    Es una función que muestra en pantalla el nombre, edad y sexo de un alumno
    Recibe 3 parametros:
    1. Nombre
    2. Edad = 18
    3. Sexo = "F"
    """
    print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}")

#Ejecución de función con parametro obligatorio
muestra_alumno("Maria")

#Ejecución utilizando el parametro obligatorio y uno opcional
muestra_alumno("Maria", 22)

#Ejecución de función con el primero y el ultimo
muestra_alumno("Juan", sexo = "M")