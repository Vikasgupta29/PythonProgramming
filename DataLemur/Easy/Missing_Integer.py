def missing_int(input: list[int])-> int:
  x=len(input)*(len(input) + 1)//2-sum(input)
  return x
