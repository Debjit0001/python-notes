# type conversion:
a, b = 1, 2.5
print(a+b) #output: 3.5, (works fine)

a, b = 1, '2.5'
print(a+b) #output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# to fix this, we need to convert the string to a number using int() or float() function
a, b = 1, '2.5'
print(a + float(b)) #output: 3.5, (works fine) 