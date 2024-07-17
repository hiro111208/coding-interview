#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ht = dict()
        for num in arr:
            ht[num] = ht.get(num, 0) + 1
        return len(set(arr)) == len(set(ht.values()))

# @lc code=end
