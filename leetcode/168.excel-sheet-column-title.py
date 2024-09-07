#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map = {i: chr(i+65) for i in range(26)}
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res = map[columnNumber % 26] + res
            columnNumber //= 26
        return res

# @lc code=end
