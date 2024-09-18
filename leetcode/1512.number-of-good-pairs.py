#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        ht = dict()
        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        for num in ht.values():
            res += (num * (num - 1)) // 2
        return res
# @lc code=end
