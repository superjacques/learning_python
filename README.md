# 🐍 Python Learning Journey (PCEP → PCAP)

## 📈 Overall Progress
Progress: 59%
████████████░░░░░░░░ 59%

Primary goals:
⬜ Pass PCEP
⬜ Pass PCAP
⬜ Build a practical Python portfolio
⬜ Be ready for Python development opportunities

## ✅ Learning Plan

### 🟩 Setup and Fundamentals
✅ Python available on Linux
✅ Thonny installed and opened
✅ PyCharm installed and opened
✅ VS Code installed and opened
✅ Run and save Python programs
✅ Comments
✅ Keywords and identifiers
✅ Variables
✅ Basic data types

### 🔵 Strings
✅ Creating strings
✅ Indexing and negative indexing
✅ Slicing
✅ String methods
✅ Formatting with f-strings

### 🟡 Containers
✅ Lists
✅ Tuples
✅ Sets
✅ Dictionaries

### 🟠 Operators and Conversion
✅ Arithmetic operators
✅ Assignment operators
✅ Comparison operators
✅ Logical operators
✅ Bitwise and special operators
✅ Implicit type conversion
✅ Explicit type casting

### 🟣 Flow Control
✅ if
✅ if / else
✅ if / elif / else
✅ Nested conditions

### 🔁 Loops
✅ for
✅ range()
✅ while
✅ break
✅ continue
✅ pass
✅ Loop else blocks

### ⚙️ Functions
✅ Creating and calling functions
✅ Parameters and positional arguments
✅ Return values
✅ Default parameters
✅ Keyword arguments
✅ *args
✅ Recursion
✅ Lambda functions

### 🌐 Scope and Namespaces
✅ Local scope
✅ Global scope
✅ Enclosing and nonlocal scope
✅ Built-in scope
✅ global and nonlocal keywords

### 📦 Modules and Packages
✅ import
✅ from ... import
✅ Module aliases
✅ Creating modules
✅ Packages

### 📄 Files and Directories
✅ Reading files
✅ Writing files
✅ with open()
✅ File modes
✅ Working with directories

### 🚨 Exceptions
✅ try
✅ except
✅ else
✅ finally
⬜ Common built-in exceptions
⬜ Custom exceptions

### 🏗️ Object-Oriented Programming
⬜ Classes
⬜ Objects
⬜ Attributes
⬜ Methods
⬜ Constructors and __init__
⬜ self
⬜ Inheritance
⬜ Method overriding
⬜ super()
⬜ Encapsulation
⬜ Polymorphism

### 🚀 Advanced Course Topics
⬜ Multiple inheritance
⬜ Multilevel inheritance
⬜ Method Resolution Order
⬜ Operator overloading
⬜ Iterators
⬜ Custom iterators

### 💻 Practical Projects
⬜ Calculator
⬜ File organiser
⬜ CSV reader
⬜ API client
⬜ AI API script
⬜ Property cashflow calculator
⬜ Linux automation script
⬜ GitHub portfolio

### 🏆 Certifications
⬜ PCEP exam
⬜ PCAP course
⬜ PCAP exam

## 🌟 Career Additions — Not Part of This Course
These are deliberate additions for practical development ability and employability. They are not listed as part of the supplied training presentation.

⬜ Git basics
⬜ Virtual environments (venv)
⬜ pip and dependency installation
⬜ requests for APIs
⬜ pathlib for files and paths
⬜ JSON handling
⬜ argparse for command-line tools
⬜ pytest for testing
⬜ Build five polished portfolio projects

---

# Python Learning Hub

## Purpose
This document is the working hub for the PCEP and later PCAP training. It condenses the supplied Python for Beginners presentation into practical study notes without copying the full slide deck or its animations.

## Course Source
Presentation: Python for Beginners, presented by Isaac.
Primary environment: Thonny IDE. Python scripts use the .py extension. Other IDEs such as IDLE, PyCharm and VS Code can also run Python.

## Core Language Foundations
Python is cross-platform, free and open-source. The language is case-sensitive and uses indentation to define code blocks.

### Keywords and identifiers
Keywords are reserved words with a special meaning and cannot be used as variable, function or class names. Identifiers are names given to variables, functions, classes and methods.

Identifier rules:
- Start with a letter or underscore.
- May contain letters, digits and underscores.
- Cannot start with a digit.
- Cannot contain spaces or special symbols.
- Cannot be a Python keyword.
- Names are case-sensitive.

