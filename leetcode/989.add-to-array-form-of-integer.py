#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # https://www.youtube.com/watch?v=eBTZQt1TWfk&t=606s
        num.reverse()
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            carry = num[i] // 10
            num[i] %= 10
            k //= 10
            k += carry
            i += 1
        num.reverse()
        return num

# @lc code=end
