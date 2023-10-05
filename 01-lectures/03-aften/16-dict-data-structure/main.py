"""
Examples of creating and using Pythons "dict" data structure
"""

# Example 1 - Creating a dict
me = {
  "first_name": "Jonas",
  "last_name": "Phillipson",
  "age": 41,
  "fav_food": ["Lasagna", "Risotto", "fruit pie"]
}
print(me)


# Example 2 - Accessing a value by key name in dict using bracket notation
print(me["age"])


# Example 3 - Accessing a value with the "get" method
print(me.get("fav_food"))


# Example 4 - Changing the value by referencing the key
me["age"] = 87
print(me)


# Example 5 - Changing/Updating a value with the "update" method
me.update({"last_name": "Mogensen"})
print(me)