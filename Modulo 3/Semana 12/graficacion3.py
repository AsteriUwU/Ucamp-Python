import random
import matplotlib.pyplot as plt

ejeX = [random.randint(1, 100) for n in range(100)]

ejeY = [random.randint(1, 100) for n in range(100)]

plt.scatter(ejeX, ejeY)

plt.title("Gráfica de dispersión")

plt.show()