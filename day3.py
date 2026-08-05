"""
Day 3: Scope, Collections, Strings, Sets, Files, and Exceptions

Topics covered:
- LEGB scope
- global and nonlocal
- Negative indexing and slicing
- List methods
- Tuples
- Strings and f-strings
- Sets
- File operations
- with open()
- File modes
- Basic exception handling
"""


# ==========================
# LEGB SCOPE
# Local → Enclosing → Global → Built-in
# ==========================

"""
Python searches for names in this order:

L = Local
E = Enclosing
G = Global
B = Built-in
"""


# ==========================
# NONLOCAL
# Changes a variable in an enclosing function
# ==========================

def outer():
    message = "local"

    def inner():
        nonlocal message
        message = "nonlocal"
        print("Inner:", message)

    inner()
    print("Outer:", message)


outer()


# ==========================
# GLOBAL
# Changes a variable outside all functions
# ==========================

count = 1


def increase_count():
    global count
    count += 2
    print("Inside function:", count)


increase_count()
print("Outside function:", count)


# ==========================
# GLOBAL VS LOCAL
# The same name can refer to different variables
# ==========================

number = 10


def outer_function():
    number = 20

    def inner_function():
        global number
        number = 25

    print("Before inner:", number)
    inner_function()
    print("After inner:", number)


outer_function()
print("Outside both:", number)


# ==========================
# IMPORT STYLES
# ==========================

from math import pi
import math as m

print("Pi:", pi)
print("Square root:", m.sqrt(25))


# ==========================
# NEGATIVE INDEXING
# ==========================

languages = ["Python", "Java", "C++"]

print(languages[-1])   # Last item
print(languages[-3])   # Third-last item


# ==========================
# LIST SLICING
# Start is included, stop is excluded
# ==========================

letters = ["p", "r", "o", "g", "r", "a", "m"]

print(letters[3:4])    # Index 3 only
print(letters[3:])     # Index 3 to the end
print(letters[:])      # Entire list
print(letters[-3:])    # Last three items


# ==========================
# ADDING ITEMS TO LISTS
# append(), extend(), and insert()
# ==========================

numbers = [1, 3, 5]

print("Before append:", numbers)

numbers.append(30)
print("After append:", numbers)

even_numbers = [4, 6, 8]

numbers.extend(even_numbers)
print("After extend:", numbers)

numbers.insert(1, 20)
print("After insert:", numbers)


# ==========================
# REMOVING ITEMS FROM LISTS
# del, remove(), and pop()
# ==========================

del numbers[7]
print("After deleting index 7:", numbers)

del numbers[-1]
print("After deleting last item:", numbers)

numbers.remove(3)
print("After removing value 3:", numbers)

removed_item = numbers.pop()
print("Popped item:", removed_item)
print("After pop:", numbers)


# ==========================
# COMMON LIST METHODS
# ==========================

"""
append()   Add one item
extend()   Add several items
insert()   Add at a position
remove()   Remove by value
pop()      Remove and return an item
clear()    Remove all items
index()    Find an item's position
count()    Count occurrences
sort()     Sort the list
reverse()  Reverse the list
copy()     Make a shallow copy
"""


# ==========================
# ITERATING THROUGH A LIST
# ==========================

languages = ["Python", "Swift", "C++"]

for language in languages:
    print(language)

print("C" in languages)
print("Python" in languages)


# ==========================
# BUILDING A LIST WITH A LOOP
# ==========================

squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)


# ==========================
# CREATING TUPLES
# Ordered, immutable, duplicates allowed
# ==========================

empty_tuple = ()
print(empty_tuple)

integer_tuple = (1, 2, 3, 4)
print(integer_tuple)

mixed_tuple = ("Python", 3.12, True, 100)
print(mixed_tuple)

nested_tuple = (1, 2, ("Apple", "Banana"), 4)
print(nested_tuple)


# ==========================
# ACCESSING NESTED TUPLES
# ==========================

print(nested_tuple[2])
print(nested_tuple[2][1])   # Banana

device_data = ("mouse", [8, 4, 6], (1, 2, 3))

