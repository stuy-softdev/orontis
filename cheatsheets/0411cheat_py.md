# SoftDev Cheat Sheet: Python3 Preliminaries

> Devo: LEON WONG
> Last updated: 2026-09-28
> Collaborators: Leon Wong

## USAGE:
- For each entry: write a 1-line working definition (simplest colloquial English possible), a minimal example, and a "gotcha."
- Mark status: ⬜ not started · 🟨 in progress · ✅ done

---

## 1. Environment & Tooling
| Item | Status | Notes |
|------|--------|-------|
| `python3 --version` | ✅ | Definition: Shows installed Python 3 version. Example: 'python3 --version' --> Python 3.13.7. Gotcha: Some computers use python --version instead of python3 |

## 2. Core Syntax
### 2.1 Variables & Types 
- [✅] `int`, `float`, `str`, `bool`, `None`
    - Definition: Basic kinds of values in Python. A float is like a double from Java.
    - Example: 'age = 17', 'price = 2.58', 'name = Gregory', 'hasCancer = true', 'x = None'
    - Gotcha: "5" is a str, not an int
- [✅ ] `type()`, `isinstance()`
    - Definition: type() tells you what something is; isinstance() checks if it's a certain type and returns true or false
    - Example: type(5) gives 'int', isinstance(5, int) gives true
    - Gotcha: type() returns the type, while isinstance() returns true or false
- [✅ ] Type conversion: `int()`, `str()`, `float()`
    - Definition: Converts a value from one type to another. Like casting in Java
    - Example: 'int("5")' gives 5, 'str(5)' gives "5"
    - Gotcha: Not every value can be converted like 'int("Gregory")'

### 2.2 Strings 
- [✅ ] f-strings
    - Definition: Lets you put variables directly inside a string.
    - Example: 'name = "Bob"; print(f"Hello {name}")
    - Gotcha: Ya need to put 'f' before the quotation marks
- [✅ ] Common methods: `.strip()`, `.split()`, `.join()`, `.lower()`, `.replace()`, `.startswith()`
    - Definition: Methods for changing / checking strings
    - Example: " hello ".strip() gives "hello" and "a,b,c".split(",") gives ["a", "b", "c"]
    - Gotcha: Most string methods return a new string instead of changing the original
- [✅ ] Slicing
    - Definition: Gets part of a string using indeces. Starts before the first index and ends before the second
    - Example: "gagaw"[1:3] gives "ag"
    - Gotcha: Ending index is NOT included.
- [✅ ] Multiline strings (`"""`)
    - Definition: Allows for strings across multiple lines.
    - Example: """Gregory
    is great"""
    - Gotcha: Need matching triple quotes at the beginning and end

### 2.3 Operators
- [✅ ] Comparison: `==`, `!=`, `<`, `>`
    - Definition: Compares two values and returns a boolean
    - Example: 5 > 3 gives True
    - Gotcha: = is not an operator, it assigns a value
- [✅ ] Logical: `and`, `or`, `not`
    - Definition: Combines / reverses booleans
    - Example: '5 > 3 and 2 < 4' gives True
    - Gotcha: and requires both conditions, or requires one
- [✅ ] Identity/membership: `is`, `is not`, `in`, `not in`
    - Def: 'is' checks whether two references point to the same object, 'in' checks whether something is contained within something else
    - Example: "a" in "cat" gives True
    - Gotcha: 'is' shouldn't usually be used to compare normal values
- [✅ ] `==` vs `is`
    - Definition: == checks if values are equal, is checks if they're exactly the same object
    - Example: [1, 2] == [1, 2] gives True
    - Gotcha: Two objects can have equal values w/o being the same object

## 3. Control Flow
- [✅ ] `if` / `elif` / `else`
    - Definition: Conditionals - Runs different code depending on whether conditions are true or false
    - Example: 'if x > 0: print("this number is positive")'
    - Gotcha: Indentation matters
- [✅ ] `for` loops, `range()`, `enumerate()`, `zip()`
    - Definition: Repeats code over a group of values
    - Example: for i in range(12): print(i)
    - Gotcha: range(3) gives 0, 1, 2 and not 0, 1, 2, 3
- [✅ ] `while`, `break`, `continue`
    - Definition: while repeats while a condition is true, break breaks a loop, continue skips to the next loop
    - Example: while x < 5: x += 1
    - Gotcha: A while loop can run forever if condition stays true
- [✅ ] `pass`
    - Definition: Literally does nothing. A placeholder
    - Example: if x > 2: pass
    - Gotcha: It literally does nothing. 
- [✅ ] Ternary expression: `x if cond else y`
    - Definition: Short way to write an if/else
    - Example: 'result = "yes" if x > 2 else "greg"'
    - Gotcha: The cond goes in the middle (might look confusing)

