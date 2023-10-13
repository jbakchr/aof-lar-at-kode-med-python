"""
ADDITIONAL EXERCISE

Print the following pattern:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

for i in range(1, 6):
    txt_print = ""
    for j in range(0, i):
        txt_print += str(i) + " "
    print(txt_print)
