#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # https://youtu.be/X8k48xek8g8?si=WC7qzvEhtZ5y2oQT
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i == ROWS or j == COLS):
                return 0
            if grid[i][j] == 1 or (i, j) in visited:
                return 1
            visited.add((i, j))
            return min(dfs(i, j+1), dfs(i+1, j), dfs(i-1, j), dfs(i, j-1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in visited:
                    res += dfs(i, j)
        return res

# @lc code=end
