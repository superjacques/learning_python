# PCAP Class Practice Test — Marked Baseline

**Purpose:** Class-use marking sheet + post-class training baseline.

**Source:** `📘 Comprehensive PCAP Practice Test` supplied by the class.

## Baseline score

- **Adjusted score: 62 / 99 scorable questions = 62.6% → 63%**
- **Q65 is not scored** because its wording mixes an *attribute* (`__mro__`) with a *method* (`mro()`) even though both expose the MRO.
- The PDF also contains a **duplicate Question 94**. I label the second one **94B** and do not score it because your 1–100 answer sequence clearly maps to the first Q94 and then Q95 onward.
- A correct answer marked with `?`, `guess`, or similar is **credited for the test score but remains an uncertainty in the training ledger**.

---

## Section 1 — Modules & Packages

### 1. Which statement correctly imports the `sqrt` function from the `math` module?

a) `import math.sqrt`  
b) `from math import sqrt`  
c) `import sqrt from math`  
d) `math import sqrt`  

**Your answer:** C  
**Mark:** ❌ Incorrect  
**Correct answer:** B — `from math import sqrt`  
**Why:** `from module import name` imports a specific name from a module. `import sqrt from math` is not valid Python syntax.

### 2. What is the role of `__init__.py` in a package?

a) Defines global variables  
b) Marks a directory as a package  
c) Automatically imports all modules  
d) Stores metadata only  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** For the conventional package model used in this course, `__init__.py` identifies/initializes a package and can contain package initialization code. Modern Python also supports namespace packages without it.

### 3. Why is `import *` discouraged?

a) It slows down execution  
b) It hides private attributes  
c) It pollutes the namespace and causes collisions  
d) It prevents module reuse  

**Your answer:** C  
**Mark:** ✅ Correct  
**Correct answer:** C  
**Why:** `from module import *` injects many names into the current namespace, making collisions and unclear name origins more likely.

### 4. Which command installs a package using `pip`?

a) `python install package`  
b) `pip install package`  
c) `import package`  
d) `pip add package`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** The standard command is `pip install package`.

---

## Section 2 — Strings

### 5. Strings in Python are:

a) Mutable  
b) Immutable  
c) Stored as lists  
d) Stored as dictionaries  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** Strings are immutable: individual characters cannot be changed in place.

### 6. What is the output of:

```python
s = "Python"
print(s[-1])
```

a) `P`  
b) `n`  
c) `o`  
d) Error  

**Your answer:** D  
**Mark:** ❌ Incorrect  
**Correct answer:** B — `n`  
**Why:** Index `-1` means the last element of a sequence. The last character of `Python` is `n`.

### 7. Which method converts a string to uppercase?

a) `upper()`  
b) `capitalize()`  
c) `toUpper()`  
d) `case()`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** `str.upper()` returns an uppercase copy of the string.

### 8. What is the result of:

```python
"Py" + "thon"
```

a) Error  
b) `Python`  
c) `Py thon`  
d) `None`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** The `+` operator concatenates strings directly; it does not insert a space.

---

## Section 3 — Lists

### 9. Which method adds an element at the end of a list?

a) `insert()`  
b) `append()`  
c) `extend()`  
d) `add()`  

**Your answer:** B?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** B  
**Why:** `append(x)` adds one object `x` as a single new element at the end of a list.
  
**Training note:** You marked this as uncertain, so it should still get a quick repetition later.

### 10. What is the output?

```python
nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)
```

a) `[1,2,3,[4,5]]`  
b) `[1,2,3,4,5]`  
c) Error  
d) `None`  

**Your answer:** A?  
**Mark:** ❌ Incorrect  
**Correct answer:** B — `[1, 2, 3, 4, 5]`  
**Why:** `extend()` iterates over the supplied iterable and adds each item separately. `append([4,5])` would create the nested list in option A.

### 11. Which method removes the first occurrence of a value?

a) `del`  
b) `remove()`  
c) `pop()`  
d) `clear()`  

**Your answer:** B?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** B  
**Why:** `remove(value)` removes the first matching value. `pop()` removes by index (default: last item).

### 12. What is the result of:

```python
[x**2 for x in range(3)]
```

a) `[0,1,4]`  
b) `[1,4,9]`  
c) `[0,1,2]`  
d) Error  

**Your answer:** B?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — `[0, 1, 4]`  
**Why:** `range(3)` produces `0, 1, 2`; squaring each gives `0, 1, 4`.

