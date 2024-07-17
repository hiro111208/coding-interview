#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # https://www.youtube.com/watch?v=Uei1fwDoyKk

        # adj = collections.defaultdict(list)  # Map a -> list of [b, a/b]
        # for i, eq in enumerate(equations):
        #     a, b = eq
        #     adj[a].append([b, values[i]])
        #     adj[b].append([a, 1/values[i]])

        # def bfs(src, target):
        #     if src not in adj or target not in adj:
        #         return -1
        #     q, visited = deque(), set()
        #     q.append([src, 1])
        #     visited.add(src)
        #     while q:
        #         n, w = q.popleft()
        #         if n == target:
        #             return w
        #         for nei, weight in adj[n]:
        #             q.append([nei, w * weight])
        #             visited.add(nei)
        #     return -1
        # return [bfs(q[0], q[1]) for q in queries]

        # https://walkccc.me/LeetCode/problems/399/
        ans = []
        # graph[A][B] := A / B
        graph = collections.defaultdict(dict)

        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        def devide(A: str, C: str, seen: Set[str]) -> float:
            """Returns A / C."""
            if A == C:
                return 1.0

            seen.add(A)

            # value := A / B
            for B, value in graph[A].items():
                if B in seen:
                    continue
                res = devide(B, C, seen)  # B / C
                if res > 0:  # valid result
                    return value * res  # (A / B) * (B / C) = A / C

            return -1.0  # invalid result

        for A, C in queries:
            if A not in graph or C not in graph:
                ans.append(-1.0)
            else:
                ans.append(devide(A, C, set()))

        return ans

# @lc code=end
