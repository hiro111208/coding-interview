#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # https://www.youtube.com/watch?v=UuiTKBwPgAo
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res


# @lc code=end
