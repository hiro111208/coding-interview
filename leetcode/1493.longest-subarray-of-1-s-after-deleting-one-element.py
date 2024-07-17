#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # l = 0
        # res = 0
        # queue = []
        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         l = l if not queue else queue.pop(0) + 1
        #         queue.append(r)
        #     res = max(res, r-l)
        # return res

        # similar to 1004 (<- this is more generalised one)
        l, r = 0, 0
        k = 1
        while r < len(nums):
            k -= (1-nums[r])
            if k < 0:
                k += (1 - nums[l])
                l += 1
            r += 1
        return r - l - 1

# @lc code=end
