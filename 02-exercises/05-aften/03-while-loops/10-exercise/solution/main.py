"""
Solution to exercise 10

Create a while loop that'll print the even numbers from 2 to 10 but breaks
if the number is 8
"""
num = 2
while num <= 10:
  if num == 8:
    break
  print(num)
  num += 2