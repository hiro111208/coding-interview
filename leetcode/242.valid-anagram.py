#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht = {}
        for char in s:
            ht[char] = ht.get(char, 0) + 1
        for char in t:
            if char in ht:
                ht[char] -= 1
                if ht[char] == 0:
                    del ht[char]
            else:
                return False
        return not len(ht) > 0
# @lc code=end
