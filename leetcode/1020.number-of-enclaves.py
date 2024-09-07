#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # https://youtu.be/gf0zsh1FIgE?si=1kxxFf2d0AdOsCyO
        m, n = len(grid), len(grid[0])
        visited = set()
        land, boarder = 0, 0

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or not grid[i][j] or (i, j) in visited:
                return 0
            visited.add((i, j))
            res = 1
            direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for v, h in direct:
                res += dfs(i + v, j + h)
            return res

        for i in range(m):
            for j in range(n):
                land += grid[i][j]
                if grid[i][j] and (i, j) not in visited and (i in [0, m - 1] or j in [0, n - 1]):
                    boarder += dfs(i, j)
        return land - boarder
# @lc code=end
