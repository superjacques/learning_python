# PCEP-30-02 Training Material

A guided, mastery-based course for the Python Institute PCEP-30-02 exam. The supplied **PythonTutorial.pptx** provides the introductory explanations and examples; the official [PCEP exam syllabus](https://pythoninstitute.org/pcep-exam-syllabus) defines the exam scope and weighting. This guide selects the PCEP material from the broader presentation and leaves its PCAP-level topics for the PCAP course.

## How to use this file

Study one block at a time. Read the short explanation, predict what the example will do, then type and run it in Python. Answer the cold check without looking at the answer key. If an answer is uncertain or incorrect, review that topic and try a fresh example before moving on.

For guided tutoring, copy the full text of [PCEP ChatGPT Instructions](PCEP_ChatGPT_instructions.md) into a ChatGPT conversation, then attach or paste this training material and [PCEP Mock Exam](PCEP_30-02_Mock_exam.md). Ask ChatGPT to begin or tell it your current block. Attempt the mock exam before consulting its answer key at the end.

**Environment:** Thonny is suitable for first exercises. Any Python 3 editor or terminal works. Save scripts with the `.py` extension. Run examples yourself; reading code alone is not enough practice.

## 🧭 Course Map

| Block | Official weight | What you will learn |
|---|---:|---|
| 1. Computer Programming and Python Fundamentals | 18% | Programming vocabulary, Python structure, values, names, operators, and console input/output |
| 2. Control Flow — Conditional Blocks and Loops | 29% | Decisions, iteration, nested flow, and loop control |
| 3. Data Collections — Tuples, Dictionaries, Lists, and Strings | 25% | Create, inspect, process, and choose basic collections and strings |
| 4. Functions and Exceptions | 28% | Decompose programs, pass data, understand scope, and handle exceptions |
| **Total** | **100%** | |

The official exam has 30 scored items across these four weighted blocks. The repository mock is a longer 200-question practice set for revision; it is not the official exam.

---

# Block 1 — Computer Programming and Python Fundamentals · 18%

## Block 1.1 — Programming vocabulary and running Python

**Tiny theory**

- A program is a set of instructions. A programming language defines their syntax and meaning.
- An interpreter executes instructions; compilation translates source code before execution. Python implementations may use both steps internally, but the exam tests the distinction in general terms.
- Syntax describes valid structure; semantics describes what valid code means; lexis concerns the language's tokens and vocabulary.
- A `.py` file contains Python source code. An IDE helps edit and run it; it is not the Python language itself.

**Try it**

Create `hello.py` and run:

```python
print("Hello, Python!")
```

**Cold check**

Explain the difference between source code and machine code. Identify whether a missing colon is a syntax problem or a wrong calculation is a logic problem.

## Block 1.2 — Keywords, instructions, comments, and indentation

**Tiny theory**

- Keywords such as `if`, `for`, and `def` have reserved meanings. They cannot be used as ordinary identifiers.
- Python is case-sensitive: `score` and `Score` are different names.
- Indentation groups statements into blocks. Use consistent indentation, conventionally four spaces.
- `#` begins a comment. A comment explains code to readers; Python does not execute it.

**Predict / try**

```python
score = 8
if score > 5:
    print("High")
# This line is a comment.
print("Done")
```

**Cold check**

Find the block controlled by `if`. What changes if the `print("High")` line is not indented? Is `True` a keyword, and is `true` the same name?

## Block 1.3 — Names, variables, literals, and number systems

**Tiny theory**

- A literal is a value written directly in code. A variable name refers to an object assigned to it.
- Identifiers may contain letters, digits, and underscores, but cannot start with a digit or be a keyword. Use clear `snake_case` names for variables and follow basic PEP 8 spacing conventions.
- Common PCEP values include `bool`, `int`, `float`, and `str`. `True`, `False`, and `None` have special meanings.
- Integers can be written in decimal, binary (`0b`), octal (`0o`), or hexadecimal (`0x`). Scientific notation such as `2.5e3` represents a floating-point value.
- Floating-point arithmetic has finite precision; some decimal fractions cannot be represented exactly in binary.

**Predict / try**

```python
count = 12
binary_count = 0b1100
price = 2.5e2
print(count == binary_count, price, type(price))
```

**Cold check**

Give one valid and one invalid identifier. Write decimal 10 in binary and hexadecimal. Why might `0.1 + 0.2 == 0.3` be false?

## Block 1.4 — Operators, types, and expressions

**Tiny theory**

- Numeric operators include `+`, `-`, `*`, `/`, `//`, `%`, and `**`. `/` produces a float; `//` performs floor division.
- `+` joins strings and `*` repeats them. Operators can be unary (one operand, such as `-x`) or binary (two operands, such as `x - y`).
- Comparisons produce Booleans. Boolean operators are `not`, `and`, and `or`. Parentheses make grouping explicit; otherwise use precedence rules to read expressions.
- Assignment operators include `=`, `+=`, and similar shortcuts. Assignment stores a value; `==` compares values.
- Bitwise operators act on integer bits: `~`, `&`, `^`, `|`, `<<`, and `>>`.
- Implicit conversion can occur in mixed numeric expressions. Explicit conversion uses functions such as `int()`, `float()`, and `str()`; conversion can lose information or fail.

**Predict / try**

```python
print(17 // 5, 17 % 5, 2 ** 3)
print("Py" + "thon", "ha" * 3)
print(3 < 5 and not False)
print(int(4.8), float("2.5"))
```

**Cold check**

Predict each result before running the code. Explain `/` versus `//`, `=` versus `==`, and one example where explicit conversion changes or rejects a value.

## Block 1.5 — Console input and output

**Tiny theory**

- `print()` displays values. Its `sep=` parameter sets the separator between values, and `end=` sets what follows the final value.
- `input()` displays an optional prompt and returns the entered text as a string.
- Convert input before numeric operations, for example with `int()` or `float()`.

**Predict / try**

```python
print("red", "blue", sep=" / ", end="!")
print("ready")

age_text = "20"  # stands in for input() so the example is repeatable
age = int(age_text)
print(age + 1)
```

**Cold check**

What is printed on each line? What type does `input()` return? How would you read a decimal number?

**Block 1 mastery check:** Read short expressions, identify names and types, convert simple values, and explain basic console I/O without relying on a worked example.

---

# Block 2 — Control Flow: Conditional Blocks and Loops · 29%

## Block 2.1 — Conditions and branching

**Tiny theory**

- `if` runs a block when its condition is true. `else` handles the other path; `elif` checks another condition.
- Conditions may combine comparisons with `and`, `or`, and `not`.
- Separate `if` statements are independent. An `if`/`elif` chain selects the first matching branch. Nested conditions put one decision inside another.

**Predict / try**

```python
mark = 82
if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
else:
    grade = "C"
print(grade)
```

**Cold check**

What is printed for marks 95, 82, and 60? Why does order matter? Write a condition for a value that is at least 10 and below 20.

## Block 2.2 — `while` loops and loop tracing

**Tiny theory**

- `while` repeats while its condition remains true. Update the state used by the condition so the loop can finish.
- Trace the condition before each iteration and record variable changes. An unchanged true condition can create an infinite loop.
- A `while` loop can have an `else` clause; it runs when the loop ends normally, but not when `break` exits it.

**Predict / try**

```python
number = 3
while number > 0:
    print(number)
    number -= 1
else:
    print("finished")
```

**Cold check**

List the output in order. What single change could make the loop never finish? When would its `else` block be skipped?

## Block 2.3 — `for`, sequences, `range()`, and membership

**Tiny theory**

- `for` assigns each item from an iterable to its loop variable, once per iteration.
- `range(stop)` starts at zero and excludes `stop`; `range(start, stop, step)` uses the same exclusive stop rule.
- `in` tests membership and can also introduce a `for` loop. Loops can be nested to process nested sequences or repeated combinations.

**Predict / try**

```python
for value in range(2, 8, 2):
    print(value)

for letter in "cat":
    print(letter)
```

**Cold check**

Which values are generated by `range(4)` and `range(1, 6, 2)`? How many times does a loop over a three-item list execute?

## Block 2.4 — Loop controls and `else`

**Tiny theory**

- `break` exits the nearest loop immediately.
- `continue` skips the remainder of the current iteration and proceeds to the next one.
- `pass` does nothing; it can keep a block syntactically valid while it is unfinished.
- A `for` loop's `else` runs if iteration finishes without `break`. The same rule applies to `while`-`else`.

**Predict / try**

```python
for number in range(5):
    if number == 2:
        continue
    if number == 4:
        break
    print(number)
else:
    print("no break")
```

**Cold check**

What prints? Does the loop's `else` run? Describe a search loop where `break` and `else` are useful.

**Block 2 mastery check:** Trace branches and nested loops accurately, determine loop counts, and explain the effect of `break`, `continue`, `pass`, and loop `else`.

---

# Block 3 — Data Collections: Tuples, Dictionaries, Lists, and Strings · 25%

## Block 3.1 — Lists and list processing

**Tiny theory**

- A list is an ordered, mutable collection. Indexing starts at zero; negative indexes count from the end. Slices select a range and exclude the stop index.
- Lists can hold mixed types and other lists. `len()` reports the number of items; `in` and `not in` test membership.
- Common operations include assignment by index, `append()`, `insert()`, `index()`, and `del`. `sorted()` returns a new sorted list; `sort()` changes a list in place.
- Assignment does not clone a list. A shallow copy can be made with `[:]` or `.copy()`. List comprehensions build a list from an iterable and expression.

**Predict / try**

```python
scores = [70, 85, 90]
scores.append(95)
print(scores[0], scores[-1], scores[1:3], len(scores))
print(sorted(scores), 85 in scores)
```

**Cold check**

What is `scores[1:3]`? What is the difference between `scores = other` and `scores = other[:]`? Build a list of squares for numbers 0 through 4 with a comprehension.

## Block 3.2 — Tuples and nested collections

**Tiny theory**

- A tuple is ordered and immutable. It supports indexing, slicing, iteration, and membership like a list, but its item references cannot be reassigned.
- A one-item tuple needs a trailing comma: `(7,)`. Parentheses alone do not make a tuple.
- Lists and tuples can contain each other. A tuple is immutable, but a mutable object stored inside it can still be changed.

**Predict / try**

```python
point = (4, 9)
x, y = point
print(x, y, point[1], point[:1])
```

**Cold check**

Which is a one-item tuple: `(7)` or `(7,)`? When should a tuple be chosen instead of a list? What can still change inside a tuple containing a list?

## Block 3.3 — Dictionaries

**Tiny theory**

- A dictionary maps unique, hashable keys to values. Create it with `{key: value}` or `dict()`.
- Read and update an item with `data[key]`; `.get(key)` can safely return a default for a missing key. Use `in` to test keys.
- `.keys()`, `.values()`, and `.items()` provide views for iteration. Add or update by assignment; `del` removes a key.
- Dictionary insertion order is preserved in modern Python, but a dictionary is accessed by keys, not numeric positions.

**Predict / try**

```python
person = {"name": "Ari", "age": 20}
person["age"] += 1
person["city"] = "Cape Town"
print(person.get("name"), "age" in person)
for key, value in person.items():
    print(key, value)
```

**Cold check**

How is a value retrieved from a dictionary? What happens when `person["email"]` is read if that key does not exist? How does `.get()` differ?

## Block 3.4 — Strings

**Tiny theory**

- A string is an immutable sequence of characters, written with single or double quotes. Triple quotes can span lines.
- Indexing and slicing work like they do for other sequences. `+` concatenates; `*` repeats; `in` tests for a substring.
- Escape sequences include `\n`, `\t`, and `\\`. Use a backslash or alternate quote style when a string contains quotes.
- Common methods include `.lower()`, `.upper()`, `.strip()`, `.find()`, `.replace()`, and `.split()`. Methods return results; strings are not changed in place.

**Predict / try**

```python
message = "  Python basics  "
print(message.strip().upper())
print("th" in message, message[2:8])
print("one,two".split(","))
```

**Cold check**

Why does `message.upper()` not change `message`? What does `\n` represent? What does the slice `word[1:4]` select?

**Block 3 mastery check:** Choose an appropriate collection, trace indexing and slicing, distinguish mutable from immutable objects, and process basic lists, tuples, dictionaries, and strings.

---

# Block 4 — Functions and Exceptions · 28%

## Block 4.1 — Define, call, and return from functions

**Tiny theory**

- `def` defines a function; calling it runs its body. Functions can make code reusable and divide a problem into smaller steps.
- `return` ends the call and sends a value back. A function with no explicit return produces `None`.
- Recursion is a function calling itself. Every recursive solution needs a base case.
- A generator function uses `yield` to produce values over time; calling it creates a generator iterator rather than immediately returning all yielded values. Generators are a way to define iterators without manually implementing the iterator protocol.

**Predict / try**

```python
def square(number):
    return number * number

def announce():
    print("Ready")

print(square(4))
result = announce()
print(result)
```

**Cold check**

Which function returns a value? What is `result`? Explain the base case in a recursive function. What does `yield` do differently from `return`?

## Block 4.2 — Parameters, arguments, and scope

**Tiny theory**

- A parameter is a name in a function definition; an argument is the value supplied when calling it.
- Positional arguments match by position. Keyword arguments match by name. Default values are used when an argument is omitted.
- A name assigned inside a function is local by default. Python looks for referenced names in local, enclosing, global, then built-in scopes (LEGB).
- A local name can shadow a name outside the function. `global` declares that an assignment targets a module-level name; it does not create a value by itself.

**Predict / try**

```python
rate = 2

def total(price, quantity=3):
    tax = 1
    return price * quantity * rate + tax

print(total(5), total(price=5, quantity=2))
```

**Cold check**

Identify the parameters and arguments. Which value is local? What result does the default produce? Explain how a local variable can shadow a global name.

## Block 4.3 — Built-in exception hierarchy

**Tiny theory**

- An exception represents an event that interrupts the normal flow of a program. Exceptions form a class hierarchy.
- `Exception` is the usual base for application errors. `ArithmeticError` includes arithmetic-related exceptions; `LookupError` includes `IndexError` and `KeyError`.
- Common errors include `TypeError` for an operation on an unsuitable type and `ValueError` when a value has the right type but an unsuitable form or content.
- `SystemExit` and `KeyboardInterrupt` are not ordinary `Exception` subclasses; broad handlers should not casually suppress them.

**Predict / try**

```python
examples = ["zero", "index", "key", "type", "value"]
print(examples[10])
```

Then change the final line to `int("not a number")` and compare the exception types.

**Cold check**

Match an invalid list index, missing dictionary key, unsupported operand types, and invalid integer text to their exception names. Where do `IndexError` and `KeyError` sit in the hierarchy?

## Block 4.4 — Handle and propagate exceptions

**Tiny theory**

- Put code that may fail in `try`; use `except` to handle specific exception types.
- Put more specific handlers before broader handlers, or a broad handler may catch the exception first.
- Exceptions can travel through function calls until a matching handler is found. Handle an error where the program has enough information to recover; otherwise let it propagate.
- `else` runs when the `try` suite succeeds; `finally` runs whether an exception occurred or not. The PCEP syllabus emphasizes `try`/`except`; recognize the related clauses as useful control flow.

**Predict / try**

```python
def read_count(text):
    return int(text)

try:
    count = read_count("12")
except ValueError:
    print("Please enter a whole number")
else:
    print(count)
finally:
    print("finished")
```

Change the input to `"twelve"` and observe which blocks run. Then put the conversion in a function and allow the caller to catch its `ValueError`.

**Cold check**

Which clause handles the invalid input? Which clauses run on success and failure? Why should `except ValueError` usually appear before `except Exception`? What does it mean for an exception to propagate across a function boundary?

**Block 4 mastery check:** Define and call small functions, trace arguments and scope, distinguish the syllabus exception types, and choose whether to handle or propagate an exception.

---

## 🧪 Final Practice Routine

1. Review the four blocks in proportion to their official weights; give extra time to control flow, the highest-weighted block.
2. Write small programs from a blank file: a number converter, a grade selector, a loop-based counter, a collection lookup, and a function with error handling.
3. Before running code, write down the expected output and explain the path Python will take.
4. Attempt the full mock exam without consulting its answer key. Mark uncertain answers as well as incorrect ones.
5. Review each missed or uncertain concept, practise it with a new example, and then retake the relevant questions.
6. Move on to PCAP after PCEP foundations are secure. Classes, inheritance, operator overloading, iterators, and the other advanced presentation sections belong to the PCAP course, not this PCEP sequence.

## 📚 Sources

- Primary teaching source: **PythonTutorial.pptx**, “Python for Beginners,” presented by Isaac, in the supplied Google Drive folder.
- Exam scope and domain weights: [Python Institute PCEP-30-02 Exam Syllabus](https://pythoninstitute.org/pcep-exam-syllabus).
