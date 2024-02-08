mistakes = 0
password = input("Escriba una contraseña: ")
while not password[0].isnumeric():
    mistakes += 1
    if mistakes == 3:
        print("Has tenido mushos errores")
        exit()
    password = input("La contraseña debe empezar con un numero. Escriba una contraseña: ")

password2 = input("Escriba la contraseña nuevamente: ")
while len(password) != len(password2):
    mistakes += 1
    if mistakes == 3:
        print("Has tenido mushos errores")
        exit()
    password2 = input("Las contraseñas son diferentes. Escriba la contraseña nuevamente: ")

check = int(len(password))

for i in range(check):
    while password[i] != password2[i]:
        mistakes += 1
        if mistakes == 3:
            print("Has tenido mushos errores")
            exit()
        password2 = input("Las contraseñas son diferentes. Escriba la contraseña nuevamente: ")

print("Contraseña correcta")