---

## Section 4 — Exceptions

### 13. Which block always executes?

a) `try`  
b) `except`  
c) `else`  
d) `finally`  

**Your answer:** D  
**Mark:** ✅ Correct  
**Correct answer:** D  
**Why:** `finally` executes after the `try`/`except` flow whether or not an exception occurs.

### 14. What is the output?

```python
try:
    print(10/0)
except ZeroDivisionError:
    print("Error")
else:
    print("No Error")
finally:
    print("Done")
```

**Your answer:** Error / Done  
**Mark:** ✅ Correct  
**Correct answer:** `Error` then `Done`  
**Why:** `10/0` raises `ZeroDivisionError`, so the matching `except` runs. `else` is skipped because an exception occurred. `finally` still runs.

### 15. Which exception occurs when accessing a list index out of range?

a) `ValueError`  
b) `IndexError`  
c) `KeyError`  
d) `TypeError`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** An invalid sequence index raises `IndexError`.

### 16. How do you define a custom exception?

a) Subclass `Exception`  
b) Use `raise CustomError` directly  
c) Modify `BaseException`  
d) Use `except CustomError` only  

**Your answer:** C???  
**Mark:** ❌ Incorrect  
**Correct answer:** A — subclass `Exception`  
**Why:** A normal custom exception is defined with something like `class MyError(Exception): pass`.
  
**Training note:** High uncertainty recorded.

---

## Section 5 — OOP

### 17. A class is:

a) An instance of an object  
b) A blueprint for objects  
c) A function container only  
d) A data type  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** A class defines structure and behaviour; objects are instances created from that class.

### 18. What does `__init__` do?

a) Defines class methods  
b) Initializes object attributes  
c) Deletes objects  
d) Creates inheritance chains  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** `__init__` runs during normal instance creation and is used to initialize the object's state.

### 19. Which syntax is used for inheritance?

a) `inherits`  
b) `extends`  
c) `class Child(Parent)`  
d) `superclass`  

**Your answer:** C?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** C  
**Why:** Python names the parent class inside parentheses in the child class declaration.

### 20. What is polymorphism?

a) Multiple inheritance  
b) Ability of methods to behave differently depending on object type  
c) Encapsulation of attributes  
d) Overloading constructors  

**Your answer:** B? maybe D?  
**Mark:** ✅ Correct choice was B — uncertainty logged  
**Correct answer:** B  
**Why:** Polymorphism means a common operation/interface can produce different behaviour depending on the object/type.

---

## Section 6 — Inheritance & MRO

### 21. Which function is used to call the next implementation in the inheritance/MRO chain (commonly a parent constructor)?

a) `parent()`  
b) `super()`  
c) `init()`  
d) `base()`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** `super()` provides access to the next class in the MRO; `super().__init__(...)` is the common constructor example.

### 22. What is the MRO of class `D(B, C)` in the diamond example where `B` and `C` both inherit from `A`?

a) `D → B → C → A → object`  
b) `D → C → B → A → object`  
c) `D → A → B → C → object`  
d) `D → object → B → C → A`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** C3 linearization preserves the local order `B` before `C` and places the shared ancestor `A` after them.

### 23. Which inheritance type involves one parent and multiple children?

a) Multiple  
b) Multilevel  
c) Hierarchical  
d) Hybrid  

**Your answer:** C  
**Mark:** ✅ Correct  
**Correct answer:** C  
**Why:** Hierarchical inheritance is one base class with multiple subclasses.

### 24. Which inheritance type combines multiple inheritance patterns, such as multiple and hierarchical?

a) Hybrid  
b) Diamond  
c) Multilevel  
d) Single  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** Hybrid inheritance is a combination of inheritance forms.

---

## Section 7 — Generators & Iterators

### 25. What keyword makes a function a generator?

a) `return`  
b) `yield`  
c) `gen`  
d) `iterator`  

**Your answer:** B?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** B  
**Why:** A function containing `yield` is a generator function.

### 26. Which built-in function returns an iterator for an iterable?

a) `iter()`  
b) `next()`  
c) `list()`  
d) `dict()`  

**Your answer:** B?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — `iter()`  
**Why:** `iter(obj)` obtains an iterator. `next(iterator)` asks that iterator for its next value.

### 27. What is the output?

```python
def gen():
    yield 1
    yield 2

print(list(gen()))
```

a) `[1]`  
b) `[2]`  
c) `[1,2]`  
d) Error  