### Comments
A hash symbol starts a single-line comment. Triple-quoted text can span multiple lines, although it is also used for strings and docstrings.

## Data Types
### Numbers
- int: whole numbers
- float: decimal numbers
- complex: numbers with real and imaginary parts
- type() reports the class of a value

Python also supports binary, octal and hexadecimal notation.

### Core containers
- list: ordered, indexed, mutable, duplicates allowed
- tuple: ordered, indexed, immutable
- set: unordered collection of unique values
- dictionary: ordered key-value pairs with unique immutable keys

### Strings
Strings are immutable sequences of characters enclosed in single or double quotes. They support indexing, negative indexing, slicing, concatenation, iteration, membership tests and methods such as upper(), lower(), replace(), split() and startswith(). f-strings embed values inside text.

## Type Conversion
Implicit conversion happens automatically where Python can safely promote a value, such as int to float. Explicit conversion uses functions such as int(), float(), str() and complex(). Explicit conversion may discard information, for example converting a float to an integer.

## Input and Output
- print() displays output.
- input() reads user input and returns a string.
- Convert input explicitly when a number is required.

## Operators
- Arithmetic: +, -, *, /, //, %, **
- Assignment: = and compound forms such as +=
- Comparison: ==, !=, <, <=, >, >=
- Logical: and, or, not
- Bitwise operators
- Special operators such as membership and identity operators

## Namespace and Scope
A namespace maps names to objects. Python commonly uses built-in, global, enclosing and local scopes. A name referenced inside a function is searched from the closest local scope outward. Variables declared outside functions are global. Variables created inside functions are local unless global or nonlocal is used.

## Flow Control
### Conditions
- if executes a block when a condition is true.
- if...else chooses between two alternatives.
- if...elif...else handles multiple alternatives.
- Nested if statements place one condition inside another.

### Loops
- for iterates through a sequence or range.
- while repeats while a condition remains true.
- break exits a loop immediately.
- continue skips to the next iteration.
- pass is a valid placeholder that performs no operation.
- Loop else blocks run when a loop finishes normally, but not after break.

## Functions
A function is a reusable block of code declared with def. It may accept parameters and return a value.

Function concepts:
- positional arguments
- keyword arguments
- default parameter values
- arbitrary positional arguments using *args
- return ends a function and sends a value back
- recursion is when a function calls itself and requires a base condition
- lambda creates a small anonymous function containing one expression

## Modules and Packages
A module is a Python file containing code that can be imported. Use import module and access members with dot notation. Use from module import name to import specific definitions. Aliases can shorten names. Importing everything with * is discouraged because it can create naming collisions.

A package groups related modules in directories. The presentation describes __init__.py as the marker used for a package.

## File and Directory Handling
File workflow:
1. Open the file.
2. Read or write.
3. Close it.

Prefer with open(...) because it closes the file automatically, including when an exception occurs. Common modes include r for reading and w for writing. Opening an existing file with w erases its current contents.

The os module provides directory functions such as getcwd() and chdir().

## Exceptions
Exceptions are runtime problems represented by exception objects.

Use:
- try for code that may fail
- except to handle a specific exception
- else for code that runs when try succeeds
- finally for cleanup that must always run

Examples include ZeroDivisionError, FileNotFoundError, ImportError and IndexError. Custom exceptions can inherit from Exception.

## Object-Oriented Programming
A class is a blueprint; an object is an instance of that class.

Key concepts:
- attributes store object data
- methods are functions defined inside classes
- __init__ initializes new objects
- self refers to the current instance
- inheritance creates a child class from a parent class
- method overriding replaces inherited behavior
- super() accesses parent-class behavior
- encapsulation groups data and methods and uses naming conventions such as _ and __
- polymorphism allows the same interface or method name to behave differently
- multiple and multilevel inheritance are supported
- Method Resolution Order decides which inherited method Python selects
- operator overloading uses special methods such as __add__ and __lt__

## Iterators
An iterator returns items one at a time. It implements __iter__() and __next__(). iter() creates an iterator and next() retrieves the next value. When exhausted, it raises StopIteration. A for loop handles this process automatically.

## Priority for PCEP Preparation
Master first:
1. variables and basic data types
2. strings and type conversion
3. lists and tuples
4. dictionaries and sets
5. input and output
6. operators
7. if, elif and else
8. for and while loops
9. functions, parameters and return values
10. basic exceptions, modules and scope

Treat detailed OOP, inheritance, operator overloading, custom iterators and advanced package structure as later or PCAP-oriented material unless the instructor includes them in the PCEP assessment.

