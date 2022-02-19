# Procesa un string separado por comas e inicializalo en una lista de diccionarios

csv="""pokedex,name,type
1,bulbasaur,grass
2,ivysaur,grass
4,charmander,fire
7,squirtle,water"""

# Primero, separamos el string original por lineas
bylines = csv.split('\n')

# Sabemos que la primera linea contiene los headers de los campos
# y de la segunda en adelante, contiene la data
headers = bylines[0].split(',')
lines = bylines[1:]

# Inicializamos una lista para guardar la data a procesar (separar por comas)
data = []

# Por cada una de las lineas (string), guarda la data separada por comas (lista)
# De: '1,bulbasaur,grass' => ['1','bulbasaur','grass']
for line in lines:
  data.append(line.split(','))

# ahora data es una lista de listas de data separada por coma
# [ ['1','bulbasaur','grass'], ['4','charmander','fire'] ]

# Inicializa la lista donde guardaremos los diccionarios
pokemons = []

# Por cada uno de las lineas en data, inicializa un nuevo diccionario,
# recorre todos los headers y guarda cada header (key) con su valor (value)
for pokemon in data:
  dict = {}
  for i in range(len(headers)):
    dict[headers[i]] = pokemon[i]
  
  
  pokemons.append(dict)
  

# print(pokemons)


personal_card = {
  'name': 'Willy',
  'age' : 27,
  'nationality': 'Dominican'
}

lines = []

fields = list(personal_card.keys())

headers = ''
for field in fields:
  headers = headers + field + ','

# delete last comma
headers = headers[0:-1]

# tip: is easier to use ','.join(fields)

pokemon_headers = list(pokemons[0].keys())
pokemon_data = []
pokemon_data2 = []

for pokemon in pokemons:
  pokemon_data.append(list(pokemon.values()))
  pokemon_data2.append(','.join(pokemon.values()))

# print(pokemon_data2)

output_csv = ""
output_csv = ','.join(pokemon_headers)
output_csv += '\n'

for pokemon in pokemon_data:
  output_csv += ','.join(pokemon)
  output_csv += '\n'

# print(output_csv[0:-1])

lines = []
lines.append(','.join(pokemon_headers))
for line in pokemon_data2:
  lines.append(line)

output_csv2 = '\n'.join(lines)
print(output_csv2)
