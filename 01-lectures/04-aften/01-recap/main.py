"""
Recap from lecture 3

Quick recap of:
- 1) Constructor functions and type casting
- 2) "type" function
- 3) Strings
"""

# RECAP 1

# constructor functions
name = str("Jonas")
age = int(10)
fav_num = int("60")

# type casting
dec_num = float(fav_num)

# ------------------------------------------------------

# RECAP 2

# type function
print(type(name))
print(type(fav_num))

# ------------------------------------------------------

# RECAP 3

# single, double and multiline strings
single_quote = 'Jonas'
double_quote = "Phillipson"
multiline = """First line
Second line
Third line"""

# accessing and slicing strings by bracket notation
txt = "Hello, World!"

print(txt[0:5])   # start index 0 and stop index 5
print(txt[:5])    # only stop index 5
print(txt[7:])    # only start index 7
print(txt[-6:-1]) # negative index from index -6 to -1

# loop through string
for letter in "Hello":
  print(letter)

# get length of string by using the "len" function
print(len("Jonas"))

# check if string contains string
if "J" in "Jonas":
  print("The name 'Jonas' does indeed start with a capital 'J'")

# string methods
print(txt.upper()) # prints string in uppercase
print("  Clean me!   ".strip())
print("Split, Me, Into, A, List".split(", "))

# string concatenation
my_name = "Jonas"
my_age = 41
print("Hello, my name is " + my_name + " and I'm " + str(my_age) + " years old")

# formatting strings
fav_food = "hot dogs"
fav_animal = "okapis"

sentence1 = "I like {} and {}"
sentence2 = "I like {1} and {0}"

print(sentence1.format(fav_food, fav_animal))
print(sentence2.format(fav_food, fav_animal))

f_string = f"I like {fav_food} and {fav_animal}"
print(f_string)