# PLP Python Week 6 - Exception Handling Assignment

## File Descriptions
* `safe_tools.py`: Contains utility functions designed to catch runtime errors (division by zero, value parsing, and missing dictionary keys) safely using try/except blocks.
* `unbreakable.py`: Demonstrates the functional difference and edge-case limitations between manual conditional validation (`if` statements) versus structural exception handling.

## Reflection Question Response
An `if` statement cannot catch a string like `"abc"` on its own because looking for specific string patterns (like checking `.isdigit()`) fails to account for structural data mutations or diverse invalid formats. Using `try/except` allows Python to attempt the operation directly and gracefully catch the exact `ValueError` at runtime, rather than requiring complex validation rules for every possible bad input format.
