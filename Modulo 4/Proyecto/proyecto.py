import requests
import os
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen  

while True:
    while True:
        print("\t=-=-= Pokedex =-=-=")
        pokemon = input("Esciba el nombre de un pokemon (si desea terminar el programa escriba exit): ")
        if pokemon == "exit":
            exit()
        url = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if url.status_code != 200:
            print("\nPokemon no encontrado\n")
        else:
            break

    datos = url.json()

    try:
        url_imagen = datos["sprites"]["front_default"]
        imagen = Image.open(urlopen(url_imagen))
    except:
        print("El pokemon no tiene imagen")

    plt.title(datos["name"])
    imgplot = plt.imshow(imagen)
    plt.show()

    print("\n\t=-=-= Estadisticas =-=-=")
    if os.path.exists(f"Modulo 4/Proyecto/pokedex/{pokemon}.json") == True:
        with open(f"Modulo 4/Proyecto/pokedex/{pokemon}.json", "r") as pokemonData:
            print(pokemonData.read())
    else:
        pokemonData =  open(f"Modulo 4/Proyecto/pokedex/{pokemon}.json", "w")
        pokemonData.write(f">Peso: {datos['weight']}")

        pokemonData.write(f"\n>Tamaño: {datos['height']}")

        pokemonData.write("\n>Movimientos:")
        for i in range(len(datos["moves"])):
            pokemonData.write(f" {datos['moves'][i]['move']['name']}")

        pokemonData.write("\n>Habilidades:")
        for i in range(len(datos["abilities"])):
            pokemonData.write(f" {datos['abilities'][i]['ability']['name']}")

        pokemonData.write("\n>Tipos:")
        for i in range(len(datos["types"])):
            pokemonData.write(f" {datos['types'][i]['type']['name']}")

        pokemonData.write(f"\n>Url de imagen: {url_imagen}")
        pokemonData.close()
        with open(f"Modulo 4/Proyecto/pokedex/{pokemon}.json", "r") as pokemonData:
            print(pokemonData.read())