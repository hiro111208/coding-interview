#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=OPV49AuP9lQ

        # l, mx = 0, 0
        # for index, num in enumerate(nums):
        #     k -= (1 - num)
        #     if k < 0:
        #         k += (1 - nums[l])
        #         l += 1
        #     mx = max(mx, index-l+1)
        # return mx

        l, r = 0, 0
        while r < len(nums):
            k -= (1-nums[r])
            if k < 0:
                k += (1 - nums[l])
                l += 1
            r += 1
        return r - l

# @lc code=end
