#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # counter = 0
        # visited = set()

        # def dfs(i, j):
        #     stack = [(i, j)]
        #     while stack:
        #         k, l = stack.pop()
        #         visited.add((k, l))
        #         for m in range(k, len(isConnected)):
        #             if not ((k, m) in visited) and isConnected[k][m]:
        #                 stack.append((k, m))
        #         for m in range(l+1):
        #             if not ((m, l) in visited) and isConnected[m][l]:
        #                 stack.append((m, l))
        # i = 0
        # while i < len(isConnected):
        #     j = i
        #     while j < len(isConnected):
        #         if isConnected[i][j] and not (i, j) in visited:
        #             counter += 1
        #             dfs(i, j)
        #             break
        #         j += 1
        #     i += 1
        # return counter

        # https://algo.monster/liteproblems/547
        def dfs(curr_city):
            visited[curr_city] = True
            for adj_city, connected in enumerate(isConnected[curr_city]):
                if not visited[adj_city] and connected:
                    dfs(adj_city)

        counter = 0
        visited = [False] * len(isConnected)

        for city in range(len(isConnected)):
            if not visited[city]:
                counter += 1
                dfs(city)
        return counter


# @lc code=end
