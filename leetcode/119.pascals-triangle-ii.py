#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        next_pascal = [1]
        for i in range(rowIndex):
            next_pascal = []
            tmp = [0] + pascal + [0]
            for j in range(1, len(tmp)):
                next_pascal.append(tmp[j-1] + tmp[j])
            pascal = next_pascal
        return next_pascal

# @lc code=end
