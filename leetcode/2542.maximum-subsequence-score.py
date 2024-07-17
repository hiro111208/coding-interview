#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=ax1DKi5lJwk
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        min_heap = []
        n1_sum = 0
        score = 0

        for n1, n2 in pairs:
            n1_sum += n1
            heapq.heappush(min_heap, n1)

            if len(min_heap) > k:
                n1_pop = heapq.heappop(min_heap)
                n1_sum -= n1_pop

            if len(min_heap) == k:
                score = max(score, n1_sum * n2)
        return score
# @lc code=end
