# String
# 'same' as this "same"
a = "Hello"
print(a)

# line breaks are inserted at the same position as in the code
# """ or '''
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# strings in Python are arrays of bytes representing unicode characters
print(b[4])

# loop throught String 
for loopStr in a:
  print(loopStr)

# Check length
print(len(a))

# Check string
print("do" in b)
print("do" not in b)

# String concat
d = "Hello"
e = "World"
f = d + e
print(f)

# format string 
# can combine strings and numbers by using the format() method
# method takes unlimited number of arguments
age = 36
h = "My name is John, I am {}"
print(h.format(age))

# can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."