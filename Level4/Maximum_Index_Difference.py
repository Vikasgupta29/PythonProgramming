"""
Find the maximum value for (j–i) in a list such that list[j] > list[i].
"""

num_list = [20,70,40,50,12,38,98] # input list of numbers.

max_diff=0
for i in range(0,len(num_list)):
    j=len(num_list)-1
    while j>i:
        if num_list[j]>num_list[i] and max_diff<(j-i):
            max_diff=j-i
        j-=1
print(f"maximum_difference={max_diff}")
