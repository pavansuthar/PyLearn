# Global variables: Variables that are created outside of a function
x = 'awesome'

def myfunc():
  # Local variables can only be used inside the function
  x = 'fantastic'
  print("Python is " + x)

myfunc()
print("Python is " + x)

# Making variable GLOBAL
def makeVarGlobal():
  # change a global variable inside a function
  global x
  x = 'super awesome'

  # create a global variable inside a function
  global y
  y = 'yes of course!'
  print("Python is " + x, y)

makeVarGlobal()

print(y)