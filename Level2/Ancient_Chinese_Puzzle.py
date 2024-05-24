"""
Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
"""

def solve(heads,legs):
    error_msg="No solution"
    rabbit_count=int(legs/2)-heads
    chicken_count=heads-rabbit_count
    
    if legs%2!=0 or heads>legs/2:
        print(error_msg)
    else:
        print(chicken_count,rabbit_count)

#Provide different values for heads and legs and test your program
solve(38,131)
solve(5,10)
