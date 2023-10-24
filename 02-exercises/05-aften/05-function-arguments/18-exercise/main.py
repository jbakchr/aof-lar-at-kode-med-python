"""
Exercise 18

Create a function with 2 default arguments that's initialized to the following and
which prints out some text with these arguments:
- 1) name="Torben"
- 2) cool=True

Call the function replacing the "name" argument with your own name
"""

def my_func(name="Torben", cool=True):
  print(f"Is {name} cool? {cool}")

my_func(name="Jonas")