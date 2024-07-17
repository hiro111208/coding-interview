#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        minutes = 0
        prev_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            i, j, elapsed = queue.popleft()
            if elapsed != prev_time:
                minutes += 1
                prev_time = elapsed
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                queue.append((i-1, j, elapsed+1))
                grid[i-1][j] = 2
                visited.add((i-1, j))
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                queue.append((i+1, j, elapsed+1))
                grid[i+1][j] = 2
                visited.add((i+1, j))
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                queue.append((i, j-1, elapsed+1))
                grid[i][j-1] = 2
                visited.add((i, j-1))
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                queue.append((i, j+1, elapsed+1))
                grid[i][j+1] = 2
                visited.add((i, j+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes
        # https://www.youtube.com/watch?v=y704fEOx0s0


# @lc code=end
