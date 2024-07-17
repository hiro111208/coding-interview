#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        # if x == 1:
        #     return 1
        # while left <= right:
        #     if (right - left) == 1 and (right * right > x) and (left * left < x):
        #         return int(left)
        #     else:
        #         middle = (left + right) // 2
        #         if middle * middle == x:
        #             return middle
        #         if middle * middle > x:
        #             right = middle
        #         else:
        #             left = middle

        # https://www.youtube.com/watch?v=zdMhGxRWutQ
        result = 0
        while left <= right:
            middle = left + (right - left) // 2

            if middle ** 2 > x:
                right = middle - 1
            elif middle ** 2 < x:
                left = middle + 1
                result = middle
            else:
                return middle
        return result

# @lc code=end
