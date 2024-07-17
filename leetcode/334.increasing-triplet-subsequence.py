#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # https://medium.com/@hamnaqaseem/leetcode-334-increasing-triplet-subsequence-python-solution-1b0f36ddd40
        i, j = 2**31 - 1, 2**31 - 1
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False

# @lc code=end
