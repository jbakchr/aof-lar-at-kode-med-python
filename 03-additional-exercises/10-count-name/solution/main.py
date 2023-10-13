"""
ADDITIONAL EXERCISE

Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:
txt = "Emma is good developer. Emma is a writer"

Expected Output:
Emma appeared 2 times
"""

def count_name(txt, name):
    return txt.split(" ").count(name)


txt = "Emma is good developer. Emma is a writer"
name = "Emma"

print(f"{name} appeared {count_name(txt, name)} times")