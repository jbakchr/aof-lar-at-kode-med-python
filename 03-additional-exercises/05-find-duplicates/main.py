"""
ADDITIONAL EXERCISE

In this exercise you are to create a function that'll return a list of 
duplicates from a list of names. The list of names are already given below.

If the returned list from the function includes duplicate names then it
should print the list of names to the terminal. Else some sentence like
"no duplicates" found should be printed.

To complete the exercise you would have to:
- 1)  Create a "find_duplicates" function that'll return a list of duplicate
      names
- 2)  Create an if/else statement that'll check if the returned list contains
      any duplicate names

* HINT *
- 1)  Within the function it might a good idea to count whether the provided
      list of names has a name that occurs more than once
- 2)  When checking the returned list of duplicate names one might just need
      to check whether its length is greater than zero ;)
"""

def find_duplicates(lst):
  duplicates = []

  for name in names:
      if names.count(name) > 1:
          if name not in duplicates:
              duplicates.append(name)
  
  return duplicates

names = ["Morten", "Jensine", "Preben", "Ulla", "Ulla", "Jensine", "Børge"]

duplicates = find_duplicates(names)

if len(duplicates) > 0:
    print(f"Duplicate names are: {duplicates}")
else:
    print("No duplicates found ..")


