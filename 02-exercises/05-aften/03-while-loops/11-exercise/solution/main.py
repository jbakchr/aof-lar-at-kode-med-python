"""
Exercise 11

Given the below list create a while loop that loops and prints each element
provided the element is not "beer" 
"""
shopping_list = ["butter", "milk", "beer", "chicken", "other stuff.."]

i = 0
while i < len(shopping_list):
  item = shopping_list[i]
  if item == "beer":
    i += 1
    continue
  print(item)
  i += 1