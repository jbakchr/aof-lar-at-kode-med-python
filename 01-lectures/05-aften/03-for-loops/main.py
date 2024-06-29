"""
Examples of for loops
"""

# EXAMPLE 1 - RANGE LOOPS

# range with only "stop" value
for i in range(11):
    print(f"Num is: {i}")

# range with "start" and "stop" value
for i in range(1, 10):
    print(f"Num is: {i}")


# range with "start", "stop" and "step" value
for i in range(1, 11, 4):
    print(f"Num is: {i}")


# EXAMPLE 2 - FOR LOOPS
fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)


for x in fruits:
    if x == "banana":
        break
    print(x)


for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass
