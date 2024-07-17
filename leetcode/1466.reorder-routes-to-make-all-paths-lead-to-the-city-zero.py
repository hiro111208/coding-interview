#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=m17yOR5_PpI
        changes = 0
        neighbours = defaultdict(set)
        for left, right in connections:
            neighbours[left].add(right)
            neighbours[right].add(left)
        visited = {0}
        edges = {(a, b) for a, b in connections}

        def dfs(city):
            nonlocal changes, neighbours, visited, edges
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if not (neighbour, city) in edges:
                    changes += 1
                visited.add(neighbour)
                dfs(neighbour)
        dfs(0)
        return changes
# @lc code=end
