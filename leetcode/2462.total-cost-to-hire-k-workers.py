#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # https://walkccc.me/LeetCode/problems/2462/#__tabbed_1_3
        total_cost = 0
        i, j = 0, len(costs) - 1
        first, last = [], []
        for _ in range(k):
            while len(first) < candidates and i <= j:
                heapq.heappush(first, costs[i])
                i += 1
            while len(last) < candidates and i <= j:
                heapq.heappush(last, costs[j])
                j -= 1
            if not first:
                total_cost += heapq.heappop(last)
            elif not last:
                total_cost += heapq.heappop(first)
            elif first[0] <= last[0]:
                total_cost += heapq.heappop(first)
            else:
                total_cost += heapq.heappop(last)
        return total_cost

# @lc code=end