**Your answer:** C (guess)  
**Mark:** ✅ Correct — guess logged  
**Correct answer:** C — `[1, 2]`  
**Why:** `list()` consumes the generator until exhaustion, collecting both yielded values.

### 28. Which statement about iterators is true?

a) They store all values in memory  
b) They generate/retrieve values on demand  
c) They cannot be looped  
d) They are immutable  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** Iterators provide values one at a time as requested. They do not inherently require materializing an entire sequence.

---

## Section 8 — File Handling

### 29. Which mode opens a file for reading text?

a) `r`  
b) `w`  
c) `rb`  
d) `wb`  

**Your answer:** r  
**Mark:** ✅ Correct  
**Correct answer:** A — `r`  
**Why:** `r` opens a text file for reading. `rb` is binary read mode.

### 30. What is the effect of this code?

```python
f = open("test.txt", "w")
f.write("Hello")
f.close()
```

a) Creates/overwrites the file with `"Hello"`  
b) Error  
c) Appends `"Hello"`  
d) Deletes the file  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** Mode `w` opens for writing, creating the file if necessary and truncating an existing file.

### 31. Which method reads all lines into a list?

a) `read()`  
b) `readline()`  
c) `readlines()`  
d) `list()`  

**Your answer:** A?  
**Mark:** ❌ Incorrect  
**Correct answer:** C — `readlines()`  
**Why:** `readlines()` returns a list of the remaining lines. `read()` returns one string containing the remaining contents.

### 32. Which statement ensures a file closes automatically?

a) `close()`  
b) `with open(...) as f:`  
c) `end()`  
d) `stop()`  

**Your answer:** A  
**Mark:** ❌ Incorrect  
**Correct answer:** B — `with open(...) as f:`  
**Why:** A context manager closes the file automatically when the `with` block exits. `close()` is a manual close.

---

## Section 9 — Miscellaneous

### 33. Which module provides system/platform details?

a) `os`  
b) `platform`  
c) `sys`  
d) `random`  

**Your answer:** A  
**Mark:** ❌ Incorrect  
**Correct answer:** B — `platform`  
**Why:** The `platform` module exposes functions such as `system()`, `machine()`, and `python_implementation()`.

### 34. Which module generates random numbers?

a) `math`  
b) `random`  
c) `statistics`  
d) `numpy`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** Python's standard `random` module provides pseudo-random functions.

### 35. Which function lists attributes/names available on an object or module?

a) `dir()`  
b) `list()`  
c) `help()`  
d) `globals()`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** `dir(module)` lists names available on the module.

### 36. Which statement aliases a module as `m`?

a) `import math as m`  
b) `rename math m`  
c) `alias math m`  
d) `import m as math`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** `as` creates the local alias: after this import, use `m.sqrt(...)`, etc.

---

## Section 10 — Short Answer

### 37. Explain the difference between `append()` and `extend()` in lists.

**Your answer:** “append replaces, and extend adds at the end”  
**Mark:** ❌ Incorrect  
**Correct answer:** `append(x)` adds one object; `extend(iterable)` adds each element from the iterable  
**Why:** Neither method 'replaces' the list. `append([4,5])` adds one nested list; `extend([4,5])` adds `4` and `5` as separate elements.

### 38. What is the purpose of the `finally` block?

**Your answer:** “always executes”  
**Mark:** ✅ Correct  
**Correct answer:** Runs cleanup code whether an exception occurred or not  
**Why:** That is the key idea. `finally` runs after the `try`/`except` flow, including when an exception propagates.

### 39. How does Python handle negative indexing in sequences?

**Your answer:** “works from last backwards to the first”  
**Mark:** ✅ Correct  
**Correct answer:** Negative indices count from the end  
**Why:** `-1` is the last item, `-2` the second-last, and so on.

### 40. Why is `import *` discouraged?

**Your answer:** “causes collisions”  
**Mark:** ✅ Correct  
**Correct answer:** It can pollute the namespace and cause name collisions  
**Why:** It also makes code harder to read because the source of imported names is unclear.

---

## Section 11 — Advanced Strings

### 41. Which method removes whitespace from both ends of a string?

a) `strip()`  
b) `rstrip()`  
c) `lstrip()`  
d) `clean()`  

**Your answer:** A? (guess)  
**Mark:** ✅ Correct — guess logged  
**Correct answer:** A  
**Why:** `strip()` removes leading and trailing whitespace. `lstrip()` and `rstrip()` affect one side only.

