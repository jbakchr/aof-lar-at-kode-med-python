# str (i.e. "string" - da: "tekststreng")
my_name = "Jonas"
print(my_name)

# int (i.e. "integer" - da: "heltal")
my_age = "41"
print(int(my_age) * 2)
print(my_age)

# float (da: "decimaltal")
my_bank_acount = 190342782332.3278236732
print(my_bank_acount)

# list (da: "liste")
monty_phyton_characters = ["King Arthur", "Sir Lancelot", "Knights who say 'Ni!'"]
print(monty_phyton_characters)
for char in monty_phyton_characters:
  print(char)

# tuple (da: "tupel")
my_tuple = ("Jonas", 41)
print(my_tuple)

# range
one_to_ten = range(10)
print(one_to_ten)

for i in range(1, 11):
  print(i)

for i in "Jonas":
  print(i)

# dict (da: "ordbog")
my_dict = {"name": "Jonas", "age": 41}
print(my_dict)

# set (da: "sæt")
my_set = {"apple", "banana", "cherry"}
print(my_set)

# boolean (da: "boolesk")
am_i_funny = True
print(am_i_funny)

if False:
  print("hurra!")


# None (placeholder for nothing)
the_abyss_consist_of = None
print(the_abyss_consist_of)