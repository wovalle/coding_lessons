pokemons = [
  "Charmander",
  "Bulbasaur",
  "Squirtle",
  "Pikachu"
]
last_position = pokemons[-1]
joined = ", ".join(pokemons[0:-1])
# print("Pokemons:", joined, "and", last_position)

string_to_split= "Charmander, Bulbasaur, Squirtle, Pikachu"
list_of_pokemons = string_to_split.split(",")

for i in range(len(list_of_pokemons)):
  list_of_pokemons[i] = list_of_pokemons[i].strip()


list_of_pokemons2 = string_to_split.split(", ")
# print(list_of_pokemons2)

string_to_split= "Pokemons: Charmander, Bulbasaur, Squirtle, Pikachu"
string_split_by_colon = string_to_split.split(": ")
#print('split by :', string_to_split)
list_of_pokemons = string_split_by_colon[1].split(", ")
# print(list_of_pokemons)

# print(string_to_split.count(','))
# print(string_to_split.startswith('Pokemons'), string_to_split.endswith('Pokemons'))


name = "Priscila"
age = 24
l1 = 'l'
l2 = 'o'
#print("My name is %s and I'm %i years old, %c%c%c" % (name, age, l1, l2, l1))
# print("My name is %s" % name)

lyrics = """mami que tu quiere
aqui llego tu tiburon
yo quiero perrearte y fumarme un blunt
"""

# print (lyrics)

one_line_lyrics = "mami que tu quiere \naqui llego tu tiburon \nyo quiero perrearte y fumarme un blunt"
# print (one_line_lyrics)

print("\t".join(pokemons))

wont_work = "5\4"
will_work = "5\\4"
#print(wont_work, will_work)

quote ="Y Alexis dijo lo siguiente: \"matanga dijo la changa\""
quote2 ='Y Alexis dijo lo siguiente: "matanga dijo la changa"'
# print(quote)
# print(quote2)
