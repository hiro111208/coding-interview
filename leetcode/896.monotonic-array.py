#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] < nums[0]:
            nums.reverse()
        i = 1
        while i < len(nums):
            if not nums[i-1] <= nums[i]:
                return False
            i += 1
        return True
    # @lc code=end
