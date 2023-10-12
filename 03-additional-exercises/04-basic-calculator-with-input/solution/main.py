"""
SOLUTION TO ADDITIONAL EXERCISE

This exercise builds on top of the "03-basic-calculator" exercise.

And so, in this exercise you'll just need to ask the user for both
the two integers and operator that'll be supplied to your calculator.

* HINT *
- use Pythons built-in "input" function to ask the user for integers
  and operator to use
- remember to type cast the numbers provided to the input function
"""

def calculator(num1, num2, op):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  else:
    return num1 / num2
  
x = int(input("Number for calculator: "))
y = int(input("Number for calculator: "))
op = input("Operator to use (+, -, *, /): ")

result = calculator(x, y, op)
print(result)