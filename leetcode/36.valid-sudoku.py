#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # https://youtu.be/TjFXEUCMqI8?si=Ja4u0di4qCjIm3bn
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        return True
# @lc code=end
