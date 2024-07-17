#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lower_cases = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        for i in range(k):
            if s[i] in lower_cases:
                vowel_count += 1
        max_count = vowel_count
        for i in range(k, len(s)):
            if s[i] in lower_cases:
                vowel_count += 1
            if s[i-k] in lower_cases:
                vowel_count -= 1
            max_count = max(max_count, vowel_count)
        return max_count
# @lc code=end
