def profit_margin(cost_price, sales_price):
    profit = 0.0
    profit = (cost_price - sales_price) / sales_price
    profit = round((profit*100), 1)
    if profit == 0:
        profit = abs(profit)
    else:
        profit = profit*-1
    return str(profit)+"%"

print(profit_margin(33, 84))