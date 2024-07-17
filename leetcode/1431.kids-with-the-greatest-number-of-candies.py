#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

# @lc code=end
