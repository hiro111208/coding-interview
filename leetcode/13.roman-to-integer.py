#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        specials = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        if len(s) == 1:
            return converter[s[0]]
        res = 0
        i = 0
        while i < len(s) - 1:
            if converter[s[i]] < converter[s[i+1]]:
                res += specials[s[i] + s[i+1]]
                i += 2
            else:
                res += converter[s[i]]
                i += 1
        last = 0
        if i == len(s) - 1:
            last = converter[s[len(s) - 1]]
        return res + last
    # https://www.youtube.com/watch?v=3jdxYj3DD98
# @lc code=end
