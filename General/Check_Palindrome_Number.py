num=404 # Input number.

t_num=num
rev_num=0
while t_num!=0:
    rev_num*=10
    rev_num+=(t_num%10)
    t_num=t_num//10
print(rev_num==num)
