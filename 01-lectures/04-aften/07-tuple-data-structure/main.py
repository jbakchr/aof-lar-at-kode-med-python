"""
Examples of Pythons tuple data structure
"""

# Example 1 - how to create a tuple with parenthesis and the tuple constructor function
my_tuple = ("apple", "banana", "beer", "pears", "chips", "cheese")
print(my_tuple)

my_second_tuple = ("Jonas", 41, True, ["cheese", "cake", 42])
print(my_second_tuple)


# Example 2 - when creating a tuple with only 1 element one needs to put a comma at the end
my_third_tuple = ("WTF",)
print(my_third_tuple)


# Example 3 - Getting length of tuple
print(f"Length of 'my_tuple': {len(my_tuple)}")


# Example 4 - Getting the "type" of a tuple will yield "<class 'tuple'>"
print(type(my_tuple))


# Example 5 - Accessing single elements and ranges of elements by bracket notation
print(f"Second element is: {my_tuple[1]}")
print(f"Second last element: {my_tuple[-2]}")
print(f"First two elements are: {my_tuple[0:2]}")


# Example 5 - Checking if item is in tuple
if "beer" in my_tuple:
  print("Beer is awesome!")


# Example 6 - How update a tuple (since the original cannot be changed)
change_tuple = ("apple", "pears", "beers") # Original tuple
change_to_list = list(change_tuple) # Change tuple to list with "list" constructor
change_to_list[0] = "cheese" # Change an element by bracket notation - here element at index 0
change_tuple = tuple(change_to_list) # Create new tuple and assign it back to original variable


# Example 7 - Unpack a tuple
groceries = ("apples", "bananas", "pears")

(x, y, z) = groceries
print(x, y, z)



