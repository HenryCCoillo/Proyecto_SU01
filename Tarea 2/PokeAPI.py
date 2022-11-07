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

url_2 = 'https://pokeapi.co/api/v2/pokemon-shape/'
forma = input("Ingrese la forma que desea : ")


def forma_pokemon(id2):
    resp = requests.get(url_2 + id2)

    data = resp.json()

    forma = [nombre['name'] for nombre in data['pokemon_species']]
    print(f"Lists de pokemon por forma: {forma}")


for id2 in forma:
    forma_pokemon(id2)

################################################################################

url_3 = 'https://pokeapi.co/api/v2/ability/'
hab = input("Ingrese la habilidad que desea: ")


def habilidad_pokemon(id3):
    resp = requests.get(url_3 + id3)

    data = resp.json()

    habilidad = [nombre['pokemon']['name'] for nombre in data['pokemon']]
    print(f"Lista de pokemon por habilidad: {habilidad}")


for id3 in hab:
    habilidad_pokemon(id3)

################################################################################

url_4 = 'https://pokeapi.co/api/v2/pokemon-habitat/'
habitad = input("Ingrese habitad que desea: ")


def habitad_pokemon(id4):
    resp = requests.get(url_4 + id4)

    data = resp.json()

    habitad_pokemon = [nombre['pokemon']['name'] for nombre in data['pokemon']]
    print(f"Lista de pokemon por habitad: {habitad_pokemon}")


for id4 in habitad:
    habitad_pokemon(id4)

################################################################################

url_5 = 'https://pokeapi.co/api/v2/pokemon-habitat/'
tipo = input("Ingrese habitad que desea: ")


def tipo_pokemon(id5):
    response = requests.get(url_5 + id5)

    data = response.json()

    tipo = [nombre['pokemon']['name'] for nombre in data['pokemon']]
    print(f"Lista de pokemon por habitad: {tipo}")


for id5 in tipo:
    tipo_pokemon(id5)
