# if statements:
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    
# ternary operator
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)

# clever if statement
age = int(input("Enter your age: "))
vote = ('yes', 'no')[age > 18]
print(vote)


# loops:
for i in range(10):
    print(i)
    
# range() function can take 3 arguments: start, stop, step
for i in range(1, 10, 2):
    print(i)
    
# reverse loop
for i in range(10, 0, -1):
    print(i)
    
# different ways to loop through a list
my_list = ['a', 'b', 'c', 'd']
for item in my_list:
    print(item)
    
for i in range(len(my_list)):
    print(my_list[i])


    
# while loop
count = 0
while count < 5:
    print(count)
    count += 1  
    