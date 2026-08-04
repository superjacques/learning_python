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