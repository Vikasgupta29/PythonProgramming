num=10 # number of output in fibonacci series.

n1=0
n2=1
if num<=0:
    print("Invalid")
elif num==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(2,num):
        n1,n2=n2,n1+n2
        print(n2)
