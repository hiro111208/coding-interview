#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary = bin(n)
        # count = 0
        # for char in (str(binary)[2:]):
        #     if char == '1':
        #         count += 1
        # return count

        # https://www.youtube.com/watch?v=5Km3utixwZs
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

# @lc code=end
