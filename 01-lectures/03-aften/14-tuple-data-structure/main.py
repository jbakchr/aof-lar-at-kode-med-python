"""
Examples of using Pythons "tuple" data structure
"""

# Example 1 - creating a tuple
tpl = ("apple", "banana", "beer", "mango", "whiskey", "red wine")


# Example 2 - accessing an item with positive index
print(tpl[1])


# Example 3 - accessing item with negative index
print(tpl[-1])


# Example 4 - getting range of items
print(tpl[0:3])


# Example 5 - looping through tuple
for item in tpl:
  print(item)