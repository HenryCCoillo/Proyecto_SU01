import requests
import json
#import matplotlib.pyplot as plt
#import matplotlib.image as img
'''
print("\t\t.:GENERACION POKEMON:.")
print("1.Generation-I\n"
      "2.Generation-II\n"
      "3.Generation-III\n"
      "4.Generation-IV\n"
      "5.Generation-V\n"
      "6.Generation-VI\n"
      "7.Generation-VII\n"
      "8.Generation-VIII\n")

gn = input("Introduce la Generacion de la Lista: ")
url = "https://pokeapi.co/api/v2/generation/" + gn
res = requests.get(url)

if res.status_code != 200:
    print("no se ha encontrado ninguna generacion de la lista")
    exit()
'''
'''
if gn == 1:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print(f"")
    
elif gn == 2:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print(f"")
    
elif gn == 3:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print(f"")
    
elif gn == 4:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print()
    
elif gn == 4:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print()
    
elif gn == 4:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print()
    
elif gn == 4:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print()
    
elif gn == 4:
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url)
    print()
    
else:
    print("\n'Opcion incorrecta'")
'''
    # imagen = img.imread(res.json()['sprites']['front_default'])
    # plt.title(res.json()['name'])
    # imgplot = plt.imshow(imagen)
    # plt.show()
def printl(a):

      for i in range(len(a)):
            if i==len(a)-1:
                  print(a[i])
            else:
                  print(a[i],end = ",")

def get_stat(a,arch):
      return [j['base_stat']for j in [i for i in arch['stats']] if j['stat']['name']==a]

def open_jason(x):
      f = open(x)
      pokemon = json.load(f)
      f.close()
      return pokemon

def imprimir_datos(poke):
      pokemon_archive=requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}/')
      pokemon_archive=pokemon_archive.json()
      #pokemon_archive=open_jason(poke+'.json')
      print(f"============ pokemon {poke} ============")
      stats = {
            'attack':'ataque',
            'defense': 'defensa',
            'special-attack': 'ataque especial',
            'special-defense': 'defensa especial',
            'speed': 'velocidad'
      }
      peso = pokemon_archive['weight']
      print(f'{poke} tiene un peso de:{peso}')
      habilidades = [j['name']for j in [i['ability']for i in pokemon_archive ['abilities']]]
      print('las habilidad son: ',end = " ")
      print(habilidades)
      for i in stats:
            print(f'{stats[i]} de:',end = " ")
            printl(get_stat(i,pokemon_archive ))

      pokemones = ['ditto','bulbasaur','squirtle','charmander','abra','flygon','froslass','gyarados','salamence']
      for i in pokemones:
            imprimir_datos(i)