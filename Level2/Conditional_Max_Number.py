"""
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
      a. Sum of the digits of the number is a multiple of 3
      b. Number has only two digits
      c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
"""

def find_max(num1, num2):
    max_num=-1
    num_list=[]
    if num1<num2:
        for i in range(num1,num2+1):
            if i%5==0 and 9<i<100 and ((i%10)+(i//10))%3==0:
                num_list.append(i)
        if len(num_list)>0:
            for j in num_list:
                if j>max_num:
                    max_num=j
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
