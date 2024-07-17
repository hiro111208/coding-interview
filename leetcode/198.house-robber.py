#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        one_before, two_before = 0, 0
        for num in nums:
            current = max(two_before+num, one_before)
            two_before = one_before
            one_before = current
        return one_before

        # https://www.youtube.com/watch?v=73r3KWiEvyk
        # rob1, rob2 = 0, 0
        # for n in nums:
        #     tmp = max(rob1+n, rob2)
        #     rob1 = rob2
        #     rob2 = tmp
        # return rob2
# @lc code=end
