# Iterate over the prices
# Keep track of lowest price
# Keep track of largest difference at each iteration
# Return the largest difference

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def best_day_to_buy_sell_stock(prices):
    lowest_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        elif price - lowest_price > max_profit:
            max_profit = price - lowest_price
    return max_profit


def replay(prices):
    lowest_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        else:
            max_profit = max(max_profit, price-lowest_price)
    return max_profit


if __name__ == "__main__":
    print(best_day_to_buy_sell_stock( [7,1,5,3,6,4]))
    print(best_day_to_buy_sell_stock([7,6,4,3,1]))
    print(replay([7, 1, 5, 3, 6, 4]))
    print(replay([7, 6, 4, 3, 1]))
