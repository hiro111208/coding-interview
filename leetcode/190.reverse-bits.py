#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # converted = (str(bin(n))[2:])
        # reversed_bit = converted[::-1] + \
        #     "".join(["0" for i in range(32-len(converted))])
        # res = int(reversed_bit, base=2)
        # return res

        # https://www.youtube.com/watch?v=UcoN6UjAI64
        res = 0
        for i in range(32):
            print(i)
            bit = (n >> i) & 1
            print(bin(bit))
            res = res | (bit << (31 - i))
            print(bin(res))
            print()

        return res

# @lc code=end
