"""
You have x no. of 5 rupee coins and y no. of 1 rupee coins.
You want to purchase an item for amount z.
The shopkeeper wants you to provide exact change.
You want to pay using minimum number of coins.
How many 5 rupee coins and 1 rupee coins will you use?
If exact change is not possible then display -1.
"""

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make-((rupees_to_make//5)*5)
    if five_needed>no_of_five:
        one_needed+=(five_needed-no_of_five)*5
        five_needed=no_of_five
    if one_needed>no_of_one:
        print(-1)
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
make_amount(28,4,5)
