def print_shopping_list(*items):
  "This function prints all the items in the shopping list"

  for item in items:
    print('You must buy', item)

def separator():
  print('-' * 10)

# print_shopping_list("Eggs", "Milk", "Bread", "Chicken", "Romo")
# separator()
# print_shopping_list("Coffee", "Sugar")
# separator()


# Write a function that asks how many items I want to add to the shopping list and ask for them one by one

def shopping_wizard():
  item_number = int(input('How many items do you want to register?'))

  for i in range(item_number):
    input('Write the item #' + str(i))

# shopping_wizard()


def greetings(name):
  print('Hello', name)

greetings('Willy')
greetings('Pri')
greetings('Axs')