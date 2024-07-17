#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # ht = {i: nums[i] for i in range(len(nums))}
        # for i in range(len(nums)):
        #     del ht[i]
        #     other = target - nums[i]
        #     if other in ht.values():
        #         return [i, list(ht.keys())[list(ht.values()).index(other)]]

        # https://www.youtube.com/watch?v=KLlXCFG5TnA
        prev_map = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map.keys():
                return [prev_map[diff], i]
            else:
                prev_map[num] = i


# @lc code=end
