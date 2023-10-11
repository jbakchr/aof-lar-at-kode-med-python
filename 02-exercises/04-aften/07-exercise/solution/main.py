"""
EXERCISE

In this exercise you are to try to continuously add 3 elements to a set which should not / cannot include duplicates

In order to complete this exercise you should therefore do the following:
- 1) Create a variable assigned a list with 3 string - two of them being duplicates
- 2) Create a variable assigned an empty set (use the constructor function for this)
- 3) Loop through the list variable and add each element from the list to the set
- 4) Lastly print the set
"""

groceries = ["apples", "bananas", "apples"]
new_shopping_list = set()

for item in groceries:
  new_shopping_list.add(item)

print(new_shopping_list)