"""
Day 1: Python Fundamentals

Topics covered:
- Numeric data types
- Variables
- Lists
- Tuples
- Sets
- Dictionaries
- Implicit and explicit type conversion
- print(), sep, and end
- User input
- Arithmetic operators
- Octal and hexadecimal numbers
- Logical operators
- Scope and namespaces
"""

# ==========================
# NUMERIC DATA TYPES
# ==========================

num1 = 5
print(num1, "is of type", type(num1))

num2 = 2.0
print(num2, "is of type", type(num2))

num3 = 1 + 2j
print(num3, "is of type", type(num3))


# ==========================
# VARIABLES AND BASIC MATH
# ==========================

num1 = 1
num2 = 2

print("Sum is:", num1 + num2)


# ==========================
# LISTS
# Ordered, changeable, duplicates allowed
# ==========================

languages = ["Swift", "Java", "Python", 123]

print(languages[2])
print(type(languages[3]))

# Lists are mutable:
# languages[2] = "Crazy"
# print(languages[2])

# languages[2] = 123
# print(languages[2])


# ==========================
# TUPLES
# Ordered, fixed, duplicates allowed
# ==========================

product = ("Xbox", 499.99)

print(type(product))
print(product[0])

# Tuples are immutable, so this causes an error:
# product[0] = "PlayStation"


# ==========================
# SETS
# Unordered, unique values only
# ==========================

student_ids = {112, 124, 112}

print(student_ids)

# Duplicate 112 is removed automatically.


# ==========================
# DICTIONARIES
# Key-value pairs, keys must be unique
# ==========================

capital_cities = {
    "Nepal": "Kathmandu",
    "Italy": "Rome",
    "England": "London",
}

print(capital_cities["Nepal"])

# Duplicate keys are not allowed.
# The final value assigned to a duplicate key replaces the earlier value.


# ==========================
# IMPLICIT TYPE CONVERSION
# Python converts automatically
# ==========================

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value:", new_number)
print("Data type:", type(new_number))


# ==========================
# EXPLICIT TYPE CONVERSION
# Also called type casting
# ==========================

num_string = "12"
num_integer = 23

print("Data type before casting:", type(num_string))

num_string = int(num_string)

print("Data type after casting:", type(num_string))

num_sum = num_integer + num_string

print("Sum:", num_sum)
print("Data type of sum:", type(num_sum))


# ==========================
# PRINT FUNCTION
# sep controls spacing between items
# end controls what appears after output
# ==========================

print("\\")

print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


# ==========================
# USER INPUT
# input() always returns a string
# ==========================

# num = input("Enter a number: ")
# print("You entered:", num)
# print("Data type before casting:", type(num))

# num = int(num)
# print("Data type after casting:", type(num))


# ==========================
# ARITHMETIC OPERATORS
# ==========================

print(10 / 3)     # Normal division
print(10 // 3)    # Floor division
print(7 % 2.5)    # Remainder
print(10 ** 3)    # Power


# ==========================
# OCTAL AND HEXADECIMAL
# ==========================

print(0o123)      # Octal
print(0x123)      # Hexadecimal


# ==========================
# LOGICAL OPERATORS
# and, or, not
# ==========================

a = 5
b = 6

print((a > 4) and (b >= 6))
print(not (a > 4))


# ==========================
# NAMESPACES AND SCOPE
# ==========================

x = 10  # Global variable


def test():
    y = 20  # Local variable

    print("Global x:", x)
    print("Local y:", y)


test()