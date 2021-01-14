_text = "Hello World"
_numeric = 10
_float = 10.5
_complex = 1j
_lists = ["appple", "banana", "mango"]
_tuple = ("appple", "banana", "mango")
_range = range(6)
_dict = {"name": "John", "age": 26}
_set = {"apple", "banana", "mango"}
_frozenset = frozenset({"appple", "banana", "mango"})
_boolean = True
_bytes = b"Hello"
_byteArray = bytearray(5)
_memView = memoryview(bytes(5))

# Text
print(_text, type(_text))
# Numeric
print(_numeric, type(_numeric), _float, type(_float), _complex, type(_complex))
# Sequence
print(_lists, type(_lists), _tuple, type(_tuple), _range, type(_range))
# Mapping
print(_dict, type(_dict))
# Set
print(_set, type(_set), _frozenset, type(_frozenset))
# Boolean
print(_boolean, type(_boolean))
# Binary
print(_bytes, type(_bytes), _byteArray, type(
    _byteArray), _memView, type(_memView))
