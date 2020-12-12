# Variable naming
# Case sensitive | must start with a letter or _ , no numbers | can only contain alpha-numeric characters and underscores

_letter1 = 'abc'

camelCaseVariable = 'pavans'
PascalCaseVariable = 'pavans'
snake_case_variable = 'pavans'

print(camelCaseVariable)

# Assigning values in one line

# Many Values to Multiple Variables
# Make sure the number of variables matches the number of values
x, y, z = 'Orange', 'Banana', 'Grapes'
print(x, y, z)

# One Value to Multiple Variables
a = b = 'letters'
print(a, b)

# unpacking list
fruits = ["apple", "banana", "cherry"]
fr1, fr2 ,fr3 = fruits
print(fr1, fr2, fr3, type(fruits))
