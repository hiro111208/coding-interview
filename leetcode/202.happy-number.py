#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # https://www.youtube.com/watch?v=ljz85bxOYJ0
        def sum_of_squares(num):
            output = 0
            while num:
                output += (num % 10) ** 2
                num //= 10
            return output
        ht = set()
        while n not in ht:
            ht.add(n)
            n = sum_of_squares(n)
            if n == 1:
                return True
        return False
# @lc code=end
