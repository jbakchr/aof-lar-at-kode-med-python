"""
Examples of string formatting
"""

# Example 1 - formatting strings witout indexes
character = "knights"
who_say = "Ni!"
sentence = "We are the {} who say: {}"

print(sentence.format(character, who_say))


# Example 2 - formatting strings with indexes
person = "Guido van Rossum"
title = "Dictator"
txt = "Who is the {1} of Python? Answer: {0}"

print(txt.format(person, title))


# Example 3 - formatting strings with "f-strings"
first_name = "Jonas"
middle_name = "Bak"
last_name = "Phillipson"

print(f"{first_name} {middle_name} {last_name}")