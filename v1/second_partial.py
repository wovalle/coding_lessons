# Tema 2
def is_prime (n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nextPrime (n):
  while (True):
    n +=1
    if(is_prime(n)):
      return n


# print('Next Prime after 3', nextPrime(3))
# print('Next Prime after 16', nextPrime(16))
# print('Next Prime after 1026', nextPrime(1026))

# Tema 3
def capitals (str):
  dic = {
    'capitalCount': 0,
    'capitalIndexes': []
  }

  words = str.split()
  capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  for i in range(len(words)):
    current_word = words[i]
    if(current_word[0] in capitals):
      dic['capitalCount'] += 1
      dic['capitalIndexes'].append(i)

  return dic

# print(capitals('amanecí haciendo la práctica')) #=> { count: 0, indexes: [] }
# print(capitals('Siga Boyando')) #=> { count: 2, indexes: [0, 1] }
# print(capitals('Take yourself To Higher places')) #=> { count: 3, indexes: [0, 2, 3] }
# print(capitals('Futurama is the Funniest, Cleverest show in history')) #=> { count: 3, indexes: [0, 3, 4] }


# Tema 4
def countAdjacentPairs(str):
  count = 0
  words = str.split()
  last_word = ""

  for i in range(len(words) -1):
    if(words[i] == words[i+1] and words[i] != last_word):
      count += 1
      last_word = words[i]
  
  return count


print(countAdjacentPairs("dog cat"), "and should be: ", 0)
print(countAdjacentPairs("dog dog cat"), "and should be: ", 1)
print(countAdjacentPairs("dog dog cat cat"), "and should be: ", 2)
print(countAdjacentPairs("dog dog apple cat cat"), "and should be: ", 2)
print(countAdjacentPairs("dog dog dog"), "and should be: ", 1)
