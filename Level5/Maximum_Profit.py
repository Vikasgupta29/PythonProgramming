"""
Provided with the list of prices.
Find the buy and sell price.
Also, find highest profit or minimum loss.
"""

price_list=[10,8,16,15,18,31] # input price list.

buy_price=price_list[0]
sell_price=price_list[1]
profit=sell_price-buy_price
for i in range(1,len(price_list)):
    if price_list[i]-buy_price>profit:
        sell_price=price_list[i]
        profit=sell_price-buy_price
    if price_list[i]<buy_price:
        buy_price=price_list[i]
buy_price=sell_price-profit
print(f"buy={buy_price},sell={sell_price},profit={profit}")
