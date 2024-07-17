#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # else:
        #     if nums[0] > nums[1]:
        #         return 0
        #     elif nums[len(nums) - 1] > nums[len(nums) - 2]:
        #         return len(nums) - 1
        #     else:
        #         l, r = 0, len(nums) - 1
        #         while l < r:
        #             mid_i = l + (r - l) // 2
        #             if (nums[mid_i - 1] < nums[mid_i] and nums[mid_i] < nums[mid_i + 1]) or (nums[mid_i - 1] > nums[mid_i] and nums[mid_i] < nums[mid_i + 1]):
        #                 l = mid_i
        #             elif nums[mid_i - 1] > nums[mid_i] and nums[mid_i] > nums[mid_i + 1]:
        #                 r = mid_i
        #             else:
        #                 return mid_i

        # https://www.youtube.com/watch?v=kMzJy9es7Hc
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
# @lc code=end
