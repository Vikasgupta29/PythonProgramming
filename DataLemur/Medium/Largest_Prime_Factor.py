def largest_prime_factor(target):
  i=2
  p_factor=[]
  while target>1 and i<=target:
    if target%i==0:
      p_factor.append(i)
      target/=i
    i+=1
  return max(p_factor)
