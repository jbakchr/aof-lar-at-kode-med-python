"""
Examples of set data structure
"""

# Example 1 - Creating a set with "curly brackets" and "set" constructor function
ex1 = {"apples", "bananas", "beers"}
ex2 = set(["apples", "bananas", "apples"])


# Example 2 - Get length of set
print(len(ex1))


# Example 3 - Getting the type for a "set" (will return "<class 'set'>")
print(type(ex1))


# Example 4 - Accessing elements is done by looping
for el in ex1:
  print(el)


# Example 5 - Adding elements to set
ex1.add("chips")



# Example 6 - Updating a set
ex3 = {"apples", "bananas", "pears"}
ex4 = {"beers", "wine", "more alcohol"}

ex3.update(ex4)
print(ex3)

# Example 7 - Removing an element by use of the "remove" and "discard" method
ex3.remove("apples")
print(f"Apples removed from set: {ex3}")

ex3.discard("bananas")
print(f"Bananas removed by discard method: {ex3}")


# Example 8 - Removing a random element by the "pop" method
ex3.pop()
print(f"Remaining set: {ex3}")