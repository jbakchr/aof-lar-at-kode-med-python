"""
Exercise 10

Create a while loop that'll print the even numbers from 2 to 10 but breaks
if the number is 8
"""
i = 2
while i <= 10:
  if i == 8:
    break
  print(i)
  i += 2