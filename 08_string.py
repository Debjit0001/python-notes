# strings are immutable in python.
str1 = "Hello"
str2 = "World"
# concatenation of strings using + operator
print(str1 + " " + str2) #output: Hello World

# escaping characters in strings using \ character
str3 = "This is a \"string\" with quotes."
print(str3) #output: This is a "string" with quotes.    

print("This is a string with a backslash \\ character.") #output: This is a string with a backslash \ character.
print("This is a string with a new line \n character.") #output: This is a string with a new line character.


# indexing and slicing of strings
str4 = "Python Programming"
print(str4[0]) #output: P (first character)
print(str4[-1]) #output: g (last character)
print(str4[0:6]) #output: Python (first 6 characters)
print(str4[7:18]) #output: Programming (from index 7 to index 17)
print(str4[:6]) #output: Python (from the beginning to index 6)
print(str4[7:18]) #output: Programming (from index 7 to index 17)
print(str4[7:len(str4)]) #output: Python Programming (the whole string)
print(str4[::2]) #output: Pto rgamn (every 2nd character)
print(str4[::-1]) #output: gnimmargorP nohtyP (reverse the string)
print(str4[5:0:-1]) #output: nohty (reverse from index 5 to index 1)
print(str4[5:0:-2]) #output: nh (reverse every 2nd character from index 5 to index 1)


# string methods:
str5 = "   Hello World   "
print(str5.strip()) #output: Hello World (removes leading and trailing whitespace)
print(str5.upper()) #output:    HELLO WORLD    (converts to uppercase)
print(str5.lower()) #output:    hello world    (converts to lowercase)
print(str5.replace(" ", "_")) #output: ___Hello_World___ (replaces spaces with underscores)
print(str5.split()) #output: ['Hello', 'World'] (splits the string into a list of words)
print(str5.find("World")) #output: 3 (returns the index of the first occurrence of "World")
print(str5.count("o")) #output: 2 (returns the number of occurrences of "o")

str6 = "a, b, c, d"
splits = str6.split(", ")
print(splits) #output: ['a', 'b', 'c', 'd']
print(", ".join(splits)) #output: a, b, c, d (joins the list of strings into a single string with ", " as the separator)

str7 = "Hello World"
print(str7.startswith("Hello")) #output: True (checks if the string starts with "Hello")
print(str7.endswith("World")) #output: True (checks if the string ends with "World")
print(str7.isalpha()) #output: False (checks if the string contains only alphabetic characters)
print(str7.isdigit()) #output: False (checks if the string contains only digits)