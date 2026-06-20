f = open('demo.txt', 'w')  # file will be overridden

f.write('Hellow!!')
f.close()

# with syntax:
with open('demo.txt', 'a+') as f:
    f.write('\nGood morning')
    f.close()
    
    
with open('demo.txt', 'r+') as f:
    print(f.read())
    # f.close() this isn't even necessary in the 'with' syntax
    
    
# deleting/removing a file
import os
os.remove('demo.txt')
print("demo.txt deleted successfully.")