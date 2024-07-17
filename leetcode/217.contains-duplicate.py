#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # https://www.youtube.com/watch?v=3OamzN90kPg
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        # return len(nums) != len(set(nums))
# @lc code=end
