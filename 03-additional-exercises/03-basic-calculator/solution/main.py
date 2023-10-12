"""
SOLUTION TO ADDITIONAL EXERCISE

In this exercise you are to create a function that'll act as a calculator
when given two numbers and the operator to use.

For now we'll just stick with the "+", "-", "*" and "/" operator

To complete this exercise you should therefor:
- 1)  Create two variables and assign them the integers you want
- 2)  Create a variable called "op" and assign it a string of either "+", "-", "*" or "/"
- 3)  Create a function named "calculator" that should be given 3 parameters named "num1", "num2" and "op"
- 4)  Make the function use the if, elif and else control structures like this:
      - 4.1) if the functions "op" parameter is equal to "+" then return the addition of num1 and num2
      - 4.2) elif the functions "op" parameter is equal to "-" then return the subtraction of num1 and num2
      - 4.3) elif the functions "op" parameter is equal to "*" then return the multiplication of num1 and num2
      - 4.4) else return the division of num1 and num2
- 5) Call your calculator function and prints it's result to the terminal
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
  
x = 5
y = 2
op = "*"

result = calculator(x, y, op)
print(result)