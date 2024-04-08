while True:
    menuText = "\t=-=-= Captura de calificación de alumnos =-=-=\nIntroduzca una de las opciones:\n1. Agregar un alumno nuevo\n2. Ver alumnos y calificaciónes\nS. Salir"
    
    while True:
        print(menuText)
        option = input("Opcion: ")
        if option == "1" or option == "2" or option == "s" or option == "S":
            break
        else:
            print("\nNo es una opcion valida\n")

    if option == "1":
        while True: 
            print("sans")