"""
Usind the "print function with multiple "objects"
"""
print("Hej", "med", "dig", sep="\n")

class Player:
  def __init__(self, name):
    self.name = name

  def print_player(self):
    print(self.name)

august = Player("August")
jonas = Player("Jonas")

for i in range(1, 3):
  print(i)