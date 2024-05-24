"""
Write a python program to check whether a list of integer values contains same number in adjacent position.
Display the count of such adjacent occurrences
"""

def get_count(num_list):
    count=0
    for i in range(1,len(num_list)):
        if num_list[i]==num_list[i-1]:
            count+=1
    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
