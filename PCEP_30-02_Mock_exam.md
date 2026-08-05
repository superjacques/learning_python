# PCEP 30-02 Mock Exam

> **Original form:** https://docs.google.com/forms/d/e/1FAIpQLSdhv6phnlHopuLGqpoJdkFoLR_lrgOsINWyIjz2UD4b7LsLFQ/viewform
>
> Personal details, account information, required-field markers, Google Forms footer text, and credentials have been removed.

## About the exam

PCEP 30-02
PCEP™ – Certified Entry-Level Python Programmer certification (Exam PCEP-30-0x) is a professional credential that measures the candidate's ability to accomplish coding tasks related to the essentials of programming in the Python language. A test candidate should demonstrate sufficient knowledge of the universal concepts of computer programming, the syntax and semantics of the Python language, as well as the skills in resolving typical implementation challenges with the help of the Python Standard Library.

The PCEP™ certification shows that the individual is familiar with the following concepts: fundamental terms and definitions (e.g. compilation vs. interpretation), Python's logic and structure (e.g. keywords, instructions, indentation), literals, variables, and numeral systems, operators and data types, I/O operations, control flow mechanisms (conditional blocks and loops), data collections (lists, tuples, dictionaries, strings), functions (decomposition, built-in and user-defined functions, organizing interaction between functions and their environment, generators, recursion), exceptions (exception handling, hierarchies), as well as the essentials of Python programming language syntax, semantics, and the runtime environment.

---

## Quiz Questions

### Question 1

A set of rules which defines the ways in which words can be coupled in sentences is called:

**1 point**

- [ ] C. semantics
- [ ] A. lexis
- [ ] B. syntax

---

### Question 2

A process in which the source code is translated into machine code in order to be executed later is called:

**1 point**

- [ ] A. linking
- [ ] C. compilation
- [ ] D. edition
- [ ] B. interpretation

---

### Question 3

A process in which the source code is immediately executed without the need to translate it into machine code is called:

**1 point**

- [ ] A. linking
- [ ] D. edition
- [ ] B. interpretation
- [ ] C. compilation

---

### Question 4

Which of the following expressions evaluate to a non-zero result? (Select two answers.)

**1 point**

- [ ] B. 4 / 2 ** 3 - 2
- [ ] D. 1 * 4  // 2 ** 3
- [ ] A. 2 ** 3 / 4  - 2
- [ ] C. 2 ** 3 / 4 - 1

---

### Question 5

Python is an example of which programming language category?

**1 point**

- [ ] D. machine
- [ ] C. compiled
- [ ] A. interpreted
- [ ] B. assembly

---

### Question 6

