person = {
  'name': 'Priscila',
  'lastname': 'Ovalle',
  'age': 24
}

person['name'] = 'Alexis'
# del person['age']

# print('El nombre de la persona es %s y su edad es %d' % (person['name'], person['age']))


pokemons = [
  {
    'pokedex': 1,
    'name': 'bulbasaur',
    'type': 'grass',
  },
  {
    'pokedex': 2,
    'name': 'ivysaur',
    'type': 'grass',
  },
  {
    'pokedex': 4,
    'name': 'charmander',
    'type': 'fire',
  },
]

# Escriba un programa que imprima la lista de pokemones en este formato:
# pokedex_id, {name} es tipo {type}
# pokedex_id, {name} es tipo {type}
# pokedex_id, {name} es tipo {type}

for pokemon in pokemons:
  #print('%d, %s es tipo %s' % (pokemon['pokedex'], pokemon['name'], pokemon['type']))
  pass


bulbasaur = pokemons[0]

for key in bulbasaur.keys():
#  print("El key '%s' tiene el valor de '%s'" % (key, bulbasaur[key]))
  pass

for item in bulbasaur.items():
  #print("El key '%s' tiene el valor de '%s'" % (item[0], item[1]))
  pass

for key, value in bulbasaur.items():
  #print("El key '%s' tiene el valor de '%s'" % (key, value))
  pass


#Escribe un programa que me pregunte por un pokemon e imprima la información en el siguiente formato:
# pokedex_id, {name} es tipo {type}

pokemons = [
  {
    'pokedex': 1,
    'name': 'bulbasaur',
    'type': 'grass',
  },
  {
    'pokedex': 2,
    'name': 'ivysaur',
    'type': 'grass',
  },
  {
    'pokedex': 4,
    'name': 'charmander',
    'type': 'fire',
  },
]

while(True):
  pokemon_to_search = input('Ingrese el nombre del pokemon que desea buscar: ')
  found = False

  if(pokemon_to_search == 'exit'):
    break

  for pokemon in pokemons:
    if (pokemon['name'] == pokemon_to_search): 
      print('%d, %s es tipo %s \n\n' % (pokemon['pokedex'], pokemon['name'], pokemon['type']))
      found = True

  if(not found):
    print('El pokemon %s no existe, intente de nuevo \n\n' % pokemon_to_search)

