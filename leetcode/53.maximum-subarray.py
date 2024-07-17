#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -10**4
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum

# @lc code=end