### 42. What is the output?

```python
s = "Python"
print(s[2:5])
```

**Your answer:** tho  
**Mark:** ✅ Correct  
**Correct answer:** `tho`  
**Why:** Slice start is inclusive and stop is exclusive: indices 2, 3, and 4 are `t`, `h`, `o`.

### 43. Which escape sequence represents a newline?

a) `\t`  
b) `\n`  
c) `\\`  
d) `\"`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B — `\n`  
**Why:** `\n` is newline; `\t` is tab.

### 44. What is the result of:

```python
f"{2+3}"
```

**Your answer:** 5  
**Mark:** ✅ Correct  
**Correct answer:** `"5"`  
**Why:** The expression inside the f-string evaluates to `5`, then is formatted into a string. The resulting value is the string `"5"`.

### 45. Which method checks if a string starts with a given prefix?

a) `startswith()`  
b) `prefix()`  
c) `begin()`  
d) `init()`  

**Your answer:** B?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — `startswith()`  
**Why:** Example: `"Python".startswith("Py")` returns `True`.

---

## Section 12 — Advanced Lists

### 46. Which method returns a shallow copy of a list?

a) `copy()`  
b) `clone()`  
c) `duplicate()`  
d) `slice()`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** `list.copy()` returns a shallow copy.

### 47. What is the output?

```python
nums = [1, 2, 3]
print(nums.pop())
```

**Your answer:** [1,2,3]  
**Mark:** ❌ Incorrect  
**Correct answer:** `3`  
**Why:** `pop()` removes and returns an item. With no index it removes/returns the last item, so `print(nums.pop())` prints `3`.

### 48. Which method sorts a list in place?

a) `sort()`  
b) `sorted()`  
c) `order()`  
d) `arrange()`  

**Your answer:** A?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** A  
**Why:** `list.sort()` modifies the list in place. `sorted(iterable)` returns a new sorted list.

### 49. What is the result of:

```python
len([1, 2, [3, 4]])
```

**Your answer:** 3  
**Mark:** ✅ Correct  
**Correct answer:** `3`  
**Why:** The outer list has three elements: `1`, `2`, and the nested list `[3,4]`.

### 50. Which comprehension creates a list of even numbers from 0–10?

a) `[x for x in range(11) if x%2==0]`  
b) `[x for x in range(11) if x%2!=0]`  
c) `[x for x in range(10)]`  
d) `[x+2 for x in range(11)]`  

**Your answer:** A  
**Mark:** ✅ Correct  
**Correct answer:** A  
**Why:** The condition keeps values divisible by two, and `range(11)` includes 0 through 10.

---

## Section 13 — Exceptions (Advanced)

### 51. Which exception occurs when converting a non-numeric string to `int`?

a) `ValueError`  
b) `TypeError`  
c) `IndexError`  
d) `KeyError`  

**Your answer:** B?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — `ValueError`  
**Why:** `int("abc")` receives a valid kind of input (a string), but the value cannot be parsed as an integer, so it raises `ValueError`.

### 52. What is the output?

```python
try:
    int("abc")
except ValueError:
    print("Invalid")
```

**Your answer:** “Maybe TypeError, then nothing; if ValueError it prints Invalid”  
**Mark:** ❌ Incorrect  
**Correct answer:** `Invalid`  
**Why:** `int("abc")` raises `ValueError`, so the matching handler prints `Invalid`.
  
**Training note:** This is a useful exact gap: `ValueError` vs `TypeError`.

### 53. Which keyword raises an exception manually?

a) `throw`  
b) `raise`  
c) `except`  
d) `error`  

**Your answer:** B?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** B  
**Why:** Python uses `raise`, e.g. `raise ValueError('bad value')`.

### 54. Which exception occurs when accessing a dictionary key that doesn't exist?

a) `KeyError`  
b) `IndexError`  
c) `ValueError`  
d) `TypeError`  

**Your answer:** A?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** A  
**Why:** Direct lookup of a missing dictionary key raises `KeyError`.

### 55. What is the result of:

```python
try:
    print(1/1)
except:
    print("Error")
else:
    print("No Error")
```

**Your answer:** No Error  
**Mark:** ❌ Incomplete  
**Correct answer:** `1.0` then `No Error`  
**Why:** `1/1` succeeds and prints `1.0`. Because no exception occurred, the `else` block then prints `No Error`.

---

## Section 14 — OOP (Advanced)

### 56. Which keyword defines a class?

