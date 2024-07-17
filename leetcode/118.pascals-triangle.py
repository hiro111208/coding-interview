#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            tmp = [0] + pascal[i-1] + [0]
            new_row = []
            for j in range(len(tmp)-1):
                new_row.append(tmp[j] + tmp[j+1])
            pascal.append(new_row)
        return pascal


# @lc code=end
