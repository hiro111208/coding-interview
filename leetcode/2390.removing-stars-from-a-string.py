#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        chars = []
        for char in s:
            if char == "*":
                chars.pop()
            else:
                chars.append(char)
        return "".join(chars)

# @lc code=end
