#Función simple
def funcion_simple():
    """Esta funcion no hace nada"""
    pass

#Función saludar al mundo
def saludar():
    '''Esta funcion saluda al mundo'''
    print("Hola mundo.")

print("Antes de llamar a la función")
funcion_simple()
saludar()
print("Ya se ha llamado a la función")

help(saludar)
help(funcion_simple)