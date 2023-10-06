"""
ADDITIONAL EXERCISE

In this exercixe you'll create the classic game of 'Rock', 'Paper', 'Scissor'.

To complete such an exercise you'll need to know about the following:
- import and use of the random module
- lists
- input function
- if/elif/else
- both the "and" operator and the "or" operator
"""

import random

OPTIONS = ["rock", "paper", "scissor"]

pc_hand = random.choice(OPTIONS)
user_hand = input("Type 'rock', 'paper' or 'scissor' to select your hand: ")

if (user_hand == "rock" and pc_hand == "scissor") or (user_hand == "paper" and pc_hand == "rock"):
  print("You win!")
elif (user_hand == "rock" and pc_hand == "paper") or (user_hand == "paper" and pc_hand == "scissor"):
  print("You loose ..")
else:
  print("It a draw ..")