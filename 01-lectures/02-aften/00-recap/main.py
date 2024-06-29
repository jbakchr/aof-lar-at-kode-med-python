"""
Recap from first night lecture:

- 1) Print something with the "print" function - use both double and single quotes
- 2) Clear the terminal
- 3) Break your code, run it again and try to understand the error message (Google it!)
- 4) Fix your code
- 5) Learn to look up stuff in the Python documentation https://www.python.org/
"""

# Double quotes
print("Hello world in double quotes!")

# Single quotes
print("Single quotes work too")

# Print with multiple objects and 'keyword arguments'
print("Hej", "med", "dig", sep="-", end="----ost")


# We alse looked at the built-in 'input' function and could look at others ('len')
name = input("Hvad er dit navn? ")
print("Længden af dit navn er", len(name))
