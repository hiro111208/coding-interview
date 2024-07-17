#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # https://www.youtube.com/watch?v=XYi2-LPrwm4

        # Initialisation
        dp = [[0 for j in range(len(word2) + 1)]
              for i in range(len(word1) + 1)]
        for i in range(len(word2) - 1, -1, -1):
            dp[len(word1)][i] = dp[len(word1)][i+1] + 1
        for i in range(len(word1) - 1, -1, -1):
            dp[i][len(word2)] = dp[i+1][len(word2)] + 1

        # Actual solution
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
# @lc code=end
