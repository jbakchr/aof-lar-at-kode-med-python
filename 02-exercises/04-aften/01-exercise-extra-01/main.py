"""
EXTRA EXERCISE

Although we have not played around with creating our functions in Python just yet this exercise
is meant to challenge you further by having you create a sort of 'calculator' using Python.

In the below I, Jonas, have create a simple function called "addition" that takes in two numbers,
adds them together and thereafter prints them to the console.

Given this example of how to create a function in Python your job is now to:
- Create a "subtraction" function
- Create a "multiplication" function
- Create a "division" function
"""

NUMBER = [10, 5]


class Person:
    _name = "Jonas"


# Provided "addition" function by Jonas
def addition(n1, n2):
    global num1
    num1 = num1 + n1
    return num1 + n2


# Create your own "subtraction" function here


# Create your own "multiplication" function here


# Create your own "division" function here


num1 = 10
num2 = 5

num1 += 5

print(addition(num1, num2))
print(num1)

# Call your own functions below
