# set: a built-in data structure in python that stores unique elements(duplicates would just be ignored). It is unordered and mutable. But each item must be immutable(eg Strings, numeric constants, tuples).
# Why the elements must be immutable? -> because we have to hash them 
# Sets are defined using curly braces {} or the set() constructor.

# creating a set
fruits = {"apple", "banana", "orange", "apple"} # duplicate "apple" will be ignored
print(fruits) #output: {'banana', 'orange', 'apple'}
print(type(fruits)) #output: <class 'set'>

# creating an empty set
empty_set = set()
print(empty_set) #output: set()
print(type(empty_set)) #output: <class 'set'>

# adding elements to a set
fruits.add("grape")
print(fruits) #output: {'banana', 'orange', 'apple', 'grape'}

# removing elements from a set
fruits.remove("banana")
print(fruits) #output: {'orange', 'apple', 'grape'}
# fruits.remove("guava") # as the element doesn't exist, it gives KeyError

# checking if an element is in a set
print("apple" in fruits) #output: True
print("banana" in fruits) #output: False

# set operations:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union of two sets
union_set = set1.union(set2)
print(union_set) #output: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set) #output: {4, 5}

# difference of two sets
difference_set = set1.difference(set2)
print(difference_set) #output: {1, 2, 3}

# symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) #output: {1, 2, 3, 6, 7, 8}

# popping a random value from the set:
print(fruits.pop())

# clearing a set
fruits.clear() # empties the set
print(fruits) #output: set()