print(device_data[1])
print(device_data[1][2])
print(device_data[2][2])


# ==========================
# ONE-ELEMENT TUPLES
# The comma creates the tuple
# ==========================

value1 = ("hello")
print(type(value1))         # str

value2 = ("hello",)
print(type(value2))         # tuple

value3 = "hello",
print(type(value3))         # tuple


# ==========================
# TUPLE METHODS
# ==========================

numbers_tuple = (1, 2, 2, 3)

print(numbers_tuple.count(2))
print(numbers_tuple.index(3))


# ==========================
# WHY USE TUPLES?
# ==========================

"""
- Tuples are immutable.
- They are useful for fixed data.
- They can protect values from accidental changes.
- They are often slightly faster than lists.
- Immutable tuple values can be used as dictionary keys.
"""


# ==========================
# STRINGS AND INDEXING
# Strings are immutable
# ==========================

greeting = "hello"

print(greeting[1:4])   # ell
print(greeting[1])     # e
print(greeting[-4])    # e

# This would raise TypeError:
# greeting[0] = "H"

greeting = "H" + greeting[1:]
print(greeting)


# ==========================
# MULTILINE STRINGS
# ==========================

message = """
Python is easy to read.
Python is powerful.
"""

print(message)


# ==========================
# STRING OPERATIONS
# ==========================

greeting = "Hello, "
name = "Jack"

result = greeting + name

print(result)
print(len(greeting))
print("a" in "program")
print("at" not in "battle")


# ==========================
# FORMATTED STRINGS
# f-strings place expressions inside {}
# ==========================

name = "Cathy"
country = "UK"

print(f"{name} is from {country}")


# ==========================
# SETS
# Unordered, unique values only
# ==========================

empty_set = set()
empty_dictionary = {}

print("Empty set type:", type(empty_set))
print("Empty dictionary type:", type(empty_dictionary))


integer_set = {1, 2, 3, 4}
print(integer_set)

language_set = {"Python", "Java", "C++"}
print(language_set)

mixed_set = {1, "Python", 3.14, True}
print(mixed_set)


# Duplicate values are removed automatically.

values = {1, 1, 2, 2, "Python", "Python"}
print(values)


# ==========================
# CHANGING SETS
# ==========================

permissions = {"read", "write"}

permissions.add("execute")
print(permissions)

permissions.discard("write")
print(permissions)


# ==========================
# SET OPERATIONS
# ==========================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))


# ==========================
# COMMON FUNCTIONS FOR COLLECTIONS
# ==========================

"""
all()
any()
enumerate()
len()
max()
min()
sorted()
sum()
"""


# ==========================
# FILE MODES
# ==========================

"""
r   Read. The file must already exist.
w   Write. Creates or overwrites the file.
a   Append. Creates the file if needed.
x   Create. Raises an error if the file exists.

r+  Read and write. The file must already exist.
w+  Write and read. Overwrites the file first.
a+  Append and read. Writes are added at the end.
"""


# ==========================
# WRITING TO A FILE
# with closes the file automatically
# ==========================

with open("test.txt", "w") as file:
    file.write("Hello Python\n")


# ==========================
# APPENDING TO A FILE
# ==========================

with open("test.txt", "a") as file:
    file.write("Another line\n")
    file.write("We love Python\n")


# ==========================
# READING A FILE
# ==========================

with open("test.txt", "r") as file:
    content = file.read()

print(content)


# ==========================
# READ AND WRITE WITH r+
# Writing starts at the current cursor position
# ==========================

with open("test.txt", "r+") as file:
    existing_content = file.read()
    file.write("New text\n")

print("Previous content:")
print(existing_content)


# ==========================
# FILE CURSOR WITH seek()
# Move back to the beginning before reading
# ==========================

with open("test.txt", "a+") as file:
    file.write("Appended with a+\n")
    file.seek(0)
    print(file.read())


# ==========================
# BASIC EXCEPTION HANDLING
# ==========================

try:
    with open("test.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")

else:
    print("The file was read successfully.")

finally:
    print("File operation finished.")
