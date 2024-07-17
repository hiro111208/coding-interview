#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # https://medium.com/@robertsevan/exploring-leetcode-problem-1679-max-number-of-k-sum-pairs-python-167d01c5a027
        res = 0
        ht = dict()
        # for num in nums:
        #     if num in ht.keys():
        #         ht[num] += 1
        #     else:
        #         ht[num] = 1
        # for num in nums:
        #     if num in ht.keys():
        #         other = k - num
        #         ht[num] -= 1
        #         if other in ht.keys() and ht[other] > 0:
        #             ht[other] -= 1
        #             res += 1
        #             if ht[num] == 0:
        #                 del ht[num]
        #             if other in ht.keys() and ht[other] == 0:
        #                 del ht[other]
        #         else:
        #             ht[num] += 1
        for num in nums:
            complement = k - num
            if complement in ht.keys() and ht[complement] > 0:
                res += 1
                ht[complement] -= 1
            else:
                ht[num] = ht.get(num, 0) + 1
        return res

# @lc code=end
