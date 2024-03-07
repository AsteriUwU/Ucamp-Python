print("\tPara terminar la ejecicón de este programa introduzca '0'")

def nextLetter(ascii):
    nextAscii = ascii + 1
    if nextAscii == 123:
        nextAscii = 97
    return nextAscii

def pastLetter(ascii):
    pastAscii = ascii - 1
    if pastAscii == 96:
        pastAscii = 122
    return pastAscii

loop = "True"

while loop == "True":
    letra = input("Escriba una letra: ").lower()
    while not letra.isalpha():
        if letra == "0":
            exit()
        else:
            letra = input("Esa no es una letra. Escriba una letra: ")
    ascii = int(ord(letra))
    print(f"La letra que sigue de {letra} es: {chr(nextLetter(ascii))} y la letra anterior es: {chr(pastLetter(ascii))}")