# In python, strings and numerical values can be combined in expressions using operators. The most common operators are +, -, *, /, and %.

print("Hello" + " " + "World") #output: Hello World

a, b = 2, 3
txt = '*'
print(txt * a * b) 

p, q = 'a', 7
txt1 = '^'
print((txt1 + p) * q)

# combining other data types in expressions
a, b = 5, 10.0
print(a + b) #output: 15.0, (float + int = float)
name = "Alice"
age = 25
print(name + " is " + str(age) + " years old.") #output: Alice is 25 years old. (str + int = str, so we need to convert age to a string using str() function)   

