# Calc C -> F and F -> C

# F = var * 1.8 + 32
# C = (F − 32) × 5/9 

# Print Menu
print('Temperature calculator')
print('Type 1 to convert from Celsius to Fahrenheit')
print('Type 2 to convert from Fahrenheit to Celsius')

# Ask for value and store into a variable
value = float(input('Enter the value to convert: '))

option = float(input('Enter the option: '))

# if the user selected 1, convert to F
if (option == 1):
  value_in_f = value * 1.8 + 32
  print('{} degrees celcius equals {} degrees farenheit'.format(value, value_in_f))
elif (option == 2):
  value_in_c = (value - 32) * (5/9)
  print('{} degrees farenheit equals {} degrees celcius'.format(value, value_in_c))
else:
  print('Ute ta en droga manito?, la opción {} no es valida'.format(option))
  