a) `object`  
b) `class`  
c) `def`  
d) `struct`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** Classes are declared with the `class` keyword.

### 57. What is the output?

```python
class A:
    def __init__(self):
        self.x = 5

a = A()
print(a.x)
```

**Your answer:** 5  
**Mark:** ✅ Correct  
**Correct answer:** `5`  
**Why:** `__init__` sets the instance attribute `x` to 5.

### 58. Which concept groups data and methods together?

a) Polymorphism  
b) Encapsulation  
c) Inheritance  
d) Abstraction  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** Encapsulation bundles state and behaviour in a class and supports controlled access.

### 59. Which method is used for the normal string form when printing an object?

a) `__str__`  
b) `__repr__`  
c) `__init__`  
d) `__print__`  

**Your answer:** D?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — `__str__`  
**Why:** `print(obj)` uses `str(obj)`, which calls `obj.__str__()` when defined. If not, Python falls back to inherited behaviour.

### 60. Which OOP principle allows the same method/interface to have different implementations, including overriding?

a) Polymorphism  
b) Encapsulation  
c) Abstraction  
d) Composition  

**Your answer:** A?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** A  
**Why:** Method overriding is a common way runtime polymorphism appears.

---

## Section 15 — Inheritance & MRO (Advanced)

### 61. Which inheritance type involves multiple levels of classes?

a) Multilevel  
b) Multiple  
c) Hybrid  
d) Hierarchical  

**Your answer:** D?  
**Mark:** ❌ Incorrect  
**Correct answer:** A — Multilevel  
**Why:** Multilevel inheritance is a chain such as `Grandparent → Parent → Child`.

### 62. Which keyword/function is used to access the next parent/MRO implementation?

a) `base`  
b) `super`  
c) `parent`  
d) `inherit`  

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** B  
**Why:** `super()` provides access to the next class in the method resolution order.

### 63. What is the output?

```python
class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")

b = B()
b.f()
```

**Your answer:** B  
**Mark:** ✅ Correct  
**Correct answer:** `B`  
**Why:** `B.f()` overrides `A.f()`, and method lookup finds the subclass implementation first.

### 64. Which inheritance type may cause the diamond problem?

a) Multiple  
b) Single  
c) Hybrid  
d) Hierarchical  

**Your answer:** C  
**Mark:** ❌ Incorrect  
**Correct answer:** A — Multiple inheritance  
**Why:** The classic diamond occurs when a child inherits through multiple paths that lead to the same ancestor. Hybrid designs can contain such a structure, but the fundamental cause is multiple inheritance.

### 65. Which attribute shows the MRO of a class?

a) `__mro__`  
b) `mro()`  
c) Both A and B  
d) None  

**Your answer:** B  
**Mark:** ⚠️ Ambiguous wording — not scored  
**Correct answer:** Precise wording: `__mro__` is the attribute; `mro()` is a method. Both expose the MRO.  
**Why:** The class material taught both ways to view MRO. Because the question specifically says 'attribute' but also offers a method and 'Both', it is poorly worded. This is not counted as a conceptual error.

---

## Section 16 — Generators & Iterators

### 66. Which keyword defines a generator?

**Your answer:** `iter()` ???  
**Mark:** ❌ Incorrect  
**Correct answer:** `yield`  
**Why:** `yield` makes the function a generator function. `iter()` obtains an iterator from an iterable.

### 67. What is the output?

```python
def g():
    yield 1
    yield 2

print(next(g()))
```

**Your answer:** 2  
**Mark:** ❌ Incorrect  
**Correct answer:** `1`  
**Why:** `g()` creates a fresh generator positioned before the first yield. The first `next()` returns the first yielded value, `1`.

### 68. Which function retrieves the next item from an iterator?

**Your answer:** `next()`  
**Mark:** ✅ Correct  
**Correct answer:** `next()`  
**Why:** `next(iterator)` asks the iterator for its next value.

### 69. Which built-in converts an iterator to a list?

**Your answer:** No idea  
**Mark:** ❌ Incorrect / unanswered  
**Correct answer:** `list()`  
**Why:** `list(iterator)` consumes the iterator and materializes its remaining items into a list.

### 70. Why are generators memory-efficient?

**Your answer:** “they only store one value at a time”  
**Mark:** ✅ Correct idea  
**Correct answer:** They produce values lazily instead of storing the whole sequence at once  
**Why:** A generator keeps its execution state and yields values on demand, so large sequences need not be fully materialized in memory.

