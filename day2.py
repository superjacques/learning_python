"""
Day 2: Flow Control, Functions, Modules, and Recursion

Topics covered:
- Day 1 container recap
- if, elif, else, and nested conditions
- Conditional expressions
- for and while loops
- range()
- break, continue, pass, and loop else blocks
- Iterating through lists
- Outer and inner functions
- Basic classes and placeholder blocks
- Creating and calling functions
- Parameters, arguments, and return values
- Default and keyword arguments
- Arbitrary positional arguments (*args)
- Built-in functions
- Importing modules
- Recursion and factorials
- Lambda functions
"""


# ==========================
# DAY 1 CONTAINER RECAP
# ==========================

"""
List
- Ordered
- Changeable
- Duplicates allowed
- Uses square brackets: []

Tuple
- Ordered
- Fixed / immutable
- Duplicates allowed
- Uses round brackets: ()

Set
- Unordered
- Unique values only
- Uses curly brackets: {}

Dictionary
- Stores key-value pairs
- Keys must be unique
- Uses curly brackets: {"key": "value"}

Best uses:
- List: a collection that changes, such as tasks or students
- Tuple: fixed data, such as GPS coordinates or RGB colours
- Set: unique items, such as employee IDs or permissions
- Dictionary: looking up a value by a key, such as product → price
"""


# ==========================
# IF / ELSE
# Choose between two paths
# ==========================

age = 18

if age >= 18:
    print("Adult")
else:
    print("Child")


# ==========================
# IF / ELIF / ELSE
# Choose between multiple paths
# ==========================

mark = 78

if mark >= 80:
    print("Distinction")
elif mark >= 65:
    print("Very good!")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")


# ==========================
# NESTED IF / ELSE
# One condition inside another
# ==========================

age = 18
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Fetch your ID")
else:
    print("Too young")


# ==========================
# CONDITIONAL EXPRESSION
# One-line if / else
# ==========================

age = 60
category = "Adult" if age >= 50 else "Child"

print(category)


# ==========================
# FOR LOOPS
# Repeat code for each item
# ==========================

print("For loop:")

for number in range(3):
    print(number)


# range() includes the starting value but excludes the stopping value.

count_limit = 5

for number in range(0, count_limit):
    print(number)


# ==========================
# WHILE LOOPS
# Repeat while a condition remains true
# ==========================

print("While loop:")

count = 0

while count < 3:
    print(count)
    count += 1


# ==========================
# BREAK
# Stop a loop completely
# ==========================

print("Break:")

for number in range(10):
    if number == 5:
        break

    print(number)


# ==========================
# CONTINUE
# Skip the current iteration
# ==========================

print("Continue:")

for number in range(5):
    if number == 2:
        continue

    print(number)


# ==========================
# PASS
# Placeholder that does nothing
# ==========================

if age >= 18:
    pass


# ==========================
# ITERATING THROUGH A LIST
# ==========================

words = ["Python", "is", "great"]

# Iterate using indexes:
for index in range(len(words)):
    print(words[index])

# Iterate directly through the values:
for word in words:
    print(word)

# Repeat an action once per item:
for _ in words:
    print("I love Python")


# ==========================
# LOOP ELSE BLOCKS
# Runs when a loop finishes normally
# Does not run if the loop exits with break
# ==========================

digits = [0, 3, 7]

for digit in digits:
    print(digit)
else:
    print("No items left")


counter = 0

while counter < 5:
    print("Inside loop")
    counter += 1
else:
    print("Inside else")


# ==========================
# BREAK IN A WHILE LOOP
# ==========================

count = 1

while count < 5:
    print(count)

    if count == 3:
        break

    count += 1


# ==========================
# INFINITE LOOP WARNING
# ==========================

"""
This version creates an infinite loop when count reaches 3:

count = 1

while count < 5:
    if count == 3:
        continue

    print(count)
    count += 1

Why?
- When count becomes 3, continue jumps back to the start.
- count += 1 is skipped.
- count therefore remains 3 forever.

Safe version:
"""

count = 1

