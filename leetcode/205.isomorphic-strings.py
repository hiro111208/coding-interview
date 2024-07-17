#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # ht = dict()
        # for s_char, t_char in zip(s, t):
        #     if s_char in ht.keys():
        #         if ht[s_char] != t_char:
        #             return False
        #     else:
        #         if t_char in ht.values():
        #             return False
        #         else:
        #             ht[s_char] = t_char
        # return [ht[char] for char in [*s]] == [*t]

        # https://www.youtube.com/watch?v=7yF-U1hLEqQ
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True

# @lc code=end