---

## Section 17 — File Handling

### 71. Which mode opens a file for writing text?

**Your answer:** `w` or `a`  
**Mark:** ❌ Not accepted — two different modes supplied  
**Correct answer:** `w`  
**Why:** `w` opens for writing and truncates/creates the file. `a` opens for appending and preserves existing content.

### 72. Which mode appends to a file?

**Your answer:** `a`  
**Mark:** ✅ Correct  
**Correct answer:** `a`  
**Why:** Append mode writes at the end without truncating existing contents.

### 73. What is the result/effect?

```python
f = open("t.txt", "w")
f.write("Hi")
f.close()
```

**Your answer:** “No output on screen. It writes Hi to t.txt.”  
**Mark:** ✅ Correct  
**Correct answer:** No console output; `t.txt` is written with `Hi`  
**Why:** `write()` writes to the file and its return value is not printed.

### 74. Which method reads one line?

**Your answer:** `readline()` ?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** `readline()`  
**Why:** `readline()` reads one line at a time.

### 75. Which statement ensures automatic closing?

**Your answer:** `close()`  
**Mark:** ❌ Incorrect  
**Correct answer:** `with open(...) as f:`  
**Why:** `close()` is manual. A context manager closes the file automatically when the `with` block exits.

---

## Section 18 — Advanced Modules

### 76. Which module provides OS functions?

**Your answer:** `os`  
**Mark:** ✅ Correct  
**Correct answer:** `os`  
**Why:** The `os` module provides operating-system-related functions.

### 77. Which module provides time functions?

**Your answer:** `date` ?  
**Mark:** ❌ Incorrect  
**Correct answer:** `time`  
**Why:** The `time` module contains time-related functions such as `time()` and `sleep()`.

### 78. Which module provides date/time classes?

**Your answer:** `date` ?  
**Mark:** ❌ Incorrect  
**Correct answer:** `datetime`  
**Why:** The `datetime` module provides classes such as `date`, `time`, `datetime`, and `timedelta`.

### 79. Which module provides calendar utilities?

**Your answer:** `cal` ?  
**Mark:** ❌ Not exact / uncertainty logged  
**Correct answer:** `calendar`  
**Why:** The module name is `calendar`, e.g. `calendar.month(year, month)`.

### 80. Which function lists attributes of a module?

**Your answer:** `dir()`  
**Mark:** ✅ Correct  
**Correct answer:** `dir()`  
**Why:** `dir(module)` lists names available on the module.

---

## Section 19 — Advanced OOP

### 81. Which method is associated with object finalization/destruction in Python?

**Your answer:** `del()`  
**Mark:** ❌ Incorrect  
**Correct answer:** `__del__()`  
**Why:** The special method is `__del__`. The `del` statement removes a reference/name; it is not a normal `del()` method. Python object destruction timing is implementation/lifetime dependent.

### 82. Which principle hides implementation details?

**Your answer:** ???  
**Mark:** ❌ Unanswered  
**Correct answer:** Abstraction  
**Why:** Abstraction exposes what a user needs while hiding unnecessary implementation details.

### 83. Which principle allows multiple forms of a method/interface?

**Your answer:** Polymorphism  
**Mark:** ✅ Correct  
**Correct answer:** Polymorphism  
**Why:** Polymorphism allows the same operation/interface to behave differently for different objects.

### 84. Which principle allows code reuse through parent/child classes?

**Your answer:** OOP / classes  
**Mark:** ❌ Incorrect  
**Correct answer:** Inheritance  
**Why:** Inheritance lets a subclass reuse and extend behaviour from a base class.

### 85. Which principle groups data and methods?

**Your answer:** Encapsulation  
**Mark:** ✅ Correct  
**Correct answer:** Encapsulation  
**Why:** Encapsulation groups state and behaviour and supports controlled access to internal state.

---

## Section 20 — Miscellaneous

### 86. Which keyword defines a function?

**Your answer:** `def`  
**Mark:** ✅ Correct  
**Correct answer:** `def`  
**Why:** Normal functions are declared with `def`.

### 87. Which keyword defines an anonymous function?

**Your answer:** `lambda`  
**Mark:** ✅ Correct  
**Correct answer:** `lambda`  
**Why:** A lambda is an anonymous one-expression function.

### 88. Which operator tests membership?

**Your answer:** `==`  
**Mark:** ❌ Incorrect  
**Correct answer:** `in` (or `not in`)  
**Why:** Membership asks whether a value occurs in a container/sequence: `x in items`.

