# Compare adjacent day prices
# If the next day price is greater buy and sell next day
# loop until n-1 times

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

def buy_sell_stock_multiple_times(prices):
    total_profit = 0
    for day in range(len(prices) - 1):
        if prices[day+1] > prices[day]:
            total_profit += prices[day+1] - prices[day]
    return total_profit


def replay(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total_profit +=  prices[i] - prices[i-1]
    return total_profit



if __name__ == "__main__":
    print(buy_sell_stock_multiple_times([7,1,5,3,6,4]))
    print(buy_sell_stock_multiple_times([1,2,3,4,5]))
    print(buy_sell_stock_multiple_times([7,6,4,3,1]))
    print(replay([7,1,5,3,6,4]))
    print(replay([1,2,3,4,5]))
    print(replay([7,6,4,3,1]))
