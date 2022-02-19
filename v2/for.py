favorite_fruit="coconut"

for letter in favorite_fruit:
  print('current letter', letter)

fruits = ['apple', 'orange', 'pineapple', 'pear', 'lemon']

# Print all fruits until pineapple
# for fruit in fruits:
#   print('Current fruit is: ', fruit)

#   if (fruit == 'pineapple'):
#     break

# Print all fruits but pineapple
# for fruit in fruits:
#   if (fruit == 'pineapple'):
#     continue

#   print('Current fruit is: ', fruit)

# Print all fruits but pineapple and pear
# 1st approach
# for fruit in fruits:
#   if (fruit == 'pineapple'):
#     continue
#   elif (fruit == 'pear'):
#     continue

#   print('Current fruit is: ', fruit)

# 2nd approach
# for fruit in fruits:
#   if (fruit[0] == 'p'):
#     continue

#   print('Current fruit is: ', fruit)

# 3rd approach
# for fruit in fruits:
#   if (fruit == 'pineapple' or fruit == 'pear' or fruit == 'orange'):
#     continue

#   print('Current fruit is: ', fruit)

# 4th approach
for fruit in fruits:
  if (fruit in ['pineapple', 'pear', 'orange']):
    continue

  print('Current fruit is: ', fruit)


# for number in range(5):
#   print('Current Number: ', number)

# print('finished!')


# for number in range(2, 5):
#   print('Current Number: ', number)

# print('finished!')


# range
#   from (2)
#   to (5)
#   step (2)

# for number in range(7):
#   print('Current Number: ', number)

# print('finished!')