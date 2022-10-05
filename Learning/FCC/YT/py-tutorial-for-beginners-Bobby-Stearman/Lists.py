#Using python to manipulate lists

'''
Python knows a number of compound data types, 
used to group together other values. The most
versatile of which is a list.
Others include:
tuple
dictionary
set
Lists are written as a list of comma-separated 
values (items) between square brackets
Lists are mutable - this means that items can be changed
List have a bunch of methods available.
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy() Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

# Basics
squares = [1, 4, 9, 16, 25]
print(squares)

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''
print(squares[0])
print(squares[-1])
print(squares[-3:]) # slicing returns a new list

# Create a list copy
print(squares[:])

# Concatenation (glue together)
print(squares + [36, 49, 64, 81, 100])

# Alter items
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

# List methods
cubes.append(216)
cubes.append(7**3)
print(cubes)
print(len(cubes))

# Nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0][1])

# List comprehension
y = []
for x in range(10):
    y.append(x**2)
# y = [x**2 for x in range(10)]

# Built-in function list()
x = list(('bobby', 'at', 'didcoding', 'dot', 'com'))
print(x)