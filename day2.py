"""
day 2


Reminder from day1:
✅ List       Ordered, changeable, duplicates allowed ... []
✅ Tuple      Ordered, fixed, duplicates allowed      ... ()
✅ Set        Unordered, unique values only           ... {}
✅ Dictionary Key-value pairs, keys must be unique    ... {abc:xyz, def:fgh}
| Container      | Best used for                    | Example                                                 |
| -------------- | -------------------------------- | ------------------------------------------------------- |
| **List**       | A collection that changes        | Shopping list, students, tasks                          |
| **Tuple**      | Fixed data that shouldn't change | GPS coordinate `(33.9, 25.6)`, RGB colour `(255, 0, 0)` |
| **Set**        | Unique items only                | Employee IDs, tags, permissions                         |
| **Dictionary** | Look up a value by a key         | Person → phone number, product → price                 |
"""

age = 18    #if/ else ... choose two paths
if age >= 18:   print("Adult")
else:           print("Child")

print("For loop")  #repeats the code
for number in range(3):
    print(number)

c= 5
for i in range(0, c): print(i)

print("While loop:")  #repeats while the condition stays true
count = 0
while count < 3:
    print(count)
    count += 1
    
print("Break") #stops the loop compltely
for number in range(10):
    if number == 5:
        break
    
print("Continue") #skips current round and goes to the next
for number in range(5):
    if number == 2:
        continue
    print(number)

#pass does nothing. placeholder
if age >= 18:
    pass

print("if elif else") #if / elif / else
mark = 78
if mark >= 80:
    print("Distinction")
elif mark >= 65:
    print("Very good!")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")

#Nested if/else
age = 18 ; has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Fetch your ID")
else:
    print("Too young")

age = 60
a = "Adult" if age >= 50 else "Child"
print(a)


##Iterate through a list
mylist = ["python","is","great"]
for i in range(len(mylist)): print(mylist[i])

##Iterate through a list
mylist = ["python","is","great"]
for i in range(len(mylist)): print("I love python")

#iterate list and then print when it ends
digits = [0,3,7]
for i in digits:
    print(i)
else:
    print("No items left")

#same as above, using while loop
counter = 0
while counter < 5:
    print('inside loop')
    counter = counter + 1
else:
    print('inside else')

#break in while
count = 1
while count < 5:
    print(count)
    if count == 3:
        break
    count += 1

"""
#continue
print("continue")
count = 1
while count < 5:
    if count == 3:
        continue    #demo infinite loop
    print(count)
    count += 1
"""


#outer and inner function - indentation matter
def first():              # outer function
    print("Starting")
    def second():         # inner function because it is indented
        print("Inside")
    second()              # calls the inner function
first()                   # calls the outer function

#classes
class Example:
    pass
def function(args):
    pass

#functions continued
def greet():
    print("Hello world")
greet()

def add_number(num1,num2):
    sum = num1 + num2
    print("Sum is ", sum)

add_number(1,8)

def add(a, b):
    return a+b
answer = add(5,3)
print(answer)

def find_sq(num):
    result = num * num
    return result
sqr = find_sq(5)
print("SQ is ", sqr)
print("sqr is", find_sq(6))

print(True > False)
print(True < False)

# add math module
import math
square_root = math.sqrt(4)
print(square_root)

print(math.sqrt(25))	#5.0
print(math.pow(2,3))	#8.0
print(math.floor(3.9))	#3
print(math.ceil(3.1))	#4
print(math.pi)			#3.14

print(type(math.sqrt(25)))
abc = int(math.sqrt(35))
print(type(abc)) ; print(abc)

#import whole module
import math
print(math.sqrt(16))
#import only one function
from math import sqrt
print(sqrt(16))
#give it a shorter alias
import math as m
print(m.sqrt(16))

"""
Built-in functions
print()  → display output
input()  → receive user input
type()   → show a value’s type
len()    → count items
range()  → produce a sequence for loops
int()    → convert to integer
float()  → convert to float
str()    → convert to string
"""
#default values on functions:
def greet(name="Jacques"):
    print("Hello", name)
greet()
greet("Isaac")

def add_number(num1 = 3, num2 = 4):
    result = num1 + num2
    print("Answer:",result)
add_number()
add_number(num1=100)

#answer in any order
def names(arg1, arg2, arg3):
    print(arg1, arg2, arg3, sep=" ")

names(arg2="Doe",arg1="John",arg3="Botha")

#Recursion
def countdown(number):
    print(number)
    if number > 0:
        countdown(number - 1)
countdown(3)

#Factorial recursively
def factorial(number):
    if number == 0: return 1
    return number * factorial(number - 1)

print(factorial(5))







