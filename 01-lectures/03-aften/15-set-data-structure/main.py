"""
Examples of using Pythons "set" data structure
"""

# Example 1 - creating a set
bands = {"The Beatles", "Madonna", "Cher", "Slipknot", "KISS"}
print(bands)


# Example 2 - creating a set with duplicate items
food = {"apples", "oranges", "apples"}
print(food)


# Example 3 - adding an item
food.add("melon")
print(food)


# Example 4 - Removing an item
food.remove("apples")
print(food)


# Example 5 - looping through a set
for item in food:
  print(item)