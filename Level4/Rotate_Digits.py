num=123456789 # Input number.
rotate=-9 # Input Rotations. Positive for right and negative for left.

t_num=str(num)
if rotate>len(t_num):
    rotate=abs(len(t_num)-rotate)
elif rotate<(-len(t_num)):
    rotate=len(t_num)+rotate
new_num=int(t_num[rotate:]+t_num[:rotate])
print(new_num)
