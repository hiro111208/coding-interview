#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [*rooms[0]]
        while stack:
            key = stack.pop()
            if not key in visited:
                visited.add(key)
                stack += rooms[key]
        return len(rooms) == len(visited)
# @lc code=end
