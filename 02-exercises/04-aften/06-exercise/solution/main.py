"""
EXERCISE

In this exercise you are to create a function that'll count the number of odd numbers from a tuple.

To complete this exercise, please do the following:
- 1) Create a tuple with the numbers from 1 to 5
- 2) Create a function that'll return the amount of odd numbers from your tuple
"""

def odds(tpl):
  count = 0
  for i in tpl:
    if i % 2 != 0:
      count += 1
  return count

numbers = (1, 2, 3, 4, 5)

print(odds(numbers))
