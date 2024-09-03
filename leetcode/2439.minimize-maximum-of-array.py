#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # https://youtu.be/AeHMvcKuR0Y?si=layhjkvBUyITtHht
        res = total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total / (i + 1)))
        return res

# @lc code=end
