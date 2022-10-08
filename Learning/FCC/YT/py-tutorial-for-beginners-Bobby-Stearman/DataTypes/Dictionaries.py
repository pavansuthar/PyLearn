# Using python to manipulate dictionary

'''
Python knows a number of compound data types, 
used to group together other values. One of the
most used is a dictionary
Others include:
tuple
list
set
Dictionaries are used to store data values in key:value pairs.
some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}
Dictionaries are mutable - this means that item values can be changed
Dictionaries have a bunch of methods available.
clear() Removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys() Returns a dictionary with the specified keys and value
get() Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys() Returns a list containing the dictionary's keys
pop() Removes the element with the specified key
popitem() Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: 
insert the key, with the specified value
update() Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary
'''

# The Basic
from dis import show_code


some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}
print(some_dict)
# print(some_dict[0]) #KeyError: 0 will return error as you need to ref the key by name
print(some_dict['a_key'])

# Create a dict copy
some_dict.copy()

# Alerting a dict
some_dict['a_key'] = 'a_value_new'
print(some_dict)

# Length
len(some_dict)

# Show all keys and values
print(some_dict.keys())
print(some_dict.values())

# Dict comprehension
{x: x**2 for x in (2, 4, 6)}

# built-in function dict()
x = dict(a=1, b=2, c=3, d=4)  # creates a dictionary object
print(x)