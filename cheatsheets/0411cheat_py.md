# SoftDev Cheat Sheet: Python3 Preliminaries

> Devo: LEON WONG
> Last updated: 2026-09-28
> Collaborators: Andrew Zhao, Ivan Zheng

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

## 5. Functions & Structure
- [✅] `def`, `return`, default args, keyword args
- Definition: def defines a function, return ends a function
- Example: def one(): return 1
- Gotcha: return ends the function
- [✅] Docstrings
- Definition: special strings used to document code, provide a description
- Example """Hi"""
- Gotcha: this works because python ignores undefined strings
- [🟨] Type hints (`def f(x: int) -> str:`)
- Definition: specifys what type of variable you are inputting, and also describes what it return as.
- Example: def one(x: int) -> str: return str(1)
- Gotcha:
- [✅] `lambda`
- Definition: creates small anonymous functions
- Example: x = lambda a: a+16
- Gotcha: can take any number of arguments but can only have one expression
- [✅] Modules and `import` / `from ... import ...`
- Definition: adds additional definitions and statements.
- Example: import csv
- Gotcha: you need to use module functions like this: module_name.function_name
- [🟨] `if __name__ == "__main__":`
- Definition: Allows anything under the if statement to be run if the file is run directly.
- Example: if __name__ == "__main__"
- Gotcha:
## 6. Classes & Objects (as needed)

## 7. Errors, Files & Resources
### 7.1 Exceptions
- [✅] `try` / `except` / `else` / `finally`
- Definition: an exception to an if statement
- Example: if (value1 == true): else: 
- gotcha: doesn't run if the statements before run true.
- [✅] Common exceptions: `ValueError`, `KeyError`, `TypeError`, `FileNotFoundError`
- Definition: common errors you recieve if you are referring to something that doesn't exist.
- Example: calling file if file isnt established already.
- Gotcha: sometimes your names are just misspelled by a letter.

### 7.2 Context Managers
- [✅] `with` statement
- Definition: ensures the file is closed safely after being used with with
- Example: with open("handles_w_quackers.csv") as file:
- Gotcha: 
### 7.3 Files & Paths
#### Basics
- [✅] `open()` and the `encoding` argument (modes)
- Definition: opens up a file in the local directory
- example: open("handles_w_quackers.csv")
- Gotcha: remains open until a close() call
- [✅] File modes: `r`, `w`, `a`, `x`, `b`
- Definition: set modes in how to utilize this file.
- Example: with open("handles_w_quackers.csv", "w") as file:
- Gotcha: opening a file with w erases existing data
- [⬜] `pathlib.Path`
- [✅] `with open(...) as f:`
- definition: opens a file and assigns it a variable.
- example: with open("handles_w_quackers.csv") as csv:
- gotcha: if file doesnt exist, error.
- [✅] Reading: `.read()`, `.readline()`, `.readlines()`
- Definition: reads the file
- Example: read(open("handles_w_quackers.csv"))
- Gotcha: if you run it twice, it returns an empty string.
- [⬜] Writing: `.write()`, `.writelines()`
- [✅] Gotcha: if you arent using with() you need a close() call

#### Paths (`pathlib`)
- [⬜] `Path`, `Path(__file__).parent`
- [⬜] Joining paths with `/`
- [✅] `.exists()`, `.is_file()`, `.mkdir()`
- Definition: checks if files or directories exist
- example: if file_path.exists():
- gotcha: is_file() returns false if the file doesnt exist
- [⬜] `.read_text()`, `.write_text()`
- [⬜] Gotcha: ?

#### CSV
- [✅] `import csv`; the `newline=""` argument
- definition: imports csv functions
- example: import csv
- gotcha: 
- [✅] `csv.reader`
- [✅] `csv.DictReader` and `.fieldnames`
- definition: reads the given csv as a dictionary.
- example: reader = csv.DictReader(csvfile)
- gotcha: if the csv doesn't exist, returns an error.
- [⬜] `csv.writer` and `csv.DictWriter`: `.writeheader()`, `.writerow()`, `.writerows()`
- [⬜] Type conversion of CSV values
- [⬜] `delimiter=` for non-comma files
- [⬜] Gotcha: ?

#### File Errors
- [⬜] `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError`
- [⬜] `csv.Error`
- [⬜] `KeyError` from a missing `DictReader` column

## 10. Standard Library Highlights
- [⬜] `os`, `sys`
- [⬜] `datetime` (and timezone handling)

## 11. Debugging & Testing
- [⬜] Reading tracebacks

## 12. Style & Best Practices
- [⬜] PEP 8
- [⬜] Naming conventions
- [⬜] Keep secrets out of version control

## 14. Q/C/C and the Disco Holding Pen
### Gotchas I've found:
- ...but cannot necessarily yet explain/categorize/address:

### Links
- [displaytext](url)

### DISCOVERIES
- ...I've made but have not yet fully explained/categorized
- \ lets you skip white space in python
### oustanding QUESTIONS
- Q: What is the answer to life, the universe, and everything?
- Q: Is "gatekeeping" inherently bad?
- Q: Is is an A or B day?
- Q: Will this be on the test?
