"""
You have to use the same number of spaces in the same block of code, otherwise Python will give you an error: EXAMPLE
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
# Python has no command for declaring a variable.
x = 5
y= "Hello World!"

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) #Sally

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>

#String variables can be declared either by using single or double quotes.

a = 4
A = "Sally"
#A will not overwrite a.

#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"
#Remember that variable names are case-sensitive

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"

#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"

#Unpack a Collection
#unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)# The Python print() function is often used to output variables.
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # Python is awesome

x = 5
y = 10
print(x + y) # 15

""""
x = 5
y = "John"
print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

#Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc() #Python is fantastic

print("Python is " + x) #Python is awesome
