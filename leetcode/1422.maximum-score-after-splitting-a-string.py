#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        num_1 = s.count("1")
        num_0 = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                num_0 += 1
            else:
                num_1 -= 1
            res = max(res, num_0 + num_1)
        return res

# @lc code=end
