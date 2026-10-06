# A common attempt to use an if check to filter non-numeric strings
def format_input_with_if(text):
    # Checking .isdigit() misses negative numbers, floats, or mixed characters like "12a"
    if text.isdigit():
        return int(text)
    else:
        return "Not a valid integer via IF check"

# The robust approach using try/except
def format_input_with_try(text):
    try:
        return int(text)
    except ValueError:
        return "Handled safely via EXCEPT"

# Testing both approaches
print("Testing 'abc':")
print(format_input_with_if("abc"))
print(format_input_with_try("abc"))
