#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=bNvIQI2wAjk
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans

# @lc code=end
