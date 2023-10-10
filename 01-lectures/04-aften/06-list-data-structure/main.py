"""
Examples of Python lists and how to process them
"""

# Example 1 - how to create a list
my_list = ["apple", "banana", "beer", "chips", "coca cola"]
print(f"Entire list: {my_list}")


# Example 2 - how to access an element in a list
first_element = my_list[0]
print(f"Accessing first element: {first_element}")


# Example 3 - access element using a negative index
last_element = my_list[-1]
print(f"Last element using negative indexing: {last_element}")


# Example 4 - access a range of a elements
beer_and_chips = my_list[2:4]
print(f"Range of elements: {beer_and_chips}")

dont_buy_coca_cola = my_list[:4]
print(f"All elements up until index 4: {dont_buy_coca_cola}")


# Example 5 - check if an element is in list
if "beer" in my_list:
  print("Beer is awesome!")


# Example 6 - changing an element in the list
my_list[4] = "wine"
print(f"Changing element at index 4: {my_list}")


# Example 7 - appending an element to the list
my_list.append("oranges")
print(f"Appending to the list: {my_list}")


# Example 8 - inserting an element
my_list.insert(1, "cheese")
print(f"Inserting an element at index 1: {my_list}")


# Example 9 - looping through a list
for el in my_list:
  print(el)