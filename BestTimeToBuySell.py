def best_time_buy_sell(prices):
    profit = 0
    l = 0
    r = 1
    while r < len(prices):
        if prices[r] > prices[l]:
            temp = prices[r] - prices[l]
            profit = max(profit, temp)
        else:
            l = r

        r += 1
    return profit




print(best_time_buy_sell([7,1,5,3,6,4]))
print("==================================")
print(best_time_buy_sell([7,6,4,3,1]))
print("==================================")
print(best_time_buy_sell([2,1,2,0,1]))
print("==================================")
print(best_time_buy_sell([2,1,2,0,1,2]))
