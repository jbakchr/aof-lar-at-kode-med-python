"""
SOLUTION TO ADDITIONAL EXERCISE

Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 * 4 * 3 * 2 * 1 = 120
Expected output:

120
"""


def factorial(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac


print(factorial(5))