## Working Method
For each class topic:
1. Add concise notes here.
2. Type every example manually in Thonny.
3. Recreate the same exercise in PyCharm to build IDE familiarity.
4. Save useful scripts in a structured Git repository.
5. Add mistakes, corrections and exam traps to this document.

## 🔗 Exam and Study Resources

Official references:
- GeeksforGeeks: https://www.geeksforgeeks.org/
- Python Institute: https://pythoninstitute.org/

Practice resources:
- Simulations: https://codepen.io/collection/ExkyKG
- Mock Exam: https://docs.google.com/forms/d/e/1FAIpQLSdhv6phnlHopuLGqpoJdkFoLR_lrgOsINWyIjz2UD4b7LsLFQ/viewform

Mock exam notes:
- Keep this as a study resource only.




# 📝 PCEP Mock Exam

Source: Training mock exam supplied during the NIL PCEP course.

Important: This section contains study questions only. Do not add usernames, passwords, access codes, or private account details before publishing the document to GitHub.

Quiz Questions
A set of rules which defines the ways in which words can be coupled in sentences is called:
*
1 point
C. semantics
B. syntax
A. lexis
A process in which the source code is translated into machine code in order to be executed later is called:
*
1 point
C. compilation
B. interpretation
A. linking
D. edition
A process in which the source code is immediately executed without the need to translate it into machine code is called:
*
1 point
C. compilation
B. interpretation
D. edition
A. linking
Which of the following expressions evaluate to a non-zero result? (Select two answers.)

