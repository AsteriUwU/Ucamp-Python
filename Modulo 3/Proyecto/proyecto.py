import random
import numpy as np
import matplotlib.pyplot as plot

marblePosition = []

def marbleBox(marbles):
    """Función que pone las canicas en una caja dependiendo de la dirección que toma"""
    for i in range(marbles):
        position = 0
        for j in range(12):
            if random.choice(["left", "right"]) == "left":
                position -= 0.5
            else:
                position += 0.5
        marblePosition.append(sortMarble(position))

def sortMarble(position):
    """Función que combierte los numeros negativos en numero de caja para que sea más entendible"""
    if position == -6:
        return 1
    elif position == -5:
        return 2
    elif position == -4:
        return 3
    elif position == -3:
        return 4
    elif position == -2:
        return 5
    elif position == -1:
        return 6
    elif position == 0:
        return 7
    elif position == 1:
        return 8
    elif position == 2:
        return 9
    elif position == 3:
        return 10
    elif position == 4:
        return 11
    elif position == 5:
        return 12
    elif position == 6:
        return 13

def graph(list):
    """Función que crea la gráfica"""
    npMarblePosition = np.array(list)
    plot.hist(npMarblePosition, color = "#fab387")
    plot.title("Simulación de Máquina de Galton")
    plot.xlabel("Numero de caja")

marbleBox(3000) #Cambiar el numero dentro del parentesis pra acambiar la cantidad de canicas lanzadas
graph(marblePosition)
plot.show()