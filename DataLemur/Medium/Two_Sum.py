def two_sum(input: list[int], target: int) -> list[int]:
  for i in input:
    if target-i in input and input.index(i)!=input.index(target-i):
      return [input.index(i),input.index(target-i)]
  return [-1, -1]
