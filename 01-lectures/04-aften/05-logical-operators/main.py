"""
Examples of logical operators
"""

# Example 1 - "and" operator
ex1 = 4 < 5 and 10 >= 9             # True
ex2 = 4 < 5 and 10 < 9              # False
ex3 = 4 < 5 and 10 >= 9 and 5 != 3  # True


# Example 2 - "or" operator
ex4 = 4 < 5 or 10 < 9 # True
ex5 = "Jonas" == "Jonas" or "Jonas" == "Mogens"

if 4 == 4 or "The meaning of life" == 42:
  print("Only one is true ..")


# Example 3 - "not" operator
ex6 = not True    # False
ex7 = not 5 != 4  # True

if not 5 != 4 and not 5 == 4 or not "Jonas" == "Mogens":
  print("God damn .. are all true?")