# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Keep track of min price seen so far
# calculate difference at every iteration with the min price and register the largest difference
# Return the largest difference

def best_time_to_buy_and_sell_stock(prices):
    lowest_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        max_profit = max(max_profit, price - lowest_price)
    return max_profit


if __name__ == "__main__":
    print(best_time_to_buy_and_sell_stock([7,6,4,3,1]))
    print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4]))
