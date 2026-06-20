'''
    1. Create a new file “practice.txt” using python. 
    2. Add the following data in it: 
        Hi everyone 
        we are learning File I/O 
        using Java. 
        I like programming in Java. 
    3. WAF that replace all occurrences of “java” with “python” in above file.
    4. Search if the word “learning” exists in the file or not. 
    5. WAF to check in which line 'learning' is present in.
'''

# 1. & 2. creating the file and adding data
with open('practice.txt', 'w') as f:
    f.write('Hi everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java.')
    
# 3. replacing java with python
def replacement(file):
    data = ""
    with open(file, 'r') as f:
        data = f.read()
        data.replace('Java', 'Python')

    with open(file, 'w') as f:
        f.write(data)
replacement('practice.txt')
    
# 4. searching 'learning'
with open('practice.txt', 'r') as f:
    data = f.read()
    word = 'learning'
    if word in data:
        print(f'{word} is present in the file.')
    else:
        print(f'{word} is absent from the file.')
    
# 5. finding the line number of 'learning'
def find_line(filename, word):
    n = 1
    line = True
    with open(filename, 'r') as f:
        while line:
            line = f.readline()
            if word in line:
                print(f'{word} found in line {n}.')
                return n
            n += 1
    return -1

find_line('practice.txt', 'learning')



'''
    1. Create a file with random 10 numbers separated by commas
    2. Find the even numbers from the file
'''

with open('demo.txt', 'w') as f:
    f.write('1, 2, 3, 4, 5, 6, 7')
    
with open('demo.txt', 'r') as f:
    data = f.read()
    nums = data.split(',')
    
    for num in nums:
        if int(num) % 2 == 0:
            print(int(num), end=' ')
            
        