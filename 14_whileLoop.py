# while loops
count = 1
while count <= 5:
    print(f"hello #{count}")
    count += 1
    
# printing a list using while
nums = [1, 4, 2, 6, 3, 8, 9, 12]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
    
from clear_op import woosh
woosh()
# search for a value in a tuple
tup = (1, 4, 2, 6, 3, 8, 9, 12)
x = int(input(f"enter a value to search in the tuple: \n{tup}\n"))
i = 0
while i <= len(tup):
    if tup[i] == x:
        print(f'{x} found at position: {i+1}')
        break
    i += 1
if i == len(tup):
    print(f'{x} is not present in the tuple.')