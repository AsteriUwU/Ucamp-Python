import random

def tiroDado(numTiros):
    for dado in range(numTiros):
        print("El dado ", str(dado + 1) + " dio: " + str(random.randint(1, 6)))

tiroDado(5)