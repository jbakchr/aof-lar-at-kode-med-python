"""
SOLUTION EXTRA EXERCISE

Given that we at least have some experience with looping through lists and text
you should be able to understand looping by use of Pythons "range" function.

In this exercise your task is to complete the below range loop adding each
number from each iteration to the "sum" variable above the loop.

And after having completed this you should just print out the sum using Pythons
"f-string" in any way you'd like.
"""

sum = 0

for i in range(1, 10):
  # continiously add and assign the value of "i" to the "sum" variable
  sum += i

print(f"Sum is: {sum}")