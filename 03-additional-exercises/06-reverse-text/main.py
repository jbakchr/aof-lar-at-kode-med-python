"""
ADDITIONAL EXERCISE

In this exercise you are to create a function that takes in some string and
return the reversed version of it.

One way to complete the exercise is to use a list containing each character
of the provided text in reverse and return it as string using the string "join"
method.

* HINT * 
check this link for use of the string "join" method: https://www.w3schools.com/python/ref_string_join.asp
"""

def reverser(txt):
  reversed_text = []

  for char in txt:
    reversed_text.insert(0, char)
  
  return "".join(reversed_text)

print(reverser("Jonas"))