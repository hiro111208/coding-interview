#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # hm = dict()
        # for char in [*s]:
        #     if char in hm.keys():
        #         hm[char] += 1
        #     else:
        #         hm[char] = 1
        # for char in [*t]:
        #     if char not in hm.keys():
        #         return char
        #     else:
        #         hm[char] -= 1
        #         if hm[char] == 0:
        #             del hm[char]

        # https://www.youtube.com/watch?v=oFmv4N4z00c
        count_s, count_t = Counter(s), Counter(t)
        for c in count_t:
            if c not in count_s:
                return c
            if count_s[c] < count_t[c]:
                return c
# @lc code=end
