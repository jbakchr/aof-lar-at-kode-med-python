"""
Examples of function arguments
"""


# Example 1 - function with many arguments
def say_hello(first_name: str, last_name, age, city) -> str:
    return f"Hi, my name is {first_name} {last_name} and I'm {age} years old and live in {city}"


say_hello(49, "Jonas", 41, "Ballerup")


# Example 2 - function with arbitary number of arguments
names = ["John", "Mogens", "Palle", "Jørgen", "Djarnis"]
names2 = ["John", "Mogens", "Palle", "Jørgen", "Djarnis"]


def call_out(*args):
    for name in args:
        print(name)


call_out(names, names2)


# Example 3 - function with keyword arguments
def call_out_my_kids(first_child, second_child):
    print(f"My youngest kid is: {second_child}")


call_out_my_kids(second_child="Edgar", first_child="Milton")

print("Jonas", "Mogens", end="\n\n\n", sep="*****")


# Example 4 - function with arbitary number of keyword arguments
def my_family(**kwargs):
    print("My nearest family is:")
    for k, v in kwargs.items():
        print(f"{k}: {v}")


my_family(mom="Susanne", dad="Bent", brother="Christian", uncle="John")


def recur(num):
    print(num)
    recur(num + 1)


recur(1)