## 4. Data Structures
| Structure | Literal | Key methods | Web-dev use case |
|-----------|---------|-------------|------------------|
| `list` | `[]` | `.append()`, `.pop()`, `.sort()` | Rows from a query | ✅
   - Definition: Ordered, changeable collection of values
   - Example: numbers = [0, 1, 2]
   - Gotcha: Index starts at 0 and not 1
| `dict` | `{}` | `.get()`, `.items()`, `.update()` | Form data, JSON | ✅
   - Definition: Stores data as key-value pairs
   - Example: man = {"name": "Gregory", "age": 104}
   - Gotcha: Keys must be unique

- [✅ ] Comprehensions (list, dict, set)
    - Definition: Short way to build a new collection (collections are things that store more things inside the thing, like list, dict, tuple) using a loop
    - Example: [x * 2 for x in range(5)]
    - Gotcha: Makes a new collection instead of changing the original
- [✅ ] Unpacking (`a, b = ...`, `*args`)
    - Definition: Splits values from a collection to separate values
    - Example: 'a, b = [10, 20]'
    - Gotcha: Number of variables has to match number of values
- [✅ ] Sorting: `sorted()`, `key=`, `reverse=`
    - Definition: Puts values into an order. sorted() returns a new sorted list, key tells what part of every value to sort by, reverse=True sorts in descending order
    - Example: 'sorted(["Gregory", "greg"], key=len)' gives '["greg", "Gregory"]'
    - Gotcha: .sort() changes the actual list but sorted() makes a new one
- [✅ ] Mutability and copying (`.copy()`, `copy.deepcopy`)
    - Definition: Creates another object so original remains intact / unchanged
    - Example: 'anunoby = [2, 4, 194]
                copy = anunoby.copy()
                copy.append(8494)'
                gives a copied list [2, 4, 194, 8494]
    - Gotcha: copy.deepcopy() makes separate copies of nested objects

NOTE: I'm getting tired of writing words like DEFINITION and EXAMPLE and GOTCHA so i'm gonna abbreviate it D E G from now on


## 5. Functions & Structure
- [ ] `def`, `return`, default args, keyword args
    - Definition: Def defines a function, return designates the value the function returns
    - Example: 'def Gregory():
        print("I love Gregory more than I love greg")
    - Gotcha: return doesn't print anything, it just has the function return a value
- [ ] Docstrings
    - Definition: Descriptions in the form of big comments for how code works
    - Example: '''This code prints a messsage'''
    - Gotcha: Can be declared using ''' or """
- [ ] Type hints (`def f(x: int) -> str:`)
- [ ] `lambda`
- [ ] Modules and `import` / `from ... import ...`
- [ ] `if __name__ == "__main__":`

## 6. Classes & Objects (as needed)

## 7. Errors, Files & Resources
### 7.1 Exceptions
- [ ] `try` / `except` / `else` / `finally`
- [ ] Common exceptions: `ValueError`, `KeyError`, `TypeError`, `FileNotFoundError`

### 7.2 Context Managers
- [ ] `with` statement

### 7.3 Files & Paths
#### Basics
- [ ] `open()` and the `encoding` argument (modes)
- [ ] File modes: `r`, `w`, `a`, `x`, `b`
- [ ] `pathlib.Path`
- [ ] `with open(...) as f:`
- [ ] Reading: `.read()`, `.readline()`, `.readlines()`
- [ ] Writing: `.write()`, `.writelines()`
- [ ] Gotcha:  ?

#### Paths (`pathlib`)
- [ ] `Path`, `Path(__file__).parent`
- [ ] Joining paths with `/`
- [ ] `.exists()`, `.is_file()`, `.mkdir()`
- [ ] `.read_text()`, `.write_text()`
- [ ] Gotcha: ?

#### CSV
- [ ] `import csv`; the `newline=""` argument
- [ ] `csv.reader`
- [ ] `csv.DictReader` and `.fieldnames`
- [ ] `csv.writer` and `csv.DictWriter`: `.writeheader()`, `.writerow()`, `.writerows()`
- [ ] Type conversion of CSV values
- [ ] `delimiter=` for non-comma files
- [ ] Gotcha: ?

#### File Errors
- [ ] `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError`
- [ ] `csv.Error`
- [ ] `KeyError` from a missing `DictReader` column

## 10. Standard Library Highlights
- [ ] `os`, `sys`
- [ ] `datetime` (and timezone handling)

## 11. Debugging & Testing
- [ ] Reading tracebacks

## 12. Style & Best Practices
- [ ] PEP 8
- [ ] Naming conventions
- [ ] Keep secrets out of version control

## 14. Q/C/C and the Disco Holding Pen
### Gotchas I've found:
- ...but cannot necessarily yet explain/categorize/address:

### Links
- [displaytext](url)

### DISCOVERIES
- ...I've made but have not yet fully explained/categorized
- \ lets you skip lines, but is hard to search for

### oustanding QUESTIONS
- Q: What is the answer to life, the universe, and everything?
- Q: Is "gatekeeping" inherently bad?
- Q: Is is an A or B day?
- Q: Will this be on the test?
