#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # https://www.youtube.com/watch?v=hfUxjdjVQN4
        MOD = 10 ** 9 + 7
        # cache = dict()  # (n, target) -> count

        # def count(n, target):
        #     if n == 0:
        #         return 1 if target == 0 else 0
        #     if (n, target) in cache:
        #         return cache[(n, target)]
        #     res = 0
        #     for val in range(1, k + 1):
        #         res = (res + count(n - 1, target - val)) % MOD
        #     cache[(n, target)] = res
        #     return res
        # return count(n, target)

        # https://medium.com/tech-life-fun/leet-code-1155-number-of-dice-rolls-with-target-sum-graphical-explained-python3-solution-224f8c0af23
        dp = [0] * (target + 1)
        dp[0] = 1
        for dice in range(1, n + 1):
            next_dp = [0] * (target + 1)
            for i in range(dice, min(dice * k, target)+1):
                if i - k < 0:
                    next_dp[i] += sum(dp[:i])
                else:
                    next_dp[i] += sum(dp[i - k:i])
            dp = next_dp
        return dp[target] % MOD


# @lc code=end
