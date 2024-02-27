"""
Exercise 6

Loop through a list of numbers from 1 to 10 only printing the numbers not divisable by 3

* HINT * use the "continue" keyword
"""
for i in range(1, 11):
  if i % 3 == 0:
    continue
  print(i)
