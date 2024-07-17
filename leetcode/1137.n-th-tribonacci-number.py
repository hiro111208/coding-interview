#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        res = 0
        tmp1 = 1
        tmp2 = 1
        tmp3 = 0
        for i in range(3, n+1):
            res = tmp1 + tmp2 + tmp3
            tmp3 = tmp2
            tmp2 = tmp1
            tmp1 = res

        return res
# @lc code=end
