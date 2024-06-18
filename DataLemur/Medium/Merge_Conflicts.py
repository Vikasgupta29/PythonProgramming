def has_merge_conflict(pull_requests)-> bool:
  pull_requests.sort()
  for i in range(1,len(pull_requests)):
    if pull_requests[i-1][1]>=pull_requests[i][0]:
      return True
  return False