*
1 point
B. 4 / 2 ** 3 - 2
A. 2 ** 3 / 4  - 2
D. 1 * 4  // 2 ** 3
C. 2 ** 3 / 4 - 1
Python is an example of which programming language category? 
*
1 point
D. machine
C. compiled
B. assembly
A. interpreted
How many hashes (#) does the code output to the screen?

floor = 10

while floor != 0:
    floor //= 4
    print("#", end="")

else:
    print("#")
*
1 point
D. three
B. zero ( the code outputs nothing )
C. five
A. one
How many hashes (#) does the code output to the screen?

floor = 1

while floor <= 10:
    floor += floor
    print("#", end = "")

else:
    print("#")
*
1 point
A. one
B. zero ( the code outputs nothing )
C. five
D. three
What happens when the user runs the following code?

total = 0

for i in range(4):
    if 2 * i < 4:
        total += 1
    else:
        total += 1

print(total)
*
1 point
C. The code enters an infinite loop.
B. The code outputs 4
D. The code outputs 1.
A. The code outputs 3.
What happens when the user runs the following code?

total = 0

for i in range(5):
  if i % 2 == 1:
    total += 1

else:
  total -= 1

print(total)
*
1 point
A. The code enters an infinite loop.
B. The code outputs 2.
C. The code outputs 3
D. The code outputs 1
What is expected output of the following code?

counter = 84 // 2

if counter < 0:
    print("*")

elif counter > 42:
    print("**")

else:
    print("***")
*
1 point
B. **
C. ***
D. *
A. The code produces no output.
What is expected output of the following code?

speed = 0

while speed < 30:
    speed *= 2
    if speed > 10:
        continue
    print("*", end="")

else:
    print("*")
*
1 point
D. The program enters an infinite loop.
B. The program outputs one asterisk ( * ) to the screen.
A. The program outputs three asterisks ( *** ) to the screen.
C. The program outputs five asterisks ( ***** ) to the screen.
What is expected output of the following code?

equals = 0

for i in range(2):
    for j in range(2):
        if i == j:
            equals += 1
else:
    equals += 1

print(equals)
*
1 point
B. 3
A. The code outputs nothing.
D. 4
C. 1
What is expected output of the following code?

collection = []
collection.append(1)
collection.insert(0, 2)

duplicate = collection[:]

duplicate.append(3)
print(len(collection) + len(duplicate))
*
1 point
A. 5
B. 4
D. The code raises an exception and outputs nothing.
C. 6
What is expected output of the following code?

collection = []
collection.insert(0, 2)
collection.append(3)

duplicate = collection

duplicate.append(2)

print(collection[-1] + duplicate[-1])
*
1 point
A. 5
D. The code raises an exception and outputs nothing.
B. 4
C. 6
What is expected output of the following code?

collection = []

collection.append(0,1)  
collection.insert(0, 2) 

duplicate = collection[:]  

duplicate.append(3)  

print(collection[-1] + duplicate[-1])  
*
1 point
C. 5
A. 6
B. 4
D. The code raises an exception and outputs nothing.
What is expected output of the following code?

collection = []

collection.insert(0, 1) 
collection.append(2)  

duplicate = collection[:]  

duplicate.append(3)  

print(collection[-1] + duplicate[-1])  
*
1 point
C. 5
A. 6
B. 4
D. The code raises an exception and outputs nothing.
Assuming that the following assignment has been successfully executed: 

my_list = [ 1 , 1 , 2, 3 ]

Select the expressions which will not raise any exception.

(Select two expressions.)

*
1 point
C. my list [6]
A. my_list[-10]
B. my_list[my_list[3]]
D. my_list[0:1]
Assuming that the following assignment has been successfully executed: 

my_list = [ 1 , 2 , 4, 8 ]

Select the expressions which will not raise any exception.

(Select two expressions.)

*
1 point
D. my_list [-2]
B. my_list[-3:-2]
A. my_list[my_list[3]]
C: my_list [4]
What is true about tuples ? ( Select two answers.)
*
1 point
D. Tuples can be indexed and sliced like lists.
B. The len { } function cannot be applied to tuples.
C. An empty tuple is written as { }.
A. Tuples are immutable, which means that their contents cannot be changed during their lifetime.
What is true about tuples ? ( Select two answers.)
*
1 point
B. Tuples can be concatenated using the + operator
D. If tup is a non-zero length tuple, del tup[0] is used
C. Each element of a tuple must be unique
A. An empty tuple can be written as tuple()
What is true about tuples ? ( Select two answers.)
*
1 point
C. Tuples can be subtracted using the - operator
B. The for loop can be used to iterate through a tuple
A. one-element tuple can be coded as (1,) or 1,
D. A tuple can be expanded using the .append() method
What is the expected output of the following code?


menu = ["syrniki":12.8, "shashlik":49.9, "borscht":23.2}

for value in menu.items():
   print(value[1], end="")
*
1 point
D. yh
A. 23.849.923.2
C. The code is erroneous and cannot be run
B. 293
What is the expected output of the following code?


menu = {"bunuelo":3.21, "torrijas":4.99, "churros":1.99}

for value in menu.values():
   print(str(value) [1], end="")
*
1 point
C. The code is erroneous and cannot be run
B. nru
D. 3.21.499.199
A. ...
Assuming that the following assignment has been successfully executed :

the_list = ["1",1,1.]

Which of the following expressions evaluate to True ? (Select two expressions.)
*
1 point
A. the_list.index("1") in the_list
B. 1.1 in the_list [1 : 3 ]
D. the_list.index('1') == 0
C. len(the_list [0:2]) <3
What is the expected output of the following code?

menu = {"pizza":2.39, "pasta":1.99, "folpetti":3.99}

for value in menu:
    print(str(value)[0], end="")
*
1 point
C. 213
A. The code is erroneous and cannot be run.
B. ppf
D. pizzapastafolpetti
What is the expected output of the following code?

menu = {"canistall": 1.12, "vol-au-vent": 2.99, "gougere": 0.99}

for value in menu.keys():
    print(str(value)[1], end="")
*
1 point
A. canistrellivol-au-ventgougere
C. ...
B. aoo
D. The code is erroneous and cannot be run
What is the expected result of the following code?

rates = (1.2, 1.4, 1.0)
new = rates[3:]

for rate in rates[-1:]:
    new += (rate,)

print(len(new))
*
1 point
A. 5
D. The code will cause an unhandled exception
B. 2
C. 1
What is the expected result of the following code?

rates = (1.2, 1.4, 1.0)
new = rates[:]

for rate in rates[-2:]:
    new += (rate,)

print(len(new))
*
1 point
C. 2
D. The code will cause an unhandled exception
B. 5
A. 1
What is the expected result of running the following code?

def do_the_mess(parameter):
    parameter[0] != variable
    return parameter[0]

the_list = [x for x in range(2, 3)]
variable = -1

do_the_mess(the_list)

print(the_list[0])

*
1 point
C. The code raises an unhandled exception.
D. The code prints 0.
B. The code prints 2.
A. The code prints 1.
What is the expected result of running the following code?

def do_the_mass(parameter):
    variable += parameter[0]
    return variable

the_list = [x for x in range(2, 3)]
variable = -1

do_the_mass(the_list)

print(variable)
*
1 point
B.  The code raises an unhandled exception.
A. The code prints 0
C. The code prints 1
D. The code prints 2
What is the expected output of the following code?

def runner(brand, model="", year=2021, convertible=False):
    return (brand, str(year), str(convertible))

print(runner("Fermi")[2][2])
*
1 point
A. l
C. False
D. ('Fermi, '2021' , 'False')
B. The code raises an unhandled exception.
What is the expected output of the following code?

def runner(brand, model="", year=2021, convertible=True):
    return (brand + model + str(convertible))

print(runner(model ="Reluctance", 2019 [1]))
*
1 point
D. ()
B. The code raises an unhandled exception.
C. True
A. Reluctance
What is the expected output of the following code?

def runner(brand, model="", year=2021, convertible=False):
    return brand + model + str(convertible)

print(runner("Volta", "Tension", 2019)[-1])
*
1 point
D. The code raises an unhandled exception
B. e
A. Volta Tension
C. True
What is the expected output of the following code?

def runner(brand, model="", year=2021, convertible=False):
    return (brand, str(year), str(convertible))

print(runner(model="Furious", brand="Ampere") [1][1])
*
1 point
A. 2021
B. ('Ampere', '2021','False')
D. 0
C. The code raises an unhandled exception
What is true about exceptions and debugging? (Select two answers.)
*
1 point
A. A tool that allows you to precisely trace program execution is called debugger.
B. If some Python code is executed without errors, this proves that there are no errors in it.
D. The default (anonymous) except branch cannot be the last branch in the try-except block.
C. One try-except block may contain more than one except branch.
Which of the following are the names of Python passing argument styles?
(Select two answers.) 
*
1 point
C. indicatory
D. positional
B. reference
A. keyword
What is the expected result of the following code?

def velocity(x):
    return speed + x

speed = 10

new_speed = velocity(10)
new_speed = velocity(new_speed)

print(new_speed)
*
1 point
D. 30
C. 10
A. The code is erroneous and cannot be run.
B. 20
What is the expected result of the following code?

def velocity(x):
    return speed + x

speed = 10

new_speed = velocity()
new_speed = velocity(new_speed)

print(new_speed)
*
1 point
A. The code is erroneous and cannot be run.
D. 30
C. 10
B. 20
What is the expected result of the following code?

def velocity(x=10):
    return speed + x

speed = 10

new_speed = velocity()
new_speed = velocity(new_speed)

print(new_speed)
*
1 point
D. 30
B. 20
A. The code is erroneous and cannot be run.
C. 10
What is the expected output of the following code?

def traverse(stop):
    if stop == 0:
        return 0
    else:
        return stop * traverse(stop - 1)

print(traverse(2))
*
1 point
B. 0
C. 3
D. 1
A. 2
Which of the following functions can be invoked with two arguments ?
*
1 point

Option 1

Option 3

Option 2

Option 4
A program written in a high-level programming language is called:
*
1 point
a binary code
machine code
a source code
the ASCII
Given the below lines of code which one of the following two conditional statements  depth = 0 and depth == 0 being true so that it outputs ***
*
1 point

A.

C.

B.
What happens when the users runs the following code?

speed = 3

while speed < 8:
    speed += 2
    if speed == 7:
        continue
    print("*", end="")

else:
    print("*")
*
1 point
B. The program outputs three asterisks(***) to the screen
A. The program outputs one asterisk (*) to the screen
D. The program enters an infinite loop
C. The program outputs five asterisks (*****) to the screen
Assuming that the following assignment has been successfully executed:

the_list = ['list', False, 3e8]

Which one of the following prints True

*
1 point
B. the_list[1] in the_list
D. the_list.index(False) == 1
C. 300 in the_list and the_list[1]
A. int(the_list[2]) == len(the_list)
Which of the following sentences are true?

(Select three answers)

*
1 point
B. Function is oblidged to return a value
D. It's possible to define more than one function of the same program
C. Every function must be defined before it is invoked
A. A function can invoke itself
Python:

    speed = float('48;4')

    print('Ok')

except:

    print('Failed')

    speed = None


Given the above lines of code, which word should be used to replace  Python in order to print Failed to the screen

*
1 point
A. try
B. when
C. for
What is true about exceptions in Python? 

(Select two answers)

*
1 point
A. Python's philosophy encourages developers to make all the occurrences of an execution
B. According to Python terminology, exceptions are raised
C. Not more than one except branch can be executed in program
D. According to Python terminology, exceptions are thrown
What is the expected output of the following code?

def count(start):

    print(start, end=" ")

    if start > 0:

        count(start -1)


count(3)

*
1 point
A. 1 2 3
D. 3 2 1
B. 3 2 1 0
C. 0 1 2 3
Assume the following assignment has been successfully executed:



the_list = [True, 3.1474, -1]



Which of the following expression evaluate to True

(Select two)

*
1 point
D. the_list.index(-1) == 2
B. (len(the_list) == 3 in the_list)
C. len(sorted(the_list)) != len(the_list)
A. True in the_list
Assume the following assignment has been successfully executed:



my_list = [1, 2, 4, 8]



Select the expressions which will not raise any exception

(Select two)

*
1 point
B. my_list[my_list{3}]
C. my_list[-3:-2]
D. my_list[4]
A. my_list[-2]
Which of the following functions can be invoked with one argument ?

*
1 point
A. def eta(level,size, depth=0): pass
C. def zeta(): pass
B. def theta(None): pass
D. def epsilion (level = 100): pass
Which of the following are the names of Python passing argument styles? (Select two)

*
1 point
D. indicatory
A. reference
C. positional
B. keyword
What is the expected result of the following code?



def do_the_mess(parameter):

  global variable

  variable += parameter[0]

  return variable



the_list = [x for x in range(2, 3)]

variable = 0


do_the_mess(the_list)



print(variable)

*
1 point
B. The code raises an unhandled exception
A. The code prints 1
D. The code prints 0
C. The code prints 2
What is true about exceptions and debugging? (Select two answers)

*
1 point
A. The default (anonymouse) except branch cannot be the last branch in the try-except block
B. A tool that allows you to precisely trace program execution is called a debugger
C. If some Python code is executed without errors, this proves that there are no errors in it
D. One try-except block may contain more than one except branch
Operations that can be performed by CPU is called:

*
1 point
D. an instruction set
B. an assembly order
C. the ASCII code
A. a binary code
A set of elementary operations that can be performed by a CPU is called:

*
1 point
B. a binary code
D. an instruction set
A. an assembly order
C. the ASCII code
What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?

x = float(input())
y = float(input())
print(y ** (1 / x ))
*
1 point
D. 0.0
A. 4.0
Option 2
B. 1.0
C. 2.0
What is the expected results of running the following code?

def do_the_mass(parameter):

    global variable

    variable += parameters[0]

    return variable

the_list = [x for x in range(2,3)]

variable = 0

do_the_mass(the_list)

print(variable)

*
1 point
C. The code prints 2
B. The code raises an unhandled exception
A. The code prints 0
D. The code prints 1
What is the expected output of the following code?

menu = {"syrniki" : 12.8, "shashlik": 49.9, "borscht": 23.2}

for value in menu.items():

    print(value[1], end = "")

*
1 point
C. The code is erroneous and cannot be run
A. 12.849.923.2
D. yh
B. 293
What happens when the users  runs the following code?

speed = 3

while speed < 8:

    speed += 2

    if speed == 7:                                                 

        continue

    print("*", end = "")

else:

    print("*")

*
1 point
A. The program enters an infinite loop
D. The program outputs one asterisks ( * ) to the screen
B. The program outputs three asterisks ( *** ) to the screen
C. The program outputs five asterisks ( ***** ) to the screen
 How many hashes(#) does the code output to the screen?

floor = 0

while floor != 0:

    floor -= 1

    print("#", end = "")

else:

    print("#")

*
1 point
C. zero(the code outputs nothing)
D. Three
B. five
A. One
To run the code given as a source file whose name has the .py extension, you need to have:
*
1 point
C. a Python interpreter.
A. an MS windows computer.
D. a Python editor.
B. a Python compiler .
A binary code consists of:
*
1 point
B. a set of a certain alphabet symbols.
A. a sequence of ASCII characters.
D. a sequence of bits which encodes machine instructions.
C. a list of keywords.
What is the expected output of the following code ?

planets = 1 + 2 * 3 // 4

if planets < 0 :
     print ( " # " )

elif planets > 2:
       print( " # # ") 

else :
      print( " # # #")
*
1 point
B. # # #
D. The code prodcues no output
A. #
C. # #
What happens when the user runs the following code ?

angle =  -1
for i in range ( -1 , 1) :
       if 2 * i < 4 :
             angle += 1
else:
    angle += 2 
print (angle)
*
1 point
B. The code outputs 3.
A. The code enters an infinte loop.
C. The code outputs 2.
D. The code outputs 1.
What happens when the user runs the following code ?

power = 2
while power < 5 :
         power += 1
         if power == 3 :
              continue
         print ( "0" , end=" ")
else:
      print ("0")
*
1 point
D. The program outputs one at sign ( 0 ) to the screen.
C. The program enters an infinite loop.
A. The program outputs two at signs ( 0 0 ) to the screen.
B. The program outputs three at signs ( 0 0 0) to the screen.
What is the expected output of the following code?

others = 1
for i in range (2, 4) :
      for j in range (-1, 2) : 
            if  i == j:
                  others += 1 
            else:
               break 
print (others)
*
1 point
D. The code outputs nothing.
C. 1
A. 3
B. 4
What is the expected output of the following code?

list_one = [1, 2] 
list_two = list_one[:] 
list_two.append(3) 
print(list_one[-1] + list_two[-1])
*
1 point
B. 4
A. 6
C. 5
D. The code raises an exception and outputs nothing.
What is the expected output of the following code?

points = 0 

for answer in selection[1:]: 
   if answer: points += 1 

print(points)
*
1 point
B. 3
C. Raises an unhandled exception
D. 1
A. 0
Assuming that the following assignment has been successfully executed:

the_data = [ True , 3.1415, -2 ] 

Which of the following expressions to evaluate False?
(Select two expressions.)
*
1 point
D. the_data.index (-2) not in [the_data]
B. len (the_data[0:2]) == 0
C. -2 in the_data [2:4]
A. the_data.index(the_data [ -1]) == 0
Assuming that the following assignment has been successfully executed:

numbers = [ 1, 0.5, 0.25, 0.125] 

Select the expressions which will not raise any exception.
(Select two expressions.)
*
1 point
D. numbers[ numbers [1] ]
B. numbers[ -10 ]
C. numbers [0]
A. numbers[ 0 : 4 ]
What is the expected result of the following code?

def sample (value) :
       return total - value 

total = 4

total = sample(2)
total = sample(1)

print (total)
*
1 point
A. 4
C. The code is erroneous and cannot be run.
D. 1
B. 2
What is the expected result of the following code?

def process (data) :
      data = 2
      return data

measurements = [0 for i in range(3) ]
result = process(measurements)
print (result[-2])

*
1 point
B. The code prints 2.
A. The code prints 0.
D. The code raises an unhandled exception.
C. The code prints 1.
What is the expected output of the following code?

def walk(top) :
       if top == 0 :
            return 0 
       else:
            return top * walk(top - 1)

print(walk(2))
*
1 point
D. 2
C. 1
B. 0
A. 3
Which of the following functions can be invoked with three arguments?

*
1 point
C. def three(x, y, z):
B. def two(y, z):
D. def four(x, y, z, v):
A. def one(x, y, z, v=0):
Which of the following functions can be invoked with two arguments?

*
1 point
C. def mu(None): pass
A. def kappa(level): pass
D. def iota(level, size=10): pass
B. def lambda(): pass
What is the expected output of the following code?

def combine (width, height=10, depth=0, is_3D=False) :
   if is _3D:
        return [ is_3D, width, height, depth]

print(combine (2) [0] )

*
1 point
B. The code raises an unhandled exception.
C. 2
A. 1
D. 0
Assuming the following runs successfully, which of the options would run without raising an exception ?

my_list = [5,4,3,2]

*
1 point
C. my_list[1:1]
A. my_list[my_list[-1]]
B. my_list[4]
D. my_list[-5]
What is the expected output of the following code?

counter = 11 * 4 - 2
if counter > 0 :
     print ("*")
elif counter >  42 :
        print ("**") 
else:
        print ("***")
   
    
*
1 point
A. **
B. The code produces no output
D. *
C. ***
What is the expected result of running the following code?

def do_the_mess(parameter) :
      parameter = [  variable ] 
      return parameter

the_list =  [ x for x in range(0, 1) ]

variable = -2

do_the_mess(the_list)

print(the_list[0])

*
1 point
C. The code prints 2.
B. The code prints 0.
A. The code raises an unhandled eception.
D. The code prints 1.
Which of the following expressions evaluate to a zero result?
(Select two answers.)
*
1 point
D. 4  / 2 + 2 ** 1
A. 1 // 3 * 3  **  0
B. 1 ** 2 -4 // 3
C. 4 -3 // 2 + 1
Which of the following expressions evaluate to a zero result?
(Select two answers.)
*
1 point
A. 2 // 4
B. -1 / 3 * 3 + 1
D. 1 + 2 / 4 * 3
C. 4 / 1 * 2 - 1
Which of the following expressions evaluate to a zero result?
(Select two answers.)
*
1 point
A. -3 / 2 * 4 + 1
D. 2 // 2 * 2 + 3
C. 3 ** 2 // 3 / 3 -1
B. 2 / -3 * 6 + 4
Which of the following expressions evaluate to a zero result?
(Select two answers.)
*
1 point
B. 2 // 4 * 1 / 3
A. -1 / 3 * 3 + 1
D. 1 + 2 / 4 * 3
C. 4 / 1 * 2  - 1
How many asterisks (*) does the code output to the screen?

torque = 0 
while torque != 0:
         torque //= 2 
         print ("*", end=" ")
else:
     print("*")

*
1 point
A. one
D. three
B. two
C. zero(the code outputs nothing)
What is the expected output of the following code?

train_speed = {"FlyingScotsman":201, "TGV":320, "Shinkansen":320}

for train in train_speed.items():
  print(train[0], end="")

*
1 point
C. 233
B. FTS
D. The code is erroneous and cannot be run
A. FlyingScotsmanTGVShinkansen
What is the expected output of the following code?

answers = (False, True, True)
selection = answers[:]
points = 0

for answer in selection[1:]:
    if answer:
       points += 1

print(points)
*
1 point
C. 0
A. 1
D. 2
B. 3
What is true about exceptions in Python? Select 2
*
1 point
A. An unhandled exception causes the program to terminate
C. The code put inside the try branch may not be fully executed
B. If any of the raised exceptions remains unhandled, an error message is printed, and program execution continues
D. IndexError may be raised when you try to access a nonexistent dictionery element
What of the following sentences are true? Select two answers
*
1 point
C. It's technically possible to name a variable using an already existing function name, but it will shadow that function
B. A function cannot invoke itself
D. When a function body contains no return expression statement, the function returns None implicitly
A. A function declaration may be located anywhere inside the source code
What of the following functions can be invoked with three arguments?
*
1 point
B. def one(x,y,z,v=0): pass
A. def three(x, y=0): pass
D. def two(speed,altitude): pass
C. def four():
What would the following evaluate to ?

shift = 5 - 4 * 2

if shift > 0:
   print("#")

elif shift == 0:
   print("##")

elif shift < 0:
   print("###")
*
1 point
C. ##
A. #
B. The code is errenous and will not run
D. ###
Which of the following code snippets correctly define a function which returns its only argument doubled ?
*
1 point
A. def times_again(ar): return * ar
B. def double(value): return value * value
C. def multiply_by_2: value*= 2
D. def times_2(x): return x + x
What is the output of this code?

def iterate(end, foo = 0):
    if end > 0:
        foo = iterate (end -1, foo + end)
    return foo
   
print(iterate(2))
*
1 point
A. 1
D. 0
C. 3
B. 2
What happens when the user runs the following code ?

total = 0

for i in range(4):
    if 2 * i < 4:
        total += 1
else:
      total += 1

print(total)
*
1 point
C. The code outputs 2
A. The code enters an infinite loop
D. The code outputs 3
B. The code outputs 1
What is the expected output of the following code?

counter = 7 ** 2 - 7

if counter < 0:
  print("*")
elif counter > 42:
  print("**")
else:
  print("***")
*
1 point
A. The code produces no output
B. ***
C. **
D. *
Which of the following functions can be invoked without arguments?

*
1 point
C. def beta(None): pass
D. def gamma(level): pass
A. def delta(level, size = 0): pass
B. def alpha(level=1000): pass
What is expected output of the following code?

equals = 0

for i in range(2):
  for j in range(2):
     if i == j:
        equals += 1
     else:
         break

print(equals)
*
1 point
A. 1
D. 3
C. 4
B. The code outputs nothing
What is expected output of the following code?

equals = 0

for i in range(2):
  for j in range(2):
     if i == j:
        equals += 1
else:
    equals += 1

print(equals)
*
1 point
B. The code outputs nothing
A. 1
C. 4
D. 3
What is expected output of the following code?

total = 0

for i in range(4):
   if 2 * i > 4:
        total += 1

else:
     total += 1

print(total)
*
1 point
B. 1
D. 3
C. 2
A. Infinite loop

What is expected output of the following code?

speed = 3

while speed < 0:
    speed **= 2
    if speed == 7:
        break
    print("*", end="")

else:
    print("*")
*
1 point
D. ****
C. Infinite loop
A. *
B. **


