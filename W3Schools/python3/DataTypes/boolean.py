# Boolean
# evaluate any expression
print(10 > 9)
print(10 == 10)
print(10 < 9)

# run a condition in an if statement
a = 10
b = 20
if a < b:
  print("Yes b is greater than a")
else:
  print("No! b is not greater than a")

# evaluate values and variables
# True
print(bool("abc"), bool(123), bool(["apple"]))

# False
print(bool(""), bool(0), bool([]), bool({}), bool(()), bool(None))

# built-in functions that returns a boolean value
c = 100
print(isinstance(c, int))