"""
Module level docstring
"""


def square(heltal: int):
    """
    Function level docstring
    Takes in a number n, returns the square of n
    """
    return heltal**2


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
print(square("Jonas"))

# Hover over 'Person' class constructor and 'print_name' function to show docstring
p = Person("Jonas")
p.print_name()
