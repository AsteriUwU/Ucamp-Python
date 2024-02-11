#=-=-= Conjuntos =-=-=

# canasta = {"manzana", "naranja", "manzana", "pera", "naranja", "platano"}
# print(canasta)
# print("melón" in canasta)
# vocales = ["a", "e", "i", "o", "u", "a"]
# print(vocales)
# vocales = list(set(vocales))
# print(vocales)
# vocales1 = {"a", "e", "i", "o", "u", "a"}
# vocales2 = {"e", "i", "o"}
# print(vocales2.issubset(vocales1))
vocales1 = {"a", "e", "i", "o", "u"}
vocales2 = {"A", "E", "I", "O", "u"}
print(vocales1 - vocales2)
print(vocales1 | vocales2)
print(vocales1 & vocales2)
print(vocales1 ^vocales2)