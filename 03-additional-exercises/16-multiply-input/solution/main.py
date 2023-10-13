"""
SOLUTION TO ADDITIONAL EXERCISE

Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication
"""

user_input = input("Give two numbers: ")

numbers = []

for num in user_input.split(" "):
  numbers.append(int(num))

print(numbers[0] * numbers[1])