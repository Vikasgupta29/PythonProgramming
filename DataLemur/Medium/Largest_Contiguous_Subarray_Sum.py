def max_subarray_sum(input):
  max_sum=0
  new_sum=0
  
  for i in input:
    new_sum+=i
    
    if new_sum<0:
      new_sum=0
      
    if max_sum<new_sum:
        max_sum=new_sum
        
  return max_sum
