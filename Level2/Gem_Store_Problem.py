"""
ARS Gems Store sells different varieties of gems to its customers.
Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased.
Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
Assume that quantity required by the customer for any gem will always be greater than 0.
Perform case-sensitive comparison wherever applicable.
"""

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for i in range(0,len(reqd_gems)):
        if reqd_gems[i] not in gems_list:
            bill_amount=-1
            break
        else:
            bill_amount+=reqd_quantity[i]*price_list[gems_list.index(reqd_gems[i])]
    if bill_amount>30000:
        bill_amount-=bill_amount*0.05
    return bill_amount

gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']
price_list=[4392, 1342, 8734, 6421]
reqd_gems=['Amber', 'Opal', 'Topaz']
reqd_quantity=[2,1,3]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
