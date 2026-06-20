#datatypes: python is an implicitly typed language, meaning you don't have to declare the type of a variable when you create it. The interpreter infers the type based on the value assigned to the variable.

name = "John" #string
name1 = 'Doe' #string
name2 = """Smith""" #string
name3 = '''Johnson''' #string
age = 30 #integer
height = 1.75 #float
is_student = True #boolean
a = None #NoneType

print(type(name)) #output: <class 'str'>
print(type(age)) #output: <class 'int'>
print(type(height)) #output: <class 'float'>
print(type(is_student)) 



#lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) #output: apple
fruits.append("orange") #adds orange to the list
print(fruits) #output: ['apple', 'banana', 'cherry', 'orange
fruits.remove("banana") #removes banana from the list
print(fruits) #output: ['apple', 'cherry', 'orange']

#dictionaries
person = {"name": "John",
"age": 30,
"height": 1.75,"is_student": True}
print(person["name"]) #output: John
person["age"] = 31 #updates age to 31
print(person) #output: {'name': 'John', 'age': 31, 'height': 1.75, 'is_student': True}

#tuples
coordinates = (10, 20) #tuple
print(coordinates[0]) #output: 10
#coordinates[0] = 15 #this will raise an error because tuples are immutable

