# PLP Python Week 6 Assignment: Error Handling with Try/Except

## File Descriptions
* **safe_tools.py**: Contains functions that safely handle division, string-to-integer conversion, and dictionary lookups without crashing.
* **unbreakable.py**: An interactive script that runs continuously in a loop, catching invalid numeric inputs safely.

## Reflection Question
**Why can the if check not catch "abc" on its own?**
An `if` statement is designed to check existing conditional values or states, but it cannot foresee or stop structural data type failures before they happen. When you pass a string filled with letters like `"abc"` into the `int()` function, Python attempts a structural conversion that fundamentally fails at the interpreter level, throwing a `ValueError`. An `if` statement cannot intercept or prevent that data-type crash on its own; it requires a `try/except` block to catch the exception and keep the application running.

