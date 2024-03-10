import matplotlib.pyplot as plt

def diagramaBarrasCalificaciones(notas, color, alumno):
    """Dibujar la grafica de barras con las calificaciónes"""
    plt.bar(notas.keys(), notas.values(), color = color)
    plt.title("Calificaciónes de: " + alumno)

calificaciones = {
    "Programación": 3,
    "Español": 6.5,
    "Calculo": 4,
    "Historia": 8,
    "Biología": 10,
    "Inglés": 3
}

alumno = input("Nombre de alumn@: ")
diagramaBarrasCalificaciones(calificaciones, "red", alumno)
plt.show()