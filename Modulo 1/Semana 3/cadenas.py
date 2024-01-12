# texto_variado = "Palabra 123 +-* #%&"
# print(type(texto_variado))

# Podemos utilizar comillas triples para que el texto se muestre como lo hemos escrito
# print("""
# Funcionamiento de \
# programa: (opciones)
#     -1 Para acceder a opciones
#         -2 Para salir
# """)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Subscriptiong e indexado

# texto = 'Python'

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) # Error! No podemos acceder a posiciónes que no existen
# print(texto[-7]) # Error! No podemos acceder a posiciónes que no existen

# letra = texto[0]
# print(letra)

# texto[0] = 'p' # Error! No podemos modificar una cadena

# letra = 'p'
# print(letra)

# texto_compuesto = letra + texto[1] # Concatenación
# print(texto_compuesto)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Slicing o Substringing

# texto = 'Python'
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2])

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Cadenas y formatos
# texto = 'Hola mundo! Buenas tardes'
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# texto = texto.upper()
# print(texto)

print('{} + {} = {}'.format(2, 3, 2+3))
print('{} + {} = {}'.format('Hola', 'mundo', 'Hola mundo'))
print('{:.3f} + {:.4f} = {}'.format(2, 3, 2+3))
print('{1} + {0} = {2}'.format(2, 3, 2+3))
print('{2} + {0} = {1}'.format('Hola', 'mundo', 'Hola mundo'))
print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))