"""
Examples of string in Python
"""

# EXAMPLE 1 - The regular string we know by now (single quotes around the string would work too)
name_with_double_quotes = "Jonas"
name_with_single_quotes = 'Sir Lancelot'


# EXAMPLE 2 - Multiline string
txt = """This is
a multiline
string"""
print(txt)


# EXAMPLE 3 - Accessing a character from a string by using "bracket notation" []
the_dictator = "Guido van Rossum"

print(the_dictator[0])  # will print the capital letter "G"
print(the_dictator[5])  # will print the first whitespace
print(the_dictator[-1]) # will print the last character "m"

print(the_dictator[1:5])


# EXAMPLE 4 - Looping through a string
quote = "Python"

for i in quote:
  print(i)


# EXAMPLE 5 - Check a string for a string
text_to_check = "Jonas is a programming god"

if "god" in text_to_check:
  print("It must be true then!")