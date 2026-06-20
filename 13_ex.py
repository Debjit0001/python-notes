'''
    Problem: You're given a list of subjects picked by a group of students. Assume one classroom is required for teaching each subject. How many total classrooms would be required for :
    [python, java, cpp, python, js, java, python, java, cpp, cpp]
'''

sub = ['python', 'java', 'cpp', 'python', 'js', 'java', 'python', 'java', 'python', 'cpp', 'c']
unique_sub = set(sub)
print(f"number of classrooms required = {len(list(unique_sub))}")


'''
    Problem: store the marks inputted by user, of each subject
'''
sub = input(f'enter 3 subjects (separated by spaces)\n').split()
marks = {}
for s in sub:
    m = int(input(f"marks obtained in {s}: "))
    marks.update({s : m})

print(marks)

