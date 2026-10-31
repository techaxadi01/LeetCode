# LeetCode 121: Best Time to Buy and Sell Stock
# Approach: One Pass / Greedy | Time: O(n) | Space: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]  # Lowest buying price seen so far
        max_profit = 0  # Default to 0 if no valid pair exists

        for price in prices:
            # If selling today gives profit, update max profit
            if min_price < price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price  # Found a lower buying price

        return max_profit
