"""
SOLUTION TO ADDITIONAL EXERCISE

Reverse a given integer number

Given:
76542

Expected output:
24567
"""


def reverse_number(num):
    rev_num = str(num)[::-1]
    return int(rev_num)


print(reverse_number(123))
