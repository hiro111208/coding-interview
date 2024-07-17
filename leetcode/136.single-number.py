#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # chatgpt
        result = 0
        for num in nums:
            result ^= num
        return result

        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         num_set.remove(num)
        #     else:
        #         num_set.add(num)
        # return list(num_set)[0]

# @lc code=end
