#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # https://youtu.be/gqXU1UyA8pk?si=vZuREoQOmDJKAggl
        ht = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            ht[s[r]] = 1 + ht.get(s[r], 0)
            maxf = max(maxf, ht[s[r]])
            while (r - l + 1) - maxf > k:
                ht[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
# @lc code=end
