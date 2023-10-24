"""
Exercise 15

Given the below two list of teams, create a function that takes in an arbitary numbers
of arguments and print each team
"""

def say_names(*args):
  for i in args:
    print(i)

team1 = ["Jonas", "Mogens"]
team2 = ["Palle", "Jørgen"]

say_names(team1, team2)