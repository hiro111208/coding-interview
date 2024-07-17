#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums

        # https://www.youtube.com/watch?v=2pndAmo_sMA
        self.prefix = []
        curr = 0
        for num in nums:
            curr += num
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        # return sum([self.nums[i] for i in range(left, right+1)])
        # https://www.youtube.com/watch?v=2pndAmo_sMA
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
