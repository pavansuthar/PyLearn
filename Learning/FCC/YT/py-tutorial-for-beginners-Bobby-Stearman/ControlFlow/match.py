# py control flows - Match statement

'''
Hot off the press in Python 3.10
Structural pattern matching has been added in the form of a match 
statement and case statements of patterns with associated actions. 

Patterns consist of sequences, mappings, primitive data types as 
well as class instances. Pattern matching enables programs to extract 
information from complex data types, branch on the structure of data, 
and apply specific actions based on different forms of data.

A match statement takes an expression and compares its value to 
successive patterns given as one or more case blocks.

Note: We have a class in this demo. Don't get too caught up in how it
works! We have a class video in this course :)
'''

# Basics


from dataclasses import dataclass


def http_status(status):
    match status:
        case 400:
            return 'Bad request'
        case 401 | 403:
            return 'Not allowed'
        case 404:
            return 'Not found'
        case 418:
            return 'Im a tapot'
        case _:
            return 'Something went wrong with the internet'


print(http_status(404))
print(http_status(401))

# Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple


def http_statusCheck(status):
    match status:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y={y}')
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            print('Not a point')


point_tuple = (0, 0)
http_statusCheck(point_tuple)
point_tuple = (0, 10)
http_statusCheck(point_tuple)
point_tuple = (20, 10)
http_statusCheck(point_tuple)

# Match class


@dataclass
class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


where_is(Point(0, 0))
where_is(Point(0, 10))
where_is(Point(10, 0))
where_is(Point(10, 10))
