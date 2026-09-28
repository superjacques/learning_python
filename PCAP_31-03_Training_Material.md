# PCAP-31-03 Training Material

A short, mastery-gated course for the Python Institute PCAP-31-03 exam. It follows the official five exam sections and uses the supplied **Python_Advanced.pptx** as the teaching source. The exam mock is weighted to the official distribution: 6 / 5 / 8 / 12 / 9 questions across the five sections.

## How to use this file

Work with `PCAP_ChatGPT_instructions.md` and `PCAP_31-03_Mock_exam.md`. ChatGPT should teach only one small block, ask the learner to predict or answer, then wait. It should repair gaps with fresh, focused questions before advancing. A calendar schedule never advances the learner.

Prefer the learner's existing files, especially `main.py`, `helper.py`, and `mymodule.py`. Keep exercises short. Predict before running where practical. Never treat a lucky guess as proof of understanding.

## Course map

| Course section | Official PCAP section | Blocks |
|---|---|---|
| 1. Modules, packages, and standard library | 1 — 12% | Imports and namespaces; `dir()` / `sys.path`; `math`; `random`; `platform`; user modules and `__name__`; packages and nested imports |
| 2. Exceptions | 2 — 14% | Exception hierarchy and matching; `try` / `except` / `else` / `finally`; `raise`, `assert`, `args`; custom exceptions |
| 3. Strings | 3 — 18% | Code points and encodings; indexing, slicing, immutability; operations; methods and search |
| 4. Object-oriented programming | 4 — 34% | Class/object basics; attributes and `__dict__`; methods and `self`; introspection; inheritance, overriding, polymorphism, MRO; construction |
| 5. Miscellaneous | 5 — 22% | List comprehensions; lambda, `map`, `filter`; closures; I/O terms and streams; file operations and `bytearray` |

**Extension topics from the presentation:** `pip`; `os`, `time`, `datetime`, and `calendar`; iterators and generators; extra OOP patterns such as abstract base classes and operator overloading. These are useful enrichment, but do not let them displace the official PCAP objectives. Add them after core mastery or when the learner requests them.

---

# Section 1 — Modules and Packages

## Block 1.1 — Import forms and names

**Tiny theory**

- `import math` binds the name `math`; use `math.sqrt(81)`.
- `from math import sqrt` binds `sqrt`; use `sqrt(81)`.
- `import math as m` binds `m`; use `m.pi`.
- `from math import sqrt as root` binds `root`.
- `from module import *` imports public names into the current namespace and can create name collisions; recognize it, but prefer explicit imports.

**Predict / try**

```python
import math as m
from math import sqrt

print(m.ceil(2.1))
print(sqrt(81))
```

**Cold check**

Ask the learner which names are available after each import form and how each function must be called. Include a small name-collision example.

## Block 1.2 — `dir()` and `sys.path`

**Tiny theory**

- `dir(object)` returns names available on an object; `dir()` with no argument lists names in the current scope.
- `sys.path` is the list of locations Python searches for modules and packages. The current script directory is normally searched.

**Predict / try**

```python
import math
print("sqrt" in dir(math))
```

Then inspect `sys.path` and identify it as a list of search locations, not a list of imported modules.

**Cold check**

Distinguish `dir(math)` from `sys.path`; predict what adding a directory to the search path changes.

## Block 1.3 — `math`

**Tiny theory**

- `ceil(x)` rounds toward positive infinity; `floor(x)` toward negative infinity; `trunc(x)` toward zero.
- `factorial(n)` computes `n!`; `hypot(x, y)` computes the Euclidean hypotenuse; `sqrt(x)` computes a square root.

**Predict / try**

```python
from math import ceil, floor, trunc, factorial, hypot, sqrt

print(ceil(-2.3), floor(-2.3), trunc(-2.3))
print(factorial(0), hypot(3, 4), sqrt(81))
```

**Cold check**

Use negative decimals to separate floor from truncation. Include `factorial(0)` and return types/results.

## Block 1.4 — `random`

**Tiny theory**

- `random()` returns a float with `0.0 <= value < 1.0`.
- `seed(x)` resets the pseudo-random sequence. Calls advance through the sequence; resetting to the same seed reproduces it.
- `choice(seq)` returns one element. `sample(seq, k)` returns a new list of `k` selections without replacement.

**Predict / try**

```python
from random import seed, random, choice, sample

seed(7)
a = random()
seed(7)
b = random()
print(a == b)

items = [10, 20, 30, 40]
print(choice(items))
print(sample(items, 2))
```

**Cold check**

Test range boundaries, result types, uniqueness, and whether consecutive calls after one seed must match.

