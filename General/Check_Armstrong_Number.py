num=407 # Input number.

t_num=num
new_num=0
while t_num!=0:
    new_num+=(t_num%10)**3
    t_num=t_num//10
print(new_num==num)
