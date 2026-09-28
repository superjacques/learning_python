# PCAP-31-03 Mock Exam

**Practice mock expanded from the supplied original; the added items are original practice questions, not official exam questions.** Official syllabus, objectives, and exam information: [Python Institute PCAP-31-03 Exam Syllabus](https://pythoninstitute.org/certification/pcap-certification-associate/pcap-exam-syllabus). Suggested practice time: 260 minutes. One point per question; select all answers where stated. The official exam may use other item formats.

## Weighting

| Section | Official weight | Questions |
|---|---:|---:|
| Modules and Packages | 12% | 24 |
| Exceptions | 14% | 28 |
| Strings | 18% | 36 |
| Object-Oriented Programming | 34% | 68 |
| Miscellaneous (List Comprehensions, Lambdas, Closures, I/O) | 22% | 44 |
| **Total** | **100%** | **200** |

## Questions

### Section Modules and Packages (24)

**1.** Given `import math as m`, which expression calculates the square root of 49?

A. `math.sqrt(49)`  
B. `m.sqrt(49)`  
C. `sqrt.m(49)`  
D. `from m import sqrt(49)`

**2.** Given `from math import sqrt as root`, which call is valid?

A. `math.sqrt(16)`  
B. `sqrt(16)`  
C. `root(16)`  
D. `math.root(16)`

**3.** What does `dir(module)` normally return?

A. A list of names available on the module  
B. A list of directories Python searches  
C. The module's source code as one string  
D. The module's imported values only, excluding functions

**4.** Which statement about `sys.path` is correct?

A. It stores the names of all currently running Python processes.  
B. It is a sequence of locations Python searches for modules and packages.  
C. It stores only the current working directory.  
D. It lists modules that have already been imported.

**5.** `helper.py` contains `print(__name__)`. `main.py` contains `import helper`. The learner executes `python main.py`. What does `helper.py` print?

A. `__main__`  
B. `helper`  
C. `main`  
D. Nothing

**6.** Which TWO statements are true? *(Select two.)*

A. `sample([1, 2, 3], 2)` returns a list of two selections without replacement.  
B. `random()` may return exactly `1.0`.  
C. Resetting the same seed before the same random call reproduces its result.  
D. `choice([1, 2, 3])` returns a two-element list.

### Section 2 — Exceptions (5)

**7.** With `import math as m`, which expression returns the square root of 36?

A. m.sqrt(36)
B. math.sqrt(36)
C. sqrt(m, 36)
D. from m import sqrt(36)

**8.** Given `from math import floor as down`, which call is valid?

A. math.floor(4.8)
B. floor(4.8)
C. math.down(4.8)
D. down(4.8)

**9.** What information is stored in `sys.path`?

A. The current process ID
B. The version history of the interpreter
C. Locations Python searches when importing modules
D. Names of all imported modules

**10.** What does `dir(some_module)` normally provide?

A. A list of every installed package version
B. Names defined or available on the module
C. The module source as executable bytecode
D. Only names imported from the operating system

**11.** `helper0.py` is imported by `main.py`. What is `__name__` inside the imported helper module?

A. `helper0`
B. `__main__`
C. `main`
D. An empty string

**12.** Which statement about `random.sample(population, k)` is correct?

A. It always returns the same values without seeding
B. It can return more items than the population contains
C. It changes the population list in place
D. It returns `k` selections without replacement

**13.** Which statement about `math.ceil(3.2)` is correct?

A. It returns the integer 3
B. It raises `ValueError`
C. It returns the integer 4
D. It returns the float 3.2

**14.** With `import math as calc`, which expression returns the square root of 36?

A. from calc import sqrt(36)
B. calc.sqrt(36)
C. math.sqrt(36)
D. sqrt(calc, 36)

**15.** Given `from math import floor as down`, which call is valid?

A. down(4.8)
B. math.floor(4.8)
C. floor(4.8)
D. math.down(4.8)

**16.** What information is stored in `sys.path`?

A. Names of all imported modules
B. The current process ID
C. The version history of the interpreter
D. Locations Python searches when importing modules

**17.** What does `dir(some_module)` normally provide?

A. Only names imported from the operating system
B. A list of every installed package version
C. Names defined or available on the module
D. The module source as executable bytecode

**18.** `helper1.py` is imported by `main.py`. What is `__name__` inside the imported helper module?

A. An empty string
B. `helper1`
C. `__main__`
D. `main`

**19.** Which statement about `random.sample(population, k)` is correct?

A. It returns `k` selections without replacement
B. It always returns the same values without seeding
C. It can return more items than the population contains
D. It changes the population list in place

**20.** Which statement about `math.ceil(3.2)` is correct?

A. It returns the float 3.2
B. It returns the integer 3
C. It raises `ValueError`
D. It returns the integer 4

**21.** With `import math as lib`, which expression returns the square root of 36?

A. sqrt(lib, 36)
B. from lib import sqrt(36)
C. lib.sqrt(36)
D. math.sqrt(36)

**22.** Given `from math import floor as down`, which call is valid?

A. math.down(4.8)
B. down(4.8)
C. math.floor(4.8)
D. floor(4.8)

**23.** What information is stored in `sys.path`?

A. Locations Python searches when importing modules
B. Names of all imported modules
C. The current process ID
D. The version history of the interpreter

**24.** What does `dir(some_module)` normally provide?

A. The module source as executable bytecode
B. Only names imported from the operating system
C. A list of every installed package version
D. Names defined or available on the module

### Section Exceptions (28)

**25.** What is printed?

```python
try:
    int("12x")
except ValueError:
    print("bad value")
else:
    print("ok")
finally:
    print("done")
```

A. `ok` then `done`  
B. `bad value` then `done`  
C. `bad value` only  
D. The exception is unhandled

**26.** Which ordering allows a `ValueError` handler to run before a general handler?

A.
```python
except Exception:
    ...
except ValueError:
    ...
```

B.
```python
except ValueError:
    ...
except Exception:
    ...
```

C.
```python
except:
    ...
except ValueError:
    ...
```

D. Exception handlers can be in any order.

**27.** What does a bare `raise` inside an `except` block normally do?

A. Creates a new `TypeError`  
B. Re-raises the current exception  
C. Suppresses the current exception  
D. Raises the first exception in the hierarchy

**28.** What happens?

```python
value = 4
assert value > 10, "too small"
```

A. Prints `too small` and continues  
B. Raises `AssertionError` with the message  
C. Raises `ValueError`  
D. Does nothing because `value` exists

**29.** Which definition creates a valid custom exception class?

A.
```python
class DataError(Exception):
    pass
```

B.
```python
exception DataError:
    pass
```

C.
```python
def DataError(Exception):
    pass
```

D.
```python
class DataError:
    raise Exception
```

### Section 3 — Strings (8)

**30.** To ensure `ValueError` is caught before `Exception`, how should the handlers be ordered?

A. Put `except ValueError` before `except Exception`
B. Put `except Exception` first
C. Put the handlers in separate `try` blocks only
D. Handler order never matters

**31.** When does a `finally` block run in ordinary `try`/`except` flow?

A. Only when an exception is unhandled
B. Only when the try block succeeds
C. Only when `else` is present
D. After the try/except handling, whether or not an exception occurred

**32.** What does a bare `raise` inside an active `except` block do?

A. Suppresses the exception
B. Returns from the function
C. Re-raises the currently handled exception
D. Raises a new `ValueError`

**33.** Which is a valid custom exception definition?

A. `class RecordError: Exception`
B. `class RecordError(Exception): pass`
C. `exception RecordError: pass`
D. `def RecordError(Exception): pass`

**34.** What exception does `int("12x")` raise?

A. `ValueError`
B. `TypeError`
C. `IndexError`
D. `KeyError`

**35.** What is the effect of `assert total >= 0, "negative"` when the condition is false?

A. It prints the message and continues
B. It raises `ValueError`
C. It silently sets `total` to zero
D. It raises `AssertionError` with the supplied message

**36.** Which header catches either `OSError` or `ValueError` in one handler?

A. `except OSError, ValueError:`
B. `except [OSError, ValueError]:`
C. `except (OSError, ValueError):`
D. `except OSError or ValueError:`

**37.** If an exception is not caught in the current function, what normally happens?

A. It restarts the function
B. It propagates to the caller
C. It is converted to `None`
D. It is caught automatically by `finally`

**38.** To ensure `ValueError` is caught before `Exception`, how should the handlers be ordered?

A. Put `except ValueError` before `except Exception`
B. Put `except Exception` first
C. Put the handlers in separate `try` blocks only
D. Handler order never matters

**39.** When does a `finally` block run in ordinary `try`/`except` flow?

A. Only when an exception is unhandled
B. Only when the try block succeeds
C. Only when `else` is present
D. After the try/except handling, whether or not an exception occurred

**40.** What does a bare `raise` inside an active `except` block do?

A. Suppresses the exception
B. Returns from the function
C. Re-raises the currently handled exception
D. Raises a new `ValueError`

**41.** Which is a valid custom exception definition?

A. `class RecordError: Exception`
B. `class RecordError(Exception): pass`
C. `exception RecordError: pass`
D. `def RecordError(Exception): pass`

**42.** What exception does `int("12x")` raise?

A. `ValueError`
B. `TypeError`
C. `IndexError`
D. `KeyError`

**43.** What is the effect of `assert total >= 0, "negative"` when the condition is false?

A. It prints the message and continues
B. It raises `ValueError`
C. It silently sets `total` to zero
D. It raises `AssertionError` with the supplied message

**44.** Which header catches either `OSError` or `ValueError` in one handler?

A. `except OSError, ValueError:`
B. `except [OSError, ValueError]:`
C. `except (OSError, ValueError):`
D. `except OSError or ValueError:`

**45.** If an exception is not caught in the current function, what normally happens?

A. It restarts the function
B. It propagates to the caller
C. It is converted to `None`
D. It is caught automatically by `finally`

**46.** To ensure `ValueError` is caught before `Exception`, how should the handlers be ordered?

A. Put `except ValueError` before `except Exception`
B. Put `except Exception` first
C. Put the handlers in separate `try` blocks only
D. Handler order never matters

**47.** When does a `finally` block run in ordinary `try`/`except` flow?

A. Only when an exception is unhandled
B. Only when the try block succeeds
C. Only when `else` is present
D. After the try/except handling, whether or not an exception occurred

**48.** What does a bare `raise` inside an active `except` block do?

A. Suppresses the exception
B. Returns from the function
C. Re-raises the currently handled exception
D. Raises a new `ValueError`

**49.** Which is a valid custom exception definition?

A. `class RecordError: Exception`
B. `class RecordError(Exception): pass`
C. `exception RecordError: pass`
D. `def RecordError(Exception): pass`

**50.** What exception does `int("12x")` raise?

A. `ValueError`
B. `TypeError`
C. `IndexError`
D. `KeyError`

**51.** What is the effect of `assert total >= 0, "negative"` when the condition is false?

A. It prints the message and continues
B. It raises `ValueError`
C. It silently sets `total` to zero
D. It raises `AssertionError` with the supplied message

**52.** Which header catches either `OSError` or `ValueError` in one handler?

A. `except OSError, ValueError:`
B. `except [OSError, ValueError]:`
C. `except (OSError, ValueError):`
D. `except OSError or ValueError:`

### Section Strings (36)

**53.** What does `ord("A")` return?

A. The string `"65"`  
B. The integer code point for `A`  
C. The character after `A`  
D. A UTF-8 byte sequence

**54.** What does `chr(9731)` return?

A. An integer  
B. A one-character string  
C. A list of bytes  
D. `None`

**55.** What is printed?

```python
s = "Python"
print(s[-1], s[1:4])
```

A. `P yth`  
B. `n yth`  
C. `n ytho`  
D. `Python thon`

**56.** What happens?

```python
word = "cat"
word[0] = "b"
```

A. `word` becomes `"bat"`  
B. `word` becomes `["b", "a", "t"]`  
C. A `TypeError` is raised because strings are immutable.  
D. A `ValueError` is raised because `b` is not in the string.

**57.** What is the value of `"th" in "Python"`?

A. `True`  
B. `False`  
C. `2`  
D. `TypeError`

**58.** What does this expression produce?

```python
"-".join(["a", "b", "c"])
```

A. `"abc"`  
B. `"a-b-c"`  
C. `["a-b-c"]`  
D. `"-abc"`

**59.** What is returned by `"a,b,c".split(",")`?

A. `("a", "b", "c")`  
B. `["a", "b", "c"]`  
C. `"abc"`  
D. A generator

**60.** Which TWO statements are correct? *(Select two.)*

A. `"python".find("z")` returns `-1`.  
B. `"python".index("z")` returns `-1`.  
C. `"python".index("z")` raises `ValueError`.  
D. `sorted("cab")` returns the string `"abc"`.

### Section 4 — Object-Oriented Programming (12)

**61.** What does `"Python"[-1]` return?

A. `n`
B. `P`
C. An empty string
D. An `IndexError`

**62.** What is `"Python"[1:4]`?

A. `Pyth`
B. `ytho`
C. The original string
D. `yth`

**63.** What happens when code assigns to `text[0]` for a string `text`?

A. A new list is created
B. The assignment is ignored
C. A `TypeError` is raised because strings are immutable
D. The first character changes

**64.** What does `"Python".find("zz")` return when `zz` is absent?

A. It raises `ValueError`
B. -1
C. 0
D. `None`

**65.** What does `"a,b,c".split(",")` return?

A. `["a", "b", "c"]`
B. `"abc"`
C. `("a", "b", "c")`
D. `["a,b,c"]`

**66.** What does `"-".join(["red", "blue"])` return?

A. `"-red-blue-"`
B. `["red", "blue"]`
C. `"redblue"`
D. `"red-blue"`

**67.** What does `ord("A")` return?

A. The character after `A`
B. A UTF-8 byte sequence
C. The integer Unicode code point for `A`
D. The string `"65"`

**68.** What does `chr(65)` return?

A. `None`
B. The one-character string `"A"`
C. The integer 65
D. The bytes object `b"A"`

**69.** Is `"th" in "Python"` true?

A. True
B. `None`
C. A `TypeError`
D. An integer count

**70.** What does `"coding"[-1]` return?

A. `c`
B. An empty string
C. An `IndexError`
D. `g`

**71.** What is `"coding"[1:4]`?

A. `odin`
B. The original string
C. `odi`
D. `codi`

**72.** What happens when code assigns to `text[0]` for a string `text`?

A. The assignment is ignored
B. A `TypeError` is raised because strings are immutable
C. The first character changes
D. A new list is created

**73.** What does `"coding".find("zz")` return when `zz` is absent?

A. -1
B. 0
C. `None`
D. It raises `ValueError`

**74.** What does `"a,b,c".split(",")` return?

A. `"abc"`
B. `("a", "b", "c")`
C. `["a,b,c"]`
D. `["a", "b", "c"]`

**75.** What does `"-".join(["red", "blue"])` return?

A. `["red", "blue"]`
B. `"redblue"`
C. `"red-blue"`
D. `"-red-blue-"`

**76.** What does `ord("A")` return?

A. A UTF-8 byte sequence
B. The integer Unicode code point for `A`
C. The string `"65"`
D. The character after `A`

**77.** What does `chr(65)` return?

A. The one-character string `"A"`
B. The integer 65
C. The bytes object `b"A"`
D. `None`

**78.** Is `"th" in "coding"` true?

A. `None`
B. A `TypeError`
C. An integer count
D. False

**79.** What does `"module"[-1]` return?

A. An empty string
B. An `IndexError`
C. `e`
D. `m`

**80.** What is `"module"[1:4]`?

A. The original string
B. `odu`
C. `modu`
D. `odul`

**81.** What happens when code assigns to `text[0]` for a string `text`?

A. A `TypeError` is raised because strings are immutable
B. The first character changes
C. A new list is created
D. The assignment is ignored

**82.** What does `"module".find("zz")` return when `zz` is absent?

A. 0
B. `None`
C. It raises `ValueError`
D. -1

**83.** What does `"a,b,c".split(",")` return?

A. `("a", "b", "c")`
B. `["a,b,c"]`
C. `["a", "b", "c"]`
D. `"abc"`

**84.** What does `"-".join(["red", "blue"])` return?

A. `"redblue"`
B. `"red-blue"`
C. `"-red-blue-"`
D. `["red", "blue"]`

**85.** What does `ord("A")` return?

A. The integer Unicode code point for `A`
B. The string `"65"`
C. The character after `A`
D. A UTF-8 byte sequence

**86.** What does `chr(65)` return?

A. The integer 65
B. The bytes object `b"A"`
C. `None`
D. The one-character string `"A"`

**87.** Is `"th" in "module"` true?

A. A `TypeError`
B. An integer count
C. False
D. `None`

**88.** What does `"string"[-1]` return?

A. An `IndexError`
B. `g`
C. `s`
D. An empty string

### Section Object-Oriented Programming (68)

**89.** In OOP, what is an object created from a class?

A. An instance  
B. A module  
C. A superclass  
D. A namespace path

**90.** What is printed?

```python
class Item:
    count = 0

first = Item()
second = Item()
first.count = 3
print(first.count, second.count, Item.count)
```

A. `3 3 3`  
B. `3 0 0`  
C. `0 0 3`  
D. `3 0 3`

**91.** What does the first parameter of an ordinary instance method normally receive when called as `obj.show()`?

A. The class name as a string  
B. The instance `obj`  
C. The first explicit argument after `self`  
D. `None`

**92.** What is printed?

```python
class Box:
    def __init__(self, size):
        self.size = size

b = Box(8)
print(b.size)
```

A. `self`  
B. `size`  
C. `8`  
D. `None`

**93.** What is normally true about `obj.__dict__` for a plain user-defined class without slots?

A. It maps the instance's attributes to their values.  
B. It contains every attribute inherited from every base class.  
C. It is always identical to `Class.__dict__`.  
D. It contains only methods.

**94.** Inside class `Account`, the attribute is assigned as `self.__pin = 1234`. Which name is typically used by Python's name-mangling convention?

A. `__pin`  
B. `_Account__pin`  
C. `Account__pin_`  
D. `pin`

**95.** What does `hasattr(obj, "name")` test?

A. Whether `obj` has an attribute named `name`  
B. Whether the string `name` is in `obj`  
C. Whether `obj.name` is a method  
D. Whether `name` is a class

**96.** Which class attribute gives the class's name as a string?

A. `__bases__`  
B. `__module__`  
C. `__name__`  
D. `__dict__name__`

**97.** What is printed?

```python
class A:
    def label(self):
        return "A"

class B(A):
    pass

print(B().label())
```

A. `A`  
B. `B`  
C. `None`  
D. `AttributeError`

**98.** What is printed?

```python
class A:
    def label(self):
        return "A"

class B(A):
    def label(self):
        return "B"

print(B().label())
```

A. `A`  
B. `B`  
C. `AB`  
D. `AttributeError`

**99.** Given:

```python
class A:
    pass

class B(A):
    pass

obj = B()
```

Which TWO expressions evaluate to `True`? *(Select two.)*

A. `isinstance(obj, A)`  
B. `isinstance(obj, B)`  
C. `type(obj) is A`  
D. `A is B`

**100.** What is printed?

```python
class Person:
    def __str__(self):
        return "Ada"

print(Person())
```

A. `Person`  
B. `Ada`  
C. `__str__`  
D. `None`

### Section 5 — Miscellaneous (9)

**101.** An object created from class `Device` is best described as what?

A. An instance of the class
B. A package
C. A module-level variable
D. A superclass

**102.** When `obj.show()` calls an ordinary instance method, what is passed as its first argument?

A. The class name as a string
B. The method return value
C. No argument
D. The instance `obj`

**103.** Which method is automatically called when `Device()` constructs an instance to initialize it?

A. `__name__`
B. `__bases__`
C. `__init__`
D. `__str__`

**104.** Where is a normal instance attribute such as `self.value` stored?

A. In the function’s local variables forever
B. In that instance’s attribute namespace
C. Only in the base class
D. In `sys.path`

**105.** What is the usual effect of defining an attribute as `self.__value` inside class `Box`?

A. Its name is mangled to include the class name
B. It becomes a true inaccessible private field
C. It is converted into a class variable
D. It is deleted after `__init__`

**106.** A subclass defines a method with the same name as a superclass method. Which implementation is normally selected on a subclass instance?

A. The superclass implementation always
B. Both implementations are skipped
C. Python reports an error at class definition
D. The subclass implementation

**107.** What does `isinstance(child, Parent)` return when `Child` inherits from `Parent`?

A. The class name `"Parent"`
B. A `TypeError`
C. `True`
D. `False`

**108.** What does `hasattr(obj, "name")` check?

A. Whether `name` appears in `sys.path`
B. Whether `obj` provides an attribute named `name`
C. Whether `name` is a local variable
D. Whether `obj` is callable

**109.** For a class `Device`, what does `Device.__name__` usually contain?

A. `"Device"`
B. The class’s base classes
C. The module search path
D. The instance dictionary

**110.** What does an object’s `__dict__` normally expose for a regular user-defined class?

A. All methods of every superclass
B. The source file as bytes
C. The object’s method call history
D. A mapping of the object’s stored attributes

**111.** If `self.count` is assigned on one instance, what happens to another instance’s `count`?

A. The class is automatically renamed
B. The assignment raises `AttributeError`
C. It is unaffected unless it has its own update
D. It is always changed too

**112.** What does `super()` commonly help a subclass method do?

A. Skip the parent class permanently
B. Call the next implementation in the method resolution order
C. Create a new superclass
D. Make all attributes private

**113.** What does a class’s `__bases__` attribute contain?

A. A tuple of its direct base classes
B. Its instances
C. Its source-code lines
D. Its class variables only

**114.** If a class does not define `__str__`, what does `str(instance)` use?

A. The class’s `__init__` return value
B. The value of `self.__dict__` as a list
C. An empty string
D. The inherited default object representation

**115.** An object created from class `Account` is best described as what?

A. A module-level variable
B. A superclass
C. An instance of the class
D. A package

**116.** When `obj.show()` calls an ordinary instance method, what is passed as its first argument?

A. No argument
B. The instance `obj`
C. The class name as a string
D. The method return value

**117.** Which method is automatically called when `Account()` constructs an instance to initialize it?

A. `__init__`
B. `__str__`
C. `__name__`
D. `__bases__`

**118.** Where is a normal instance attribute such as `self.value` stored?

A. Only in the base class
B. In `sys.path`
C. In the function’s local variables forever
D. In that instance’s attribute namespace

**119.** What is the usual effect of defining an attribute as `self.__value` inside class `Box`?

A. It is converted into a class variable
B. It is deleted after `__init__`
C. Its name is mangled to include the class name
D. It becomes a true inaccessible private field

**120.** A subclass defines a method with the same name as a superclass method. Which implementation is normally selected on a subclass instance?

A. Python reports an error at class definition
B. The subclass implementation
C. The superclass implementation always
D. Both implementations are skipped

**121.** What does `isinstance(child, Parent)` return when `Child` inherits from `Parent`?

A. `True`
B. `False`
C. The class name `"Parent"`
D. A `TypeError`

**122.** What does `hasattr(obj, "name")` check?

A. Whether `name` is a local variable
B. Whether `obj` is callable
C. Whether `name` appears in `sys.path`
D. Whether `obj` provides an attribute named `name`

**123.** For a class `Account`, what does `Account.__name__` usually contain?

A. The module search path
B. The instance dictionary
C. `"Account"`
D. The class’s base classes

**124.** What does an object’s `__dict__` normally expose for a regular user-defined class?

A. The object’s method call history
B. A mapping of the object’s stored attributes
C. All methods of every superclass
D. The source file as bytes

**125.** If `self.count` is assigned on one instance, what happens to another instance’s `count`?

A. It is unaffected unless it has its own update
B. It is always changed too
C. The class is automatically renamed
D. The assignment raises `AttributeError`

**126.** What does `super()` commonly help a subclass method do?

A. Create a new superclass
B. Make all attributes private
C. Skip the parent class permanently
D. Call the next implementation in the method resolution order

**127.** What does a class’s `__bases__` attribute contain?

A. Its source-code lines
B. Its class variables only
C. A tuple of its direct base classes
D. Its instances

**128.** If a class does not define `__str__`, what does `str(instance)` use?

A. An empty string
B. The inherited default object representation
C. The class’s `__init__` return value
D. The value of `self.__dict__` as a list

**129.** An object created from class `Vehicle` is best described as what?

A. An instance of the class
B. A package
C. A module-level variable
D. A superclass

**130.** When `obj.show()` calls an ordinary instance method, what is passed as its first argument?

A. The class name as a string
B. The method return value
C. No argument
D. The instance `obj`

**131.** Which method is automatically called when `Vehicle()` constructs an instance to initialize it?

A. `__name__`
B. `__bases__`
C. `__init__`
D. `__str__`

**132.** Where is a normal instance attribute such as `self.value` stored?

A. In the function’s local variables forever
B. In that instance’s attribute namespace
C. Only in the base class
D. In `sys.path`

**133.** What is the usual effect of defining an attribute as `self.__value` inside class `Box`?

A. Its name is mangled to include the class name
B. It becomes a true inaccessible private field
C. It is converted into a class variable
D. It is deleted after `__init__`

**134.** A subclass defines a method with the same name as a superclass method. Which implementation is normally selected on a subclass instance?

A. The superclass implementation always
B. Both implementations are skipped
C. Python reports an error at class definition
D. The subclass implementation

**135.** What does `isinstance(child, Parent)` return when `Child` inherits from `Parent`?

A. The class name `"Parent"`
B. A `TypeError`
C. `True`
D. `False`

**136.** What does `hasattr(obj, "name")` check?

A. Whether `name` appears in `sys.path`
B. Whether `obj` provides an attribute named `name`
C. Whether `name` is a local variable
D. Whether `obj` is callable

**137.** For a class `Vehicle`, what does `Vehicle.__name__` usually contain?

A. `"Vehicle"`
B. The class’s base classes
C. The module search path
D. The instance dictionary

**138.** What does an object’s `__dict__` normally expose for a regular user-defined class?

A. All methods of every superclass
B. The source file as bytes
C. The object’s method call history
D. A mapping of the object’s stored attributes

**139.** If `self.count` is assigned on one instance, what happens to another instance’s `count`?

A. The class is automatically renamed
B. The assignment raises `AttributeError`
C. It is unaffected unless it has its own update
D. It is always changed too

**140.** What does `super()` commonly help a subclass method do?

A. Skip the parent class permanently
B. Call the next implementation in the method resolution order
C. Create a new superclass
D. Make all attributes private

**141.** What does a class’s `__bases__` attribute contain?

A. A tuple of its direct base classes
B. Its instances
C. Its source-code lines
D. Its class variables only

**142.** If a class does not define `__str__`, what does `str(instance)` use?

A. The class’s `__init__` return value
B. The value of `self.__dict__` as a list
C. An empty string
D. The inherited default object representation

**143.** An object created from class `Widget` is best described as what?

A. A module-level variable
B. A superclass
C. An instance of the class
D. A package

**144.** When `obj.show()` calls an ordinary instance method, what is passed as its first argument?

A. No argument
B. The instance `obj`
C. The class name as a string
D. The method return value

**145.** Which method is automatically called when `Widget()` constructs an instance to initialize it?

A. `__init__`
B. `__str__`
C. `__name__`
D. `__bases__`

**146.** Where is a normal instance attribute such as `self.value` stored?

A. Only in the base class
B. In `sys.path`
C. In the function’s local variables forever
D. In that instance’s attribute namespace

**147.** What is the usual effect of defining an attribute as `self.__value` inside class `Box`?

A. It is converted into a class variable
B. It is deleted after `__init__`
C. Its name is mangled to include the class name
D. It becomes a true inaccessible private field

**148.** A subclass defines a method with the same name as a superclass method. Which implementation is normally selected on a subclass instance?

A. Python reports an error at class definition
B. The subclass implementation
C. The superclass implementation always
D. Both implementations are skipped

**149.** What does `isinstance(child, Parent)` return when `Child` inherits from `Parent`?

A. `True`
B. `False`
C. The class name `"Parent"`
D. A `TypeError`

**150.** What does `hasattr(obj, "name")` check?

A. Whether `name` is a local variable
B. Whether `obj` is callable
C. Whether `name` appears in `sys.path`
D. Whether `obj` provides an attribute named `name`

**151.** For a class `Widget`, what does `Widget.__name__` usually contain?

A. The module search path
B. The instance dictionary
C. `"Widget"`
D. The class’s base classes

**152.** What does an object’s `__dict__` normally expose for a regular user-defined class?

A. The object’s method call history
B. A mapping of the object’s stored attributes
C. All methods of every superclass
D. The source file as bytes

**153.** If `self.count` is assigned on one instance, what happens to another instance’s `count`?

A. It is unaffected unless it has its own update
B. It is always changed too
C. The class is automatically renamed
D. The assignment raises `AttributeError`

**154.** What does `super()` commonly help a subclass method do?

A. Create a new superclass
B. Make all attributes private
C. Skip the parent class permanently
D. Call the next implementation in the method resolution order

**155.** What does a class’s `__bases__` attribute contain?

A. Its source-code lines
B. Its class variables only
C. A tuple of its direct base classes
D. Its instances

**156.** If a class does not define `__str__`, what does `str(instance)` use?

A. An empty string
B. The inherited default object representation
C. The class’s `__init__` return value
D. The value of `self.__dict__` as a list

### Section Miscellaneous (List Comprehensions, Lambdas, Closures, I/O) (44)

**157.** What is printed?

```python
values = [n * 3 for n in range(4)]
print(values)
```

A. `[0, 1, 2, 3]`  
B. `[0, 3, 6, 9]`  
C. `[3, 6, 9, 12]`  
D. `[0, 4, 8, 12]`

**158.** What is printed?

```python
evens = [n for n in range(7) if n % 2 == 0]
print(evens)
```

A. `[0, 2, 4, 6]`  
B. `[1, 3, 5]`  
C. `[2, 4, 6]`  
D. `[0, 1, 2, 3, 4, 5, 6]`

**159.** Which value does this lambda return for `f(4, 5)`?

```python
f = lambda x, y: x * y
```

A. `9`  
B. `20`  
C. `(4, 5)`  
D. A function object

**160.** What does `list(map(lambda x: x + 1, [1, 2, 3]))` return?

A. `[1, 2, 3]`  
B. `[2, 3, 4]`  
C. `[True, True, True]`  
D. A single integer `9`

**161.** What does `list(filter(lambda x: x > 2, [1, 2, 3, 4]))` return?

A. `[1, 2]`  
B. `[3, 4]`  
C. `[False, False, True, True]`  
D. `[2, 3, 4]`

**162.** What is printed?

```python
def make_power(exponent):
    def power(value):
        return value ** exponent
    return power

square = make_power(2)
print(square(5))
```

A. `7`  
B. `10`  
C. `25`  
D. `None`

**163.** What type of value does reading a file opened in text mode normally return?

A. `bytes`  
B. `str`  
C. `bytearray`  
D. An integer file descriptor

**164.** What type of value does `f.read()` normally return when `f` is a binary-mode file object?

A. `str`  
B. `bytes`  
C. `list`  
D. `None`

**165.** Which TWO statements are true? *(Select two.)*

A. `bytearray` is mutable.  
B. `bytes` supports item assignment.  
C. `with open(path) as f:` arranges for the file to be closed when the block exits.  
D. `readline()` always reads every line into a list.

---

**166.** What is `[x * 2 for x in range(3)]`?

A. [0, 2, 4]
B. [2, 4, 6]
C. `range(3)`
D. An empty list

**167.** In `[x for x in range(6) if x % 2 == 0]`, which values are kept?

A. The odd values from 1 through 5
B. All values including 6
C. Only 6
D. The even values from 0 through 4

**168.** What does `(lambda x: x + 2)(3)` return?

A. 2
B. A function object
C. 5
D. 6

**169.** What does `list(map(lambda x: x + 1, [1, 2]))` return?

A. A map object even after `list()`
B. `[2, 3]`
C. `[1, 2]`
D. `[1, 1]`

**170.** What does `list(filter(lambda x: x > 1, [0, 1, 2, 3]))` return?

A. `[2, 3]`
B. `[0, 1]`
C. `[True, True]`
D. `[0, 1, 2, 3]`

**171.** What type does `f.read()` normally return when `f` is opened in text mode?

A. `bytes`
B. `bytearray`
C. A list of characters
D. `str`

**172.** What type does `f.read()` normally return when `f` is opened in binary mode?

A. `list`
B. `None`
C. `bytes`
D. `str`

**173.** What does a `with open(path) as f:` block arrange to do when the block exits?

A. Convert its content to bytes
B. Close the file object
C. Delete the file
D. Rewind the file to the beginning

**174.** Which statement about `bytearray` is correct?

A. It is mutable
B. It is immutable like `bytes`
C. It stores only Unicode text
D. It cannot be indexed

**175.** What is `[x * 3 for x in range(3)]`?

A. [3, 6, 9]
B. `range(3)`
C. An empty list
D. [0, 3, 6]

**176.** In `[x for x in range(6) if x % 2 == 0]`, which values are kept?

A. All values including 6
B. Only 6
C. The even values from 0 through 4
D. The odd values from 1 through 5

**177.** What does `(lambda x: x + 3)(3)` return?

A. A function object
B. 6
C. 9
D. 3

**178.** What does `list(map(lambda x: x + 1, [1, 2]))` return?

A. `[2, 3]`
B. `[1, 2]`
C. `[1, 1]`
D. A map object even after `list()`

**179.** What does `list(filter(lambda x: x > 1, [0, 1, 2, 3]))` return?

A. `[0, 1]`
B. `[True, True]`
C. `[0, 1, 2, 3]`
D. `[2, 3]`

**180.** What type does `f.read()` normally return when `f` is opened in text mode?

A. `bytearray`
B. A list of characters
C. `str`
D. `bytes`

**181.** What type does `f.read()` normally return when `f` is opened in binary mode?

A. `None`
B. `bytes`
C. `str`
D. `list`

**182.** What does a `with open(path) as f:` block arrange to do when the block exits?

A. Close the file object
B. Delete the file
C. Rewind the file to the beginning
D. Convert its content to bytes

**183.** Which statement about `bytearray` is correct?

A. It is immutable like `bytes`
B. It stores only Unicode text
C. It cannot be indexed
D. It is mutable

**184.** What is `[x * 4 for x in range(3)]`?

A. `range(3)`
B. An empty list
C. [0, 4, 8]
D. [4, 8, 12]

**185.** In `[x for x in range(6) if x % 2 == 0]`, which values are kept?

A. Only 6
B. The even values from 0 through 4
C. The odd values from 1 through 5
D. All values including 6

**186.** What does `(lambda x: x + 4)(3)` return?

A. 7
B. 12
C. 4
D. A function object

**187.** What does `list(map(lambda x: x + 1, [1, 2]))` return?

A. `[1, 2]`
B. `[1, 1]`
C. A map object even after `list()`
D. `[2, 3]`

**188.** What does `list(filter(lambda x: x > 1, [0, 1, 2, 3]))` return?

A. `[True, True]`
B. `[0, 1, 2, 3]`
C. `[2, 3]`
D. `[0, 1]`

**189.** What type does `f.read()` normally return when `f` is opened in text mode?

A. A list of characters
B. `str`
C. `bytes`
D. `bytearray`

**190.** What type does `f.read()` normally return when `f` is opened in binary mode?

A. `bytes`
B. `str`
C. `list`
D. `None`

**191.** What does a `with open(path) as f:` block arrange to do when the block exits?

A. Delete the file
B. Rewind the file to the beginning
C. Convert its content to bytes
D. Close the file object

**192.** Which statement about `bytearray` is correct?

A. It stores only Unicode text
B. It cannot be indexed
C. It is mutable
D. It is immutable like `bytes`

**193.** What is `[x * 5 for x in range(3)]`?

A. An empty list
B. [0, 5, 10]
C. [5, 10, 15]
D. `range(3)`

**194.** In `[x for x in range(6) if x % 2 == 0]`, which values are kept?

A. The even values from 0 through 4
B. The odd values from 1 through 5
C. All values including 6
D. Only 6

**195.** What does `(lambda x: x + 5)(3)` return?

A. 15
B. 5
C. A function object
D. 8

**196.** What does `list(map(lambda x: x + 1, [1, 2]))` return?

A. `[1, 1]`
B. A map object even after `list()`
C. `[2, 3]`
D. `[1, 2]`

**197.** What does `list(filter(lambda x: x > 1, [0, 1, 2, 3]))` return?

A. `[0, 1, 2, 3]`
B. `[2, 3]`
C. `[0, 1]`
D. `[True, True]`

**198.** What type does `f.read()` normally return when `f` is opened in text mode?

A. `str`
B. `bytes`
C. `bytearray`
D. A list of characters

**199.** What type does `f.read()` normally return when `f` is opened in binary mode?

A. `str`
B. `list`
C. `None`
D. `bytes`

**200.** What does a `with open(path) as f:` block arrange to do when the block exits?

A. Rewind the file to the beginning
B. Convert its content to bytes
C. Close the file object
D. Delete the file

## Answer Key

1. **B** — The alias `m` is the bound module name.
2. **C** — The imported function is bound under alias `root`.
3. **A** — `dir` lists names available on its argument.
4. **B** — `sys.path` contains module/package search locations.
5. **B** — Imported module name is `helper`; `main.py` is the directly executed program.
6. **A, C** — `sample` selects without replacement; reseeding reproduces a sequence. `random()` is below 1.0.
7. **A** — The module is available through its import alias.
8. **D** — The imported function is bound to the name `down`.
9. **C** — `sys.path` lists module search locations.
10. **B** — `dir` reports names available on its argument.
11. **A** — An imported module receives its module name; `__main__` names the executed entry point.
12. **D** — `sample` selects a sample without replacement.
13. **C** — `ceil` returns the smallest integer greater than or equal to the input.
14. **B** — The module is available through its import alias.
15. **A** — The imported function is bound to the name `down`.
16. **D** — `sys.path` lists module search locations.
17. **C** — `dir` reports names available on its argument.
18. **B** — An imported module receives its module name; `__main__` names the executed entry point.
19. **A** — `sample` selects a sample without replacement.
20. **D** — `ceil` returns the smallest integer greater than or equal to the input.
21. **C** — The module is available through its import alias.
22. **B** — The imported function is bound to the name `down`.
23. **A** — `sys.path` lists module search locations.
24. **D** — `dir` reports names available on its argument.
25. **B** — `ValueError` is caught; `finally` runs.
26. **B** — Put specific handlers before broad handlers.
27. **B** — Bare `raise` re-raises the active exception.
28. **B** — A false assertion raises `AssertionError` with the supplied message.
29. **A** — Custom exceptions normally subclass `Exception`.
30. **A** — A broad handler first would catch the specific exception.
31. **D** — `finally` runs as cleanup after the try handling.
32. **C** — Bare `raise` propagates the active exception.
33. **B** — Custom exceptions are classes, usually derived from `Exception`.
34. **A** — The argument has the right type but an invalid integer value.
35. **D** — A failed assertion raises `AssertionError`.
36. **C** — A tuple of exception classes can be given to one `except` clause.
37. **B** — Unhandled exceptions propagate up the call stack.
38. **A** — A broad handler first would catch the specific exception.
39. **D** — `finally` runs as cleanup after the try handling.
40. **C** — Bare `raise` propagates the active exception.
41. **B** — Custom exceptions are classes, usually derived from `Exception`.
42. **A** — The argument has the right type but an invalid integer value.
43. **D** — A failed assertion raises `AssertionError`.
44. **C** — A tuple of exception classes can be given to one `except` clause.
45. **B** — Unhandled exceptions propagate up the call stack.
46. **A** — A broad handler first would catch the specific exception.
47. **D** — `finally` runs as cleanup after the try handling.
48. **C** — Bare `raise` propagates the active exception.
49. **B** — Custom exceptions are classes, usually derived from `Exception`.
50. **A** — The argument has the right type but an invalid integer value.
51. **D** — A failed assertion raises `AssertionError`.
52. **C** — A tuple of exception classes can be given to one `except` clause.
53. **B** — `ord` returns the integer code point.
54. **B** — `chr` returns a one-character string.
55. **B** — `s[-1]` is `n`; stop index 4 is excluded.
56. **C** — Strings cannot be changed by indexed assignment.
57. **A** — `th` occurs in `Python`.
58. **B** — The separator joins the strings.
59. **B** — `split` returns a list of pieces.
60. **A, C** — `find` returns `-1`; `index` raises `ValueError` when absent.
61. **A** — Index `-1` selects the last character.
62. **D** — The start is included and the stop index is excluded.
63. **C** — Strings do not support item assignment.
64. **B** — `find` returns `-1` if the substring is not found.
65. **A** — `split` returns a list of substrings.
66. **D** — `join` inserts its string between iterable elements.
67. **C** — `ord` maps a one-character string to its code point.
68. **B** — `chr` maps an integer code point to a one-character string.
69. **A** — The `in` operator tests whether the substring occurs.
70. **D** — Index `-1` selects the last character.
71. **C** — The start is included and the stop index is excluded.
72. **B** — Strings do not support item assignment.
73. **A** — `find` returns `-1` if the substring is not found.
74. **D** — `split` returns a list of substrings.
75. **C** — `join` inserts its string between iterable elements.
76. **B** — `ord` maps a one-character string to its code point.
77. **A** — `chr` maps an integer code point to a one-character string.
78. **D** — The `in` operator tests whether the substring occurs.
79. **C** — Index `-1` selects the last character.
80. **B** — The start is included and the stop index is excluded.
81. **A** — Strings do not support item assignment.
82. **D** — `find` returns `-1` if the substring is not found.
83. **C** — `split` returns a list of substrings.
84. **B** — `join` inserts its string between iterable elements.
85. **A** — `ord` maps a one-character string to its code point.
86. **D** — `chr` maps an integer code point to a one-character string.
87. **C** — The `in` operator tests whether the substring occurs.
88. **B** — Index `-1` selects the last character.
89. **A** — An object is an instance of its class.
90. **B** — `first.count = 3` creates an instance attribute; the class value remains 0.
91. **B** — The bound instance is passed as the first method argument.
92. **C** — `__init__` stores the supplied value on the instance.
93. **A** — For this ordinary class, the instance dictionary holds its own attributes.
94. **B** — Double-leading-underscore names are class-name-mangled.
95. **A** — It checks whether the named attribute can be found on the object.
96. **C** — `__name__` is the class's name.
97. **A** — `B` inherits `label` from `A`.
98. **B** — The subclass override is selected.
99. **A, B** — A `B` instance is also an instance of its superclass `A`.
100. **B** — `print` uses the object's `__str__` result.
101. **A** — An object is an instance created from a class.
102. **D** — Python binds the instance to the method’s first parameter, conventionally `self`.
103. **C** — `__init__` initializes the newly created instance.
104. **B** — Instance attributes belong to an object.
105. **A** — Double-leading-underscore names undergo name mangling.
106. **D** — The subclass method overrides the inherited method.
107. **C** — Instances of a subclass are also instances of its base class.
108. **B** — `hasattr` checks for an attribute on the object.
109. **A** — `__name__` stores the class name.
110. **D** — An instance dictionary maps attribute names to values.
111. **C** — Assigning through `self` creates or updates that instance attribute.
112. **B** — `super()` delegates to the next class in the MRO.
113. **A** — `__bases__` lists the direct base classes.
114. **D** — The default `object.__str__` provides a representation unless overridden.
115. **C** — An object is an instance created from a class.
116. **B** — Python binds the instance to the method’s first parameter, conventionally `self`.
117. **A** — `__init__` initializes the newly created instance.
118. **D** — Instance attributes belong to an object.
119. **C** — Double-leading-underscore names undergo name mangling.
120. **B** — The subclass method overrides the inherited method.
121. **A** — Instances of a subclass are also instances of its base class.
122. **D** — `hasattr` checks for an attribute on the object.
123. **C** — `__name__` stores the class name.
124. **B** — An instance dictionary maps attribute names to values.
125. **A** — Assigning through `self` creates or updates that instance attribute.
126. **D** — `super()` delegates to the next class in the MRO.
127. **C** — `__bases__` lists the direct base classes.
128. **B** — The default `object.__str__` provides a representation unless overridden.
129. **A** — An object is an instance created from a class.
130. **D** — Python binds the instance to the method’s first parameter, conventionally `self`.
131. **C** — `__init__` initializes the newly created instance.
132. **B** — Instance attributes belong to an object.
133. **A** — Double-leading-underscore names undergo name mangling.
134. **D** — The subclass method overrides the inherited method.
135. **C** — Instances of a subclass are also instances of its base class.
136. **B** — `hasattr` checks for an attribute on the object.
137. **A** — `__name__` stores the class name.
138. **D** — An instance dictionary maps attribute names to values.
139. **C** — Assigning through `self` creates or updates that instance attribute.
140. **B** — `super()` delegates to the next class in the MRO.
141. **A** — `__bases__` lists the direct base classes.
142. **D** — The default `object.__str__` provides a representation unless overridden.
143. **C** — An object is an instance created from a class.
144. **B** — Python binds the instance to the method’s first parameter, conventionally `self`.
145. **A** — `__init__` initializes the newly created instance.
146. **D** — Instance attributes belong to an object.
147. **C** — Double-leading-underscore names undergo name mangling.
148. **B** — The subclass method overrides the inherited method.
149. **A** — Instances of a subclass are also instances of its base class.
150. **D** — `hasattr` checks for an attribute on the object.
151. **C** — `__name__` stores the class name.
152. **B** — An instance dictionary maps attribute names to values.
153. **A** — Assigning through `self` creates or updates that instance attribute.
154. **D** — `super()` delegates to the next class in the MRO.
155. **C** — `__bases__` lists the direct base classes.
156. **B** — The default `object.__str__` provides a representation unless overridden.
157. **B** — Multiply each value in `range(4)` by 3.
158. **A** — The condition keeps even values, including zero.
159. **B** — The lambda multiplies its arguments.
160. **B** — `map` applies `x + 1` to each value.
161. **B** — `filter` retains values for which the condition is true.
162. **C** — The closure retains `exponent == 2`; `5 ** 2 == 25`.
163. **B** — Text-mode reads return `str`.
164. **B** — Binary-mode reads return `bytes`.
165. **A, C** — `bytearray` is mutable; a context manager closes the file on exit.
166. **A** — The comprehension multiplies 0, 1 and 2 by the factor.
167. **D** — The filter condition retains even values; `range(6)` stops before 6.
168. **C** — The lambda is called with 3 and returns 3 plus the captured constant.
169. **B** — `map` applies the lambda to each element.
170. **A** — `filter` retains elements for which the predicate is true.
171. **D** — Text mode decodes file content to strings.
172. **C** — Binary mode returns bytes.
173. **B** — The context manager closes the file when the block exits.
174. **A** — `bytearray` is a mutable sequence of byte values.
175. **D** — The comprehension multiplies 0, 1 and 2 by the factor.
176. **C** — The filter condition retains even values; `range(6)` stops before 6.
177. **B** — The lambda is called with 3 and returns 3 plus the captured constant.
178. **A** — `map` applies the lambda to each element.
179. **D** — `filter` retains elements for which the predicate is true.
180. **C** — Text mode decodes file content to strings.
181. **B** — Binary mode returns bytes.
182. **A** — The context manager closes the file when the block exits.
183. **D** — `bytearray` is a mutable sequence of byte values.
184. **C** — The comprehension multiplies 0, 1 and 2 by the factor.
185. **B** — The filter condition retains even values; `range(6)` stops before 6.
186. **A** — The lambda is called with 3 and returns 3 plus the captured constant.
187. **D** — `map` applies the lambda to each element.
188. **C** — `filter` retains elements for which the predicate is true.
189. **B** — Text mode decodes file content to strings.
190. **A** — Binary mode returns bytes.
191. **D** — The context manager closes the file when the block exits.
192. **C** — `bytearray` is a mutable sequence of byte values.
193. **B** — The comprehension multiplies 0, 1 and 2 by the factor.
194. **A** — The filter condition retains even values; `range(6)` stops before 6.
195. **D** — The lambda is called with 3 and returns 3 plus the captured constant.
196. **C** — `map` applies the lambda to each element.
197. **B** — `filter` retains elements for which the predicate is true.
198. **A** — Text mode decodes file content to strings.
199. **D** — Binary mode returns bytes.
200. **C** — The context manager closes the file when the block exits.

**Source:** Python Institute, [PCAP-31-03 Exam Syllabus](https://pythoninstitute.org/certification/pcap-certification-associate/pcap-exam-syllabus). Original 40-question source file is retained locally and excluded from Git.