### 89. Which operator tests identity?

**Your answer:** `==`  
**Mark:** ❌ Incorrect  
**Correct answer:** `is` (or `is not`)  
**Why:** `is` tests object identity; `==` tests equality of values.

### 90. Which keyword defines a loop?

**Your answer:** `for`  
**Mark:** ✅ Accepted  
**Correct answer:** `for` is valid; `while` also defines a loop  
**Why:** The source question is broad because Python has both `for` and `while` loops. Your `for` answer is valid.

---

## Section 21 — More Code Analysis

### 91. What is the output?

```python
print(type([]))
```

**Your answer:** string?  
**Mark:** ❌ Incorrect  
**Correct answer:** `<class 'list'>`  
**Why:** `[]` is a list literal.

### 92. What is the output?

```python
print(type(()))
```

**Your answer:** tuple?  
**Mark:** ✅ Correct — uncertainty logged  
**Correct answer:** `<class 'tuple'>`  
**Why:** `()` is an empty tuple literal.

### 93. What is the output?

```python
print(type({}))
```

**Your answer:** tuple?  
**Mark:** ❌ Incorrect  
**Correct answer:** `<class 'dict'>`  
**Why:** `{}` creates an empty dictionary. An empty set is created with `set()`.

### 94. What is the output?

```python
print(type(set()))
```

**Your answer:** ???  
**Mark:** ❌ Unanswered  
**Correct answer:** `<class 'set'>`  
**Why:** `set()` constructs an empty set.

---

## Section 22 — Advanced Python Concepts

### 94B. [Source numbering error] Which keyword is used to define an anonymous function in Python?

**Your answer:** No separate answer supplied because the PDF repeats question number 94  
**Mark:** ⚠️ Not scored  
**Correct answer:** `lambda`  
**Why:** The PDF numbers both the `type(set())` question and this anonymous-function question as 94. Your 1–100 answer sequence clearly continues with source Q95 after the first Q94.

### 95. What is the output?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

**Your answer:** [1,2,3,4]  
**Mark:** ✅ Correct  
**Correct answer:** `[1, 2, 3, 4]`  
**Why:** `y = x` makes both names refer to the same list object. Mutating through `y` is visible through `x`.

### 96. Which built-in function returns an object's identity value (described in the source as its memory address)?

**Your answer:** ???  
**Mark:** ❌ Unanswered  
**Correct answer:** `id()`  
**Why:** `id(obj)` returns an integer identifying the object for its lifetime. CPython often relates this to an address, but Python only guarantees uniqueness among simultaneously existing objects.

### 97. What is the difference between `is` and `==`?

**Your answer:** “is assigns, == compares”  
**Mark:** ❌ Incorrect  
**Correct answer:** `is` tests identity; `==` tests value equality  
**Why:** Assignment uses `=`. `is` asks whether two references point to the same object; `==` asks whether their values compare equal.

### 98. Which built-in returns the length of an iterable/container?

**Your answer:** `len()`  
**Mark:** ✅ Correct  
**Correct answer:** `len()`  
**Why:** `len(obj)` returns the number of items for supported containers/sequences.

### 99. What is the output?

```python
print(bool([]))
```

**Your answer:** False  
**Mark:** ✅ Correct  
**Correct answer:** `False`  
**Why:** Empty containers are falsey.

### 100. What is the output?

```python
print("Python" * 2)
```

**Your answer:** Python Python  
**Mark:** ❌ Incorrect  
**Correct answer:** `PythonPython`  
**Why:** String repetition does not insert a separator. Multiplying the string by 2 concatenates two copies directly.

---

# Section Results

