# tuples: a built-in data structure in python that is similar to lists but is immutable. They are defined using parentheses ().
# creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits) #output: ('apple', 'banana', 'cherry')
print(type(fruits)) #output: <class 'tuple'>

# accessing elements in a tuple using indexing, just like lists

''' 
modifying elements in a tuple is not allowed, it will raise a TypeError
fruits[0] = "grape" #output: TypeError: 'tuple' object does not support item assignment
'''


# tuple methods: tuples have only two built-in methods: count() and index()
print(fruits.count("banana")) #output: 1 (returns the number of occurrences of "banana")
print(fruits.index("cherry")) #output: 2 (returns the index of the first occurrence of "cherry")


# python treats a single value followed by a comma as a tuple, even if it is not enclosed in parentheses
single_tuple = "apple",
print(single_tuple) #output: ('apple',)
print(type(single_tuple)) #output: <class 'tuple'>

# but if we create a tuple with only single integer without a comma, it will be treated as a int
not_a_tuple = (5)
print(not_a_tuple) #output: 5
print(type(not_a_tuple)) #output: <class 'int'>

# the correct way to create a tuple with a single integer is to include a comma after the value
single_int_tuple = (5,)
print(single_int_tuple) #output: (5,)
print(type(single_int_tuple)) #output: <class 'tuple'>