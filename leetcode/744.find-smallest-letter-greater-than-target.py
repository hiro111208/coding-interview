#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for letter in letters:
        #     if target < letter:
        #         return letter
        # return letters[0]
        # https://www.youtube.com/watch?v=uFRTcMsd2Jw
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l < len(letters) else letters[0]
# @lc code=end
