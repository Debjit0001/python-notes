# lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [].
# creating a list
marks = [85, 90, 78, 92, 88]
print(marks) #output: [85, 90, 78, 92, 88]
print(type(marks)) #output: <class 'list'>

# accessing elements in a list using indexing
print(marks[0]) #output: 85 (first element)
print(marks[-1]) #output: 88 (last element)
print(marks[1:4]) #output: [90, 78, 92] (from index 1 to index 3)
print(marks[:3]) #output: [85, 90, 78] (from the beginning to index 2)
print(marks[2:]) #output: [78, 92, 88] (from index 2 to the end)
print(marks[::2]) #output: [85, 78, 88] (every 2nd element)
print(marks[::-1]) #output: [88, 92, 78, 90, 85] (reverse the list)

# modifying elements in a list
marks[0] = 95
print(marks) #output: [95, 90, 78, 92, 88]  


# list methods:
marks.append(100) # adds 100 to the end of the list: [95, 90, 78, 92, 88, 100]
marks.insert(2, 85) # inserts 85 at index 2: [95, 90, 85, 78, 92, 88, 100]
marks.remove(78) # removes the first occurrence of 78: [95, 90, 85, 92, 88, 100]
marks.pop() # removes the last element: [95, 90, 85, 92, 88]
marks.sort() # sorts the list in ascending order: [85, 88, 90, 92, 95]
marks.reverse() # reverses the list: [95, 92, 90, 88, 85]
# sorting a list in descending order
marks.sort(reverse=True) # sorts the list directly in descending order: [95, 92, 90, 88, 85]
marks.pop(1) # removes the element at index 1: [95, 90, 88, 85]




# WAP to check if a list is palindrome or not (using 1. copy() 2. slicing)
def is_palindrome1(lst):
    # method 1: using copy() method : returns a shallow copy of the list.
    lst_copy = lst.copy()
    lst_copy.reverse()
    if lst == lst_copy:
        return True
    else:
        return False
    
def is_palindrome2(lst):
    # method 2: using slicing
    if lst == lst[::-1]:
        return True
    else:
        return False