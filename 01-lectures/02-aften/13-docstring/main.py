"""
Module level docstring
"""

def square(n):
  """
  Function level docstring
  Takes in a number n, returns the square of n
  """
  return n**2

class Person:
  """
  Class level docstring
  This Person class is super duper awesome!
  """
  def __init__(self, name):
    self.name = name
  
  def print_name(self):
    print(self.name)

# Hover over 'square' function to show docstring
print(square(2))

# Hover over 'Person' class constructor and 'print_name' function to show docstring
p = Person("Jonas")
p.print_name()
