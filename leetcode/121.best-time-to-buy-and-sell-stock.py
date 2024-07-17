#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        least_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < least_price:
                least_price = prices[i]
            else:
                profit = prices[i] - least_price
                max_profit = max(max_profit, profit)
        return max_profit
# @lc code=end
