def sum(a, b):
  "this function receives two numbers and return its sum"
  return a + b

def substract(a, b):
  a - b

def sum_and_print(a, b):
  print("La suma de ", a, "y ", b, " = ", sum(a, b))
 
# print("La suma de 4 y 6 = ", sum(4, 6))
# print("La suma de 5 y 3 = ", sum(5, 3))
# print("La suma de 8 y 3245235 = ", sum(8, 3245235))

# print("La resta de 8 y 3 = ", substract(8, 3245235))

# print('a', 'b', 'c')
# sum_and_print(5, 10)




# numbers = [4, 5, 6]
# sum = 4
# number = 4
def sum_any(*numbers):
  sum = 0
  
  for number in numbers:
    sum = sum + number
  
  return sum
  
# print("La suma de la funda de numeros =", sum_any(4, 6, 5))
