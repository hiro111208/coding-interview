#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        max_counter = 0
        prev = 1 if arr[1] > arr[0] else 0 if arr[1] < arr[0] else -1
        counter = 0 if arr[1] == arr[0] else 1
        for i in range(2, len(arr)):
            if arr[i] > arr[i - 1]:
                if 1 != prev:
                    counter += 1
                    prev = 1
                else:
                    max_counter = max(max_counter, counter)
                    counter = 1
            elif arr[i] < arr[i - 1]:
                if 0 != prev:
                    counter += 1
                    prev = 0
                else:
                    max_counter = max(max_counter, counter)
                    counter = 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0
                prev = -1
        return max(max_counter, counter) + 1
# @lc code=end
