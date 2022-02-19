# Escribe una función para calcular el factorial de un número (n!)
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 5! = 5 x 4! = 5 x 4 x 3! = 5 x 4 x 3 x 2! = 2 x 1!
# 0! = 1
# 1! = 1

# Algoritmos iterativos (while)
def factorial(n):
  result = 1
  while (n > 1):
    result *= n
    n = n - 1
  
  return result

# Algoritmos iterativos (for)
def factorial_for(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  
  return result

# Algoritmos recursivos
# 1- condición de salida, caso base 
# 2- Que se llame a sí misma

def factorial_rec(n):
  if (n <= 1):
    return n

  return n * factorial_rec(n-1) 

# fact(5) => 5 * fact(4)
# fact(4) => 4 * fact(3)
# fact(3) => 3 * fact(2)
# fact(2) => 2 * fact(1)
# fact(1) => 1

# fact(2) => 2 * fact(1) = 2 * 1 = 2
# fact(3) => 3 * fact(2) = 3 * 2 = 6
# fact(4) => 4 * fact(3) = 4 * 6 = 24
# fact(5) => 5 * fact(4) = 5 * 24 = 120

# print('Factorial de 5' , factorial(5))
# print('Factorial (for) de 5' , factorial_for(5))
# print('Factorial (recursivo) de 5' , factorial_rec(5))


# Secuencia de fibonacci
# f(n) = f(n-1) + f(n-2); f(0) = 0 y f(1) = 1

def fib(n):
  if(n == 0):
    return 0
  elif(n == 1):
    return 1
  
  return fib(n - 1) + fib(n - 2)


print('Fib de 6:' , fib(6))
print('Fib de 10:' , fib(10))

# Imprime todos los numeros de 1 a n utilizando una funcion recursiva
# f(4)= 5 + 4 + 4