How many hashes (#) does the code output to the screen?

```python
floor = 10

while floor != 0:
    floor //= 4
    print("#", end="")

else:
    print("#")
```

**1 point**

- [ ] D. three
- [ ] B. zero ( the code outputs nothing )
- [ ] A. one
- [ ] C. five

---

### Question 7

How many hashes (#) does the code output to the screen?

```python
floor = 1

while floor <= 10:
    floor += floor
    print("#", end = "")

else:
    print("#")
```

**1 point**

- [ ] A. one
- [ ] D. three
- [ ] B. zero ( the code outputs nothing )
- [ ] C. five

---

### Question 8

What happens when the user runs the following code?

```python
total = 0

for i in range(4):
    if 2 * i < 4:
        total += 1
    else:
        total += 1

print(total)
```

**1 point**

- [ ] D. The code outputs 1.
- [ ] A. The code outputs 3.
- [ ] B. The code outputs 4
- [ ] C. The code enters an infinite loop.

---

### Question 9

What happens when the user runs the following code?

```python
total = 0

for i in range(5):
  if i % 2 == 1:
    total += 1

else:
  total -= 1

print(total)
```

**1 point**

- [ ] C. The code outputs 3
- [ ] B. The code outputs 2.
- [ ] D. The code outputs 1
- [ ] A. The code enters an infinite loop.

---

### Question 10

What is expected output of the following code?

```python
counter = 84 // 2

if counter < 0:
    print("*")

elif counter > 42:
    print("**")

else:
    print("***")
```

**1 point**

- [ ] D. *
- [ ] C. ***
- [ ] A. The code produces no output.
- [ ] B. **

---

### Question 11

What is expected output of the following code?

```python
speed = 0

while speed < 30:
    speed *= 2
    if speed > 10:
        continue
    print("*", end="")

else:
    print("*")
```

**1 point**

- [ ] B. The program outputs one asterisk ( * ) to the screen.
- [ ] A. The program outputs three asterisks ( *** ) to the screen.
- [ ] C. The program outputs five asterisks ( ***** ) to the screen.
- [ ] D. The program enters an infinite loop.

---

### Question 12

What is expected output of the following code?

```python
equals = 0

for i in range(2):
    for j in range(2):
        if i == j:
            equals += 1
else:
    equals += 1

print(equals)
```

**1 point**

- [ ] D. 4
- [ ] A. The code outputs nothing.
- [ ] B. 3
- [ ] C. 1

---

### Question 13

What is expected output of the following code?

```python
collection = []
collection.append(1)
collection.insert(0, 2)

duplicate = collection[:]

duplicate.append(3)
print(len(collection) + len(duplicate))
```

**1 point**

- [ ] D. The code raises an exception and outputs nothing.
- [ ] A. 5
- [ ] C. 6
- [ ] B. 4

---

### Question 14

What is expected output of the following code?

```python
collection = []
collection.insert(0, 2)
collection.append(3)

duplicate = collection

duplicate.append(2)

print(collection[-1] + duplicate[-1])
```

**1 point**

- [ ] D. The code raises an exception and outputs nothing.
- [ ] A. 5
- [ ] C. 6
- [ ] B. 4

---

### Question 15

What is expected output of the following code?

```python
collection = []

collection.append(0,1)
collection.insert(0, 2)

duplicate = collection[:]

duplicate.append(3)

print(collection[-1] + duplicate[-1])
```

**1 point**

- [ ] C. 5
- [ ] A. 6
- [ ] D. The code raises an exception and outputs nothing.
- [ ] B. 4

---

### Question 16

What is expected output of the following code?

```python
collection = []

collection.insert(0, 1)
collection.append(2)

duplicate = collection[:]

duplicate.append(3)

print(collection[-1] + duplicate[-1])
```

**1 point**

- [ ] C. 5
- [ ] B. 4
- [ ] A. 6
- [ ] D. The code raises an exception and outputs nothing.

---

### Question 17

Assuming that the following assignment has been successfully executed:

```python
my_list = [ 1 , 1 , 2, 3 ]
```

Select the expressions which will not raise any exception.

(Select two expressions.)

**1 point**

- [ ] D. my_list[0:1]
- [ ] C. my list [6]
- [ ] A. my_list[-10]
- [ ] B. my_list[my_list[3]]

---

### Question 18

Assuming that the following assignment has been successfully executed:

```python
my_list = [ 1 , 2 , 4, 8 ]
```

Select the expressions which will not raise any exception.

(Select two expressions.)

**1 point**

- [ ] B. my_list[-3:-2]
- [ ] A. my_list[my_list[3]]
- [ ] D. my_list [-2]
- [ ] C: my_list [4]

---

### Question 19

What is true about tuples ? ( Select two answers.)

**1 point**

- [ ] B. The len { } function cannot be applied to tuples.
- [ ] C. An empty tuple is written as { }.
- [ ] A. Tuples are immutable, which means that their contents cannot be changed during their lifetime.
- [ ] D. Tuples can be indexed and sliced like lists.

---

### Question 20

What is true about tuples ? ( Select two answers.)

**1 point**

- [ ] C. Each element of a tuple must be unique
- [ ] D. If tup is a non-zero length tuple, del tup[0] is used
- [ ] B. Tuples can be concatenated using the + operator
- [ ] A. An empty tuple can be written as tuple()

---

### Question 21

What is true about tuples ? ( Select two answers.)

**1 point**

- [ ] D. A tuple can be expanded using the .append() method
- [ ] A. one-element tuple can be coded as (1,) or 1,
- [ ] C. Tuples can be subtracted using the - operator
- [ ] B. The for loop can be used to iterate through a tuple

---

### Question 22

What is the expected output of the following code?

```python
menu = ["syrniki":12.8, "shashlik":49.9, "borscht":23.2}

for value in menu.items():
   print(value[1], end="")
```

**1 point**

- [ ] C. The code is erroneous and cannot be run
- [ ] A. 23.849.923.2
- [ ] D. yh
- [ ] B. 293

---

### Question 23

What is the expected output of the following code?

```python
menu = {"bunuelo":3.21, "torrijas":4.99, "churros":1.99}

for value in menu.values():
   print(str(value) [1], end="")
```

**1 point**

- [ ] B. nru
- [ ] D. 3.21.499.199
- [ ] A. ...
- [ ] C. The code is erroneous and cannot be run

---

### Question 24

Assuming that the following assignment has been successfully executed :

```python
the_list = ["1",1,1.]
```

Which of the following expressions evaluate to True ? (Select two expressions.)

**1 point**

- [ ] D. the_list.index('1') == 0
- [ ] C. len(the_list [0:2]) <3
- [ ] A. the_list.index("1") in the_list
- [ ] B. 1.1 in the_list [1 : 3 ]

---

### Question 25

What is the expected output of the following code?

```python
menu = {"pizza":2.39, "pasta":1.99, "folpetti":3.99}

for value in menu:
    print(str(value)[0], end="")
```

**1 point**

- [ ] A. The code is erroneous and cannot be run.
- [ ] D. pizzapastafolpetti
- [ ] B. ppf
- [ ] C. 213

---

### Question 26

What is the expected output of the following code?

```python
menu = {"canistall": 1.12, "vol-au-vent": 2.99, "gougere": 0.99}

for value in menu.keys():
    print(str(value)[1], end="")
```

**1 point**

- [ ] D. The code is erroneous and cannot be run
- [ ] B. aoo
- [ ] C. ...
- [ ] A. canistrellivol-au-ventgougere

---

### Question 27

What is the expected result of the following code?

```python
rates = (1.2, 1.4, 1.0)
new = rates[3:]

for rate in rates[-1:]:
    new += (rate,)

print(len(new))
```

**1 point**

- [ ] B. 2
- [ ] A. 5
- [ ] C. 1
- [ ] D. The code will cause an unhandled exception

---

### Question 28

What is the expected result of the following code?

```python
rates = (1.2, 1.4, 1.0)
new = rates[:]

for rate in rates[-2:]:
    new += (rate,)

print(len(new))
```

**1 point**

- [ ] A. 1
- [ ] C. 2
- [ ] D. The code will cause an unhandled exception
- [ ] B. 5

---

### Question 29

What is the expected result of running the following code?

```python
def do_the_mess(parameter):
```

parameter[0] != variable

```python
    return parameter[0]

the_list = [x for x in range(2, 3)]
variable = -1
```

do_the_mess(the_list)

```python
print(the_list[0])
```

**1 point**

- [ ] A. The code prints 1.
- [ ] D. The code prints 0.
- [ ] B. The code prints 2.
- [ ] C. The code raises an unhandled exception.

---

### Question 30

What is the expected result of running the following code?

```python
def do_the_mass(parameter):
    variable += parameter[0]
    return variable

the_list = [x for x in range(2, 3)]
variable = -1
```

do_the_mass(the_list)

```python
print(variable)
```

**1 point**

- [ ] C. The code prints 1
- [ ] D. The code prints 2
- [ ] A. The code prints 0
- [ ] B.  The code raises an unhandled exception.

---

### Question 31

What is the expected output of the following code?

```python
def runner(brand, model="", year=2021, convertible=False):
    return (brand, str(year), str(convertible))

print(runner("Fermi")[2][2])
```

**1 point**

- [ ] D. ('Fermi, '2021' , 'False')
- [ ] C. False
- [ ] A. l
- [ ] B. The code raises an unhandled exception.

---

### Question 32

What is the expected output of the following code?

```python
def runner(brand, model="", year=2021, convertible=True):
    return (brand + model + str(convertible))

print(runner(model ="Reluctance", 2019 [1]))
```

**1 point**

- [ ] C. True
- [ ] B. The code raises an unhandled exception.
- [ ] A. Reluctance
- [ ] D. ()

---

### Question 33

What is the expected output of the following code?

```python
def runner(brand, model="", year=2021, convertible=False):
    return brand + model + str(convertible)

print(runner("Volta", "Tension", 2019)[-1])
```

**1 point**

- [ ] B. e
- [ ] D. The code raises an unhandled exception
- [ ] A. Volta Tension
- [ ] C. True

---

### Question 34

What is the expected output of the following code?

```python
def runner(brand, model="", year=2021, convertible=False):
    return (brand, str(year), str(convertible))

print(runner(model="Furious", brand="Ampere") [1][1])
```

**1 point**

- [ ] B. ('Ampere', '2021','False')
- [ ] C. The code raises an unhandled exception
- [ ] A. 2021
- [ ] D. 0

---

### Question 35

What is true about exceptions and debugging? (Select two answers.)

**1 point**

- [ ] A. A tool that allows you to precisely trace program execution is called debugger.
- [ ] C. One try-except block may contain more than one except branch.
- [ ] D. The default (anonymous) except branch cannot be the last branch in the try-except block.
- [ ] B. If some Python code is executed without errors, this proves that there are no errors in it.

---

### Question 36

Which of the following are the names of Python passing argument styles?

(Select two answers.)

**1 point**

- [ ] C. indicatory
- [ ] D. positional
- [ ] B. reference
- [ ] A. keyword

---

### Question 37

What is the expected result of the following code?

```python
def velocity(x):
    return speed + x

speed = 10

new_speed = velocity(10)
new_speed = velocity(new_speed)

print(new_speed)
```

**1 point**

- [ ] C. 10
- [ ] B. 20
- [ ] D. 30
- [ ] A. The code is erroneous and cannot be run.

---

### Question 38

What is the expected result of the following code?

```python
def velocity(x):
    return speed + x

speed = 10

new_speed = velocity()
new_speed = velocity(new_speed)

print(new_speed)
```

**1 point**

- [ ] D. 30
- [ ] A. The code is erroneous and cannot be run.
- [ ] B. 20
- [ ] C. 10

---

### Question 39

What is the expected result of the following code?

```python
def velocity(x=10):
    return speed + x

speed = 10

new_speed = velocity()
new_speed = velocity(new_speed)

print(new_speed)
```

**1 point**

- [ ] C. 10
- [ ] B. 20
- [ ] A. The code is erroneous and cannot be run.
- [ ] D. 30

---

### Question 40

What is the expected output of the following code?

```python
def traverse(stop):
    if stop == 0:
        return 0
    else:
        return stop * traverse(stop - 1)

print(traverse(2))
```

**1 point**

- [ ] D. 1
- [ ] B. 0
- [ ] A. 2
- [ ] C. 3

---

### Question 41

Which of the following functions can be invoked with two arguments? *(Adapted replacement: the original form renders its options as images, which are not present in this text copy.)*

**1 point**

- [ ] A. `def alpha(x, y): pass`
- [ ] B. `def beta(x, y=0): pass`
- [ ] C. `def gamma(x): pass`
- [ ] D. `def delta(): pass`

---

### Question 42

A program written in a high-level programming language is called:

**1 point**

- [ ] machine code
- [ ] a source code

---

### Question 43

Which condition should replace `???` so that this code outputs `***`?

```python
depth = 0

if ???:
    print("***")
else:
    print("---")
```

*(Adapted replacement: the original form renders the answer choices as images, which are not present in this text copy.)*

**1 point**

- [ ] A. `depth = 0`
- [ ] B. `depth == 0`
- [ ] C. `depth != 0`

---

### Question 44

What happens when the users runs the following code?

```python
speed = 3

while speed < 8:
    speed += 2
    if speed == 7:
        continue
    print("*", end="")

else:
    print("*")
```

**1 point**

- [ ] C. The program outputs five asterisks (*****) to the screen
- [ ] A. The program outputs one asterisk (*) to the screen
- [ ] B. The program outputs three asterisks(***) to the screen
- [ ] D. The program enters an infinite loop

---

### Question 45

Assuming that the following assignment has been successfully executed:

```python
the_list = ['list', False, 3e8]
```

Which one of the following prints True

**1 point**

- [ ] B. the_list[1] in the_list
- [ ] A. int(the_list[2]) == len(the_list)
- [ ] C. 300 in the_list and the_list[1]
- [ ] D. the_list.index(False) == 1

---

### Question 46

Which of the following sentences are true?

(Select three answers)

**1 point**

- [ ] D. It's possible to define more than one function of the same program
- [ ] A. A function can invoke itself
- [ ] B. Function is oblidged to return a value
- [ ] C. Every function must be defined before it is invoked

---

### Question 47

Python:

```python
    speed = float('48;4')

    print('Ok')

except:

    print('Failed')

    speed = None
```

Given the above lines of code, which word should be used to replace  Python in order to print Failed to the screen

**1 point**

- [ ] A. try
- [ ] C. for
- [ ] B. when

---

### Question 48

What is true about exceptions in Python?

(Select two answers)

**1 point**

- [ ] B. According to Python terminology, exceptions are raised
- [ ] C. Not more than one except branch can be executed in program
- [ ] D. According to Python terminology, exceptions are thrown
- [ ] A. Python's philosophy encourages developers to make all the occurrences of an execution

---

### Question 49

What is the expected output of the following code?

```python
def count(start):

    print(start, end=" ")

    if start > 0:
```

count(start -1)

count(3)

**1 point**

- [ ] D. 3 2 1
- [ ] A. 1 2 3
- [ ] C. 0 1 2 3
- [ ] B. 3 2 1 0

---

### Question 50

Assume the following assignment has been successfully executed:

```python
the_list = [True, 3.1474, -1]
```

Which of the following expression evaluate to True

(Select two)

**1 point**

- [ ] D. the_list.index(-1) == 2
- [ ] B. (len(the_list) == 3 in the_list)
- [ ] C. len(sorted(the_list)) != len(the_list)
- [ ] A. True in the_list

---

### Question 51

Assume the following assignment has been successfully executed:

```python
my_list = [1, 2, 4, 8]
```

Select the expressions which will not raise any exception

(Select two)

**1 point**

- [ ] C. my_list[-3:-2]
- [ ] B. my_list[my_list{3}]
- [ ] A. my_list[-2]
- [ ] D. my_list[4]

---

### Question 52

Which of the following functions can be invoked with one argument ?

**1 point**

- [ ] A. def eta(level,size, depth=0): pass
- [ ] D. def epsilion (level = 100): pass
- [ ] B. def theta(None): pass
- [ ] C. def zeta(): pass

---

### Question 53

Which of the following are the names of Python passing argument styles? (Select two)

**1 point**

- [ ] B. keyword
- [ ] D. indicatory
- [ ] A. reference
- [ ] C. positional

---

### Question 54

What is the expected result of the following code?

```python
def do_the_mess(parameter):
```

global variable

variable += parameter[0]

```python
  return variable



the_list = [x for x in range(2, 3)]

variable = 0
```

do_the_mess(the_list)

```python
print(variable)
```

**1 point**

- [ ] D. The code prints 0
- [ ] B. The code raises an unhandled exception
- [ ] A. The code prints 1
- [ ] C. The code prints 2

---

### Question 55

What is true about exceptions and debugging? (Select two answers)

**1 point**

- [ ] D. One try-except block may contain more than one except branch
- [ ] C. If some Python code is executed without errors, this proves that there are no errors in it
- [ ] B. A tool that allows you to precisely trace program execution is called a debugger
- [ ] A. The default (anonymouse) except branch cannot be the last branch in the try-except block

---

### Question 56

Operations that can be performed by CPU is called:

**1 point**

- [ ] B. an assembly order
- [ ] D. an instruction set
- [ ] C. the ASCII code
- [ ] A. a binary code

---

### Question 57

A set of elementary operations that can be performed by a CPU is called:

**1 point**

- [ ] A. an assembly order
- [ ] C. the ASCII code
- [ ] B. a binary code
- [ ] D. an instruction set

---

### Question 58

What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?

```python
x = float(input())
y = float(input())
print(y ** (1 / x ))
```

**1 point**

- [ ] C. 2.0
- [ ] A. 4.0
- [ ] B. 1.0
- [ ] D. 0.0

---

### Question 59

What is the expected results of running the following code?

```python
def do_the_mass(parameter):
```

global variable

variable += parameters[0]

```python
    return variable

the_list = [x for x in range(2,3)]

variable = 0
```

do_the_mass(the_list)

```python
print(variable)
```

**1 point**

- [ ] A. The code prints 0
- [ ] B. The code raises an unhandled exception
- [ ] D. The code prints 1
- [ ] C. The code prints 2

---

### Question 60

What is the expected output of the following code?

```python
menu = {"syrniki" : 12.8, "shashlik": 49.9, "borscht": 23.2}

for value in menu.items():

    print(value[1], end = "")
```

**1 point**

- [ ] B. 293
- [ ] C. The code is erroneous and cannot be run
- [ ] A. 12.849.923.2
- [ ] D. yh

---

### Question 61

What happens when the users  runs the following code?

```python
speed = 3

while speed < 8:

    speed += 2

    if speed == 7:

        continue

    print("*", end = "")

else:

    print("*")
```

**1 point**

- [ ] D. The program outputs one asterisks ( * ) to the screen
- [ ] A. The program enters an infinite loop
- [ ] C. The program outputs five asterisks ( ***** ) to the screen
- [ ] B. The program outputs three asterisks ( *** ) to the screen

---

### Question 62

How many hashes(#) does the code output to the screen?

```python
floor = 0

while floor != 0:

    floor -= 1

    print("#", end = "")

else:

    print("#")
```

**1 point**

- [ ] B. five
- [ ] C. zero(the code outputs nothing)
- [ ] D. Three
- [ ] A. One

---

### Question 63

To run the code given as a source file whose name has the .py extension, you need to have:

**1 point**

- [ ] C. a Python interpreter.
- [ ] D. a Python editor.
- [ ] B. a Python compiler .
- [ ] A. an MS windows computer.

---

### Question 64

A binary code consists of:

**1 point**

- [ ] B. a set of a certain alphabet symbols.
- [ ] A. a sequence of ASCII characters.
- [ ] D. a sequence of bits which encodes machine instructions.
- [ ] C. a list of keywords.

---

### Question 65

What is the expected output of the following code ?

```python
planets = 1 + 2 * 3 // 4

if planets < 0 :
```

print ( " # " )

```python
elif planets > 2:
       print( " # # ")
```

else :

```python
      print( " # # #")
```

**1 point**

- [ ] D. The code prodcues no output
- [ ] B. # # #
- [ ] C. # #
- [ ] A. #

---

### Question 66

What happens when the user runs the following code ?

```python
angle =  -1
for i in range ( -1 , 1) :
       if 2 * i < 4 :
             angle += 1
else:
    angle += 2
```

print (angle)

**1 point**

- [ ] B. The code outputs 3.
- [ ] A. The code enters an infinte loop.
- [ ] D. The code outputs 1.
- [ ] C. The code outputs 2.

---

### Question 67

What happens when the user runs the following code ?

```python
power = 2
while power < 5 :
         power += 1
         if power == 3 :
              continue
```

print ( "0" , end=" ")

```python
else:
```

print ("0")

**1 point**

- [ ] D. The program outputs one at sign ( 0 ) to the screen.
- [ ] B. The program outputs three at signs ( 0 0 0) to the screen.
- [ ] A. The program outputs two at signs ( 0 0 ) to the screen.
- [ ] C. The program enters an infinite loop.

---

### Question 68

What is the expected output of the following code?

```python
others = 1
for i in range (2, 4) :
      for j in range (-1, 2) :
            if  i == j:
                  others += 1
            else:
```

break

print (others)

**1 point**

- [ ] B. 4
- [ ] A. 3
- [ ] C. 1
- [ ] D. The code outputs nothing.

---

### Question 69

What is the expected output of the following code?

```python
list_one = [1, 2]
list_two = list_one[:]
list_two.append(3)
print(list_one[-1] + list_two[-1])
```

**1 point**

- [ ] D. The code raises an exception and outputs nothing.
- [ ] B. 4
- [ ] A. 6
- [ ] C. 5

---

### Question 70

What is the expected output of the following code?

```python
points = 0

for answer in selection[1:]:
   if answer: points += 1

print(points)
```

**1 point**

- [ ] C. Raises an unhandled exception
- [ ] B. 3
- [ ] A. 0
- [ ] D. 1

---

### Question 71

Assuming that the following assignment has been successfully executed:

```python
the_data = [ True , 3.1415, -2 ]
```

Which of the following expressions to evaluate False?

(Select two expressions.)

**1 point**

- [ ] A. the_data.index(the_data [ -1]) == 0
- [ ] C. -2 in the_data [2:4]
- [ ] D. the_data.index (-2) not in [the_data]
- [ ] B. len (the_data[0:2]) == 0

---

### Question 72

Assuming that the following assignment has been successfully executed:

```python
numbers = [ 1, 0.5, 0.25, 0.125]
```

Select the expressions which will not raise any exception.

(Select two expressions.)

**1 point**

- [ ] B. numbers[ -10 ]
- [ ] C. numbers [0]
- [ ] D. numbers[ numbers [1] ]
- [ ] A. numbers[ 0 : 4 ]

---

### Question 73

What is the expected result of the following code?

```python
def sample (value) :
       return total - value

total = 4

total = sample(2)
total = sample(1)
```

print (total)

**1 point**

- [ ] C. The code is erroneous and cannot be run.
- [ ] B. 2
- [ ] A. 4
- [ ] D. 1

---

### Question 74

What is the expected result of the following code?

```python
def process (data) :
      data = 2
      return data

measurements = [0 for i in range(3) ]
result = process(measurements)
```

print (result[-2])

**1 point**

- [ ] B. The code prints 2.
- [ ] A. The code prints 0.
- [ ] C. The code prints 1.
- [ ] D. The code raises an unhandled exception.

---

### Question 75

What is the expected output of the following code?

```python
def walk(top) :
       if top == 0 :
            return 0
       else:
            return top * walk(top - 1)

print(walk(2))
```

**1 point**

- [ ] A. 3
- [ ] D. 2
- [ ] C. 1
- [ ] B. 0

---

### Question 76

Which of the following functions can be invoked with three arguments?

**1 point**

- [ ] B. def two(y, z):
- [ ] C. def three(x, y, z):
- [ ] A. def one(x, y, z, v=0):
- [ ] D. def four(x, y, z, v):

---

### Question 77

Which of the following functions can be invoked with two arguments?

**1 point**

- [ ] B. def lambda(): pass
- [ ] A. def kappa(level): pass
- [ ] D. def iota(level, size=10): pass
- [ ] C. def mu(None): pass

---

### Question 78

What is the expected output of the following code?

```python
def combine (width, height=10, depth=0, is_3D=False) :
   if is _3D:
        return [ is_3D, width, height, depth]

print(combine (2) [0] )
```

**1 point**

- [ ] D. 0
- [ ] C. 2
- [ ] A. 1
- [ ] B. The code raises an unhandled exception.

---

### Question 79

Assuming the following runs successfully, which of the options would run without raising an exception ?

```python
my_list = [5,4,3,2]
```

**1 point**

- [ ] D. my_list[-5]
- [ ] A. my_list[my_list[-1]]
- [ ] C. my_list[1:1]
- [ ] B. my_list[4]

---

### Question 80

What is the expected output of the following code?

```python
counter = 11 * 4 - 2
if counter > 0 :
```

print ("*")

```python
elif counter >  42 :
```

print ("**")

```python
else:
```

print ("***")

**1 point**

- [ ] C. ***
- [ ] D. *
- [ ] B. The code produces no output
- [ ] A. **

---

### Question 81

What is the expected result of running the following code?

```python
def do_the_mess(parameter) :
      parameter = [  variable ]
      return parameter

the_list =  [ x for x in range(0, 1) ]

variable = -2
```

do_the_mess(the_list)

```python
print(the_list[0])
```

**1 point**

- [ ] C. The code prints 2.
- [ ] B. The code prints 0.
- [ ] D. The code prints 1.
- [ ] A. The code raises an unhandled eception.

---

### Question 82

Which of the following expressions evaluate to a zero result?

(Select two answers.)

**1 point**

- [ ] C. 4 -3 // 2 + 1
- [ ] B. 1 ** 2 -4 // 3
- [ ] A. 1 // 3 * 3  **  0
- [ ] D. 4  / 2 + 2 ** 1

---

### Question 83

Which of the following expressions evaluate to a zero result?

(Select two answers.)

**1 point**

- [ ] C. 4 / 1 * 2 - 1
- [ ] D. 1 + 2 / 4 * 3
- [ ] B. -1 / 3 * 3 + 1
- [ ] A. 2 // 4

---

### Question 84

Which of the following expressions evaluate to a zero result?

(Select two answers.)

**1 point**

- [ ] B. 2 / -3 * 6 + 4
- [ ] A. -3 / 2 * 4 + 1
- [ ] C. 3 ** 2 // 3 / 3 -1
- [ ] D. 2 // 2 * 2 + 3

---

### Question 85

Which of the following expressions evaluate to a zero result?

(Select two answers.)

**1 point**

- [ ] A. -1 / 3 * 3 + 1
- [ ] D. 1 + 2 / 4 * 3
- [ ] C. 4 / 1 * 2  - 1
- [ ] B. 2 // 4 * 1 / 3

---

### Question 86

How many asterisks (*) does the code output to the screen?

```python
torque = 0
while torque != 0:
         torque //= 2
```

print ("*", end=" ")

```python
else:
     print("*")
```

**1 point**

- [ ] C. zero(the code outputs nothing)
- [ ] B. two
- [ ] D. three
- [ ] A. one

---

### Question 87

What is the expected output of the following code?

```python
train_speed = {"FlyingScotsman":201, "TGV":320, "Shinkansen":320}

for train in train_speed.items():
  print(train[0], end="")
```

**1 point**

- [ ] A. FlyingScotsmanTGVShinkansen
- [ ] B. FTS
- [ ] D. The code is erroneous and cannot be run
- [ ] C. 233

---

### Question 88

What is the expected output of the following code?

```python
answers = (False, True, True)
selection = answers[:]
points = 0

for answer in selection[1:]:
    if answer:
       points += 1

print(points)
```

**1 point**

- [ ] D. 2
- [ ] C. 0
- [ ] B. 3
- [ ] A. 1

---

### Question 89

What is true about exceptions in Python? Select 2

**1 point**

- [ ] A. An unhandled exception causes the program to terminate
- [ ] D. IndexError may be raised when you try to access a nonexistent dictionery element
- [ ] C. The code put inside the try branch may not be fully executed
- [ ] B. If any of the raised exceptions remains unhandled, an error message is printed, and program execution continues

---

### Question 90

What of the following sentences are true? Select two answers

**1 point**

- [ ] A. A function declaration may be located anywhere inside the source code
- [ ] D. When a function body contains no return expression statement, the function returns None implicitly
- [ ] C. It's technically possible to name a variable using an already existing function name, but it will shadow that function
- [ ] B. A function cannot invoke itself

---

### Question 91

What of the following functions can be invoked with three arguments?

**1 point**

- [ ] C. def four():
- [ ] B. def one(x,y,z,v=0): pass
- [ ] A. def three(x, y=0): pass
- [ ] D. def two(speed,altitude): pass

---

### Question 92

What would the following evaluate to ?

```python
shift = 5 - 4 * 2

if shift > 0:
   print("#")

elif shift == 0:
   print("##")

elif shift < 0:
   print("###")
```

**1 point**

- [ ] A. #
- [ ] D. ###
- [ ] B. The code is errenous and will not run
- [ ] C. ##

---

### Question 93

Which of the following code snippets correctly define a function which returns its only argument doubled ?

**1 point**

- [ ] B. def double(value): return value * value
- [ ] A. def times_again(ar): return * ar
- [ ] C. def multiply_by_2: value*= 2
- [ ] D. def times_2(x): return x + x

---

### Question 94

What is the output of this code?

```python
def iterate(end, foo = 0):
    if end > 0:
        foo = iterate (end -1, foo + end)
    return foo

print(iterate(2))
```

**1 point**

- [ ] D. 0
- [ ] B. 2
- [ ] C. 3
- [ ] A. 1

---

### Question 95

What happens when the user runs the following code ?

```python
total = 0

for i in range(4):
    if 2 * i < 4:
        total += 1
else:
      total += 1

print(total)
```

**1 point**

- [ ] D. The code outputs 3
- [ ] C. The code outputs 2
- [ ] A. The code enters an infinite loop
- [ ] B. The code outputs 1

---

### Question 96

What is the expected output of the following code?

```python
counter = 7 ** 2 - 7

if counter < 0:
  print("*")
elif counter > 42:
  print("**")
else:
  print("***")
```

**1 point**

- [ ] D. *
- [ ] B. ***
- [ ] C. **
- [ ] A. The code produces no output

---

### Question 97

Which of the following functions can be invoked without arguments?

**1 point**

- [ ] A. def delta(level, size = 0): pass
- [ ] C. def beta(None): pass
- [ ] D. def gamma(level): pass
- [ ] B. def alpha(level=1000): pass

---

### Question 98

What is expected output of the following code?

```python
equals = 0

for i in range(2):
  for j in range(2):
     if i == j:
        equals += 1
     else:
         break

print(equals)
```

**1 point**

- [ ] C. 4
- [ ] A. 1
- [ ] D. 3
- [ ] B. The code outputs nothing

---

### Question 99

What is expected output of the following code?

```python
equals = 0

for i in range(2):
  for j in range(2):
     if i == j:
        equals += 1
else:
    equals += 1

print(equals)
```

**1 point**

- [ ] C. 4
- [ ] B. The code outputs nothing
- [ ] A. 1
- [ ] D. 3

---

### Question 100

What is expected output of the following code?

```python
total = 0

for i in range(4):
   if 2 * i > 4:
        total += 1

else:
     total += 1

print(total)
```

**1 point**

- [ ] D. 3
- [ ] A. Infinite loop
- [ ] B. 1
- [ ] C. 2

---

### Question 101

What is expected output of the following code?

```python
speed = 3

while speed < 0:
    speed **= 2
    if speed == 7:
        break
    print("*", end="")

else:
    print("*")
```

**1 point**

- [ ] A. *
- [ ] B. **
- [ ] C. Infinite loop
- [ ] D. ****

---

## Additional Questions

### Question 102

What term describes the meaning of a Python statement?


**1 point**

- [ ] A. lexis
- [ ] B. syntax
- [ ] C. semantics
- [ ] D. compilation

---
### Question 103

Which is a valid Python identifier?


**1 point**

- [ ] A. 2nd_value
- [ ] B. total-value
- [ ] C. class
- [ ] D. total_value

---
### Question 104

Which line is a Python comment?


**1 point**

- [ ] A. // comment
- [ ] B. # comment
- [ ] C. <!-- comment -->
- [ ] D. /* comment */

---
### Question 105

What is the type of True?


**1 point**

- [ ] A. int
- [ ] B. bool
- [ ] C. str
- [ ] D. float

---
### Question 106

What is the decimal value of 0b1011?


**1 point**

- [ ] A. 9
- [ ] B. 10
- [ ] C. 11
- [ ] D. 12

---
### Question 107

What is the decimal value of 0x10?


**1 point**

- [ ] A. 10
- [ ] B. 16
- [ ] C. 20
- [ ] D. 32

---
### Question 108

What is the value of 3e2?


**1 point**

- [ ] A. 3.2
- [ ] B. 30
- [ ] C. 300
- [ ] D. 3000

---
### Question 109

What is the result of 17 // 5?


**1 point**

- [ ] A. 2
- [ ] B. 3
- [ ] C. 3.4
- [ ] D. 4

---
### Question 110

What is the result of 17 % 5?


**1 point**

- [ ] A. 0
- [ ] B. 2
- [ ] C. 3
- [ ] D. 5

---
### Question 111

What is the result of 2 ** 3 ** 2?


**1 point**

- [ ] A. 64
- [ ] B. 128
- [ ] C. 256
- [ ] D. 512

---
### Question 112

What is the result of -2 ** 2?


**1 point**

- [ ] A. -4
- [ ] B. 4
- [ ] C. -8
- [ ] D. 8

---
### Question 113

What is the value of 7 / 2 in Python 3?


**1 point**

- [ ] A. 2
- [ ] B. 2.0
- [ ] C. 3
- [ ] D. 3.5

---
### Question 114

What is the result of "Py" + "thon"?


**1 point**

- [ ] A. "Python"
- [ ] B. "Py thon"
- [ ] C. "Py+thon"
- [ ] D. A TypeError

---
### Question 115

What is the result of "ha" * 3?


**1 point**

- [ ] A. "hahaha"
- [ ] B. "ha3"
- [ ] C. "ha ha ha"
- [ ] D. A TypeError

---
### Question 116

What is the value of not (3 > 1)?


**1 point**

- [ ] A. True
- [ ] B. False
- [ ] C. 3
- [ ] D. 1

---
### Question 117

What is the value of True or False and False?


**1 point**

- [ ] A. True
- [ ] B. False
- [ ] C. None
- [ ] D. A SyntaxError

---
### Question 118

What is the value of (5 == 5) and (2 > 8)?


**1 point**

- [ ] A. True
- [ ] B. False
- [ ] C. 5
- [ ] D. 2

---
### Question 119

Which operator tests whether two values are different?


**1 point**

- [ ] A. =<
- [ ] B. !=
- [ ] C. <>
- [ ] D. !==

---
### Question 120

What is the result of 5 & 3?


**1 point**

- [ ] A. 0
- [ ] B. 1
- [ ] C. 2
- [ ] D. 7

---
### Question 121

What is the result of 4 << 1?


**1 point**

- [ ] A. 2
- [ ] B. 4
- [ ] C. 8
- [ ] D. 16

---
### Question 122

What is the result of ~0?


**1 point**

- [ ] A. 0
- [ ] B. 1
- [ ] C. -1
- [ ] D. -2

---
### Question 123

What does input() return before explicit conversion?


**1 point**

- [ ] A. An integer
- [ ] B. A float
- [ ] C. A string
- [ ] D. A Boolean

---
### Question 124

What is printed by print("A", "B", sep="-", end="!")?


**1 point**

- [ ] A. A B!
- [ ] B. A-B!
- [ ] C. A-B
- [ ] D. AB!

---
### Question 125

Which two expressions convert the string "12" to a numeric value?


(Select two answers.)

**1 point**

- [ ] A. int("12")
- [ ] B. float("12")
- [ ] C. number("12")
- [ ] D. str(12)

---
### Question 126

What is printed by: value = 8; if value > 10: print("high"); else: print("low")?


**1 point**

- [ ] A. high
- [ ] B. low
- [ ] C. Nothing
- [ ] D. An infinite loop

---
### Question 127

What is printed when score = 75 and the branches test >=80, then >=70, then else?


**1 point**

- [ ] A. A
- [ ] B. B
- [ ] C. C
- [ ] D. Nothing

---
### Question 128

If x = 4, which nested test prints the result of x % 2 == 0?


**1 point**

- [ ] A. even
- [ ] B. odd
- [ ] C. negative
- [ ] D. Nothing

---
### Question 129

Which statement does nothing and is syntactically valid?


**1 point**

- [ ] A. skip
- [ ] B. continue
- [ ] C. pass
- [ ] D. empty

---
### Question 130

What values are produced by range(2, 7)?


**1 point**

- [ ] A. 2, 3, 4, 5, 6
- [ ] B. 2, 3, 4, 5, 6, 7
- [ ] C. 1, 2, 3, 4, 5, 6
- [ ] D. 7, 6, 5, 4, 3, 2

---
### Question 131

How many iterations does range(1, 10, 3) produce?


**1 point**

- [ ] A. 2
- [ ] B. 3
- [ ] C. 4
- [ ] D. 9

---
### Question 132

What is the sum produced by: total = 0; for number in range(1, 4): total += number?


**1 point**

- [ ] A. 3
- [ ] B. 5
- [ ] C. 6
- [ ] D. 7

---
### Question 133

What is printed by a while loop starting at count = 3 and decrementing to zero, with end=""?


**1 point**

- [ ] A. 012
- [ ] B. 123
- [ ] C. 321
- [ ] D. 333

---
### Question 134

What is printed when a loop over "abc" continues when the letter is "b"?


**1 point**

- [ ] A. abc
- [ ] B. ac
- [ ] C. bc
- [ ] D. ab

---
### Question 135

What is printed when a loop breaks when number == 3, before printing the number?


**1 point**

- [ ] A. 012
- [ ] B. 0123
- [ ] C. 1234
- [ ] D. 01234

---
### Question 136

What does a completed for loop followed by else execute?


**1 point**

- [ ] A. The loop's else block
- [ ] B. Only the first iteration
- [ ] C. Nothing
- [ ] D. An infinite loop

---
### Question 137

What happens to a loop's else block if the loop exits with break?


**1 point**

- [ ] A. It always runs
- [ ] B. It runs twice
- [ ] C. It does not run
- [ ] D. It raises TypeError

---
### Question 138

What is printed when number starts at 0 and a while loop increments it while number < 3, followed by else printing it?


**1 point**

- [ ] A. 0
- [ ] B. 2
- [ ] C. 3
- [ ] D. Nothing

---
### Question 139

Which two statements correctly describe break?


(Select two answers.)

**1 point**

- [ ] A. It terminates the nearest loop.
- [ ] B. It skips only the current iteration.
- [ ] C. It prevents that loop's else clause after breaking.
- [ ] D. It can be used outside a loop without error.

---
### Question 140

Which two statements correctly describe continue?


(Select two answers.)

**1 point**

- [ ] A. It skips the rest of the current iteration.
- [ ] B. It terminates every enclosing loop.
- [ ] C. It starts the next iteration of the nearest loop.
- [ ] D. It can replace break in every situation.

---
### Question 141

What is the final result when two outer iterations each contain three inner iterations and result starts at zero, increasing once per inner iteration?


**1 point**

- [ ] A. 2
- [ ] B. 3
- [ ] C. 5
- [ ] D. 6

---
### Question 142

How many even numbers are counted in range(4)?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. 4

---
### Question 143

What is printed when value starts at 1 and is doubled while value < 10?


**1 point**

- [ ] A. 8
- [ ] B. 10
- [ ] C. 16
- [ ] D. 20

---
### Question 144

What is printed by range(3, 0, -1) with end=""?


**1 point**

- [ ] A. 012
- [ ] B. 123
- [ ] C. 321
- [ ] D. 4321

---
### Question 145

What is printed by a for loop containing only pass, followed by print("done")?


**1 point**

- [ ] A. Nothing
- [ ] B. done
- [ ] C. pass
- [ ] D. An exception

---
### Question 146

Which condition is true when x is even and greater than 10?


**1 point**

- [ ] A. x > 10 or x % 2 == 0
- [ ] B. x > 10 and x % 2 == 0
- [ ] C. x < 10 and x % 2 == 1
- [ ] D. x == 10 and x % 2 == 0

---
### Question 147

What is printed when value == 10 and the if suite contains pass, followed by print("ready")?


**1 point**

- [ ] A. Nothing
- [ ] B. pass
- [ ] C. ready
- [ ] D. A NameError

---
### Question 148

What is the sum from 1 through 4 when number == 3 is skipped with continue?


**1 point**

- [ ] A. 6
- [ ] B. 7
- [ ] C. 9
- [ ] D. 10

---
### Question 149

What is printed when x increases from 0 to 3 and x == 2 is skipped with continue?


**1 point**

- [ ] A. 123
- [ ] B. 13
- [ ] C. 12
- [ ] D. 23

---
### Question 150

Which two loops can iterate over every character in "cat"?


(Select two answers.)

**1 point**

- [ ] A. for character in "cat":
- [ ] B. for character in range("cat"):
- [ ] C. for character in ["c", "a", "t"]:
- [ ] D. while "cat":

---
### Question 151

What is the first value produced by range(5, 0, -2)?


**1 point**

- [ ] A. 0
- [ ] B. 1
- [ ] C. 3
- [ ] D. 5

---
### Question 152

What is the value of [10, 20, 30][1]?


**1 point**

- [ ] A. 10
- [ ] B. 20
- [ ] C. 30
- [ ] D. An IndexError

---
### Question 153

What is the value of [10, 20, 30][-1]?


**1 point**

- [ ] A. 10
- [ ] B. 20
- [ ] C. 30
- [ ] D. An IndexError

---
### Question 154

What is the result of [1, 2, 3][1:]?


**1 point**

- [ ] A. [1]
- [ ] B. [2, 3]
- [ ] C. [1, 2]
- [ ] D. [3]

---
### Question 155

What is the result of [1, 2, 3][:2]?


**1 point**

- [ ] A. [1]
- [ ] B. [2, 3]
- [ ] C. [1, 2]
- [ ] D. [1, 2, 3]

---
### Question 156

What is printed after items = [1, 2]; items.append(3)?


**1 point**

- [ ] A. [1, 2]
- [ ] B. [3, 1, 2]
- [ ] C. [1, 2, 3]
- [ ] D. [1, 3, 2]

---
### Question 157

What is printed after items = [1, 2]; items.insert(1, 9)?


**1 point**

- [ ] A. [9, 1, 2]
- [ ] B. [1, 9, 2]
- [ ] C. [1, 2, 9]
- [ ] D. [1, 2]

---
### Question 158

What does len([4, 5, 6, 7]) return?


**1 point**

- [ ] A. 3
- [ ] B. 4
- [ ] C. 5
- [ ] D. 7

---
### Question 159

What does sorted([3, 1, 2]) return?


**1 point**

- [ ] A. [3, 2, 1]
- [ ] B. [1, 2, 3]
- [ ] C. None
- [ ] D. A TypeError

---
### Question 160

What is [1, 2, 3] after del items[1]?


**1 point**

- [ ] A. [1, 2]
- [ ] B. [2, 3]
- [ ] C. [1, 3]
- [ ] D. [1, 2, 3]

---
### Question 161

Which two expressions are true for [1, 2, 3]?


(Select two answers.)

**1 point**

- [ ] A. 2 in [1, 2, 3]
- [ ] B. 4 in [1, 2, 3]
- [ ] C. 4 not in [1, 2, 3]
- [ ] D. 1 not in [1, 2, 3]

---
### Question 162

What is [x * 2 for x in range(3)]?


**1 point**

- [ ] A. [0, 1, 2]
- [ ] B. [0, 2, 4]
- [ ] C. [2, 4, 6]
- [ ] D. [1, 2, 3]

---
### Question 163

What is matrix[1][0] for matrix = [[1, 2], [3, 4]]?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. 4

---
### Question 164

A slice copy is made with original[:] . If copy.append(3), what is len(original) for original = [1, 2]?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. An exception

---
### Question 165

If alias = original and alias.append(3), what is len(original) for original = [1, 2]?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. An exception

---
### Question 166

What is the result of (1, 2, 3)[-2]?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. An IndexError

---
### Question 167

Which two statements about tuples are true?


(Select two answers.)

**1 point**

- [ ] A. Tuples are immutable.
- [ ] B. Tuples cannot be indexed.
- [ ] C. Tuples can be sliced.
- [ ] D. Tuples must contain unique values.

---
### Question 168

What creates a one-element tuple?


**1 point**

- [ ] A. (5)
- [ ] B. [5]
- [ ] C. (5,)
- [ ] D. {5}

---
### Question 169

What is the result of (1, 2) + (3,)?


**1 point**

- [ ] A. (1, 2, 3)
- [ ] B. [1, 2, 3]
- [ ] C. (1, 2)(3,)
- [ ] D. A TypeError

---
### Question 170

What is printed by person = {"name": "Ada", "age": 30}; print(person["name"])?


**1 point**

- [ ] A. Ada
- [ ] B. name
- [ ] C. 30
- [ ] D. A KeyError

---
### Question 171

Which statement adds or replaces the key "city"?


**1 point**

- [ ] A. data.add("city", "Paris")
- [ ] B. data["city"] = "Paris"
- [ ] C. data.insert("city", "Paris")
- [ ] D. data.append("city", "Paris")

---
### Question 172

What is len({"a": 1, "b": 2})?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. 3
- [ ] D. 4

---
### Question 173

Which two expressions test for the presence of a dictionary key?


(Select two answers.)

**1 point**

- [ ] A. "a" in data
- [ ] B. "a" in data.keys()
- [ ] C. data.contains("a")
- [ ] D. data.has_key("a")

---
### Question 174

What does data.values() provide?


**1 point**

- [ ] A. The dictionary's keys
- [ ] B. The key-value pairs
- [ ] C. The dictionary's values
- [ ] D. A sorted list of keys

---
### Question 175

What does a for key in data loop over for data = {"a": 1, "b": 2}?


**1 point**

- [ ] A. The values 1 and 2
- [ ] B. The keys a and b
- [ ] C. The key-value pairs
- [ ] D. Nothing

---
### Question 176

What is the result of "Python"[1:4]?


**1 point**

- [ ] A. Pyt
- [ ] B. yth
- [ ] C. ytho
- [ ] D. tho

---
### Question 177

What is the value of "hello"[-1]?


**1 point**

- [ ] A. h
- [ ] B. e
- [ ] C. o
- [ ] D. An IndexError

---
### Question 178

What is printed by add(a, b) returning a + b when called as add(2, 3)?


**1 point**

- [ ] A. 2
- [ ] B. 3
- [ ] C. 5
- [ ] D. None

---
### Question 179

What does a function return when it reaches the end without return?


**1 point**

- [ ] A. 0
- [ ] B. False
- [ ] C. None
- [ ] D. An exception

---
### Question 180

What is printed when show(value) prints value but has no return, then result = show(4); print(result)?


**1 point**

- [ ] A. 4 only
- [ ] B. None only
- [ ] C. 4 followed by None
- [ ] D. An exception

---
### Question 181

Which two are valid function definitions?


(Select two answers.)

**1 point**

- [ ] A. def calculate(x): return x
- [ ] B. function calculate(x): return x
- [ ] C. def calculate(x=0): pass
- [ ] D. define calculate(x): pass

---
### Question 182

What is returned by greet(name="friend") when greet() is called?


**1 point**

- [ ] A. Hello
- [ ] B. Hello friend
- [ ] C. friend
- [ ] D. A TypeError

---
### Question 183

What is returned by combine(first, second="!") when combine("Hi") is called?


**1 point**

- [ ] A. Hi
- [ ] B. Hi!
- [ ] C. !
- [ ] D. A TypeError

---
### Question 184

What is returned by describe(name, age) when called as describe(age=20, name="Sam")?


**1 point**

- [ ] A. Sam:20
- [ ] B. 20:Sam
- [ ] C. Sam20
- [ ] D. A TypeError

---
### Question 185

Which two calls correctly invoke power(base, exponent)?


(Select two answers.)

**1 point**

- [ ] A. power(2, 3)
- [ ] B. power(base=2, exponent=3)
- [ ] C. power(2, exponent, 3)
- [ ] D. power(base: 2, exponent: 3)

---
### Question 186

If change(value) assigns value = 99, what is printed after number = 5; change(number); print(number)?


**1 point**

- [ ] A. 5
- [ ] B. 99
- [ ] C. None
- [ ] D. A NameError

---
### Question 187

If add_item(items) calls items.append("new"), what is len(values) after values = [] and add_item(values)?


**1 point**

- [ ] A. 0
- [ ] B. 1
- [ ] C. 2
- [ ] D. A TypeError

---
### Question 188

What is printed when global value = 10, show() has local value = 20 and returns it, and print(show(), value) runs?


**1 point**

- [ ] A. 10 10
- [ ] B. 20 20
- [ ] C. 20 10
- [ ] D. 10 20

---
### Question 189

Which keyword allows a function to assign to a module-level variable?


**1 point**

- [ ] A. outer
- [ ] B. global
- [ ] C. public
- [ ] D. nonlocal

---
### Question 190

What is printed when counter = 1, increase() declares global counter and increments it, then counter is printed?


**1 point**

- [ ] A. 1
- [ ] B. 2
- [ ] C. None
- [ ] D. A SyntaxError

---
### Question 191

What is factorial(3) for a recursive factorial with base case n == 0 returning 1?


**1 point**

- [ ] A. 3
- [ ] B. 6
- [ ] C. 9
- [ ] D. indefinite

---
### Question 192

What is the purpose of a recursion base case?


**1 point**

- [ ] A. To call the function again
- [ ] B. To stop recursive calls
- [ ] C. To create a global variable
- [ ] D. To handle input

---
### Question 193

Which two are built-in exception classes?


(Select two answers.)

**1 point**

- [ ] A. ValueError
- [ ] B. IndexError
- [ ] C. ProblemError
- [ ] D. LoopError

---
### Question 194

Which exception is raised by int("abc")?


**1 point**

- [ ] A. IndexError
- [ ] B. KeyError
- [ ] C. TypeError
- [ ] D. ValueError

---
### Question 195

Which exception is raised by [1, 2][5]?


**1 point**

- [ ] A. IndexError
- [ ] B. KeyError
- [ ] C. ValueError
- [ ] D. NameError

---
### Question 196

Which exception is raised by {"a": 1}["b"]?


**1 point**

- [ ] A. IndexError
- [ ] B. KeyError
- [ ] C. ValueError
- [ ] D. NameError

---
### Question 197

Which exception is raised by 1 + "1"?


**1 point**

- [ ] A. IndexError
- [ ] B. KeyError
- [ ] C. TypeError
- [ ] D. ValueError

---
### Question 198

Which exception is raised by float("abc")?


**1 point**

- [ ] A. IndexError
- [ ] B. KeyError
- [ ] C. TypeError
- [ ] D. ValueError

---
### Question 199

What is printed when 10 / 0 is inside try and except ZeroDivisionError prints "zero"?


**1 point**

- [ ] A. 10
- [ ] B. 0
- [ ] C. zero
- [ ] D. Nothing

---
### Question 200

What is printed when a missing dictionary key is caught by except KeyError?


**1 point**

- [ ] A. missing
- [ ] B. other
- [ ] C. Nothing
- [ ] D. A SyntaxError
