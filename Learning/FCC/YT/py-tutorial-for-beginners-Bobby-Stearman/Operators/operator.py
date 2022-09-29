# Using py as calculator
# Using interpreter to take an input and return an output

# Arthimetic operators
'''
+ Addition
- Subtraction
* Multiplication
/ Division (returns float which is number type, i.e 10 / 4 is 2.5)
// Floor division (returns integer version, i.e 10 / 4 is 2) 
% Modulus (returns remainder of x / y, i.e remainder of 10 % 4 is 2) | use divmod(a, b)
** Exponentation (power of) | can also use pow(x, y) instead of x ** y
'''
print(2 + 2)
print(3 - 6)
print(7 * 10)
print(10 / 4)
print(10 // 4)
print(10 % 4)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4) # Division returns float
print(5 * 3 + 2)
print(5 ** 2)

# Assignment operators
'''
= Equals
and others ...
'''
width = 60
height = 3 * 7
tax = 12.5 / 1000
price = 100.50

# Number types
'''
int (2, 3, 458, 678)
float (2.2, 3.5, 5.666675678)
'''
print(width * height)
price * tax # In interactive mode, last printed exp is assigned to the variable _
print(price + _) # we reference _ but this exp is now assigned to _

# Built in functions
'''
round() (rounds a number with specific no of decimals, i.e round(5.666675678, 2) is 5.67)
divmod(a, b)
pow(x, y)
'''
print(divmod(10, 4)) # does 2 calcualtions floor division with modulus
print(pow(5, 2))
round(_, 2)

# Big int
'''
py has handly way of making big int's easier to read 4000000000 can be written as 4_000_000_000
'''
