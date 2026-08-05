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



