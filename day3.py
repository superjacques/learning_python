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































