#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = set()
        for num in nums1:
            if num not in ht:
                ht.add(num)
        ans = list()
        for num in nums2:
            if num in ht:
                ans.append(num)
                ht.remove(num)
        return ans

# @lc code=end
