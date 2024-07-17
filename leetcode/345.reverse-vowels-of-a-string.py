#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # https://www.youtube.com/watch?v=94RdOzbXvHM
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if not s[l] in vowels:
                l += 1
            if not s[r] in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

# @lc code=end
