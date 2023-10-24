"""
Exercise 17

Create a function with an arbitary number of keyword arguments and print
each one
"""

def print_data(**kwargs):
  for k, v in kwargs.items():
    print(f"{k}:\t {v}")


print_data(name="Jonas", age=41, city="Ballerup", cool=True)