#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = Counter(nums).most_common(k)
        # res = []
        # for num, _ in nums:
        #     res.append(num)
        # return res

        # https://youtu.be/YPTqKIgVk-k?si=yMCwQAryd7h1EQ0M
        freq = [[] for i in range(len(nums) + 1)]
        counter = dict()

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
# @lc code=end
