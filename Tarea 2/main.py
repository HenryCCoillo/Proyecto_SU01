
import requests
import json

################################################################################
def menu():
    print("\n* * * * * * * * Bienvenido al programa de listado de Pokemon* * * * * * * * ")
    print("Elige la opcion segun el listado :")
    print("[1] -> Opcion por generación")
    print("[2] -> Opcion por forma")
    print("[3] -> Opcion por habilidad")
    print("[4] -> Opcion por habitad")
    print("[5] -> Opcion por tipo")
    print("[6] -> Salir")

################################################################################
def op_1():
    print("\t\t.:GENERACION POKEMON:.")
    print("Generation -> 1\n"
          "Generation -> 2\n"
          "Generation -> 3\n"
          "Generation -> 4\n"
          "Generation -> 5\n"
          "Generation -> 6\n"
          "Generation -> 7\n"
          "Generation -> 8\n")

    url_1 = 'https://pokeapi.co/api/v2/generation/'

    input_1 = input("Introduce la generacion: ")

    def lista_pokemon(id1):
        response = requests.get(url_1 + id1)

        data = response.json()

        generacion = [gen['name'] for gen in data['pokemon_species']]
        print(f"Pokemon: {generacion} ")

    for id1 in input_1:
        lista_pokemon(id1)

################################################################################
def op_2():
    print("\t\t.:FORMA POKEMON:.")
    print("Elija un numero del 1 al 14 para seleccionar el listado por forma que desea.")

    input_2 = input("Ingrese la forma que desea : ")

    url_2 = 'https://pokeapi.co/api/v2/pokemon-shape/'

    def forma_pokemon(id2):
        response = requests.get(url_2 + id2)

        data = response.json()

        forma = [forma['name'] for forma in data['pokemon_species']]
        print(f"Lists de pokemon por forma: {forma}")

    for id2 in input_2:
        forma_pokemon(id2)

################################################################################
def op_3():
    print("\t\t.:HABILIDAD POKEMON:.")
    print("Elija un numero del 1 al 327 para seleccionar el listado por habilidad que desea.")

    input_3 = input("Ingrese la habilidad que desea: ")

    url_3 = 'https://pokeapi.co/api/v2/ability/'

    def habilidad_pokemon(id3):
        response = requests.get(url_3 + id3)

        data = response.json()

        habilidad = [habilidad['pokemon']['name'] for habilidad in data['pokemon']]
        print(f"Lista de pokemon por habilidad: {habilidad}")

    for id3 in input_3:
        habilidad_pokemon(id3)

################################################################################
def op_4():
    print("\t\t.:HABITAD POKEMON:.")
    print("Elija un numero del 1 al 9 para seleccionar el listado por habitad que desea.")

    input_4 = input("Ingrese el habitad que desea: ")

    url_4 = 'https://pokeapi.co/api/v2/pokemon-habitat/'

    def habitad_pokemon(id4):
        response = requests.get(url_4 + id4)

        data = response.json()

        habitad = [habitad['name'] for habitad in data['pokemon_species']]
        print(f"Lista de pokemon por hábitad: {habitad}")

    for id4 in input_4:
        habitad_pokemon(id4)

################################################################################
def op_5():
    print("\t\t.:TIPO POKEMON:.")
    print("Elija un numero del 1 al 20 para seleccionar el listado por tipo que desea.")

    input_5 = input("Ingrese el tipo que desea: ")

    url_5 = 'https://pokeapi.co/api/v2/type/'

    def tipo_pokemon(id5):
        response = requests.get(url_5 + id5)

        data = response.json()

        tipo = [tipo['pokemon']['name'] for tipo in data['pokemon']]
        print(f"Lista de pokemon por tipo: {tipo}")

    for id5 in input_5:
        tipo_pokemon(id5)

################################################################################
option = 0
while option != 6:
    print("\n* * * * * * * * Bienvenido al programa de listado de Pokemon* * * * * * * * ")
    print("Elige la opcion segun el listado :")
    print("[1] -> Opcion por generación")
    print("[2] -> Opcion por forma")
    print("[3] -> Opcion por habilidad")
    print("[4] -> Opcion por habitad")
    print("[5] -> Opcion por tipo")
    print("[6] -> Salir")
    option = int(input("Ingrese su opcion: "))
    if option == 1:
        op_1()

    if option == 2:
        op_2()

    if option == 3:
        op_3()

    if option == 4:
        op_4()

    if option == 5:
        op_5()

    else:
        print("Fin del PokeAPI, Gracias.")
