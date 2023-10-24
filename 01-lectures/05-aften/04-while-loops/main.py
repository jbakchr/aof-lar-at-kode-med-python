"""
Examples of while loops
"""

# Example 1 - while loop with variable for condition
num1 = 1
while num1 <= 5:
  print(num1)
  num1 += 1


# Example 2 - while loop with break statement
num2 = 1
while num2 <= 5:
  if num2 == 3:
    break
  print(num2)
  num2 += 1


# Example 3 - while loop with continue statement
num3 = 6
while num3 > 1:
  num3 -= 1
  if num3 == 3:
    continue
  print(num3)


# Example 4 - while loop with else statement
num4 = 5
while num4 >= 1:
  print(num4)
  num4 -= 1
else:
  print("While loop done!")