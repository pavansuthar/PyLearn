# Using py to manipulate strings
# Python can be used to manipulate strings, which can be expressed in several ways.

'''
They can be enclosed in single quotes ('...') or double quotes ("...")
'\' can be used to escape quotes
Python strings cannot be changed — they are immutable.

We will also look at the built in function called len()
This function returns the length of a string:

Strings have a bunch of methods available.
capitalize() Converts the first character to upper case
casefold() Converts string into lower case
center() Returns a centered string
count() Returns the number of times a specified value occurs in a string
encode() Returns an encoded version of the string
endswith() Returns true if the string ends with the specified value
expandtabs() Sets the tab size of the string
find() Searches the string for a specified value and returns the position of where it was found
format() Formats specified values in a string
format_map() Formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
isalnum() Returns True if all characters in the string are alphanumeric
isalpha() Returns True if all characters in the string are in the alphabet
isascii() Returns True if all characters in the string are ascii characters
isdecimal() Returns True if all characters in the string are decimals
isdigit() Returns True if all characters in the string are digits
isidentifier() Returns True if the string is an identifier
islower() Returns True if all characters in the string are lower case
isnumeric() Returns True if all characters in the string are numeric
isprintable() Returns True if all characters in the string are printable
isspace() Returns True if all characters in the string are whitespaces
istitle() Returns True if the string follows the rules of a title
isupper() Returns True if all characters in the string are upper case
join() Converts the elements of an iterable into a string
ljust() Returns a left justified version of the string
lower() Converts a string into lower case
lstrip() Returns a left trim version of the string
maketrans() Returns a translation table to be used in translations
partition() Returns a tuple where the string is parted into three parts
replace() Returns a string where a specified value is replaced with a specified value
rfind()	 Searches the string for a specified value and returns the last position of where it was found
rindex() Searches the string for a specified value and returns the last position of where it was found
rjust() Returns a right justified version of the string
rpartition() Returns a tuple where the string is parted into three parts
rsplit() Splits the string at the specified separator, and returns a list
rstrip() Returns a right trim version of the string
split() Splits the string at the specified separator, and returns a list
splitlines() Splits the string at line breaks and returns a list
startswith() Returns true if the string starts with the specified value
strip() Returns a trimmed version of the string
swapcase() Swaps cases, lower case becomes upper case and vice versa
title() Converts the first character of each word to upper case
translate() Returns a translated string
upper() Converts a string into upper case
zfill() Fills the string with a specified number of 0 values at the beginning
'''

# Basics
eggs = '"Yes," they said, they doesn\'t spam eggs'
print(eggs)
lines = 'First line\nSecond line'
print(lines)  # py interpretor prints like 'First line\nSecond line'
print(r'C:\some\name')  # reg x prints as raw string as print() inserts new line

# String literals
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Concatenated
times = 3 * 'un' + 'ium'
print(times)
'Did' 'Coding'  # 'DidCoding'
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Did'
print(prefix + ' Coding')
# print(prefix 'Coding') # This only works with two literals, not with variables or expressions

# Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''
word = 'Didcoding'
print(word[5])  # character in position 5
# characters from position x (included) to y (excluded)
print(word[0:2])
print(word[2:5])
# character from the beginning to position y (excluded)
print(word[:2])
# character from the position 4 (included) to the end
print(word[4:])
print(word[:2] + word[2:])
print(word[-2:]) # characters from the second-last (included) to the end
# Changing strings
# word[0] = 'P' # TypeError: 'str' object does not support item assignment
print('P' + word[1:])

# String length
print(len(word))

# Handy built-in functions
'''
When you don’t need fancy output but just want a quick display 
of some variables for debugging purposes, you can convert any 
value to a string with the repr() or str() functions.

The str() function is meant to return representations of values 
which are fairly human-readable, while repr() is meant to generate 
representations which can be read by the interpreter
You also have format().

The format() method formats the specified value(s) and insert them 
inside the string's placeholder '{}'.
'''

x = 200
y = 400
print(repr((x, y, ('spam', 'eggs'))))
print(str((x, y, ('spam', 'eggs'))))
print('{0} {1}'.format('spam', 'eggs'))
print('{0} {1}'.format('eggs', 'spam'))
