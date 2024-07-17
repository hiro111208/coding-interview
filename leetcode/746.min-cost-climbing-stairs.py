#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_before = cost[1]
        two_before = cost[0]
        for i in range(2, len(cost)):
            current = min(one_before+cost[i], two_before+cost[i])
            two_before = one_before
            one_before = current
        return min(one_before, two_before)

# @lc code=end
