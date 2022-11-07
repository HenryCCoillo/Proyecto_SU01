
import requests
import json

################################################################################

print("\t\t.:GENERACION POKEMON:.")
print("1.Generation-1\n"
      "2.Generation-2\n"
      "3.Generation-3\n"
      "4.Generation-4\n"
      "5.Generation-5\n"
      "6.Generation-6\n"
      "7.Generation-7\n"
      "8.Generation-8\n")

url_1 = 'https://pokeapi.co/api/v2/generation/'
gen1 = input("Introduce la generacion que desea: ")


def gen_pokemon(id1):
    response = requests.get(url_1+id1)

    data = response.json()

    generacion = [nombre['name'] for nombre in data['pokemon_species']]
    print(f"Pokemon: {generacion} ")


for id1 in gen1:
    gen_pokemon(id1)

################################################################################
