#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # https://www.youtube.com/watch?v=ypn0aZ0nrL4
        window = set()  # in the window, the elements inside are all within abs(r-l)<=k
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
        # counter = dict()
        # for i in range(len(nums)):
        #     if nums[i] in counter.keys():
        #         if abs(counter[nums[i]][-1] - i) <= k:
        #             return True
        #         else:
        #             counter[nums[i]].append(i)
        #     else:
        #         counter[nums[i]] = [i]
        # return False

# @lc code=end
