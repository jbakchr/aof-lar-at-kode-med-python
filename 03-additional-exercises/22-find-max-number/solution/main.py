"""
SOLUTION TO ADDITIONAL EXERCISE

Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]

Expected Output:
24
"""

# Solution 1 - The "classic" looping way
def find_max(lst):
    largest_num = lst[0]
    for i in lst[1:]:
        if i > largest_num:
            largest_num = i
    return largest_num

# Solution 2 - The most concise way
def quick_max(lst):
    return max(lst)

x = [4, 6, 8, 24, 12, 2]

print(find_max(x))
print(quick_max(x))
