# dictionary: a built-in data structure in python that stores key-value pairs. It is unordered and mutable. Dictionaries are defined using curly braces {}.

# creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}
print(student) #output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'subjects': ['Math', 'Science', 'English']}
print(type(student)) #output: <class 'dict'>

# accessing values in a dictionary using keys
print(student["name"]) #output: Alice
print(student["age"]) #output: 25
print(student["grade"]) #output: A
print(student["subjects"]) #output: ['Math', 'Science', 'English']  

# modifying values in a dictionary
student["age"] = 26
print(student["age"]) #output: 26
student["subjects"].append("History")
print(student["subjects"]) #output: ['Math', 'Science', 'English', 'History']

student["isAdult"] = True # adding a new key-value pair
print(student) #output: {'name': 'Alice', 'age': 26, 'grade': 'A', 'subjects': ['Math', 'Science', 'English', 'History'], 'isAdult': True}


'''
    keys in a dictionary must be unique and immutable (e.g. strings, numbers, tuples; but not lists), while values can be of any data type and can be duplicated.
'''


# nested dictionaries: a dictionary can contain another dictionary as a value.
student1 = {
    "name": "Bob",
    "age": 22,
    "grade": "B",
    "subjects": {
        "Math": 85,
        "Science": 90,
        "English": 78
    }
}
print(student1) #output: {'name': 'Bob', 'age': 22, 'grade': 'B', 'subjects': {'Math': 85, 'Science': 90, 'English': 78}}
print(student1["subjects"]["Math"]) #output: 85 


# dictionary methods:
print(student.keys()) #output: dict_keys(['name', 'age', 'grade', 'subjects', 'isAdult']) (returns a view object of all the keys in the dictionary)
print(student.values()) #output: dict_values(['Alice', 26, 'A', ['Math', 'Science', 'English', 'History'], True]) (returns a view object of all the values in the dictionary)
print(student.items()) #output: dict_items([('name', 'Alice'), ('age', 26), ('grade', 'A'), ('subjects', ['Math', 'Science', 'English', 'History']), ('isAdult', True)]) (returns a view object of all the key-value pairs in the dictionary as tuples) 
print(student.get("name")) #output: Alice (returns the value for the specified key, or None if the key does not exist)
print(student.update({"age": 27, "grade": "A+"})) # updates the values for the specified keys, or adds new key-value pairs if the keys do not exist
print(student) #output: {'name': 'Alice', 'age': 27, 'grade': 'A+', 'subjects': ['Math', 'Science', 'English', 'History'], 'isAdult': True}

print(len(list(student.keys()))) #output: 5 (returns the number of key-value pairs in the dictionary)
print(student.pop("isAdult")) #output: True (removes the specified key-value pair and returns the value, or raises a KeyError if the key does not exist)



# to get better output, we can convert dict to list
print(list(student.keys())) #output: ['name', 'age', 'grade', 'subjects'] (returns a list of all the keys in the dictionary)
print(list(student.values())) #output: ['Alice', 27, 'A+', ['Math', 'Science', 'English', 'History']] (returns a list of all the values in the dictionary)



# now, another thing, if we can use subscript notation to access values in a dictionary, we can also use the get() method. The difference is that if the key does not exist, the get() method will return None instead of raising a KeyError.
print(student.get("name")) #output: Alice
print(student.get("address")) #output: None (since the key "address" does not exist in the dictionary)

# same with update
print(student.update({"address": "123 Main St"})) #output: None (adds a new key-value pair to the dictionary)
# but if we try to do something similar with subscript operator, it will raise a KeyError