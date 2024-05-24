"""
Python Program to return True if there is a Pythagorean triplet. (a**2 + b**2 = c**2)
"""

num_list=[10, 4, 6, 12, 5] # input list.

sq_list=[i**2 for i in num_list]
temp_flag=False
for i in sq_list:
    for j in sq_list:
        if i+j in sq_list:
            temp_flag=True
print(temp_flag)
