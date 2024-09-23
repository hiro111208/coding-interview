#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(seq):
            if len(seq) <= 1:
                return seq

            mid = len(seq) // 2

            left = merge_sort(seq[:mid])
            right = merge_sort(seq[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0

            while (i < len(left)) and (j < len(right)):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            if i < len(left):
                result += left[i:]
            if j < len(right):
                result += right[j:]

            return result

        return merge_sort(nums)

# @lc code=end
