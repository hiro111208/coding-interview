#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            # convert into binary
            # エラトステネス762
# @lc code=end

