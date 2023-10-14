"""
SOLUTION TO ADDITIONAL EXERCISE

Return multiple values from a function

Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

Given:

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)

Expected Output:

50, 30
"""


def calculation(num1, num2):
    return f"{num1 + num2}, {num1 - num2}"


print(calculation(40, 10))
