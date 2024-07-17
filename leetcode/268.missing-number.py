#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sorted_nums = sorted(nums)
        # n = len(sorted_nums)
        # for i in range(n):
        #     if i != sorted_nums[i]:
        #         return i
        # return n

        # https://www.youtube.com/watch?v=WnPLSRLSANE
        res = len(nums)

        for i in range(len(nums)):
            res += (i-nums[i])

        return res


# @lc code=end
