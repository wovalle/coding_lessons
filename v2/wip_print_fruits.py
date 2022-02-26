# print_fruits("coconut", "banana", "orange") => "The fruits are coconut, banana and orange"
  # print_fruits("coconut", "banana", "orange") => "coconut, banana, orange, "
  # print_fruits("coconut", "banana", "orange") => "coconut, banana, orange"
  # print_fruits("coconut", "banana", "orange") => "The fruits are coconut, banana, orange"
  # print_fruits("coconut", "banana", "orange") => "The fruits are coconut, banana and orange"


def print_fruits(*fruits):
  "Print all the fruits appending an 'and' before the last fruit"

  result = ""

  for fruit in fruits:
    result += fruit 

  return result


print('El resultado es:', print_fruits("coconut", "banana", "orange"))


