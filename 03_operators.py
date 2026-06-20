#different types of operators:

#arithmetic operators
print(2 + 3) #addition
print(5 - 2) #subtraction
print(4 * 3) #multiplication
print(2 ** 3) #exponentiation (2 raised to the power of 3)

#different types of divisions
print(10 / 3) #output: 3.3333333333333335 (float division)
print(10 // 3) #output: 3 (integer division rounds down to negative infinity)
print(-10 // 3) #output: -4 
print(10 % 3) #output: 1 
# a%b = a - (a//b)*b
print(10 - (10 // 3) * 3) #output: 1
print(10 % -3) #output: -2
print(-10 % -3) #output: -1
# output of modulo operator has the same sign as the divisor


#comparison operators
print(5 > 3) #greater than
print(2 < 4) #less than
print(6 >= 6) #greater than or equal to
print(3 <= 5) #less than or equal to
print(4 == 4) #equal to
print(7 != 2) #not equal to


#logical operators
print(True and False) #logical AND
print(True or False) #logical OR
print(not True) #logical NOT


#bitwise operators
print(5 & 3) #bitwise AND (0101 & 0011 = 0001, output: 1)
print(5 | 3) #bitwise OR (0101 | 0011 = 0111, output: 7)
print(5 ^ 3) #bitwise XOR (0101 ^ 0011 = 0110, output: 6)
print(~5) #bitwise NOT (~0101 = 1010, output: -even though the result is -6, it is represented in two's complement form as 1010)
print(5 << 1) #left shift (0101 << 1 = 1010, output: 10)
print(5 >> 1) #right shift (0101 >> 1 = 0010, output: 2)


#assignment operators
x = 5 #assignment
x += 3 #add and assign (x = x + 3)
print(x) #8
x -= 2 #subtract and assign (x = x - 2)
print(x) #6
x *= 4 #multiply and assign (x = x * 4)
print(x) #24
x /= 2 #divide and assign (x = x / 2)
print(x) #12.0
x %= 5 #modulus and assign (x = x % 5)
print(x) #2.0


#membership operators
print('a' in 'apple') #output: True (checks if 'a' is a substring of 'apple')
print('b' in 'apple') #output: False (checks if 'b' is a substring of 'apple')
print('p' not in 'apple') #output: False (checks if 'p' is not a substring of 'apple')
print('x' not in 'apple') #output: True (checks if 'x' is not a substring of 'apple')


#identity operators
a = [1, 2, 3]
b = a #b references the same list as a
c = [1, 2, 3] #c is a different list with the same contents as a
print(a is b) #output: True (a and b reference the same object in memory)
print(a is c) #output: False (a and c reference different objects in memory)
print(a == c) #output: True (a and c have the same contents, so they are considered equal)