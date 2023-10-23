"""
Recap from lecture 4

Quick recap of:
- 1) Operators
- 2) Data structures
"""

# RECAP 1 - OPERATORS

# Arithmetic operators (some of them ..)
ex1 = 20 + 10
ex2 = 20 - 10
ex3 = 20 * 10
ex4 = 20 / 10


# Assignment operators (some of them ..)
ex5 = 10

ex5 += 20   # sum = 30
ex5 -= 10   # sum = 20
ex5 *= 2    # sum = 40
ex5 /= 4    # sum = 10


# Comparison operators (==, !=, >, <, >=, <=)
ex6 = 4 == 4  # True
ex7 = 4 != 4  # False
ex8 = 5 > 4   # True
ex9 = 5 < 4   # False


# Logical operators ("and", "or", "not")
ex10 = 4 == 4 and 4 != 5  # True
ex11 = 4 == 4 or 4 != 4   # True
ex12 = not 4 == 4         # False


# RECAP 2 - DATA STRUCTURES

# "list" data structure (and some operations on it ..)
my_list = ["apples", "bananas", "beer", "pears", 42, True, ["The Beatles", "Madonna", "Elvis"]]

# Acessing a list
ex13 = my_list[0]
ex14 = my_list[-1]
ex15 = my_list[1:3]

# Changing a list
my_list[1] = "milk"
my_list.append("wine")
my_list.insert(1, "oranges")


# "tuple" data structure (and some operations on it ..)
my_tuple = ("apple", "banana", "beer", "pears", "chips", "cheese")

# Accessing a tuple
ex16 = my_tuple[0]
ex17 = my_tuple[-1]
ex17 = my_tuple[2:4]

# Unpacking a tuple
point = (55, 12)
lat, long = point

