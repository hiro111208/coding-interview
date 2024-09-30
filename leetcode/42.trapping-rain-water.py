#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # https://youtu.be/ZI2z5pq0TqA?si=gNRDaXaTuUuOJkrj
        l, r = 0, len(height) - 1
        area = 0
        left_elevation, right_elevation = height[0], height[r]
        while l < r:
            if left_elevation < right_elevation:
                l += 1
                left_elevation = max(left_elevation, height[l])
                area += max(left_elevation - height[l], 0)
            else:
                r -= 1
                right_elevation = max(right_elevation, height[r])
                area += max(right_elevation - height[r], 0)
        return area
# @lc code=end
