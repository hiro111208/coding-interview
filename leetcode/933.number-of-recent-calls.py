#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
class RecentCounter:
    # https://walkccc.me/LeetCode/problems/933/#__tabbed_1_3
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