while count < 5:
    if count == 3:
        count += 1
        continue

    print(count)
    count += 1


# ==========================
# OUTER AND INNER FUNCTIONS
# Indentation determines nesting
# ==========================

def first():
    print("Starting")

    def second():
        print("Inside")

    second()


first()


# ==========================
# CLASS AND PASS
# ==========================

class Example:
    """An empty example class."""

    pass


def placeholder_function(argument):
    """A placeholder function that currently does nothing."""

    pass


# ==========================
# CREATING AND CALLING FUNCTIONS
# ==========================

def greet_world():
    print("Hello world")


greet_world()


# ==========================
# FUNCTION PARAMETERS
# ==========================

def add_numbers(number1, number2):
    result = number1 + number2
    print("Sum is:", result)


add_numbers(1, 8)


# ==========================
# RETURN VALUES
# print() displays a value.
# return sends a value back to the caller.
# ==========================

def add(number1, number2):
    return number1 + number2


answer = add(5, 3)
print("Answer:", answer)


def find_square(number):
    return number * number


square_result = find_square(5)

print("Square is:", square_result)
print("Square is:", find_square(6))


# ==========================
# BOOLEAN COMPARISONS
# True behaves like 1 and False like 0
# ==========================

print(True > False)
print(True < False)


# ==========================
# IMPORTING MODULES
# ==========================

import math

square_root = math.sqrt(4)
print("Square root of 4:", square_root)

print(math.sqrt(25))      # 5.0
print(math.pow(2, 3))     # 8.0
print(math.floor(3.9))    # 3
print(math.ceil(3.1))     # 4
print(math.pi)            # 3.14159...

print(type(math.sqrt(25)))

converted_root = int(math.sqrt(35))
print(type(converted_root))
print(converted_root)


# Import only one function:
from math import sqrt

print(sqrt(16))


# Give a module a shorter alias:
import math as m

print(m.sqrt(16))


# ==========================
# BUILT-IN FUNCTIONS
# No import is required
# ==========================

"""
print()  → display output
input()  → receive user input
type()   → show a value's type
len()    → count items
range()  → produce a sequence for loops
int()    → convert to integer
float()  → convert to float
str()    → convert to string
bool()   → convert to Boolean
max()    → find the largest value
min()    → find the smallest value
sum()    → add numeric values
"""


# ==========================
# DEFAULT PARAMETER VALUES
# Used when no argument is supplied
# ==========================

def greet_person(name="Jacques"):
    print("Hello", name)


greet_person()
greet_person("Isaac")


def add_with_defaults(number1=3, number2=4):
    result = number1 + number2
    print("Answer:", result)


add_with_defaults()
add_with_defaults(number1=100)


# ==========================
# KEYWORD ARGUMENTS
# Matched by name, so order does not matter
# ==========================

def display_names(first_name, surname, middle_name):
    print(first_name, surname, middle_name)


display_names(
    surname="Doe",
    first_name="John",
    middle_name="Botha",
)


# ==========================
# RECURSION
# A function calls itself
# A base case stops the recursion
# ==========================

def countdown(number):
    print(number)

    if number > 0:
        countdown(number - 1)


countdown(3)


# ==========================
# RECURSIVE FACTORIAL
# 5! = 5 × 4 × 3 × 2 × 1
# ==========================

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


print("5! =", factorial(5))


# ==========================
# ARBITRARY POSITIONAL ARGUMENTS
# *numbers collects arguments into a tuple
# ==========================

def find_sum(*numbers):
    result = 0

    for number in numbers:
        result += number

    print("Answer:", result)


find_sum(2, 3, 4)


# ==========================
# LAMBDA / ANONYMOUS FUNCTIONS
# Small one-expression functions
# ==========================

square = lambda number: number * number
print(square(5))


numbers = [5, 2, 8, 1]

# The lambda tells sort() which value to use as its sorting key.
numbers.sort(key=lambda number: number)

print(numbers)


# A lambda is usually unnecessary for a direct one-off calculation:

result = 5 * 2
print(result)

# This works, but is less useful here:
double = lambda number: number * 2
result = double(5)

print(result)