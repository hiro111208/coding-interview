#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=7pnhv842keE
        # Boyer Moore algorithm
        result, count = 0, 0
        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count += 1
            else:
                count -= 1
        return result

        # counter = dict()
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1
        # return max(counter, key=counter.get)

# @lc code=end
