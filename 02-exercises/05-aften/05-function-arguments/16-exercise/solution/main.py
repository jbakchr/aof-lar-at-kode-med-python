"""
Exercise 16

Create a function with the below arguments in the mentioned order and call the function
using keyword arguments in reverse order:
- age
- name
"""

def say_hello(age, name):
  print(f"Hi, my name is {name} and I'm {age} old.")


say_hello(name="Jonas", age=41)