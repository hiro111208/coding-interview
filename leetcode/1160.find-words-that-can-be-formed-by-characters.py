#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        ht = dict()
        for char in chars:
            ht[char] = ht.get(char, 0) + 1
        for word in words:
            ht_w = dict()
            valid = True
            for char in word:
                ht_w[char] = ht_w.get(char, 0) + 1
                if char not in ht.keys() or ht_w[char] > ht[char]:
                    valid = False
                    break
            if valid:
                ans += len(word)
        return ans
# @lc code=end
