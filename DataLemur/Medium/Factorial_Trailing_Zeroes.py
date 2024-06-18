def trailing_zeroes(n):
  trail=0
  fact=1
  while n>1:
    fact*=n
    n-=1
  while fact%10==0:
    trail+=1
    fact=fact//10
  return trail
