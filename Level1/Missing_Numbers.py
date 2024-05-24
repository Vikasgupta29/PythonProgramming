num_list=[5, 6, 10, 11, 13] # input list.

miss_list=[]
for i in range(min(num_list),max(num_list)):
    if i not in num_list:
        miss_list.append(i)
print(miss_list)
