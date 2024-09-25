#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # https://youtu.be/gdXkkmzvR3c?si=d9pA4W8V3_ezajjJ
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = min(dfs(i + 1, total),
                                 dfs(i + 1, total + stones[i]))

            return dp[(i, total)]

        dp = {}
        return dfs(0, 0)

# @lc code=end
