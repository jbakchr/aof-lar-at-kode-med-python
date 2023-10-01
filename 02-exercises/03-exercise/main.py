# import random module
import random

# Generate random number between 1 and 10 for user to guess
r = random.randint(1, 10)

# Make user choode a number between 1 and 10 and type cast it to an integer since prompts will be in text format
user_number = int(input("Guess the number: "))
guesses = 1

while r != user_number and guesses < 3:
  print("Incorrect guees ..")
  
  
  user_number = input("Try again: ")

  guesses += 1
  print(guesses)

if r == user_number:
  print("You gueesed the correct number in " + str(guesses) + " tries")
else:
  print("You didn't succeed in guessing the correct number " + str(r))