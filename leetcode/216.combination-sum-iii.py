#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(k, n, cur_comb, choices):
            if k == 1 and n in choices:
                res.append(cur_comb+[n])
            else:
                for i in range(len(choices)):
                    if k <= n:
                        backtrack(k-1, n-choices[i],
                                  cur_comb+[choices[i]], choices[i+1:])
        backtrack(k, n, [], [i for i in range(1, 10)])
        return res

# @lc code=end
