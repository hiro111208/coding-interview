#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, i = 0, 0
        while l < len(s) and i < len(t):
            if s[l] == t[i]:
                l += 1
            i += 1
        return l == len(s)
# @lc code=end
