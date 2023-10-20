"""
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected output:
{'name': 'Kelly', 'salary': 8000}
"""


def extract_keys(sample: dict, keys: list) -> dict:
    extracted_dict = {}
    for key, value in sample.items():
        if key in keys:
            extracted_dict.update({key: value})
    return extracted_dict


sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

print(extract_keys(sample_dict, keys))
