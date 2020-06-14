# Escriba un programa que me devuelva la suma hasta n (con un while)

# Usuario ingresa 5 (1,2,3,4,5)
# Imprime: Suma: 15
# num = int(input('Dame el número de la sumatoria: ')) # 5
# i = 0
# sum = 0

# while i <= num:
#   sum = sum + i # sum += i
#   i = i + 1 # i += 1

# print('La sumatoria es: ', sum)



# Escriba un programa que me devuelva la suma hasta n de los numeros pares y de los numeros impares
# Usuario ingresa 5
# Imprime: Suma números pares: 6
# Imprime: Suma números impares: 9

num = 5 #int(input('Dame el número: '))
i = 0
sum_even = 0
sum_odd = 0

while i <= num:
  sum_even += i
  i += 2

i = 1
while i <= num:
  sum_odd += i
  i += 2

# print('La sumatoria de los números pares: ', sum_even)
# print('La sumatoria de los números impares: ', sum_odd)


# En un solo while

num = int(input('Dame el número: '))
i = 0
sum_even = 0
sum_odd = 0

while i <= num:
  if i % 3 == 0 and i != 0:
    print ('El número: ', i, ' es divisible entre 3')
    if i % 2 == 0:
      print ('El número: ', i, ' es divisible entre 3 y 2')

  if i % 2 == 0:
    sum_even += i
  else:
    sum_odd += i

  i += 1

print('La sumatoria de los números pares: ', sum_even)
print('La sumatoria de los números impares: ', sum_odd)