## Block 1.5 — `platform`

**Tiny theory**

Recognize what these report; the exact result depends on the learner's computer:

- `system()` — operating-system name
- `machine()` — machine architecture
- `processor()` — processor information
- `version()` — OS version details
- `platform()` — combined platform description
- `python_implementation()` — implementation such as CPython
- `python_version_tuple()` — Python version components as strings

**Predict / try**

Import and print two or three functions. Focus on what each asks for, not memorizing the learner's output.

**Cold check**

Match each function to the kind of information it returns.

## Block 1.6 — User-defined modules and `__name__`

Use `main.py` and `helper.py` where possible.

**Tiny theory**

- A module is a Python file that can define reusable functions, classes, and values.
- When a file is run directly, its `__name__` is `"__main__"`; when imported, it is its module name.
- Importing runs top-level statements on the first import in a process. Later imports normally reuse the loaded module.
- `if __name__ == "__main__":` protects code intended only for direct execution.

**Predict / try**

```python
# helper.py
print("helper name:", __name__)

if __name__ == "__main__":
    print("direct run")
```

```python
# main.py
import helper
import helper
print("main name:", __name__)
```

Ask for the predicted output before running. Identify which file is executed.

**Cold check**

Use explicit wording: state whether `main.py` or `helper.py` is executed. Test imported name, direct name, top-level execution, and the direct-run guard.

## Block 1.7 — Bytecode and package basics

**Tiny theory**

- `.py` is readable Python source.
- Python may cache compiled bytecode in `__pycache__` as `.pyc` files. It is generated cache; do not edit it as source.
- A package groups related modules in directories. `__init__.py` is the conventional package initialization file; its code can run when the package is imported. Modern Python also supports namespace packages without it, but the course examples use the conventional form.

**Predict / try**

```text
main.py
shop/
    __init__.py
    prices.py
```

```python
# shop/__init__.py
print("shop initialized")
```

```python
# main.py
import shop
```

Predict the output and what `__pycache__` may contain after imports.

**Cold check**

Identify source vs bytecode, package vs module, and when package initialization code runs.

## Block 1.8 — Nested imports and package search

**Tiny theory**

For `shop/products/prices.py`, the import statement controls the names available:

```python
import shop.products.prices
print(shop.products.prices.vat)

from shop.products import prices
print(prices.vat)

from shop.products.prices import vat
print(vat)
```

Python searches locations in `sys.path`. Directory trees alone do not guarantee that a file is importable; package structure and the search path matter.

**Predict / try**

Use one `prices.py` with `vat = 0.15`. Change only the import line and predict which qualified names work.

**Cold check**

Test nested qualification, names introduced by each import form, and the role of `sys.path`.

**Section exit gate:** a short mixed check spanning all eight blocks, with at least 80% correct and no unresolved high-impact misconception. Repair only missed concepts, then retest with different examples.

---

# Section 2 — Exceptions

## Block 2.1 — Exception types and matching

**Tiny theory**

Exceptions are runtime events represented by objects. Catch the most specific exceptions needed. An earlier broad handler such as `except Exception:` also catches its subclasses, making later narrower handlers unreachable.

Common types: `ValueError`, `TypeError`, `IndexError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`, `ImportError`, `NameError`, `AttributeError`.

**Predict / try**

```python
try:
    int("x")
except ValueError:
    print("value")
except Exception:
    print("other")
```

**Cold check**

Classify short failing expressions and choose the first matching handler. Include `except Exception as err` and `err.args`.

## Block 2.2 — `try`, `except`, `else`, `finally`

**Tiny theory**

- `except` runs when a matching exception is raised in `try`.
- `else` runs only if `try` completes without an exception.
- `finally` runs whether or not an exception occurred, including when it propagates.

**Predict / try**

Trace a success path and a failure path through the same four clauses.

**Cold check**

Ask the learner to state the exact output and whether an exception remains unhandled.

## Block 2.3 — Raise, assert, and exception objects

**Tiny theory**

- `raise ValueError("message")` creates and raises an exception.
- Bare `raise` inside an `except` block re-raises the current exception.
- `raise err` raises the named exception object.
- `assert condition, message` raises `AssertionError` when the condition is false.
- Exception objects expose `.args`.

**Predict / try**

Trace a validation function and a caught/re-raised error.

**Cold check**

Distinguish raising, re-raising, catching, and an assertion failure.

## Block 2.4 — Custom exceptions

**Tiny theory**

Create a custom exception by subclassing `Exception` (or an appropriate existing exception). It can then be raised and caught by its type.

```python
class InvalidAgeError(Exception):
    pass
```

**Cold check**

Identify valid definitions, superclass relationships, and the matching handler.

