#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        res = length // 2 + int(length % 2 == 1 and low % 2 == 1)
        return res
# @lc code=end

