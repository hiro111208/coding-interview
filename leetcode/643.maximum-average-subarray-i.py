#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k]
            max_sum = max(current_sum, max_sum)
        return max_sum/k
    # https://www.youtube.com/watch?v=56TxHMG0qhQ
# @lc code=end
