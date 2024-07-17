#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # https://www.youtube.com/watch?v=ZGxqqjljpUI
        flowerbed = [0] + flowerbed + [0]
        i = 1
        while i < len(flowerbed) - 1 and n > 0:
            if flowerbed[i] == flowerbed[i-1] and flowerbed[i+1] == flowerbed[i]:
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0
# @lc code=end
