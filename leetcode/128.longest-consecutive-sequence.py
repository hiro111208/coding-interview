#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # https://youtu.be/P6RZZMu_maU?si=8bb9vW3OnxINSn5T
        num_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                res = max(res, length)
        return res
# @lc code=end
