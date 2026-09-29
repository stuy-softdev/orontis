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
### 2.1 Variables & Types ✅
- [ ] `int`, `float`, `str`, `bool`, `None`
    - Definition: Basic kinds of values in Python. A float is like a double from Java.
    - Example: 'age = 17', 'price = 2.58', 'name = Gregory', 'hasCancer = true', 'x = None'
    - Gotcha: "5" is a str, not an int
- [ ] `type()`, `isinstance()`
    - Definition: type() tells you what something is; isinstance() checks if it's a certain type and returns true or false
    - Example: type(5) gives 'int', isinstance(5, int) gives true
    - Gotcha: type() returns the type, while isinstance() returns true or false
- [ ] Type conversion: `int()`, `str()`, `float()`
    - Definition: Converts a value from one type to another. Like casting in Java
    - Example: 'int("5")' gives 5, 'str(5)' gives "5"
    - Gotcha: Not every value can be converted like 'int("Gregory")'

### 2.2 Strings 🟨
- [ ] f-strings
- [ ] Common methods: `.strip()`, `.split()`, `.join()`, `.lower()`, `.replace()`, `.startswith()`
- [ ] Slicing
- [ ] Multiline strings (`"""`)

### 2.3 Operators
- [ ] Comparison: `==`, `!=`, `<`, `>`
- [ ] Logical: `and`, `or`, `not`
- [ ] Identity/membership: `is`, `is not`, `in`, `not in`
- [ ] `==` vs `is`

## 3. Control Flow
- [ ] `if` / `elif` / `else`
- [ ] `for` loops, `range()`, `enumerate()`, `zip()`
- [ ] `while`, `break`, `continue`
- [ ] `pass`
- [ ] Ternary expression: `x if cond else y`

## 4. Data Structures
| Structure | Literal | Key methods | Web-dev use case |
|-----------|---------|-------------|------------------|
| `list` | `[]` | `.append()`, `.pop()`, `.sort()` | Rows from a query |
| `dict` | `{}` | `.get()`, `.items()`, `.update()` | Form data, JSON |

- [ ] Comprehensions (list, dict, set)
- [ ] Unpacking (`a, b = ...`, `*args`)
- [ ] Sorting: `sorted()`, `key=`, `reverse=`
- [ ] Mutability and copying (`.copy()`, `copy.deepcopy`)

## 5. Functions & Structure
- [ ] `def`, `return`, default args, keyword args
- [ ] Docstrings
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

### oustanding QUESTIONS
- Q: What is the answer to life, the universe, and everything?
- Q: Is "gatekeeping" inherently bad?
- Q: Is is an A or B day?
- Q: Will this be on the test?
