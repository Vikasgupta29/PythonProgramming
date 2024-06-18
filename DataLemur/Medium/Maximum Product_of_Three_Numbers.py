def max_three(input):
  input.sort()
  p_prod=input[-1]*input[-2]*input[-3]
  n_prod=input[-1]*input[0]*input[1]
  if p_prod>n_prod:
    return p_prod
  else:
    return n_prod
