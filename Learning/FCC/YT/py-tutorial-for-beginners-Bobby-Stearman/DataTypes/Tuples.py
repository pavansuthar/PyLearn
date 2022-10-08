# Using python to manipulate tuples

'''
Python knows a number of compound data types, 
used to group together other values.
They are:
tuple
dictionary
set
list
Tuples are written as a list of comma-separated 
values (items) between parentheses.
Tuples are immutable - this means that items can not be changed. However,
a tuple can contain mutable objects.
Tuple has 2 methods available.
count()	Returns the number of elements with the specified value
index() Returns the index of the first element with the specified value
'''

# Basics - tuple packing
t = 12345, 54321, 'hello!'
print(t[0])

# Tuples can be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuple are immutable
# t[0] = '12345' # typeError: 'tuple' object does not support item assignment

# But they can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 2
print(v)

# Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''
print(t[2])
print(t[-2])

# Trailing comma
empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

# Unpacking a tuple
a, b, c = t
print(a, b, c)

# Builtin functions
tlist = tuple(['bobby', 'at', 'discoding', 'dot', 'com'])
print(tlist)

# Tuple comprehension...Just use list comprehension with the tuple function
tuple([x**2 for x in range(10)])
