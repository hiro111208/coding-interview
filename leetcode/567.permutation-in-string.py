#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window = len(s1)
        # ht = dict()
        # for char in s1:
        #     ht[char] = 1 + ht.get(char, 0)
        # i = 0
        # while i < len(s2):
        #     if s2[i] in ht and i <= len(s2) - window:
        #         tmp = dict()
        #         valid = True
        #         for j in range(i, window + i):
        #             tmp[s2[j]] = 1 + tmp.get(s2[j], 0)
        #             if s2[j] not in ht or tmp[s2[j]] > ht[s2[j]]:
        #                 valid = False
        #                 break
        #         if valid:
        #             return True
        #     i += 1
        # return False

        # https://youtu.be/UbyhOgBN834?si=fXpg2kUgFSLRvjwv
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
# @lc code=end
