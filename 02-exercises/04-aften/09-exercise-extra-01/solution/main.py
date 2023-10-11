"""
SOLUTION TO EXTRA EXERCISE

In this exercise you are to create a function that'l check whether your
shopping list contains a "beer" element.

If an element in your shopping list contains a "beer" element then you 
should just remind yourself not to buy so much alcohol by printing a kind
of "Note to self" sentence to the terminal.

Else - meaning if an element is not "beer" - then you should appende this 
element to a new list within the function

Lastly the function should return the new list without "beer" elements.

So, to complete this exercise do the following:
- 1)  Create a list with some strings of stuff to buy (for example "milk", "beer", cheese - whatever)
- 2)  Create a function that takes in a list and that:
        - 2.1) Creates a new variable with an empty list
        - 2.2) Loops over the provided list and checks it for "beer" using an if/else statement and
               adds the element to the new list if it is not "beer"
        - 2.3) Returns the new list without "beer" elements
- 3) Print the cleaned list returned from the function if you'd like
"""

def shopping_list_shortner(grocery_list):
  new_list = []

  for el in grocery_list:
    if el == "beer":
      print("Note to self: Stop buying som much alcohol ..")
    else:
      new_list.append(el)
  
  return new_list


shopping_list = ["apple", "banana", "beer", "pears"]

new_list = shopping_list_shortner(shopping_list)
print(f"Hey honey, I'm removed beers from our shopping list: {new_list}")