**Section exit gate:** at least 80% on a new mixed check; repair exceptions by exact misconception before moving on.

---

# Section 3 — Strings

## Block 3.1 — Characters, code points, encodings

**Tiny theory**

Unicode assigns code points to characters; `ord(character)` returns a code point and `chr(integer)` returns the corresponding one-character string. ASCII is a smaller character set; UTF-8 is a common Unicode encoding. Escape sequences represent special characters such as newline (`\n`) and tab (`\t`).

**Cold check**

Match `ord`, `chr`, Unicode, ASCII, UTF-8, and common escapes. Keep code-point identity distinct from encoded bytes.

## Block 3.2 — Indexing, slicing, and immutability

**Tiny theory**

Strings are sequences: index from zero, use negative indices from the end, and slice with an exclusive stop. Strings are immutable; operations produce new strings rather than changing a character in place.

**Predict / try**

```python
s = "Python"
print(s[0], s[-1], s[1:4], s[:2], s[3:])
```

Then predict `s[0] = "J"`.

**Cold check**

Trace positive/negative indices, omitted slice bounds, out-of-range indexing vs slicing, and assignment to a string index.

## Block 3.3 — String operations and comparisons

**Tiny theory**

Strings support iteration, concatenation (`+`), repetition (`*`), and membership (`in`, `not in`). Comparisons are lexicographic by character code point, not language-aware dictionary order.

**Cold check**

Predict short expressions; separate substring membership from list-style element membership.

## Block 3.4 — String methods and searching

**Tiny theory**

Recognize common `.is...()` tests, `.join()`, `.split()`, `.strip()`, `.find()`, `.rfind()`, and `.index()`. `find` returns `-1` when absent; `index` raises `ValueError`. `sorted(text)` returns a list of sorted characters.

**Predict / try**

```python
parts = ["red", "green", "blue"]
print("/".join(parts))
print("red,green,blue".split(","))
print("  Python  ".strip())
```

**Cold check**

Test return types, missing-substring behavior, join direction, and sorted output.

**Section exit gate:** an exam-style mixed string set at 80% or better, with focused repair for misses.

---

# Section 4 — Object-Oriented Programming

The largest exam section (34%). Keep it in small blocks and revisit earlier rules through mixed prediction.

## Block 4.1 — Classes, objects, and vocabulary

**Tiny theory**

A class defines a structure and behavior; an object is an instance. Attributes hold values, methods are functions associated with a class/object. Encapsulation groups data and behavior; inheritance reuses/specializes behavior; polymorphism lets a common operation work with different object types.

**Cold check**

Match examples to class, instance, attribute, method, superclass, subclass, encapsulation, and polymorphism.

## Block 4.2 — Instance and class variables

**Tiny theory**

Class attributes are stored on the class and can be shared/looked up by instances. Instance attributes belong to individual objects. Assigning `obj.x` may create or shadow an instance attribute without changing `Class.x`.

**Predict / try**

```python
class Counter:
    count = 0

one = Counter()
two = Counter()
one.count = 5
print(one.count, two.count, Counter.count)
```

**Cold check**

Trace lookup and assignment, then inspect `Class.__dict__` and `obj.__dict__`.

## Block 4.3 — Methods, `self`, and construction

**Tiny theory**

An ordinary instance method receives the instance as its first argument, conventionally `self`. `__init__` initializes a newly created object; it should not return a non-`None` value.

**Predict / try**

```python
class Box:
    def __init__(self, value):
        self.value = value

    def show(self):
        return self.value

box = Box(7)
print(box.show())
```

**Cold check**

Trace method binding, missing/extra arguments, constructor calls, and instance creation.

## Block 4.4 — Private names and `__dict__`

**Tiny theory**

A leading underscore is a convention for internal use. A double leading underscore in a class triggers name mangling (for example `__x` becomes `_ClassName__x`); it is not strict security. `__dict__` exposes an object's or class's attribute dictionary where applicable.

**Cold check**

Predict attribute lookup, name-mangled spellings, and whether a class attribute appears in an instance dictionary.

## Block 4.5 — Introspection

**Tiny theory**

`hasattr(obj, "name")` checks for an attribute. Common class metadata includes `__name__`, `__module__`, and `__bases__`. Compare the class and instance being inspected.

**Cold check**

Predict `hasattr`, identify which object owns a property, and interpret class names/base classes.

## Block 4.6 — Inheritance and overriding

**Tiny theory**

A subclass inherits accessible behavior from a superclass. A same-named subclass method overrides the inherited method. An overridden parent `__init__` is not automatically called; use `super()` when the parent initialization is needed.

**Predict / try**

