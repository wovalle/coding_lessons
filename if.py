number1 = int(input('Ingrese el primer número: '))
number2 = int(input('Ingrese el segundo número: '))
operation = input('Ingrese la operación (+ - * /): ')

result = 0
can_print = True

if operation == '+':
  result = number1 + number2
elif operation == '-':
  result = number1 - number2
elif operation == '*':
  result = number1 * number2
elif operation == '/':
  result = number1 / number2
else:
  print('Operación inválida: ', operation)
  can_print = False

if can_print:
  print('El resultado es: ', result)