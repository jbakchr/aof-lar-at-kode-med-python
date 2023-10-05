"""
SOLUTION TO EXTRA EXERCISE

In this exercise you are to create an empty shopping list, add 3 items to by 
use of the "input" function that we haven't used before and lastly print
each item in the shopping list to the terminal

To complete the exercise you should therefore follow these steps:

- 1) Create a variable called "shopping_list" and assign it an empty list

- 2) Use the range function to create a loop that'll do something 3 times
- 3) Within this loop create a variable called "item" and assign it result of an input function
- 4) Append the "item" variable to the "shopping_list"

- 5) Loop through the shopping list printing one element on each iteration
"""

shopping_list = []

for i in range(3):
  item = input("Add item to shopping list: ")
  shopping_list.append(item)

for item in shopping_list:
  print(item)