"""
Examples of if, elif, else statements
"""

# Example 1 - simple if check that evaluates to True
x = 20
y = 10

if x > y:
  print("OMG!! x is greater than y ..")


# Example 2 - if statement that won't get executed
if x <= y:
  print("Oopsii .. this code won't get executed ..")


# Example 3 - Multiple if checks
z = 15

if x > y:
  print("Whoa .. part 1")

if x > z:
  print("Whoa .. part 2")


# Example 4 - if and elif check
if "Jonas" is "God":
  print("Damn ..")
elif "Guido is God":
  print("He is!?!?")


# Example 5 - if and multiple elif checks
if 10 == 15:
  print("Uuhhmmm .. m'kay ..")
elif 10 == 12:
  print("This can't be true .. !")
elif 10 == 10:
  print("That's what I thought .. happiness restored!")


# Example 6 - if and else check
if "Jonas" is "God":
  print("I knew it!")
else:
  print("No way! Guido is GOD!")


# Example 7 - using all control structures, i.e. if, elif and else
if 10 == 12:
  print("That's not true!")
elif 10 == 11:
  print("Yo .. 10 is NOT equal to 11!")
else:
  print("10 is 10 .. like True is True .. mind blown!")