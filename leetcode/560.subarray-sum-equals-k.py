#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=fFVZt-6sgyo
        prefix_sum = {0: 1}
        current_sum = 0
        result = 0
        for num in nums:
            current_sum += num
            diff = current_sum - k
            result += prefix_sum.get(diff, 0)
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return result

# @lc code=end
