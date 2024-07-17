#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        ht = {}
        l = 0
        for r in range(len(s)):
            if s[r] in ht.keys() and ht[s[r]] >= l:
                l = ht[s[r]] + 1
                ht[s[r]] = r
            else:
                ht[s[r]] = r
                longest = max(r - l + 1, longest)
        return longest

        # https://www.youtube.com/watch?v=wiGpQwVHdE0
        # char_set = set()
        # l, res = 0, 0

        # for r in range(len(s)):
        #     while s[r] in char_set:
        #         char_set.remove(s[l])
        #         l += 1
        #     char_set.add(s[r])
        #     res = max(res, r - l + 1)

        # return res


# @lc code=end
