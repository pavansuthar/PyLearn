import random

# Numbers - int / float / complex
x = 1
y = 1.5
z = 1j

print(x, y, z)

# Verify type
print(type(x))

# Int
a = 1
b = 35656222554887711
c = -3255522
print(type(a), type(b), type(c))

# Float
#  "e" to indicate the power of 10
d = 1.10
e = 1.0
f = -35.59
g = 35e3
h = 12E4
print(type(d), type(e), type(f))
print(g, h)

# Complex
# Are written with a "j" as the imaginary part
i = 3+5j
j = 5j
print(i, j)

# Type conversion
# You cannot convert complex numbers into another number type
floatToInt = float(1)
IntToFloat = int(2.8)
IntToComplex = complex(floatToInt)
print(floatToInt, IntToFloat, IntToComplex)
print(type(floatToInt), type(IntToFloat), type(IntToComplex))

# Generate random numbers
print(random.randrange(1,5))