"""
Solution to exercise 5

Given the below list loop through the list printing each element but breaking the
loop if the list contains the word "beer"
"""
groceries = ["apples", "bananas", "beer", "cheese", "salad"]

for item in groceries:
  if item == "beer":
    break
  print(item)