"""
Day 3: Quick Start

Important reminders from Day 2:
- Indentation defines code blocks.
- if / elif / else choose between paths.
- for repeats through a sequence.
- while repeats while a condition is true.
- break stops a loop.
- continue skips one loop cycle.
- pass does nothing; it is a placeholder.
- A function is created with def.
- return sends a value back.
- *args collects extra positional arguments into a tuple.
- Recursion needs a base case.
- lambda creates a small one-expression function.
- import loads code from a module.
"""


# ==========================
# QUICK REMINDERS
# ==========================

# Condition:
age = 18

if age >= 18:
    print("Adult")
else:
    print("Child")


# Loop:
for number in range(3):
    print(number)


# Function:
def add(number1, number2):
    return number1 + number2


print(add(2, 3))


# Default value:
def greet(name="Jacques"):
    print("Hello", name)


greet()
greet("Isaac")


# *args:
def find_sum(*numbers):
    return sum(numbers)


print(find_sum(2, 3, 4))


# Module:
import math

print(math.sqrt(25))

############################
def outer():
    message = 'local'
    #nested function
    def inner():
        #declare nonlocal variable
        nonlocal message
        
        message = 'nonlocal'
        print("inner:",message)
    inner()
    print("outer:", message)
    
outer()

#global variable
c = 1
def add():
    #use global keyword
    global c
    #increment c by 2
    c = c + 2
    print(c)
add()

print(c)

#global
def outer_function():
    num = 20
    
    def inner_function():
        global num
        num = 25
        
    print("Before inner:", num)
    inner_function()
    print("After inner:", num)

outer_function()
print("Outside both:", num)

"""
Python searches names using LEGB:
Local → Enclosing → Global → Built-in
"""

#from math import pi
#import math as m
#from math import *


#negative indexing
#print(languages[-1]) 	#last item
#print(languages[-3]) 	#3rd last item

#slicing
my_list = ["p", "r", "o", "g", "r", "a", "m"]
print(my_list[3:4]) 	#item 3-4 (4 wont be included)
print(my_list[3:])		#index 5 onwards
print(my_list[:])		#beginning to end
#start included, end NOT included

#add items to list
numbers = [1, 3, 5]
print("before append: ", numbers)
numbers.append(30)				#add one item
print("after append: ", numbers)

even_numbers = [4, 6, 8]
numbers.extend(even_numbers)	#add a list to another list
print("list after append:", numbers)

#insert()
numbers.insert(1, 20)		#insert at index 1, number 20
print("Insert at index 1:", numbers)

#del() remove()
del numbers[7]
print("deleted index 7", numbers)
del numbers[-1]
print("deleted last item", numbers)

numbers.remove(3)
print("delete item named 3", numbers)

#list methods
#append extend insert remove pop clear index count sort reverse copy

languages = ["python", "swift", "C++"]
for language in languages:
	print(language)
print('C' in languages)
print('python' in languages)

numbers = []
for n in range(1, 6):
    numbers.append(n**2)
print(numbers)

#creating tuple
#empty, with integers, mixed datatypes, nested tuple
#empty

# ==========================
# CREATING TUPLES
# ==========================

# Empty tuple
empty = ()
print(empty)

# Tuple with integers
numbers = (1, 2, 3, 4)
print(numbers)

# Tuple with mixed data types
mixed = ("Python", 3.12, True, 100)
print(mixed)

# Nested tuple (tuple inside a tuple)
nested = (1, 2, ("Apple", "Banana"), 4)
print(nested)

# Accessing nested tuple
print(nested[2])
print(nested[2][1])    # Banana

#nested2
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple[1])
print(my_tuple[1][2])
print(my_tuple[2][2])

#tuple with one element
var1 = ("hello")
print (type(var1))	#str
var2 = ("hello",)	#trailiing ,
print(type(var2))	#tuple

var3 = "hello",		# parentheses is optional
print(type(var3))

#remember negative indexing [-1][-3]

print(nested.count(2))

#adv of tuple over list
"""
tuple heterogeneous data
list for homogeneous data
tuple faster - because immutable
tuple can be used for dictionaries, because immutable
data that doesn't change => tuple makes it write protected
"""

#str
greet = 'hello'
print(greet[1:4])	#ell
print(greet[1])		#e
print(greet[-4])	#negative indexing


#str = immutable
greet = "hello"
greet = "H" + greet[1:]
greet[0] = 'H'

print(greet)


















