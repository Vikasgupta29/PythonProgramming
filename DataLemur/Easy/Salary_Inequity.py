def min_inequity(salaries, n):
  salaries.sort()
  t_sal=salaries[0:n]
  res=t_sal[-1]-t_sal[0]
  return res
