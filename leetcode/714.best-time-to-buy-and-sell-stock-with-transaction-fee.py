#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # https://algo.monster/liteproblems/714
        # https://medium.com/@_monitsharma/daily-leetcode-problems-problem-714-best-time-to-buy-and-sell-stock-with-transaction-fee-17cec07e368a
        sell = 0
        hold = -math.inf

        for price in prices:
            sell = max(sell, hold + price)
            hold = max(hold, sell - price - fee)

        return sell
# @lc code=end
