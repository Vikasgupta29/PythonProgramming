def smallest_multiple(target):
  num=target
  m=1
  while True:
    for i in range(2,target):
      if num%i!=0:
        break
    else:
        return num
    m+=1
    num=target*m
