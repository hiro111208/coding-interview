#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = ""
        max_digit = 0  # no contageous possible
        counter = 1
        found = False
        for char in num:
            if char == prev:
                counter += 1
                if counter == 3:
                    max_digit = max(max_digit, int(char))
                    found = True
                    counter = 1
            else:
                counter = 1
                prev = char
        return str(max_digit) * 3 if found else ""

# @lc code=end
