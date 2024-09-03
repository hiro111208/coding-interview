#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        res = 0
        for i in range(length):
            res += mat[i][i]
            res += mat[i][length - i - 1]
        if length % 2:
            res -= mat[length // 2][length // 2]
        return res
# @lc code=end
