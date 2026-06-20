name = input("What is your name? ") #input() function takes user input as a string
print("Hello, " + name + "!") #output: Hello, [name]!


age = input("How old are you? ") #input() function takes user input as a string
age = int(age) #convert the input string to an integer using int() function
print("You are " + str(age) + " years old.") #output: You are [age] years old. (str() function converts age back to a string for concatenation)


height = input("What is your height in meters? ") #input() function takes user input as a string
height = float(height) #convert the input string to a float using float() function
print("Your height is " + str(height) + " meters.") #output: Your height is [height] meters. (str() function converts height back to a string for concatenation)


is_student = input("Are you a student? (yes/no) ") #input() function takes user input as a string
is_student = is_student.lower() #convert the input string to lowercase for easier comparison
if is_student == "yes":
    print("You are a student.") #output: You are a student.
elif is_student == "no":
    print("You are not a student.") #output: You are not a student.
else:
    print("Invalid input. Please enter 'yes' or 'no'.") #output: Invalid input. Please enter 'yes' or 'no'.
    