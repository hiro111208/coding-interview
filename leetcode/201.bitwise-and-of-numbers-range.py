#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # https://www.youtube.com/watch?v=R3T0olAhUq0
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i

# @lc code=end