Trace a base method, an override, and a child constructor that calls `super().__init__()`.

**Cold check**

Predict inherited lookup, constructor state, and behavior when a parent constructor is omitted.

## Block 4.7 — Multiple inheritance, MRO, and polymorphism

**Tiny theory**

Python searches methods using the class's method resolution order. In `class D(B, C)`, the declared order matters, subject to Python's consistent MRO. `isinstance(obj, Base)` is true for instances of subclasses. `is` tests identity; `==` tests equality. `__str__` controls the user-facing string form.

**Predict / try**

Use a small diamond hierarchy and predict which method is found first. Inspect `D.__mro__` after predicting.

**Cold check**

Test override selection, `isinstance`, equality vs identity, `__str__`, and a simple multiple-inheritance lookup.

**Section exit gate:** do not require perfect first-pass recall. Use a 12–15 item mixed check, repair misses, then retest with new examples. Require at least 80% and no repeated confusion over lookup, `self`, or constructor behavior.

---

# Section 5 — Miscellaneous

## Block 5.1 — List comprehensions

**Tiny theory**

A list comprehension builds a list from an iterable, with optional conditions and nested loops. The order of `for` clauses controls iteration order.

**Predict / try**

```python
doubles = [n * 2 for n in range(5)]
evens = [n for n in range(8) if n % 2 == 0]
pairs = [(a, b) for a in range(2) for b in range(3)]
```

**Cold check**

Trace values, condition placement, nesting order, and result length.

## Block 5.2 — Lambdas, `map`, and `filter`

**Tiny theory**

A `lambda` creates a small anonymous function with one expression. `map(function, iterable)` transforms items; `filter(function, iterable)` keeps items whose function result is truthy. In Python 3 both return iterators; wrap with `list()` to display/materialize them.

**Predict / try**

```python
nums = [1, 2, 3, 4]
print(list(map(lambda n: n * 2, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))
```

**Cold check**

Distinguish transform from select and identify lazy iterator results.

## Block 5.3 — Closures

**Tiny theory**

A closure is an inner function that retains access to names from its enclosing scope after the outer function has returned.

**Predict / try**

```python
def make_adder(amount):
    def add(value):
        return amount + value
    return add

add_five = make_adder(5)
print(add_five(3))
```

**Cold check**

Identify which value is retained and trace calls after the outer function has finished.

## Block 5.4 — I/O concepts and modes

**Tiny theory**

A file handle is an object used to interact with a stream. Text mode reads/writes `str` with encoding; binary mode reads/writes `bytes`. Standard streams include `stdin`, `stdout`, and `stderr`. Common modes include `r`, `w`, `a`, `x`, and their binary forms (`rb`, `wb`, etc.).

**Cold check**

Choose mode and result type for common file tasks; distinguish a stream from its underlying file.

## Block 5.5 — File operations and buffers

**Tiny theory**

`open()` returns a file object or raises an exception. Know `.read()`, `.readline()`, `.readlines()`, `.write()`, `.close()`, and context-manager use. Text reads return `str`; binary reads return `bytes`. `bytearray` is mutable and can be used as a writable buffer; `bytes` is immutable. `errno` represents OS error codes.

**Predict / try**

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("one\ntwo\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.readline().strip())
```

Use a tiny binary example to compare `bytes` and `bytearray`.

**Cold check**

Test modes, returned types, `read` family behavior, writing, closing, `bytearray`, and errors such as a missing file.

## Section 5 extensions from the presentation

After the official blocks are secure, briefly explore the presentation's remaining topics:

- **Iterators:** `iter(obj)` obtains an iterator; `next(it)` obtains the next value; exhaustion raises `StopIteration`.
- **Generators:** a function containing `yield` produces values lazily and retains its local state between requests.
- **Environment/date modules:** `os`, `time`, `datetime`, and `calendar` provide operating-system, time, date, and calendar tools.
- **`pip`:** installs and manages external Python packages.
- **OOP enrichment:** abstract base classes and operator overloading.

These are presentation extensions, not separate weighted domains in the official PCAP-31-03 syllabus used for the mock.

**Final readiness sequence:** section checks at 80%+; then take the 40-question weighted mock under timed conditions; repair by domain; finish with a fresh mixed retest. Readiness is based on demonstrated results, not the calendar.

---

## Source and scope

- Primary course source: supplied `Python_Advanced.pptx` (136 slides).
- Exam scope and weightings: Python Institute, [PCAP-31-03 Exam Syllabus](https://pythoninstitute.org/pcap-exam-syllabus), accessed 28 September 2026.
- If the official syllabus changes, update the weighting and question counts before reusing the mock.
