#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hm = dict()
        # for string in strs:
        #     key = tuple(sorted([*string]))
        #     if key in hm.keys():
        #         hm[key].append(string)
        #     else:
        #         hm[key] = [string]
        # return hm.values()

        # https://www.youtube.com/watch?v=vzdNOK2oB2E
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

# @lc code=end
