"""
Find the count of combinations of coins to make a given amount.
"""

denominations = [1,2,5] # input variety of coins.
amount = 5 # input amount.

sol_list=[0]*(amount+1)
sol_list[0]=1
for i in denominations:
    for j in range(i,amount+1):
        sol_list[j]+=sol_list[j-i]
print(sol_list[-1])
