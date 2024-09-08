#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                continue
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1

        # https://youtu.be/QC4c9fyr8As?si=WF_uneDfl58UaY8R
        # l = 0
        # for r in range(len(nums)):
        #     if nums[r] % 2 == 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        return nums

# @lc code=end
