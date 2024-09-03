#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        partitions = 1
        for char in s:
            if char in chars:
                partitions += 1
                chars = set()
            chars.add(char)
        return partitions
# @lc code=end
