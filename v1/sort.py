def sort_func(e):
  return -e

list = [4,5,7,8,54,6,8,9,0,43]
list2 = list.copy()
list2.sort(key=sort_func)

# print("La lista Original", list)
# print("La lista Sorted", list2)


pokemons = [
  {
    'pokedex': 1,
    'name': 'bulbasaur',
    'type': 'grass',
  },
  {
    'pokedex': 4,
    'name': 'charmander',
    'type': 'fire',
  },
  {
    'pokedex': 7,
    'name': 'squirtle',
    'type': 'water'
  },
  {
    'pokedex': 2,
    'name': 'ivysaur',
    'type': 'grass',
  }
]

def order_by_pokedex(pokemon):
  return pokemon['pokedex']

def order_by_type(pokemon):
  return pokemon['type']

def order_by_name(pokemon):
  return pokemon['name']

# pokemons.sort(key=order_by_pokedex, reverse=True)
# pokemons.sort(key=order_by_name)
# pokemons.sort(key=lambda pokemon: pokemon['type'])
pokemons.sort(key=lambda pokemon: len(pokemon['name']), reverse=True)
# print("La lista Sorted", pokemons)

