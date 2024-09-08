#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # https://youtu.be/K7-mXA0irhY?si=S8PJ_KxvMzRruRqj
        visited = set()
        score = 10 ** 4
        adj = defaultdict(list)  # node -> list of (neighbour, dist)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            nonlocal score
            for nei, dist in adj[i]:
                score = min(score, dist)
                dfs(nei)
        dfs(1)
        return score
# @lc code=end
