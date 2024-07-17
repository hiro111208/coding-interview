#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ht = dict()
        for column in grid:
            if tuple(column) in ht.keys():
                ht[tuple(column)][0] += 1
            else:
                ht[tuple(column)] = [1, 0]

        for i in range(len(grid)):
            row = []
            for j in range(len(grid)):
                row.append(grid[j][i])
            if tuple(row) in ht.keys():
                ht[tuple(row)][1] += 1
            else:
                ht[tuple(row)] = [0, 1]
        return sum([pair[0] * pair[1] for pair in ht.values()])

# @lc code=end
