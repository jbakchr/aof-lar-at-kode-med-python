"""
SOLUTION TO ADDITIONAL EXERCISE

Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected output:
["Mike", "Emma", "Kelly", "Brad"]
"""


def remove_empty_strings(lst: list) -> list:
    cleaned_list = []
    for el in lst:
        if el != "":
            cleaned_list.append(el)
    return cleaned_list


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print(remove_empty_strings(list1))
