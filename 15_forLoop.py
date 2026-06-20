# looping through a container:
l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
s = {1, 2, 3, 4, 5}
d = {1:None, 2:None, 3:None, 4:None, 5:None}

for item in d:
    print(item, end=" ")
else:
    print('[end]')  # executes only when all the elements are iterated, meaning, won't execute if 'break' executes in the middle
    
'''
    RANGE(): returns a sequence of numbers constructed from it's arguments
    range(start=0, stop, step=1)
    start is inclusive, and stop is exclusive
'''
for i in range(1, 5, 2):
    print(i, end=" ")
else:
    print('[end]')
    
for i in range(10, -1, -2):
    print(i, end=' ')
else:
    print('[end]')