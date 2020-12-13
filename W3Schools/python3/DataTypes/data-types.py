# Built-in data types
# In Python, the data type is set when you assign a value to a variable

# text type - str
a = 'Hello world'

# numeric types - int / float / complex
b = 20
c = 20.5
d = 1j

# sequence types - list / tuple / range
e  = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(0, 2)

# mapping type - dict
h = {"name" : "John", "age" : 36}

# set types - set, frozenset
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})

# boolean - bool
k = True

# binary Types - bytes, bytearray, memoryview
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))

# Getting data type of any variable - type(var)
print(a, type(a))