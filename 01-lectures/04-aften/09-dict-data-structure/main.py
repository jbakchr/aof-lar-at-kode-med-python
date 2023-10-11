"""
Examples of the Python "dict" data structure
"""

# Example 1 - Creating a dict
ex1 = {"name": "Jonas", "age": 41, "likes": ["Bad Omens", "The Prodigy", "Pink Floyd"]}
my_dict = dict(name = "Guido", age = 99, likes = ["Python", "Being a Dictator"])


# Example 2 - Duplicates not allowed
car = {"brand": "Volvo", "speed": 250, "prod_year": 2000, "prod_year": 2012}
print(car)


# Example 3 - Getting length of dict
print(len(car))


# Example 4 - the type of a dict is "<class 'dict'>"
print(type(car))


# Example 5 - Accessing a value in dict by "bracket notation" with key name
print(my_dict["name"])


# Example 6 - Accessing a value through use of the "get" method
print(my_dict.get("age"))


# Example 7 - Getting all keys from a dict
keys = ex1.keys()
print(keys)


# Example 8 - Getting all values from a dict
values = ex1.values()
print(values)


# Example 9 - Getting both all key and value pair
items = ex1.items()
print(items)


# Example 10 - Checking if key exists in dict
if "brand" in car:
  print("It's a Volvo!")


# Example 11 - Changing a value in dict by bracket notation and the update
car["speed"] = 900
car.update({"prod_year": 2022})
print(car)


# Example 12 - Adding an item to a dict by bracket notation and the "update" method
car["color"] = "Yellow"
car.update({"horse_power": 400})
print(car)


# Example 13 - Remove a key/value from  dict
car.pop("color")
print(car)


# Example 14 - Removing last inserted item
car.popitem()
print(car)
