#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=fISIuAFRM2s
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            peri = dfs(i, j+1)
            peri += dfs(i+1, j)
            peri += dfs(i, j-1)
            peri += dfs(i-1, j)
            return peri

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

# @lc code=end