| Section | Score | Result | Training meaning |
|---|---:|---:|---|
| 1 Modules & Packages | 3/4 | 75% | Mostly sound; repair import syntax. |
| 2 Strings | 3/4 | 75% | Basic string knowledge good; refresh negative indexing. |
| 3 Lists | 2/4 | 50% | Needs PCEP refresh: `append`, `extend`, comprehensions. |
| 4 Exceptions | 3/4 | 75% | Basic flow good; custom exceptions need repair. |
| 5 OOP | 4/4 | 100% | Strong first-pass understanding. |
| 6 Inheritance & MRO | 4/4 | 100% | Strong first-pass understanding. |
| 7 Generators & Iterators | 3/4 | 75% | Concept introduced, but `iter()` vs `next()` still shaky. |
| 8 File Handling | 2/4 | 50% | Needs work: `readlines()` and context managers. |
| 9 Miscellaneous | 3/4 | 75% | `platform` module needs refresh. |
| 10 Short Answer | 3/4 | 75% | `append()` vs `extend()` is a real gap. |
| 11 Advanced Strings | 4/5 | 80% | Generally good; `startswith()` needs recall. |
| 12 Advanced Lists | 4/5 | 80% | Generally good; `pop()` behaviour needs refresh. |
| 13 Exceptions (Advanced) | 2/5 | 40% | High-priority repair: exception types and `else` flow. |
| 14 OOP (Advanced) | 4/5 | 80% | Good; learn `__str__` firmly. |
| 15 Inheritance & MRO (Advanced) | 2/4 scorable | 50% | Repair multilevel vs multiple/diamond. Q65 unscored. |
| 16 Generators & Iterators | 2/5 | 40% | High-priority class topic: `yield`, first `next()`, `list(iterator)`. |
| 17 File Handling | 3/5 | 60% | Modes mostly okay; automatic closing still weak. |
| 18 Advanced Modules | 2/5 | 40% | Class-extension gap: `time`, `datetime`, `calendar`. |
| 19 Advanced OOP | 2/5 | 40% | Repair `__del__`, abstraction, inheritance. |
| 20 Miscellaneous | 3/5 | 60% | Refresh `in`, `is`, `==`. |
| 21 More Code Analysis | 1/4 | 25% | Core type-literal refresh needed: list/tuple/dict/set. |
| 22 Advanced Python Concepts | 3/6 | 50% | Repair `id()`, identity vs equality, exact string repetition. |

# Training Reference Point

## Strong / demonstrated

- Core OOP vocabulary: class, object, `__init__`, polymorphism.
- Core inheritance: `super()`, hierarchical/hybrid concepts, basic MRO order and overriding.
- Encapsulation as a concept.
- Basic strings and several advanced string operations.
- List comprehension syntax once shown.
- Basic file writing and append mode.
- `dir()`, random module, alias imports.

## High-priority repair queue

1. **Exceptions:** `ValueError` vs `TypeError`, custom exceptions, exact `try/except/else/finally` output.
2. **OOP advanced details (important because OOP is heavily weighted in PCAP):** `__str__`, abstraction vs inheritance, multilevel vs multiple inheritance, diamond/MRO details, `__del__` terminology.
3. **File I/O:** `read()` vs `readline()` vs `readlines()`, `with open(...)` and automatic closing, `w` vs `a`.
4. **Core Python/PCEP refresh:** `append()` vs `extend()`, `pop()`, negative indexing, literal types `[] / () / {} / set()`, `in` vs `is` vs `==`.
5. **Generators/iterators:** `yield`, `iter()`, `next()`, generator state, `list(iterator)`. This matters for class coverage; in our PCAP-31-03 training material, iterators/generators are extension topics rather than a separate official weighted domain.
6. **Class extension modules:** `os`, `time`, `datetime`, `calendar`.

## Uncertainty that must not be mistaken for mastery

Correct answers that were explicitly uncertain/guessed include Q9, Q11, Q19, Q20, Q25, Q27, Q41, Q48, Q53, Q54, Q60, Q74 and Q92. These count toward the class test score, but should still receive short future reps.

## How this fits our main PCAP question bank

- Keep this class test as a **separate baseline/reference bank** rather than merging it into the main mock.
- Use the existing `PCAP_31-03_Mock_exam.md` as the **primary exam bank**, because it is deliberately weighted to the official PCAP domains.
- Use this class test for **class follow-along, quick refresh, and identifying gaps**.
- After class week, resume the mastery workflow from the recorded checkpoint and target the gaps above rather than restarting from zero.

## Current training ledger

- **Pre-class mastery track:** Modules/Packages through Block 1.7 demonstrated; Block 1.8 (nested imports/package search) and the Section 1 mixed exit gate remain outstanding.
- **Class-mode OOP exposure:** classes/objects, `self`, `__init__`, class vs instance ideas, inheritance types, `super()`, MRO/C3, polymorphism, duck typing, operator overloading, encapsulation/access conventions/getters-setters, abstraction/ABC/`@abstractmethod`.
- **Class-mode additional exposure:** iterators, generators, closures, file handling, `calendar` and related modules.
- **This test is the new baseline for what survived first exposure.** Class coverage does not automatically count as mastery.
