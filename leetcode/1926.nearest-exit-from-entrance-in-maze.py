#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # https://medium.com/@alessandroamenta1/leetcode-1926-nearest-exit-from-entrance-in-maze-python-e1b01541313c
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            i, j, step = queue.popleft()
            for d in directions:
                next_row = i + d[0]
                next_col = j + d[1]
                if 0 <= next_row < len(maze) and 0 <= next_col < len(maze[0]) and maze[next_row][next_col] == ".":
                    if (next_row == 0 or next_row == len(maze) - 1 or next_col == 0 or next_col == len(maze[0]) - 1):
                        return step + 1
                    maze[next_row][next_col] = "+"
                    queue.append((next_row, next_col, step+1))
        return -1

# @lc code=end
