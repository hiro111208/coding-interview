#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0
        for n in gain:
            current += n
            highest = max(current, highest)
        return highest
# @lc code=end
