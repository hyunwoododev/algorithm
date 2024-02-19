# Python String Helpers


### String Validation
- [`.islanum()`](https://www.w3schools.com/python/ref_string_isalnum.asp)
    - Check if all the characters in the text are alphanumeric


### String Manipulation
- `.strip()`
    - The string method .strip() can be used to remove characters from the beginning and end of a string.
    - A string argument can be passed to the method, specifying the set of characters to be stripped. With no arguments to the method, whitespace is removed.

```python
    text1 = '   apples and oranges   '
    text1.strip()       # => 'apples and oranges'

    text2 = '...+...lemons and limes...-...'

    # Here we strip just the "." characters
    text2.strip('.')    # => '+...lemons and limes...-'

    # Here we strip both "." and "+" characters
    text2.strip('.+')   # => 'lemons and limes...-'

    # Here we strip ".", "+", and "-" characters
    text2.strip('.+-')  # => 'lemons and limes'
```

- `.split()`
    - The string method .split() splits a string into a list of items:
    - If no argument is passed, the default behavior is to split on whitespace.
    - If an argument is passed to the method, that value is used as the delimiter on which to split the string.

```python
    text = "Silicon Valley"

    print(text.split())     
    # Prints: ['Silicon', 'Valley']

    print(text.split('i'))  
    # Prints: ['S', 'l', 'con Valley']
```