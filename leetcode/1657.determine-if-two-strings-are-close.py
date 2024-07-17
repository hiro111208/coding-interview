#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)

        if count1.keys() != count2.keys():
            return False

        return sorted(count2.values()) == sorted(count1.values())
# @lc code=end
