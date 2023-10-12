"""
EXTRA EXERCISE

In order for you to get even more eperience with Python topics that we haven't
fully gone through yet I've created this exercise in order to "push" your
understanding even further.

The exercise will of course be based on our current topic of logical operators.

But given the fact that you have already been exposed to both "if" statements,
functions and a tiny bit about the "return" keyword this exercise will challenge
you to gain even more experience with these topics - and be exposed to an "else"
part of an if statement which is very often used in conjuction with this.

In the code below I have provide a function that takes in two parameters/arguments
and from there checks if BOTH of two expressions are true. If so, the function returns
True. Else it'll return False.

Your job in this exercise is therefore to do the following:
- 1)  Create a function that replicates my function but that uses an "or" operator in
      the "if" statement part of it
- 2)  Create another function that does the same but which uses the "not" operator
- 3)  Call your functions the way if done below

PS. ASK IF YOU NEED HELP!!!
"""

def and_function(num1, num2):
  if num1 == 5 and num2 != 10:
    return True
  else:
    return False

# define your function with the "or" operator below this line
def or_function(num1, num2):
  return num1 == 5 or num2 != 10

# define you function with the "not" operator below this line
def not_function(num1, num2):
  return not num1 != num2

# Call your functions like I've called mine below the print statement
print(and_function(5, 5))
print(or_function(5, 5))
print(not_function(5, 5))

