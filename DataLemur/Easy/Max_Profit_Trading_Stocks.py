def max_subarray_sum(prices):
  buy_price=prices[0]
  sell_price=prices[1]
  profit=sell_price-buy_price
  for price in prices:
    if price-buy_price>profit:
      profit=price-buy_price
      sell_price=price
    if price<buy_price:
      buy_price=price
  if profit<0:
    return 0
  return profit
