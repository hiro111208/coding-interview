#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [char for char in s.split(" ") if not char == ""]
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)
# @lc code=end
#
