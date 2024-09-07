#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                res += count
            else:
                count = 0
        return res

# @lc code=end
